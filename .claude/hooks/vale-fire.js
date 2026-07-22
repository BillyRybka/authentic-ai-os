#!/usr/bin/env node
// PostToolUse hook: auto-lint markdown edits against Billy's voice rules.
// Runs Vale on the edited file. Silent on clean files. Reports findings to
// Claude's context on dirty ones. Applies conservative Tier 1 auto-fixes.

const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const VALE_BIN = 'C:\\Users\\billr\\.local\\bin\\vale.exe';
// Hook lives at <vault>/.claude/hooks/vale-fire.js, derive vault root from __dirname.
const VAULT = path.resolve(__dirname, '..', '..');
const LOG = path.join(VAULT, '.claude', 'voice-audit-log.md');

// Deterministic 1:1 swaps safe to auto-apply. Anything not here gets reported.
const AUTO_FIX = {
  'utilize': 'use',
  'utilizes': 'uses',
  'utilized': 'used',
  'utilizing': 'using',
  'in order to': 'to',
  'furthermore,': 'and',
  'moreover,': 'also,',
  'therefore,': 'so,',
};

function readStdin() {
  try { return fs.readFileSync(0, 'utf8'); } catch { return ''; }
}

function exitSilent() { process.exit(0); }

function isExcluded(filePath) {
  const rel = path.relative(VAULT, filePath).replace(/\\/g, '/');
  if (!rel.endsWith('.md')) return true;
  if (rel.startsWith('..')) return true; // outside vault
  const skipDirs = [
    'Content/pieces/',
    'Resources/references/',
    'raw/',
    'Daily/',
    'Intelligence/',
    'Onboarding/',
    '.claude/',
    'node_modules/',
  ];
  if (skipDirs.some(d => rel.startsWith(d))) return true;
  if (/transcript.*\.md$/i.test(rel)) return true;
  // Meta files that document the voice rules themselves. They must contain the banned words.
  const metaFiles = ['CLAUDE.md', 'Context/system-evolution.md'];
  if (metaFiles.includes(rel)) return true;
  // Frontmatter checks
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    const fm = content.match(/^---\n([\s\S]*?)\n---/);
    if (fm) {
      if (/^ownership:\s*third-party/m.test(fm[1])) return true;
      if (/^voice_audit:\s*skip/m.test(fm[1])) return true;
      if (/^status:\s*(published|sent)/m.test(fm[1])) return true;
    }
  } catch { /* file missing, skip */ }
  return false;
}

function runVale(filePath) {
  try {
    const out = execFileSync(VALE_BIN, ['--output=JSON', filePath], {
      cwd: VAULT,
      encoding: 'utf8',
      stdio: ['ignore', 'pipe', 'pipe'],
    });
    return JSON.parse(out);
  } catch (err) {
    // Vale exits non-zero when it finds violations. That's expected. Output still valid.
    if (err.stdout) {
      try { return JSON.parse(err.stdout); } catch { return null; }
    }
    return null;
  }
}

function logSwap(filePath, line, match, replacement) {
  try {
    const rel = path.relative(VAULT, filePath).replace(/\\/g, '/');
    const ts = new Date().toISOString();
    const entry = `- ${ts} | ${rel}:${line} | "${match}" → "${replacement}"\n`;
    fs.mkdirSync(path.dirname(LOG), { recursive: true });
    fs.appendFileSync(LOG, entry);
  } catch { /* logging is best-effort */ }
}

function applyAutoFixes(filePath, findings) {
  let content;
  try { content = fs.readFileSync(filePath, 'utf8'); } catch { return 0; }
  let applied = 0;
  let newContent = content;
  for (const f of findings) {
    const match = f.Match;
    if (!match) continue;
    const replacement = AUTO_FIX[match.toLowerCase()];
    if (!replacement) continue;
    const before = newContent;
    newContent = newContent.replace(match, replacement);
    if (newContent !== before) {
      applied++;
      logSwap(filePath, f.Line, match, replacement);
    }
  }
  if (applied > 0) {
    const tmp = filePath + '.vale-tmp';
    try {
      fs.writeFileSync(tmp, newContent, 'utf8');
      fs.renameSync(tmp, filePath);
    } catch { applied = 0; }
  }
  return applied;
}

function main() {
  const raw = readStdin();
  if (!raw) exitSilent();
  let payload;
  try { payload = JSON.parse(raw); } catch { exitSilent(); }

  // Claude Code hook payload: { tool_name, tool_input: { file_path, ... }, ... }
  const tool = payload.tool_name || '';
  if (!['Edit', 'Write', 'MultiEdit', 'NotebookEdit'].includes(tool)) exitSilent();

  const filePath = payload.tool_input?.file_path;
  if (!filePath || !fs.existsSync(filePath)) exitSilent();

  if (isExcluded(filePath)) exitSilent();

  const result = runVale(filePath);
  if (!result) exitSilent();

  // Flatten file-keyed findings object
  const allFindings = [];
  for (const key of Object.keys(result)) {
    for (const f of result[key] || []) allFindings.push(f);
  }
  if (allFindings.length === 0) exitSilent();

  const autoFixed = applyAutoFixes(filePath, allFindings);

  // Re-run Vale after auto-fix to get remaining findings
  let remaining = allFindings;
  if (autoFixed > 0) {
    const after = runVale(filePath);
    if (after) {
      remaining = [];
      for (const key of Object.keys(after)) {
        for (const f of after[key] || []) remaining.push(f);
      }
    }
  }

  if (remaining.length === 0 && autoFixed > 0) {
    const rel = path.relative(VAULT, filePath).replace(/\\/g, '/');
    console.log(`\n## Voice audit: ${rel}`);
    console.log(`Auto-fixed ${autoFixed} deterministic swap(s). Clean otherwise.\n`);
    exitSilent();
  }

  if (remaining.length === 0) exitSilent();

  // Report remaining findings
  const rel = path.relative(VAULT, filePath).replace(/\\/g, '/');
  const errors = remaining.filter(f => f.Severity === 'error');
  const warnings = remaining.filter(f => f.Severity === 'warning');

  console.log(`\n## Voice audit: ${rel}`);
  if (autoFixed > 0) console.log(`Auto-fixed ${autoFixed} deterministic swap(s).`);
  if (errors.length) {
    console.log(`\n**Errors (${errors.length}), fix before publishing:**`);
    for (const f of errors.slice(0, 10)) {
      console.log(`  L${f.Line}: ${f.Message}`);
    }
    if (errors.length > 10) console.log(`  ...and ${errors.length - 10} more`);
  }
  if (warnings.length) {
    console.log(`\n**Warnings (${warnings.length}), review:**`);
    for (const f of warnings.slice(0, 10)) {
      console.log(`  L${f.Line}: ${f.Message}`);
    }
    if (warnings.length > 10) console.log(`  ...and ${warnings.length - 10} more`);
  }
  console.log(`\nRun \`vale ${rel}\` for full output. See .vale/styles/ProductVoice/ for the rules.\n`);
  exitSilent();
}

main();
