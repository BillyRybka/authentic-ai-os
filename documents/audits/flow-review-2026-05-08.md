---
type: audit
doc: flow-review
project: authentic-ai-os
date: 2026-05-08
status: active
tags: [audit, flow-review, pipeline, integration]
---

# Build Spec for Missing Writing Skills, Derived from Built-Skill Contracts (2026-05-08)

> [!note] Reframe note
> Originally scoped as an end-to-end flow review. Reframed mid-task: the BUILT 5-skill chain (vid-title, vid-thumbnail, vid-intro, vid-segment, vid-ending) is too partial to verify end-to-end coherence. The real deliverable is a build spec for the UNBUILT skills (vid-intake, vid-framing, vid-structure, vid-pressure-test, vid-pipeline) derived from the contracts the built skills already declare. Shutdown was requested before a full rewrite, so the original stage-by-stage trace is preserved below as the contract source.
>
> How to read this file as a build spec:
> - Stages 1, 2, 3, 9, 10 below are the UNBUILT skills. Each has a "Contract Phase 4 build must honor" sub-section that IS the build spec.
> - "Cross-stage seams" lists the open questions and contract ambiguities to resolve before building (especially Seam #1 thumbnail ordering, Seam #4 meta.md ownership, Seam #5 segment list shape).
> - "Recommended Phase 4 priorities" is the build order.
> - Re-fire a flow review against the full 8-skill pipeline once Phase 4 builds complete. Today's review cannot verify end-to-end coherence because half the pipeline does not exist.

## Summary

- Pipeline traced for hypothetical Peak Systems video. Idea: "How I cut my client onboarding from 2 weeks to 90 minutes." Format: Case Study. Avatar problem: #1 (solo founder drowning in onboarding admin). Voice: Billy's.
- BUILT skills (8): vid-foundation, vid-voice-capture, vid-capture, vid-thumbnail, vid-title, vid-intro, vid-segment, vid-ending.
- UNBUILT skills (4 in pipeline): vid-intake, vid-framing, vid-structure, vid-pressure-test, plus vid-pipeline orchestrator.
- Verdict on built portion: SEAMS PRESENT. The four BUILT writing/packaging skills (title, thumbnail, intro, segment, ending) form an internally coherent chain on the happy path AS LONG AS the upstream NOT-BUILT skills produce the contracts they each declare. Two real seams exist between BUILT skills (intro→thumbnail ordering, segment→ending packet hand-off). The bigger risk is silent contract drift between BUILT skills and the unwritten upstream skills (vid-intake, vid-framing, vid-structure), which together feed half the inputs that intro/segment/ending depend on.

## Stage-by-stage trace

Hypothetical scenario context used throughout: slug `cut-onboarding-2-weeks-to-90-minutes`, format `case-study`, goal `sales`, pillar `systems-and-automation`. Avatar problem #1 = "solo founder drowning in onboarding admin." Transformation = 2-week onboarding shortened to 90 minutes.

### Stage 1, vid-intake → brain-dump.md

- BUILT: NO.
- Build-plan name: "Raw material capture with type tagging." Spec: produce `Content/pieces/{slug}/brain-dump.md` (Section 4 inventory line 445).
- Expected output (inferred from downstream consumers):
  - File at `Content/pieces/{slug}/brain-dump.md`.
  - Contents must include the actual numbers/named methods/named clients in the creator's voice (vid-title's "lock list" reads from here, vid-intro's "lock list" too, vid-segment's voice anchoring leans on it as "the brain dump IS the voice").
  - Should include type-tagged fragments per build-plan ("type tagging"). Tag taxonomy not yet defined.
- Downstream consumers: vid-framing (NOT BUILT), vid-structure (NOT BUILT), vid-title (BUILT, reads brain-dump as source for lock list), vid-intro (BUILT, hard requirement: "brain dump or reference block exists"), vid-segment (BUILT, hard requirement: "brain-dump.md AND/OR reference-block.md exists"), vid-ending (BUILT, less direct, reads body in script.md but reference-block.md fallback).
- Contract that Phase 4 build must honor:
  1. Path: exactly `Content/pieces/{slug}/brain-dump.md`. All four BUILT writing skills hardcode this path.
  2. Must contain the locked numbers in plain readable form, since title/intro/segment build their lock lists by scanning this file and reference-block.md verbatim. If brain-dump is too summarized, the lock list comes up empty and skills push back on the creator.
  3. Should preserve creator's actual phrasing (not Claude-polished). vid-segment Phase 3 says "the brain dump IS the voice. Don't polish into 'better' prose."
  4. Must also create or seed `Content/pieces/{slug}/meta.md` with at minimum frontmatter `format`, `goal`, `pillar` so downstream skills can load it. UNCLEAR whether vid-intake or vid-framing creates meta.md. Build-plan does not say. SEAM.
- Hand-off coherence: UNBUILT, but the contract is documented enough across consumer skills that a Phase 4 builder can construct it. The meta.md ownership question is the open one.

### Stage 2, vid-framing → reference-block.md

- BUILT: NO.
- Build-plan name: "3-5 framings, Core Payoff, format pick, goal pick. Output: reference-block.md" (Section 4 line 446).
- Expected output (inferred from downstream consumers):
  - File at `Content/pieces/{slug}/reference-block.md`.
  - Must contain "the locked angle" and "core payoff" and "segment job" / "point list" (vid-segment Phase 1 references all three by name).
  - Must contain the format pick (case-study) and goal (sales). UNCLEAR whether reference-block.md holds these or whether vid-framing also writes them into `meta.md`. Both vid-segment and vid-intro hard-require `meta.md` to have `format` and `goal` set, so SOMEONE upstream has to populate meta.md. Logical owner: vid-framing (since it picks format and goal). SEAM.
  - Should include the segment list: "step 1 of 5, point 3 of 7, the case-study story beat" per vid-segment's "Frame the segment" example. UNCLEAR whether vid-framing or vid-structure produces this list. vid-structure spec says "keep/cut/combine review, Type 1 skeleton" suggesting structure decomposes ideas into segments, but vid-segment reads its segment job from reference-block.md, not from a structure artifact.
- Downstream consumers: vid-structure (NOT BUILT), vid-intro (BUILT, alternative source if no brain-dump), vid-segment (BUILT, reads "the segment's purpose in the body" from here), vid-ending (BUILT, reads "transformation the video delivers").
- Contract that Phase 4 build must honor:
  1. Path: exactly `Content/pieces/{slug}/reference-block.md`.
  2. Must populate `meta.md` `format:`, `goal:`, `pillar:` so vid-segment and vid-ending can load them. (Or vid-structure handles this. To be specified.)
  3. Must include the segment list in a parseable form vid-segment can read. UNCLEAR shape. SEAM.
  4. Must contain "core payoff" and "locked angle" as named sections so vid-segment Phase 1 can pull them.
- Hand-off coherence: UNBUILT, contract is partially documented across consumers but the segment-list shape and meta.md write ownership are gaps Phase 4 must close.

### Stage 3, vid-structure → script.md skeleton

- BUILT: NO.
- Build-plan name: "Keep/cut/combine review, Type 1 skeleton assembly. Invokes vid-title and vid-intro" (Section 4 line 447).
- Expected output:
  - `Content/pieces/{slug}/script.md` exists with a skeleton (segment headings, intro placeholder).
  - Title locked in `meta.md` (via invoking vid-title).
  - Intro written into `script.md ## Intro` section (via invoking vid-intro).
- Downstream consumers: vid-segment, vid-ending, vid-pressure-test, vid-pipeline orchestrator.
- Contract that Phase 4 build must honor:
  1. Must invoke vid-title in sub-skill mode (vid-title returns title string, vid-structure writes to meta.md per vid-title SKILL.md "Sub-skill mode: caller handles the save").
  2. Must invoke vid-intro in sub-skill mode (vid-intro returns intro_packet, vid-structure writes the intro into script.md `## Intro` AND writes the meta.md flags `intro_locked`, `intro_strategy`, etc.).
  3. CRITICAL ORDERING SEAM (see Cross-stage seams #1): vid-intro's hard requirement is `thumbnail-brief.md` exists. So before vid-structure can invoke vid-intro, EITHER vid-thumbnail must have already run, OR vid-structure must invoke vid-thumbnail first too. Build-plan Section 5 says "thumbnail decision might invoke vid-thumbnail here or defer to a separate run", which leaves this unresolved. The intro skill cannot run with thumbnail deferred, full stop.
  4. Must produce the segment list that vid-segment will loop over.
- Hand-off coherence: BLOCKED until the thumbnail ordering is resolved (see Seam #1).

### Stage 4, vid-title → meta.md (locked title)

- BUILT: YES.
- Input expected: `meta.md` exists (or is created by this skill, vid-title says "if missing, hard stop, run vid-foundation first" but the prerequisite is foundation docs, NOT a piece meta.md, so vid-title implicitly creates or expects meta.md). `creator-foundation.md`, `packaging-system.md`, plus `brain-dump.md` / `reference-block.md` / `script.md` (whichever exists). `banks/title-bank.md` (with seed fallback).
- Output produced:
  - Standalone mode: writes `title:` field to `Content/pieces/{slug}/meta.md` and updates `last_refreshed`.
  - Sub-skill mode: returns title string + BENS letters to caller; caller saves.
- Downstream consumers: vid-intro (reads `meta.md` `title:` and uses locked title to derive Top 3 viewer questions), vid-thumbnail (reads `meta.md` for locked title to pair with thumbnail text), vid-ending (reads `meta.md`).
- Hand-off coherence: PASS, with one note. Both vid-intro and vid-thumbnail explicitly load `Content/pieces/{slug}/meta.md` and use the `title:` field. Schema match: title is a string in meta.md, both consumers expect a string. 
- Notes: vid-title respects title-thumbnail pairing implicitly. If vid-thumbnail has run first, vid-title reads thumbnail-brief.md and avoids word repeats. Mutual coordination already documented.

### Stage 5, vid-thumbnail → thumbnail-brief.md

- BUILT: YES.
- Input expected: `meta.md` with locked title, `packaging-system.md`, `script.md` if exists, `banks/packaging-bank/*.md` (with empty-bank fallback).
- Output produced: `Content/pieces/{slug}/thumbnail-brief.md` with frontmatter `type: thumbnail-brief`, `title_paired:`, `strategies_tested:`, `picks:`, `creation_path:`, `captured:`, `status:`, `tags:`. Body follows `assets/thumbnail-brief-template.md`.
- Downstream consumers: vid-intro (REQUIRES thumbnail-brief.md to derive Top 3 viewer questions per Phase 1 step 11 and per knowledge/intro-architecture.md Step 1).
- Hand-off coherence: PASS schema-wise. The thumbnail-brief.md path is fixed. vid-intro reads it as part of its silent loads. The picks plus strategy plus title pairing all flow into vid-intro's question derivation.
- Notes: Schema mismatch risk on the `picks:` field. vid-thumbnail's frontmatter declares `picks: 2` (a count). The actual picked text is in the body, not frontmatter. vid-intro reads "the locked thumbnail picks" but does not specify whether it parses body or frontmatter. Either works since it's a silent context load, but if a future audit/test wants to query "what's the thumbnail text" programmatically, the body-vs-frontmatter ambiguity is a small seam.

### Stage 6, vid-intro → script.md ## Intro

- BUILT: YES.
- Input expected (5 hard requirements, all explicit in SKILL.md):
  1. `foundation/creator-foundation.md` (avatar Top 3 problems, credibility brags).
  2. `foundation/voice-profile.md` (preferred_hook_types, opener pattern, energy baseline, words avoided, anti-patterns).
  3. `Content/pieces/{slug}/meta.md` with `title:` locked AND `format:` set.
  4. `Content/pieces/{slug}/thumbnail-brief.md` with locked picks.
  5. `brain-dump.md` OR `reference-block.md` exists.
- Plus conditional loads: hook-bank.md, transition-bank.md (Sections 1 + 4), format-planners/{format}.md, voice-rhythm.md, voice-pressure-test.md, intro-architecture.md, reference-pieces, story-bank/proof-bank/testimonial-bank if credibility-line uses them.
- Output produced:
  - Standalone: writes `## Intro` section to `Content/pieces/{slug}/script.md`. Updates `meta.md` with `intro_locked: true`, `intro_strategy:`, `intro_hook_type:`, `intro_credibility_form:`, `voice_pressure_test:` block, `last_refreshed:`. If banks consumed, updates `stories_used:`, `proofs_used:`, `testimonials_used:` AND each bank entry's `used_in:` and `status:` (bidirectional rule honored explicitly).
  - Sub-skill: returns `intro_packet` per the documented schema (full_intro, hook, problem_result, setup, transition, credibility, proof_used, stories_used, voice_pressure_test).
- Downstream consumers: vid-segment (reads `## Intro` for "prior segment closing line and prior banks pulled inform setup continuity"), vid-ending (reads `## Intro` section for Setup contract, hook lane, problem anchor, credibility line, per its callback rules).
- Hand-off coherence: STRONG. The intro_packet schema in vid-intro SKILL.md "Output packet" section is mirrored almost field-for-field in vid-ending SKILL.md Phase 1 step 14, where vid-ending reads `setup.text`, `setup.top_3_questions_used`, `problem_result.top_3_problem_anchored`, `hook.text`, `hook.type`, `credibility.text`. This is the single best example of cross-skill contract discipline in the BUILT set.
- Notes:
  - `visual_proofs_called_out:` schema is introduced by vid-intro AND used by vid-segment. Both skills append to the same array. Coherent.
  - `intro_locked` flag in meta.md is a useful sentinel for vid-pressure-test or future orchestrators to gate downstream phases.

### Stage 7, vid-segment → script.md (per body segment, runs N times)

- BUILT: YES.
- Input expected: foundation/creator-foundation.md, foundation/voice-profile.md, foundation/reference-pieces (optional), knowledge/format-planners/{format}.md, voice-rhythm.md, voice-pressure-test.md, capture-guides for each bank type, `meta.md`, `brain-dump.md` AND/OR `reference-block.md`, `script.md` (for prior segment continuity), the relevant bank folders.
- Output produced: appends segment prose under a heading (`## Step 2: Refactor your week`) to `Content/pieces/{slug}/script.md`. Appends bank wikilinks to `meta.md` `stories_used`, `proofs_used`, `metaphors_used`, `frameworks_used` (note: `frameworks_used` introduced here, not in vid-intro's set, see Cross-stage seams #2). Appends to `visual_proofs_called_out:` array. Logs `voice_pressure_test:` block (overwrites or appends? UNCLEAR, see Cross-stage seams #3). Updates each pulled bank entry's `used_in:` and `status: used` per the "update both sides" rule. Sub-skill mode returns `segment_packet`.
- Downstream consumers: next vid-segment invocation (reads prior segment's closing line for setup continuity), vid-ending (reads body in script.md to lift transformation language and identify the avatar problem the body resolved), vid-pressure-test (reads full assembled script).
- Hand-off coherence: STRONG within the loop. Each segment cleanly reads prior and writes the same shape. The bidirectional bank-update rule is honored.
- Notes:
  - The `voice_pressure_test:` block in meta.md is written by both vid-intro AND vid-segment. The schema in each is identical, but if both skills write it as an object (not an array), the second write overwrites the first. SEAM (see Cross-stage seams #3).
  - The framework-bank reads for `framework-shapes.md` are skill-local references, not in the global knowledge folder. OK, but worth noting that vid-segment introduces `frameworks_used:` as a meta.md array which vid-intro's set didn't include.
  - Segment list source: vid-segment relies on reference-block.md to define segment job. If reference-block.md does not contain a parseable segment list (because vid-framing/vid-structure didn't write one), vid-segment falls back to creator confirmation: "Segment job: {one-line restatement}." This works as a degraded mode but means vid-pipeline cannot loop vid-segment without human input in the loop.

### Stage 8, vid-ending → script.md ## Ending

- BUILT: YES.
- Input expected: creator-foundation.md, voice-profile.md and reference-pieces, vault-integration.md, voice-rhythm.md, voice-pressure-test.md, format-planners/{format}.md, transition-bank.md Sections 3 + 4, skill-local references (pivot-gap-bridge-shapes.md, cta-placement-by-format.md, ending-anti-patterns.md, end-screen-design.md), `meta.md`, `script.md` (with `## Intro` section as standalone-mode source for callback rules), `reference-block.md` if exists. Sub-skill mode also reads `intro_packet`.
- Output produced: writes filled `## Ending` template into `script.md`. Updates `meta.md` with `ending_locked: true`, `next_video: "[[slug]]"`, `cta_shape:`, `ending_be_pattern:`, `last_refreshed:`. Sub-skill mode returns `ending_packet`.
- Downstream consumers: vid-pressure-test (reads full script), vid-measurement post-publish (logs winning Bridge patterns).
- Hand-off coherence: STRONG inbound, unverified outbound.
  - Inbound: The callback rules in vid-ending Phase 1 step 14 explicitly read intro_packet fields by name (setup.text, hook.type, etc.). This is the closest contract pairing in the system.
  - Outbound: vid-pressure-test does not exist yet, so we cannot verify whether `ending_packet` and the meta.md ending fields meet its needs.
- Notes:
  - The `next_video_status: real-published | next-stack-placeholder | none` field is a smart graceful-degradation pattern. It tracks the case where a Bridge points to a piece that isn't yet published. vid-pipeline could later use this to retro-link.

### Stage 9, vid-pressure-test → pressure-test.md

- BUILT: NO.
- Build-plan name: "Focused adversarial review agents: source alignment, creator voice, AI-slop, retention logic, proof/claim traceability. Each returns top 3 issues only" (Section 4 line 448).
- Expected inputs (inferred):
  - `script.md` fully assembled (intro + N segments + ending).
  - `meta.md` with all the locked flags and arrays (`stories_used`, `proofs_used`, `metaphors_used`, `frameworks_used`, `visual_proofs_called_out`, `voice_pressure_test`, `intro_locked`, `ending_locked`, `next_video`, `cta_shape`).
  - `reference-block.md` with locked angle / core payoff (for source-alignment review).
  - `brain-dump.md` (for retention logic review against the original raw material).
  - `voice-profile.md` plus reference-pieces (for AI-slop and creator-voice review).
- Output: `Content/pieces/{slug}/pressure-test.md` with the multi-agent findings. Top 3 issues per agent.
- Contract Phase 4 must honor:
  1. The `visual_proofs_called_out:` array is the auditable trail for proof/claim traceability. vid-pressure-test should walk this array and verify each `bank_link:` resolves OR is flagged as "claim made, no proof captured."
  2. The `voice_pressure_test:` block in meta.md is the result of inline voice checks done by vid-intro and vid-segment. vid-pressure-test does the FULL-SCRIPT adversarial pass on top.
  3. Should NOT auto-fix. Per build-plan principles, surface issues; creator decides.
- Hand-off coherence: BLOCKED until built. The data is mostly there, the analysis isn't.

### Stage 10, save and lock

- BUILT: NO at the orchestrator level (vid-pipeline is unbuilt). Save discipline IS implemented inside each writing skill.
- vid-pipeline orchestrator's job (when built):
  - Verify all expected artifacts exist in `Content/pieces/{slug}/`: `meta.md`, `brain-dump.md`, `reference-block.md`, `script.md`, `thumbnail-brief.md`, `pressure-test.md`.
  - Verify meta.md has `intro_locked: true` and `ending_locked: true`.
  - Set meta.md `status:` to `filming-ready`.
  - Surface the visibility report (failures, orphan wikilinks, missing People stubs) per the vault-integration "visibility rule."
- Hand-off coherence: BLOCKED until vid-pipeline is built. The state machine (`status: ideating | drafting | filming-ready | filmed | editing | published`) is in vault-integration.md schema, but no skill currently advances it past whatever the writing skills set on save.

## Cross-stage seams

### Seam #1, BLOCKING: vid-intro requires thumbnail-brief.md, but build-plan Section 5 lets vid-thumbnail be deferred

vid-intro Phase 1 hard prerequisite: `Content/pieces/{slug}/thumbnail-brief.md` exists with locked picks. The Top 3 viewer questions are derived from "title plus thumbnail brief together" per intro-architecture.md Step 1.

Build-plan Section 5 "How the orchestrator delegates" lists vid-thumbnail as: "Gets thumbnail text decision (might invoke vid-thumbnail here or defer to a separate run)." Step 4 says "INVOKES vid-title -> returns locked title" and Step 5 says "INVOKES vid-intro -> returns hook drawing from the brain dump." If vid-thumbnail is deferred, vid-intro hard-stops in Step 5.

Resolution paths for Phase 4:
- (a) Make vid-thumbnail mandatory before vid-intro in vid-structure / vid-pipeline. Update build-plan Section 5 to reflect this. Cleanest.
- (b) Soften vid-intro's prerequisite to "if thumbnail-brief.md exists, use it; otherwise derive Top 3 viewer questions from title + brain-dump alone" and accept the quality tradeoff.
- (c) Have vid-structure / vid-pipeline invoke vid-thumbnail in sub-skill mode mid-flow before invoking vid-intro.

Recommendation: (a) or (c). The intro-architecture.md Step 1 method depends on thumbnail signal. Removing it weakens the question derivation.

### Seam #2, MINOR: meta.md array fields are not declared once in a canonical schema

The piece meta.md schema in vault-integration.md declares `stories_used:`, `metaphors_used:`, `proofs_used:`. vid-intro adds `testimonials_used:` (implied in stories_used/proofs_used/testimonials_used at Phase 5). vid-segment adds `frameworks_used:`. vid-ending adds `next_video:`, `cta_shape:`, `ending_be_pattern:`, `ending_locked:`. vid-intro adds `intro_locked:`, `intro_strategy:`, `intro_hook_type:`, `intro_credibility_form:`, `voice_pressure_test:`, `visual_proofs_called_out:`.

None of these extensions are declared in vault-integration.md's per-video pieces frontmatter schema (which currently shows only `stories_used`, `metaphors_used`, `proofs_used`). This is fine in practice because YAML is open-shape, but a Phase 4 builder reading vault-integration.md alone would not know the canonical list. Recommend updating vault-integration.md to declare the full meta.md schema once, with each field's source skill annotated.

### Seam #3, MINOR: voice_pressure_test: block is written by both vid-intro and vid-segment

Both skills write `voice_pressure_test:` to meta.md as an object (date, result, layer1_pass, layer2_context, layer2_pass, flags, read_aloud_confirmed). If vid-segment runs after vid-intro, the second write overwrites the first. The result is meta.md only reflects the LAST voice check, not the full intro+segments+ending result.

Resolution: convert `voice_pressure_test:` to an array of objects, one per skill invocation. Or scope it to a sub-key (`voice_pressure_test.intro:`, `voice_pressure_test.segments: []`, `voice_pressure_test.ending:`). vid-pressure-test will likely consume this block, so the shape needs to be decided before that skill is built.

### Seam #4, MINOR: meta.md ownership at piece creation is unclear

vid-title's prerequisite is "`Content/pieces/{slug}/` exists with at minimum meta.md OR a brain-dump / framing artifact." vid-thumbnail's prerequisite is "the video slug argument, or an existing meta.md with a locked title." vid-intro and vid-segment hard-require meta.md with `format:` and `goal:` set.

Logical owner: vid-intake or vid-framing (since vid-framing picks format and goal). Build-plan does not explicitly say which skill creates meta.md and seeds the initial frontmatter. vid-foundation creates folder structure but not per-piece meta.md (it runs once per creator, not per video).

Resolution: assign meta.md creation to vid-intake (when the piece slug is first created) and meta.md frontmatter population (`format:`, `goal:`, `pillar:`) to vid-framing. Document this in build-plan Section 5.

### Seam #5, MINOR: segment list shape is undefined

vid-segment relies on reference-block.md to contain the segment's job ("step 1 of 5, point 3 of 7, the case-study story beat"). vid-structure is supposed to do "keep/cut/combine review, Type 1 skeleton assembly" which presumably produces the segment list. But:
- Is the segment list in reference-block.md (vid-framing's output) or in script.md skeleton (vid-structure's output)?
- What's the shape? Bullet list? YAML array in frontmatter? Headings in script.md awaiting prose?

vid-segment Phase 1 frames the segment with creator confirmation, which works as a degraded mode. But for vid-pipeline to loop vid-segment N times unattended, the segment list must be machine-readable.

Resolution: Phase 4 vid-structure spec should declare the segment list shape. Recommend: `segments:` array in meta.md with each entry having `label`, `purpose`, `position` (1-of-N). vid-segment iterates this array. vid-pipeline's loop reads its length.

### Seam #6, MINOR: vid-ending standalone mode reads ## Intro section in script.md

In standalone mode, vid-ending reads the `## Intro` section from script.md to lift the Setup contract, hook lane, and Top-3 problem anchor. This requires script.md to have a parseable `## Intro` heading with the specific structure vid-intro produces.

If vid-intro's save format ever changes (e.g., adds a `## Intro Hook` sub-heading), vid-ending's standalone parsing breaks silently. Sub-skill mode is safe (reads structured intro_packet).

Resolution: leave as-is for now. Document the implicit contract: vid-intro writes `## Intro` as a single block, vid-ending parses it. If the format ever evolves, audit both at the same time.

## Bidirectional contract check

The "update both sides" rule from vault-integration.md states: when a writing skill uses a bank entry, the piece's meta.md gets the wikilink in `stories_used`/`metaphors_used`/`proofs_used` AND the bank entry's `used_in:` array gets the piece slug AND `status:` flips from `captured` to `used`.

Honored at:
- vid-intro Phase 5: "If a story, proof, or testimonial got woven in, update both sides of the wikilink graph per knowledge/vault-integration.md: piece's stories_used/proofs_used/testimonials_used AND the bank entry's used_in and status. Both sides. Always." Explicit.
- vid-segment Phase 4: "Update each bank entry's used_in. Per the vault-integration 'update both sides' rule. For every bank entry pulled in Phase 2 and surviving Phase 3, open the entry, append [[piece-slug]] to its used_in array, and flip status from captured to used if it was still captured." Explicit.

Misses:
- vid-ending: handles bank pulls in conditional loads (story-pulling-criteria, proof-placement-rules, metaphor-integration, testimonial implied) but its Phase 4 save section does not explicitly enumerate the both-sides update for any banks the close happens to use. It DOES handle the next-video wikilink validation ("If the next-video wikilink target doesn't exist, do NOT save a broken link"). But banks pulled into the recap or Gap are not covered by an explicit both-sides-update step.
  - Risk: low because endings are claim-light (vid-ending says "endings are claim-light by design, so most runs skip these"). Real risk only when a roast close pulls a story or a case-study close pulls a testimonial.
  - Recommendation: add an explicit "if any bank entries were pulled, update both sides per vault-integration.md" step in vid-ending Phase 4. Single sentence. Closes the gap.
- vid-thumbnail: does not pull from story/proof/metaphor banks (it pulls from packaging-bank only, and packaging-bank has no `used_in:` field per current schema). No miss.
- vid-title: does not pull from story/proof/metaphor banks. No miss.

People stub creation rule (vault-integration.md plus CLAUDE.md rule 20):
- vid-segment Phase 4 explicitly handles: "People stub missing for a client mentioned in a pulled bank entry: create the stub immediately per CLAUDE.md rule 20." Honored.
- vid-intro's bank pulls also could mention clients (story-bank, testimonial-bank). vid-intro Phase 5 does not explicitly call out the People-stub creation step. The `vault-integration.md` load is referenced, which contains the rule, so it's covered by inheritance. But an explicit reminder would match vid-segment's discipline.

## Recommended Phase 4 priorities (build order)

The end-to-end pipeline is currently blocked at the upstream end. vid-intro / vid-segment / vid-ending work, but they cannot run because brain-dump.md, reference-block.md, and the seeded meta.md don't exist yet for any new piece.

1. **vid-intake first.** Smallest scope, no upstream dependencies, creates the piece folder + initial meta.md + brain-dump.md. Without this, no other Phase 3 skill has anything to read. Highest-leverage first build.

2. **vid-framing second.** Reads brain-dump.md, picks format/goal, produces reference-block.md, and crucially POPULATES meta.md `format:`, `goal:`, `pillar:`. After this, vid-title, vid-thumbnail, vid-intro, vid-segment, vid-ending all have what they need.

3. **End-to-end smoke test (manual orchestration).** Build vid-intake and vid-framing, then manually run the chain: vid-intake -> vid-framing -> vid-title -> vid-thumbnail -> vid-intro -> vid-segment x N -> vid-ending. This is the "if the creator wants to test the existing skills end-to-end before vid-intro is built" path from build-plan Section 6 Step 4, but with the upstream skills now built. This will surface any contract drift NOT visible from reading SKILL.md files alone. Time it. Read script aloud. Per build-plan Section 6 Step 5.

4. **vid-structure third.** Once steps 1-3 work manually, vid-structure formalizes the keep/cut/combine review and produces the machine-readable segment list (resolves Seam #5). Decides the meta.md ownership question (resolves Seam #4 if not already resolved by vid-framing). Picks the resolution for Seam #1 (thumbnail ordering).

5. **vid-pressure-test fourth.** Now there are full scripts to test against. The multi-agent design needs the actual artifacts to validate.

6. **vid-pipeline last.** Per build-plan principle: "build leaves first, orchestrator last." Once steps 1-5 work in manual mode, vid-pipeline wraps them in adaptive routing.

Before step 1, do these housekeeping fixes (low effort, high value):
- Resolve Seam #1 explicitly in build-plan Section 5 (thumbnail ordering before intro).
- Resolve Seam #3 (voice_pressure_test schema as array or scoped object).
- Add the explicit both-sides-update step to vid-ending Phase 4 (closes Seam #6 gap).
- Update vault-integration.md piece schema with the full meta.md field list (closes Seam #2).
- Decide meta.md ownership (vid-intake creates, vid-framing populates) and document in build-plan Section 5 (closes Seam #4).

These fixes are spec-only edits, no skill code changes. Doing them before Phase 4 means vid-intake / vid-framing are built against a closed contract.

## Confidence

What I traced:
- Full read of all 8 BUILT SKILL.md files plus knowledge/vault-integration.md.
- build-plan.md Sections 4 (skills inventory), 5 (data flow), 6 (build sequence), 7 (where things live), 9 (verification).
- Spot-checks of intro-architecture.md to confirm the title+thumbnail-derived Top 3 viewer questions method.

What I could not trace:
- vid-intake, vid-framing, vid-structure, vid-pressure-test, vid-pipeline have no SKILL.md yet. The contracts they need to honor are inferred from downstream consumers, which is the right method but depends on those consumers being internally consistent. (They are, with the seams listed above.)
- I did not load the format-planners/{format}.md files individually. Each format planner shapes the segment shape, the close shape, and the hook lane. There may be format-specific contract requirements I missed (e.g., interview format may need a `guest:` field in meta.md). For Phase 4 builders: spot-check format planners against meta.md schema to confirm no per-format fields are expected by vid-segment / vid-ending without a write step somewhere.
- I did not load skill-local references (skills/vid-segment/references/setup-tension-payoff-shapes.md, etc.). These are runtime decision aids, not contract documents, so they should not affect the integration trace. But if a runtime reference encodes an implicit contract (e.g., framework-shapes.md tells vid-segment to expect `framework_type:` from framework-bank entries), I would have missed it.
- I did not test in a live environment. The trace is paper-only against documented contracts. A real run on the hypothetical Peak Systems video would surface drift the SKILL.md files don't reveal.

Verdict re-stated for clarity: the BUILT 5-skill writing chain (title, thumbnail, intro, segment, ending) is internally coherent on the happy path with two flagged blocking-or-near-blocking issues (Seam #1 thumbnail ordering, Seam #3 voice_pressure_test overwrite). The bigger risk is that vid-intake / vid-framing / vid-structure get built without the upstream contract being closed first. The recommended fixes are mostly spec edits that should land before Phase 4 implementation begins.
