# Authentic AI OS System Map

How the system works, skill by skill. Built from a full audit of all three skill roots (`plugins/authentic-ai-os/skills/`, `.claude/skills/`, `.claude/skills-wip/`), plus `knowledge/`, `banks/`, and `CLAUDE.md`, on 2026-06-19. vid-intake card refreshed 2026-06-24 (Top-3 removal, cold-open lazy-load, voice drop). All skill descriptions expanded 2026-06-29 from each skill's full SKILL.md, capturing the real mechanics (phases, decision gates, anti-fabrication rules) rather than a one-line summary.

**How to read a card:** each skill is a card. `READS` = the context loaded in. `WRITES` = what it produces. `NEXT` = what runs after. `STATUS` = the packaging tier.

**Three tiers, by packaging meaning:**

- `RELEASED` lives in `plugins/authentic-ai-os/skills/` and ships to creators.
- `STAGED` lives in `.claude/skills/`. Works in this repo, not yet released.
- `WIP` lives in `.claude/skills-wip/`. Not ready to ship.

**Three families.** The system runs three skill lines:

- `vid-*` the video pipeline (the backbone: idea to filming-ready script).
- `aud-*` the synthetic-audience pipeline (build avatars from real audience data, then panel-review content).
- `post-*` distribution (turn finished material into platform posts).

Plus one cross-cutting skill, `aaios-feedback`, available throughout.

> This map is a release-process artifact. It is regenerated as a mandatory step whenever a skill graduates (WIP to STAGED to RELEASED) or is parked. See the graduation checklist in `documents/RELEASE.md`, `documents/DEV-WORKFLOW.md`, and the `peak-release` skill.

---

## The video pipeline at a glance

```mermaid
flowchart TD
    classDef released fill:#1e3a5f,stroke:#4a90d9,color:#fff
    classDef staged fill:#2f3a1e,stroke:#9bd94a,color:#fff
    classDef wip fill:#3a2f1e,stroke:#d9a64a,color:#fff

    A["0. SETUP<br/>creator-setup"]:::released
    B["1. IDENTITY<br/>avatar to positioning to pillars<br/>to credibility to backstory"]:::released
    D["3. BANKS<br/>vid-research (released)<br/>+ vid-capture (staged)"]:::released
    C["2. VOICE<br/>vid-voice-capture"]:::staged
    E["4. PRE-SCRIPT<br/>ideas to intake to framing<br/>to title + thumbnail"]:::staged
    F["5. SCRIPT<br/>structure to intro to<br/>segment to ending"]:::staged
    G["6. REVIEW<br/>vid-pressure-test + vid-voice-audit"]:::staged

    A --> B --> D --> E --> F --> G
    B -.optional.-> C

    note["Blue = released. Green = staged. Tan = WIP.<br/>Stages 0-3 are one-time setup.<br/>Stages 4-6 repeat for every video."]
```

Build the creator's identity once, then the shipped handoff sends them to `vid-research` to fill the pattern banks. Voice capture and per-video stages 4-6 are STAGED (work in this repo, not yet released). The `aud-*` and `post-*` lines are WIP.

---

## Stage 0: Setup

### creator-setup `RELEASED`
One-time installer that scaffolds the workspace into the folder the creator names as their content home, working only inside that folder (never scanning above or below it). It is manifest-driven: it reads `manifest.md`, builds folders only for currently-released skills, and copies bank templates without overwriting creator edits. Routing has three branches: detect an existing workspace and run an additive update, flat-scaffold an empty directory, or inspect a populated vault by reading inside every plausible content-home candidate before recommending one. It always writes a scoped workspace `CLAUDE.md` plus a `.env.example`, never destroys creator content, and closes with a state-aware handoff to `/foundation` or `vid-research` depending on what is already locked.
- **READS**: `knowledge/update-check.md` (pre-flight), `knowledge/vault-integration.md`, the creator's `manifest.md`
- **WRITES**: the workspace folder structure (folders only), plus two seeded banks copied from templates: `banks/hook-bank.md` (from `hook-bank-template.md`) and `banks/transition-bank.md` (from `transition-bank-template.md`). Idempotent, never overwrites creator edits
- **NEXT**: /foundation

---

## Stage 1: Foundation Identity

`/foundation` is a thin orchestrator. It checks what's done and auto-advances the five identity skills in order. All five write into **one shared file**: `creator-foundation.md`.

### /foundation `RELEASED` · orchestrator
Thin orchestrator that runs no interviews itself. It does two silent checks: a workspace check (if `foundation/` and the workspace `CLAUDE.md` are missing it runs `creator-setup` first), then a state check that reads `creator-foundation.md` to see which sections are filled (Offer, Avatar, Top 3, Iceberg, Pillars, Credibility, Backstory). It maps that state to the next of five identity sub-skills, tells the creator in plain language what is locked and what comes next, then auto-invokes that skill with no friction step. It honors stop signals ("hold on", "stop here") by halting the chain, and once all five sections lock it offers `vid-research` as the only next step.
- **READS**: `creator-foundation.md`, `packaging-system.md` (to see what's done), `knowledge/feedback-offer.md`, `knowledge/update-check.md`
- **WRITES**: nothing (offers `vid-research` at Step 5, and `aaios-feedback` via the end-of-journey path)
- **NEXT**: runs avatar to positioning to pillars to credibility to backstory, then offers vid-research

### vid-avatar `RELEASED` · identity 1 of 5
The first foundation interview, a three-phase conversation that locks who the viewer is and writes Offer, Avatar, and Top 3 perceived problems. It asks one question at a time with an absorb-first posture, mirroring answers that spill across phases instead of re-asking. Phase 1 captures the Offer, Phase 2 the Avatar as a plain few-sentence description (never a structured field set), Phase 3 three genuinely different problems in the viewer's own language, using a "disappearance probe" ("if they already had that, what would disappear?") to turn solutions into problems. Every phase enforces a show-before-save gate where the creator locks the exact wording out loud, and Top 3 (flagged as where this skill most often fails) caps sharpening at two rounds per problem.
- **READS**: `knowledge/interview-posture.md`, `knowledge/vault-integration.md`, `knowledge/creator-foundation-template.md`, `knowledge/update-check.md`, `voice-profile.md` (if it exists)
- **WRITES**: `creator-foundation.md` (Avatar section)
- **NEXT**: vid-positioning

### vid-positioning `RELEASED` · identity 2 of 5
The second foundation skill, a drafting skill (not discovery) that produces the one-sentence Iceberg Statement. It hard-requires Offer, Avatar, and Top 3 to exist first, then builds from four internal components (WHO + WHAT + HOW + TENSION), where HOW is the differentiating mechanism and TENSION is a named enemy or refused axis that keeps the line from sounding like 1000 other channels. It drafts exactly two candidates that vary only the TENSION, never three rewordings of one template, then iterates in the creator's exact language under a read-aloud test. A literal-words rule preserves any short enemy phrase the creator repeated (like "cry it out") verbatim, and bland drafts get silently rejected against three checks: could 1000 channels say it, can the viewer picture searching it, does the creator reword it.
- **READS**: `creator-foundation.md` (Avatar, Offer, Top 3), `knowledge/interview-posture.md`, `knowledge/vault-integration.md`, `knowledge/update-check.md`
- **WRITES**: `creator-foundation.md` (Iceberg Statement)
- **NEXT**: vid-pillars

### vid-pillars `RELEASED` · identity 3 of 5
The third foundation skill, a discovery interview that locks 8 to 12 content pillars as short 1-to-4-word labels. Its defining move is root-cause framing: a pillar is not a category that sounds like the niche but another sub-problem that, when broken in the avatar's life, blocks the Iceberg promise (so if the Iceberg promises YouTube growth, "YouTube growth" cannot be a pillar). It proposes a starter list mined from the Top 3, the Offer and Avatar, and standard root causes the creator may not have named, then pushes tactics and single tools off the list with a "could you make 10 videos on this without repeating yourself?" test. It validates the full set ("if the avatar fixed all of these, would they get the promise?"), adds anything missing, enforces a floor of 8, and saves short labels only.
- **READS**: `creator-foundation.md` (Iceberg Statement, Top 3), `knowledge/interview-posture.md`, `knowledge/vault-integration.md`, `knowledge/update-check.md`
- **WRITES**: `creator-foundation.md` (Pillars section)
- **NEXT**: vid-credibility

### vid-credibility `RELEASED` · identity 4 of 5
The fourth foundation skill. It deliberately over-collects proof through sharp one-at-a-time prompts (personal results, client wins, recognized-authority proof, volume proof) then ranks it down to three viewer-relevant brags, each Big, Specific, Personal, declarative past tense, one number per sentence. The ranking pass is made visible to the creator and runs a false-belief test (a brag that kills a false belief beats a bigger number that kills nothing), an Iceberg-tension coverage check, and a mandatory anti-proof check that rewrites any brag reading as if the creator produced the failure. It writes twice: the locked three to the foundation verbatim, and every leftover strong proof point as its own `banks/proof-bank/` entry. It offers fallback brags for creators with no numbers yet.
- **READS**: `creator-foundation.md` (Avatar, Top 3), `knowledge/proof-bank-schema.md`, `knowledge/interview-posture.md`, `knowledge/vault-integration.md`, `knowledge/update-check.md`
- **WRITES**: `creator-foundation.md` (Credibility section) + seeds `banks/proof-bank/`
- **NEXT**: vid-backstory

### vid-backstory `RELEASED` · identity 5 of 5
The fifth and final foundation interview, locking a Problem-Action-Outcome backstory (1 to 2 conversational paragraphs plus a 3-sentence compressed intro version). It hard-requires Avatar and Iceberg first, then runs four questions with absorb-first posture: the starting state with numbers, the specific trigger, the concrete moves (flagged as where most backstories fail, demanding what they stopped, started, and tried that failed rather than "I built a system"), and the measurable outcome including any setback. It pushes hard against corporate tone and vague struggle, and never fabricates a detail the creator can't recall. For professionals who never had the avatar's problem, it swaps "you" for a clearly attributed real client and creates a wikilinked person stub. Since it completes the identity chain, it offers `vid-research` rather than auto-chaining.
- **READS**: `creator-foundation.md` (Avatar, Iceberg, Top 3), `knowledge/interview-posture.md`, `knowledge/vault-integration.md`, `knowledge/update-check.md`
- **WRITES**: `creator-foundation.md` (Backstory section)
- **NEXT**: vid-research (offers it at the close, launches on the creator's go). Voice capture is still in development and is not part of the shipped handoff

---

## Stage 2: Foundation Voice

### vid-voice-capture `STAGED`
Builds the creator's voice engine in two artifacts and deliberately stores no statistics or rhythm numbers. It runs a six-stage flow: write every source to disk under `raw/voice-sources/` before analysis (including pasted transcripts), group by `voice_context` (youtube-script, shorts, linkedin), then pull 3 to 8 verbatim intact passages per context, each with a plain-language `> Demonstrates:` line. Patterns that hold across contexts become the thin guardrail; single-context patterns stay in the reference pieces; single-source ones drop. It enforces a source floor (3 to 5 short-form pieces or ~5,000 words long-form), asks which live-delivered improvised moments to never draft (those become refusals, never seeds), and the read-aloud gate is absolute: nothing enters either file until the creator confirms it out loud. It produces `foundation/reference-pieces/{voice_context}.md` files plus a thin `voice-profile.md`, then stops without auto-invoking anything.
- **READS**: `creator-foundation.md`, `raw/voice-sources/` (creator's transcripts/scripts), `knowledge/voice-profile-schema.md`, `knowledge/voice-extraction-methods.md`, `knowledge/voice-pressure-test.md`, `knowledge/voice-rhythm.md`, `knowledge/interview-posture.md`, `knowledge/vault-integration.md`
- **WRITES**: `foundation/reference-pieces/{voice_context}.md` (verbatim passages, the voice engine), `foundation/voice-profile.md` (thin guardrail)
- **NEXT**: optional. Not yet wired into the released handoff chain

---

## Stage 3: Material Banks

Two skills fill the reusable banks. Done once, then topped up over time.

### vid-research `RELEASED`
Builds and refreshes the creator's three pattern banks from real YouTube data so downstream skills ground decisions in what audiences actually click. It runs Three-Circle Research (the creator's own channel, about 5 direct competitors, 3 to 5 adjacent channels), pulling data via a YouTube API key from `.env` (never hallucinated), setting a per-channel outlier floor off the median, recording every video that clears it, and running thumbnail vision classification on a studied subset. The hard rule between circles: adjacent niches contribute only transferable structure (title shapes, power words, thumbnail moves, formats), never topics. An LLM synthesis spread-ranks patterns across channels, then a Theory of One human curation pass (Keep / Drop / Modify per pattern, in plain language, drops kept sticky) decides what survives. It saves the three bank files plus a light `packaging-system.md` (a 3+1 format rotation and 1 to 2 thumbnail strategies to test), runs in three modes (full first build, quarterly refresh, 5-to-10-minute single-outlier add), and saves partial state after every phase so it resumes cleanly. It is the next step the foundation identity chain points to.
- **READS**: `foundation/creator-foundation.md`, `packaging-system.md`, `knowledge/three-circle-research.md`, `knowledge/outlier-identification-rules.md`, `knowledge/format-rotation-guide.md`, `knowledge/packaging-system-template.md`, `knowledge/theory-of-one-curation.md`, `knowledge/interview-posture.md`, `knowledge/thumbnail-text-patterns.md`, `knowledge/update-check.md` (pre-flight), YouTube API key from `.env`
- **WRITES**: `banks/pattern-bank.md`, `banks/title-bank.md`, `banks/power-words-bank.md`, `foundation/packaging-system.md`
- **NEXT**: vid-framing (its close points the creator there for the next video)

### vid-capture `STAGED`
A looped, single-item bank-capture skill with five stage flows (story, metaphor, proof, testimonial, framework) that runs standalone (loops after every save) or as a sub-skill another vid- skill calls mid-script (captures one item, returns its wikilink, skips the loop). The defining move is a dig-deeper requirement: it refuses the first pass and plans 2 to 3 probing rounds for the exact number or the worst-moment detail, then runs a dedup scan against existing bank files before saving. Each stage has its own logic (stories capture Problem-Action-Outcome and locate the lesson second, metaphors classify visual versus non-visual, testimonials stay verbatim with no cleanup, frameworks handle only the log path). Any named client auto-creates a `people/{Full Name}.md` stub with a bidirectional wikilink, and the entry is not saved if the stub fails. Anti-fabrication is absolute: if a prompt yields nothing, it writes "no story here yet" rather than inventing one.
- **READS**: `creator-foundation.md`, `voice-profile.md` (alignment checks), `knowledge/story-capture-guide.md`, `knowledge/proof-capture-guide.md`, `knowledge/metaphor-builder.md`, `knowledge/testimonial-capture.md`, `knowledge/framework-builder.md`, `knowledge/vault-integration.md`
- **WRITES**: `banks/story-bank/`, `banks/proof-bank/`, `banks/metaphor-bank/`, `banks/testimonial-bank/`, `banks/framework-bank/`, `people/{Name}.md` stubs
- **NEXT**: vid-intake

---

## Stage 4: Pre-Script (per video)

From here, work happens inside one video folder: `content/pieces/{slug}/`. `piece.md` is the **frontmatter hub** every per-video skill reads and updates. The one exception is `vid-ideas`, the optional front-door that runs before any piece folder exists.

### vid-ideas `STAGED` · optional front-door
The optional front-door for the blank-slate moment; skip it when the creator already has a topic. It hard-stops if `creator-foundation.md` or `banks/pattern-bank.md` is missing, then generates roughly 5 to 6 ideas one at a time off a five-step spine: start from a real winning title, name the single load-bearing element that drove its multiple, carry that engine onto the creator's topic (bounded so it is neither a lost engine nor the source with the nouns swapped), run a click test, and gate on iceberg fit. The hard anti-fabrication rule is that every anchored idea must cite a real per-channel row (actual title, channel, views, multiplier) and the cited engine must be the one actually used; 1 to 2 unproven experimental swings are allowed but flagged. An in-session dial (more / tighter / wilder / different pillar / regenerate) re-rolls the batch until the creator picks. It writes only keepers to `content/ideas-backlog.md`, keeps dropped ideas sticky, and hands the picked idea to vid-intake as a seed packet without creating a piece folder.
- **READS**: `creator-foundation.md` (iceberg, pillars, avatar, Top 3), `banks/pattern-bank.md`, `content/ideas-backlog.md` (if present), `knowledge/iceberg-and-top-3-alignment.md`, `knowledge/theory-of-one-curation.md`, `knowledge/update-check.md` (pre-flight), `knowledge/vault-integration.md`
- **WRITES**: `content/ideas-backlog.md` (kept ideas only). Writes no piece folder
- **NEXT**: vid-intake (hands the picked idea as a seed packet)

### vid-intake `STAGED`
Captures one video's raw material into `brain-dump.md` in the creator's exact words. It does not frame, title, or write. It runs five phases on one spine: open the door and silently match what the creator brought without naming a category, reflect back then checkpoint (derive a slug and write both `brain-dump.md` and a `piece.md` to disk immediately so a dropped session never loses the dump), offer one deeper pass on the 2 to 3 highest-leverage spots (pushing at most twice each, verifying uncertain claims via an isolated subagent, turning gaps into TODOs not inventions), confirm iceberg fit and name the likely pillar, then hand to vid-framing. It carries an internal taxonomy of material shapes (story, client-win, news, unbacked claim) it handles without ever telling the creator. The dump leads with a lossless verbatim `## Raw dump` as the source of truth, with organized sections layered on top as an index, and every save passes a Vale check for em-dashes. Cold open: it loads nothing until a phase needs it, the fit check is iceberg-only (no Top 3), and it never loads voice.
- **READS**: `creator-foundation.md` (Phase 4 fit check, not cold), `knowledge/story-capture-guide.md` (only when a thin story needs drilling), `knowledge/update-check.md` (pre-flight), `knowledge/vault-integration.md` (at save). `references/mode-conversation-examples.md` is fallback-only
- **WRITES**: `pieces/{slug}/brain-dump.md`, `pieces/{slug}/piece.md` (standalone). As a sub-skill, returns the packet to the caller and skips the save
- **NEXT**: vid-framing

### vid-framing `STAGED`
Picks the single angle for one video, built on one ordering principle: psychology first, evidence second. It reads the brain-dump, then gets into the one viewer's head (what they want, the main problem they are stuck on, the underlying tension, the transformation, the core payoff) and lays that read back in plain lines, waiting for a "that's the video" before building anything. Only after that yes does it pull `pattern-bank.md` to shape one or two angles that deliver the confirmed payoff, naming the real outlier (title, channel, views) where a pattern backs an angle so it is a hypothesis, not a guess. The hard rule: the pattern bank shapes and grounds the angle but never generates it, because an angle pulled from a bank with no viewer behind it is the generic AI angle the brand opposes. Every dropped angle gets a one-line reason and stays sticky across re-frames, and it never invents an outlier, number, or result.
- **READS**: `brain-dump.md`, `piece.md`, `creator-foundation.md`, `banks/pattern-bank.md`, `knowledge/three-circle-research.md`, `knowledge/outlier-identification-rules.md`, `knowledge/audience-temperature-model.md`, `knowledge/format-planners/{format}.md`
- **WRITES**: `piece.md` (angle, payoff, format, goal, viewer stage)
- **NEXT**: vid-title (packaging: title then thumbnail, locked before structure)

### vid-title `STAGED`
Packages a video into one title with a claim-first, differentiation-over-safety engine across five phases. Its most distinctive move is bank quarantine: it forbids reading the pattern, title, or power-words banks (or any competitor title) until Phase 3, because reading the nearest competitor title early turns the output into that title with the nouns swapped. Phase 1 gets into the viewer's head, builds a "lock list" of every verifiable specific in the material, and names the claim (the disagreeable true thing the video argues). Phase 2 writes 6 to 8 raw titles cold from the claim with the banks still closed. Phase 3 opens the banks to group titles into 4 to 5 lanes, pins a real competitor outlier with its multiplier to each, labels each crowded-or-underused and on-brand-or-off-brand, and names the on-brand-AND-underused lane "the opportunity." It presents that lane first as Recommended, with crowded lanes shown as the safe tradeoff, and kicks a number-driven title back to framing if the material has no real number to ground it.
- **READS**: `creator-foundation.md`, `packaging-system.md`, `knowledge/BENS-framework.md`, `knowledge/thumbnail-text-patterns.md`, `banks/pattern-bank.md`, `banks/title-bank.md`, `banks/power-words-bank.md`, `piece.md`, `brain-dump.md`
- **WRITES**: `piece.md` (title field)
- **NEXT**: vid-thumbnail (coordinates to avoid repeating words)

### vid-thumbnail `STAGED`
A thumbnail TEXT planner only. Layouts, hero elements, expressions, color, and AI prompts are out of scope (deferred to a future vid-thumbnail-gen skill). It builds a script-derived lock list of every verbatim number, then generates 5 to 10 candidates drawn from at least 3 of 5 named patterns (cognitive-dissonance, number-hero, named-system, single-word, imperative). Before any candidate is shown, six filters run: anti-fabrication (reject any number not on the lock list), curiosity-versus-spoiler (reject anything that gives away the central insight), tonal pairing, a distinctiveness test, an anti-pattern filter, and a title-overlap rule, all under a 2-to-4-word preference. It has the creator pick 1 to 2 winners and pushes back if both are the same strategy, then locks each with a tight rationale (text, strategy, BENS, one why-it-lands line, no composition spec). It saves `thumbnail-brief.md`, whose presence is how the pipeline knows this step finished.
- **READS**: `packaging-system.md`, `knowledge/thumbnail-strategy-menu.md`, `knowledge/thumbnail-text-patterns.md`, `knowledge/thumbnail-examples-library.md`, `knowledge/thumbnail-composition-guide.md`, `knowledge/BENS-framework.md`, `knowledge/gift-framework.md`, `knowledge/vault-integration.md`, `piece.md`, `banks/packaging-bank/`
- **WRITES**: `pieces/{slug}/thumbnail-brief.md`
- **NEXT**: vid-structure

---

## Stage 5: Scripting (per video)

`script.md` is built up incrementally: structure lays the skeleton, intro/segment/ending fill it in.

### vid-structure `STAGED`
Builds the Tier 1 outline for one video, running as a sparring partner not a form-filler. It mines every brain-dump item by silently tagging it Core / Tangent / Support / Combine, finds the title's central question and pushes the title-promise payoff late (60 to 80% through the body), picks 1 to 2 cross-segment threads, and maps surviving material onto the format's native body shape (Case Study is a narrative arc, Listicle is N items, never a generic "N segments" template). It surfaces an outline with per-segment material anchors, bank-pulled block candidates (surfaced not locked, empty banks reported as empty), handoffs, and an explicit CUTS/COMBINES list, looping until the creator locks. It then writes `script.md` (empty Intro and Ending stubs, format-native body sections each with material, block candidates, a 3-to-5 bullet outline, and a tension role, plus a `## Blocks to capture` manifest) and a `tension_plan` to piece.md. A gap-fill seam offers to batch-capture missing blocks now via vid-capture or fill them inline later, and no block is ever silently skipped.
- **READS**: `brain-dump.md`, `piece.md`, `creator-foundation.md`, `voice-profile.md`, `thumbnail-brief.md`, `knowledge/format-planners/{format}.md`, `knowledge/script-tension-architecture.md`, `knowledge/voice-profile-schema.md`, `knowledge/framework-builder.md` (via `assets/script-skeleton-template.md`), all 5 evidence banks
- **WRITES**: `pieces/{slug}/script.md` (skeleton + `## Blocks to capture` manifest), `piece.md` (structure status)
- **NEXT**: gap-fill decision (batch now or inline), then vid-intro. Title and thumbnail are already locked in Pre-Script
- Note: vid-structure does not load `vault-integration.md`, unlike the other writing skills

### vid-intro `STAGED`
Produces the full 6-part intro (Top 3 viewer questions, Hook, Problem/Result, Setup, Transition, with Credibility woven into one of the first three slots), hard-stopping if the title or thumbnail are not locked since the intro depends on both. It builds a lock list of every real number, name, and claim (the intro may use nothing outside it), derives the Top 3 viewer questions from the title plus thumbnail and gets them approved, and picks the hook lane by cross-referencing the format planner against the voice profile's preferred hook types. It generates 2 to 3 Hook candidates (each under ~5 seconds) and 2 to 3 Problem/Result candidates, builds the Setup as a three-clause contract that maps to the locked viewer questions, and weaves credibility into a claim moment rather than bolting it on as a self-intro. It runs the two-pass voice-pressure-test plus a creator read-aloud, handing permanent-sounding rewords to vid-voice-update before applying. It saves to `script.md` `## Intro` and, in sub-skill mode, returns an intro_packet to the caller.
- **READS**: `piece.md`, `thumbnail-brief.md`, `brain-dump.md`, `creator-foundation.md`, `voice-profile.md`, `reference-pieces/`, `banks/hook-bank.md`, `knowledge/intro-architecture.md`, `knowledge/parable-decision-matrix.md`, `knowledge/story-pulling-criteria.md`, `knowledge/proof-placement-rules.md`, `knowledge/metaphor-integration.md`, `knowledge/visual-proof-callouts.md`, `knowledge/thumbnail-text-patterns.md`, `knowledge/voice-profile-schema.md`, `knowledge/voice-pressure-test.md`, `knowledge/voice-rhythm.md`, `knowledge/vault-integration.md`, `knowledge/format-planners/{format}.md`
- **WRITES**: `script.md` (`## Intro`)
- **NEXT**: vid-segment (hands to vid-voice-update on a creator voice reaction)

### vid-segment `STAGED`
Writes one body segment at a time as parable (the show), then principle (the tell), then transition (the handoff). Its defining discipline is a two-pass internal review where structure locks before any prose is written. It reads (does not re-derive) the shape vid-structure already wrote, applies the format planner's parable/principle weighting, then runs the bank-pulling logic that is this skill's differentiator: querying all five evidence banks by their match fields and surfacing 0 to 3 candidates each with a WHY, under a hard no-fabrication gate (empty banks route to vid-capture mid-skill, swap block type, or skip). The structure pass loops until locked, then the prose pass writes in the creator's voice anchored to brain-dump phrasing first and reference-piece cadence second (grain only, never echoed words), runs Pass 1 of the voice check inline, and surfaces the draft for a read-aloud loop. It appends the prose under a named heading (never overwriting), updates `segments_completed` (the pipeline's body-progress counter), flips every pulled bank entry's status, then STOPS rather than writing the next segment.
- **READS**: `piece.md`, `brain-dump.md`, `script.md`, `voice-profile.md`, `reference-pieces/`, `creator-foundation.md`, `banks/transition-bank.md`, all 5 evidence banks, the parable/proof/story/metaphor/visual knowledge set (including `emotion-brick-decision-matrix.md` and `script-tension-architecture.md`), voice set, and `knowledge/format-planners/{format}.md` (see the dependency map for the full 17 + 7 list)
- **WRITES**: `script.md` (one body section), `piece.md` (banks used)
- **NEXT**: vid-segment again until done, then vid-ending (hands to vid-voice-update on a voice reaction)

### vid-ending `STAGED`
Writes only the close using the 3-Part End Formula (Pivot recaps the transformation in one sentence, Gap reveals the next problem from the avatar's Top 3, Bridge points to a specific real published video), hard-stopping unless the full body and a non-stub Intro already exist. It reads the intro verbatim to lift the Setup contract, hook lane, and credibility receipt, then picks the next video FIRST from what the creator has already published and converts, and derives the Gap as the problem that video solves (never inventing a problem or promising an unmade video). It sets the CTA shape from the goal (sales, emails, and views close differently) and obeys intro-coordination rules: pay off the Setup near-verbatim, do not reopen with the intro's hook lane, do not re-cite the same credibility receipt. It drafts 2 complete candidates (same Gap, different rhythm, 30 to 60 seconds), auto-rejects fabrication and banned phrases (including "thanks for watching"), and runs the voice check plus read-aloud. The load-bearing principle throughout is "never end a video": the close should be so smooth the viewer is already moving to the next one.
- **READS**: `piece.md`, `script.md` (full), `voice-profile.md`, `reference-pieces/`, `creator-foundation.md`, `banks/transition-bank.md`, `knowledge/emotion-brick-decision-matrix.md`, `knowledge/parable-decision-matrix.md`, `knowledge/intro-architecture.md`, `knowledge/story-pulling-criteria.md`, `knowledge/proof-placement-rules.md`, `knowledge/metaphor-integration.md`, `knowledge/visual-proof-callouts.md`, the voice set, `knowledge/vault-integration.md`, `knowledge/format-planners/{format}.md`
- **WRITES**: `script.md` (`## Ending`), `piece.md` (ending status)
- **NEXT**: vid-pressure-test

### vid-voice-update `STAGED` · writing sibling
A surgical, append-only triage skill whose entire job is reading a creator's mid-draft voice signal correctly and writing refusals to `voice-profile.md` ONLY when the correction is permanent. It classifies the signal into three types: a hard rule ("never use X", "swap Y for Z") which appends a refusal, a one-time edit ("this line specifically") which writes nothing permanent and hands back the local rewrite, and an ambiguous preference shift ("feels off") which it never classifies silently but asks one direct question ("avoided in future drafts too, or just this line?") and routes on the answer. For a hard rule it picks the refusal shape, appends it to the matching sub-section, and logs the change with date and trigger. When a hard rule lands during an active draft, it invokes vid-voice-audit on the in-progress script so the draft immediately picks up the new refusal. It refuses to run at all if `voice-profile.md` does not exist, since that bootstrap belongs to vid-voice-capture.
- **READS**: the flagged line + the creator's reaction, `foundation/voice-profile.md`, `knowledge/voice-profile-schema.md`
- **WRITES**: `foundation/voice-profile.md` (refusals only, and only when the correction is permanent). One-time edits rewrite the line in place and save nothing
- **NEXT**: returns control to the calling writing skill with a status packet. Invoked by vid-intro, vid-segment, vid-ending; also callable standalone

---

## Stage 6: Review (per video)

### vid-pressure-test `STAGED`
The last-mile adversarial audit of the fully-assembled script before filming, editing `script.md` in place rather than producing a separate report. It conditions its rubrics by piece context (goal sales weights source-traceability heavier, views weights AI-slop and retention), then spawns 4 independent fresh-context reviewers in parallel, each capped at its top 3 issues to force severity ranking: source-traceability, voice-authenticity (which invokes vid-voice-audit as its sub-reviewer), AI-slop, and retention-logic, every flag citing an exact quote and line. It consolidates into hard versus soft issues, then walks the hard ones one at a time with an Approve / Deny-and-rewrite / Skip loop, where hard-rule violations (fabricated claims, banned phrases, em-dashes) cannot be skipped, only fixed or marked as a gap to source before filming. A non-negotiable creator read-aloud is the final gate. It writes the `pressure_test_audit` block to piece.md and sets `status: filming-ready` only on a clean verdict, the pipeline's done signal.
- **READS**: `script.md` (full), `piece.md`, `creator-foundation.md`, `voice-profile.md`, `knowledge/script-tension-architecture.md`, `knowledge/voice-profile-schema.md`, `knowledge/intro-architecture.md` (via references/), `knowledge/audience-temperature-model.md` (via references/)
- **WRITES**: `piece.md` (pressure-test audit block), issue comments in `script.md`
- **NEXT**: filming (pipeline ends). Invokes vid-voice-audit as its voice reviewer
- Note: vid-pressure-test no longer loads the `format-planners/` (it did in a prior build)

### vid-voice-audit `STAGED` · review sibling
The system's single source of voice-truth, a read-and-report-only deep voice check. It reads the finished script against the creator's reference pieces, the voice-profile guardrail, brand.md, and optional raw transcript samples, then returns every failing line with no top-3 cap (unlike the parallel reviewers it replaces inside pressure-test). It can sample 2 to 3 random raw passages as background calibration to catch drift where the script matches the curated set but feels off against unfiltered transcripts. It scans sentence by sentence assigning Hard severity (refusal words, anti-patterns, breached hard rules, banned words, any em-dash) or Soft severity (rhythm mismatch, AI-default phrasing, generic where the creator goes specific), then produces a per-beat verdict map (hook, each segment, ending rated passes / soft-flag / would-reword). It writes a read-aloud-passing rewrite for every finding but never auto-edits the script, and on a dispute it does not argue, because the read-aloud test is the final arbiter.
- **READS**: `script.md` (full), `foundation/voice-profile.md`, `foundation/reference-pieces/`, `brand.md`, optional raw transcript samples, `knowledge/voice-pressure-test.md`, `knowledge/voice-profile-schema.md`, `knowledge/voice-rhythm.md`
- **WRITES**: a voice findings list (severity, location, quote, suggested rewrite) plus a per-beat verdict (passes / soft-flag / would-reword)
- **NEXT**: returns control. Runs as the last gate before filming (standalone) or as the voice reviewer inside vid-pressure-test (sub-skill)

---

## The video orchestrator

### vid-pipeline `STAGED` · orchestrator
A deliberately thin orchestrator that moves one piece from idea to filming-ready by reading its state and auto-invoking the next skill, never writing content itself. It runs two silent prerequisite checks (foundation hard-halts to /foundation if missing, voice-profile soft-warns but never blocks), then picks the piece via a fast path (a named slug, or led-with-material straight to vid-intake) or an entry menu, falling back to a scan of in-progress pieces and refusing to silently pick when several are open. Its core is a routing table matched top-to-bottom on piece.md frontmatter plus sibling-file presence (no angle to vid-framing, title-but-no-thumbnail to vid-thumbnail, segments below their target count loops vid-segment, and so on), with title always locked before thumbnail. It passes a pipeline-session context line so sub-skills skip re-running pre-flight, honors stop signals (state persists in piece.md for clean resume), and terminates at `status: filming-ready`. The voice skills sit outside the chain since they fire on their own triggers.
- **READS**: `piece.md` and sibling-file presence in `content/pieces/{slug}/`, `knowledge/update-check.md` (pre-flight only). No other knowledge files; the sub-skills own all knowledge loading
- **WRITES**: nothing (delegates to the skill it routes to)
- **ROUTES** (state to next skill): no framing → vid-intake; framed, no format → vid-ideas; format locked, no angle → vid-framing; angle locked, no title → vid-title; title locked, no thumbnail-brief → vid-thumbnail; thumbnail locked, no structure → vid-structure; structure locked, no intro → vid-intro; intro locked, segments incomplete → vid-segment (loop); segments complete, no ending → vid-ending; ending locked, not filming-ready → vid-pressure-test; filming-ready → done

---

## The audience pipeline (`aud-*`)

A separate pipeline that builds synthetic avatars from real audience data, then runs them as a review panel. Four skills, run in order. All `WIP`.

```mermaid
flowchart LR
    classDef wip fill:#3a2f1e,stroke:#d9a64a,color:#fff
    AI["aud-intake"]:::wip --> AB["aud-avatar-build"]:::wip --> AV["aud-validate"]:::wip --> AR["aud-review"]:::wip
```

### aud-intake `WIP` · audience 1 of 4
The first skill in the synthetic-audience line, strictly file-based: it refuses material pasted into chat and reads call transcripts from `inbox/audience/calls/` and comment CSVs from `inbox/audience/comments/`, capping each run at 5 calls and 100 comments. Calls get high-trust full processing (detect host versus prospect, stub any named prospect, scan only the prospect's lines for up to ~15 verbatim quote units tagged by five moment types: I-am, I-tried, I-fear, I-want, I-pushed-back), while comments get low-trust treatment kept only as vocabulary samples. A contamination scan runs on every unit, flagging 2+ AI tells, but never blocks per entry: flagged items are kept as `needs_review` and surfaced in one batched table at the end. Quotes are preserved verbatim with filler intact, because the voice is the data. It moves raw source files into `raw/audience/` as an audit trail rather than deleting them, and never auto-invokes the next skill.
- **READS**: raw transcripts in `inbox/audience/calls/`, comment exports in `inbox/audience/comments/{video-slug}.csv`, existing `banks/audience-data/` (incremental), `knowledge/synthetic-audience-method.md`, `knowledge/vault-integration.md`
- **WRITES**: `banks/audience-data/calls/{call-slug}.md`, `banks/audience-data/comments/{video-slug}/{id}.md`
- **NEXT**: aud-avatar-build

### aud-avatar-build `WIP` · audience 2 of 4
The second pipeline skill clusters the audience-data into a deliberately small 4 to 6 segments and drafts one synthetic avatar per segment, under a bounded-interview rule (3 clustering questions, 5 quotes shown per question, resumable state saved to `audience/state.md`). Clustering is creator-named, not Claude-named: Claude pre-clusters silently by language similarity (pain pattern, not demographics) and the creator picks, overrides, or splits. The load-bearing move is held-out segregation: before any avatar is drafted, the strongest 25 to 30% of each segment's quotes (preferring the hard-to-mimic I-fear and I-pushed-back ones) are written to `audience/held-out/` and read back from disk, because file-system separation, not working memory, is the guardrail that prevents the validation set leaking into the avatar. Avatars draft from the non-held-out pool only, on a fixed 4-section schema (Identity, Top Problems, Top Objections, Vocabulary Bank) where every claim needs 2+ citations from calls (single-citation claims get stripped as stereotype). Each saves with `status: draft`, unusable until validation flips it.
- **READS**: `banks/audience-data/`, `audience/state.md` (resume state), existing `audience/segments/` and `audience/avatars/` for refresh, `knowledge/synthetic-audience-method.md`, `knowledge/vault-integration.md`
- **WRITES**: `audience/segments/{slug}.md`, `audience/held-out/{slug}.md` (written before drafts), `audience/avatars/{slug}.md` (status: draft)
- **NEXT**: aud-validate

### aud-validate `WIP` · audience 3 of 4
The gate, and the only skill permitted to read `audience/held-out/`. It runs three deterministic pass-or-fail tests per draft avatar: quote attribution (mix 5 of the avatar's own held-out quotes with 5 from another avatar, ask "would you say this?", require 7/10), objection prediction (feed a generic in-niche offer, require 2 of the top 3 predicted objections to substance-match the real held-out I-pushed-back quotes), and vocabulary leak (describe the top problem in 100 words, require novel words under 15% against the avatar's own vocabulary plus common English). The tiering is the distinctive logic: tests 1 and 3 yield `validated-vocabulary` (usable for vocabulary and objections, not behavioral predictions), all three yield `validated-full` (usable for any review), anything less stays `draft`. It writes a plain-English report (statistics jargon is banned from creator-facing output), runs one validation per date so results cannot be gamed, and never auto-invokes aud-review.
- **READS**: `audience/avatars/{slug}.md` (status: draft), `audience/held-out/{slug}.md`, `knowledge/common-english.txt`, `knowledge/synthetic-audience-method.md`, `knowledge/vault-integration.md`
- **WRITES**: `audience/avatars/{slug}-validation-{date}.md`, sets avatar `status` to `validated-vocabulary` or `validated-full`
- **NEXT**: aud-review

### aud-review `WIP` · audience 4 of 4
The final pipeline skill runs a panel of only validated avatars against one piece (script, email, paired title+thumbnail, hook, or CTA), filtering by content type (CTA review demands validated-full only; title+thumbnail are always reviewed as one paired artifact). The core move is subagent isolation: each avatar runs in its own isolated subagent that sees only its own profile, the piece, the content-type question block, and the 5 scoring dimensions, with no knowledge of the other avatars or the synthesis, and each response is written to disk before the next runs. Synthesis reads those files back and computes the median (never the mean, so a lone skeptic is not averaged away), flags dissent wherever an avatar scored 3+ below the median and quotes its reason verbatim, then computes a verdict (REWRITE, FIX-THEN-SHIP, or SHIP). Top-3 fixes must each be actionable in 60 seconds, and a stale-data calibration check is force-appended if the audience data is more than 60 days old. Each re-run creates a new numbered iteration folder rather than overwriting.
- **READS**: validated avatars in `audience/avatars/` (status validated-*), `banks/audience-data/` (calibration date check), the piece being reviewed, `knowledge/synthetic-audience-method.md`, `knowledge/vault-integration.md`
- **WRITES**: a review with a verdict (SHIP / FIX-THEN-SHIP / REWRITE)
- **NEXT**: none (terminal; returns to the creator)

---

## The distribution line (`post-*`)

### post-write `WIP`
The first skill in the distribution family, turning one source (an ideas batch or a long-form script, transcript, or article) into multiple platform posts written one at a time with an approval gate. Its defining rule is that two layers never collapse: post-type is the shape of the idea (mistake, story, framework, contrarian, warning, and so on) and platform is the delivery (LinkedIn, Instagram carousel, Instagram caption). It splits the source into one-idea-per-post units in the creator's exact phrasing, fit-filters each through the iceberg + Top 3 gate, then runs a core-first loop: write one platform-agnostic core piece with an engineered hook, run an anti-slop pass (strip AI tells, hedging test, hook test, read-aloud, no invented numbers), and lock the core with the creator BEFORE adapting it per platform, so no platform effort is spent on a piece about to change. Adaptation is a real per-platform transformation with its own re-engineered opening line, and carousels first pass a "worth-it gate" that defaults a single story to a caption. It saves one note per idea with provenance wikilinks in frontmatter but clean paste-ready `## Publishable` blocks in the body, and never fabricates a story, number, or client to make a post land.
- **READS**: `creator-foundation.md` (iceberg, Top 3), `voice-profile.md`, `reference-pieces/`, the source (an ideas batch or a long-form piece, including finished `script.md` from the video line), `knowledge/iceberg-and-top-3-alignment.md`, `knowledge/ai-hedging.md`, `knowledge/voice-profile-schema.md`, `knowledge/voice-pressure-test.md`, `knowledge/vault-integration.md`
- **WRITES**: platform posts (LinkedIn argument, Instagram carousel slide copy + visual brief, Instagram caption)
- **NEXT**: none (terminal). Post-type (the shape of the idea) and platform (the delivery) never collapse into each other

---

## Cross-cutting: Feedback

Not a pipeline stage. The feedback channel is available throughout. It surfaces via the offer protocol when a skill fails, when a creator is clearly frustrated, or when a journey completes, and it can be invoked by name any time.

### aaios-feedback `RELEASED`
The plugin's feedback channel. It turns a creator's one or two sentences into a structured bug report and sends it to Billy, not to Claude. It silently reconstructs context from the session (which skill ran and where it went sideways), looks that skill up in the capture map, and assembles a replay bundle: a reproduction case rebuilt from how the creator actually responded, a snapshot of the determinative vault files (each under a path header, but never held-out quote files), the bad output verbatim, and a tagged failure mode plus the plugin version. It asks at most two light questions (severity, what happened versus what they wanted), always writes a local copy to `feedback/{date}-{skill}.md` before any network call as both record and fallback, then runs a mandatory consent gate that previews exactly which real files will be sent before submitting. On failure it does not retry in a loop; it gives the creator the form link and confirms the saved local copy so nothing is lost.
- **READS**: `knowledge/feedback-submit.md` (endpoint + payload + curl recipe), `knowledge/feedback-capture-map.md` (what to capture per skill), `knowledge/feedback-offer.md` (the proactive offer protocol), `knowledge/vault-integration.md`, `.claude-plugin/plugin.json` (version), plus the determinative vault files the capture map names for the skill being reported
- **WRITES**: a local copy at `feedback/{date}-{skill}.md` (record + fallback), and a submission to the `aaios-feedback` form on peak-tools via a public Convex endpoint
- **OFFERED BY**: `/foundation` at the end of the identity chain (Step 5), and any skill via `knowledge/feedback-offer.md`, under a once-per-session guard
- **NEXT**: none (terminal; returns to whatever ran)

Feedback is only invited for **RELEASED** skills (those in `plugins/authentic-ai-os/skills/`). STAGED and WIP skills do not ship, so a creator cannot have run them. The capture map's tiering is the source of truth.

---

## The files that get reused everywhere

A few files carry context across many skills. If you understand these, you understand the data flow.

| File | Who reads it | What it carries |
|------|--------------|-----------------|
| `creator-foundation.md` | every identity, pre-script, script, and post skill | The identity: avatar, iceberg, pillars, credibility, backstory |
| `voice-profile.md` | capture + every writing skill + post-write | The thin voice guardrail, loaded before any prose |
| `foundation/reference-pieces/` | every writing skill, vid-voice-audit, post-write | The verbatim voice engine, the passages prose is written from |
| `piece.md` | every Stage 4-6 skill | Per-video frontmatter hub. Status flags gate the pipeline |
| `knowledge/vault-integration.md` | 20 skills | The routing, frontmatter, and wikilink rules contract |
| `knowledge/voice-profile-schema.md` | 9 skills | The voice-profile structure, loaded by everything that touches voice |

The **5 evidence banks** (story, proof, metaphor, testimonial, framework) are filled once by `vid-capture` and pulled as blocks by `vid-structure` and `vid-segment`. The **audience-data bank** is filled by `aud-intake` and consumed by the rest of the `aud-*` line.

---

## Audit findings

Every skill, knowledge file, and bank was grep-verified on 2026-06-19 against all three skill roots. The wiring is sound. The gaps are all expected for a work-in-progress build.

**Open gaps (expected for a WIP build):**

- **The video orchestrator exists; the other two lines have none yet.** `vid-pipeline` chains the per-video stages 4-6 and is STAGED. The `aud-*` and `post-*` lines have no orchestrator, so they run as manual invokes until one is written. Expected, not a defect.
- **Five bank-schema files are orphaned** (`framework-bank-schema`, `metaphor-bank-schema`, `packaging-bank-schema`, `story-bank-schema`, `testimonial-bank-schema`). They are staged ahead of `vid-capture`, which currently loads the matching `-builder` and `-capture` guides instead. They wire up when vid-capture is finished. See the dependency map, section 3.
- **`aaios-feedback` skips the update-check pre-flight** that the other eight released skills run. Intentional for a terminal cross-cutting skill that runs mid-session after another skill already checked.
- **Two decision-matrix files coexist** (`parable-decision-matrix.md`, `emotion-brick-decision-matrix.md`), both consumed by vid-segment and vid-ending. The `emotion-brick-*` name predates the Block System rename to parable/principle and may be legacy. Worth a content audit before either skill ships.

**Verified as correct (not issues):**

- **Knowledge files all wired, with five known exceptions.** Every file in `knowledge/` except the five orphaned bank-schemas is referenced by at least one skill. The capture/placement guides load conditionally deep in skill bodies, not always in header read-lists.
- **`thumbnail-composition-guide.md` is loaded** by vid-thumbnail. It was an intentional orphan in an early map; it no longer is.
- **The `hook-bank` / `transition-bank` references resolve.** They were re-architected as vault banks (`banks/hook-bank.md`, `banks/transition-bank.md`) seeded by creator-setup from `hook-bank-template.md` and `transition-bank-template.md`. No broken references remain.
- **`/foundation` and `vid-backstory` both hand off to `vid-research`.** The shipped foundation chain offers vid-research at the close and launches it on the creator's go. Voice capture is STAGED and not yet part of the released handoff.
- **`vid-avatar` reading `voice-profile.md` is correctly guarded** with "if it exists". Voice capture runs later, and the skill handles its absence cleanly.

**Note on the `foundation/` folder:** in this dev repo `creator-foundation.md` sits at the root with no `foundation/` directory. That is expected. The client installer scaffolds `foundation/` on setup. Not a bug.
