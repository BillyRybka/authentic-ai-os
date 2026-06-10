# Skill-to-Knowledge Dependency Map

The packaging contract for Authentic AI OS. When a skill ships to the live plugin, every `knowledge/` file it references must ship with it. A skill's own `references/` and `assets/` are packaged inside the skill folder, so they travel automatically. But `knowledge/` files live outside the skill and are the thing that gets forgotten.

This map answers one question: **for any skill, exactly which `knowledge/` files must be in the plugin for it to work.**

Built by grepping every `SKILL.md`, `references/*.md`, and `assets/*.md` across `.claude/skills/` and `.claude/skills-wip/` on 2026-05-21, then cross-checking every referenced path against the `knowledge/` directory on disk.

**Important:** transitive references count. If a skill's packaged `references/` or `assets/` file points at a `knowledge/` file, that knowledge file is required too. Those cases are marked `(via references/)` or `(via assets/)` below.

**Status tags:** `SHIPPED` skills are live and their dependency lists are verified. `WIP` skills are in `skills-wip/` and their lists are accurate as of this scan but **unverified** — the skills are still changing, so re-run this map before shipping any of them.

---

## 1. Forward map — skill to required knowledge files

### SHIPPED skills

**creator-setup** `SHIPPED`
- Required knowledge files: **none**. Pure scaffolder, references no `knowledge/`.

**vid-foundation** `SHIPPED`
- Required knowledge files: **none**. Thin orchestrator, references no `knowledge/`.

**vid-avatar** `SHIPPED`
- `knowledge/interview-posture.md`
- `knowledge/vault-integration.md`
- `knowledge/creator-foundation-template.md`

**vid-positioning** `SHIPPED`
- `knowledge/interview-posture.md`
- `knowledge/vault-integration.md`

**vid-pillars** `SHIPPED`
- `knowledge/interview-posture.md`
- `knowledge/vault-integration.md`

**vid-credibility** `SHIPPED`
- `knowledge/interview-posture.md`
- `knowledge/vault-integration.md`
- `knowledge/proof-bank-schema.md`

**vid-backstory** `SHIPPED`
- `knowledge/interview-posture.md`
- `knowledge/vault-integration.md`

**vid-research**
- `knowledge/three-circle-research.md`
- `knowledge/outlier-identification-rules.md`
- `knowledge/format-rotation-guide.md`
- `knowledge/packaging-system-template.md`
- Outputs three bank files: `banks/pattern-bank.md`, `banks/title-bank.md`, `banks/power-words-bank.md` (plus `foundation/packaging-system.md` from Phase 7 evidence)

### WIP skills (unverified — re-scan before shipping)

**vid-voice-capture** `WIP`
- `knowledge/interview-posture.md`
- `knowledge/vault-integration.md`
- `knowledge/voice-profile-schema.md`
- `knowledge/voice-extraction-methods.md`
- `knowledge/voice-pressure-test.md`
- Note: `voice-rhythm.md` is named in this skill but explicitly **not loaded** by it ("loaded by writing skills, not this one"). Not required for vid-voice-capture.

**vid-capture** `WIP`
- `knowledge/vault-integration.md`
- `knowledge/story-capture-guide.md`
- `knowledge/proof-capture-guide.md`
- `knowledge/metaphor-builder.md`
- `knowledge/testimonial-capture.md`
- `knowledge/framework-builder.md`

**vid-intake** `WIP`
- `knowledge/vault-integration.md`
- `knowledge/story-capture-guide.md` (also via `references/push-vs-pause-rules.md`)

**vid-framing** `WIP`
- `knowledge/three-circle-research.md`
- `knowledge/outlier-identification-rules.md` (also via `references/angle-anchor-rules.md`)
- `knowledge/audience-temperature-model.md` (also via `references/audience-temperature-fit.md`)
- `knowledge/format-planners/*.md` — all 7 (case-study, deep-dive, interview, listicle, news, roast, short-process)

**vid-title** `WIP`
- `knowledge/BENS-framework.md`
- `knowledge/thumbnail-text-patterns.md`

**vid-thumbnail** `WIP`
- `knowledge/vault-integration.md`
- `knowledge/thumbnail-strategy-menu.md`
- `knowledge/thumbnail-text-patterns.md`
- `knowledge/thumbnail-examples-library.md`
- `knowledge/BENS-framework.md`
- `knowledge/gift-framework.md`
- Note: `thumbnail-composition-guide.md` is named but explicitly **not loaded** — reserved for the future `vid-thumbnail-gen` skill. Not required for vid-thumbnail.

**vid-structure** `WIP`
- `knowledge/voice-profile-schema.md`
- `knowledge/script-tension-architecture.md`
- `knowledge/framework-builder.md` (via `assets/script-skeleton-template.md`)
- `knowledge/format-planners/*.md` — all 7

**vid-intro** `WIP`
- `knowledge/vault-integration.md`
- `knowledge/intro-architecture.md`
- `knowledge/voice-profile-schema.md`
- `knowledge/voice-rhythm.md`
- `knowledge/voice-pressure-test.md`
- `knowledge/parable-decision-matrix.md`
- `knowledge/story-pulling-criteria.md`
- `knowledge/proof-placement-rules.md`
- `knowledge/visual-proof-callouts.md`
- `knowledge/metaphor-integration.md`
- `knowledge/format-planners/*.md` — all 7
- `knowledge/hook-bank.md` *(planned, not yet authored. Billy-built reference of hook patterns. Required before vid-intro ships.)*

**vid-segment** `WIP`
- `knowledge/vault-integration.md`
- `knowledge/voice-profile-schema.md`
- `knowledge/voice-rhythm.md`
- `knowledge/voice-pressure-test.md`
- `knowledge/parable-decision-matrix.md`
- `knowledge/story-capture-guide.md`
- `knowledge/story-pulling-criteria.md`
- `knowledge/proof-capture-guide.md`
- `knowledge/proof-placement-rules.md`
- `knowledge/metaphor-builder.md`
- `knowledge/metaphor-integration.md`
- `knowledge/testimonial-capture.md`
- `knowledge/framework-builder.md`
- `knowledge/visual-demo-builder.md`
- `knowledge/visual-proof-callouts.md`
- `knowledge/format-planners/*.md` — all 7
- `knowledge/transition-bank.md` *(planned, not yet authored. Billy-built reference of transition patterns. Required before vid-segment ships.)*

**vid-ending** `WIP`
- `knowledge/vault-integration.md`
- `knowledge/voice-profile-schema.md`
- `knowledge/voice-rhythm.md` (also via `references/pivot-gap-bridge-shapes.md`)
- `knowledge/voice-pressure-test.md` (also via `references/pivot-gap-bridge-shapes.md`)
- `knowledge/parable-decision-matrix.md`
- `knowledge/story-pulling-criteria.md`
- `knowledge/proof-placement-rules.md`
- `knowledge/visual-proof-callouts.md`
- `knowledge/metaphor-integration.md`
- `knowledge/format-planners/*.md` — all 7
- `knowledge/transition-bank.md` *(planned, not yet authored. Same file vid-segment uses. Required before vid-ending ships.)*

**vid-pressure-test** `WIP`
- `knowledge/voice-profile-schema.md` (also via `vid-voice-audit` invoked as reviewer 2 sub-skill)
- `knowledge/script-tension-architecture.md` (also via `references/reviewer-retention-logic.md`)
- `knowledge/intro-architecture.md` (via `references/reviewer-ai-slop.md`)
- `knowledge/audience-temperature-model.md` (via `references/reviewer-retention-logic.md`)
- `knowledge/format-planners/*.md` — all 7

---

## 2. Reverse map — knowledge file to consuming skills

Use this when editing or renaming a knowledge file: it tells you every skill that breaks.

| Knowledge file | Consumed by |
|----------------|-------------|
| `BENS-framework.md` | vid-title, vid-thumbnail |
| `audience-temperature-model.md` | vid-framing, vid-pressure-test |
| `creator-foundation-template.md` | vid-avatar |
| `parable-decision-matrix.md` | vid-intro, vid-segment, vid-ending |
| `format-rotation-guide.md` | vid-research |
| `framework-builder.md` | vid-capture, vid-segment, vid-structure |
| `gift-framework.md` | vid-thumbnail |
| `hook-bank.md` *(planned, not yet authored)* | vid-intro |
| `interview-posture.md` | vid-avatar, vid-positioning, vid-pillars, vid-credibility, vid-backstory, vid-voice-capture |
| `intro-architecture.md` | vid-intro, vid-pressure-test |
| `metaphor-builder.md` | vid-capture, vid-segment |
| `metaphor-integration.md` | vid-intro, vid-segment, vid-ending |
| `outlier-identification-rules.md` | vid-research, vid-framing |
| `packaging-system-template.md` | vid-research |
| `proof-bank-schema.md` | vid-credibility |
| `proof-capture-guide.md` | vid-capture, vid-segment |
| `proof-placement-rules.md` | vid-intro, vid-segment, vid-ending |
| `script-tension-architecture.md` | vid-structure, vid-pressure-test |
| `story-capture-guide.md` | vid-capture, vid-intake, vid-segment |
| `story-pulling-criteria.md` | vid-intro, vid-segment, vid-ending |
| `testimonial-capture.md` | vid-capture, vid-segment |
| `three-circle-research.md` | vid-research, vid-framing |
| `thumbnail-composition-guide.md` | **none** (see Orphans) |
| `transition-bank.md` *(planned, not yet authored)* | vid-segment, vid-ending |
| `thumbnail-examples-library.md` | vid-thumbnail |
| `thumbnail-strategy-menu.md` | vid-thumbnail |
| `thumbnail-text-patterns.md` | vid-title, vid-thumbnail |
| `vault-integration.md` | vid-avatar, vid-positioning, vid-pillars, vid-credibility, vid-backstory, vid-voice-capture, vid-capture, vid-intake, vid-thumbnail, vid-intro, vid-segment, vid-ending |
| `visual-demo-builder.md` | vid-segment |
| `visual-proof-callouts.md` | vid-intro, vid-segment, vid-ending |
| `voice-extraction-methods.md` | vid-voice-capture |
| `voice-pressure-test.md` | vid-voice-capture, vid-intro, vid-segment, vid-ending |
| `voice-profile-schema.md` | vid-voice-capture, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `voice-rhythm.md` | vid-intro, vid-segment, vid-ending |
| `format-planners/case-study.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/deep-dive.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/interview.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/listicle.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/news.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/roast.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |
| `format-planners/short-process.md` | vid-framing, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test |

The 7 `format-planners/` files are always loaded one at a time (`{format}.md` matched to the video's format), but any of the 7 can be needed, so all 7 must ship with any consuming skill.

---

## 3. Orphan list — knowledge files with no consumer

`thumbnail-composition-guide.md` — referenced by no skill. **Intentional.** `vid-thumbnail/SKILL.md` line 57 explicitly states it is reserved for `vid-thumbnail-gen`, a skill that does not exist yet. It does not need to ship until that skill is built.

No other orphans. Every other file in `knowledge/` has at least one consumer.

---

## 4. Broken-reference list — referenced files that don't exist

Two planned `knowledge/` files are referenced by WIP skills but have not been authored yet. They must exist before their consuming skills can ship:

- `knowledge/hook-bank.md` — referenced by vid-intro. Billy-built reference of hook patterns and worked examples.
- `knowledge/transition-bank.md` — referenced by vid-segment and vid-ending. Billy-built reference of transition patterns (intro-forward, segment-pivot, body-to-ending).

These are NOT in `banks/`. They are universal reference content authored by the system maintainer that ships with the plugin and is read by skills, same shape as `format-rotation-guide.md` or `BENS-framework.md`. The pre-publish skills (vid-intro, vid-segment, vid-ending) cannot ship until these two files exist.

One thing that looks like a broken reference but is not: the string `knowledge/X.md` appears in several SKILL.md files (vid-avatar, vid-positioning, vid-pillars, vid-credibility, vid-backstory, vid-research, vid-voice-capture). It is **not a reference** — it is a documentation line explaining how to resolve `knowledge/` paths at runtime (`${CLAUDE_PLUGIN_ROOT}/knowledge/` when installed, repo-relative in dev). The `X` is a literal placeholder. Ignore it.

---

## 5. Per-skill packaging checklist

When you ship a skill, confirm every box. The skill's own `SKILL.md`, `references/`, and `assets/` ship inside the skill folder automatically — these checklists are only the **external `knowledge/` files** that must also be present in the plugin.

### SHIPPED skills

- [ ] **creator-setup** — no knowledge files needed.
- [ ] **vid-foundation** — no knowledge files needed.
- [ ] **vid-avatar** — interview-posture, vault-integration, creator-foundation-template (3)
- [ ] **vid-positioning** — interview-posture, vault-integration (2)
- [ ] **vid-pillars** — interview-posture, vault-integration (2)
- [ ] **vid-credibility** — interview-posture, vault-integration, proof-bank-schema (3)
- [ ] **vid-backstory** — interview-posture, vault-integration (2)
- [ ] **vid-research** — three-circle-research, outlier-identification-rules, format-rotation-guide, packaging-system-template (4)

### WIP skills (re-verify dependency list before shipping)

- [ ] **vid-voice-capture** — interview-posture, vault-integration, voice-profile-schema, voice-extraction-methods, voice-pressure-test (5)
- [ ] **vid-capture** — vault-integration, story-capture-guide, proof-capture-guide, metaphor-builder, testimonial-capture, framework-builder (6)
- [ ] **vid-intake** — vault-integration, story-capture-guide (2)
- [ ] **vid-framing** — three-circle-research, outlier-identification-rules, audience-temperature-model, format-planners/ ×7 (10)
- [ ] **vid-title** — BENS-framework, thumbnail-text-patterns (2)
- [ ] **vid-thumbnail** — vault-integration, thumbnail-strategy-menu, thumbnail-text-patterns, thumbnail-examples-library, BENS-framework, gift-framework (6)
- [ ] **vid-structure** — voice-profile-schema, script-tension-architecture, framework-builder, format-planners/ ×7 (10)
- [ ] **vid-intro** — vault-integration, intro-architecture, voice-profile-schema, voice-rhythm, voice-pressure-test, parable-decision-matrix, story-pulling-criteria, proof-placement-rules, visual-proof-callouts, metaphor-integration, format-planners/ ×7 (17)
- [ ] **vid-segment** — vault-integration, voice-profile-schema, voice-rhythm, voice-pressure-test, parable-decision-matrix, story-capture-guide, story-pulling-criteria, proof-capture-guide, proof-placement-rules, metaphor-builder, metaphor-integration, testimonial-capture, framework-builder, visual-demo-builder, visual-proof-callouts, format-planners/ ×7 (22)
- [ ] **vid-ending** — vault-integration, voice-profile-schema, voice-rhythm, voice-pressure-test, parable-decision-matrix, story-pulling-criteria, proof-placement-rules, visual-proof-callouts, metaphor-integration, format-planners/ ×7 (16)
- [ ] **vid-pressure-test** — voice-profile-schema, script-tension-architecture, intro-architecture, audience-temperature-model, format-planners/ ×7 (11)

---

## 6. Maintenance

Re-run this map whenever:
- A new skill is added, or a WIP skill is finished and moved to `skills/`.
- A skill's `SKILL.md`, `references/`, or `assets/` is edited (a reference may have been added or removed).
- A `knowledge/` file is added, renamed, or deleted.

To regenerate the raw data: grep `knowledge/[A-Za-z0-9-]+\.md` and `format-planners` across `.claude/skills/` and `.claude/skills-wip/`, exclude the `knowledge/X.md` documentation placeholder and the `vid-foundation-workspace/` dev folder, then group by skill.
