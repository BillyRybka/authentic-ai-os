# Skill-to-Knowledge Dependency Map

The packaging contract for Authentic AI OS. When a skill ships to the live plugin, every `knowledge/` file it references must ship with it. A skill's own `references/` and `assets/` are packaged inside the skill folder, so they travel automatically. But `knowledge/` files live outside the skill and are the thing that gets forgotten.

This map answers one question: **for any skill, exactly which `knowledge/` files must be in the plugin for it to work.**

Regenerated 2026-07-21 by grepping every `SKILL.md`, `references/*.md`, `assets/*.md`, and `manifest.md` across all three skill roots (`plugins/authentic-ai-os/skills/`, `.claude/skills/`, `.claude/skills-wip/`), then cross-checking every referenced path against the `knowledge/` directory on disk. Dev-only `WORKING-NOTES.md` files are excluded from the scan.

**Important:** transitive references count. If a skill's packaged `references/` or `assets/` file points at a `knowledge/` file, that knowledge file is required too. Those cases are marked `(via references/)` or `(via assets/)` below. One refinement: when a references file names a `knowledge/` path only to say a *different* skill loads it later, that is a pointer, not a load, and it does not count. The one current case is flagged on vid-framing.

**Three tiers, by packaging meaning:**

- `RELEASED` lives in `plugins/authentic-ai-os/skills/`. Ships to creators. Dependency lists verified.
- `STAGED` lives in `.claude/skills/`. Works in this repo, not yet released. Accurate as of this scan, not yet packaged.
- `WIP` lives in `.claude/skills-wip/`. Not ready. Lists accurate as of this scan but unverified, because the skills are still changing. Re-run this map before moving any of them.

The skills split into three families: `vid-*` (the video pipeline), `aud-*` (the synthetic-audience pipeline), and `post-*` (distribution into platform posts).

---

## 1. Forward map: skill to required knowledge files

### RELEASED skills (9)

**creator-setup** `RELEASED`
- `knowledge/update-check.md` (mandatory update-check pre-flight)
- `knowledge/vault-integration.md`
- **Carries two seed rows for the writing-skill banks.** The manifest lists `hook-bank-template.md` into `banks/hook-bank.md` and `transition-bank-template.md` into `banks/transition-bank.md` as seed-class rows (idempotent, copy-if-absent). The rows sit in the manifest's pending table today and go live when `vid-intro`, `vid-segment`, and `vid-ending` ship. Both templates must ship with the plugin so the seeds can fire. See section 6.

**foundation** `RELEASED`
- `knowledge/feedback-offer.md` (the end-of-journey feedback offer at Step 5)
- `knowledge/update-check.md` (update-check pre-flight)

**vid-avatar** `RELEASED`
- `knowledge/creator-foundation-template.md`
- `knowledge/interview-posture.md`
- `knowledge/update-check.md`
- `knowledge/vault-integration.md`

**vid-positioning** `RELEASED`
- `knowledge/interview-posture.md`
- `knowledge/update-check.md`
- `knowledge/vault-integration.md`

**vid-pillars** `RELEASED`
- `knowledge/interview-posture.md`
- `knowledge/update-check.md`
- `knowledge/vault-integration.md`

**vid-credibility** `RELEASED`
- `knowledge/interview-posture.md`
- `knowledge/proof-bank-schema.md`
- `knowledge/update-check.md`
- `knowledge/vault-integration.md`, `knowledge/bank-contract.md` (the leftover-wins proof entries)
- Note: the proof bank this skill seeds is pulled downstream by `vid-intro`, `vid-segment`, `vid-ending`, and `vid-structure` (per the downstream-consumers line in the skill itself).

**vid-backstory** `RELEASED`
- `knowledge/interview-posture.md`
- `knowledge/update-check.md`
- `knowledge/vault-integration.md`

**vid-research** `RELEASED`
- `knowledge/format-rotation-guide.md`
- `knowledge/interview-posture.md`
- `knowledge/outlier-identification-rules.md`
- `knowledge/packaging-system-template.md`
- `knowledge/theory-of-one-curation.md`
- `knowledge/three-circle-research.md`
- `knowledge/thumbnail-text-patterns.md`
- `knowledge/update-check.md` (update-check pre-flight, added on graduation)
- Outputs bank files in the creator's vault: `banks/pattern-bank.md`, `banks/title-bank.md`, `banks/power-words-bank.md`, plus `foundation/packaging-system.md`. Those are vault content, not knowledge dependencies.

**aaios-feedback** `RELEASED`
- `knowledge/feedback-capture-map.md`
- `knowledge/feedback-offer.md`
- `knowledge/feedback-submit.md`
- `knowledge/vault-integration.md`
- Note: aaios-feedback does **not** load the `update-check.md` pre-flight that the other eight released skills run. Confirmed by grep, flagged in section 8.

### STAGED skills (15)

**vid-ideas** `STAGED`
- `knowledge/iceberg-and-top-3-alignment.md`
- `knowledge/theory-of-one-curation.md`
- `knowledge/update-check.md` (pre-flight)
- Note: vid-ideas no longer loads `vault-integration.md` (the prior map listed it). Confirmed by grep.

**vid-intake** `STAGED`
- `knowledge/story-capture-guide.md`
- `knowledge/update-check.md` (pre-flight)
- `knowledge/piece-contract.md`

**vid-capture** `STAGED`
- `knowledge/framework-builder.md`
- `knowledge/story-capture-guide.md`
- `knowledge/bank-contract.md`
- Skill-local `references/` (moved out of `knowledge/`; vid-capture is their only consumer): `metaphor-builder.md`, `proof-capture-guide.md`, `testimonial-capture.md`

**vid-framing** `STAGED`
- `knowledge/piece-contract.md`
- Skill-local `references/`: `format-index.md` (moved out of `knowledge/`; vid-framing is its only consumer), `stake-finder.md`, `framing-conversation-examples.md`
- Note: `references/format-index.md` names `knowledge/format-planners/{format}.md` only to say vid-structure loads it later. A pointer, not a load; vid-framing does not consume the planners. As of the 2026-07-27 narrowing, vid-framing no longer loads `BENS-framework.md` or `banks/pattern-bank.md` (packaging and receipts are vid-title's job), and `reframe-toolkit.md` plus `angle-anchor-rules.md` moved into `vid-title/references/`. It also no longer loads `audience-temperature-model.md`, `outlier-identification-rules.md`, or `three-circle-research.md`.

**vid-title** `STAGED`
- `knowledge/BENS-framework.md`
- Skill-local `references/`: `title-filters.md`, `angle-anchor-rules.md`, `reframe-toolkit.md` (the last two moved in from vid-framing on 2026-07-27)
- Note: no longer loads `thumbnail-text-patterns.md` (the prior map listed it). The cross-skill pointer into vid-framing's folder is gone; every reference vid-title makes is now skill-local, so it packages standalone.

**vid-thumbnail** `STAGED`
- `knowledge/thumbnail-text-patterns.md` (the one craft reference: the 5 patterns, anti-patterns, pairing rules, and the examples library, now folded into this file)
- Note: four thumbnail craft files were deleted from `knowledge/` (`gift-framework.md`, `thumbnail-composition-guide.md`, `thumbnail-examples-library.md`, `thumbnail-strategy-menu.md`); `thumbnail-text-patterns.md` absorbed what the skill still uses. vid-thumbnail no longer loads `BENS-framework.md` or `vault-integration.md` either. Confirmed by grep.

**vid-structure** `STAGED`
- `knowledge/parable-decision-matrix.md`
- `knowledge/script-tension-architecture.md`
- `knowledge/format-planners/*.md`: all 7
- Note: vid-structure does **not** load `vault-integration.md`. Confirmed by grep. It also no longer loads `framework-builder.md` (the prior map had it via `assets/script-skeleton-template.md`) or `voice-profile-schema.md`.

**vid-intro** `STAGED`
- `knowledge/attention-craft.md`
- `knowledge/intro-architecture.md`
- `knowledge/transition-patterns.md`
- `knowledge/bank-contract.md`
- `knowledge/visual-proof-callouts.md`
- `knowledge/voice-pressure-test.md`
- `knowledge/voice-rhythm.md`
- `knowledge/metaphor-integration.md` (conditional: only when a hook runs on metaphor)
- `knowledge/proof-placement-rules.md` (conditional: only when the credibility weave pulls bank material)
- `knowledge/story-pulling-criteria.md` (conditional, same trigger)
- `knowledge/format-planners/*.md`: all 7
- Skill-local `references/`: `hook-patterns.md` (moved out of `knowledge/`; vid-intro is its only consumer)
- Soft-loads `banks/hook-bank.md` when the vault has one (creator-owned bank, seeded by creator-setup from `hook-bank-template.md`; missing is fine). Not a knowledge dependency.

**vid-segment** `STAGED`
- `knowledge/attention-craft.md`
- `knowledge/framework-builder.md`
- `knowledge/parable-decision-matrix.md`
- `knowledge/script-tension-architecture.md`
- `knowledge/transition-patterns.md`
- `knowledge/bank-contract.md`
- `knowledge/visual-proof-callouts.md`
- `knowledge/voice-pressure-test.md`
- `knowledge/voice-rhythm.md`
- `knowledge/format-planners/*.md`: all 7
- Skill-local `references/`: `visual-demo-builder.md` (moved out of `knowledge/`; vid-segment is its only consumer), `parable-principle-shapes.md`
- Soft-loads `banks/transition-bank.md` when the vault has one (seeded by creator-setup from `transition-bank-template.md`; missing is fine). Not a knowledge dependency.
- Note: `emotion-brick-decision-matrix.md` is renamed to `parable-decision-matrix.md`. The old name no longer exists anywhere.

**vid-ending** `STAGED`
- `knowledge/attention-craft.md`
- `knowledge/transition-patterns.md`
- `knowledge/bank-contract.md`
- `knowledge/voice-pressure-test.md`
- `knowledge/voice-rhythm.md`
- `knowledge/format-planners/*.md`: all 7
- Conditional (rare, only when the close pulls a bank block): `knowledge/story-pulling-criteria.md`, `knowledge/proof-placement-rules.md`, `knowledge/metaphor-integration.md`, `knowledge/parable-decision-matrix.md`
- Soft-loads `banks/transition-bank.md` when the vault has one (same seed as vid-segment; missing is fine). Not a knowledge dependency.

**vid-pressure-test** `STAGED`
- `knowledge/script-tension-architecture.md`
- `knowledge/attention-craft.md` (deferred: loads only when the Phase 2 retention-logic reviewer fires)
- `knowledge/format-planners/*.md`: all 7 (same deferred load)
- `knowledge/transition-patterns.md` (via `references/reviewer-ai-slop.md`)
- `knowledge/intro-architecture.md` (via `references/reviewer-ai-slop.md`)
- `knowledge/audience-temperature-model.md` (via `references/reviewer-retention-logic.md`)
- `knowledge/voice-profile-schema.md`
- Note: the planners are back. The prior map said vid-pressure-test no longer loaded `format-planners/`; the current build loads them deferred, at the Phase 2 retention reviewer only. Invokes `vid-voice-audit` as its voice reviewer (see that skill's deps).

**vid-voice-capture** `STAGED`
- `knowledge/interview-posture.md`
- `knowledge/vault-integration.md`
- `knowledge/voice-extraction-methods.md`
- `knowledge/voice-pressure-test.md`
- `knowledge/voice-profile-schema.md`
- `knowledge/voice-rhythm.md`

**vid-voice-audit** `STAGED`
- `knowledge/voice-pressure-test.md`
- `knowledge/voice-profile-schema.md`
- `knowledge/voice-rhythm.md`
- Note: there is no `brand.md` anywhere in the system. The voice authorities are the `voice-profile.md` refusals (the creator's banned words and required swaps) plus the Vale house rules.

**vid-voice-update** `STAGED`
- `knowledge/voice-profile-schema.md`

**vid-pipeline** `STAGED` (orchestrator)
- `knowledge/update-check.md` (pre-flight only)
- Loads no other knowledge files. It reads each piece's `piece.md` plus sibling-file presence and routes to the next writing skill, with a blank-on-ideas branch that invokes `vid-ideas` first. Pure router; the sub-skills own all knowledge-file loading.

### WIP skills (re-scan before shipping)

#### Audience family (`aud-*`)

All four `aud-*` skills load two parked files straight from `.claude/skills-wip/`: `synthetic-audience-method.md` (method, thresholds, banned vocabulary) and `vault-integration-aud-schemas.md` (the audience-family frontmatter schemas, extracted from `knowledge/vault-integration.md`). Neither is a `knowledge/` file, so neither ships while the family is WIP.

**aud-intake** `WIP`
- `knowledge/bank-contract.md` (the person-stub rule)
- Parked: `.claude/skills-wip/synthetic-audience-method.md`, `.claude/skills-wip/vault-integration-aud-schemas.md`

**aud-avatar-build** `WIP`
- No `knowledge/` files.
- Parked: `.claude/skills-wip/synthetic-audience-method.md`, `.claude/skills-wip/vault-integration-aud-schemas.md`

**aud-validate** `WIP`
- No `knowledge/` files.
- Parked: `.claude/skills-wip/synthetic-audience-method.md`, `.claude/skills-wip/vault-integration-aud-schemas.md`
- Skill-local `references/`: `common-english.txt` (the vocabulary-leak word list, moved out of `knowledge/`; aud-validate is its only consumer)

**aud-review** `WIP`
- No `knowledge/` files.
- Parked: `.claude/skills-wip/synthetic-audience-method.md`, `.claude/skills-wip/vault-integration-aud-schemas.md`

#### Distribution family (`post-*`)

**post-write** `WIP`
- `knowledge/iceberg-and-top-3-alignment.md`
- `knowledge/vault-integration.md`, `knowledge/piece-contract.md`, `knowledge/bank-contract.md`
- `knowledge/voice-pressure-test.md`
- `knowledge/voice-profile-schema.md`
- Skill-local `references/`: `ai-hedging.md` (moved out of `knowledge/`; post-write is its only consumer)

---

## 2. Reverse map: knowledge file to consuming skills

Use this when editing or renaming a knowledge file: it tells you every skill that breaks.

| Knowledge file | Consumed by |
|----------------|-------------|
| `attention-craft.md` | vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `audience-temperature-model.md` | vid-pressure-test (via references/) |
| `bank-contract.md` | vid-capture, vid-credibility, vid-intro, vid-segment, vid-ending, aud-intake, post-write |
| `BENS-framework.md` | vid-framing, vid-title |
| `creator-foundation-template.md` | vid-avatar |
| `feedback-capture-map.md` | aaios-feedback |
| `feedback-offer.md` | aaios-feedback, foundation |
| `feedback-submit.md` | aaios-feedback |
| `format-planners/case-study.md` | vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/deep-dive.md` | vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/interview.md` | vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/listicle.md` | vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/news.md` | vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/roast.md` | vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/short-process.md` | vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-rotation-guide.md` | vid-research |
| `framework-builder.md` | vid-capture, vid-segment |
| `hook-bank-template.md` | creator-setup (pending seed row into `banks/hook-bank.md`, then soft-loaded at runtime by vid-intro) |
| `iceberg-and-top-3-alignment.md` | vid-ideas, post-write |
| `interview-posture.md` | vid-avatar, vid-positioning, vid-pillars, vid-credibility, vid-backstory, vid-research, vid-voice-capture |
| `intro-architecture.md` | vid-intro, vid-pressure-test (via references/) |
| `metaphor-integration.md` | vid-intro (conditional), vid-ending (conditional, rare) |
| `outlier-identification-rules.md` | vid-research |
| `packaging-system-template.md` | vid-research |
| `parable-decision-matrix.md` | vid-structure, vid-segment, vid-ending (conditional, rare) |
| `piece-contract.md` | vid-intake, vid-framing, post-write |
| `proof-bank-schema.md` | vid-credibility |
| `proof-placement-rules.md` | vid-intro (conditional), vid-ending (conditional, rare) |
| `script-tension-architecture.md` | vid-structure, vid-segment, vid-pressure-test |
| `story-capture-guide.md` | vid-intake, vid-capture |
| `story-pulling-criteria.md` | vid-intro (conditional), vid-ending (conditional, rare) |
| `theory-of-one-curation.md` | vid-ideas, vid-research |
| `three-circle-research.md` | vid-research |
| `thumbnail-text-patterns.md` | vid-research, vid-thumbnail |
| `transition-bank-template.md` | creator-setup (pending seed row into `banks/transition-bank.md`, then soft-loaded at runtime by vid-segment, vid-ending) |
| `transition-patterns.md` | vid-intro, vid-segment, vid-ending, vid-pressure-test (via references/) |
| `update-check.md` | creator-setup, foundation, vid-avatar, vid-positioning, vid-pillars, vid-credibility, vid-backstory, vid-research, vid-ideas, vid-intake, vid-pipeline |
| `vault-integration.md` | aaios-feedback, creator-setup, vid-avatar, vid-positioning, vid-pillars, vid-credibility, vid-backstory, vid-voice-capture, post-write |
| `visual-proof-callouts.md` | vid-intro, vid-segment |
| `voice-extraction-methods.md` | vid-voice-capture |
| `voice-pressure-test.md` | vid-intro, vid-segment, vid-ending, vid-voice-capture, vid-voice-audit, post-write |
| `voice-profile-schema.md` | vid-pressure-test, vid-voice-capture, vid-voice-audit, vid-voice-update, post-write |
| `voice-rhythm.md` | vid-intro, vid-segment, vid-ending, vid-voice-capture, vid-voice-audit |

The 7 `format-planners/` files are always loaded one at a time (`{format}.md` matched to the video's format), but any of the 7 can be needed, so all 7 must ship with any consuming skill. For vid-pressure-test the load is deferred to the Phase 2 retention reviewer, but all 7 still have to ship.

Files that left `knowledge/` since the prior map, and where they went:

| Former knowledge file | Where it is now |
|-----------------------|-----------------|
| `hook-patterns.md` | `.claude/skills/vid-intro/references/hook-patterns.md` |
| `visual-demo-builder.md` | `.claude/skills/vid-segment/references/visual-demo-builder.md` |
| `format-index.md` | `.claude/skills/vid-framing/references/format-index.md` |
| `metaphor-builder.md`, `proof-capture-guide.md`, `testimonial-capture.md` | `.claude/skills/vid-capture/references/` (moved in an earlier push, restated for completeness) |
| `ai-hedging.md` | `.claude/skills-wip/post-write/references/ai-hedging.md` |
| `common-english.txt` | `.claude/skills-wip/aud-validate/references/common-english.txt` |
| `synthetic-audience-method.md` | `.claude/skills-wip/synthetic-audience-method.md` (parked with the WIP aud-* skills) |
| audience-family schemas (never a standalone file) | extracted from `vault-integration.md` into `.claude/skills-wip/vault-integration-aud-schemas.md` |
| `emotion-brick-decision-matrix.md` | renamed to `knowledge/parable-decision-matrix.md` |
| `framework-bank-schema.md`, `metaphor-bank-schema.md`, `packaging-bank-schema.md`, `story-bank-schema.md`, `testimonial-bank-schema.md` | deleted (vid-capture writes entries from its own `assets/` templates) |
| `gift-framework.md`, `thumbnail-composition-guide.md`, `thumbnail-examples-library.md`, `thumbnail-strategy-menu.md` | deleted (absorbed into `knowledge/thumbnail-text-patterns.md`) |

---

## 3. Orphan list: knowledge files with no consumer

**None.** Every file in `knowledge/` has at least one consumer. The five bank-schema files the prior map tracked as orphans are deleted: `vid-capture` writes bank entries from its own `assets/*-entry-template.md` templates, so the schemas never gained a consumer. The one bank-schema that ships, `proof-bank-schema.md`, is loaded by vid-credibility.

---

## 4. Broken-reference list: referenced files that don't exist

**None.** Every `knowledge/` path referenced by any skill resolves to a file on disk.

Watch items that look like broken references but are not:

- The string `knowledge/X.md` appears in many SKILL.md files. It is **not a reference**. It is a documentation line explaining how to resolve `knowledge/` paths at runtime (`${CLAUDE_PLUGIN_ROOT}/knowledge/` when installed, repo-relative in dev). The `X` is a literal placeholder. Ignore it.
- The vault banks `banks/hook-bank.md` and `banks/transition-bank.md` are soft-loads: vid-intro, vid-segment, and vid-ending use them when present and run fine without. creator-setup's manifest carries the seed rows (pending table) that copy `hook-bank-template.md` and `transition-bank-template.md` into the vault once the writing skills ship.
- `references/format-index.md` (vid-framing) names `knowledge/format-planners/{format}.md` only to say vid-structure loads it later. A pointer, not a load.

---

## 5. Per-skill packaging checklist

When you ship a skill, confirm every box. The skill's own `SKILL.md`, `references/`, and `assets/` ship inside the skill folder automatically. These checklists are only the **external `knowledge/` files** that must also be present in the plugin. Counts treat `format-planners/` as 7, and conditional loads count (the plugin cannot predict which fire).

### RELEASED skills

- [ ] **creator-setup**: update-check, vault-integration, plus 2 seed templates (hook-bank-template, transition-bank-template) (4)
- [ ] **foundation**: feedback-offer, update-check (2)
- [ ] **vid-avatar**: creator-foundation-template, interview-posture, update-check, vault-integration (4)
- [ ] **vid-positioning**: interview-posture, update-check, vault-integration (3)
- [ ] **vid-pillars**: interview-posture, update-check, vault-integration (3)
- [ ] **vid-credibility**: bank-contract, interview-posture, proof-bank-schema, update-check, vault-integration (5)
- [ ] **vid-backstory**: interview-posture, update-check, vault-integration (3)
- [ ] **vid-research**: format-rotation-guide, interview-posture, outlier-identification-rules, packaging-system-template, theory-of-one-curation, three-circle-research, thumbnail-text-patterns, update-check (8)
- [ ] **aaios-feedback**: feedback-capture-map, feedback-offer, feedback-submit, vault-integration (4)

### STAGED skills

- [ ] **vid-ideas**: iceberg-and-top-3-alignment, theory-of-one-curation, update-check (3)
- [ ] **vid-intake**: piece-contract, story-capture-guide, update-check (3)
- [ ] **vid-capture**: bank-contract, framework-builder, story-capture-guide (3; metaphor-builder, proof-capture-guide, and testimonial-capture ship inside the skill's own `references/`)
- [ ] **vid-framing**: BENS-framework, piece-contract (2; format-index and the other decision files ship inside the skill's own `references/`)
- [ ] **vid-title**: BENS-framework (1)
- [ ] **vid-thumbnail**: thumbnail-text-patterns (1)
- [ ] **vid-structure**: parable-decision-matrix, script-tension-architecture, format-planners/ x7 (9)
- [ ] **vid-intro**: attention-craft, bank-contract, intro-architecture, metaphor-integration, proof-placement-rules, story-pulling-criteria, transition-patterns, visual-proof-callouts, voice-pressure-test, voice-rhythm, format-planners/ x7 (17)
- [ ] **vid-segment**: attention-craft, bank-contract, framework-builder, parable-decision-matrix, script-tension-architecture, transition-patterns, visual-proof-callouts, voice-pressure-test, voice-rhythm, format-planners/ x7 (16)
- [ ] **vid-ending**: attention-craft, bank-contract, metaphor-integration, parable-decision-matrix, proof-placement-rules, story-pulling-criteria, transition-patterns, voice-pressure-test, voice-rhythm, format-planners/ x7 (16)
- [ ] **vid-pressure-test**: attention-craft, audience-temperature-model, intro-architecture, script-tension-architecture, transition-patterns, voice-profile-schema, format-planners/ x7 (13)
- [ ] **vid-voice-capture**: interview-posture, vault-integration, voice-extraction-methods, voice-pressure-test, voice-profile-schema, voice-rhythm (6)
- [ ] **vid-voice-audit**: voice-pressure-test, voice-profile-schema, voice-rhythm (3)
- [ ] **vid-voice-update**: voice-profile-schema (1)
- [ ] **vid-pipeline**: update-check (1, pre-flight only; pure router, no other knowledge deps)

### WIP skills (re-verify dependency list before shipping)

- [ ] **aud-intake**: bank-contract (1, plus the two parked `.claude/skills-wip/` files)
- [ ] **aud-avatar-build**: none in `knowledge/` (0, plus the two parked `.claude/skills-wip/` files)
- [ ] **aud-validate**: none in `knowledge/` (0, plus the two parked files and skill-local `references/common-english.txt`)
- [ ] **aud-review**: none in `knowledge/` (0, plus the two parked `.claude/skills-wip/` files)
- [ ] **post-write**: bank-contract, iceberg-and-top-3-alignment, piece-contract, vault-integration, voice-pressure-test, voice-profile-schema (6; ai-hedging ships inside the skill's own `references/`)

---

## 6. Seed templates (copied, not loaded)

Two `knowledge/` files are not loaded as context. They are copied into the creator's vault by creator-setup as starter banks the creator then owns and grows:

| Template in `knowledge/` | Copied to | Soft-loaded at runtime by |
|--------------------------|-----------|--------------------|
| `hook-bank-template.md` | `banks/hook-bank.md` | vid-intro |
| `transition-bank-template.md` | `banks/transition-bank.md` | vid-segment, vid-ending |

The copy is idempotent (skip if the target exists), so a creator's edited bank is never overwritten. The seed rows sit in the manifest's pending table today and move into the live table when `vid-intro`, `vid-segment`, and `vid-ending` ship. The writing skills treat a missing bank as fine: the plugin's pattern libraries (`references/hook-patterns.md` in vid-intro, `knowledge/transition-patterns.md`) stay the craft reference, and the seeded bank is the creator's own supplement. The `banks/` files themselves are vault content and never ship in `knowledge/`.

---

## 7. Maintenance

> [!note] Provenance
> Regenerated 2026-07-21, updated 2026-07-27 for the vault-integration split by grepping all three skill roots (`plugins/authentic-ai-os/skills/`, `.claude/skills/`, `.claude/skills-wip/`), including each skill's `SKILL.md`, `references/`, `assets/`, and `manifest.md`, then cross-checking every referenced path against `knowledge/` on disk. Dev-only `WORKING-NOTES.md` files were excluded. This scan reflects the post-slimming state: six craft files moved from `knowledge/` into skill-local `references/`, four thumbnail files and five bank-schemas deleted, the aud-* method and schemas parked at `.claude/skills-wip/`, `vault-integration.md` split into a slim shared core plus `piece-contract.md` and `bank-contract.md`, `attention-craft.md` and `transition-patterns.md` added, and `emotion-brick-decision-matrix.md` renamed to `parable-decision-matrix.md`.

**This map is a release-process artifact.** It is regenerated as a mandatory step whenever a skill graduates (WIP to STAGED to RELEASED) or is parked. See the graduation checklist in `documents/RELEASE.md`, `documents/DEV-WORKFLOW.md`, and the `peak-release` skill.

Re-run this map whenever:
- A new skill is added, or a skill moves between roots (WIP to staged, staged to released).
- A skill's `SKILL.md`, `references/`, `assets/`, or `manifest.md` is edited (a reference may have been added or removed).
- A `knowledge/` file is added, renamed, moved into a skill, or deleted.

To regenerate the raw data:
1. Grep `knowledge/[A-Za-z0-9/_.-]+\.(md|txt)` across `plugins/authentic-ai-os/skills/`, `.claude/skills/`, and `.claude/skills-wip/`, then group by skill. Exclude `WORKING-NOTES.md` and any other dev-only files.
2. Separately grep `format-planners` (the `{format}.md` placeholder uses braces and is missed by the first pattern), the seed templates named in `creator-setup/manifest.md`, and the parked `.claude/skills-wip/*.md` files the `aud-*` skills load by repo-relative path.
3. Exclude the `knowledge/X.md` documentation placeholder.
4. Distinguish loads from pointers: a `knowledge/` path named only to say another skill loads it later is not a dependency of the file that names it.
5. Cross-check every referenced path against `knowledge/` on disk for orphans (files with no consumer) and broken references (refs with no file).

---

## 8. Known irregularities (not defects, worth tracking)

- **aaios-feedback skips the update-check pre-flight** that the other eight released skills run. Intentional: feedback is a terminal cross-cutting skill that runs mid-session after another skill already checked, so it skips the pre-flight to avoid interrupting a feedback report with an update notice.
- **vid-structure does not load `piece-contract.md`** while every other writing skill that touches piece.md does. It writes `script.md` and updates `piece.md` and may rely on a calling skill having loaded the field-ownership map. Confirm before shipping vid-structure standalone.
- **vid-pressure-test loads `format-planners/` and `attention-craft.md` deferred**, only when the Phase 2 retention-logic reviewer fires. The prior map said the planners were dropped entirely; the current build re-added them as a deferred load. Easy to mis-scan either way.
- **The decision-matrix rename is resolved.** `emotion-brick-decision-matrix.md` no longer exists; `knowledge/parable-decision-matrix.md` is the one matrix file, consumed by vid-structure and vid-segment, with a rare conditional pull from vid-ending.
- **vid-title's cross-skill pointer is resolved.** `angle-anchor-rules.md` and `reframe-toolkit.md` moved into `vid-title/references/` on 2026-07-27 when vid-framing was narrowed to the argument and stopped shopping the banks. vid-title now packages standalone.
- **The two bank seed rows are pending** in `creator-setup/manifest.md` until `vid-intro`, `vid-segment`, and `vid-ending` ship. The templates ship in `knowledge/` either way; the rows move tables at graduation.
