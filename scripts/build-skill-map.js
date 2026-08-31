// Authentic AI OS - skill system map generator
// Renders one card per skill in Billy's 3-band format: Step / Reads / Writes
// POSTs to the local Excalidraw canvas server.

const API = 'http://localhost:3000/api';

// ---------- palette ----------
const C = {
  ink: '#1e1e1e',
  bandStep: '#ffec99',   // yellow
  bandRead: '#e6fcf5',   // teal
  bandWrite: '#fff4e6',  // orange
  stepChip: '#eaddd7',   // tan
  piece: '#a5d8ff',      // blue   - per-video files
  found: '#d0bfff',      // purple - foundation + banks
  craft: '#ffd8a8',      // tan-orange - knowledge/ + references/
  write: '#b2f2bb',      // green  - writes
  writeAlt: '#8ce99a',   // green darker - the pipeline gate field
  shellReleased: '#d0ebff',
  shellStaged: '#e9fac8',
  shellWip: '#ffe8cc',
  white: '#ffffff',
};

// ---------- geometry ----------
const LABEL_W = 150;
const COL_W = 218;
const COL_GAP = 14;
const PITCH = COL_W + COL_GAP;
const PAD = 18;
const CHIP_W = COL_W;
const CHIP_GAP = 8;
const FS = 12;          // chip font size
const LH = 15;          // line height px at FS 12
const CHARS = 30;       // wrap width

const els = [];
const uid = (() => { let n = 0; return p => `${p}-${++n}`; })();

function wrap(text, chars = CHARS) {
  const out = [];
  for (const para of String(text).split('\n')) {
    let line = '';
    for (const w of para.split(' ')) {
      if (!line) { line = w; }
      else if ((line + ' ' + w).length <= chars) { line += ' ' + w; }
      else { out.push(line); line = w; }
    }
    out.push(line);
  }
  return out;
}

function chipH(text, chars = CHARS) {
  return Math.max(34, wrap(text, chars).length * LH + 16);
}

function rect(x, y, w, h, bg, opts = {}) {
  const e = {
    id: opts.id || uid('r'), type: 'rectangle', x, y, width: w, height: h,
    backgroundColor: bg, strokeColor: opts.stroke || C.ink, fillStyle: 'solid',
    strokeWidth: opts.strokeWidth || 1, strokeStyle: opts.strokeStyle || 'solid',
    roughness: opts.roughness === undefined ? 1 : opts.roughness,
    roundness: { type: 3 },
  };
  els.push(e);
  return e;
}

function label(x, y, w, text, size = FS, opts = {}) {
  els.push({
    id: uid('t'), type: 'text', x, y, width: w, height: wrap(text, opts.chars || CHARS).length * (size * 1.25),
    text, fontSize: size, fontFamily: 6,
    textAlign: opts.align || 'center', verticalAlign: 'top',
    strokeColor: opts.color || C.ink, backgroundColor: 'transparent',
  });
}

// a chip = rounded rect + centred text
function chip(x, y, text, bg, opts = {}) {
  const w = opts.w || CHIP_W;
  const lines = wrap(text, opts.chars || CHARS);
  const h = opts.h || Math.max(34, lines.length * LH + 16);
  rect(x, y, w, h, bg, { roughness: 1, strokeStyle: opts.strokeStyle });
  const th = lines.length * (FS * 1.25);
  label(x + 8, y + (h - th) / 2, w - 16, lines.join('\n'), FS, { chars: 999 });
  return h;
}

// ---------- card renderer ----------
// skill = { name, status, note, steps: [{ title, reads:[[text,kind]], writes:[[text,kind]] }] }
function card(x, y, skill) {
  const n = skill.steps.length;
  const cardW = LABEL_W + n * PITCH - COL_GAP + PAD * 2;

  // measure bands
  const stepH = Math.max(...skill.steps.map(s => chipH(s.title, 26)));
  const stepBandH = PAD + stepH + PAD;

  const colH = (items) => items.reduce((a, it) => a + chipH(it[0]) + CHIP_GAP, 0) - CHIP_GAP;
  const readBandH = PAD + Math.max(46, ...skill.steps.map(s => colH(s.reads || []))) + PAD;
  const writeBandH = PAD + Math.max(46, ...skill.steps.map(s => colH(s.writes || []))) + PAD;
  const cardH = stepBandH + readBandH + writeBandH;

  // title above the card
  label(x, y - 62, cardW, skill.name, 30, { align: 'left', chars: 999 });
  label(x, y - 26, cardW, `${skill.status}${skill.note ? '  ·  ' + skill.note : ''}`, 14, { align: 'left', chars: 999, color: '#6b6b6b' });

  // bands
  rect(x, y, cardW, stepBandH, C.bandStep, { roughness: 0 });
  rect(x, y + stepBandH, cardW, readBandH, C.bandRead, { roughness: 0 });
  rect(x, y + stepBandH + readBandH, cardW, writeBandH, C.bandWrite, { roughness: 0 });

  // row labels
  label(x + 22, y + PAD + 4, LABEL_W - 30, 'Step', 26, { align: 'left', chars: 999 });
  label(x + 22, y + stepBandH + PAD, LABEL_W - 30, 'Reads', 26, { align: 'left', chars: 999 });
  label(x + 22, y + stepBandH + readBandH + PAD, LABEL_W - 30, 'Writes', 26, { align: 'left', chars: 999 });

  // columns
  skill.steps.forEach((s, i) => {
    const cx = x + PAD + LABEL_W + i * PITCH;
    chip(cx, y + PAD, s.title, C.stepChip, { chars: 26, h: stepH });

    let cy = y + stepBandH + PAD;
    for (const [txt, kind] of (s.reads || [])) {
      cy += chip(cx, cy, txt, C[kind] || C.craft) + CHIP_GAP;
    }
    cy = y + stepBandH + readBandH + PAD;
    for (const [txt, kind] of (s.writes || [])) {
      cy += chip(cx, cy, txt, C[kind] || C.write) + CHIP_GAP;
    }
  });

  return { w: cardW, h: cardH };
}

// ================= DATA =================
// kinds: piece (blue, per-video files) | found (purple, foundation+banks)
//        craft (tan, knowledge/ + references/) | write / writeAlt (green)

const PIPELINE = [
  {
    name: 'vid-ideas', status: 'STAGED', note: 'optional front door · no piece folder yet',
    steps: [
      { title: '1. Lean load + focus',
        reads: [['creator-foundation.md\niceberg · pillars · avatar · Top 3', 'found'],
                ['banks/pattern-bank.md\nreal outlier rows', 'found'],
                ['content/ideas-backlog.md\nif present (anti-repeat scan)', 'found']],
        writes: [] },
      { title: '2. Generate the batch',
        reads: [['knowledge/iceberg-and-top-3-\nalignment.md', 'craft'],
                ['knowledge/theory-of-one-\ncuration.md', 'craft']],
        writes: [] },
      { title: '3. Adjust + pick (the dial)',
        reads: [['(no new loads)\nsharper / more / tighter / wilder', 'craft']],
        writes: [] },
      { title: '4. Save keepers + hand off',
        reads: [],
        writes: [['content/ideas-backlog.md\nKEEPERS ONLY', 'write'],
                 ['seed packet → vid-intake\nfull receipt: title, channel,\nviews, multiplier', 'writeAlt']] },
    ],
  },
  {
    name: 'vid-intake', status: 'STAGED', note: 'creates the piece folder',
    steps: [
      { title: '1. Open the door',
        reads: [['knowledge/piece-contract.md\ncreation subset', 'craft']],
        writes: [['piece.md  CREATED\nslug · created · status: ideating\nanchor · pillar (from packet)', 'writeAlt']] },
      { title: '2. Reflect + checkpoint',
        reads: [['brain-dump schema\nowned by this SKILL.md', 'craft']],
        writes: [['brain-dump.md  CREATED\n## Raw dump (verbatim,\nsource of truth) + sections', 'writeAlt']] },
      { title: '3. Offer one deeper pass',
        reads: [['references/digging-deeper.md\nwhich spots pay off', 'craft'],
                ['references/verify-subagent.md\nuncertain claims only', 'craft'],
                ['knowledge/story-capture-guide.md\nthin story only', 'craft']],
        writes: [['brain-dump.md\nnew material in their words\n+ TODOs (never inventions)', 'write']] },
      { title: '4. Fit + pillar, one move',
        reads: [['creator-foundation.md\niceberg + pillars\n(loaded HERE, not cold)', 'found']],
        writes: [['piece.md\niceberg_aligned · pillar\nalignment_note', 'write']] },
      { title: '5. Finalize + hand off',
        reads: [],
        writes: [['(close only, already on disk)\n→ vid-framing', 'write']] },
    ],
  },
  {
    name: 'vid-framing', status: 'STAGED', note: 'psychology first, evidence second',
    steps: [
      { title: '1. Read the brain-dump',
        reads: [['brain-dump.md\nthe material + the problem\nit keeps circling', 'piece']],
        writes: [] },
      { title: "2. Viewer's head, then confirm",
        reads: [['creator-foundation.md\navatar + iceberg', 'found']],
        writes: [] },
      { title: '3. Hunt the stake',
        reads: [['references/stake-finder.md\nwhere the stake lives,\nwhen to call the ceiling', 'craft']],
        writes: [] },
      { title: '4. Lock format + goal',
        reads: [['voice-profile.md\nthe refusals list', 'found'],
                ['references/format-index.md\nthe 7 formats and their jobs', 'craft']],
        writes: [] },
      { title: '5. Save + hand off',
        reads: [],
        writes: [['piece.md frontmatter\nframe · core_payoff · mechanism\nformat · goal · voice_context', 'writeAlt'],
                 ['piece.md body\n## The Read (Target · Transformation\nStakes)\nproof TODOs', 'write']] },
    ],
  },
  {
    name: 'vid-title', status: 'STAGED', note: 'shop the banks, adjust to true material',
    steps: [
      { title: '1. Inherit frame, build lock list',
        reads: [['piece.md\nlocked angle + payoff', 'piece'],
                ['brain-dump.md\n(+ script.md if it exists)', 'piece'],
                ['creator-foundation.md\navatar · iceberg · credibility', 'found']],
        writes: [] },
      { title: '2. Shop the banks',
        reads: [['banks/pattern-bank.md', 'found'],
                ['banks/title-bank.md\nproven structures + sources', 'found']],
        writes: [] },
      { title: '3. Write wide, then kill',
        reads: [['banks/power-words-bank.md', 'found'],
                ['knowledge/BENS-framework.md\nthe feeling lens', 'craft']],
        writes: [] },
      { title: '4. One checklist pass',
        reads: [['references/title-filters.md\non demand: soft flags,\nno-banks fallback', 'craft'],
                ['references/angle-anchor-rules.md\non demand. THE canonical\nreceipt rule. Moved here\nout of vid-framing.', 'craft'],
                ['references/reframe-toolkit.md\non demand: the 5 shapes,\nwhen the plain statement\nis not landing', 'craft']],
        writes: [] },
      { title: '5. Present with receipts',
        reads: [], writes: [] },
      { title: '6. Lock one title',
        reads: [],
        writes: [['piece.md\ntitle  (+ its receipt)', 'writeAlt']] },
    ],
  },
  {
    name: 'vid-thumbnail', status: 'STAGED', note: 'text only · completes the title, never restates it',
    steps: [
      { title: '1. Read title, mine its partner',
        reads: [['piece.md\nlocked title · format · goal', 'piece'],
                ['script.md if complete,\nelse brain-dump.md\n(numbers → the lock list)', 'piece']],
        writes: [] },
      { title: '2. Shape candidates',
        reads: [['knowledge/thumbnail-text-\npatterns.md: the one craft ref', 'craft'],
                ['packaging-system.md +\nbanks/packaging-bank/\nOVERRIDE every default', 'found']],
        writes: [] },
      { title: '3. Filter hard, show package',
        reads: [], writes: [] },
      { title: '4. Pick 1-2 to test',
        reads: [], writes: [] },
      { title: '5. Save + hand off',
        reads: [],
        writes: [['piece.md\nthumbnail_text (1-2)\nthumbnail_shape', 'writeAlt']] },
    ],
  },
  {
    name: 'vid-structure', status: 'STAGED', note: 'plans, never writes prose',
    steps: [
      { title: '1. Rough the spine',
        reads: [['brain-dump.md\nmine the points', 'piece'],
                ['piece.md\nangle · payoff · format · goal', 'piece'],
                ['knowledge/format-planners/\n{format}.md', 'craft'],
                ['references/brain-dump-mining.md', 'craft']],
        writes: [] },
      { title: '2. Build out the plan',
        reads: [['knowledge/parable-decision-\nmatrix.md: pick, not shortlist', 'craft'],
                ['knowledge/script-tension-\narchitecture.md: ordering', 'craft'],
                ['the 5 evidence banks\nqueried ONE at a time,\nonly when a point calls', 'found']],
        writes: [] },
      { title: '3. Write it down',
        reads: [['assets/script-skeleton-\ntemplate.md', 'craft']],
        writes: [['script.md  CREATED\nIntro stub · one section per\npoint (Parable + Principle)\nEnding stub · ## To build\nCUTS comment', 'writeAlt'],
                 ['piece.md\nsegment_purposes · tension_plan\nstatus: drafting', 'writeAlt']] },
    ],
  },
  {
    name: 'vid-intro', status: 'STAGED', note: 'hard-stops without a locked title + thumbnail',
    steps: [
      { title: '1. Anchor',
        reads: [['piece.md\ntitle · thumbnail_text · format', 'piece'],
                ['brain-dump.md + script.md\nmaterial + the outline\nthe intro forwards into', 'piece'],
                ['creator-foundation.md\navatar + credibility brags', 'found'],
                ['voice-profile.md\nguardrails ·\npreferred_hook_types', 'found'],
                ['knowledge/intro-architecture.md\nknowledge/format-planners/\n{format}.md', 'craft']],
        writes: [] },
      { title: '2. Hook + Problem/Result',
        reads: [['references/hook-patterns.md', 'craft'],
                ['banks/hook-bank.md\nsoft-load, missing is fine', 'found']],
        writes: [] },
      { title: '3. Setup + Transition',
        reads: [['knowledge/transition-patterns.md\nSections 1 + 4', 'craft']],
        writes: [] },
      { title: '4. Assemble + pressure-test',
        reads: [['reference-pieces/\n{voice_context}.md', 'found'],
                ['knowledge/voice-pressure-test.md\nvoice-rhythm.md', 'craft'],
                ['knowledge/visual-proof-callouts.md\nattention-craft.md', 'craft'],
                ['conditional: story-pulling-criteria\nproof-placement-rules\nmetaphor-integration + banks', 'craft']],
        writes: [] },
      { title: '5. Lock and save',
        reads: [['knowledge/bank-contract.md\nupdate-both-sides rule', 'craft']],
        writes: [['script.md\n## Intro (replaces the stub)', 'writeAlt'],
                 ['piece.md\nintro_locked · viewer_questions\n*_used · last_updated', 'writeAlt'],
                 ['bank entries\nused_in + status', 'write']] },
    ],
  },
  {
    name: 'vid-segment', status: 'STAGED', note: 'ONE segment per run, then stops · loops until body done',
    steps: [
      { title: '1. Read plan, verify materials',
        reads: [['piece.md\nformat · goal', 'piece'],
                ['script.md\nTHIS section + its picked\nparable / principle / blocks', 'piece'],
                ['brain-dump.md', 'piece'],
                ['knowledge/format-planners/\n{format}.md', 'craft']],
        writes: [] },
      { title: '2. Repair what verify flagged',
        reads: [['knowledge/parable-decision-\nmatrix.md (re-pick, max 3)', 'craft'],
                ['knowledge/framework-builder.md\nreferences/visual-demo-builder.md', 'craft'],
                ['the 5 evidence banks\n→ can call vid-capture\nmid-flow for a new entry', 'found']],
        writes: [] },
      { title: '3. Draft fast, for tension',
        reads: [['voice-profile.md +\nreference-pieces/', 'found'],
                ['brain-dump.md phrasing first,\nreference cadence second', 'piece'],
                ['references/parable-principle-\nshapes.md', 'craft']],
        writes: [] },
      { title: '4. Edit out loud',
        reads: [['knowledge/transition-patterns.md\nSection 2', 'craft'],
                ['banks/transition-bank.md\nsoft-load, missing is fine', 'found'],
                ['knowledge/attention-craft.md\nvoice-pressure-test.md\nvoice-rhythm.md', 'craft']],
        writes: [] },
      { title: '5. The creator gate',
        reads: [['read-aloud, the voice test', 'craft']],
        writes: [] },
      { title: '6. Save + update the graph',
        reads: [['knowledge/bank-contract.md', 'craft']],
        writes: [['script.md\nONE body section, APPENDED\nnever overwrites', 'writeAlt'],
                 ['piece.md\nsegments_completed += label\n*_used += wikilinks', 'writeAlt'],
                 ['bank entries\nstatus: used · used_in', 'write']] },
    ],
  },
  {
    name: 'vid-ending', status: 'STAGED', note: 'needs full body + non-stub Intro',
    steps: [
      { title: '1. Read video, pick the next',
        reads: [['piece.md\nformat · goal · pillar\nframe', 'piece'],
                ['script.md\nFULL body + ## Intro VERBATIM\n(Setup contract, hook lane,\ncredibility receipt)', 'piece'],
                ['creator-foundation.md\navatar + Top 3 problems', 'found'],
                ['knowledge/format-planners/\n{format}.md: close shape', 'craft'],
                ['references/end-screen-design.md\npicking the next video', 'craft']],
        writes: [] },
      { title: '2. Draft 2 candidates',
        reads: [['voice-profile.md +\nreference-pieces/\n{voice_context}.md', 'found'],
                ['knowledge/transition-patterns.md\nSections 3 + 4 (BE-1..BE-8)', 'craft'],
                ['banks/transition-bank.md\nsoft-load', 'found'],
                ['references/pivot-gap-bridge-shapes\ncta-placement-by-format\nending-anti-patterns', 'craft']],
        writes: [] },
      { title: '3. Pick and refine',
        reads: [['knowledge/attention-craft.md\nenergy + pacing', 'craft']],
        writes: [] },
      { title: '4. Lock and save',
        reads: [['knowledge/voice-pressure-test.md\nvoice-rhythm.md', 'craft'],
                ['knowledge/bank-contract.md', 'craft']],
        writes: [['script.md\n## Ending (Pivot·Gap·Bridge)', 'writeAlt'],
                 ['piece.md\nending_locked · next_video\nlast_updated', 'writeAlt']] },
    ],
  },
  {
    name: 'vid-pressure-test', status: 'STAGED', note: 'edits script.md in place · sets filming-ready',
    steps: [
      { title: '1. Load + condition rubrics',
        reads: [['script.md FULL\nno stub sections allowed', 'piece'],
                ['piece.md\nframe · format · goal\n(goal + format weight rubrics)', 'piece'],
                ['brain-dump.md\nclaim traceability source', 'piece'],
                ['creator-foundation.md\nvoice-profile.md', 'found']],
        writes: [] },
      { title: '2. Run 4 reviewers in parallel',
        reads: [['references/reviewer-*.md\nsource-trace · voice · AI-slop\n· retention (top 3 each)', 'craft'],
                ['reference-pieces/\n{voice_context}.md\n+ raw/voice-sources/ (opt)', 'found'],
                ['the 5 evidence banks\nused-material traceability', 'found'],
                ['knowledge/attention-craft.md\nformat-planners (DEFERRED)\ntransition-patterns\nintro-architecture\naudience-temperature-model', 'craft']],
        writes: [] },
      { title: '3. Consolidate + rank',
        reads: [['hard vs soft split', 'craft']], writes: [] },
      { title: '4. Walk hard issues',
        reads: [['approve / deny+rewrite / skip\nhard-rule breaks cannot skip', 'craft']],
        writes: [['script.md\nin-place fixes + issue comments', 'write']] },
      { title: '5. Read-aloud (final gate)',
        reads: [['the creator, out loud.\nnon-negotiable', 'craft']],
        writes: [] },
      { title: '6. Update piece.md + verdict',
        reads: [],
        writes: [['piece.md\npressure_test_audit block', 'write'],
                 ['piece.md\nstatus: filming-ready\nTHE DONE SIGNAL', 'writeAlt']] },
    ],
  },
];

const ORCHESTRATOR = {
  name: 'vid-pipeline', status: 'STAGED', note: 'thin orchestrator · reads state, routes, writes NOTHING',
  steps: [
    { title: '1. Prerequisites (silent)',
      reads: [['foundation/creator-foundation.md\nMISSING → hard halt to /foundation', 'found'],
              ['foundation/voice-profile.md\nmissing → soft warn, never blocks', 'found'],
              ],
      writes: [['nothing', 'write']] },
    { title: '2. Pick the piece',
      reads: [['content/pieces/{slug}/\nnamed slug · led-with-material\n· entry menu · scan in-progress', 'piece']],
      writes: [['nothing', 'write']] },
    { title: '3. Route to the next skill',
      reads: [['piece.md frontmatter +\nsibling-file presence.\nMatched top-to-bottom.\nNO other knowledge files.\nSub-skills own all loading.', 'piece']],
      writes: [['nothing (delegates)', 'write']] },
    { title: '4-6. Invoke, stop, finish',
      reads: [['stop signals honored.\nState persists in piece.md\nfor clean resume', 'piece']],
      writes: [['nothing\nterminates at\nstatus: filming-ready', 'write']] },
  ],
};

const VOICE = [
  {
    name: 'vid-voice-capture', status: 'STAGED', note: 'builds the voice engine · stores NO statistics',
    steps: [
      { title: '1. Source intake + grouping',
        reads: [['raw/voice-sources/\ncreator transcripts + scripts\n(everything hits disk first)', 'found'],
                ['creator-foundation.md', 'found']],
        writes: [['raw/voice-sources/\npasted transcripts written\nto disk BEFORE analysis', 'write']] },
      { title: '2. Diagnose + select passages',
        reads: [['knowledge/voice-extraction-\nmethods.md', 'craft'],
                ['knowledge/voice-profile-schema.md', 'craft']],
        writes: [] },
      { title: '3. Guardrail build',
        reads: [['knowledge/voice-pressure-test.md\nvoice-rhythm.md', 'craft']],
        writes: [] },
      { title: '4-5. Assemble + read-aloud',
        reads: [['knowledge/interview-posture.md\nvoice-profile-schema.md', 'craft']],
        writes: [] },
      { title: '6. Save + state contract',
        reads: [],
        writes: [['foundation/reference-pieces/\n{voice_context}.md\nVERBATIM passages.\nTHE VOICE ENGINE', 'writeAlt'],
                 ['foundation/voice-profile.md\nthin guardrail: refusals\n+ signature phrases', 'writeAlt']] },
    ],
  },
  {
    name: 'vid-voice-update', status: 'STAGED', note: 'surgical · append-only · invoked mid-draft',
    steps: [
      { title: '1-2. Read + classify the signal',
        reads: [['the flagged line + the\ncreator reaction', 'piece'],
                ['foundation/voice-profile.md', 'found'],
                ['knowledge/voice-profile-schema.md', 'craft']],
        writes: [] },
      { title: '3. Apply by type',
        reads: [['HARD RULE → append refusal\nONE-TIME → rewrite in place\nAMBIGUOUS → ask one question', 'craft']],
        writes: [['foundation/voice-profile.md\nrefusals ONLY, and only when\nthe correction is permanent', 'writeAlt'],
                 ['one-time edits save NOTHING\npermanent', 'write']] },
      { title: '4-5. Re-run + report',
        reads: [['invokes vid-voice-audit on the\nin-progress script if a hard\nrule landed mid-draft', 'craft']],
        writes: [['status packet → back to the\ncalling writing skill', 'write']] },
    ],
  },
  {
    name: 'vid-voice-audit', status: 'STAGED', note: 'single source of voice-truth · READ-ONLY, never auto-edits',
    steps: [
      { title: '1. Line-by-line scan',
        reads: [['script.md FULL', 'piece'],
                ['foundation/reference-pieces/\nthe gold-standard passages', 'found'],
                ['foundation/voice-profile.md\nrefusals: banned words +\nrequired swaps', 'found'],
                ['raw/voice-sources/\noptional: 2-3 random passages\nfor drift calibration', 'found'],
                ['references/voice-fault-rubric.md\nseverity tiers + output schema', 'craft']],
        writes: [] },
      { title: '2. Per-beat verdict',
        reads: [['knowledge/voice-pressure-test.md\nvoice-rhythm.md\nvoice-profile-schema.md', 'craft']],
        writes: [] },
      { title: '3-4. Rewrites + return',
        reads: [],
        writes: [['findings list\nseverity · location · quote\n· suggested rewrite', 'write'],
                 ['per-beat verdict map\npasses / soft-flag / would-reword', 'write'],
                 ['NEVER edits script.md.\nNo top-3 cap.', 'write']] },
    ],
  },
];

const SETUP = [
  {
    name: 'creator-setup', status: 'RELEASED', note: 'one-time installer · additive, never destroys',
    steps: [
      { title: '1. Inspect + pick content home',
        reads: [['knowledge/vault-integration.md', 'craft'],
                ['manifest.md\ncurrent-release folder table', 'craft']],
        writes: [] },
      { title: '2. Scaffold',
        reads: [],
        writes: [['the workspace folder structure\nfolders only, per manifest', 'writeAlt'],
                 ['workspace CLAUDE.md\n+ .env.example', 'write'],
                 ['PENDING seeds: banks/hook-bank.md\n+ banks/transition-bank.md\n(go live when the writing\nskills ship)', 'write']] },
    ],
  },
  {
    name: '/foundation', status: 'RELEASED', note: 'thin orchestrator · runs the 5 identity skills in order',
    steps: [
      { title: '1. Silent state check',
        reads: [['creator-foundation.md\nwhich sections are filled', 'found'],
                ['packaging-system.md', 'found'],
                ['knowledge/feedback-offer.md', 'craft']],
        writes: [['nothing', 'write']] },
      { title: '2. Auto-advance the chain',
        reads: [['avatar → positioning → pillars\n→ credibility → backstory', 'craft']],
        writes: [['nothing (delegates)\noffers vid-research at Step 5', 'write']] },
    ],
  },
  {
    name: 'the 5 identity skills', status: 'RELEASED', note: 'vid-avatar · vid-positioning · vid-pillars · vid-credibility · vid-backstory: ALL write ONE file',
    steps: [
      { title: '1. vid-avatar',
        reads: [['knowledge/interview-posture.md\nvault-integration.md\ncreator-foundation-template.md', 'craft'],
                ['voice-profile.md\nif it exists (guarded)', 'found']],
        writes: [['creator-foundation.md\nOffer · Avatar · Top 3', 'writeAlt']] },
      { title: '2. vid-positioning',
        reads: [['creator-foundation.md\nAvatar · Offer · Top 3', 'found'],
                ['knowledge/interview-posture.md', 'craft']],
        writes: [['creator-foundation.md\nIceberg Statement\n(WHO+WHAT+HOW+TENSION)', 'writeAlt']] },
      { title: '3. vid-pillars',
        reads: [['creator-foundation.md\nIceberg · Top 3', 'found']],
        writes: [['creator-foundation.md\nPillars (8-12, root-cause,\n1-4 word labels)', 'writeAlt']] },
      { title: '4. vid-credibility',
        reads: [['creator-foundation.md\nAvatar · Top 3', 'found'],
                ['knowledge/proof-bank-schema.md', 'craft']],
        writes: [['creator-foundation.md\nCredibility (the locked 3)', 'writeAlt'],
                 ['banks/proof-bank/\nEVERY leftover strong proof\n→ pulled by intro, segment,\nending, structure', 'write']] },
      { title: '5. vid-backstory',
        reads: [['creator-foundation.md\nAvatar · Iceberg · Top 3', 'found']],
        writes: [['creator-foundation.md\nBackstory (Problem-Action-\nOutcome) + 3-sentence version', 'writeAlt'],
                 ['people/{Name}.md stub\nif the story is a client\'s', 'write']] },
    ],
  },
  {
    name: 'vid-research', status: 'RELEASED', note: 'Three-Circle Research · fills the pattern banks from real YouTube data',
    steps: [
      { title: '1. Three-Circle pull',
        reads: [['foundation/creator-foundation.md\npackaging-system.md', 'found'],
                ['Public YouTube channel pages\nNEVER hallucinated data', 'craft'],
                ['knowledge/three-circle-research.md\noutlier-identification-rules.md', 'craft']],
        writes: [] },
      { title: '2. Synthesis + curation',
        reads: [['knowledge/theory-of-one-\ncuration.md: Keep/Drop/Modify', 'craft'],
                ['knowledge/thumbnail-text-\npatterns.md', 'craft'],
                ['knowledge/format-rotation-guide.md\npackaging-system-template.md', 'craft']],
        writes: [] },
      { title: '3. Save the banks',
        reads: [],
        writes: [['banks/pattern-bank.md', 'writeAlt'],
                 ['banks/title-bank.md', 'writeAlt'],
                 ['banks/power-words-bank.md', 'writeAlt'],
                 ['foundation/packaging-system.md\n3+1 format rotation +\n1-2 thumbnail strategies', 'writeAlt']] },
    ],
  },
  {
    name: 'vid-capture', status: 'STAGED', note: 'loops one item at a time · also callable mid-script by vid-segment',
    steps: [
      { title: '0. Session start',
        reads: [['knowledge/bank-contract.md\nlocks the schemas', 'craft'],
                ['creator-foundation.md\nvoice-profile.md\nalignment checks', 'found']],
        writes: [] },
      { title: 'Stage S / M / P / T / F',
        reads: [['S → knowledge/story-capture-guide\nM → references/metaphor-builder\nP → references/proof-capture-guide\nT → references/testimonial-capture\nF → knowledge/framework-builder', 'craft']],
        writes: [] },
      { title: 'Finish any entry',
        reads: [['assets/{type}-entry-template.md', 'craft'],
                ['dedup scan against the\nexisting bank files', 'found']],
        writes: [['banks/story-bank/\nbanks/metaphor-bank/\nbanks/proof-bank/\nbanks/testimonial-bank/\nbanks/framework-bank/', 'writeAlt'],
                 ['people/{Full Name}.md stub\nbidirectional wikilink.\nEntry NOT saved if stub fails.', 'write']] },
    ],
  },
];
const WIP = [
  {
    name: 'aud-intake', status: 'WIP', note: 'audience 1 of 4 · file-based only, refuses pasted material',
    steps: [
      { title: '1. Read the inbox',
        reads: [['inbox/audience/calls/\nmax 5 per run, high trust', 'found'],
                ['inbox/audience/comments/\n{video-slug}.csv\nmax 100, LOW trust:\nvocabulary samples only', 'found'],
                ['banks/audience-data/\nexisting, for incremental runs', 'found']],
        writes: [] },
      { title: '2. Pull quote units',
        reads: [['skills-wip/synthetic-audience-\nmethod.md (parked)', 'craft'],
                ['skills-wip/vault-integration-\naud-schemas.md (parked)', 'craft'],
                ['knowledge/bank-contract.md\nthe person-stub rule', 'craft']],
        writes: [] },
      { title: '3. Contamination scan + save',
        reads: [['flags 2+ AI tells.\nNever blocks: kept as\nneeds_review, batched at end.', 'craft']],
        writes: [['banks/audience-data/calls/\n{call-slug}.md\n~15 verbatim units tagged\nI-am · I-tried · I-fear\nI-want · I-pushed-back', 'writeAlt'],
                 ['banks/audience-data/comments/\n{video-slug}/{id}.md', 'write'],
                 ['raw/audience/\nsources MOVED here as an\naudit trail, never deleted', 'write']] },
    ],
  },
  {
    name: 'aud-avatar-build', status: 'WIP', note: 'audience 2 of 4 · held-out segregation is the guardrail',
    steps: [
      { title: '1. Cluster (creator names them)',
        reads: [['banks/audience-data/\nclustered by pain pattern,\nnot demographics', 'found'],
                ['audience/state.md\nresume state', 'found'],
                ['the parked method +\naud schemas', 'craft']],
        writes: [['audience/segments/{slug}.md\n4 to 6 segments, deliberately\nsmall', 'writeAlt']] },
      { title: '2. Segregate held-out FIRST',
        reads: [['strongest 25-30% of each\nsegment, preferring I-fear\nand I-pushed-back', 'found']],
        writes: [['audience/held-out/{slug}.md\nWRITTEN BEFORE ANY DRAFT,\nthen read back FROM DISK.\nFile separation, not memory,\nis what stops the leak.', 'writeAlt']] },
      { title: '3. Draft avatars',
        reads: [['the NON-held-out pool only.\n2+ citations per claim or the\nclaim is stripped as stereotype', 'found']],
        writes: [['audience/avatars/{slug}.md\nstatus: draft (unusable until\nvalidation flips it)\nIdentity · Top Problems ·\nTop Objections · Vocabulary', 'writeAlt']] },
    ],
  },
  {
    name: 'aud-validate', status: 'WIP', note: 'audience 3 of 4 · the ONLY skill allowed to read held-out/',
    steps: [
      { title: '1. Three pass-or-fail tests',
        reads: [['audience/avatars/{slug}.md\nstatus: draft', 'found'],
                ['audience/held-out/{slug}.md\nEXCLUSIVE READER', 'found'],
                ['references/common-english.txt\nfor the vocabulary-leak test', 'craft'],
                ['the parked method +\naud schemas', 'craft']],
        writes: [] },
      { title: '2. Tier the result',
        reads: [['tests 1+3 pass:\nvalidated-vocabulary\nall three pass: validated-full\nanything less stays draft', 'craft']],
        writes: [['audience/avatars/\n{slug}-validation-{date}.md\nplain English, stats jargon\nis BANNED from creator output', 'writeAlt'],
                 ['avatar status flips to\nvalidated-vocabulary or\nvalidated-full.\nOne validation per date.', 'writeAlt']] },
    ],
  },
  {
    name: 'aud-review', status: 'WIP', note: 'audience 4 of 4 · panel of validated avatars only',
    steps: [
      { title: '1. Filter the panel',
        reads: [['audience/avatars/\nstatus validated-* only.\nCTA review demands\nvalidated-full.', 'found'],
                ['banks/audience-data/\ncalibration date check:\n60+ days stale forces a\nwarning appended', 'found'],
                ['the piece under review\nscript · email · hook · CTA ·\ntitle+thumbnail (always paired)', 'piece']],
        writes: [] },
      { title: '2. Isolated subagent per avatar',
        reads: [['each sees ONLY its own profile,\nthe piece, the question block,\nthe 5 dimensions.\nBlind to the other avatars\nand to the synthesis.', 'craft']],
        writes: [['each response written to disk\nBEFORE the next runs', 'write']] },
      { title: '3. Synthesise',
        reads: [['reads those files back.\nMEDIAN, never mean, so a lone\nskeptic is not averaged away.', 'craft']],
        writes: [['a review with a verdict\nSHIP / FIX-THEN-SHIP / REWRITE\n+ dissent flagged and quoted\n+ top 3 fixes, 60 seconds each\nnew numbered folder per re-run', 'writeAlt']] },
    ],
  },
  {
    name: 'post-write', status: 'WIP', note: 'distribution · post-type and platform NEVER collapse',
    steps: [
      { title: '1. Split + fit-filter',
        reads: [['the source: an ideas batch, or\na long-form script.md,\ntranscript, or article', 'piece'],
                ['creator-foundation.md\niceberg + Top 3 (the gate)', 'found'],
                ['knowledge/iceberg-and-top-3-\nalignment.md', 'craft']],
        writes: [] },
      { title: '2. Core first, then lock',
        reads: [['voice-profile.md +\nreference-pieces/', 'found'],
                ['knowledge/voice-profile-schema\nvoice-pressure-test', 'craft'],
                ['references/ai-hedging.md\nthe anti-slop pass', 'craft']],
        writes: [['ONE platform-agnostic core.\nLocked with the creator BEFORE\nany platform work, so no\neffort is spent on a piece\nabout to change.', 'write']] },
      { title: '3. Adapt per platform',
        reads: [['knowledge/piece-contract.md\nprovenance wikilinks', 'craft']],
        writes: [['one note per idea:\nLinkedIn argument ·\nInstagram carousel copy +\nvisual brief · IG caption.\nClean ## Publishable blocks.', 'writeAlt']] },
    ],
  },
  {
    name: 'aaios-feedback', status: 'RELEASED', note: 'cross-cutting · available throughout · goes to Billy, not to Claude',
    steps: [
      { title: '1. Reconstruct context silently',
        reads: [['knowledge/feedback-capture-\nmap.md: what to capture\nper skill', 'craft'],
                ['knowledge/feedback-offer.md\nthe proactive offer protocol', 'craft'],
                ['knowledge/feedback-submit.md\nendpoint + payload + curl', 'craft'],
                ['.claude-plugin/plugin.json\nversion', 'craft'],
                ['the determinative vault files\nthe capture map names.\nNEVER held-out quote files.', 'found']],
        writes: [] },
      { title: '2. Local copy, then consent',
        reads: [['at most 2 light questions:\nseverity, what happened vs\nwhat they wanted', 'craft']],
        writes: [['feedback/{date}-{skill}.md\nWRITTEN BEFORE any network\ncall. Record and fallback.', 'writeAlt']] },
      { title: '3. Submit',
        reads: [['mandatory consent gate:\npreviews exactly which real\nfiles will be sent', 'craft']],
        writes: [['submission to the aaios-feedback\nform on peak-tools via a public\nConvex endpoint.\nOn failure: no retry loop,\ngives the form link instead.', 'write']] },
    ],
  },
];

// ================= LAYOUT =================
let Y = 0;
const X0 = 0;

function heading(text, sub, y, size = 60) {
  label(X0, y, 1600, text, size, { align: 'left', chars: 999 });
  if (sub) label(X0, y + size + 8, 1600, sub, 18, { align: 'left', chars: 999, color: '#6b6b6b' });
  return y + size + (sub ? 44 : 20);
}

// ---- Legend ----
Y = heading('Authentic AI OS: the skill system', 'Every skill as a card. Top row = its steps. Middle = what it READS at that step. Bottom = what it WRITES.', Y, 68);
Y += 30;

const legendItems = [
  ['piece', 'Per-video files\npiece.md · brain-dump.md · script.md'],
  ['found', 'Creator data\nfoundation/ · banks/ · voice-profile'],
  ['craft', 'Craft reference (static)\nknowledge/ · references/ · assets/'],
  ['write', 'Writes'],
  ['writeAlt', 'Writes a field the PIPELINE reads\n(the gate that unlocks the next skill)'],
];
let lx = X0;
for (const [kind, text] of legendItems) {
  const h = chip(lx, Y, text, C[kind], { w: 300, chars: 42 });
  lx += 316;
}
Y += 70;

// ---- Per-video pipeline ----
Y += 60;
Y = heading('The per-video pipeline', 'Runs once per video. piece.md is the hub every one of these reads and appends to.', Y, 48);
Y += 60;

for (const s of PIPELINE) {
  const { h } = card(X0, Y, s);
  Y += h + 150;
}

// ---- Orchestrator ----
Y += 40;
Y = heading('The orchestrator', 'Reads state off disk and routes. It never writes content.', Y, 48);
Y += 60;
Y += card(X0, Y, ORCHESTRATOR).h + 150;

// ---- Voice line ----
Y += 40;
Y = heading('The voice line', 'Sits outside the chain. Fires on its own triggers, and from inside the writing skills.', Y, 48);
Y += 60;
for (const s of VOICE) { Y += card(X0, Y, s).h + 150; }

// ---- Setup + banks ----
Y += 40;
Y = heading('One-time setup: identity and banks', 'Stages 0-3. Done once, topped up over time. Everything above depends on these files existing.', Y, 48);
Y += 60;
for (const s of SETUP) { Y += card(X0, Y, s).h + 150; }

// ---- WIP lines ----
Y += 40;
Y = heading('Not shipped yet: the audience line, distribution, and feedback', 'aud-* builds synthetic avatars from real audience data, then panels them. post-* turns finished work into platform posts. aaios-feedback runs across everything.', Y, 48);
Y += 60;
for (const s of WIP) { Y += card(X0, Y, s).h + 150; }

// ================= piece.md FIELD LEDGER =================
Y += 60;
Y = heading('piece.md: the field ledger', 'Who writes each field, and who actually reads it. A field with no reader does not get written.', Y, 48);
Y += 70;

const LEDGER = [
  ['slug · created · status: ideating', 'vid-intake', 'vid-pipeline (is there a piece at all)'],
  ['anchor  (full outlier receipt)', 'vid-intake, from the vid-ideas seed packet', 'vid-title (the receipt it presents)'],
  ['pillar · iceberg_aligned · alignment_note', 'vid-intake', 'vid-structure, vid-ending. Unset iceberg_aligned = intake never finished'],
  ['frame', 'vid-framing', 'vid-title, vid-structure, vid-ending, vid-pressure-test, vid-pipeline (route gate)'],
  ['core_payoff', 'vid-framing', 'vid-title, vid-structure'],
  ['format', 'vid-framing', 'vid-thumbnail, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test: picks the format planner'],
  ['goal   (sales | emails | views)', 'vid-framing', 'vid-thumbnail, vid-structure, vid-ending (CTA shape), vid-pressure-test (rubric weights)'],
  ['voice_context', 'vid-framing (or post-write)', 'vid-intro, vid-segment, vid-ending, vid-voice-audit: picks WHICH reference-piece loads'],
  ['title', 'vid-title', 'vid-thumbnail, vid-intro (Top 3 viewer questions), vid-pipeline'],
  ['thumbnail_text · thumbnail_shape', 'vid-thumbnail', 'vid-intro (the questions derive from title + thumbnail), vid-pipeline'],
  ['segment_purposes · tension_plan', 'vid-structure', 'vid-segment, vid-pipeline (compares length to segments_completed)'],
  ['status: drafting', 'vid-structure', 'vid-pipeline'],
  ['intro_locked · viewer_questions', 'vid-intro', 'vid-ending (Setup callback), vid-pipeline'],
  ['segments_completed', 'vid-segment (appends one per run)', 'vid-pipeline: length vs segment_purposes is the body-progress counter'],
  ['stories_used · proofs_used · metaphors_used\ntestimonials_used · frameworks_used', 'vid-intro, vid-segment, vid-ending', 'vid-pressure-test (used-material traceability). Bank entry gets the backlink.'],
  ['ending_locked · next_video', 'vid-ending', 'vid-pipeline'],
  ['pressure_test_audit · status: filming-ready', 'vid-pressure-test', 'vid-pipeline: THE terminal signal'],
  ['last_updated', 'EVERY skill that writes the file', '(bookkeeping)'],
];

const LW = [430, 340, 700];
const lhead = ['Field', 'Written by', 'Read by'];
let ly = Y;
let lxx = X0;
lhead.forEach((h, i) => {
  rect(lxx, ly, LW[i], 46, C.bandStep, { roughness: 0 });
  label(lxx + 12, ly + 12, LW[i] - 24, h, 20, { align: 'left', chars: 999 });
  lxx += LW[i] + 6;
});
ly += 52;

for (const row of LEDGER) {
  const hh = Math.max(
    wrap(row[0], 46).length,
    wrap(row[1], 36).length,
    wrap(row[2], 74).length
  ) * 17 + 20;
  lxx = X0;
  const bgs = [C.white, C.write, C.piece];
  row.forEach((cell, i) => {
    rect(lxx, ly, LW[i], hh, bgs[i], { roughness: 0 });
    const lines = wrap(cell, [46, 36, 74][i]);
    label(lxx + 12, ly + (hh - lines.length * 15) / 2, LW[i] - 24, lines.join('\n'), FS, { align: 'left', chars: 999 });
    lxx += LW[i] + 6;
  });
  ly += hh + 6;
}

// ================= PUSH =================
(async () => {
  await fetch(`${API}/elements`, { method: 'DELETE' }).catch(() => {});
  // clear via the canvas route if DELETE isn't supported
  const CHUNK = 60;
  let ok = 0, fail = 0;
  for (let i = 0; i < els.length; i += CHUNK) {
    const batch = els.slice(i, i + CHUNK);
    const res = await fetch(`${API}/elements/batch`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ elements: batch }),
    });
    const j = await res.json();
    if (j.success) ok += batch.length; else { fail += batch.length; console.log('FAIL', JSON.stringify(j).slice(0, 300)); }
  }
  console.log(`elements: ${els.length}  ok: ${ok}  fail: ${fail}`);
  console.log(`canvas height: ${Math.round(ly)}`);
})();
