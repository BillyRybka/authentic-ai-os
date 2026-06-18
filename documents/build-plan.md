---
type: project-doc
doc: build-plan
project: authentic-ai-os
status: active
last_refreshed: 2026-05-08
tags: [project, build-plan, architecture, roadmap]
---

# Authentic AI OS Build Plan

The single source of truth for what this is, what's done, what's next, and how it all fits together. Read this before resuming work, before adding skills, before refactoring anything structural.

---

## 1. Context

### What we're building

A productizable Claude Code skill system that takes any expertise-based YouTube creator from idea to filming-ready script in roughly an hour, in their actual voice. Built as an Obsidian-native vault. Every artifact links into the graph. Every story captured once auto-surfaces at script-writing time. Every winning thumbnail logs back into the bank for future reference.

The point is not to make "AI content." The point is to amplify the creator's authentic expertise without sanding off their specificity, weirdness, phrasing, lived proof, or hard-earned taste. AI does the heavy lifting of organizing, drafting, pressure-testing, and assembling. The knowledge, stories, standards, language, and judgment come from the creator.

### Who it's for

Two audiences, one product:

- **The creator using the system**, an expertise-based YouTube business owner who runs the skills against their own workspace. They install the template, run setup once, then use per-video skills weekly to ship content. Over time they grow the workspace into the place they run their business.
- **Billy (Peak Systems)**, the first creator AND the system designer. authentic-ai-os is both the product template AND Billy's personal test workspace. Once the system works for him, the same template ships to other creators with their own foundation docs.

### What success looks like

A creator can:

1. Install the template, run `vid-foundation` once → produces creator-foundation.md and packaging-system.md, then hands off to `vid-voice-capture` for voice-profile.md
2. Capture stories / proofs / metaphors / testimonials anytime via `vid-capture` → grow evergreen banks
3. Run `vid-pipeline` per video → idea-to-filming-ready-script in ~60 minutes
4. Post-publish, run `vid-measurement` → log winners back into banks, refine the loop
5. Read the script aloud and not reword a single sentence (the voice is theirs, not Claude's)

### Where this lives

- **Product template:** `c:/Users/billr/projects/authentic-ai-os/`. The standalone, distributable workspace. Has `.claude/skills/`, `knowledge/`, `banks/`, etc. This IS the product.
- **Development reference path (read-only, not shipped):** the underlying study material lives at a path outside this product workspace. Consulted during development. Read-only. Never shipped or referenced in productized output. All content in skill files is stripped of attribution per the productization rule.

---

## 2. Architecture

### Three-layer architecture

**Layer 1: Foundation Docs**, created once per creator and selectively loaded by downstream skills when a decision needs identity, voice, or packaging context. The creator's identity codified without forcing every skill to carry every field.

- `foundation/creator-foundation.md`: positioning, avatar, top 3 problems, credibility brags, backstory
- `foundation/voice-profile.md`: the thin voice guardrail (fingerprint, signature phrases, refusals, POV/energy). No statistics. Populated by `vid-voice-capture`.
- `foundation/packaging-system.md`: starting packaging defaults, format rotation, thumbnail strategy tests, design guardrails
- `foundation/reference-pieces/{voice_context}.md` (one file per populated context, passages as `## ` sections), the voice engine: real creator passages, the generation seed writing skills write from. Populated by `vid-voice-capture`.
- `foundation/channel-audit.md`: optional, existing channels only

**Layer 2: Evergreen Banks**, grow continuously. Every script pulls from these.

- `banks/story-bank/`: narrative entries (Problem-Action-Outcome)
- `banks/proof-bank/`: creator's own evidence (numbers, screenshots, credentials)
- `banks/testimonial-bank/`: other people's words about the creator
- `banks/metaphor-bank/`: analogies and comparisons
- `banks/framework-bank/`: creator's own named systems / rules / methods
- `banks/packaging-bank/`: winning title+thumbnail combos (own + studied outliers)
- `banks/title-bank.md`: fill-in-the-blank title patterns (file, not folder)
- `banks/pattern-bank.md`: research synthesis and pattern pointers, built by `vid-research`

**Layer 3: Per-Video Content**, Obsidian content pieces.

- `Content/pieces/{slug}/`: idea, brain-dump, reference-block, script, thumbnail-brief, pressure-test, meta. All wikilinked, frontmatter'd, tagged.

### Skill architecture: orchestrator + sub-skills

Confirmed best practice for creative work, learned from analyzing the original `youtube-pipeline` mega-skill.

- ~150-line orchestrator (`vid-pipeline`) that ROUTES and delegates. Pure delegator. Never duplicates sub-skill logic.
- ~100-400 line sub-skills that each do ONE unit of work. Independently invokable AND callable by the orchestrator.
- One source of truth per domain. When STRUCTURE phase needs a hook, it INVOKES `vid-intro`; the same `vid-intro` runs again at SCRIPT phase if revision is needed. No duplicate hook logic in the orchestrator.

This pattern is the locked architectural decision. Don't break it by inlining sub-skill logic into `vid-pipeline` to "save a step."

### Reference / knowledge strategy

Three buckets:

**Skill-local references** (`.claude/skills/{skill}/references/`): packaged reference files only that skill needs. If a file in this folder becomes useful to a second skill, move it to `knowledge/` instead of having the second skill reach into the first skill's folder.

**Shared knowledge** (`knowledge/` at workspace root): packaged reference files multiple skills need. Format planners, vault-integration.md, BENS framework, gift framework, thumbnail strategy, format rotation, audience temperature, and any reusable examples live here.

**Creator workspace outputs** (`foundation/`, `banks/`, `Content/`, `People/`): creator-specific files that skills read and write. These may be used by many skills, but they are not packaged reference material. They belong to the creator and the plugin never overwrites them.

The placement rule:

- One skill uses a packaged reference file: keep it under that skill.
- Two or more skills use a packaged reference file: put it in `knowledge/`.
- A file stores the creator's actual answers, patterns, stories, videos, people, or measured results: keep it in the workspace, even if many skills read it.
- No skill should read another skill's private `references/` folder. If it needs that material, promote the file to `knowledge/` and update both skills.

Why split this way: skills evolve independently; shared concepts need one home so updates propagate. Creator-owned data needs a separate home so plugin updates never overwrite it. Don't copy-paste references across skills.

### Source-material discipline

Every skill must be grounded in the underlying study material before it is built or materially changed. "Grounded" means the builder has read the relevant source files directly, extracted the usable operating patterns, and translated them into productized instructions without attribution leakage.

For each skill build, complete this source pass before drafting the skill:

1. **Find the relevant source files.** Start at the development reference path on the builder's machine, then narrow to the modules, shared materials, notes, transcripts, or framework files that map to the skill's job.
2. **Extract operating patterns, not lessons.** Pull what the skill must DO: decision rules, prompt questions, examples, anti-patterns, structure shapes, and judgment checks.
3. **Convert into runnable guidance.** Reference files should read like calibration sheets for Claude at runtime, not course notes for the creator.
4. **Scrub attribution.** Productized files must not mention source-curriculum names, teacher names, instructor names, course names, or named public-figure examples. Keep internal source paths in this build plan only.
5. **Record the source dependency.** In this plan, each new skill's build notes should list the source files read and the patterns extracted. That record stays internal so future builders know the skill is source-backed.

If a proposed rule cannot be traced to creator input, source material, observed platform data, or a real downstream need, it is fluff. Cut it.

### Principle traceability standard

Every skill, knowledge file, bank, and handoff needs a traceable reason to exist. The reason can come from four places:

1. **Source principle**, a pattern, framework, or workflow from the underlying study material.
2. **Creator data**, something the creator said, proved, experienced, or repeatedly does.
3. **Platform feedback**, retention, CTR, comments, sales actions, or other observed performance.
4. **AI workflow need**, a constraint needed because AI agents need clearer context, narrower tasks, or better verification than a human collaborator would.

If it cannot be mapped to one of those four, it does not belong in the build plan yet.

Use this check before creating or expanding any file:

| Proposed piece | Must answer |
|---|---|
| New skill | Which repeatable job does it own that no existing skill owns? |
| New knowledge file | Which multiple skills need the same reference? |
| New bank | What reusable creator-owned asset gets captured here? |
| New field | Which downstream decision changes because this field exists? |
| New example | Which rule boundary does this example make easier to apply? |
| New agent | Which failure mode does this agent catch better than the main writer? |

The current source-principle map:

| Build-plan piece | Source / workflow anchor | Productized interpretation |
|---|---|---|
| `vid-foundation` | Positioning basics, top-of-umbrella/iceberg, avatar problems, credibility and backstory setup | Lock creator identity once so downstream skills do not invent positioning or audience language |
| `vid-voice-capture` | "Update the AI brain" and creator-specific guardrails | Build the creator's AI brain from real speech/writing sources, not generic style adjectives |
| `vid-capture` | Story/proof/metaphor lessons, minimum viable story, proof through lived examples | Capture reusable raw material when it appears so scripts pull from owned experience |
| `vid-title` | BENS, outlier title patterns, warning not to use AI title suggestions verbatim | Generate options from proven shapes, then filter through creator judgment and read-aloud fit |
| `vid-thumbnail` | Gift framework, thumbnail strategy, text/image separation, no fabricated numbers | Plan only the text promise and rationale; design/generation happens elsewhere |
| `vid-research` | Three-circle research, outlier study, repeat what works, anti-fluke checks | Build pattern banks from real channel evidence so framing and packaging are not guesses |
| `vid-intake` | Creator-owned raw material, iceberg fit, Top 3 problem alignment | Capture the creator's exact words before the system tries to frame or write the video |
| `vid-intro` | Intro architecture, top 3 viewer questions, IntroBot feedback loop | Write and review the opening against viewer questions, title promise, and voice profile |
| `vid-segment` | Setup/Tension/Payoff, parables, principles, cut when the viewer gets it | Build points that change belief without over-explaining |
| `vid-ending` | CTA and end-screen lessons, bridge to next best action | Make the ending feel like the logical next step, not a bolted-on pitch |
| `vid-framing` | Guardrails AI alignment scoring and research pattern bank | Decide whether an idea is worth making before spending writing effort |
| `vid-structure` | Keep/cut/combine planning, format templates as reusable layer | Assemble the skeleton without duplicating title, intro, or segment logic |
| `vid-pressure-test` | IntroBot/PointBot feedback, script roasting, color-code review | Run focused reviewers that catch drift, bloat, missing payoffs, and AI-sounding prose |
| `vid-measurement` | 3-hour / 7-day / 30-day checkpoints, retention as research | Turn performance data into updates to banks and future decisions |
| `vid-monthly-review` | Pattern learning over time, AI brain should change every 6 months | Refresh the system from observed patterns, not opinions |
| `vid-thumbnail-gen` | AI thumbnail workflow and creation-path selection | Optional generation layer only after the text promise and visual constraints are locked |

### AI-first workflow standard

This is not a human process copied into Claude. It is an AI-first workflow that preserves human judgment.

Humans can carry fuzzy context in their heads. AI agents cannot. They need:

- narrow jobs
- explicit inputs
- clear stop conditions
- small context packets
- examples that teach boundaries
- verification loops that catch plausible nonsense

Every skill should follow this rhythm:

1. **Load only the minimum context needed for the next decision.**
2. **Ask for missing creator-owned inputs before guessing.**
3. **Generate multiple useful options when exploration helps.**
4. **Use source-backed examples to expand creative range, not constrain it.**
5. **Let the creator choose or correct the direction.**
6. **Save the locked decision in a structured field.**
7. **Pass forward only the fields downstream skills need.**

Good AI-first example:

`vid-framing` loads creator-foundation, packaging-system, the brain dump, and the relevant pattern bank. It produces 3-5 possible framings, each with source-backed rationale and a risk note. The creator chooses one. Only the selected framing, rejected alternatives, format, core payoff, and viewer-stage decision move forward.

Why it works: AI explores more angles than the creator would manually, but the locked context stays small.

Bad AI-first example:

`vid-framing` writes a 2,000-word strategy memo and passes the entire memo to every downstream skill.

Why it fails: downstream agents inherit too much prose, summarize instead of decide, and start sounding like the memo instead of the creator.

### Context budget rule

Context is a budget, not a closet.

Each skill must declare:

| Context type | Rule |
|---|---|
| Required inputs | Load every time. The skill cannot work without them. |
| Conditional inputs | Load only when the artifact exists or the format needs it. |
| Forbidden inputs | Do not load because they create noise or duplicate another skill's job. |
| Output packet | The smallest set of fields the next skill needs. |

Example context packet from `vid-intro` to `vid-structure`:

```yaml
intro_packet:
  locked_hook: "..."
  intro_strategy: problem-poke | result-tease | combined
  top_3_questions_used:
    - "..."
    - "..."
    - "..."
  proof_used:
    - "[[proof-slug]]"
  voice_check: pass | needs_creator_revision
```

Do not pass the entire intro reference file. Do not pass every foundation field. Pass the result of the decision.

### Creative constraint rule

Examples should increase creativity, not shrink it.

Use examples as shape libraries:

- **Match the underlying move**, not the literal words.
- **Show multiple niches** so Claude does not overfit to one category.
- **Include near-misses** so Claude understands the boundary.
- **Allow creator-approved deviations** when the deviation strengthens voice, proof, or delivery.

The "iceberg" language is approved as the creator-facing name for the source material's umbrella/top-bottom positioning idea. It is a translation, not an invention. The underlying principle stays the same: own one clear top-level promise while keeping a broad bottom of related subtopics. This kind of rename is allowed when it makes the system easier for the creator to use without changing the source logic.

Bad constraint:

"Use this exact hook formula every time."

Good constraint:

"Here are five hook shapes. Pick the one that fits the title promise, viewer question, and creator's natural speaking style. If none fit, create a new hook and explain which source-backed principle it preserves."

### Human vs. AI-sounding script standard

Every writing skill needs a way to recognize AI-sounding prose.

AI-sounding script:

> "In today's video, we're going to dive into the powerful strategies that can help you unlock your true potential and transform the way you approach content creation."

Why it fails: generic promise, no lived context, inflated verbs, could belong to anyone, no specific tension.

Human-sounding script:

> "Most people don't have a content problem. They have a 'I forgot what I actually know' problem. So they ask AI for ideas, and AI gives them the same beige list it gave everybody else."

Why it works: specific belief, plain phrasing, creator point of view, concrete enemy, natural spoken rhythm.

AI-sounding script:

> "This framework is designed to streamline your workflow and ensure optimal results across every stage of the process."

Why it fails: corporate abstraction, no viewer pain, no visual, no proof.

Human-sounding script:

> "If the AI needs a 4-page prompt to remember who you are, you don't have a system yet. You have a very polite memory problem."

Why it works: memorable line, clear critique, specific image, sounds sayable.

The test is not "does this sound casual?" The test is: would this specific creator naturally say this sentence while making this specific point?

### Multi-agent orchestration standard

Use multiple agents when different judgment lenses can run in parallel and catch different failure modes. Do not spawn agents just to make the process look sophisticated.

Good times to use multiple agents:

| Moment | Agents worth using | Why |
|---|---|---|
| After a skill draft is written | Source-faithfulness reviewer, context-bloat reviewer, schema reviewer | Catches unsupported invention, unnecessary context, broken contracts |
| After `vid-framing` creates options | Alignment reviewer, novelty reviewer, risk reviewer | Checks fit to iceberg/top problems, whether the angle is fresh, and whether the idea is thin |
| After `vid-intro` draft | Voice reviewer, intro-architecture reviewer, AI-slop reviewer | Checks creator voice, source structure, and generic phrasing |
| During `vid-segment` review | Setup-payoff reviewer, proof reviewer, compression reviewer | Catches unresolved setups, unsupported claims, and over-explanation |
| During `vid-pressure-test` | Source alignment, voice authenticity, retention logic, offer/CTA alignment | Focused adversarial pass before the creator films |
| After publish data comes in | Measurement analyst, pattern-miner, bank-updater | Separates diagnosis, pattern extraction, and durable system updates |

Bad times to use multiple agents:

- During creator identity capture, where too many reviewers can muddy the creator's own words.
- Before the creator has made a core choice, because agents will optimize every branch and bloat the session.
- For simple file-scaffolding tasks where deterministic checks are enough.
- When the task needs one clear owner and fast execution.

Default `vid-pressure-test` agent set:

1. **Source Alignment Reviewer**: does the script preserve the source-backed structure and format logic?
2. **Creator Voice Reviewer**: does it sound like this creator, using their voice profile and brain dump?
3. **AI-Slop Reviewer**: flags generic phrasing, inflated verbs, abstract transitions, and empty "value" language.
4. **Viewer Retention Reviewer**: checks unresolved setups, early payoffs, over-explaining, and weak transitions.
5. **Proof / Claim Reviewer**: verifies numbers, results, testimonials, and claims trace to source artifacts.

Each agent returns only:

```yaml
reviewer:
  verdict: pass | revise | block
  top_3_issues:
    - issue: "..."
      evidence: "line or section"
      fix: "specific edit"
  do_not_change:
    - "what is already working"
```

No long essays. No rewriting the whole script unless explicitly asked. Reviewers diagnose; the main writing skill integrates.

### Context handoff discipline

Context handoff is allowed only when the receiving skill or artifact uses the information to make a better decision. Passing context "because it might be useful" creates mushy prompts and generic output.

Every handoff must answer four questions:

| Question | Required answer |
|---|---|
| Who consumes it? | The specific downstream skill, artifact, or bank |
| What decision does it improve? | The concrete choice it affects |
| What exact field is passed? | Filename + field/section, not a vague document reference |
| What happens if it is missing? | Fallback, ask-user behavior, or stop condition |

Positive handoff example:

`vid-framing` writes the framing decisions into `Content/pieces/{slug}/piece.md` (frontmatter fields: `format`, `core_payoff`, `viewer_stage`, `selected_angle`, `goal`, `outlier_anchor`, `anchor_confidence`). `vid-intro` consumes those fields to choose intro length, Problem/Result balance, hook type, and transition style. This works because each field changes an actual writing decision. piece.md is the main per-piece ledger. Every skill in the pipeline appends to it.

Negative handoff example:

`vid-intro` receives "all prior notes about the creator" and tries to infer the hook from everything. This fails because the receiving skill has no clear decision boundary. It invites summary, repetition, and generic AI-sounding glue.

Positive source handoff example:

`vid-foundation` captures `top_3_perceived_problems` in `foundation/creator-foundation.md`. `vid-intro` uses those exact problems to shape the opening questions and problem poke. This works because viewer-language collected once becomes reusable pressure in every script.

Negative source handoff example:

`vid-foundation` passes a broad "audience avatar summary" to every writing skill, and each skill independently chooses what matters. This fails because the same vague blob gets reinterpreted differently and weakens consistency across the system.

### Example standard

Every skill reference should be example-heavy and contrastive.

Required shape:

1. **Positive examples**: multiple examples showing the pattern working in different niches or content formats.
2. **Why it works**: one tight explanation tied to the actual decision rule.
3. **Negative / near-miss examples**: examples that look plausible but fail.
4. **Why it fails**: one tight explanation that teaches the boundary.
5. **Application instruction**: how Claude should adapt the shape to the creator's own voice and source material.

Example of a good reference entry:

| Type | Example |
|---|---|
| Positive | "I rebuilt my offer around one painful moment: the sales call where the prospect says yes emotionally but disappears after seeing the proposal." |
| Why it works | Specific moment, real tension, clear business stakes, sounds like a person describing something they lived. |
| Near-miss | "This video is about how to improve your offer so prospects convert better." |
| Why it fails | Abstract, category-level, no lived moment, sounds like a topic label instead of a creator's point of view. |

One positive and one negative is the minimum. Multiple positives and multiple near-misses are the standard for high-load skills like `vid-foundation`, `vid-intro`, `vid-segment`, and `vid-framing`.

### Format-aware writing

Each writing sub-skill (`vid-intro`, `vid-segment`, `vid-ending`) reads the video's format from `piece.md` and loads the matching planner from `knowledge/format-planners/`. Different formats route through different internal workflows:

- News → bullet workflow, light tension, scripted hook only
- Deep Dive → full word-for-word, heavy STP (Setup-Tension-Payoff)
- Listicle → per-point STP
- Roast → scripted frames + bullet riff zones
- Short Process → tight STP
- Case Study → P-A-O tension, framework payoff
- Interview → scripted intro + question list

The format planner dictates the workflow. Skills don't hardcode format logic. They read the planner.

### Obsidian-native, graph-first

Every artifact follows `knowledge/vault-integration.md`: frontmatter schemas, wikilink contracts, tag conventions, file naming, callout patterns. Stories link to clients (People/), clients link back via Obsidian backlinks, scripts reference the stories they pulled in via `stories_used:` frontmatter, stories update their `used_in:` field with the video slug. Bidirectional. The "update both sides" rule is non-negotiable.

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
6. **Voice handling:** The brain dump IS the voice. Claude structures the creator's actual phrases, never generates from scratch.
7. **Output format:** Format-aware. Each writing sub-skill detects format and routes internally.
8. **Reference strategy:** Skill-local in each skill's `references/` folder; truly cross-skill in `knowledge/` at root.
9. **Examples-heavy, contrastive:** Every reference doc (every skill prompt, every guide, every pattern library) leads with **real examples** before principles. Wherever a rule exists, show a worked example AND a near-miss with a one-line "why this lands / why this doesn't." Examples are sourced from the underlying study material, creator banks, or observed real-world examples. **Never attributed in productized files.** Principles without examples are abstract; rules without counter-examples are formulaic. Examples are the teaching surface. The creator and Claude both calibrate from them, not from rules.
10. **Orchestrator role:** Pure delegator. Never duplicates sub-skill logic. Invokes the right sub-skill at each phase.
11. **Status updates:** CLAUDE.md instructions, not a skill.
12. **Capture skill:** One combined skill (`vid-capture` for story + proof + metaphor + testimonial + framework). Not separate skills per block tool. Framework added 2026-05-11 as Stage F (Log path only; the 5-step Create flow lives in `knowledge/framework-builder.md`).
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

### Phase 1: Foundation (run once per creator)

The original `vid-foundation` mega-skill was split into a thin orchestrator plus 6 focused interview skills. Each sub-skill owns one unit of work and loads `knowledge/interview-posture.md` for shared conversational posture. Sub-skills run in sequence; each one writes its locked section to `creator-foundation.md` or `packaging-system.md` and then stops.

| Skill | Status | Description | Key dependencies | Files |
|---|---|---|---|---|
| `vid-foundation` | ✅ | Thin orchestrator (~100 lines). Reads `creator-foundation.md` and `packaging-system.md`, routes the creator to the correct next sub-skill in the foundation sequence. Does NOT run interview content itself. | None | `.claude/skills/vid-foundation/SKILL.md` |
| `vid-avatar` | ✅ | Interview locks Offer + Avatar + Top 3 perceived problems in viewer language. First in the foundation sequence. | `knowledge/interview-posture.md`, `knowledge/creator-foundation-template.md` | `.claude/skills/vid-avatar/` (SKILL.md + avatar-guide.md) |
| `vid-positioning` | ✅ | Drafts the Iceberg Statement using WHO + WHAT + HOW + TENSION. Claude drafts 2 candidates after avatar inputs lock, creator reacts. Literal-words rule for tension preserves brand-defining phrases. | Avatar + Top 3 locked | `.claude/skills/vid-positioning/` (SKILL.md + positioning-method.md + positioning-examples.md) |
| `vid-pillars` | ✅ | Locks 8 to 12 content pillars (bottom of the iceberg) that deliver on the Iceberg Statement. Categories of teaching, not video titles. | Iceberg Statement locked | `.claude/skills/vid-pillars/SKILL.md` |
| `vid-credibility` | ✅ | Locks three viewer-relevant brags for video intros. Big + Specific + Personal. Anti-proof check before lock. | Avatar + Top 3 locked | `.claude/skills/vid-credibility/` (SKILL.md + credibility-method.md) |
| `vid-backstory` | ✅ | Locks Problem-Action-Outcome backstory in 1 to 2 paragraphs plus a 3-sentence compressed version. Action-section test catches summary-instead-of-moves failures. | Avatar + Iceberg Statement locked | `.claude/skills/vid-backstory/` (SKILL.md + backstory-method.md) |
| `vid-packaging` | ❌ DELETED 2026-05-19 | Collapsed. No irreducible purpose: evidence fields → `vid-research` authorship, per-video → `vid-title`/`vid-thumbnail`, the title+thumbnail beat → `vid-pipeline`. `packaging-system.md` now authored by vid-research from evidence. Identity residue (design guardrails, creation path) parked, not yet homed. See work-log 2026-05-19. | n/a | removed |
| `vid-voice-capture` | ✅ | Dedicated voice profile build: Layer 1 Core (cross-context patterns) + Layer 2 Context Maps (per-format sub-profiles). Multi-source extraction (transcripts + writing + live monologue). The only skill that creates `foundation/voice-profile.md`. Refresh-aware (90 days / 20+ videos). Built by another session, audited 5/1. | foundation/creator-foundation.md, knowledge/voice-extraction-methods.md, knowledge/voice-pressure-test.md, knowledge/voice-profile-schema.md | `.claude/skills/vid-voice-capture/` (SKILL.md + 2 templates) |
| `vid-capture` | ✅ | Combined story + metaphor + proof + testimonial + framework capture. Runnable standalone OR invoked by another skill mid-script. Dedup check per stage. People stub auto-creation. Invocation-mode aware (standalone loops, sub-skill mode returns wikilink). proof_type simplified to 2 (personal-result / client-win); presentation format moved to body. Stage F (framework) is Log-only. The 5-step build lives in `knowledge/framework-builder.md` and runs inline in vid-segment when mid-write framework crafting is needed. | foundation/creator-foundation.md (Top 3 problems), knowledge/vault-integration.md, capture guides in knowledge/, knowledge/framework-builder.md | `.claude/skills/vid-capture/` (SKILL.md + 5 templates) |

### Phase 2: Research and Pattern Banks

| Skill | Status | Description | Notes |
|---|---|---|---|
| `vid-research` | ✅ | Builds or refreshes pattern banks from own channel, niche competitors, and adjacent niches. Produces three banks: pattern-bank.md (outlier evidence + cross-channel synthesis, loaded by vid-framing for angle selection), title-bank.md (fill-in-the-blank title shapes, loaded by vid-title), power-words-bank.md (lean word list, loaded by vid-title). Thumbnail strategy and visual data live IN pattern-bank outlier rows (no separate thumbnail-patterns-bank file). Three modes: first build, quarterly refresh, single outlier add. | Run after foundation + voice capture and before first `vid-framing` when pattern banks do not exist. Requires YouTube Data API key. |

### Phase 3: Per-video pipeline

Build leaves first, orchestrator last. Writing sub-skills before structure/routing skills before orchestrator.

| Skill | Status | Description | Key dependencies |
|---|---|---|---|
| `vid-thumbnail` | ✅ | Text planner ONLY. Generates 5-10 thumbnail text candidates using the patterns playbook. Creator picks 1-2. Output: brief with picks + strategy + BENS + rationale. Does NOT design the visual (no layouts, hero, expressions, AI prompts). | foundation/packaging-system.md, knowledge/thumbnail-text-patterns.md, knowledge/thumbnail-strategy-menu.md, knowledge/BENS-framework.md, knowledge/gift-framework.md, packaging-bank |
| `vid-title` | ✅ | BENS title generation. Loads creator-foundation, packaging-system, BENS framework, title-bank patterns, and the video's actual material. Generates 5-10 candidates each ≤50 chars and hitting at least one BENS letter. Anti-fabrication enforced (numbers must come from the script). Standalone OR sub-skill (returns title string to caller when invoked by vid-structure). | knowledge/BENS-framework.md, banks/title-bank.md, the video's brain-dump/framing artifact, foundation docs |
| `vid-intro` | ✅ | Full 6-part intro builder: Top 3 viewer questions, Hook, Problem/Result, Setup, Transition, and credibility woven in. Format-aware, title-aware, thumbnail-aware, anti-fabrication. | creator-foundation.md, voice-profile.md, reference-pieces, piece.md, thumbnail-brief.md, brain-dump.md, format-planners/ |
| `vid-segment` | ✅ | Builds one body segment at a time using Setup/Tension/Payoff. Format-aware, pulls stories/proofs/metaphors/testimonials/frameworks, runs structure pass then prose pass before saving. | creator-foundation.md, voice-profile.md, piece.md, brain-dump.md, format-planners/, banks/ |
| `vid-ending` | ✅ | Writes the close using Pivot/Gap/Bridge, recaps the transformation, reveals the next problem, and points to a real next video. Format-aware CTA placement. | creator-foundation.md, piece.md, script.md, voice-profile.md if present |
| `vid-intake` | ✅ | Captures raw video material into brain-dump.md with exact creator phrasing preserved. Auto-detects intake mode, checks iceberg and Top 3 alignment, saves the raw material for downstream skills. | creator-foundation.md, voice-profile.md optional |
| `vid-framing` | ✅ | 3-4 framings (3 anchored + 1 experimental), Core Payoff, format pick from current packaging defaults, goal pick, viewer_stage prediction. Output: framing decisions appended to piece.md. | foundation docs, banks/pattern-bank.md, knowledge/three-circle-research, knowledge/audience-temperature-model, knowledge/outlier-identification-rules |
| `vid-structure` | ✅ | Builds the Tier 1 outline from the brain dump and locked framing: segment purposes, block candidates, tension plan, and script.md skeleton ready for vid-segment. | brain-dump.md, piece.md, creator-foundation.md, format-planners/, banks/ |
| `vid-pressure-test` | ✅ | Catch-and-fix audit before filming. 4 parallel reviewers (source-traceability, voice-authenticity, AI-slop, retention-logic) each return top 3 issues. Interactive approve/deny/skip loop applies fixes to script.md in place. Skip restricted on hard-rule violations (Mark-as-gap path). Light-vet creator rewrites for new violations. Creator read-aloud is the final gate. Audit logged to piece.md frontmatter; no separate pressure-test.md file. | The full script + piece.md + brain-dump + foundation docs + brand.md |
| `vid-pipeline` | ✅ | Thin orchestrator. Routes on field-presence + the canonical `status` lifecycle (`ideating` → `drafting` → `filming-ready`); never writes piece.md itself. Lists in-progress pieces and asks which when given no slug. Title before thumbnail (forced). Voice skills are NOT in the chain. Built 2026-06-18 at `.claude/skills/vid-pipeline/SKILL.md`. | Everything above |

### Phase 4: Feedback skills

| Skill | Status | Description |
|---|---|---|
| `vid-measurement` | ⬜ | 4-checkpoint analysis (CTR, retention through hook, average view duration, end-screen action). Flop diagnosis. Logs winners to packaging-bank. Post-publish. |
| `vid-monthly-review` | ⬜ | Pipeline tracker review + routing decisions. Looks at the full month's data, surfaces patterns. Post-publish. |
| `vid-voice-audit` | 🚧 | THE pre-publish voice check. Reads a finished draft against the creator's actual past sentences and flags any line that fails the read-aloud test. Loads `foundation/reference-pieces/{voice_context}.md` + `foundation/voice-profile.md` + `Context/brand.md`, optionally samples 2-3 raw passages from `raw/voice-sources/` per run (varies between runs so the creator does not start gaming the curated set), scans line by line with severity tiers (hard: words-avoided, anti-patterns, em-dashes, brand-swap misses, breached creator hard rules; soft: rhythm mismatch, energy mismatch, AI-default phrasing). Returns every finding ranked by severity (no top-3 cap) plus a per-beat verdict (passes / soft-flag / would-reword) and a suggested rewrite for each finding. Absorbs the prior voice-authenticity reviewer rubric (the inline pressure-test rubric file was deleted on first build of this skill; content moved to `vid-voice-audit/references/voice-fault-rubric.md`). `vid-pressure-test` invokes `vid-voice-audit` as one of its parallel reviewers instead of running an inline reviewer. Also standalone-callable as the creator's last gate before filming when they want a deeper check than pressure-test's batch run. |
| `vid-voice-update` | 🚧 | Mid-draft voice signal triage and surgical update. Fires when the creator reacts to a line in chat. Triages the signal into three types: **hard rule** ("never use X", "swap Y for Z", "I'd never write that") → appends to `foundation/voice-profile.md` refusals (words-avoided with reason, anti-pattern, or creator hard rule depending on shape), then re-runs the current piece's pressure-test; **one-time edit** ("this line is off here", "doesn't work for this segment") → just rewrites the line in the current draft, saves nothing; **preference shift** ("I don't love that, try something else") → asks the creator "one-time, or should I avoid this generally?" then routes accordingly. Reading the signal correctly is the work. Same target file as `vid-voice-capture` but different scale: capture is a quarterly heavy rebuild from all sources, update is a surgical one-line append in response to a single signal. Loaded by `vid-intro`, `vid-segment`, `vid-ending` as a sibling skill they hand a correction off to. Renamed from `vid-voice-correction-capture` (2026-05-22) for clarity. Not every correction becomes a rule. |

### Phase 5: Optional

| Skill | Status | Description |
|---|---|---|
| `vid-channel-audit` | 🟡 | Existing channels only. Analyzes a creator's current channel state to inform packaging refresh. |
| `vid-thumbnail-gen` | 🟡 | Image generation extension. Takes a brief from vid-thumbnail + creator's AI tool config + their packaging-bank winners. Includes "training mode": creator drops in title+thumbnail winner pairs to teach the generator their style. Optional add-on, requires creator to configure their own AI tool API keys. |

### Phase 6: Session orchestrator (after vid-pipeline lands)

| Skill | Status | Description |
|---|---|---|
| `/assistant` | ⬜ | Content-only session orchestrator. Resume session, save session, reconcile-notes, web extract, route knowledge into the right vault file. Built after vid-pipeline lands. NOT meetings, NOT tasks, NOT daily reviews. Strictly content workflow glue. |

### Synthetic-audience subsystem (parallel track)

Pre-publish copy review using synthetic avatars built from the creator's real call transcripts and YouTube comments. Independent of the vid-* pipeline; integrates only via `Content/pieces/{slug}/`. Has its own dedicated build plan at `documents/synthetic-audience-plan.md` (Columbia Digital Twins Lab method, held-out validation, 4 MVP skills built, Phase 2 deferred).

| Skill | Status | Description | Files |
|---|---|---|---|
| `aud-intake` | ✅ | Ingests call transcripts + YouTube comments. Extracts the 5 moment types from calls. Runs the contamination scan. | `.claude/skills-wip/aud-intake/SKILL.md` |
| `aud-avatar-build` | ✅ | Clusters audience-data into 4-6 segments via bounded interview. Writes held-out files BEFORE drafting avatars. | `.claude/skills-wip/aud-avatar-build/SKILL.md` |
| `aud-validate` | ✅ | Three-test gate per avatar (quote attribution, objection prediction, vocabulary leak). Tiered status. | `.claude/skills-wip/aud-validate/SKILL.md` |
| `aud-review` | ✅ | Runs validated avatars as a panel against a piece. Subagent-isolated. Median-plus-dissent synthesis. | `.claude/skills-wip/aud-review/SKILL.md` |
| Phase 2 (deferred) | 🟡 | `aud-cluster`, `aud-panel-config`, `aud-synthesize`, `aud-feedback-loop`, `aud-survey-design`. See `documents/synthetic-audience-plan.md`. | n/a |

Detailed architecture, source grounding, locked decisions, and Phase 2 spec live in the dedicated plan file. This main build plan acknowledges the subsystem and points at it; it does not duplicate the spec.

**Total:** 21 content skills + the `/assistant` orchestrator. (Phase 1 expanded from 1 mega-skill to 7 skills after the foundation split. Phase 4 expanded to 4 with the voice-family consolidation: `vid-voice-audit` absorbs the pressure-test voice-authenticity reviewer; `vid-voice-update` triages mid-draft corrections.) The synthetic-audience subsystem (`aud-*` skills) is a parallel track with its own build plan in `documents/synthetic-audience-plan.md` and is not counted in this total.

---

## 5. Data flow / dependency map

```
                Foundation Docs (creator-foundation, voice-profile, packaging-system)
                        ↓ selectively loaded by field when a decision needs them
                        ↓
    ┌───────────────────┼───────────────────┐
    ↓                   ↓                   ↓
 vid-capture       vid-thumbnail        vid-pipeline (orchestrator)
    ↓                                       ↓
 BANKS                                  per-phase invokes:
 (story / proof /                       vid-intake → brain-dump.md
  testimonial /                         vid-framing → piece.md (framing fields)
  metaphor /                            vid-title → title locked
  framework /                            vid-thumbnail → thumbnail-brief.md
  packaging)                             vid-structure → script.md skeleton + Blocks-to-capture
    ↓                                   vid-intro → hook in script
    ↓                                   vid-segment (per segment) → script body
    ↓                                   vid-ending → script close
 read by writing skills                 vid-pressure-test → pressure-test.md
 (vid-segment, vid-intro, vid-ending,
  vid-thumbnail)
                                            ↓
                                        Content/pieces/{slug}/
                                        - piece.md (main metadata + framing decisions)
                                        - brain-dump.md
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

- **Foundation docs** are mandatory anchors, not mandatory full-context dumps. Skills load the sections they need for the current decision: positioning / Top 3 problems from creator-foundation, voice rules from voice-profile, packaging constraints from packaging-system.
- **Banks** are the connective tissue. Captured once via `vid-capture`, pulled at script-writing time by writing skills. Bidirectional wikilinks ensure traceability.
- **`packaging-system.md`** drives both `vid-thumbnail` (current thumbnail strategy tests + design guardrails) and the format-planner selection in writing skills. It stores first defaults and later updates from research or performance data, not final rules.
- **`title-bank.md`** is read by `vid-title` (patterns to adapt). Updated by `vid-measurement` (winning patterns get logged).
- **`packaging-bank/`** is read by `vid-thumbnail` (style anchors for past winners + studied outliers). Updated by `vid-measurement` post-publish.

### How the orchestrator delegates (the pattern)

`vid-pipeline` reads one piece's `piece.md` plus the presence of its sibling files, decides the next step from that state, and invokes the responsible skill. It never does the work itself, not even "lightweight logic." The next-step decision is field-presence, not a stored micro-status:

- no `selected_angle` → `vid-framing`
- `selected_angle`, no `title` → `vid-title`
- `title`, no `thumbnail-brief.md` → `vid-thumbnail`
- `thumbnail-brief.md`, no `segment_purposes` → `vid-structure`
- `segment_purposes`, no `intro_locked` → `vid-intro`
- `intro_locked`, `segments_completed` count < `segment_purposes` count → `vid-segment` (next unwritten segment)
- segments complete, no `ending_locked` → `vid-ending`
- `ending_locked`, `status` not `filming-ready` → `vid-pressure-test`
- `status: filming-ready` → done

Packaging (title then thumbnail, in that order) runs after framing and before structure. A weak package is where the creator stops, before any time goes into scripting. Title comes first because the thumbnail must avoid repeating the title's words.

The sub-skill owns its work AND its writes. `vid-structure` mines the brain-dump, runs keep/cut/combine, surfaces block candidates, writes the `## Blocks to capture` manifest, and saves the skeleton; the orchestrator just invoked it. When the script phase runs, `vid-intro` writes the hook, `vid-segment` each body section, `vid-ending` the close. Each writes its own `piece.md` fields in both standalone and pipeline mode, so the orchestrator can always re-read true state. Title and thumbnail are never re-opened here.

---

## 6. Build sequence (current state forward)

### Step 1: Knowledge layer first ✅ (mostly done)

The references downstream skills will load. Build before the skills that need them.

- [x] `knowledge/vault-integration.md`: frontmatter schema, wikilink contracts
- [x] `knowledge/BENS-framework.md`: Big/Easy/New/Safe title logic
- [x] `knowledge/gift-framework.md`: wrapping/box/gift packaging philosophy
- [x] `knowledge/format-rotation-guide.md`: Rule of 3+1
- [x] `knowledge/thumbnail-strategy-menu.md`: 6 strategies, format-strategy pairing
- [x] `knowledge/thumbnail-text-patterns.md`: 5 winning patterns + anti-patterns + examples library + title-thumbnail pairing
- [x] `knowledge/thumbnail-composition-guide.md`: visual composition (reserved for vid-thumbnail-gen, not loaded by vid-thumbnail)
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
- [x] `knowledge/voice-rhythm.md` ✅

### Step 2: Phase 1 foundation skills ✅ (done)

- [x] `vid-foundation`
- [x] `vid-voice-capture`
- [x] `vid-capture`

### Step 3: Bank READMEs ✅ (done)

- [x] `banks/story-bank/README.md`
- [x] `banks/proof-bank/README.md`
- [x] `banks/testimonial-bank/README.md`
- [x] `banks/metaphor-bank/README.md`
- [x] `banks/framework-bank/README.md`
- [x] `banks/packaging-bank/README.md`
- [ ] `banks/title-bank.md`: exists as a seed file from vid-foundation; expand patterns over time
- [ ] `banks/pattern-bank.md`: workspace output, created by `vid-research` when the creator runs it
- [x] `banks/hook-bank.md` ✅
- [x] `banks/transition-bank.md` ✅

### Step 4: Research skill ✅ (done)

- [x] `vid-research` ✅ (first build / quarterly refresh / single outlier add)

### Step 5: Phase 3 writing pipeline

Build in dependency order. Writing sub-skills before structure/routing before orchestrator.

- [x] `vid-title` ✅ (smallest, no deps, built and tested through 4 iterations)
- [x] All 7 format planners ✅ (case-study, deep-dive, interview, listicle, news, roast, short-process)
- [x] `knowledge/intro-architecture.md` ✅
- [x] `knowledge/voice-rhythm.md` ✅
- [x] `vid-intro` ✅
- [x] `vid-segment` ✅
- [x] `vid-ending` ✅
- [x] `vid-intake` ✅
- [x] `vid-framing` ✅
- [x] `vid-structure` ✅
- [ ] **`vid-pressure-test` ← NEXT**
- [ ] `vid-pipeline` (orchestrator, build last)

**Current remaining core build items:**
1. `vid-pressure-test`: focused adversarial reviewers for source alignment, creator voice, AI-slop, retention logic, and proof/claim traceability.
2. `vid-pipeline`: orchestrator that routes through the built per-video skills without duplicating their logic.

### Parallel track: Synthetic-audience subsystem

The `aud-*` pipeline (intake → avatar-build → validate → review) builds in parallel to the vid-* pipeline above. 4 MVP skills are built; Phase 2 is deferred. The sequence and dependencies live in the dedicated plan at `documents/synthetic-audience-plan.md`. No vid-* skill depends on aud-* and no aud-* skill depends on vid-* (they share only the `Content/pieces/{slug}/` integration surface). Build state of one track does not block the other.

### Step 6: End-to-end test

Use a real creator video and run the current chain: /foundation → vid-voice-capture → vid-capture as needed → vid-research if banks are missing → vid-ideas (optional, when the creator is blank on what to make) → vid-intake → vid-framing → vid-title → vid-thumbnail → vid-structure → vid-intro → vid-segment per body section → vid-ending.

- [ ] Run the manual chain on a real creator video
- [ ] After `vid-pipeline` is built, rerun the same video through `vid-pipeline`
- [ ] Time it. Real clock time, not aspirational. Target: under 60 minutes idea-to-filming-ready.
- [ ] Read script aloud. Would Billy reword anything? If yes, voice profile or skill is broken.
- [ ] Verify all artifacts in `Content/pieces/{slug}/`
- [ ] Verify: when STRUCTURE invoked `vid-intro`, the hook in skeleton MATCHES the hook in final script (no duplicate logic regression)
- [ ] Verify: running with format=News routes through different workflow than format=Deep Dive

### Step 7: Phase 4 feedback skills

- [ ] `vid-measurement`
- [ ] `vid-monthly-review`

### Step 8: Optional (Phase 5)

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
│       ├── vid-foundation/      ✅ SKILL.md, 5 references/, 3 assets/
│       ├── vid-voice-capture/   ✅ SKILL.md, 2 assets/
│       ├── vid-capture/         ✅ SKILL.md, 5 assets/
│       ├── vid-thumbnail/       ✅ SKILL.md, 2 assets/
│       ├── vid-title/           ✅ SKILL.md
│       ├── vid-research/        ✅ SKILL.md, 3 references/, 8 assets/, 3 scripts/
│       ├── vid-intake/          ✅ SKILL.md, 3 references/
│       ├── vid-framing/         ✅ SKILL.md, 3 references/, 1 asset/
│       ├── vid-structure/       ✅ SKILL.md, 2 references/, 1 asset/
│       ├── vid-intro/           ✅ SKILL.md, 3 references/
│       ├── vid-segment/         ✅ SKILL.md, 2 references/, 1 asset/
│       ├── vid-ending/          ✅ SKILL.md, 4 references/, 1 asset/
│       └── creator-setup/       ⚠️ folder exists, no SKILL.md
├── knowledge/                                         ← shared references loaded by skills
│   ├── vault-integration.md     ✅ shared schema contract
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
│   ├── voice-rhythm.md          ✅ writing skills load it
│   └── format-planners/
│       ├── short-process.md     ✅
│       └── {6 others}.md        ✅
├── foundation/                                        ← creator identity (skill-populated)
│   ├── creator-foundation.md    (created by vid-foundation)
│   ├── voice-profile.md         ← thin voice guardrail (created by vid-voice-capture)
│   ├── packaging-system.md      (created by vid-foundation Stage 4)
│   └── reference-pieces/{voice_context}.md  ← the voice engine: real creator passages as `##` sections (populated by vid-voice-capture)
├── banks/                                             ← evergreen, grows over time
│   ├── story-bank/              ✅ README + entries from vid-capture
│   ├── proof-bank/              ✅ README + entries from vid-capture
│   │   └── assets/              ← screenshots, charts, video clips
│   ├── testimonial-bank/        ✅ README + entries from vid-capture
│   ├── metaphor-bank/           ✅ README + entries from vid-capture
│   ├── framework-bank/          ✅ README + manual entries (creator-authored)
│   ├── packaging-bank/          ✅ README + winners (own + outliers)
│   ├── title-bank.md            (seeded by vid-foundation when missing)
│   ├── pattern-bank.md          (created by vid-research when run)
│   ├── hook-bank.md             ✅ hook patterns
│   └── transition-bank.md       ✅ transition patterns
├── Content/
│   ├── pieces/                  ← per-video folders, each with full artifact set; single newsletters/posts also live here
│   ├── ideas/                   ← swipe file for not-yet-built content
│   └── email-sequences/         ← email sequences (multi-piece)
├── People/                                            ← auto-stubbed when clients mentioned
│   └── {Full Name}.md
├── Notes/                                             ← optional drop-zone for on-the-go brain dumps (reconciled later)
├── raw/                                               ← optional, creator's own raw material full text (transcripts, articles)
└── references/                                        ← optional, external study material pointers (no full content)
```

In-scope folders only. Out-of-scope (intentionally not present): `Daily/`, `Projects/`, `Trainings/`, `Companies/`, `Intelligence/`. This vault is content-only.

### Source material (read-only, not in product)

The underlying study material lives at a development reference path on the builder's machine, outside this product workspace. It contains modules on packaging, video strategy/ideation, writing/planning, and shared materials including title/hook/transition banks. Read these files directly when a skill needs source-material backing. Never reference the path, the curriculum, the teacher, or the source by name in productized skill files (attribution-scrub rule).

---

## 8. Banks system (deeper dive)

Each bank serves a different purpose. Don't duplicate content across banks.

| Bank | Source | Read by | Written by | Purpose |
|---|---|---|---|---|
| story-bank | creator's lived/observed stories | vid-segment, vid-intro | vid-capture (Story stage) | Narrative beats |
| proof-bank | creator's own evidence | vid-intro, vid-segment | vid-capture (Proof stage) | Credibility through specifics |
| testimonial-bank | other people's words | vid-intro, vid-segment | vid-capture (Testimonial stage) | Social proof |
| metaphor-bank | creator's analogies | vid-segment, vid-intro | vid-capture (Metaphor stage) | Concrete-ifying abstractions |
| framework-bank | creator's named systems | vid-framing, vid-structure, vid-segment | manual (for now) | Repeatable teaching structures |
| packaging-bank | own winners + studied outliers | vid-thumbnail, vid-thumbnail-gen | vid-measurement post-publish | Style anchors for proven packages |
| title-bank | fill-in-the-blank patterns + winners | vid-title | vid-foundation seeds, vid-measurement adds winners | Reusable title formulas |
| pattern-bank | hook/structure patterns | vid-framing | vid-measurement post-publish | What's worked structurally |
| hook-bank | hook patterns | vid-intro | seed + creator additions | Hook starting points |
| transition-bank | transition phrases | vid-segment, vid-ending | seed + creator additions | Smooth segment-to-segment flow |

**Patterns vs. winners distinction:**
- **Patterns** = reusable formulas (mad-libs). Live in single-file banks like title-bank.md, hook-bank.md.
- **Winners** = specific past wins, instantiated. Live in folder banks (packaging-bank/, story-bank/, etc.), one entry per win.

---

## 9. Verification & testing plan

### After each skill build

- Audit for schema match with `vault-integration.md` (frontmatter, wikilinks)
- Path correctness: every referenced file resolves
- Conversation pattern: short messages, ask-and-wait, no reference-dumping
- Attribution scrub: no source-curriculum names, teacher names, instructor names, course names, or named third-party creators in productized files
- Cross-skill integration: does it write to the same files other skills read?
- **Source-principle traceability**: every new skill, knowledge file, field, bank, example, and handoff maps to source principle, creator data, platform feedback, or AI workflow need.
- **Context budget declared**: required inputs, conditional inputs, forbidden inputs, and output packet are explicit. No whole-document handoff unless the receiving skill truly reads the whole document.
- **Contrastive examples present**: every rule, pattern, or guideline in the skill's references has at least one worked example AND one near-miss / failure mode, each with a one-line "why this lands / why this doesn't." Examples sourced from the underlying study material. Rules without examples = abstract; examples without contrast = unfalsifiable.
- **Foundation anchors present**: every writing skill explicitly loads the specific foundation sections it needs (`creator-foundation.md`, `voice-profile.md`, `packaging-system.md`) and uses them to filter, calibrate, or shape output. A skill that runs identically across two different creators has failed.
- **AI-sounding prose check**: writing skills include positive/negative examples and an explicit check for generic AI phrasing, inflated verbs, abstract transitions, and source-less claims.
- **Agent usefulness check**: if a skill uses multiple agents, each agent has a distinct failure mode and returns a bounded output. If agents duplicate each other, collapse them.
- Honest pass count: what % of the skill works without manual fix?

### After Phase 3 (the big test)

- Run `vid-pipeline` end-to-end on a real creator video
- Time it. Actual clock time, not aspirational.
- Read the script aloud. Does Billy reword anything?
- Check artifacts at `Content/pieces/{slug}/`:
  - piece.md ✓ (main metadata + framing decisions)
  - brain-dump.md ✓
  - script.md ✓
  - thumbnail-brief.md ✓
  - pressure-test.md ✓
- Verify: STRUCTURE-phase hook = SCRIPT-phase hook (orchestrator didn't duplicate logic)
- Verify: News format routes differently than Deep Dive format (format-aware works)

### After Phase 4

- vid-measurement on a published video: does it correctly log a winner to packaging-bank?
- Does the next vid-thumbnail run pull that winner as a style anchor?
- Does vid-monthly-review surface patterns across multiple videos?

---

## 10. Open questions / known gaps

### Architectural

1. **No standalone packaging refresh skill for now.** It does not exist as a built skill. `vid-foundation` sets first packaging defaults, `vid-research` supplies pattern evidence, `vid-framing` chooses a format per video, and future `vid-monthly-review` can update packaging-system.md if real data says to change defaults.
2. **Title vs. thumbnail role asymmetry.** The underlying material doesn't explicitly say which carries more click weight. Worth documenting once packaging-bank has data.

### Knowledge gaps (from deeper source-material mining)

These are real gaps in our knowledge files that surfaced during deeper source mining. Address when building related skills:

- **Outlier extraction methodology pressure-test.** `vid-research` now has the systematic extraction job. It still needs real-channel testing against messy data to prove the protocol holds.
- **A/B testing protocol for thumbnails**: sample size, threshold-to-judge, refresh/pivot timing. Belongs in vid-measurement.
- **Niche-specific gift-framework lookup**: concrete wrapping/box/gift examples per niche (crypto / wellness / business / fitness). Currently abstract. Add as we see real creator data.
- **Series thumbnail templating.** When videos are part of a series, thumbnails share visual elements. Implied in the source teaching, never systematized.

### Product / distribution

- **Vale linter integration.** Autocorrect-style voice enforcement on draft saves. The voice-profile refusals compile to Vale rules. Separate from `vid-voice-update` (Phase 4), which appends refusals from mid-draft creator corrections; Vale would then enforce those compiled rules on save. Future enhancement, not blocking Phase 3.
- **Test harness**: currently ad-hoc (spawn agents, read output). At some point want a proper eval suite for each skill.
- **Distribution mechanism**: answered. See Section 13: package as a Claude Code plugin. Migration deferred until Phase 3 skills land.

---

## 11. Patterns and principles (the meta-layer)

These hold across every skill in the system. Violating any of them = something to re-think.

1. **Conversation, not document.** Skills run as dialogues. Short messages. Ask-and-wait. References are for Claude to think with, not paste at the creator.
2. **Creator drives, Claude structures.** Skills extract and organize. They never generate identity, voice, stories, numbers, or claims. The creator's brain dump is the raw material; Claude does not invent.
3. **No fabrication.** Numbers, client names, results, quotes all must trace to source (script, foundation docs, banks). Visual elements (objects in a thumbnail, scene descriptions in a brief) must derive from what the creator actually has or said.
4. **Specificity wins.** Vague answers get pushed back on. "Busy professionals" → push for "solo founders, $200k-$2M, working from home." Generic verbs → specific verbs. Round numbers → real numbers.
5. **Read aloud is the voice test.** If the creator would reword it when speaking, the draft is wrong. Applies everywhere: scripts, thumbnails, emails, social posts.
6. **The graph is the product.** Every artifact wikilinks. Every story knows which videos used it. The Obsidian backlink pane and graph view should always show meaningful connections.
7. **Update both sides.** When a script uses a story, BOTH `script.md` and the story's `used_in:` get updated. Non-negotiable.
8. **Banks grow.** Patterns and winners both. Static banks are dead banks. Every published video should add to the bank ecosystem.
9. **MVP principle.** First version of every doc / skill / bank entry needs refinement after real data comes in. Don't grind for perfection upfront. Lock the best version the creator can articulate today.
10. **Match scope to skill.** A planner plans. A capturer captures. A writer writes. Skills that drift across roles (e.g. a planner that also designs) should be split.

11. **This is an implementation engine, not a teaching system.** Skills do not exist to teach the creator how YouTube works. That's what the underlying study material is for, and they can read it elsewhere. Skills exist to PRODUCE creative, unique, voice-authentic content the creator could not produce alone in the same time. Reference docs use examples to calibrate Claude's judgment at run-time, not to educate the creator. If a reference doc reads like a course lesson, it's wrong. It should read like a contrastive cheat-sheet a writer pulls open mid-draft.

12. **The whole system exists to mimic the creator authentically and dynamically.** Foundation docs (positioning, voice profile, packaging system) exist so EVERY downstream skill produces output that sounds like the specific creator using it, not generic AI output, not the source material's voice, not anybody else's voice. The same `vid-intro` skill should produce a different intro for a fitness coach than for a B2B SaaS founder, because their foundation docs differ. If two creators run the same skill on the same brain dump and get content that sounds the same, the system has failed at its core job. Examples in references calibrate Claude TOWARD that creator's voice; foundation docs anchor it; the brain dump supplies the actual phrases.

---

## 12. Recent work log (last refreshed 2026-06-18)

- 2026-04-18: vid-foundation built and audited
- 2026-04-20: vid-capture built, four-stage capture
- 2026-04-20: authentic-ai-os standalone workspace established (split from business-os)
- 2026-04-20: All bank READMEs written (story / proof / testimonial / metaphor / framework)
- 2026-04-21: packaging-bank added (consolidated title+thumbnail winners)
- 2026-04-21: vid-thumbnail v1 built (planner)
- 2026-04-22: knowledge/thumbnail-text-patterns.md added (5 winning patterns, anti-patterns, examples)
- 2026-04-23: packaging-bank scope: own winners + studied outliers (one bank, source field)
- 2026-04-28: vid-voice-capture built in another session, audited and migrated
- 2026-04-30: schema sweep, last_refreshed and contexts_populated fields added to foundation doc schema
- 2026-04-30: vid-thumbnail upgraded with anti-fabrication, distinctiveness, tonal-pairing, click-pull-with-delivery rules; AI prompt template + composition guide created
- 2026-05-01: vid-thumbnail SCOPE STRIPPED. Text planner only, no design. Composition guide reserved for future vid-thumbnail-gen.
- 2026-05-01: thumbnail-text-patterns.md gained real-world examples library (mined combos with channel context)
- 2026-05-01: build-plan.md consolidated, single source of truth at authentic-ai-os root
- 2026-05-01: Section 13 added, plugin packaging strategy locked (one plugin / boundary table / 4 update-safety rules / migration plan)
- 2026-05-01: vid-title built (smallest Phase 3 writing skill, no deps). 3-phase Q-script: load context → 5-10 candidates with BENS+char-count annotations → creator picks → save to meta.md. Anti-fabrication enforced. Standalone OR sub-skill mode.
- 2026-05-01: vid-title tested 3x. After 1st run produced AI-mash-ups, added READ-ALOUD test as primary filter + 4 new anti-patterns (mid-title periods, invented compound nouns, number-stuffing, parenthetical clutter) + Natural Language Patterns section. 4th test landed natural-sounding titles ("How I Added 40 Pounds To My Squat In 11 Weeks" / "Why I Dropped My Squat 20% To Hit 405"). Also added shape-variety rule (at least 2 candidates use a shape NOT in past winners) and split filters into HARD (auto-reject: fabrication, >50 chars, invented nouns, read-aloud failure) vs SOFT FRICTION (flag and explain, creator decides).
- 2026-05-02: knowledge/intro-architecture.md written (universal 6-part: Top 3 Q's → Hook → Problem/Result → Setup → Transition → Credibility woven in + Visual Proof). 5 hook types, 3 P/R options, banned transition phrases, length targets, format-adaptation map.
- 2026-05-02: 3 format planners written (case-study, news + short-process updated). Each has explicit "Intro adaptation" section.
- 2026-05-02: After feedback, softened all "REJECT" language in format planners + intro-architecture + vid-title. Defaults presented WITH explanations of why they tend to work. Hard rules stay (anti-fabrication, ≤50 chars, invented compound nouns, read-aloud). Soft friction = flag and explain, creator decides. Principle: locking everything as REJECT stifles creativity. Defaults are pattern-matches, not laws.
- 2026-05-04: 4 remaining format planners written (deep-dive, interview, roast, listicle). All 7 format planners now complete in `knowledge/format-planners/`. Each has Intro adaptation table that vid-intro will load when assembling intros.
- 2026-05-05: Workspace renamed `peak-content-ic-tools` → `authentic-ai-os`. Build-plan paths and proposed plugin name updated. Skill files use relative paths so the rename was non-breaking.
- 2026-05-08: **Phase 1 Knowledge & Schema Coordinator delivered shared infrastructure.** Locked content-only scope across the build plan (removed any business-OS framing, removed Phase 6 biz-* scope, simplified vault-integration optional folders to raw/ + references/ + Notes/, dropped Daily/, Projects/, Trainings/, Companies/, Intelligence/ from in-scope). Added `foundation/reference-pieces/` to the foundation layer (full polished pieces for piece-level voice rhythm, populated by vid-voice-capture, loaded by every writing skill). Renamed `Content/sequences/` to `Content/email-sequences/` everywhere. Created `knowledge/voice-rhythm.md` (sentence rhythm, paragraph structure, opener pattern, punctuation signature, energy modulation, examples-first contrastive, ~150-200 lines). Created `banks/hook-bank.md` (5 hook types × 5-8 fill-in-the-blank patterns × worked examples + near-misses, ~40-50 patterns total). Created `banks/transition-bank.md` (intro-forward, segment-pivot, body-to-ending transitions; banned phrases section explicit). Added 3 optional fields to `voice-profile-schema.md`: `preferred_hook_types`, `transition_style_preferences`, `intro_pacing`. Added `reference-piece` frontmatter schema to vault-integration.md. Created `templates/skill-working-notes-template.md` for in-development source citation tracking. Phase 2 writing-skill builders (vid-intro, vid-segment, vid-ending) can now spawn against stable infrastructure.
- 2026-05-05: vid-foundation gained context absorption + incremental save. Two real gaps from live testing fixed. **(1) Context absorption.** Before each phase's question, the skill now scans prior turns. If the creator already gave 70%+ of the answer (which happens a lot in Phase 1 when they describe the offer), surface it back as "here's what I heard, confirm or sharpen" instead of asking blind. Saves the creator from repeating themselves. Applies especially to Phases 2, 3, 4, 5 of Stage 1. **(2) Incremental save at every phase lock.** Each phase locks, the section gets written to creator-foundation.md immediately via Edit. Lock confirmation uses AskUserQuestion (Yes, lock or Refine UI). If chat closes mid-stage, the work is on disk and the next session resumes from where it stopped. RESUME protocol added to FIRST ACTION: skill reads creator-foundation.md at start, detects partial completion, surfaces "picking up where you left off" and skips to first unfilled phase. No pause command needed. Creator just leaves and starts a new session. The new session reads the file and picks up.
- 2026-05-05: Vale linter integrated, two-tier architecture locked. **Dev-side** (this workspace): ProductVoice rules in `.vale/styles/ProductVoice/` lock the skill chain (em-dashes, en-dashes, AI-isms, banned words, attribution leaks). PostToolUse hook at `.claude/hooks/vale-fire.js` fires on every Edit/Write to flag violations and auto-apply safe swaps. Path exclusions skip build-plan, foundation/, Content/pieces/, Notes/, raw/, Daily/, Intelligence/, Onboarding/. **Creator-side** (ships with the plugin to other creators): opinionated rules do NOT ship. Creators get a blank `.vale/styles/CreatorVoice/` template that vid-voice-capture compiles from voice-profile.md, plus an OPTIONAL `AISanitizer/` pack (em-dashes, AI-isms, generic banned words) that creators can flip on if they want it. Default off. Their voice, their rules. Future work: build vid-voice-rule-capture skill (mirrors business-os pattern) for dynamic creator-side rule capture during draft review. Build creator-side scaffolding template that ships with the plugin.
- 2026-05-05: Em-dash purge across all production files. Live test of vid-foundation revealed the skill defaulted to em-dashes everywhere because the example bank itself was full of them. Mechanical scrub caught all 1,103 em-dashes and en-dashes across 46 files. Numeric ranges broken by the scrub (8-12 became 8.12, 1-10 became 1.10) restored to hyphens. Five sub-agents in parallel rewrote the 41 mechanically-scrubbed files for prose flow: stilted "X. Y" breaks converted to commas where thoughts continued, parentheses where asides belonged, colons in headers, periods only where clean breaks made sense. Substance preserved across all files. Lesson: never do mass mechanical text replacements on prose. Always rewrite, don't substitute. Vale layer above prevents this from recurring.
- 2026-05-05: vid-foundation strategic overhaul after live test surfaced gaps the scripted eval missed. Real-conversation failures: skill defaulted to em-dashes, contrast-template sharpening, switched perspective without permission, ignored creator's exact words, didn't pull from locked example bank. Five strategic fixes shipped:
  1. **Hard voice rules at skill start.** No em-dashes ever, declarative no hedging, no contrast/comparison templates, use creator's exact words. Loaded in SKILL.md before Stage 1 fires. Voice-profile.md overrides if it exists.
  2. **Examples-first protocol.** Reading locked examples in positioning-framework.md and avatar-guide.md is now REQUIRED before drafting any sub-artifact, not "if stuck." Skill writes IN the shape of proven examples, not from cold templates.
  3. **Example libraries massively expanded.** Mining agent pulled additional locked examples from the underlying study material. positioning-framework.md grew from 185 → 278 lines (8 good/bad pairs, 10 locked statements, 10 anti-pattern examples). avatar-guide.md grew from 169 → 374 lines (8 avatar pairs, ~25 viewer-voice phrasing pairs across 6 niches, 12 common mistakes). All source attribution stripped per locked decision #15.
  4. **Differentiator dropped as a saved field.** The probe still fires in Phase 4 (sharpens the Iceberg Statement so the differentiator gets baked in), but the answer doesn't get its own row in creator-foundation.md. Matches the underlying study material's actual model. Differentiator informs the statement, not captured separately. Updated iceberg-discovery-method.md, SKILL.md Stage 1, creator-foundation-template.md.
  5. **Lock-and-move discipline.** After 2 sharpening rounds on a sub-artifact, lock the best version and move forward. Iceberg Statement is the goal of Stage 1, not perfectly polished sub-bullets. Added to conversation rules.
  Also: dropped "Known-for word" optional field. Renamed Iceberg Top → Iceberg Statement (creator-facing terminology). Cleared meta-commentary bleed from iceberg-discovery-method.md. Eval workspace at vid-foundation-workspace/ remains for iteration tracking.
- 2026-05-05: TodoWrite-at-start pattern added to vid-foundation and vid-voice-capture. First action after loading vault-integration.md is to create a task list mirroring the skill's stages, marked in_progress / completed as work moves. Forces sequence discipline and gives the creator visibility into what's coming. Pattern applies to multi-stage sequential skills only. vid-capture (loop), vid-title (single-shot), vid-thumbnail (single-shot) skip it.
- 2026-05-05: Architecture decision, credibility brags + backstory STAY in vid-foundation. Earlier proposal to move them into vid-capture rejected because the user-facing promise of vid-foundation is "run once → complete foundation." Fragmenting the foundation across two skills breaks that. Brags + backstory remain identity-level data in `creator-foundation.md`, loaded by every downstream writing skill. New wins captured later via vid-capture flow into proof-bank/story-bank as separate entries; foundation brags refresh only when the creator re-runs vid-foundation.
- 2026-05-05: vid-foundation Stage 1 fundamentally restructured. Old Stage 1 (Positioning, 4 questions) + Stage 2 (Avatar, 5 questions) merged into a single **Stage 1: Iceberg Discovery**. Adopts the "iceberg" metaphor (top + bottom) as the creator-facing model. New skill-local reference `iceberg-discovery-method.md` holds the full conversation backbone (6 phases: Opening → Audience Narrowing → Problem Discovery → Iceberg Top → Iceberg Bottom → Final Validation) with one-question-at-a-time rules, problem-vs-solution disappearance probe, urgency 1–10 check, and good/bad-pair pull rules. Stage body in SKILL.md is now tight, loads three references (method + positioning + avatar), drives the conversation per the method file. Output expanded: creator-foundation.md now captures Iceberg Top + Iceberg Bottom (8–12 angles) + Person + Top 3 + Axis owned. Renumbered subsequent stages: Credibility 2, Backstory 3, Packaging 4, Voice handoff 5. Total stages dropped from 6 to 5. creator-foundation-template.md updated to match.
- 2026-05-07: **Skill renamed `vid-hook` → `vid-intro`.** The skill produces the FULL 6-part intro (Top 3 questions → Hook → Problem/Result → Setup → Transition → Credibility woven), not just the 5-second hook line. Old name described one ingredient; new name describes the deliverable. Mechanical rename across 15 files (build-plan, intro-architecture, vault-integration, voice-profile-schema, voice-pressure-test, all bank READMEs, all capture guides, vid-capture/vid-title SKILL.md). Frees the word "hook" to mean only the 5-second opener (step 2 of the 6-part architecture) everywhere downstream. `banks/hook-bank.md` (step 2 patterns) and `banks/transition-bank.md` (step 5 patterns) both feed `vid-intro`.
- 2026-05-07: **Locked decisions #11 and #12 added.** #11: this is an implementation engine, not a teaching system, skills produce content, references are run-time calibration not creator education. #12: the whole system exists to mimic the creator authentically and dynamically, same skill, same brain dump, two different creators must produce different content. Foundation docs anchor it. #9 amplified: examples are contrastive (worked + near-miss with why-this/why-not), sourced from underlying material, never attributed. Principle: examples are the teaching surface, not rules.
- 2026-05-07: Build-plan audit layer added for source-principle traceability and AI-first workflow design. New standards: every skill/field/bank/handoff maps to source principle, creator data, platform feedback, or AI workflow need; skills declare context budgets; examples should expand creativity; "iceberg" approved as creator-facing translation of the umbrella/top-bottom positioning principle; `vid-pressure-test` gets bounded multi-agent reviewers for source alignment, creator voice, AI-slop, retention, and proof/claim traceability.
- 2026-05-04: Foundation audit + reconciliation pass before building vid-framing/vid-intro. Critical schema drift fixed:
  1. **vid-foundation voice handoff → vid-voice-capture.** vid-foundation no longer writes a partial voice-profile.md; it finishes creator foundation and packaging, then tells the creator to run vid-voice-capture next. Removed `vid-foundation/assets/voice-profile-template.md` and `vid-foundation/references/voice-capture-methods.md` (now redundant). The two-layer voice profile lives only in vid-voice-capture, where it belongs.
  2. **Proof-bank reconciled to 2 types end-to-end.** `proof_type` is now strictly `personal-result | client-win` (about who the result belongs to). Presentation format (static-screenshot / before-after-pairing / live-clip / inline-stat) moved to body section in `proof-entry-template.md`. Updated: `knowledge/proof-capture-guide.md`, `vault-integration.md` proof-type slugs, `proof-entry-template.md` filling instructions, `banks/proof-bank/README.md` tag schema.
  3. **Source attributions scrubbed ruthlessly.** Source names, source-course references, instructor references, and named public-figure examples removed from productized files. Calibration examples were replaced with niche/category descriptors. Files affected: format-planners (news, interview, listicle, roast), thumbnail-text-patterns, thumbnail-examples-library, thumbnail-composition-guide, story-capture-guide, framework-bank/README, build-plan.md. Locked decision #15 updated to clarify named-creator policy.
  4. **Hook taxonomy reconciled to the locked 5.** Listicle and roast planners no longer reference off-list "Confession Hook" or "Visual Demo Hook." Confession framing is now a delivery style on top of Statement Hook. Visual Demo is an emotion brick (not a hook), paired with Statement Hook. The 5 locked types in intro-architecture.md are the single source of truth.
  Foundation now matches the schemas downstream skills will load. vid-framing and vid-intro can be built against a stable contract.
- 2026-05-11: **vid-framing built** (skill 11 of 14). Decision: surfaces 3 outlier-anchored candidates plus 1 experimental angle (Rule of 3+1 extended from format rotation to angle generation). `viewer_stage` field locked as cold/warm/hot per the Audience Temperature Model. Format pulled from creator's packaging-system rotation, not all 7. Goal locked at sales/email/views. Anti-fabrication: every anchored angle cites a real pattern-bank entry. Files: SKILL.md (229 lines), 3 references (167/148/259), 1 asset, 1 WORKING-NOTES. Right-size pass kept all files under target.
- 2026-05-11: **`reference-block.md` collapsed into `piece.md`.** Old plan had vid-framing writing a separate `reference-block.md`. Reality: all existing writing skills (vid-title, vid-intro, vid-segment, vid-ending, vid-thumbnail, vid-capture) already read `meta.md` as the main metadata file; `reference-block.md` was envisioned but never actually used by any built skill. Consolidated: framing decisions now append to `piece.md` (renamed from `meta.md` to better signal the file's role as the per-piece identity card). piece.md becomes the main lifecycle ledger. vid-intake writes intake fields, vid-framing appends framing decisions, vid-thumbnail/vid-title append their picks, vid-segment writes stories_used/proofs_used/metaphors_used, vid-ending writes the ending packet, vid-pressure-test writes audit status. No skill overwrites another's fields. Schema-coherence matrix mapped in `C:/Users/billr/.claude/plans/remaining-skills-contracts.md`.
- 2026-05-11: **Audience Temperature Model added as shared knowledge.** `knowledge/audience-temperature-model.md` (144 lines) defines cold/warm/hot, what determines temperature (topic, problem framing, stories, frameworks), the conversion math (broad: 250k cold → 10 sales; specific: 50k hot → 40 sales), and goal × temperature matching. Loaded by vid-framing, vid-ending (CTA placement), and future vid-measurement.
- 2026-05-11: **Contract-level plan for remaining 3 skills locked.** vid-structure invokes vid-title and vid-intro inline as sub-skills, writes script.md skeleton with intro complete and segments stubbed. vid-pressure-test runs 5 parallel adversarial reviewers (source-alignment, voice-authenticity, AI-slop, retention-logic, proof/claim traceability) each capped at top-3 issues. vid-pipeline is the adaptive orchestrator (~150 lines target) routing based on piece state. Pipeline order confirmed: framing → thumbnail → structure (invokes title + intro) → per-segment → ending → pressure-test. Plan at `C:/Users/billr/.claude/plans/remaining-skills-contracts.md`.
- 2026-05-11: **Brick-closure trim (vid-capture v2 minimum-viable).** Mapped all 6 brick tools (Story/Metaphor/Framework/Proof/Testimonial/Visual Demo + Checklist). Two gaps: framework had a bank but no capture flow; Visual Demo had nothing. First plan over-engineered (6 new files + new visual-demo-bank + dual-mode Stage V + entry templates). Three audit agents (workflow simulator, over-engineering hawk, source fidelity critic) pressure-tested and converged: drop Stage V entirely, drop visual-demo-bank, drop entry-template files, move Framework's 5-step build into knowledge file (not vid-capture stage). Final implementation: 2 new files + 3 edits. **Built:** `knowledge/framework-builder.md` (5 shapes, selection matrix, 5-step build, naming rules, entry schema inline), `knowledge/visual-demo-builder.md` (3 sub-types, planning filters, 3-step brainstorm, anti-patterns, transitions, no-bank rationale). **Edited:** vid-capture SKILL.md (added Stage F Log-only path; total now 243 lines), vid-segment SKILL.md (added knowledge file silent loads, async-brick-notes flow, no-Visual-Demo-bank handling), banks/framework-bank/README.md (capture flow + craft-lives-in-knowledge-file note). Verification: 0 em-dashes, 0 attribution leaks across all 5 changed files. Stage F handles Log save (standalone or after inline crafting); Framework Create lives in knowledge file loaded by vid-segment; Visual Demo craft is purely inline (no save target). Async-brick-notes.md captures cross-segment ideas without flow-breaks.
- 2026-05-11: **Post-audit source-fidelity patches.** Respawned the 3 audit agents (workflow simulator, over-engineering hawk, source fidelity) against the built implementation. Workflow + Over-engineering passed clean (SHIP AS-IS verdicts, no friction or YAGNI violations). Source Fidelity passed architecture but flagged 3 pedagogical gaps from source teaching: sticky-notes visual (lesson-10:39, the "dump 12, keep 3" aid), "three is an example, not a rule" tactic (lesson-10:57), and Checklists as a co-equal logic-brick tool alongside Frameworks and Proof (lesson-10:21). All 3 patched: framework-builder.md gained the sticky-notes visual in Step 1 and "three is an example" callout in Naming rules (now 294 lines); a "Frameworks in the logic-brick context" section added to cross-reference proof-placement-rules.md and the new step-markers section. `knowledge/visual-proof-callouts.md` extended with an "On-screen step markers (checklists as the third logic-brick tool)" section covering when to flag step markers, callout syntax, what NOT to need step markers (cycles/venns/listicles), and piece.md tracking. Final state: 0 em-dashes, 0 attribution leaks, all line counts under target. Audit-build-audit loop validated the trim held.
- 2026-05-13: **vid-structure built** (skill 12 of 14). Decision: vid-structure is the Tier 1 outline builder. Mines brain-dump against framing, surfaces brick candidates per segment (frameworks/stories/proofs/metaphors from brain-dump + banks), plans cross-segment tension (title-promise location + 1-2 active threads + handoffs), writes script.md skeleton with material-anchored segment purposes. Tier 2 word-for-word prose handed off to vid-segment. **Cut from prior contract** (per 3 audit agents converging): inline vid-title/vid-intro invocations (orchestrator concern, not vid-structure's), piece.md `segment_count` field (redundant with script.md headers + segment_purposes), hard-stop on missing thumbnail-brief (no longer relevant after sub-skill cut), Phase 1 Keep/Cut/Combine as a separate review phase (merged into mining). 4 phases collapsed to 2: Mine + propose outline → Write script.md skeleton. **Format-native shapes:** Case Study runs as narrative arc (Setup/Problem/Action/Outcome/Lesson, not N abstract segments), Listicle/Short-Process/Deep-Dive/Roast/Interview/News as N segments with format-prescribed counts. Skill loads `knowledge/format-planners/{format}.md` at runtime; never hard-codes a count. **piece.md additions:** `segment_purposes` (material-anchored), `tension_plan` (central_question + title_promise_segment + active_threads), `structure_locked_at`, `piece_status: structured`. **New shared knowledge:** `knowledge/script-tension-architecture.md` (224 lines, target <250) defines cross-segment tension flow + title-promise-late discipline + threading + handoff rules; loaded by vid-structure (planning), vid-segment (per-segment tension role), vid-pressure-test (retention audit). Distinct from vid-segment's local `references/setup-tension-payoff-shapes.md` which owns per-segment STP. Files: SKILL.md (327 lines, target <500), references/brain-dump-mining.md (148 lines) + references/structure-conversation-examples.md (237 lines), assets/script-skeleton-template.md (199 lines), WORKING-NOTES.md (99 lines, dev-only). Plus the shared knowledge file. Verification: 0 em-dashes, 0 attribution leaks in productized files. Pre-build audit-1 validated the trim from 4 phases to 2; Billy caught at consolidation that vid-structure is more substantive than the trim implied (it mines AND maps to segments, not just headers), restoring material-anchored segment purposes + brick surfacing per segment as load-bearing work.
- 2026-05-14: **vid-pressure-test built** (skill 13 of 14). Full audit-build-audit loop. Catch-and-fix audit before filming, NOT a report tool. 4 parallel reviewers (source-traceability, voice-authenticity, AI-slop, retention-logic), each hard-cap top 3 issues. Multi-agent always (no mode prompt; toggle CUT per Billy's call "each reviewer has its own job"). Rubric conditioning by piece.md goal/format/viewer_stage (Billy locked YES despite both audits pushing back on 5% lift for complexity). Phase 5 creator read-aloud REPLACES re-audit ceremony (source-taught: "if you would reword it, the script failed"). Skip RESTRICTED on hard-rule violations (fabricated claims / em-dashes / banned phrases): must Approve, Deny+rewrite, or Mark-as-gap (logs to piece.md `claims_to_source_before_filming` and blocks ready-to-film verdict until resolved). Light-vet inline check on creator's own rewrites for banned phrases / words_avoided / em-dashes / hedges before applying to script.md. Soft issues NEVER walked interactively (would kill creator energy before filming): logged to piece.md frontmatter + chat summary. pressure-test.md file DROPPED entirely (Hawk + Source Fidelity convergent: script is the deliverable, piece.md frontmatter is the receipt). Files: SKILL.md (279 lines), references/reviewer-source-traceability.md (129), references/reviewer-voice-authenticity.md (137), references/reviewer-ai-slop.md (135), references/reviewer-retention-logic.md (181), references/rubric-conditioning.md (51), references/interactive-fix-loop.md (282), assets/pressure-test-frontmatter.md (199), WORKING-NOTES.md (102, dev-only). Total: 1495 lines productized. Verification: 0 em-dashes, 0 attribution leaks across all productized files.
- 2026-05-14: **vid-pressure-test post-build audit-2 patches.** Respawned 3 audit agents. **Workflow Simulator: 4 SHIP / 1 PATCH** (read-aloud loop missing soft cap after 2 re-read cycles). **Over-engineering Hawk: 4 CUTS + 3 TRIMS** flagged (~190 lines proposed savings). **Source Fidelity: 1 CLEAN / 3 PATCH / 1 OVER** (retention-logic missing 3 anti-patterns from script-tension-architecture: promise drift, stacked lessons, cliffhanger-as-content; WORKING-NOTES had false-positive "Future vid-presenter skill" infrastructure proposal). Applied: read-aloud soft-cap nudge after 2 re-reads (Workflow Sim); output packet CUT (Hawk; piece.md frontmatter is sufficient handoff); 4 repeated "Anti-fabrication for the reviewer" sections CUT (Hawk; SKILL.md Phase 2 covers once); retention-logic patched with 3 missing anti-patterns (Source Fidelity); rubric-conditioning.md trimmed 122→51 lines (Hawk); Phase 1 format-planners load deferred to retention reviewer (Hawk); "Future vid-presenter skill" proposal removed from WORKING-NOTES (Source Fidelity). Pushed back: Hawk's 5→3 gates in retention-logic (Source Fidelity flagged MORE anti-patterns needed; kept 5 gates and added the missing checks); Hawk's "1 example per reviewer" (Workflow Sim validated examples as teaching surface; kept 2-3 each); Hawk's full interactive-fix-loop collapse (kept Example 5 and 6 separately: one demonstrates accept-anyway, other demonstrates revise). Final state: 1495 lines productized, all files under target, 0 em-dashes, 0 attribution leaks. Audit-build-audit loop closed.
- 2026-05-19: **Pattern banks consolidated 7 to 4.** Source-fidelity agent confirmed the source teaches ONE holistic pattern bank (study the whole outlier, repeat the whole package), not seven decomposed silos. Billy pressure-tested each. **Kept (4):** `pattern-bank.md` (synthesis + per-outlier full packages + topic clusters folded in), `power-words-bank.md`, `title-patterns-bank.md`, `thumbnail-patterns-bank.md`. These three sub-banks are source-taught AND legitimately decomposable (downstream skills consume specific slices: vid-title reads power-words+title, vid-thumbnail reads thumbnail). **Cut (3):** `topic-patterns-bank.md` (merged into pattern-bank synthesis; source never treats topics standalone, only attached to the outlier that worked), `viewer-hates-bank.md` (NOT source-taught as pre-research; source teaches post-publish flop diagnosis, which belongs to future vid-measurement, not research), `format-patterns-bank.md` (cannot classify a competitor's format from title+thumbnail+metadata; needs transcripts of every outlier, infeasible at ~47/session, so it was fiction-by-inference. Format is a menu pick, not a mined pattern). **Format rotation mechanism unchanged:** the Rule of 3+1 + the fixed 7-format menu + the 4-check filter already live in `knowledge/format-rotation-guide.md` (source-taught, no competitor data needed). vid-research Phase 7 now has the creator pick their 3 core + 1 experiment from that menu using the filter, writes the locked rotation into packaging-system.md. The experiment-promote/retire step is post-publish, deferred to vid-measurement (manual until then). Downstream: vid-framing's silent-load drops from 6 sub-banks to 3; its viewer-hates soft-friction removed (flop knowledge is post-publish, not pre-research). Net: less to maintain, the source's holistic per-outlier view emphasized, no fiction-by-inference banks.
- 2026-05-19: **vid-packaging collapsed (skill deleted).** Decision after 3-agent investigation (source fidelity, dataflow mapper, workflow simulator) plus Billy's own walkthrough. Finding: vid-packaging had no irreducible purpose. Its evidence fields (format rotation, thumbnail strategy, thumbnail style, title-bank seed, 5 of 9 fields) are exactly what `vid-research` produces from real outliers; asking the creator to commit them from memory in a foundation interview produced throwaway data the skill itself flagged as "overwritten once vid-research runs." Its per-video function belongs to `vid-title`/`vid-thumbnail`; the "do title+thumbnail together" beat belongs to `vid-pipeline`. The thin identity residue (design guardrails, creation path) is ~10 lines and does not justify a skill. Real-world trigger: Billy hit the wall live on a fresh positioning pivot with zero transferable data, the source's exact "run research first" case. **Change:** `vid-packaging` skill deleted. `foundation/packaging-system.md` (still read by vid-framing, vid-title, vid-thumbnail, vid-structure, vid-pressure-test) is now authored by `vid-research` from the evidence it already gathers. Packaging defaults become a research output, not a pre-research guess. Foundation identity sequence shortens to 5 interviews (avatar → positioning → pillars → credibility → backstory); after backstory the orchestrator points at vid-voice-capture then vid-research, and vid-research authors packaging-system.md. **Parked (open question, not homed yet):** where the identity residue (design guardrails, creation path) gets captured. Deliberately not forced into a half-baked home; revisit after first real vid-research run confirms the packaging-system.md authorship shape. Source-aligned: source teaches packaging defaults come FROM evidence (own-channel data or research outliers), not creator memory; the collapse removes the fiction-by-default path the source warns against.
- 2026-05-19: **vid-voice-capture redesigned: exemplar-led + split (the voice model inverted).** External research (convergent, one-directional: literary-imitation stylometry, Anthropic multishot guidance, the everyday-authors paper, context-rot / lost-in-the-middle evidence) plus Billy's own stored feedback (`feedback_reference_pieces_not_voice_profiles`) found the old design backwards: it stored distilled rules + statistics framed "preservation checklist, NOT a generation seed," and loaded one monolith with 9 context maps every generation. Evidence: voice reproduces from verbatim real passages; rules are a thin constraint layer; statistics are validation instruments, not generation input; unused context maps are a measured quality tax. **New model:** `foundation/reference-pieces/{voice_context}/` is the voice engine (3 to 5 tight real passages per medium, the generation seed, lazy-loaded by the writing skill matching the piece's `voice_context`); `foundation/voice-profile.md` demotes to a thin guardrail (fingerprint, signature phrases, refusals, POV/energy, no statistics). Rhythm is judged by ear against the reference pieces at validation time, never stored as numbers. `voice_context` is a piece.md field (default `youtube-script`, always written by vid-framing, orthogonal to `format`: medium vs structure). The faith-close (and any improvised creator moment) is stored ONLY as a hard refusal, never a reference piece (exemplar-as-seed would otherwise regenerate the exact thing the creator forbade). "Voice locked" terminology banned per Billy. **Built via audit-build-audit:** 3 pre-build agents (Workflow Sim, Over-engineering Hawk, Source Fidelity) flagged the format↔context naming mismatch (resolved with the orthogonal piece.md `voice_context` field, not a lookup table), faith-close-as-refusal, and templates-must-stay-empty-placeholders; trim confirmed with Billy. **Files:** rewrote `voice-profile-schema.md` (now the canonical two-artifact + unified load contract), `voice-pressure-test.md` (by-ear Pass 2 vs reference pieces, absorbed the rhythm lens), `voice-rhythm.md` (numbers → by-ear lens, filename kept), `voice-extraction-methods.md` (passage selection, not rule extraction), `vid-voice-capture/SKILL.md` + `voice-profile-template.md` (thin guardrail, empty placeholders) + new `reference-piece-template.md` + rewritten `extraction-worksheet-template.md`. **Rewired consumers to the unified contract:** vid-segment, vid-intro, vid-ending, vid-structure, vid-pressure-test (SKILL + reviewer-voice-authenticity + interactive-fix-loop + reviewer-ai-slop), vid-framing (sets voice_context), vid-ending/ending-anti-patterns, `vault-integration.md` (piece.md + reference-pieces schema), `CLAUDE.md` (asset routing rows). **Post-build audit:** 3 agents. Source Fidelity caught 2 em-dashes in voice-profile-schema (brand violation, fixed; REDESIGN-SPEC dev file deleted since its audit purpose was discharged). Workflow caught the pressure-test logging field mismatch (`layer1_pass/layer2` → `pass1_guardrail/voice_context/pass2_grain`, fixed in vid-segment + vid-intro) and the missing-voice_context default (mooted by vid-framing always-writing the field). Workflow's "BLOCKER: built voice-profile.md contradicts schema" findings were misreads of Billy's old gitignored test workspace file (the skill regenerates it on next run; not a deliverable). Over-engineering Hawk's deeper DRY cuts declined on judgment: these knowledge files load independently into different skills, so brief principled restatement is standalone-load context, and the worksheet checklist is a real pre-save safety gate for the leaks Source Fidelity flagged. 0 em-dashes, 0 attribution leaks across productized files. Audit-build-audit loop closed.
- 2026-05-13: **vid-structure post-build audit-2 patches.** Respawned the 3 audit agents. **Workflow Simulator: SHIP AS-IS** (build matched contract, format-native shapes held across Case Study + Short Process + re-structure scenarios). **Over-engineering Hawk: TRIM ~122 lines** flagged. **Source Fidelity: PATCH** flagged 3 false-quantification leaks (60-80% title-promise range, 1-2 thread cap as a hard rule, working-memory overload framing, format-specific percentages, all extrapolations not source teaching). All Source Fidelity patches applied: replaced hardened percentages with "push it LATE in the body, past midpoint" and "the exact spot depends on format"; replaced "Cap at 1-2 active threads" with "most scripts stay clearest with 1-2 prominent loops, more is doable but harder to honor"; replaced "working memory floods" overload framing with "the more open at once, the harder to honor every payoff." High-confidence Hawk cuts applied: redundant soft-friction reference table dropped from SKILL.md (~9 lines), brain-dump-mining principles section dropped (~6 lines, redundant with anti-patterns), News removed from segmented-formats list in template (~3 lines, News is its own shape not segmented). Pushed back on 3 Hawk trims with reasoning: Phase 1 sub-numbering kept (Workflow Sim validated as AI's roadmap, not chat-visible NPC-tick); Example 5 in conversation-examples kept (shows unique AI mid-draft reversal, not redundant with SKILL.md text); tension-architecture principles section kept (file is shared with vid-segment + vid-pressure-test, those skills shouldn't have to load SKILL.md for principles). Final state: SKILL.md 318 lines, brain-dump-mining 141, conversation-examples 237, script-skeleton-template 199, script-tension-architecture 224. 0 em-dashes, 0 attribution leaks across productized files. Audit-build-audit loop closed.
- 2026-05-22: **vid-voice-capture post-run reconciliation.** First real run landed in Billy's content vault (6 sources, ~8,744 words). Three findings patched. (1) **Schema-drift claim verified false.** An external review flagged `voice-profile-schema.md` and `voice-pressure-test.md` as still using folder-style `reference-pieces/{voice_context}/` paths against SKILL.md's single-file form. `grep` for the folder form returns zero matches anywhere; the single-file `.md` pattern is consistent across SKILL.md, knowledge/, templates, and writing skills. No reconciliation needed. (2) **`signature_phrases` filler leak.** `"right?"` recurred 4-of-4 sources and passed cross-validation, but it is a discourse marker, not signature. Added a surface-and-ask filler check: a candidate matching a known-filler shape (`right?`, `you know`, `like`, `so`, `okay`, `alright`, `I mean`, `basically`) is flagged to the creator before locking; load-bearing stays, filler routes to words-avoided. Hint list is a prompt, not a blacklist. Patched `voice-profile-schema.md`, `voice-extraction-methods.md`, `vid-voice-capture/SKILL.md` Stage 3. (3) **Source floor split by format-length.** The single `~5,000 words per context` rule meant `shorts` needed 30-plus reels. Split: long-form contexts (`youtube-script`, `tutorial`, `newsletter`, `podcast`, `talk`) use ~5,000 words or 3 to 5 pieces; short-form (`shorts`, `linkedin`, `twitter`) use 3 to 5 pieces. Patched `voice-extraction-methods.md` Source minimums + `SKILL.md` Prerequisites/Stage 1. Also reframed Stage 1 source intake: pasted transcripts are expected and accepted (Claude writes them to `raw/voice-sources/{slug}.txt` itself), not refused. Skill is in `skills-wip/` pending more iteration; eval loop deferred until writing skills exercise the artifacts.
- 2026-05-22: **Build-plan refresh: synthetic-audience cross-reference, voice family consolidation, vid-capture non-split.** Gap audit surfaced three architectural decisions; all three approved and applied here. (1) **Synthetic-audience subsystem now acknowledged.** The `aud-*` pipeline has its own build plan at `documents/synthetic-audience-plan.md` (4 MVP skills built, Phase 2 deferred). The main build-plan did not reference it. Added a new "Synthetic-audience subsystem (parallel track)" subsection to Section 4 and a parallel-track note to Section 6. No content duplication; the aud-* plan stays self-contained. (2) **Voice family consolidated into three sharp skills.** `vid-voice-capture` (build), `vid-voice-audit` (check), `vid-voice-update` (mid-draft signal triage, renamed from the odd `vid-voice-correction-capture`). `vid-voice-audit` is new in Phase 4 and ABSORBS the current voice-authenticity reviewer at `.claude/skills-wip/vid-pressure-test/references/reviewer-voice-authenticity.md`. When audit is built, that file will be deleted and pressure-test will invoke `vid-voice-audit` instead of running an inline reviewer. Net: one source of voice-truth (no parallel checks drifting), deeper than the reviewer was allowed to be (no top-3 cap, optional raw-sources sampling to keep curation honest, per-beat verdicts). `vid-voice-update` is the rename and adds explicit triage. Not every correction is a hard rule; the skill triages hard rule / one-time edit / preference shift and writes to voice-profile only when permanent. Phase 4 row count went 3 → 4; total content skills went 20 → 21. Vale linter integration bullet updated to reference the new name. (3) **vid-capture stays unified.** Considered splitting into 5 per-brick skills (story, proof, metaphor, testimonial, framework) and rejected it. The single-purpose principle applies to skills with genuinely different output types serving different audiences (LinkedIn vs YouTube hooks). vid-capture does one job five ways: classify raw material and write it into the right bank with the right schema. Splitting would force pre-classification of ambiguous material, fragment cross-cutting concerns (frontmatter, dedup, People stubs, wikilinks) across 5 files, and not match the creator's mental model ("capture this," not "capture-story this"). No `/capture` slash command either. Natural-language triggers already cover discovery and a router with nothing to route is duplicative. Documented here so the next session does not re-litigate the decision. **No skill code landed this session; all changes are plan-only.** The `vid-voice-audit` and `vid-voice-update` skills remain queued.
- 2026-06-04: **Voice family consolidation: built.** Extension of the 2026-05-22 plan from metadata-only to full build, per Billy's "we are doing every change, scope this properly" direction. Dev save-point committed first (`34b7412`) before any new code. Then the build. **Built `vid-voice-audit`** (`.claude/skills-wip/vid-voice-audit/SKILL.md` 188 lines + `references/voice-fault-rubric.md` 163 lines). Single-purpose pre-publish voice check, callable standalone OR as reviewer-2 sub-skill from pressure-test. Drops the top-3 cap (returns every finding ranked by severity), adds optional `raw/voice-sources/` sampling (2-3 random passages per run to keep curated reference set honest), returns a per-beat verdict map (hook / segment_N / ending → passes | soft-flag | would-reword) alongside the flat finding list. **Refactored `vid-pressure-test/SKILL.md`** to invoke `vid-voice-audit` as reviewer 2 (replacing the inline rubric). Pressure-test still takes top-3 hard findings for parallel-reviewer parity; remaining audit findings flow into piece.md `soft_issues_list`; the per-beat verdict map preserves into Phase 6 chat summary. **Deleted** the obsolete `.claude/skills-wip/vid-pressure-test/references/reviewer-voice-authenticity.md` (137 lines, content moved into audit). **Built `vid-voice-update`** (`.claude/skills-wip/vid-voice-update/SKILL.md` 176 lines). Three-signal triage skill: hard rule → append to `foundation/voice-profile.md` refusals + re-run audit on in-progress draft; one-time edit → rewrite locally, save nothing; preference shift → ask creator one direct question, route by answer. Narrower than business-os `voice-rule-capture` (which is 269 lines with Vale integration + feedback memory; neither applies here). **Wired sibling handoffs** into `vid-intro` (Phase 4 read-aloud), `vid-segment` (Phase 3 prose-pass read-aloud), `vid-ending` (Phase 3 grain pass): one paragraph each pointing at `vid-voice-update` for permanent-rule signals, with explicit guidance to NOT invoke it for one-time edits (it is a permanence gate, not a logger). Updated `documents/skill-knowledge-map.md` to point at vid-voice-audit instead of the deleted reviewer file. Verification: 0 em-dashes across all 7 affected files; reviewer file confirmed deleted; all line counts under target (audit 188, rubric 163, update 176); sibling-handoff present in all three writing skills.
- 2026-06-05: **vid-research output: 4 banks to 3, with adversarial-check revisions.** Scope audit found three real problems: (1) sub-banks duplicated data (title-patterns, power-words, thumbnail-patterns all reused worked examples from pattern-bank outliers); (2) routing was broken (vid-title never loaded power-words-bank despite the bank existing for that purpose); (3) padded fields nothing read (thumbnail-patterns-bank's vision data sat unread by vid-thumbnail, which is text-only). A three-agent workflow audit confirmed and an adversarial-check pass flagged two of my original cuts as real-concern: dropping `view_count` removed citation evidence that vid-framing actually uses ("@channel 145k views" anchor strength); dropping `hero_element` removed the design reference future vid-thumbnail-gen needs for novel-angle scenarios. Revised plan: keep both fields, add `outlier_multiplier` ("3.5x channel avg") as the real signal-strength field so AI ranks by multiplier not raw views (solving the bias concern without losing citation). **Changes applied.** Slimmed `pattern-bank-template.md` to new outlier row schema (dropped `format` only; added `video_id`, clickable URL, `outlier_multiplier`; kept view_count, hero_element, all other fields). Merged `title-patterns-bank-template.md` into new `title-bank-template.md` (one file: research + creator-curated, creator edits in place). Slimmed `power-words-bank-template.md` (dropped frequency / channels / confidence ranks; word fit is judged by when-it-lands / when-it-fails criteria, not popularity). Deleted `thumbnail-patterns-bank-template.md` (thumbnail data lives in pattern-bank outlier rows: image + strategy + text + hero element; future vid-thumbnail-gen queries pattern-bank by strategy match). **Updated consumers.** `vid-research/SKILL.md` writes 3 banks not 4 (description, What-this-produces, Phase 6 references, Phase 7 packaging-system seeding, Reference index, Related skills all updated). `vid-title/SKILL.md` now loads `banks/power-words-bank.md` (the routing-bug fix). `vid-framing/SKILL.md` load line collapsed from 4 banks to 1 (`pattern-bank.md` only). Verification: 0 em-dashes across all 7 affected files. No populated runtime banks existed yet, so no migration needed.
- 2026-06-11: **Pipeline reconciliation: packaging-first order, gap-fill beat, seam cleanup.** The script-writing skills had drifted off the canonical packaging-first chain (line 652), and a field-level verification sweep surfaced more seams. Fixed in one pass. **(1) Packaging-first order locked.** Title and thumbnail are a PACKAGING phase that runs after framing and before structure; structure never invokes title/thumbnail/intro. Rewrote the contradictory lines in vid-thumbnail, vid-title, vid-structure, vid-framing, vid-intro, vid-segment, vid-ending, plus this section's orchestrator-delegation prose and the ASCII flow diagram. **(2) Gap-fill beat.** vid-structure now writes a `## Blocks to capture` manifest into script.md aggregating every flagged block gap, then offers batch-now vs inline-later at the structure-to-prose seam. vid-segment reads and clears the manifest. Nothing silently drops; order-only, no enforced gate (creator's call). **(3) Dangling-ref cleanup.** `vid-foundation` (dead skill name) repointed to `/foundation` (the orchestrator) or the real producer (vid-positioning for iceberg, vid-research for packaging-system) across the writing skills + knowledge files + creator-setup + SYSTEM-MAP. `reference-block` collapsed to piece.md. SYSTEM-MAP bank count 4 to 3. Added pillar capture + piece.md creation to vid-intake (the field was producer-less). Removed deleted vid-packaging from interview-posture. **(4) hook/transition banks.** Authored `knowledge/hook-bank-template.md` + `knowledge/transition-bank-template.md` (generic starters mirroring the proven vault structure); wired a `seed` class into the creator-setup manifest with staged pending rows for vid-intro/vid-segment/vid-ending, so a new creator's vault gets seeded on setup, additive, creator-owned and grown (the title-bank model). **(5) Vocabulary.** Confirmed block/parable/principle throughout live files; renamed the `async-brick-notes.md` artifact to `async-block-notes.md`. **(6) Runtime guards.** Kept vid-intro's title+thumbnail hard-stop (de-facto packaging enforcement at runtime); added vid-ending non-stub-Intro guard + full-body requirement. Verification: static contract greps clean (no vid-foundation / reference-block / old-bank-names / structure-invokes-packaging in live files), live load-integrity clean. No orchestrator built: skills correct first, vid-pipeline on top later.
- 2026-06-11: **vid-ideas built (the optional front-door idea generator).** The pipeline started at `vid-intake`, which assumes a seed; nothing served the blank-slate moment ("I don't know what to make"). `vid-ideas` fills it. **Inputs (lean):** iceberg + pillars + avatar + Top 3 from `creator-foundation.md`, plus the `pattern-bank` synthesis + confirmed-winners + dropped sections (NOT the full outlier table). Deliberately does not load voice/reference/title banks; it proposes topics, not prose. The four-input set is a starting point, prunable if output skews. **Output:** ~5-6 ideas per batch, each anchored to a real pattern-bank signal (own-channel-proven / convergent / confirmed-winner) with 1-2 flagged experimental swings, each tagged to a pillar + Top 3 problem + iceberg-fit verdict. Anti-fabrication: every anchored idea cites a real bank entry; patterns are translated to the creator's pillars, never competitor titles copied; off-iceberg and dropped patterns rejected. **The dial:** in-session re-roll on "more / tighter / wilder / different pillar". **Backlog:** keepers only. The creator picks one to make now and flags any others they like; only those save to a new `content/ideas-backlog.md` (no junk dump), with sticky `dropped` status. **Handoff:** the picked idea hands a seed packet `{idea_title, pillar, top_3_problem, iceberg_fit, anchor}` to `vid-intake`, which captures the brain-dump; `vid-ideas` writes no piece folder. **Boundary vs vid-framing:** ideas picks the topic from blank, framing picks the angle once a topic exists. **Files:** new `.claude/skills-wip/vid-ideas/` (SKILL.md + references/idea-generation-rules.md + assets/ideas-backlog-template.md + WORKING-NOTES.md). Reuses the iceberg 2-layer check (`vid-intake/references/iceberg-and-top-3-alignment.md`), the signal tiers (`vid-framing/references/angle-anchor-rules.md`), and Theory of One (`vid-research/references/theory-of-one-curation.md`) by reference, not duplication. **Wired:** vid-intake When-to-run + Related skills (handoff note), SYSTEM-MAP Stage 4 (optional front-door entry), vault-integration (new `content/ideas-backlog.md` artifact schema; also fixed vid-intake's piece.md `type: piece` to canonical `type: content-piece`). Optional and standalone; stays in `skills-wip` until the chain is proven. Verification: 0 em-dashes, anchors cite real bank entries, block/parable/principle vocab, `/foundation` not `vid-foundation`.
- 2026-06-18: **vid-pipeline orchestrator built + lifecycle contract unified.** Before building the router, a 10-agent wiring-verification workflow mapped what each of the 9 writing skills ACTUALLY writes/reads in piece.md (not what descriptions claim), then an adversarial pass tried to break the proposed routing. It found the orchestrator-as-planned would stall in four places: (a) the lifecycle field was three different things (vid-intake wrote `status: ideating`, vid-framing/vid-structure wrote a separate `piece_status`, vid-intro/vid-ending wrote only boolean locks, vid-pressure-test wrote `pressure_test_status`); (b) `segments_completed` was written by zero skills, so the segment-loop counter was fiction; (c) routes read `status` values nothing wrote, leaving pressure-test unreachable; (d) the load-bearing one: vid-title / vid-intro / vid-ending / vid-segment SKIP their piece.md writes in sub-skill (pipeline) mode, so a pure-reader orchestrator would invoke them and nothing would persist. **Decisions (Billy):** skills own their lifecycle (each writes its own fields in BOTH standalone and pipeline mode); the orchestrator is a pure reader/router; title before thumbnail (forced, vid-thumbnail needs the locked title). **Contract unified on the canonical `status` field** (`ideating | drafting | filming-ready | filmed | editing | published`, already in vault-integration.md, which is the list-view status). The ad-hoc `piece_status` is RETIRED: vid-framing/vid-structure re-entry detection switched to field-presence (`selected_angle` present, `segment_purposes` present). The orchestrator routes on field-presence + `segments_completed` vs `segment_purposes` counts, not a parallel micro-status. **Dates:** `created` stamped once by vid-intake (fixes an existing mismatch, vid-framing already read `created` while intake wrote `captured`); `last_updated` bumped by every piece.md writer, per a new rule in the creator-setup asset CLAUDE.md + the vault-integration schema. **Edits:** all 9 writing skills + 2 assets (piece-framing-additions, pressure-test-frontmatter) + 2 example references + vault-integration.md piece schema + asset CLAUDE.md. **Built** `.claude/skills/vid-pipeline/SKILL.md` (thin router): foundation hard-gate, voice soft-warn, list-and-ask across multiple in-progress pieces, the field-presence routing table, stop-signals, filming-ready completion. Voice skills (capture/audit/update) explicitly NOT in the chain. Verification: 0 em-dashes across every edited file; repo grep for `piece_status` / `framed_at` / `structure_locked_at` clean in live files. The 8 wiring-verification patterns in `documents/skill-wiring-lessons.md` (especially #1 routing-is-a-bug-class and #2 every-field-needs-a-consumer) directly drove this; the workflow caught all four stalls before any orchestrator code landed.

---

## 13. Plugin packaging strategy

How this system distributes to other creators without overwriting their data on update. **Defer the actual restructuring** until Phase 3 skills land, but build with these rules in mind so we don't paint into a corner.

### Why this matters

When the system ships to other creators, three things must hold:
1. The creator gets updates when the plugin updates (skills, knowledge, bug fixes flow in).
2. **The creator's own data never gets overwritten.** Their foundation docs, captured stories, winning packages, content pieces, these are theirs. A plugin update touches none of it.
3. The structure is simple enough that a creator can install with one command and get to work.

Claude Code plugins solve all three IF the plugin/workspace boundary is clean. If we blur it (e.g. ship the user's banks alongside the skills), updates either wipe creator data or stop being safe. Get the boundary right.

### How Claude Code plugins actually work

- Plugins live cached at `~/.claude/plugins/cache/{marketplace}/{plugin}/` on the creator's machine
- **Plugin files are read-only.** On update, the cache directory is replaced wholesale.
- The creator's project workspace (their `foundation/`, their `banks/`, their `Content/`) is in a totally different location and never touched by Claude Code's plugin system.
- Skills inside the plugin reference internal assets via `${CLAUDE_PLUGIN_ROOT}/...`. This resolves to the plugin's cache location regardless of where the user invokes from.

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
├── skills/                                                    ← built skills plus planned skill folders
│   ├── vid-foundation/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── assets/
│   │       ├── creator-foundation-template.md
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
│   ├── vid-voice-capture/                                     ← owns voice-profile-template.md and voice-profile.md writes
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
├── foundation/
│   ├── creator-foundation.md                                  ← created by vid-foundation
│   ├── voice-profile.md                                       ← created by vid-voice-capture
│   └── packaging-system.md                                    ← created by vid-foundation Stage 4
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
│   └── email-sequences/
└── People/{name}.md
```

### Update safety rules: non-negotiable

**Rule 1: Skills never write to a workspace file that already exists without explicit creator approval.**

Pattern (used throughout the codebase already):
```
Silent check: read `foundation/creator-foundation.md` if it exists.
→ If exists: surface the first line and ask refresh / keep / replace.
→ If missing: create fresh.
```

Same rule applies to bank README scaffolding, title-bank seeding, CLAUDE.md scaffolding. **Existence check before write. Always.**

**Rule 2: Plugin updates do not touch the creator's workspace.** This is enforced by Claude Code's plugin system (the plugin cache is a different filesystem location from the creator's workspace), but skills also can't reach into the plugin cache to modify it. They reference plugin files via `${CLAUDE_PLUGIN_ROOT}` for read-only.

**Rule 3: First-run scaffolding is the ONLY time files copy from plugin → workspace.** After that, the creator owns those files. If a future plugin version updates a bank README schema, the creator decides whether to refresh. The plugin doesn't decide for them.

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
1. Plugin update happens (cache replaced), workspace untouched
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

Roughly 30-50 path edits across built and planned skills. Mechanical work.

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
  "description": "Video content operating system for YouTube creators: foundation, capture, voice, packaging, and per-video pipeline skills.",
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

- `1.0.x`: bug fixes, doc tweaks, knowledge file corrections (no new fields, no schema changes)
- `1.x.0`: new skills, new knowledge files, new bank types
- `2.0.0`: breaking schema changes (e.g. foundation doc fields renamed). Trigger a migration message on first run after upgrade.

Tag every release in Git: `authentic-ai-os--v{version}`.

### What this means for current development

Don't worry about plugin packaging yet. But when adding new skills or knowledge files, build them with these mental models:

1. **Knowledge files = universal.** Going to ship to every creator. Don't put creator-specific data here.
2. **Banks = creator-specific.** Don't ship pre-populated entries. Banks ship empty (with READMEs as scaffolding).
3. **Skills should never assume a path layout that wouldn't work post-`${CLAUDE_PLUGIN_ROOT}` migration.** Don't reach across the workspace to read another skill's internal files. Go through `${CLAUDE_PLUGIN_ROOT}` (during dev, this is just the relative `knowledge/` and skill-local paths; will become explicit later).
4. **Anything that scaffolds into the user workspace** should be in a skill's `assets/` folder. That's where templates live in the plugin model. We're already doing this for foundation templates; bank READMEs should move there during migration.

If we hold these rules during the rest of Phase 3, the migration is mechanical when we get there.

---

## How to resume work after a break

1. Read this file, top to bottom.
2. Check the Skills inventory (Section 4) for what's `⬜` next in the build order.
3. Check open questions (Section 10). Anything blocking the next skill?
4. Build the smallest unblocked thing first. Don't batch.
5. After building, update Section 4 (status), Section 12 (work log), and any relevant Section 10 entries.
6. The recent work log gets new entries dated; old entries stay. Decisions log via dated bullets, never delete history.
