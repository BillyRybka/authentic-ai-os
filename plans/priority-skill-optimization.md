# Priority Skill Optimization Push

Date: 2026-07-21. Branch: `dag`. Checkpoint before work: `c78dd50`.

## Goal

Make the four priority skills (vid-intro, vid-segment, vid-ending, vid-capture) read like
domain experts instead of process docs: principles and worked great-vs-weak examples inline,
plumbing cut. Close the attention-craft gap. Leave the knowledge layer deduplicated,
correctly placed (multi-skill = `knowledge/`, single-skill = skill-local `references/`),
and fully wired, with Tier A tests proving the four skills before and after.

## Locked decisions (from owner, 2026-07-21)

1. Scope C: four skills + knowledge cleanup + wiring fixes + maps, craft work first.
2. Expert bar: each SKILL.md teaches judgment (principles + worked examples inline) AND
   stays adaptive: skills read the creator's own vault files (foundation, banks, voice
   profile), so client edits to those files change behavior. Never hardcode one creator.
3. vid-capture identity: capture stories/metaphors/proof/testimonials/frameworks into the
   banks, AND carry the bar for what makes material script-worthy at capture time.
4. New shared `knowledge/attention-craft.md` (pattern interrupts, pacing as felt time,
   mid-segment re-engagement), consumed by vid-intro, vid-segment, vid-ending.
5. Tests first: Tier A suites for all four priority skills, locked before any rewrite.
6. Dead banks: rewire writing skills to read vault `banks/hook-bank.md` and
   `banks/transition-bank.md` in addition to plugin `hook-patterns.md` /
   `transition-patterns.md` (creator-grown patterns = adaptability). Fix creator-setup
   seed rows to match. (Owner may veto; fallback is cutting the seeding.)
7. Parked for later: skyscraper comment mining, retention-graph feedback loop
   (vid-review), thumbnail visual concept pass.
8. Course material: mine, never ship. No references to the source course, its author, or
   `business-os` paths in any repo file. Absorb teachings under workspace terminology
   (parable/principle, Pivot/Gap/Bridge). Workers may read the source path for depth only.

## Craft gaps to close (from audit)

- attention-craft layer missing everywhere (pattern interrupts, pacing, re-engagement).
- vid-segment: NEI filter (New/Easy/Inspiring) absent from the edit pass; curiosity-spiking
  payoff unnamed; Minimum Viable Story untaught; payoff timing not calibrated to avatar.
- vid-intro: no "what makes a hook land" principles (curiosity gap, specificity as trust,
  recognition test); missing redundancy rule (delete Problem/Result when the hook carries
  it); first-shot expectation matching orphaned in a knowledge file; 18-row load table;
  duplicated Hard rules section.
- vid-ending: hard filters restated (reference teaches them better); pseudo-regex and
  dangling pointers in `references/ending-anti-patterns.md`; Gap anatomy never named as
  families; template-slot filling is ceremony.
- vid-capture: five repeated save choreographies (~50 lines); contract/failure/reference
  sections restate vault-integration; Stage F packet contract is API docs; per-stage craft
  principles missing (emotion-stores-memory, twist-or-receipt, everyday-recognition test,
  receipt-the-avatar-can-simulate).

## Stages

- **Stage 1 — Tier A suites (this push, parallel):** build `tests/skills/{vid-intro,
  vid-segment, vid-ending, vid-capture}/` per `tests/README.md`, modeled on existing
  suites, using `tests/lib/` checks and `tests/corpus/seeds.json`. LOCKED once built:
  no edits to eval.py/rubric.md during the rewrite loop. Do not modify `tests/lib/` or
  existing suites.
- **Stage 2 — Rewrites (one worker per skill, parallel after Stage 1 gate):** rewrite the
  four SKILL.md files to the expert bar; create `knowledge/attention-craft.md`; relocate
  single-consumer knowledge files into skill `references/` (hook-patterns → vid-intro,
  visual-demo-builder → vid-segment, metaphor-builder/proof-capture-guide/
  testimonial-capture → vid-capture, format-index → vid-framing); rewire vault banks per
  decision 6. Each worker re-runs its skill's Tier A suite until green.
- **Stage 3 — Knowledge cleanup:** cut the 13 dead files (5 orphaned bank schemas,
  hook-bank-template, transition-bank-template, gift-framework, thumbnail trio,
  ai-hedging/common-english/synthetic-audience parked with their WIP families); slim
  vault-integration.md (park ~180 lines of aud-family schemas); make format-planners the
  single per-format authority (trim restatements in intro-architecture and
  script-tension-architecture).
- **Stage 4 — Wiring fixes:** vid-structure → vid-intro handoff text; vid-ideas into
  vid-pipeline Step 2 + stale "(future)"/"SCRIPT phase" lines; resolve phantom `brand.md`
  references; vid-ideas description under 1024 chars; vid-research/aaios-feedback
  description trims toward 240–490; vid-thumbnail/vid-segment next-skill pointers;
  shipped-file staleness bugs (vid-credibility `vid-script`, vid-research Mode-1
  voice-capture assumption + API-key path, root CLAUDE.md `_guide.md`).
- **Stage 5 — Verification + maps:** regenerate `documents/skill-knowledge-map.md` and
  `documents/SYSTEM-MAP.md`; repo-wide greps (old names, "in development", brand.md,
  dead knowledge files); Vale on all touched files (zero errors); all Tier A suites run;
  em-dash sweep; final report.

## Standing constraints (every stage)

- No em-dashes/en-dashes; plain spoken language; wikilinks for internal references;
  frontmatter per `knowledge/vault-integration.md`.
- Skill descriptions: 1024-char hard cap, target 240–490.
- One skill, one job; load-bearing logic inline in SKILL.md, references for depth only.
- Every output field needs a named consumer; grep the Load sections, not descriptions.
- Never fabricate creator material; ask before scanning; auto-save and report.
- Nothing dev-only (WORKING-NOTES, DEBUG-TRACE, plans, tests) enters
  `plugins/authentic-ai-os/`.
- Line endings: LF in anything that may ship.
