#!/usr/bin/env node
/**
 * generate-plugins.mjs
 *
 * Rebuilds plugins/ from the source layer. EVERYTHING under plugins/ is derived
 * and disposable. This script deletes the whole directory and recreates it.
 * Never hand-edit a file under plugins/, it will be overwritten.
 *
 * Source of truth:
 *   .claude-plugin/marketplace.json  plugin metadata and version (one entry per plugin)
 *   .claude-plugin/plugins-map.json  what goes IN each plugin
 *   shared-skills/                   every shippable skill, exactly once
 *   knowledge/                       shared reference docs, pulled in automatically
 *   connectors/                      one MCP server config per file
 *   agents/                          one subagent per file
 *   commands/                        one slash command per file
 *
 * A skill that belongs to two plugins is listed twice in the map and stored once
 * in shared-skills/. That is the whole point.
 *
 * Usage:
 *   node scripts/generate-plugins.mjs            rebuild plugins/
 *   node scripts/generate-plugins.mjs --check    verify plugins/ matches source, exit 1 if stale
 *   node scripts/generate-plugins.mjs --root DIR run against a different repo root
 */

import { readFileSync, writeFileSync, existsSync, rmSync, mkdirSync, readdirSync, statSync } from 'node:fs';
import { join, dirname, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { tmpdir } from 'node:os';

const DESCRIPTION_LIMIT = 1024; // plugin validator rejects the whole plugin above this
const KNOWLEDGE_REF = /knowledge\/([A-Za-z0-9_./-]+\.md)/g;

/**
 * Build junk that must never reach a client. The generator copies from the working
 * tree, not from git, so gitignored files are present on disk and would otherwise
 * be packaged. Anything matched here is skipped.
 */
const JUNK = [/(^|[\\/])__pycache__([\\/]|$)/, /\.pyc$/, /(^|[\\/])\.DS_Store$/, /(^|[\\/])Thumbs\.db$/, /(^|[\\/])\.env$/];
const isJunk = (p) => JUNK.some((re) => re.test(p));

/**
 * Copy a file, forcing LF on anything that is text.
 *
 * This is not cosmetic. core.autocrlf is true on Windows, so a source file with
 * no eol rule is checked out with CRLF. Cowork's YAML frontmatter parser rejects
 * CRLF and silently leaks the whole frontmatter block into the body of the skill.
 * The repo-root .gitattributes is the first defence; this is the second, because
 * the generator reads the working tree rather than git and must be correct even
 * if someone's checkout is not.
 *
 * Binary is detected by a NUL byte in the first 8KB, which is the standard
 * heuristic and avoids maintaining an extension allowlist that will drift.
 */
function copyFileNormalized(from, to) {
  const buf = readFileSync(from);
  mkdirSync(dirname(to), { recursive: true });
  const isBinary = buf.subarray(0, 8192).includes(0);
  writeFileSync(to, isBinary ? buf : Buffer.from(buf.toString('utf8').replace(/\r\n/g, '\n'), 'utf8'));
}

/** Recursive copy that drops build junk and normalizes text line endings. */
function copyClean(from, to) {
  if (statSync(from).isFile()) {
    if (!isJunk(from)) copyFileNormalized(from, to);
    return;
  }
  for (const rel of walk(from)) copyFileNormalized(join(from, rel), join(to, rel));
}

// ---------------------------------------------------------------- args

const argv = process.argv.slice(2);
const CHECK = argv.includes('--check');
const rootFlag = argv.indexOf('--root');
const ROOT = rootFlag !== -1 && argv[rootFlag + 1]
  ? argv[rootFlag + 1]
  : join(dirname(fileURLToPath(import.meta.url)), '..');

const SRC = {
  marketplace: join(ROOT, '.claude-plugin', 'marketplace.json'),
  map: join(ROOT, '.claude-plugin', 'plugins-map.json'),
  skills: join(ROOT, 'shared-skills'),
  knowledge: join(ROOT, 'knowledge'),
  connectors: join(ROOT, 'connectors'),
  agents: join(ROOT, 'agents'),
  commands: join(ROOT, 'commands'),
};

const errors = [];
const warnings = [];
const fail = (msg) => errors.push(msg);
const warn = (msg) => warnings.push(msg);

// ---------------------------------------------------------------- helpers

function readJson(path, label) {
  if (!existsSync(path)) {
    console.error(`Missing ${label}: ${path}`);
    process.exit(1);
  }
  try {
    return JSON.parse(readFileSync(path, 'utf8'));
  } catch (e) {
    console.error(`${label} is not valid JSON: ${e.message}`);
    process.exit(1);
  }
}

function writeJson(path, data) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, JSON.stringify(data, null, 2) + '\n');
}

/** Every file under dir, as paths relative to dir, sorted. */
function walk(dir, base = dir, out = []) {
  if (!existsSync(dir)) return out;
  for (const entry of readdirSync(dir).sort()) {
    const full = join(dir, entry);
    if (isJunk(full)) continue;
    if (statSync(full).isDirectory()) walk(full, base, out);
    else out.push(relative(base, full).split(sep).join('/'));
  }
  return out;
}

/** Frontmatter `description:` of a SKILL.md, or null. Handles folded/literal blocks. */
function skillDescription(skillMd) {
  const raw = readFileSync(skillMd, 'utf8');
  const fm = raw.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!fm) return null;
  const lines = fm[1].split(/\r?\n/);
  const start = lines.findIndex((l) => /^description:\s*/.test(l));
  if (start === -1) return null;
  const first = lines[start].replace(/^description:\s*/, '');
  // Block scalar (| or >): description continues across indented lines.
  if (/^[|>][-+]?\d*\s*$/.test(first.trim())) {
    const body = [];
    for (let i = start + 1; i < lines.length; i++) {
      if (lines[i].trim() !== '' && !/^\s/.test(lines[i])) break;
      body.push(lines[i].trim());
    }
    return body.join(' ').trim();
  }
  return first.trim();
}

/** knowledge/*.md paths referenced by any markdown inside a directory. */
function knowledgeRefs(dir) {
  const found = new Set();
  for (const rel of walk(dir)) {
    if (!rel.endsWith('.md')) continue;
    const text = readFileSync(join(dir, rel), 'utf8');
    for (const m of text.matchAll(KNOWLEDGE_REF)) found.add(m[1]);
  }
  return found;
}

// ---------------------------------------------------------------- build

function build(outRoot) {
  const marketplace = readJson(SRC.marketplace, 'marketplace.json');
  const map = readJson(SRC.map, 'plugins-map.json');

  const metaByName = new Map((marketplace.plugins ?? []).map((p) => [p.name, p]));
  const pluginNames = Object.keys(map.plugins ?? {});

  // --- guards that make the marketplace leak structurally impossible -------
  for (const name of metaByName.keys()) {
    if (!pluginNames.includes(name)) {
      fail(`marketplace.json lists "${name}" but plugins-map.json does not define it. ` +
           `It would ship as an entry pointing at a folder that does not exist.`);
    }
  }
  for (const name of pluginNames) {
    if (!metaByName.has(name)) {
      fail(`plugins-map.json defines "${name}" but marketplace.json has no entry for it. ` +
           `It would be built but never listed.`);
    }
    const meta = metaByName.get(name);
    if (meta && meta.source !== `./plugins/${name}`) {
      fail(`marketplace.json entry "${name}" has source "${meta.source}", expected "./plugins/${name}".`);
    }
  }
  if (errors.length) return null;

  rmSync(outRoot, { recursive: true, force: true });
  const report = [];

  for (const name of pluginNames) {
    const spec = map.plugins[name];
    const meta = metaByName.get(name);
    const dir = join(outRoot, name);

    // --- resolve the skill list (supports deriving a bundle from others) ---
    let skillIds;
    if (spec.includePluginsSkills) {
      const union = new Set();
      for (const other of spec.includePluginsSkills) {
        if (!map.plugins[other]) {
          fail(`"${name}" derives from "${other}", which is not a plugin.`);
          continue;
        }
        for (const s of map.plugins[other].skills ?? []) union.add(s);
      }
      for (const s of spec.skills ?? []) union.add(s);
      skillIds = [...union].sort();
    } else {
      skillIds = spec.skills ?? [];
    }

    // --- plugin.json (version comes from marketplace.json, one source) -----
    const pluginJson = {
      name,
      ...(meta.displayName ? { displayName: meta.displayName } : {}),
      description: meta.description ?? '',
      version: meta.version ?? '0.0.0',
      ...(meta.author ? { author: meta.author } : {}),
      ...(meta.homepage ? { homepage: meta.homepage } : {}),
      ...(meta.repository ? { repository: meta.repository } : {}),
      ...(meta.license ? { license: meta.license } : {}),
      ...(meta.keywords ? { keywords: meta.keywords } : {}),
      ...(meta.category ? { category: meta.category } : {}),
    };

    // --- skills -------------------------------------------------------------
    const wantedKnowledge = new Set(spec.knowledge ?? []);
    for (const id of skillIds) {
      const from = join(SRC.skills, id);
      if (!existsSync(from)) {
        fail(`"${name}" wants skill "${id}" but shared-skills/${id}/ does not exist.`);
        continue;
      }
      if (!existsSync(join(from, 'SKILL.md'))) {
        fail(`shared-skills/${id}/ has no SKILL.md.`);
        continue;
      }
      const desc = skillDescription(join(from, 'SKILL.md'));
      if (desc === null) {
        fail(`shared-skills/${id}/SKILL.md has no frontmatter description.`);
      } else if (desc.length > DESCRIPTION_LIMIT) {
        fail(`shared-skills/${id}/SKILL.md description is ${desc.length} chars, ` +
             `over the ${DESCRIPTION_LIMIT} plugin-validator limit.`);
      }
      copyClean(from, join(dir, 'skills', id));
      for (const ref of knowledgeRefs(from)) wantedKnowledge.add(ref);
    }

    // --- knowledge (auto-detected from skill references, plus explicit) ----
    // Skills reference `knowledge/x.md`. At repo root that resolves to knowledge/x.md.
    // Inside an installed plugin it must resolve under the plugin root, so it is
    // copied to plugins/<name>/knowledge/x.md and the reference keeps working.
    for (const ref of [...wantedKnowledge].sort()) {
      const from = join(SRC.knowledge, ref);
      if (!existsSync(from)) {
        warn(`"${name}": knowledge/${ref} is referenced by a skill but does not exist. ` +
             `Treating it as a placeholder string, not copying.`);
        continue;
      }
      copyFileNormalized(from, join(dir, 'knowledge', ref));
    }

    // --- agents -------------------------------------------------------------
    for (const id of spec.agents ?? []) {
      const from = join(SRC.agents, `${id}.md`);
      if (!existsSync(from)) { fail(`"${name}" wants agent "${id}" but agents/${id}.md does not exist.`); continue; }
      copyFileNormalized(from, join(dir, 'agents', `${id}.md`));
    }

    // --- commands -----------------------------------------------------------
    for (const id of spec.commands ?? []) {
      const from = join(SRC.commands, `${id}.md`);
      if (!existsSync(from)) { fail(`"${name}" wants command "${id}" but commands/${id}.md does not exist.`); continue; }
      copyFileNormalized(from, join(dir, 'commands', `${id}.md`));
    }

    // --- .mcp.json from declared connectors --------------------------------
    const connectors = spec.connectors ?? [];
    if (connectors.length) {
      const servers = {};
      for (const id of connectors) {
        const from = join(SRC.connectors, `${id}.json`);
        if (!existsSync(from)) { fail(`"${name}" wants connector "${id}" but connectors/${id}.json does not exist.`); continue; }
        servers[id] = readJson(from, `connectors/${id}.json`);
      }
      if (Object.keys(servers).length) writeJson(join(dir, '.mcp.json'), servers);
    }

    // --- hooks declared in the map land in plugin.json ---------------------
    if (spec.hooks && Object.keys(spec.hooks).length) {
      const hooks = {};
      for (const [event, entries] of Object.entries(spec.hooks)) {
        const built = [];
        for (const h of entries) {
          const from = join(ROOT, 'hooks', h.file);
          if (!existsSync(from)) { fail(`"${name}" wants hook "${h.file}" but hooks/${h.file} does not exist.`); continue; }
          copyFileNormalized(from, join(dir, 'hooks', h.file));
          built.push({
            type: 'command',
            command: '${CLAUDE_PLUGIN_ROOT}/hooks/' + h.file,
            ...(h.timeout ? { timeout: h.timeout } : {}),
          });
        }
        if (built.length) hooks[event] = [{ matcher: '', hooks: built }];
      }
      if (Object.keys(hooks).length) pluginJson.hooks = hooks;
    }

    // --- verbatim passthrough files (LICENSE, README, .gitattributes) ------
    for (const f of spec.files ?? []) {
      const from = join(ROOT, f);
      if (!existsSync(from)) { fail(`"${name}" wants file "${f}" but ${f} does not exist.`); continue; }
      copyFileNormalized(from, join(dir, f.split('/').pop()));
    }

    writeJson(join(dir, '.claude-plugin', 'plugin.json'), pluginJson);
    report.push({ name, skills: skillIds.length, knowledge: wantedKnowledge.size, connectors: connectors.length });
  }

  // --- builder-only tracing must never reach a client ----------------------
  for (const rel of walk(outRoot)) {
    if (!/\.(md|json|ya?ml|mjs|js|py|sh|ps1)$/.test(rel)) continue;
    if (readFileSync(join(outRoot, rel), 'utf8').includes('DEBUG-TRACE')) {
      fail(`DEBUG-TRACE instrumentation would ship in plugins/${rel}. Remove it.`);
    }
  }

  return report;
}

// ---------------------------------------------------------------- run

const target = join(ROOT, 'plugins');
const outRoot = CHECK ? join(tmpdir(), `aai-plugins-check-${process.pid}`) : target;
const report = build(outRoot);

if (errors.length) {
  if (CHECK) rmSync(outRoot, { recursive: true, force: true });
  console.error('\nGeneration failed:\n');
  for (const e of errors) console.error(`  ${e}`);
  console.error('');
  process.exit(1);
}

for (const w of warnings) console.warn(`  warning: ${w}`);

if (CHECK) {
  const built = walk(outRoot);
  const committed = walk(target);
  const inBuilt = new Set(built);
  const inCommitted = new Set(committed);

  const missing = built.filter((f) => !inCommitted.has(f));
  const extra = committed.filter((f) => !inBuilt.has(f));
  const changed = built.filter(
    (f) => inCommitted.has(f) &&
      !readFileSync(join(outRoot, f)).equals(readFileSync(join(target, f)))
  );

  rmSync(outRoot, { recursive: true, force: true });

  if (missing.length || extra.length || changed.length) {
    console.error('\nplugins/ is out of date with the source layer.\n');
    for (const f of missing) console.error(`  missing from plugins/  ${f}`);
    for (const f of extra) console.error(`  stale in plugins/      ${f}`);
    for (const f of changed) console.error(`  content differs        ${f}`);
    console.error('\nRun: node scripts/generate-plugins.mjs\n');
    process.exit(1);
  }
  console.log('plugins/ matches the source layer.');
} else {
  console.log('');
  for (const r of report) {
    console.log(`  ${r.name}: ${r.skills} skills, ${r.knowledge} knowledge files, ${r.connectors} connectors`);
  }
  console.log('\nplugins/ rebuilt from shared-skills/ and plugins-map.json.\n');
}
