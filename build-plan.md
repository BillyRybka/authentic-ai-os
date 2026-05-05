---
type: project-doc
doc: build-plan
project: youtube-content-os
status: active
last_refreshed: 2026-05-01
tags: [project, build-plan, architecture, roadmap]
---

# YouTube Content OS — Build Plan

The single source of truth for what this is, what's done, what's next, and how it all fits together. Read this before resuming work, before adding skills, before refactoring anything structural.

---

## 1. Context

### What we're building

A productizable Claude Code skill system that takes any YouTube business owner from idea to filming-ready script in roughly an hour, in their actual voice. Built as an Obsidian-native vault — every artifact links into the graph, every story captured once auto-surfaces at script-writing time, every winning thumbnail logs back into the bank for future reference.

### Who it's for

Two audiences, one product:

- **The creator using the system** — a YouTube business owner who runs the skills against their own workspace. They install the template, run setup once, then use per-video skills weekly to ship content.
- **Billy (Peak Systems)** — the first creator AND the system designer. authentic-ai-os is both the product template AND Billy's personal test workspace. Once the system works for him, the same template ships to other creators with their own foundation docs.

### What success looks like

A creator can:

1. Install the template, run `vid-foundation` once → produces creator-foundation.md, voice-profile.md, packaging-system.md
2. Capture stories / proofs / metaphors / testimonials anytime via `vid-capture` → grow evergreen banks
3. Run `vid-pipeline` per video → idea-to-filming-ready-script in ~60 minutes
4. Post-publish, run `vid-measurement` → log winners back into banks, refine the loop
5. Read the script aloud and not reword a single sentence (the voice is theirs, not Claude's)

### Where this lives

- **Product template:** `c:/Users/billr/projects/authentic-ai-os/` — the standalone, distributable workspace. Has `.claude/skills/`, `knowledge/`, `banks/`, etc. This IS the product.
- **Underlying study material (Billy's reference, not shipped):** `c:/Users/billr/projects/business-os/Resources/references/` — Billy's third-party study materials. Consulted during development. Read-only. Never shipped or referenced in productized output. All content in skill files is stripped of attribution per the productization rule.
- **Billy's personal workspace:** `c:/Users/billr/projects/business-os/` — Billy's full Obsidian vault (separate concerns, has Peak Systems content). The YouTube Content OS skills do NOT live there anymore.

---

## 2. Architecture

### Three-layer architecture

**Layer 1: Foundation Docs** — created once per creator, loaded by every downstream skill at startup. The creator's identity codified.

- `foundation/creator-foundation.md` — positioning, avatar, top 3 problems, credibility brags, backstory
- `foundation/voice-profile.md` — how the creator actually talks, multi-format Context Maps
- `foundation/packaging-system.md` — Gift Framework commitments, format rotation, thumbnail strategy, design guardrails
- `foundation/channel-audit.md` — optional, existing channels only

**Layer 2: Evergreen Banks** — grow continuously. Every script pulls from these.

- `banks/story-bank/` — narrative entries (Problem-Action-Outcome)
- `banks/proof-bank/` — creator's own evidence (numbers, screenshots, credentials)
- `banks/testimonial-bank/` — other people's words about the creator
- `banks/metaphor-bank/` — analogies and comparisons
- `banks/framework-bank/` — creator's own named systems / rules / methods
- `banks/packaging-bank/` — winning title+thumbnail combos (own + studied outliers)
- `banks/title-bank.md` — fill-in-the-blank title patterns (file, not folder)
- `banks/pattern-bank.md` — hook/structure patterns that worked (planned)

**Layer 3: Per-Video Content** — Obsidian content pieces.

- `Content/pieces/{slug}/` — idea, brain-dump, reference-block, script, thumbnail-brief, pressure-test, meta. All wikilinked, frontmatter'd, tagged.

### Skill architecture: orchestrator + sub-skills

Confirmed best practice for creative work, learned from analyzing the original `youtube-pipeline` mega-skill.

- ~150-line orchestrator (`vid-pipeline`) that ROUTES and delegates. Pure delegator. Never duplicates sub-skill logic.
- ~100-400 line sub-skills that each do ONE unit of work. Independently invokable AND callable by the orchestrator.
- One source of truth per domain — when STRUCTURE phase needs a hook, it INVOKES `vid-hook`; the same `vid-hook` runs again at SCRIPT phase if revision is needed. No duplicate hook logic in the orchestrator.

This pattern is the locked architectural decision. Don't break it by inlining sub-skill logic into `vid-pipeline` to "save a step."

### Reference / knowledge strategy

Two tiers:

**Skill-local references** — `.claude/skills/{skill}/references/` — files only that skill needs. Each skill loads its own.

**Shared knowledge** — `knowledge/` at workspace root — files multiple skills need. Format planners, vault-integration.md, BENS framework, gift framework, etc.

Why split this way: skills evolve independently; shared concepts need one canonical location so updates propagate. Don't copy-paste references across skills.

### Format-aware writing

Each writing sub-skill (`vid-hook`, `vid-segment`, `vid-ending`) reads the video's format from `reference-block.md` and loads the matching planner from `knowledge/format-planners/`. Different formats route through different internal workflows:

- News → bullet workflow, light tension, scripted hook only
- Deep Dive → full word-for-word, heavy STP (Setup-Tension-Payoff)
- Listicle → per-point STP
- Roast → scripted frames + bullet riff zones
- Short Process → tight STP
- Case Study → P-A-O tension, framework payoff
- Interview → scripted intro + question list

The format planner dictates the workflow. Skills don't hardcode format logic — they read the planner.

### Obsidian-native, graph-first

Every artifact follows `knowledge/vault-integration.md` — frontmatter schemas, wikilink contracts, tag conventions, file naming, callout patterns. Stories link to clients (People/), clients link back via Obsidian backlinks, scripts reference the stories they pulled in via `stories_used:` frontmatter, stories update their `used_in:` field with the video slug. Bidirectional. The "update both sides" rule is non-negotiable.

A creator should be able to:
- Open any story → see which videos used it (Obsidian backlinks)
- Open any video → see which stories/proofs/metaphors it pulled
- Filter the graph by tag or problem to see meaningful clusters

Isolated markdown that doesn't connect = build failure.

---

## 3. Locked architectural decisions

These are decisions made early and held throughout. Don't relitigate without strong reason.

1. **Architecture pattern:** Orchestrator + sub-skills + foundation docs + banks + minimal shared knowledge.
2. **Build approach:** Standalone productizable skills in authentic-ai-os. Billy's existing `billy-local` skills stay separate (those are Peak Systems-specific).
3. **Skill naming:** `vid-` prefix to avoid invocation conflict with other Billy-local skills.
4. **Skill location:** `.claude/skills/vid-*` at authentic-ai-os root. Each is self-contained.
5. **Default mode:** Adaptive (rich brain dump → Collaborative riff-and-clean; thin → Guided).
6. **Voice handling:** The brain dump IS the voice. Claude structures the creator's actual phrases — never generates from scratch.
7. **Output format:** Format-aware. Each writing sub-skill detects format and routes internally.
8. **Reference strategy:** Skill-local in each skill's `references/` folder; truly cross-skill in `knowledge/` at root.
9. **Examples-heavy:** Every reference doc shows good examples first, principles second. Real winners, not invented ones.
10. **Orchestrator role:** Pure delegator. Never duplicates sub-skill logic. Invokes the right sub-skill at each phase.
11. **Status updates:** CLAUDE.md instructions, not a skill.
12. **Capture skill:** One combined skill (`vid-capture` for story + proof + metaphor + testimonial). Not four separate skills.
13. **Research skill:** Deferred. Not building this pass.
14. **No expand-to-tier-2 skill:** `vid-segment` handles two-pass review (structure → prose) internally.
15. **Attribution scrub:** Skill files, knowledge files, and bank READMEs reference no source-curriculum names, teacher names, instructor names, or course names. Public-figure examples in calibration material (e.g. thumbnail libraries) are replaced with niche/category descriptors. The underlying material is consulted during development but never cited in productized output.
16. **Banks are content-typed, not skill-typed:** `story-bank/` lives independent of which skill writes to it. Multiple skills can read/write the same bank.
17. **Thumbnail planning vs. generation are separate skills:** `vid-thumbnail` plans text only; `vid-thumbnail-gen` (future) generates images. The text planner doesn't try to design.
18. **Numbers in thumbnails must come verbatim from the script.** No fabrication. (Hard rule, codified in `knowledge/thumbnail-text-patterns.md`.)
19. **Clickbait OK if delivered.** A thumbnail can carry a contrarian command if the script honors it.

---

## 4. Skills inventory

Status legend: ✅ done · 🚧 building · ⬜ not started · 🟡 optional/deferred

### Phase 1 — Foundation (run once per creator)

| Skill | Status | Description | Key dependencies | Files |
|---|---|---|---|---|
| `vid-foundation` | ✅ | 6-stage Q-script questionnaire walks the creator through positioning → avatar → credibility → backstory → voice profile (Stage 5) → packaging system. Outputs the 3 foundation docs. ICP-creator-style (one question at a time, exact prompts, probes for vague answers). | None — first skill run | `.claude/skills/vid-foundation/` (487-line SKILL.md, 5 references, 4 templates) |
| `vid-voice-capture` | ✅ | Deeper voice profile build — Layer 1 Core (cross-context patterns) + Layer 2 Context Maps (per-format sub-profiles). Multi-source extraction (transcripts + writing + live monologue). Strict superset of vid-foundation Stage 5. Refresh-aware (90 days / 20+ videos). Built by another session, audited 5/1. | foundation/creator-foundation.md, knowledge/voice-extraction-methods.md, knowledge/voice-pressure-test.md, knowledge/voice-profile-schema.md | `.claude/skills/vid-voice-capture/` (SKILL.md + 2 templates) |
| `vid-capture` | ✅ | Combined story + metaphor + proof + testimonial capture. Runnable standalone OR invoked by another skill mid-script. Dedup check per stage. People stub auto-creation. Invocation-mode aware (standalone loops, sub-skill mode returns wikilink). proof_type simplified to 2 (personal-result / client-win); presentation format moved to body. | foundation/creator-foundation.md (Top 3 problems), knowledge/vault-integration.md, capture guides in knowledge/ | `.claude/skills/vid-capture/` (SKILL.md + 5 templates) |

### Phase 2 — Packaging (run once per creator, refresh occasionally)

| Skill | Status | Description | Notes |
|---|---|---|---|
| `vid-packaging` | 🟡 | Standalone packaging refresh skill. **Likely redundant with vid-foundation Stage 6.** Decide before building — probably skip and let creators re-run vid-foundation Stage 6 for refresh. |

### Phase 3 — Per-video pipeline

Build leaves first, orchestrator last. Writing sub-skills before structure/routing skills before orchestrator.

| Skill | Status | Description | Key dependencies |
|---|---|---|---|
| `vid-thumbnail` | ✅ | Text planner ONLY. Generates 5-10 thumbnail text candidates using the patterns playbook. Creator picks 1-2. Output: brief with picks + strategy + BENS + rationale. Does NOT design the visual (no layouts, hero, expressions, AI prompts). | foundation/packaging-system.md, knowledge/thumbnail-text-patterns.md, knowledge/thumbnail-strategy-menu.md, knowledge/BENS-framework.md, knowledge/gift-framework.md, packaging-bank |
| `vid-title` | ✅ | BENS title generation. Loads creator-foundation, packaging-system, BENS framework, title-bank patterns, and the video's actual material. Generates 5-10 candidates each ≤50 chars and hitting at least one BENS letter. Anti-fabrication enforced (numbers must come from the script). Standalone OR sub-skill (returns title string to caller when invoked by vid-structure). | knowledge/BENS-framework.md, banks/title-bank.md, the video's brain-dump/framing artifact, foundation docs |
| `vid-hook` | ⬜ | Problem/Proof/Promise + 6-part intro. Format-aware. | format-planners/, voice-profile.md, banks/story-bank/, banks/proof-bank/ |
| `vid-segment` | ⬜ | One Setup/Tension/Payoff per segment. Two-pass review (structure → prose) internally. Format-aware. The biggest sub-skill. | format-planners/, voice-profile.md, banks/story-bank/, banks/proof-bank/, banks/metaphor-bank/, banks/framework-bank/ |
| `vid-ending` | ⬜ | Pivot/Gap/Bridge close. Format-aware. CTA placement. | format-planners/, voice-profile.md |
| `vid-intake` | ⬜ | Raw material capture with type tagging. Output: brain-dump.md. | None — first per-video skill |
| `vid-framing` | ⬜ | 3-5 framings, Core Payoff, format pick, goal pick. Output: reference-block.md. | foundation docs, banks/pattern-bank.md, knowledge/three-circle-research |
| `vid-structure` | ⬜ | Keep/cut/combine review, Type 1 skeleton assembly. Invokes vid-title and vid-hook. | brain-dump.md, reference-block.md |
| `vid-pressure-test` | ⬜ | Parallel adversarial review agents. | The full script |
| `vid-pipeline` | ⬜ | Orchestrator (~150 lines target). Adaptive routing at start. Delegates to all of the above. Build LAST. | Everything above |

### Phase 4 — Feedback (post-publish)

| Skill | Status | Description |
|---|---|---|
| `vid-measurement` | ⬜ | 4-checkpoint analysis (CTR, retention through hook, average view duration, end-screen action). Flop diagnosis. Logs winners to packaging-bank. |
| `vid-monthly-review` | ⬜ | Pipeline tracker review + routing decisions. Looks at the full month's data, surfaces patterns. |

### Phase 5 — Optional

| Skill | Status | Description |
|---|---|---|
| `vid-channel-audit` | 🟡 | Existing channels only. Analyzes a creator's current channel state to inform packaging refresh. |
| `vid-thumbnail-gen` | 🟡 | Image generation extension. Takes a brief from vid-thumbnail + creator's AI tool config + their packaging-bank winners. Includes "training mode" — creator drops in title+thumbnail winner pairs to teach the generator their style. Optional add-on, requires creator to configure their own AI tool API keys. |

**Total:** 14 skills if all built (4 done, 9 to build, 1 optional). If we drop `vid-packaging` and `vid-channel-audit`, 12 skills.

---

## 5. Data flow / dependency map

```
                Foundation Docs (creator-foundation, voice-profile, packaging-system)
                        ↓ loaded by every downstream skill at startup
                        ↓
    ┌───────────────────┼───────────────────┐
    ↓                   ↓                   ↓
 vid-capture       vid-thumbnail        vid-pipeline (orchestrator)
    ↓                                       ↓
 BANKS                                  per-phase invokes:
 (story / proof /                       vid-intake → brain-dump.md
  testimonial /                         vid-framing → reference-block.md
  metaphor /                            vid-structure → script.md skeleton
  framework /                              ↳ invokes vid-title → title locked
  packaging)                               ↳ invokes vid-hook → hook in script
    ↓                                   vid-segment (per segment) → script body
    ↓                                   vid-ending → script close
    ↓                                   vid-pressure-test → pressure-test.md
 read by writing skills                 vid-thumbnail → thumbnail-brief.md
 (vid-segment, vid-hook, vid-ending,
  vid-thumbnail)
                                            ↓
                                        Content/pieces/{slug}/
                                        - meta.md (frontmatter)
                                        - brain-dump.md
                                        - reference-block.md
                                        - script.md
                                        - thumbnail-brief.md
                                        - pressure-test.md
                                            ↓
                                        Post-publish:
                                        vid-measurement → updates banks
                                        - winning packages → packaging-bank
                                        - winning hooks → hook-bank
                                        - winning patterns → pattern-bank
```

### Specific dependencies

- **Foundation docs** are loaded at startup by EVERY skill that produces user-facing content. They define the creator's voice and identity.
- **Banks** are the connective tissue. Captured once via `vid-capture`, pulled at script-writing time by writing skills. Bidirectional wikilinks ensure traceability.
- **`packaging-system.md`** drives both `vid-thumbnail` (committed thumbnail strategy + design guardrails) and the format-planner selection in writing skills.
- **`title-bank.md`** is read by `vid-title` (patterns to adapt). Updated by `vid-measurement` (winning patterns get logged).
- **`packaging-bank/`** is read by `vid-thumbnail` (style anchors for past winners + studied outliers). Updated by `vid-measurement` post-publish.

### How the orchestrator delegates (the pattern)

When `vid-pipeline` runs the STRUCTURE phase:

1. Reads `brain-dump.md`, `reference-block.md`
2. Extracts distinct ideas (lightweight logic in the orchestrator)
3. Runs keep/cut/combine review with the creator
4. **INVOKES `vid-title`** → returns locked title
5. **INVOKES `vid-hook`** → returns hook drawing from the brain dump
6. Gets thumbnail text decision (might invoke `vid-thumbnail` here or defer to a separate run)
7. Assembles Type 1 skeleton (the outline)
8. Saves to `script.md`

When the SCRIPT phase runs, it invokes `vid-hook` again ONLY if the hook needs revision — otherwise uses the one from STRUCTURE. Same source of truth, no duplication.

---

## 6. Build sequence (current state forward)

### Step 1 — Knowledge layer first ✅ (mostly done)

The references downstream skills will load. Build before the skills that need them.

- [x] `knowledge/vault-integration.md` — frontmatter schema, wikilink contracts
- [x] `knowledge/BENS-framework.md` — Big/Easy/New/Safe title logic
- [x] `knowledge/gift-framework.md` — wrapping/box/gift packaging philosophy
- [x] `knowledge/format-rotation-guide.md` — Rule of 3+1
- [x] `knowledge/thumbnail-strategy-menu.md` — 6 strategies, format-strategy pairing
- [x] `knowledge/thumbnail-text-patterns.md` — 5 winning patterns + anti-patterns + examples library + title-thumbnail pairing
- [x] `knowledge/thumbnail-composition-guide.md` — visual composition (reserved for vid-thumbnail-gen, not loaded by vid-thumbnail)
- [x] `knowledge/story-capture-guide.md`
- [x] `knowledge/metaphor-builder.md`
- [x] `knowledge/proof-capture-guide.md`
- [x] `knowledge/testimonial-capture.md`
- [x] `knowledge/voice-extraction-methods.md`
- [x] `knowledge/voice-pressure-test.md`
- [x] `knowledge/voice-profile-schema.md`
- [x] `knowledge/format-planners/short-process.md` ✅
- [x] `knowledge/format-planners/case-study.md` ✅
- [x] `knowledge/format-planners/news.md` ✅
- [x] `knowledge/format-planners/deep-dive.md` ✅
- [x] `knowledge/format-planners/interview.md` ✅
- [x] `knowledge/format-planners/roast.md` ✅
- [x] `knowledge/format-planners/listicle.md` ✅
- [x] `knowledge/intro-architecture.md` ✅
- [ ] `knowledge/voice-rhythm.md` — referenced in original build plan, used by all writing skills. Build before vid-hook / vid-segment.

### Step 2 — Phase 1 foundation skills ✅ (done)

- [x] `vid-foundation`
- [x] `vid-voice-capture`
- [x] `vid-capture`

### Step 3 — Bank READMEs ✅ (done)

- [x] `banks/story-bank/README.md`
- [x] `banks/proof-bank/README.md`
- [x] `banks/testimonial-bank/README.md`
- [x] `banks/metaphor-bank/README.md`
- [x] `banks/framework-bank/README.md`
- [x] `banks/packaging-bank/README.md`
- [ ] `banks/title-bank.md` — exists as a seed file from vid-foundation; expand patterns over time
- [ ] `banks/pattern-bank.md` — not yet created; populated by vid-measurement
- [ ] `banks/hook-bank.md` — patterns; build alongside vid-hook
- [ ] `banks/transition-bank.md` — patterns; build alongside vid-segment

### Step 4 — Phase 3 writing pipeline (next)

Build in dependency order. Writing sub-skills before structure/routing before orchestrator.

- [x] `vid-title` ✅ (smallest, no deps — built and tested through 4 iterations)
- [x] All 7 format planners ✅ (case-study, deep-dive, interview, listicle, news, roast, short-process)
- [x] `knowledge/intro-architecture.md` ✅
- [ ] `knowledge/voice-rhythm.md`
- [ ] **`vid-hook` ← NEXT** (intro builder using the 6-part architecture + format planners)
- [ ] `vid-segment` (the biggest)
- [ ] `vid-ending`
- [ ] `vid-intake`
- [ ] `vid-framing`
- [ ] `vid-structure` (invokes vid-title and vid-hook)
- [ ] `vid-pressure-test`
- [ ] `vid-pipeline` (orchestrator — build last)

**Quick reference for vid-hook (the next skill to build):**

vid-hook produces the FULL intro (6 parts), not just the hook line. Loads:
- `knowledge/intro-architecture.md` (universal template)
- `knowledge/format-planners/{format}.md` (per-format adaptation)
- `foundation/voice-profile.md` (creator preferences)
- `foundation/creator-foundation.md` (avatar Top 3 problems for Problem-poke source)
- `Content/pieces/{slug}/meta.md` + locked title + thumbnail-brief.md (drives Top 3 viewer questions)
- `banks/hook-bank.md` and `banks/transition-bank.md` (NOT YET BUILT — see open items below)
- the video's brain-dump or framing artifact

**Pre-vid-hook open items:**
1. `banks/hook-bank.md` — seed file in vid-foundation/assets/. Mine from `business-os/Resources/references/ed-lawrence-ygs/materials-shared/ytgs-video-planner.txt` "Hook bank" section. Patterns + worked examples (same shape as title-bank-seed).
2. `banks/transition-bank.md` — same. Mine from the "Transition Bank" section.
3. `knowledge/voice-rhythm.md` — build alongside vid-hook; loaded by all writing skills.
4. Voice-profile schema additions: `preferred_hook_types`, `transition_style_preferences`, `intro_pacing` fields. Small addition.
5. Possibly add a `hook-style` field to packaging-system.md so the creator can pre-commit to certain hook types.

If the creator wants to test the existing skills end-to-end before vid-hook is built, run vid-foundation → vid-capture (a few entries) → vid-title → vid-thumbnail to get a sense of how the assembled output feels. The intro is missing but the rest of the brief comes together.

### Step 5 — End-to-end test

- [ ] Run `vid-pipeline` on a real Peak Systems video
- [ ] Time it. Real clock time, not aspirational. Target: under 60 minutes idea-to-filming-ready.
- [ ] Read script aloud — would Billy reword anything? If yes, voice profile or skill is broken.
- [ ] Verify all artifacts in `Content/pieces/{slug}/`
- [ ] Verify: when STRUCTURE invoked `vid-hook`, the hook in skeleton MATCHES the hook in final script (no duplicate logic regression)
- [ ] Verify: running with format=News routes through different workflow than format=Deep Dive

### Step 6 — Phase 4 feedback skills

- [ ] `vid-measurement`
- [ ] `vid-monthly-review`

### Step 7 — Optional (Phase 5)

- [ ] `vid-channel-audit` (only if existing-channel use case demands it)
- [ ] `vid-thumbnail-gen` (image generator + training mode)

---

## 7. Where things live

```
c:/Users/billr/projects/authentic-ai-os/        ← THE PRODUCT TEMPLATE
├── CLAUDE.md                                          ← content-engine rules, vault routing
├── build-plan.md                                      ← THIS FILE
├── .claude/
│   └── skills/
│       ├── vid-foundation/      ✅ SKILL.md, 5 references/, 4 assets/
│       ├── vid-voice-capture/   ✅ SKILL.md, 2 assets/
│       ├── vid-capture/         ✅ SKILL.md, 5 assets/
│       ├── vid-thumbnail/       ✅ SKILL.md, 2 assets/
│       └── vid-{title,hook,segment,ending,...}/      ⬜ to build
├── knowledge/                                         ← shared references loaded by skills
│   ├── vault-integration.md     ✅ canonical schema contract
│   ├── BENS-framework.md        ✅
│   ├── gift-framework.md        ✅
│   ├── format-rotation-guide.md ✅
│   ├── thumbnail-strategy-menu.md ✅
│   ├── thumbnail-text-patterns.md ✅ examples library + rules
│   ├── thumbnail-composition-guide.md ✅ reserved for vid-thumbnail-gen
│   ├── story-capture-guide.md   ✅
│   ├── metaphor-builder.md      ✅
│   ├── proof-capture-guide.md   ✅
│   ├── testimonial-capture.md   ✅
│   ├── voice-extraction-methods.md ✅
│   ├── voice-pressure-test.md   ✅
│   ├── voice-profile-schema.md  ✅
│   ├── voice-rhythm.md          ⬜ to build (writing skills load it)
│   └── format-planners/
│       ├── short-process.md     ✅
│       └── {6 others}.md        ⬜ to build
├── foundation/                                        ← creator identity (skill-populated)
│   ├── creator-foundation.md    (created by vid-foundation)
│   ├── voice-profile.md         (created by vid-foundation Stage 5 / vid-voice-capture)
│   └── packaging-system.md      (created by vid-foundation Stage 6)
├── banks/                                             ← evergreen, grows over time
│   ├── story-bank/              ✅ README + entries from vid-capture
│   ├── proof-bank/              ✅ README + entries from vid-capture
│   │   └── assets/              ← screenshots, charts, video clips
│   ├── testimonial-bank/        ✅ README + entries from vid-capture
│   ├── metaphor-bank/           ✅ README + entries from vid-capture
│   ├── framework-bank/          ✅ README + manual entries (creator-authored)
│   ├── packaging-bank/          ✅ README + winners (own + outliers)
│   ├── title-bank.md            ⬜ patterns + winning titles
│   ├── pattern-bank.md          ⬜ structure/hook patterns
│   ├── hook-bank.md             ⬜ hook patterns (alongside vid-hook)
│   └── transition-bank.md       ⬜ transition patterns (alongside vid-segment)
├── Content/
│   ├── pieces/                  ← per-video folders, each with full artifact set
│   ├── ideas/                   ← swipe file for not-yet-built content
│   └── sequences/               ← email sequences (multi-piece)
└── People/                                            ← auto-stubbed when clients mentioned
    └── {Full Name}.md
```

### Source material (read-only, not in product)

```
c:/Users/billr/projects/business-os/Resources/references/ed-lawrence-ygs/
├── frameworks.md
├── insights.md
├── learning-paths.md
├── modules/
│   ├── phase-03-packaging-videos/
│   ├── phase-04-video-strategy-ideation/
│   ├── phase-05-writing-planning-videos/
│   └── ...
└── materials-shared/
    ├── ytgs-video-planner.txt   ← Title Bank, Hook Bank, Transition Bank source
    └── ...
```

When a skill's content needs source-material backing, read these files directly. Never reference them by name in productized skill files (attribution-scrub rule).

---

## 8. Banks system (deeper dive)

Each bank serves a different purpose. Don't duplicate content across banks.

| Bank | Source | Read by | Written by | Purpose |
|---|---|---|---|---|
| story-bank | creator's lived/observed stories | vid-segment, vid-hook | vid-capture (Story stage) | Narrative beats |
| proof-bank | creator's own evidence | vid-hook, vid-segment | vid-capture (Proof stage) | Credibility through specifics |
| testimonial-bank | other people's words | vid-hook, vid-segment | vid-capture (Testimonial stage) | Social proof |
| metaphor-bank | creator's analogies | vid-segment, vid-hook | vid-capture (Metaphor stage) | Concrete-ifying abstractions |
| framework-bank | creator's named systems | vid-framing, vid-structure, vid-segment | manual (for now) | Repeatable teaching structures |
| packaging-bank | own winners + studied outliers | vid-thumbnail, vid-thumbnail-gen | vid-measurement post-publish | Style anchors for proven packages |
| title-bank | fill-in-the-blank patterns + winners | vid-title | vid-foundation seeds, vid-measurement adds winners | Reusable title formulas |
| pattern-bank | hook/structure patterns | vid-framing | vid-measurement post-publish | What's worked structurally |
| hook-bank | hook patterns | vid-hook | seed + creator additions | Hook starting points |
| transition-bank | transition phrases | vid-segment, vid-ending | seed + creator additions | Smooth segment-to-segment flow |

**Patterns vs. winners distinction:**
- **Patterns** = reusable formulas (mad-libs). Live in single-file banks like title-bank.md, hook-bank.md.
- **Winners** = specific past wins, instantiated. Live in folder banks (packaging-bank/, story-bank/, etc.) — one entry per win.

---

## 9. Verification & testing plan

### After each skill build

- Audit for schema match with `vault-integration.md` (frontmatter, wikilinks)
- Path correctness — every referenced file resolves
- Conversation pattern — short messages, ask-and-wait, no reference-dumping
- Attribution scrub — no source-curriculum names, teacher names, instructor names, course names, or named third-party creators in productized files
- Cross-skill integration — does it write to the same files other skills read?
- Honest pass count — what % of the skill works without manual fix?

### After Phase 3 (the big test)

- Run `vid-pipeline` end-to-end on a real Peak Systems video
- Time it. Actual clock time, not aspirational.
- Read the script aloud — does Billy reword anything?
- Check artifacts at `Content/pieces/{slug}/`:
  - meta.md ✓
  - brain-dump.md ✓
  - reference-block.md ✓
  - script.md ✓
  - thumbnail-brief.md ✓
  - pressure-test.md ✓
- Verify: STRUCTURE-phase hook = SCRIPT-phase hook (orchestrator didn't duplicate logic)
- Verify: News format routes differently than Deep Dive format (format-aware works)

### After Phase 4

- vid-measurement on a published video — does it correctly log a winner to packaging-bank?
- Does the next vid-thumbnail run pull that winner as a style anchor?
- Does vid-monthly-review surface patterns across multiple videos?

---

## 10. Open questions / known gaps

### Architectural

1. **vid-packaging** — probably redundant with vid-foundation Stage 6. Default: skip. Confirm before building.
2. **vid-research** — deferred from original plan. Revisit only if creators consistently need fresh data injection mid-script.
3. **Title vs. thumbnail role asymmetry** — the underlying material doesn't explicitly say which carries more click weight. Worth documenting once packaging-bank has data.

### Knowledge gaps (from deeper source-material mining)

These are real gaps in our knowledge files that surfaced during deeper source mining. Address when building related skills:

- **Outlier extraction methodology** — the source teaches "study outliers" but no systematic extraction protocol. Belongs in vid-channel-audit or a future research skill.
- **A/B testing protocol for thumbnails** — sample size, threshold-to-judge, refresh/pivot timing. Belongs in vid-measurement.
- **Niche-specific gift-framework lookup** — concrete wrapping/box/gift examples per niche (crypto / wellness / business / fitness). Currently abstract. Add as we see real creator data.
- **Series thumbnail templating** — when videos are part of a series, thumbnails share visual elements. Implied in the source teaching, never systematized.

### Product / distribution

- **Vale linter integration** — autocorrect-style voice enforcement on draft saves. The voice-profile compiles to Vale rules; a vid-voice-rule-capture skill would mirror business-os pattern. Future enhancement, not blocking Phase 3.
- **Test harness** — currently ad-hoc (spawn agents, read output). At some point want a proper eval suite for each skill.
- **Distribution mechanism** — answered. See Section 13: package as a Claude Code plugin. Migration deferred until Phase 3 skills land.

---

## 11. Patterns and principles (the meta-layer)

These hold across every skill in the system. Violating any of them = something to re-think.

1. **Conversation, not document.** Skills run as dialogues. Short messages. Ask-and-wait. References are for Claude to think with, not paste at the creator.
2. **Creator drives, Claude structures.** Skills extract and organize. They never generate identity, voice, stories, numbers, or claims. The creator's brain dump is the raw material; Claude does not invent.
3. **No fabrication.** Numbers, client names, results, quotes — all must trace to source (script, foundation docs, banks). Visual elements (objects in a thumbnail, scene descriptions in a brief) must derive from what the creator actually has or said.
4. **Specificity wins.** Vague answers get pushed back on. "Busy professionals" → push for "solo founders, $200k-$2M, working from home." Generic verbs → specific verbs. Round numbers → real numbers.
5. **Read aloud is the voice test.** If the creator would reword it when speaking, the draft is wrong. Applies everywhere: scripts, thumbnails, emails, social posts.
6. **The graph is the product.** Every artifact wikilinks. Every story knows which videos used it. The Obsidian backlink pane and graph view should always show meaningful connections.
7. **Update both sides.** When a script uses a story, BOTH `script.md` and the story's `used_in:` get updated. Non-negotiable.
8. **Banks grow.** Patterns and winners both. Static banks are dead banks. Every published video should add to the bank ecosystem.
9. **MVP principle.** First version of every doc / skill / bank entry needs refinement after real data comes in. Don't grind for perfection upfront. Lock the best version the creator can articulate today.
10. **Match scope to skill.** A planner plans. A capturer captures. A writer writes. Skills that drift across roles (e.g. a planner that also designs) should be split.

---

## 12. Recent work log (last refreshed 2026-05-01)

- 2026-04-18: vid-foundation built and audited
- 2026-04-20: vid-capture built, four-stage capture
- 2026-04-20: authentic-ai-os standalone workspace established (split from business-os)
- 2026-04-20: All bank READMEs written (story / proof / testimonial / metaphor / framework)
- 2026-04-21: packaging-bank added (consolidated title+thumbnail winners)
- 2026-04-21: vid-thumbnail v1 built (planner)
- 2026-04-22: knowledge/thumbnail-text-patterns.md added (5 winning patterns, anti-patterns, examples)
- 2026-04-23: packaging-bank scope: own winners + studied outliers (one bank, source field)
- 2026-04-28: vid-voice-capture built in another session, audited and migrated
- 2026-04-30: schema sweep — last_refreshed and contexts_populated fields added to foundation doc schema
- 2026-04-30: vid-thumbnail upgraded with anti-fabrication, distinctiveness, tonal-pairing, click-pull-with-delivery rules; AI prompt template + composition guide created
- 2026-05-01: vid-thumbnail SCOPE STRIPPED — text planner only, no design. Composition guide reserved for future vid-thumbnail-gen.
- 2026-05-01: thumbnail-text-patterns.md gained real-world examples library (mined combos with channel context)
- 2026-05-01: build-plan.md consolidated — single source of truth at authentic-ai-os root
- 2026-05-01: Section 13 added — plugin packaging strategy locked (one plugin / boundary table / 4 update-safety rules / migration plan)
- 2026-05-01: vid-title built (smallest Phase 3 writing skill, no deps). 3-phase Q-script: load context → 5-10 candidates with BENS+char-count annotations → creator picks → save to meta.md. Anti-fabrication enforced. Standalone OR sub-skill mode.
- 2026-05-01: vid-title tested 3x. After 1st run produced AI-mash-ups, added READ-ALOUD test as primary filter + 4 new anti-patterns (mid-title periods, invented compound nouns, number-stuffing, parenthetical clutter) + Natural Language Patterns section. 4th test landed natural-sounding titles ("How I Added 40 Pounds To My Squat In 11 Weeks" / "Why I Dropped My Squat 20% To Hit 405"). Also added shape-variety rule (at least 2 candidates use a shape NOT in past winners) and split filters into HARD (auto-reject: fabrication, >50 chars, invented nouns, read-aloud failure) vs SOFT FRICTION (flag and explain, creator decides).
- 2026-05-02: knowledge/intro-architecture.md written (universal 6-part: Top 3 Q's → Hook → Problem/Result → Setup → Transition → Credibility woven in + Visual Proof). 5 hook types, 3 P/R options, banned transition phrases, length targets, format-adaptation map.
- 2026-05-02: 3 format planners written (case-study, news + short-process updated). Each has explicit "Intro adaptation" section.
- 2026-05-02: After feedback, softened all "REJECT" language in format planners + intro-architecture + vid-title. Defaults presented WITH explanations of why they tend to work. Hard rules stay (anti-fabrication, ≤50 chars, invented compound nouns, read-aloud). Soft friction = flag and explain, creator decides. Principle: locking everything as REJECT stifles creativity. Defaults are pattern-matches, not laws.
- 2026-05-04: 4 remaining format planners written (deep-dive, interview, roast, listicle). All 7 format planners now complete in `knowledge/format-planners/`. Each has Intro adaptation table that vid-hook will load when assembling intros.
- 2026-05-05: Workspace renamed `peak-content-ic-tools` → `authentic-ai-os`. Build-plan paths and proposed plugin name updated. Skill files use relative paths so the rename was non-breaking.
- 2026-05-05: vid-foundation Stage 1 fundamentally restructured. Old Stage 1 (Positioning, 4 questions) + Stage 2 (Avatar, 5 questions) merged into a single **Stage 1: Iceberg Discovery**. Adopts the "iceberg" metaphor (top + bottom — same concept as the underlying source curriculum's "umbrella," renamed to carry the visual better). New skill-local reference `iceberg-discovery-method.md` holds the full conversation backbone (6 phases: Opening → Audience Narrowing → Problem Discovery → Iceberg Top → Iceberg Bottom → Final Validation) with one-question-at-a-time rules, problem-vs-solution disappearance probe, urgency 1–10 check, and good/bad-pair pull rules. Stage body in SKILL.md is now tight — loads three references (method + positioning + avatar), drives the conversation per the method file. Output expanded: creator-foundation.md now captures Iceberg Top + Iceberg Bottom (8–12 angles) + Person + Top 3 + Axis owned + optional Known-for word. Renumbered subsequent stages: Credibility 2, Backstory 3, Voice handoff 4, Packaging 5. Total stages dropped from 6 to 5. creator-foundation-template.md updated to match.
- 2026-05-04: Foundation audit + reconciliation pass before building vid-framing/vid-hook. Critical schema drift fixed:
  1. **vid-foundation Stage 5 → handoff to vid-voice-capture.** Stage 5 no longer writes a partial voice-profile.md; it now tells the creator to run vid-voice-capture next. Removed `vid-foundation/assets/voice-profile-template.md` and `vid-foundation/references/voice-capture-methods.md` (now redundant). The two-layer schema (cross-context + 7 context maps) lives only in vid-voice-capture, where it belongs.
  2. **Proof-bank reconciled to 2 types end-to-end.** `proof_type` is now strictly `personal-result | client-win` (about who the result belongs to). Presentation format (static-screenshot / before-after-pairing / live-clip / inline-stat) moved to body section in `proof-entry-template.md`. Updated: `knowledge/proof-capture-guide.md`, `vault-integration.md` proof-type slugs, `proof-entry-template.md` filling instructions, `banks/proof-bank/README.md` tag schema.
  3. **Source-teacher attributions scrubbed ruthlessly.** All `Ed`, `Ed's`, `the source curriculum`, `the source teacher`, named-instructor references gone. Public-figure named creators in calibration material (Hormozi, MrBeast, Matt D'Avella, Nisha, Dan Martell, Iman Gadzhi, Joe Dispenza, Casey Neistat, MKBHD, Marques Brownlee, Taylor Swift, Livin' Leggings, etc.) replaced with niche/category descriptors. Files affected: format-planners (news, interview, listicle, roast), thumbnail-text-patterns, thumbnail-examples-library, thumbnail-composition-guide, story-capture-guide, framework-bank/README, build-plan.md. Locked decision #15 updated to clarify named-creator policy.
  4. **Hook taxonomy reconciled to canonical 5.** Listicle and roast planners no longer reference non-canonical "Confession Hook" or "Visual Demo Hook." Confession framing is now a delivery style on top of Statement Hook. Visual Demo is an emotion brick (not a hook), paired with Statement Hook. The 5 canonical types in intro-architecture.md are the single source of truth.
  Foundation now matches the schemas downstream skills will load. vid-framing and vid-hook can be built against a stable contract.

---

## 13. Plugin packaging strategy

How this system distributes to other creators without overwriting their data on update. **Defer the actual restructuring** until Phase 3 skills land — but build with these rules in mind so we don't paint into a corner.

### Why this matters

When the system ships to other creators, three things must hold:
1. The creator gets updates when the plugin updates (skills, knowledge, bug fixes flow in).
2. **The creator's own data never gets overwritten.** Their foundation docs, captured stories, winning packages, content pieces — these are theirs. A plugin update touches none of it.
3. The structure is simple enough that a creator can install with one command and get to work.

Claude Code plugins solve all three IF the plugin/workspace boundary is clean. If we blur it (e.g. ship the user's banks alongside the skills), updates either wipe creator data or stop being safe. Get the boundary right.

### How Claude Code plugins actually work

- Plugins live cached at `~/.claude/plugins/cache/{marketplace}/{plugin}/` on the creator's machine
- **Plugin files are read-only.** On update, the cache directory is replaced wholesale.
- The creator's project workspace (their `foundation/`, their `banks/`, their `Content/`) is in a totally different location and never touched by Claude Code's plugin system.
- Skills inside the plugin reference internal assets via `${CLAUDE_PLUGIN_ROOT}/...` — this resolves to the plugin's cache location regardless of where the user invokes from.

So the question becomes: **what goes in the plugin** (read-only, updates flow in) vs **what goes in the creator's workspace** (writable, updates never touch).

### The plugin/workspace boundary

| Component | Lives in | Why |
|---|---|---|
| All `.claude/skills/vid-*/SKILL.md` and `references/` and `assets/` | **Plugin** | Skill logic. Updates roll out fixes and improvements. |
| `knowledge/` (vault-integration, frameworks, format planners, examples library, schemas) | **Plugin** | Universal reference. Same for every creator. Updates flow in. |
| Bank README templates (the structure docs) | **Plugin assets**, scaffolded INTO workspace on first run | Read-only documentation, but the creator might want to annotate them. Ship as templates. |
| `foundation/creator-foundation.md`, `voice-profile.md`, `packaging-system.md` | **Workspace** | Creator's identity. Owned by them. Plugin never overwrites. |
| `banks/{type}/{slug}.md` (actual entries) | **Workspace** | Creator's captured material. Owned by them. |
| `banks/title-bank.md`, `pattern-bank.md`, `hook-bank.md`, `transition-bank.md` (creator-specific patterns) | **Workspace** | Creator's adapted patterns. Owned by them. Seed file ships with plugin and gets copied once on first run. |
| `Content/pieces/{slug}/*` | **Workspace** | Creator's videos. Owned by them. |
| `People/{name}.md` | **Workspace** | Creator's client profiles. Owned by them. |
| `CLAUDE.md` (vault rules) | **Plugin ships a template; workspace owns the active file** | Creator may customize. Plugin ships a reference version. |
| `build-plan.md` (this file) | **Plugin** (as documentation) | Project plan. Read-only for creators. |

### File-by-file allocation when packaged

```
~/.claude/plugins/cache/peak-systems/authentic-ai-os/         ← THE PLUGIN (read-only)
├── .claude-plugin/
│   └── plugin.json                                            ← name, version, description
├── skills/                                                    ← all 14 skills
│   ├── vid-foundation/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── assets/
│   │       ├── creator-foundation-template.md
│   │       ├── voice-profile-template.md
│   │       ├── packaging-system-template.md
│   │       ├── title-bank-seed.md
│   │       └── bank-readmes/                                  ← scaffolded to workspace on first run
│   │           ├── story-bank-README.md
│   │           ├── proof-bank-README.md
│   │           ├── testimonial-bank-README.md
│   │           ├── metaphor-bank-README.md
│   │           ├── framework-bank-README.md
│   │           └── packaging-bank-README.md
│   ├── vid-capture/
│   ├── vid-voice-capture/
│   ├── vid-thumbnail/
│   └── ... (all other vid- skills)
├── knowledge/                                                 ← universal reference, plugin-owned
│   ├── vault-integration.md
│   ├── BENS-framework.md
│   ├── gift-framework.md
│   ├── thumbnail-strategy-menu.md
│   ├── thumbnail-text-patterns.md
│   ├── thumbnail-examples-library.md
│   ├── thumbnail-composition-guide.md
│   ├── format-rotation-guide.md
│   ├── format-planners/{7 files}
│   ├── voice-extraction-methods.md
│   ├── voice-pressure-test.md
│   ├── voice-profile-schema.md
│   ├── story-capture-guide.md
│   ├── metaphor-builder.md
│   ├── proof-capture-guide.md
│   └── testimonial-capture.md
├── docs/
│   ├── README.md
│   ├── build-plan.md (this file)
│   └── installation.md
└── CLAUDE.md.template                                         ← scaffolded to workspace on first run

~/projects/{creator-name}/                                     ← CREATOR'S WORKSPACE (never touched by plugin updates)
├── CLAUDE.md                                                  ← scaffolded once from template, creator owns
├── foundation/                                                ← created by vid-foundation
│   ├── creator-foundation.md
│   ├── voice-profile.md
│   └── packaging-system.md
├── banks/                                                     ← scaffolded once, creator-owned
│   ├── story-bank/
│   │   ├── README.md                                          ← scaffolded from plugin, creator owns
│   │   └── {their entries}.md
│   ├── proof-bank/
│   │   ├── README.md
│   │   ├── assets/
│   │   └── {their entries}.md
│   ├── testimonial-bank/
│   ├── metaphor-bank/
│   ├── framework-bank/
│   ├── packaging-bank/
│   ├── title-bank.md                                          ← scaffolded from seed, creator-owned
│   └── pattern-bank.md
├── Content/
│   ├── pieces/{slug}/...
│   ├── ideas/
│   └── sequences/
└── People/{name}.md
```

### Update safety rules — non-negotiable

**Rule 1: Skills never write to a workspace file that already exists without explicit creator approval.**

Pattern (used throughout the codebase already):
```
Silent check: read `foundation/creator-foundation.md` if it exists.
→ If exists: surface the first line and ask refresh / keep / replace.
→ If missing: create fresh.
```

Same rule applies to bank README scaffolding, title-bank seeding, CLAUDE.md scaffolding. **Existence check before write. Always.**

**Rule 2: Plugin updates do not touch the creator's workspace.** This is enforced by Claude Code's plugin system (the plugin cache is a different filesystem location from the creator's workspace), but skills also can't reach into the plugin cache to modify it — they reference plugin files via `${CLAUDE_PLUGIN_ROOT}` for read-only.

**Rule 3: First-run scaffolding is the ONLY time files copy from plugin → workspace.** After that, the creator owns those files. If a future plugin version updates a bank README schema, the creator decides whether to refresh — the plugin doesn't decide for them.

**Rule 4: All skill-internal references use `${CLAUDE_PLUGIN_ROOT}` prefix when packaged.** During development (current state), they use relative paths from the workspace. Migration step changes these.

### How bank READMEs work post-packaging

Currently in `authentic-ai-os/banks/{name}/README.md`. After plugin packaging:

- **Source of truth (read-only):** `${CLAUDE_PLUGIN_ROOT}/skills/vid-foundation/assets/bank-readmes/{name}-README.md`
- **Working copy (creator owns):** `{workspace}/banks/{name}/README.md`

When `vid-foundation` runs first time:
1. Check if `{workspace}/banks/story-bank/README.md` exists
2. If missing → copy from `${CLAUDE_PLUGIN_ROOT}/skills/vid-foundation/assets/bank-readmes/story-bank-README.md`
3. If present → leave alone (creator owns it now)

When the plugin updates and the bank README schema changes:
1. Plugin update happens (cache replaced) — workspace untouched
2. Next `vid-foundation` run flags: "The plugin's `story-bank` README schema changed since you last scaffolded. Want to see the diff and decide what to update?"
3. Creator decides per-file. Plugin never auto-updates.

### Migration plan from current state to plugin form

**Stay in current state until Phase 3 writing pipeline is built.** Restructuring now slows down skill iteration. The current authentic-ai-os layout is fine for development.

When ready to package (after vid-pipeline ships):

**Step 1: Create plugin directory structure**
```
authentic-ai-os/
├── .claude-plugin/plugin.json
├── skills/         ← copy from authentic-ai-os/.claude/skills/vid-*
├── knowledge/      ← move from authentic-ai-os/knowledge/
├── docs/           ← copy build-plan.md, README.md
└── CLAUDE.md.template ← copy current CLAUDE.md
```

**Step 2: Path-prefix migration in skills**

Every reference in SKILL.md files like:
```
load `knowledge/vault-integration.md`
```

Becomes:
```
load `${CLAUDE_PLUGIN_ROOT}/knowledge/vault-integration.md`
```

Roughly 30-50 path edits across 14 skills. Mechanical work.

**Step 3: Move bank READMEs to plugin assets**

```
authentic-ai-os/banks/story-bank/README.md
  → authentic-ai-os/skills/vid-foundation/assets/bank-readmes/story-bank-README.md
```

**Step 4: Add scaffolding logic to vid-foundation**

vid-foundation gets a new step: after creating the foundation docs, check if banks/ READMEs exist in the workspace; if any are missing, copy from `${CLAUDE_PLUGIN_ROOT}/skills/vid-foundation/assets/bank-readmes/`.

**Step 5: Plugin manifest**

`.claude-plugin/plugin.json`:
```json
{
  "name": "authentic-ai-os",
  "version": "1.0.0",
  "description": "Video content operating system for YouTube creators — foundation, capture, voice, packaging, and per-video pipeline skills.",
  "author": { "name": "Billy Rybka / Peak Systems" },
  "keywords": ["content", "youtube", "video", "creators", "scripting", "packaging"]
}
```

**Step 6: Test locally before publishing**

```
claude --plugin-dir ./authentic-ai-os
```

Run each skill against a fresh test workspace. Confirm:
- Skills load without path errors
- Bank READMEs scaffold correctly on first run
- Subsequent runs DON'T overwrite scaffolded files
- Knowledge references resolve via `${CLAUDE_PLUGIN_ROOT}`

**Step 7: Publish via marketplace**

Create a marketplace.json in a Git repo (could be a separate `peak-plugins` repo). Add the plugin entry. Tag the release `authentic-ai-os--v1.0.0`.

Creators install via:
```
/plugin marketplace add github:peak-systems/peak-plugins
/plugin install authentic-ai-os@peak-systems
```

### Versioning rules going forward

- `1.0.x` — bug fixes, doc tweaks, knowledge file corrections (no new fields, no schema changes)
- `1.x.0` — new skills, new knowledge files, new bank types
- `2.0.0` — breaking schema changes (e.g. foundation doc fields renamed). Trigger a migration message on first run after upgrade.

Tag every release in Git: `authentic-ai-os--v{version}`.

### What this means for current development

Don't worry about plugin packaging yet. But when adding new skills or knowledge files, build them with these mental models:

1. **Knowledge files = universal.** Going to ship to every creator. Don't put creator-specific data here.
2. **Banks = creator-specific.** Don't ship pre-populated entries. Banks ship empty (with READMEs as scaffolding).
3. **Skills should never assume a path layout that wouldn't work post-`${CLAUDE_PLUGIN_ROOT}` migration.** Don't reach across the workspace to read another skill's internal files — go through `${CLAUDE_PLUGIN_ROOT}` (during dev, this is just the relative `knowledge/` and skill-local paths; will become explicit later).
4. **Anything that scaffolds into the user workspace** should be in a skill's `assets/` folder — that's where templates live in the plugin model. We're already doing this for foundation templates; bank READMEs should move there during migration.

If we hold these rules during the rest of Phase 3, the migration is mechanical when we get there.

---

## How to resume work after a break

1. Read this file, top to bottom.
2. Check the Skills inventory (Section 4) for what's `⬜` next in the build order.
3. Check open questions (Section 10) — anything blocking the next skill?
4. Build the smallest unblocked thing first. Don't batch.
5. After building, update Section 4 (status), Section 12 (work log), and any relevant Section 10 entries.
6. The recent work log gets new entries dated; old entries stay. Decisions log via dated bullets — never delete history.
