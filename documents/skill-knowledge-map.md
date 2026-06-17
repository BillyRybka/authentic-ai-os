# Skill-to-Knowledge Dependency Map

The packaging contract for Authentic AI OS. When a skill ships to the live plugin, every `knowledge/` file it references must ship with it. A skill's own `references/` and `assets/` are packaged inside the skill folder, so they travel automatically. But `knowledge/` files live outside the skill and are the thing that gets forgotten.

This map answers one question: **for any skill, exactly which `knowledge/` files must be in the plugin for it to work.**

Built by grepping every `SKILL.md`, `references/*.md`, `assets/*.md`, and `manifest.md` across all three skill roots (`plugins/authentic-ai-os/skills/`, `.claude/skills/`, `.claude/skills-wip/`) on 2026-06-16, then cross-checking every referenced path against the `knowledge/` directory on disk.

**Important:** transitive references count. If a skill's packaged `references/` or `assets/` file points at a `knowledge/` file, that knowledge file is required too. Those cases are marked `(via references/)` or `(via assets/)` below.

**Three tiers, by packaging meaning:**

- `RELEASED` lives in `plugins/authentic-ai-os/skills/`. Ships to creators. Dependency lists verified.
- `STAGED` lives in `.claude/skills/`. Works in this repo, not yet released. Accurate as of this scan, not yet packaged.
- `WIP` lives in `.claude/skills-wip/`. Not ready. Lists accurate as of this scan but unverified, because the skills are still changing. Re-run this map before moving any of them.

The skills now split into three families: `vid-*` (the video pipeline), `aud-*` (the synthetic-audience pipeline), and `post-*` (distribution into platform posts).

---

## 1. Forward map: skill to required knowledge files

### RELEASED skills (8)

**creator-setup** `RELEASED`
- `knowledge/update-check.md` (mandatory update-check pre-flight)
- `knowledge/vault-integration.md`
- **Seeds two starter banks from templates.** creator-setup copies `knowledge/hook-bank-template.md` into `banks/hook-bank.md` and `knowledge/transition-bank-template.md` into `banks/transition-bank.md` (idempotent, copy-if-absent). Both templates must ship with creator-setup even though they are copied, not loaded. See section 7.

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
- `knowledge/vault-integration.md`

**vid-backstory** `RELEASED`
- `knowledge/interview-posture.md`
- `knowledge/update-check.md`
- `knowledge/vault-integration.md`

**aaios-feedback** `RELEASED`
- `knowledge/feedback-capture-map.md`
- `knowledge/feedback-offer.md`
- `knowledge/feedback-submit.md`
- `knowledge/vault-integration.md`
- Note: aaios-feedback does **not** load the `update-check.md` pre-flight that the other seven released skills run. Confirmed by grep, flagged in section 8.

### STAGED skills (3)

**vid-ideas** `STAGED`
- `knowledge/iceberg-and-top-3-alignment.md`
- `knowledge/theory-of-one-curation.md`

**vid-intake** `STAGED`
- `knowledge/iceberg-and-top-3-alignment.md`
- `knowledge/story-capture-guide.md`
- `knowledge/vault-integration.md`

**vid-research** `STAGED`
- `knowledge/format-rotation-guide.md`
- `knowledge/interview-posture.md`
- `knowledge/outlier-identification-rules.md`
- `knowledge/packaging-system-template.md`
- `knowledge/theory-of-one-curation.md`
- `knowledge/three-circle-research.md`
- `knowledge/thumbnail-text-patterns.md`
- Outputs bank files in the creator's vault: `banks/pattern-bank.md`, `banks/title-bank.md`, `banks/power-words-bank.md`, plus `foundation/packaging-system.md`. Those are vault content, not knowledge dependencies.

### WIP skills (re-scan before shipping)

#### Audience family (`aud-*`)

**aud-intake** `WIP`
- `knowledge/synthetic-audience-method.md`
- `knowledge/vault-integration.md`

**aud-avatar-build** `WIP`
- `knowledge/synthetic-audience-method.md`
- `knowledge/vault-integration.md`

**aud-validate** `WIP`
- `knowledge/common-english.txt` (vocabulary-leak test word list)
- `knowledge/synthetic-audience-method.md`
- `knowledge/vault-integration.md`

**aud-review** `WIP`
- `knowledge/synthetic-audience-method.md`
- `knowledge/vault-integration.md`

#### Distribution family (`post-*`)

**post-write** `WIP`
- `knowledge/ai-hedging.md`
- `knowledge/iceberg-and-top-3-alignment.md`
- `knowledge/vault-integration.md`
- `knowledge/voice-pressure-test.md`
- `knowledge/voice-profile-schema.md`

#### Video family (`vid-*`)

**vid-capture** `WIP`
- `knowledge/framework-builder.md`
- `knowledge/metaphor-builder.md`
- `knowledge/proof-capture-guide.md`
- `knowledge/story-capture-guide.md`
- `knowledge/testimonial-capture.md`
- `knowledge/vault-integration.md`

**vid-framing** `WIP`
- `knowledge/audience-temperature-model.md`
- `knowledge/outlier-identification-rules.md`
- `knowledge/three-circle-research.md`
- `knowledge/format-planners/*.md`: all 7 (case-study, deep-dive, interview, listicle, news, roast, short-process)

**vid-title** `WIP`
- `knowledge/BENS-framework.md`
- `knowledge/thumbnail-text-patterns.md`

**vid-thumbnail** `WIP`
- `knowledge/BENS-framework.md`
- `knowledge/gift-framework.md`
- `knowledge/thumbnail-composition-guide.md`
- `knowledge/thumbnail-examples-library.md`
- `knowledge/thumbnail-strategy-menu.md`
- `knowledge/thumbnail-text-patterns.md`
- `knowledge/vault-integration.md`
- Note: `thumbnail-composition-guide.md` is now loaded by this skill. It was an intentional orphan in the prior map (reserved for a future `vid-thumbnail-gen`). It is no longer an orphan.

**vid-structure** `WIP`
- `knowledge/framework-builder.md` (via `assets/script-skeleton-template.md`)
- `knowledge/script-tension-architecture.md`
- `knowledge/voice-profile-schema.md`
- `knowledge/format-planners/*.md`: all 7
- Note: vid-structure does **not** load `vault-integration.md`. Confirmed by grep.

**vid-intro** `WIP`
- `knowledge/intro-architecture.md`
- `knowledge/metaphor-integration.md`
- `knowledge/parable-decision-matrix.md`
- `knowledge/proof-placement-rules.md`
- `knowledge/story-pulling-criteria.md`
- `knowledge/vault-integration.md`
- `knowledge/visual-proof-callouts.md`
- `knowledge/voice-pressure-test.md`
- `knowledge/voice-profile-schema.md`
- `knowledge/voice-rhythm.md`
- `knowledge/format-planners/*.md`: all 7
- Pulls hook patterns from `banks/hook-bank.md` (vault bank, seeded by creator-setup from `hook-bank-template.md`, not a knowledge dependency).

**vid-segment** `WIP`
- `knowledge/framework-builder.md`
- `knowledge/metaphor-builder.md`
- `knowledge/metaphor-integration.md`
- `knowledge/parable-decision-matrix.md`
- `knowledge/proof-capture-guide.md`
- `knowledge/proof-placement-rules.md`
- `knowledge/story-capture-guide.md`
- `knowledge/story-pulling-criteria.md`
- `knowledge/testimonial-capture.md`
- `knowledge/vault-integration.md`
- `knowledge/visual-demo-builder.md`
- `knowledge/visual-proof-callouts.md`
- `knowledge/voice-pressure-test.md`
- `knowledge/voice-profile-schema.md`
- `knowledge/voice-rhythm.md`
- `knowledge/format-planners/*.md`: all 7
- Pulls transitions from `banks/transition-bank.md` (vault bank, seeded by creator-setup from `transition-bank-template.md`, not a knowledge dependency).

**vid-ending** `WIP`
- `knowledge/metaphor-integration.md`
- `knowledge/parable-decision-matrix.md`
- `knowledge/proof-placement-rules.md`
- `knowledge/story-pulling-criteria.md`
- `knowledge/vault-integration.md`
- `knowledge/visual-proof-callouts.md`
- `knowledge/voice-pressure-test.md`
- `knowledge/voice-profile-schema.md`
- `knowledge/voice-rhythm.md`
- `knowledge/format-planners/*.md`: all 7
- Pulls transitions from `banks/transition-bank.md` (vault bank, same seed as vid-segment, not a knowledge dependency).

**vid-pressure-test** `WIP`
- `knowledge/audience-temperature-model.md` (via `references/`)
- `knowledge/intro-architecture.md` (via `references/`)
- `knowledge/script-tension-architecture.md`
- `knowledge/voice-profile-schema.md`
- `knowledge/format-planners/*.md`: all 7
- Invokes `vid-voice-audit` as its voice reviewer (see that skill's deps).

**vid-voice-capture** `WIP`
- `knowledge/interview-posture.md`
- `knowledge/vault-integration.md`
- `knowledge/voice-extraction-methods.md`
- `knowledge/voice-pressure-test.md`
- `knowledge/voice-profile-schema.md`
- `knowledge/voice-rhythm.md`

**vid-voice-audit** `WIP`
- `knowledge/voice-pressure-test.md`
- `knowledge/voice-profile-schema.md`
- `knowledge/voice-rhythm.md`

**vid-voice-update** `WIP`
- `knowledge/voice-profile-schema.md`

---

## 2. Reverse map: knowledge file to consuming skills

Use this when editing or renaming a knowledge file: it tells you every skill that breaks.

| Knowledge file | Consumed by |
|----------------|-------------|
| `ai-hedging.md` | post-write |
| `audience-temperature-model.md` | vid-framing, vid-pressure-test |
| `BENS-framework.md` | vid-title, vid-thumbnail |
| `common-english.txt` | aud-validate |
| `creator-foundation-template.md` | vid-avatar |
| `feedback-capture-map.md` | aaios-feedback |
| `feedback-offer.md` | aaios-feedback, foundation |
| `feedback-submit.md` | aaios-feedback |
| `format-rotation-guide.md` | vid-research |
| `framework-bank-schema.md` | **none** (see Orphans) |
| `framework-builder.md` | vid-capture, vid-segment, vid-structure |
| `gift-framework.md` | vid-thumbnail |
| `hook-bank-template.md` | creator-setup (seed into `banks/hook-bank.md`, then used at runtime by vid-intro) |
| `iceberg-and-top-3-alignment.md` | vid-ideas, vid-intake, post-write |
| `interview-posture.md` | vid-avatar, vid-positioning, vid-pillars, vid-credibility, vid-backstory, vid-research, vid-voice-capture |
| `intro-architecture.md` | vid-intro, vid-pressure-test |
| `metaphor-bank-schema.md` | **none** (see Orphans) |
| `metaphor-builder.md` | vid-capture, vid-segment |
| `metaphor-integration.md` | vid-intro, vid-segment, vid-ending |
| `outlier-identification-rules.md` | vid-research, vid-framing |
| `packaging-bank-schema.md` | **none** (see Orphans) |
| `packaging-system-template.md` | vid-research |
| `parable-decision-matrix.md` | vid-intro, vid-segment, vid-ending |
| `proof-bank-schema.md` | vid-credibility |
| `proof-capture-guide.md` | vid-capture, vid-segment |
| `proof-placement-rules.md` | vid-intro, vid-segment, vid-ending |
| `script-tension-architecture.md` | vid-structure, vid-pressure-test |
| `story-bank-schema.md` | **none** (see Orphans) |
| `story-capture-guide.md` | vid-intake, vid-capture, vid-segment |
| `story-pulling-criteria.md` | vid-intro, vid-segment, vid-ending |
| `synthetic-audience-method.md` | aud-intake, aud-avatar-build, aud-validate, aud-review |
| `testimonial-bank-schema.md` | **none** (see Orphans) |
| `testimonial-capture.md` | vid-capture, vid-segment |
| `theory-of-one-curation.md` | vid-ideas, vid-research |
| `three-circle-research.md` | vid-research, vid-framing |
| `thumbnail-composition-guide.md` | vid-thumbnail |
| `thumbnail-examples-library.md` | vid-thumbnail |
| `thumbnail-strategy-menu.md` | vid-thumbnail |
| `thumbnail-text-patterns.md` | vid-research, vid-title, vid-thumbnail |
| `transition-bank-template.md` | creator-setup (seed into `banks/transition-bank.md`, then used at runtime by vid-segment, vid-ending) |
| `update-check.md` | creator-setup, foundation, vid-avatar, vid-positioning, vid-pillars, vid-credibility, vid-backstory |
| `vault-integration.md` | aaios-feedback, creator-setup, vid-avatar, vid-positioning, vid-pillars, vid-credibility, vid-backstory, vid-intake, aud-intake, aud-avatar-build, aud-validate, aud-review, post-write, vid-capture, vid-thumbnail, vid-intro, vid-segment, vid-ending, vid-voice-capture |
| `visual-demo-builder.md` | vid-segment |
| `visual-proof-callouts.md` | vid-intro, vid-segment, vid-ending |
| `voice-extraction-methods.md` | vid-voice-capture |
| `voice-pressure-test.md` | post-write, vid-intro, vid-segment, vid-ending, vid-voice-capture, vid-voice-audit |
| `voice-profile-schema.md` | post-write, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test, vid-voice-capture, vid-voice-audit, vid-voice-update |
| `voice-rhythm.md` | vid-intro, vid-segment, vid-ending, vid-voice-capture, vid-voice-audit |
| `format-planners/case-study.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/deep-dive.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/interview.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/listicle.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/news.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/roast.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/short-process.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |

The 7 `format-planners/` files are always loaded one at a time (`{format}.md` matched to the video's format), but any of the 7 can be needed, so all 7 must ship with any consuming skill.

---

## 3. Orphan list: knowledge files with no consumer

Five files exist in `knowledge/` but are referenced by no skill:

- `framework-bank-schema.md`
- `metaphor-bank-schema.md`
- `packaging-bank-schema.md`
- `story-bank-schema.md`
- `testimonial-bank-schema.md`

All five are bank-schema files authored ahead of their consumer. The skill that will write those banks, `vid-capture`, currently loads the matching `-builder` and `-capture` guides (`framework-builder.md`, `metaphor-builder.md`, `proof-capture-guide.md`, `story-capture-guide.md`, `testimonial-capture.md`) rather than the schema files. The one bank-schema that IS wired is `proof-bank-schema.md`, loaded by vid-credibility. These five are not defects, they are content staged ahead of the skill that will consume it, and they do not need to ship until `vid-capture` (or another skill) loads them.

No other orphans. Every other file in `knowledge/` has at least one consumer.

---

## 4. Broken-reference list: referenced files that don't exist

**None.** Every `knowledge/` path referenced by any skill resolves to a file on disk.

The two reference banks the prior map flagged as broken (`hook-bank.md`, `transition-bank.md`) are resolved. They were re-architected as vault banks seeded from templates: `knowledge/hook-bank-template.md` seeds `banks/hook-bank.md` (used by vid-intro), and `knowledge/transition-bank-template.md` seeds `banks/transition-bank.md` (used by vid-segment and vid-ending). Both templates exist in `knowledge/`. creator-setup copies them into the vault at setup, so the consuming skills find their banks at runtime.

One thing that looks like a broken reference but is not: the string `knowledge/X.md` appears in many SKILL.md files. It is **not a reference**. It is a documentation line explaining how to resolve `knowledge/` paths at runtime (`${CLAUDE_PLUGIN_ROOT}/knowledge/` when installed, repo-relative in dev). The `X` is a literal placeholder. Ignore it.

---

## 5. Per-skill packaging checklist

When you ship a skill, confirm every box. The skill's own `SKILL.md`, `references/`, and `assets/` ship inside the skill folder automatically. These checklists are only the **external `knowledge/` files** that must also be present in the plugin. Counts treat `format-planners/` as 7.

### RELEASED skills

- [ ] **creator-setup**: update-check, vault-integration, plus 2 seed templates (hook-bank-template, transition-bank-template) (4)
- [ ] **foundation**: feedback-offer, update-check (2)
- [ ] **vid-avatar**: creator-foundation-template, interview-posture, update-check, vault-integration (4)
- [ ] **vid-positioning**: interview-posture, update-check, vault-integration (3)
- [ ] **vid-pillars**: interview-posture, update-check, vault-integration (3)
- [ ] **vid-credibility**: interview-posture, proof-bank-schema, update-check, vault-integration (4)
- [ ] **vid-backstory**: interview-posture, update-check, vault-integration (3)
- [ ] **aaios-feedback**: feedback-capture-map, feedback-offer, feedback-submit, vault-integration (4)

### STAGED skills

- [ ] **vid-ideas**: iceberg-and-top-3-alignment, theory-of-one-curation (2)
- [ ] **vid-intake**: iceberg-and-top-3-alignment, story-capture-guide, vault-integration (3)
- [ ] **vid-research**: format-rotation-guide, interview-posture, outlier-identification-rules, packaging-system-template, theory-of-one-curation, three-circle-research, thumbnail-text-patterns (7)

### WIP skills (re-verify dependency list before shipping)

- [ ] **aud-intake**: synthetic-audience-method, vault-integration (2)
- [ ] **aud-avatar-build**: synthetic-audience-method, vault-integration (2)
- [ ] **aud-validate**: common-english.txt, synthetic-audience-method, vault-integration (3)
- [ ] **aud-review**: synthetic-audience-method, vault-integration (2)
- [ ] **post-write**: ai-hedging, iceberg-and-top-3-alignment, vault-integration, voice-pressure-test, voice-profile-schema (5)
- [ ] **vid-capture**: framework-builder, metaphor-builder, proof-capture-guide, story-capture-guide, testimonial-capture, vault-integration (6)
- [ ] **vid-framing**: audience-temperature-model, outlier-identification-rules, three-circle-research, format-planners/ x7 (10)
- [ ] **vid-title**: BENS-framework, thumbnail-text-patterns (2)
- [ ] **vid-thumbnail**: BENS-framework, gift-framework, thumbnail-composition-guide, thumbnail-examples-library, thumbnail-strategy-menu, thumbnail-text-patterns, vault-integration (7)
- [ ] **vid-structure**: framework-builder, script-tension-architecture, voice-profile-schema, format-planners/ x7 (10)
- [ ] **vid-intro**: intro-architecture, metaphor-integration, parable-decision-matrix, proof-placement-rules, story-pulling-criteria, vault-integration, visual-proof-callouts, voice-pressure-test, voice-profile-schema, voice-rhythm, format-planners/ x7 (17)
- [ ] **vid-segment**: framework-builder, metaphor-builder, metaphor-integration, parable-decision-matrix, proof-capture-guide, proof-placement-rules, story-capture-guide, story-pulling-criteria, testimonial-capture, vault-integration, visual-demo-builder, visual-proof-callouts, voice-pressure-test, voice-profile-schema, voice-rhythm, format-planners/ x7 (22)
- [ ] **vid-ending**: metaphor-integration, parable-decision-matrix, proof-placement-rules, story-pulling-criteria, vault-integration, visual-proof-callouts, voice-pressure-test, voice-profile-schema, voice-rhythm, format-planners/ x7 (16)
- [ ] **vid-pressure-test**: audience-temperature-model, intro-architecture, script-tension-architecture, voice-profile-schema, format-planners/ x7 (11)
- [ ] **vid-voice-capture**: interview-posture, vault-integration, voice-extraction-methods, voice-pressure-test, voice-profile-schema, voice-rhythm (6)
- [ ] **vid-voice-audit**: voice-pressure-test, voice-profile-schema, voice-rhythm (3)
- [ ] **vid-voice-update**: voice-profile-schema (1)

---

## 6. Seed templates (copied, not loaded)

Two `knowledge/` files are not loaded as context. They are copied into the creator's vault by creator-setup as starter banks the creator then owns and grows:

| Template in `knowledge/` | Copied to | Used at runtime by |
|--------------------------|-----------|--------------------|
| `hook-bank-template.md` | `banks/hook-bank.md` | vid-intro |
| `transition-bank-template.md` | `banks/transition-bank.md` | vid-segment, vid-ending |

The copy is idempotent (skip if the target exists), so a creator's edited bank is never overwritten. Both templates must ship with creator-setup. The `banks/` files themselves are vault content and never ship in `knowledge/`.

---

## 7. Maintenance

> [!note] Provenance
> Built 2026-06-16 by grepping all three skill roots (`plugins/authentic-ai-os/skills/`, `.claude/skills/`, `.claude/skills-wip/`), including each skill's `SKILL.md`, `references/`, `assets/`, and `manifest.md`, then cross-checking every referenced path against `knowledge/` on disk. This scan covers the released `plugins/` root (the prior map missed it), the `update-check.md` pre-flight, and the `aud-*` and `post-*` families that the prior map did not track.

Re-run this map whenever:
- A new skill is added, or a skill moves between roots (WIP to staged, staged to released).
- A skill's `SKILL.md`, `references/`, `assets/`, or `manifest.md` is edited (a reference may have been added or removed).
- A `knowledge/` file is added, renamed, or deleted.

To regenerate the raw data:
1. Grep `knowledge/[A-Za-z0-9/_.-]+\.(md|txt)` across `plugins/authentic-ai-os/skills/`, `.claude/skills/`, and `.claude/skills-wip/`, then group by skill.
2. Separately grep `format-planners` (the `{format}.md` placeholder uses braces and is missed by the first pattern) and the seed templates named in `creator-setup/manifest.md`.
3. Exclude the `knowledge/X.md` documentation placeholder.
4. Cross-check every referenced path against `knowledge/` on disk for orphans (files with no consumer) and broken references (refs with no file).

---

## 8. Known irregularities (not defects, worth tracking)

- **aaios-feedback skips the update-check pre-flight** that the other seven released skills run. Either intentional (feedback is a terminal cross-cutting skill) or an omission. Flagged for the maintainer to confirm.
- **Five bank-schema files are orphaned** (section 3). They will wire up when `vid-capture` is finished and consumes them. Until then they ship with nothing.
- **vid-structure does not load `vault-integration.md`** while every other writing skill does. It writes `script.md` and `piece.md` and may rely on a calling skill having loaded the routing rules. Confirm before shipping vid-structure standalone.
