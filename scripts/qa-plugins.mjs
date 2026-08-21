#!/usr/bin/env node
/**
 * qa-plugins.mjs
 *
 * Production-readiness gate for the plugin marketplace. Every check here exists
 * because something actually broke, or would have. Read the `why` on each one
 * before deleting it.
 *
 * BLOCKER = a client gets a broken install. Release must not proceed.
 * WARNING = worth a look, does not stop a release.
 *
 * Usage:
 *   node scripts/qa-plugins.mjs                 full pass against the repo
 *   node scripts/qa-plugins.mjs --root DIR      run against a different root
 *   node scripts/qa-plugins.mjs --ref dev       check committed state of that ref
 *   node scripts/qa-plugins.mjs --no-git        skip every git-dependent check
 *   node scripts/qa-plugins.mjs --json          machine-readable output
 */

import { readFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import { join, dirname, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';

const argv = process.argv.slice(2);
const flag = (n) => { const i = argv.indexOf(n); return i !== -1 && argv[i + 1] ? argv[i + 1] : null; };
const ROOT = flag('--root') ?? join(dirname(fileURLToPath(import.meta.url)), '..');
const REF = flag('--ref') ?? 'HEAD';
const NO_GIT = argv.includes('--no-git');
const JSON_OUT = argv.includes('--json');

const DESCRIPTION_LIMIT = 1024;
const findings = [];
const add = (level, check, message, where) => findings.push({ level, check, message, where });
const blocker = (c, m, w) => add('BLOCKER', c, m, w);
const warning = (c, m, w) => add('WARNING', c, m, w);

// ---------------------------------------------------------------- helpers

function walk(dir, base = dir, out = []) {
  if (!existsSync(dir)) return out;
  for (const e of readdirSync(dir).sort()) {
    const f = join(dir, e);
    if (/(^|[\\/])(__pycache__|node_modules|\.git)([\\/]|$)/.test(f)) continue;
    if (statSync(f).isDirectory()) walk(f, base, out);
    else out.push(relative(base, f).split(sep).join('/'));
  }
  return out;
}

const readJson = (p) => JSON.parse(readFileSync(p, 'utf8'));
const isText = (b) => !b.subarray(0, 8192).includes(0);

function git(args) {
  try {
    return execFileSync('git', args, { cwd: ROOT, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] });
  } catch { return null; }
}
const gitHas = (ref, path) => git(['cat-file', '-e', `${ref}:${path}`]) !== null;

function frontmatter(text) {
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!m) return null;
  const out = {};
  const lines = m[1].split(/\r?\n/);
  for (let i = 0; i < lines.length; i++) {
    const kv = lines[i].match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
    if (!kv) continue;
    let [, k, v] = kv;
    if (/^[|>][-+]?\d*\s*$/.test(v.trim())) {
      const body = [];
      for (let j = i + 1; j < lines.length; j++) {
        if (lines[j].trim() !== '' && !/^\s/.test(lines[j])) break;
        body.push(lines[j].trim()); i = j;
      }
      v = body.join(' ');
    }
    out[k] = v.trim().replace(/^["']|["']$/g, '');
  }
  return out;
}

// ---------------------------------------------------------------- checks

const MP = join(ROOT, '.claude-plugin', 'marketplace.json');
const MAP = join(ROOT, '.claude-plugin', 'plugins-map.json');

if (!existsSync(MP)) { console.error('No .claude-plugin/marketplace.json'); process.exit(2); }
if (!existsSync(MAP)) { console.error('No .claude-plugin/plugins-map.json'); process.exit(2); }

const marketplace = readJson(MP);
const map = readJson(MAP);
const metaByName = new Map((marketplace.plugins ?? []).map((p) => [p.name, p]));
const pluginNames = Object.keys(map.plugins ?? {});
const SHARED = join(ROOT, 'shared-skills');

// --- 1. marketplace and map agree, both directions -------------------------
// why: a marketplace entry with no folder ships a broken listing to every client.
for (const n of metaByName.keys())
  if (!pluginNames.includes(n))
    blocker('manifest-parity', `marketplace.json lists "${n}" but the map does not define it`, '.claude-plugin/marketplace.json');
for (const n of pluginNames) {
  if (!metaByName.has(n))
    blocker('manifest-parity', `map defines "${n}" but marketplace.json has no entry`, '.claude-plugin/plugins-map.json');
  const meta = metaByName.get(n);
  if (meta && meta.source !== `./plugins/${n}`)
    blocker('manifest-parity', `"${n}" source is "${meta.source}", expected "./plugins/${n}"`, '.claude-plugin/marketplace.json');
  if (meta && !meta.version)
    blocker('version', `"${n}" has no version in marketplace.json`, '.claude-plugin/marketplace.json');
  if (meta && meta.version && !/^\d+\.\d+\.\d+$/.test(meta.version))
    warning('version', `"${n}" version "${meta.version}" is not semver`, '.claude-plugin/marketplace.json');
}

// --- 2. plugin name collisions across the whole marketplace ----------------
// why: skills invoke as <plugin>:<skill>. Two plugins with one name collide on
// the user's machine, including against plugins from OTHER marketplaces.
const seen = new Set();
for (const n of pluginNames) {
  if (seen.has(n)) blocker('name-collision', `plugin "${n}" is defined twice`, '.claude-plugin/plugins-map.json');
  seen.add(n);
}

// --- 3. every declared skill resolves and is well-formed ------------------
const allSkills = new Set();
for (const n of pluginNames) {
  const spec = map.plugins[n];
  for (const id of spec.skills ?? []) {
    allSkills.add(id);
    const dir = join(SHARED, id);
    const md = join(dir, 'SKILL.md');
    if (!existsSync(dir)) { blocker('missing-skill', `"${n}" declares skill "${id}" but shared-skills/${id}/ is missing`, '.claude-plugin/plugins-map.json'); continue; }
    if (!existsSync(md)) { blocker('missing-skill', `shared-skills/${id}/ has no SKILL.md`, `shared-skills/${id}`); continue; }

    const raw = readFileSync(md, 'utf8');
    const fm = frontmatter(raw);
    if (!fm) { blocker('frontmatter', `shared-skills/${id}/SKILL.md has no YAML frontmatter`, `shared-skills/${id}/SKILL.md`); continue; }
    if (!fm.name) blocker('frontmatter', `shared-skills/${id}/SKILL.md has no name:`, `shared-skills/${id}/SKILL.md`);
    // why: a name that disagrees with its folder silently fails to resolve.
    else if (fm.name !== id) blocker('frontmatter', `shared-skills/${id}/SKILL.md declares name "${fm.name}", must match the folder`, `shared-skills/${id}/SKILL.md`);
    if (!fm.description) blocker('frontmatter', `shared-skills/${id}/SKILL.md has no description:`, `shared-skills/${id}/SKILL.md`);
    // why: over 1024 and the plugin validator rejects the ENTIRE plugin, not just the skill.
    else if (fm.description.length > DESCRIPTION_LIMIT)
      blocker('description-length', `shared-skills/${id} description is ${fm.description.length} chars, limit ${DESCRIPTION_LIMIT}`, `shared-skills/${id}/SKILL.md`);
  }
  for (const [kind, dir, ext] of [['agent', 'agents', '.md'], ['command', 'commands', '.md'], ['connector', 'connectors', '.json']]) {
    for (const id of spec[`${kind}s`] ?? [])
      if (!existsSync(join(ROOT, dir, id + ext)))
        blocker('missing-asset', `"${n}" declares ${kind} "${id}" but ${dir}/${id}${ext} is missing`, '.claude-plugin/plugins-map.json');
  }
  for (const f of spec.files ?? [])
    if (!existsSync(join(ROOT, f)))
      blocker('missing-asset', `"${n}" declares file "${f}" which is missing`, '.claude-plugin/plugins-map.json');
}

// --- 4. orphaned skills ----------------------------------------------------
// why: a skill in shared-skills/ that no plugin claims will never ship. Usually
// means someone forgot the map entry after graduating it.
if (existsSync(SHARED))
  for (const id of readdirSync(SHARED))
    if (statSync(join(SHARED, id)).isDirectory() && !allSkills.has(id))
      warning('orphan-skill', `shared-skills/${id}/ is claimed by no plugin, it will never ship`, `shared-skills/${id}`);

// --- 5. internal references resolve ----------------------------------------
// why: a skill that says "read references/foo.md" when there is no foo.md sends
// the agent looking for a file the client does not have.
const KNOWLEDGE_REF = /knowledge\/([A-Za-z0-9_./-]+\.md)/g;
const LOCAL_REF = /(?:^|[\s(`"'])((?:references|assets|scripts|templates)\/[A-Za-z0-9_./-]+\.[a-z0-9]+)/gi;
const neededKnowledge = new Set();

for (const id of allSkills) {
  const dir = join(SHARED, id);
  if (!existsSync(dir)) continue;
  const own = new Set(walk(dir));
  for (const rel of own) {
    if (!rel.endsWith('.md')) continue;
    const text = readFileSync(join(dir, rel), 'utf8');
    for (const m of text.matchAll(KNOWLEDGE_REF)) {
      if (m[1] === 'X.md') continue; // documented placeholder string
      neededKnowledge.add(m[1]);
    }
    for (const m of text.matchAll(LOCAL_REF)) {
      const target = m[1].replace(/^\.\//, '');
      if (!own.has(target))
        blocker('dangling-ref', `shared-skills/${id}/${rel} points at "${target}" which does not exist in that skill`, `shared-skills/${id}/${rel}`);
    }
  }
}

// --- 6. knowledge files exist on disk AND are committed --------------------
// why: this is the bank-contract.md bug. The file was on disk so every local
// check passed, but it was never committed, so it never reached the release
// branch and clients got a skill pointing at nothing.
for (const k of [...neededKnowledge].sort()) {
  if (!existsSync(join(ROOT, 'knowledge', k))) {
    blocker('missing-knowledge', `knowledge/${k} is referenced by a shipped skill but does not exist`, 'knowledge/');
    continue;
  }
  if (!NO_GIT && !gitHas(REF, `knowledge/${k}`))
    blocker('uncommitted-knowledge', `knowledge/${k} exists on disk but is not committed on "${REF}", so it will not ship`, 'knowledge/');
}

// --- 7. generated tree is in sync -----------------------------------------
// why: plugins/ is what actually ships. If someone edited a skill and did not
// regenerate, the release ships the old copy.
try {
  execFileSync('node', [join(ROOT, 'scripts', 'generate-plugins.mjs'), '--check', '--root', ROOT],
    { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
} catch (e) {
  const out = ((e.stdout ?? '') + (e.stderr ?? '')).trim();
  blocker('stale-build', `plugins/ does not match the source layer. Run: node scripts/generate-plugins.mjs`, out.split('\n').slice(0, 6).join(' | '));
}

// --- 8. hygiene of the generated output ------------------------------------
const OUT = join(ROOT, 'plugins');
const ABS_PATH = /(?:[A-Za-z]:\\Users\\[A-Za-z0-9._-]+|\/Users\/[A-Za-z0-9._-]+|\/home\/[A-Za-z0-9._-]+)/;
const SECRETISH = /(sk-[A-Za-z0-9]{16,}|AIza[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,})/;

for (const rel of walk(OUT)) {
  const buf = readFileSync(join(OUT, rel));
  if (!isText(buf)) continue;
  const text = buf.toString('utf8');

  // why: Cowork's YAML parser rejects CRLF and leaks the whole frontmatter into the body.
  if (buf.includes(Buffer.from('\r\n')))
    blocker('crlf', `plugins/${rel} has CRLF line endings`, `plugins/${rel}`);

  // why: builder-only tracing must never reach a client.
  if (text.includes('DEBUG-TRACE'))
    blocker('debug-trace', `plugins/${rel} contains DEBUG-TRACE instrumentation`, `plugins/${rel}`);

  // why: a hardcoded home directory is useless on a client machine and leaks your username.
  const abs = text.match(ABS_PATH);
  if (abs) blocker('absolute-path', `plugins/${rel} contains the machine-local path "${abs[0]}"`, `plugins/${rel}`);

  if (SECRETISH.test(text))
    blocker('secret', `plugins/${rel} looks like it contains a live API key`, `plugins/${rel}`);

  // why: Billy's hard rule. Em dashes are the AI tell the whole brand is built against.
  // Code spans and fenced blocks are exempt: a doc that states the rule has to be
  // able to quote the character it is banning.
  if (rel.endsWith('.md')) {
    const prose = text
      .replace(/```[\s\S]*?```/g, '')  // fenced blocks
      .replace(/`[^`\n]*`/g, '');      // inline code spans
    if (prose.includes('—')) {
      const lines = prose.split('\n');
      for (let i = 0; i < lines.length; i++)
        if (lines[i].includes('—'))
          warning('em-dash', `plugins/${rel} has an em dash in prose`, `plugins/${rel}:${i + 1}  ${lines[i].trim().slice(0, 70)}`);
    }
  }
}

// --- 9. every plugin actually produced something --------------------------
for (const n of pluginNames) {
  const dir = join(OUT, n);
  if (!existsSync(join(dir, '.claude-plugin', 'plugin.json')))
    blocker('empty-plugin', `plugins/${n}/ has no plugin.json`, `plugins/${n}`);
  else if (!walk(join(dir, 'skills')).length)
    blocker('empty-plugin', `plugins/${n}/ ships zero skills`, `plugins/${n}`);
}

// --- 10. release-state checks ---------------------------------------------
if (!NO_GIT) {
  const status = git(['status', '--porcelain']);
  if (status && status.trim())
    warning('dirty-tree', `working tree has uncommitted changes, a release would not capture them`, `${status.trim().split('\n').length} file(s)`);

  const branch = (git(['branch', '--show-current']) ?? '').trim();
  if (branch && branch !== 'dev')
    warning('branch', `on "${branch}", releases are cut from dev`, branch);

  for (const n of pluginNames) {
    const v = metaByName.get(n)?.version;
    if (!v) continue;
    for (const tag of [`v${v}`, `${n}-v${v}`])
      if ((git(['tag', '--list', tag]) ?? '').trim())
        warning('version', `"${n}" is still at ${v} and tag ${tag} already exists, bump before releasing`, tag);
  }
}

// ---------------------------------------------------------------- report

const blockers = findings.filter((f) => f.level === 'BLOCKER');
const warns = findings.filter((f) => f.level === 'WARNING');

if (JSON_OUT) {
  console.log(JSON.stringify({ ok: blockers.length === 0, blockers, warnings: warns }, null, 2));
} else {
  const byCheck = (list) => {
    const g = new Map();
    for (const f of list) { if (!g.has(f.check)) g.set(f.check, []); g.get(f.check).push(f); }
    return g;
  };
  console.log('');
  if (blockers.length) {
    console.log(`BLOCKERS (${blockers.length}) - do not release\n`);
    for (const [check, list] of byCheck(blockers)) {
      console.log(`  [${check}]`);
      for (const f of list) console.log(`    ${f.message}${f.where ? `\n      ${f.where}` : ''}`);
    }
    console.log('');
  }
  if (warns.length) {
    console.log(`WARNINGS (${warns.length})\n`);
    for (const [check, list] of byCheck(warns)) {
      console.log(`  [${check}]`);
      for (const f of list) console.log(`    ${f.message}${f.where ? `\n      ${f.where}` : ''}`);
    }
    console.log('');
  }
  const skillCount = allSkills.size;
  console.log(blockers.length
    ? `FAIL. ${pluginNames.length} plugin(s), ${skillCount} skill(s). ${blockers.length} blocker(s).\n`
    : `PASS. ${pluginNames.length} plugin(s), ${skillCount} skill(s), ${warns.length} warning(s). Production ready.\n`);
}

process.exit(blockers.length ? 1 : 0);
