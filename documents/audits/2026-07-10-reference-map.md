# Reference map, 2026-07-10

Map 1 of the Phase 1 sweep (build-plan re-audit). Mechanical scan of every path-like reference in 164 markdown files across `.claude/skills/`, `.claude/skills-wip/`, `plugins/authentic-ai-os/`, and `knowledge/`. 1,182 references extracted and resolved against the repo. Every finding below was hand-verified after the scan; the scan's raw JSON lives in the session scratchpad, regenerate with the same script if needed.

Classification rules: paths under `foundation/`, `banks/`, `content/`, `raw/`, `People/`, `audience/` are creator-workspace outputs and are EXPECTED to not exist in this repo. "Broken" means a pointer that cannot resolve anywhere it will run.

## Confirmed findings, ranked

### F1. Framework bank split: writer and readers use different folders (critical)

- vid-capture WRITES `banks/frameworks/{slug}.md` ([SKILL.md:32](../../.claude/skills/vid-capture/SKILL.md), :65, :173, :176)
- vid-segment READS `banks/framework-bank/*.md` ([SKILL.md:38](../../.claude/skills/vid-segment/SKILL.md), :72, :101, :269), as do vid-pressure-test ([SKILL.md:34](../../.claude/skills/vid-pressure-test/SKILL.md), reviewer-source-traceability.md:35) and vid-segment/references/framework-shapes.md:14

Outcome: every framework captured through vid-capture Stage F lands where no consumer looks. Silent data loss, no error surfaces.

### F2. `Context/brand.md` is load-bearing in three skills but nothing in the product creates it (critical for distribution)

Runtime references: vid-ending [SKILL.md:31](../../.claude/skills/vid-ending/SKILL.md) (voice fallback), vid-pressure-test SKILL.md:29/:56/:264 + references/reviewer-ai-slop.md:28, vid-voice-audit SKILL.md:41 (listed as a hard requirement)/:57/:93/:181 + references/voice-fault-rubric.md:19/:28.

The file exists only in Billy's business-os vault. creator-setup does not scaffold it, no skill produces it, vault-integration does not define it. Any other creator hits a missing hard requirement; vid-ending's fallback path lands on a file that does not exist.

### F3. Stale `.claude/skills-wip/` pointers to skills that moved

vid-voice-audit, vid-voice-capture, and vid-ideas now live in `.claude/skills/`, but:
- vid-pressure-test SKILL.md:256 points at `.claude/skills-wip/vid-voice-audit/SKILL.md`
- vid-voice-update SKILL.md:169-170 points at `.claude/skills-wip/vid-voice-audit` and `.claude/skills-wip/vid-voice-capture`
- knowledge/vault-integration.md:436 points at `.claude/skills-wip/vid-ideas/assets/ideas-backlog-template.md`

### F4. Shared knowledge files point into skills' private references/ folders (boundary violations, wrong-path as written)

The targets exist, but the paths only resolve from inside the owning skill, and the placement rule says no file reaches into another skill's references/:
- knowledge/script-tension-architecture.md:12 → `references/parable-principle-shapes.md` (actual home: vid-segment/references/)
- knowledge/parable-decision-matrix.md:247 → `vid-segment/references/framework-shapes.md`
- knowledge/hook-bank-template.md:154 → `references/hook-type-selection-flow.md` (actual home: vid-intro/references/)

### F5. `plugin.js` referenced, absent from the repo

`${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.js` is referenced by knowledge/update-check.md:21, knowledge/feedback-submit.md:42, and plugins/.../aaios-feedback/SKILL.md:35. The plugin's `.claude-plugin/` contains only plugin.json. VERIFY at next release whether release.ps1 or the publish repo supplies plugin.js; if not, the update-check and feedback flows read a file that does not exist.

### F6. Missing-prefix shorthand paths in live skill files (minor)

- vid-pressure-test SKILL.md:103: `format-planners/{format}.md` (elsewhere the same skill uses the full `knowledge/` prefix)
- vid-intro/references/credibility-line-weaving.md:124: `format-planners/case-study.md`

Resolve fine when the model infers, but they are the pattern that becomes silent failure after plugin packaging.

## Orphan knowledge files (nothing loads them at runtime)

| File | Lines | Verified status |
|---|---|---|
| knowledge/story-bank-schema.md | 62 | Orphan. SYSTEM-MAP.md:316 says these were staged for vid-capture, which loads the capture guides instead. Parked decision, now stale. |
| knowledge/metaphor-bank-schema.md | 67 | Same. |
| knowledge/testimonial-bank-schema.md | 74 | Same. |
| knowledge/packaging-bank-schema.md | 135 | Same. |
| knowledge/framework-bank-schema.md | 199 | Same (documents/skill-knowledge-map.md:253 lists it as orphan too). |
| knowledge/hook-bank-template.md | 158 | NOT a true orphan: creator-setup seeds it into `banks/hook-bank.md` via its manifest (creator-setup SKILL.md:93/:213). It is a write-target template, not a load reference. |
| knowledge/transition-bank-template.md | 112 | Same as hook-bank-template. |

Note: proof-bank-schema.md is NOT orphaned (loaded by shipped vid-credibility, see SYSTEM-MAP.md:91).

## Naming inconsistencies spotted in workspace paths

- `banks/frameworks/` vs `banks/framework-bank/` (finding F1)
- `content/ideas/content-ideas.md` (vid-ideas area) vs `content/ideas-backlog.md` (vault-integration): two different idea-file homes referenced. Resolve in the D3/D4 memos.

## Expected classes (no action, documented so nobody re-flags them)

- **WORKING-NOTES.md citations** to `C:/Users/billr/projects/business-os/resources/references/...` (the source curriculum) and other absolute dev paths: dev-only provenance records, deliberately outside the repo. They must never ship, but they are not broken references. ~180 of the 235 raw "missing" hits are this class.
- **Creator-workspace paths** (`foundation/*`, `banks/*`, `content/pieces/{slug}/*`, `raw/*`, `audience/*`): 425 references, created at runtime by skills or creator-setup. Correct by design.
- **`knowledge/X.md` placeholders** in the path-resolution preamble several skills carry: literal placeholder, not a reference.
- **TARGET/... paths** in creator-setup: documentation notation for "the creator's chosen folder."

## Repo layout facts the build plan does not reflect

- Dev `.claude/skills/` (15 skills) and shipped `plugins/authentic-ai-os/skills/` (9 skills) are DISJOINT sets. The foundation interview skills exist only in the plugin tree; the pipeline skills exist only in the dev tree.
- `.claude/skills-wip/` holds aud-* (4) plus `post-write`, a skill the build plan does not mention at all.
- The plugin tree carries no knowledge/ folder on this branch; `scripts/release.ps1:83-117` auto-relocates knowledge files referenced by shipped skills at release time.
- Prior mapping docs exist and partially overlap this sweep: `documents/skill-knowledge-map.md` (2026-06-16) and `documents/SYSTEM-MAP.md`. The Phase 3 doc rework must state which maps are living and which are superseded.
