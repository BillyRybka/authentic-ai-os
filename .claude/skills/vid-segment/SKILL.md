---
name: vid-segment
description: Build one body segment of a video script as a parable then a principle then a transition (show, then tell, then hand off to the next point). Format-aware, bank-pulling (story, proof, metaphor, testimonial, framework), two-pass review (structure first, then prose). Standalone OR invoked by vid-pipeline once per body segment in the script phase. Triggers on "write segment", "draft point", "build the next point", "write point [N]", "expand step [N]", "next body segment", or when an orchestrator asks for one segment of script body.
---

# Video Segment Writer

Build ONE body segment in the creator's voice, pulling from the evergreen banks. The full shape is a parable (the show), then a principle (the tell), then a transition (the handoff), but the format decides how much of that shape each segment uses. Two passes, and the order is the core rule: **lock the structure first, then write the prose.** Structure dictates voice, never the other way around.

**Scope: one segment at a time.** Intro, ending, title, thumbnail, and the full skeleton are other skills. For a multi-segment body, this skill runs once per segment.

**This is a conversation, not a document.** Short messages. References are for your thinking; never paste them at the creator.

## What loads, and when

Load each file at the phase that needs it. Do not front-load.

| Phase | Load | For |
|---|---|---|
| 1 | `content/pieces/{slug}/piece.md` | format, goal, voice_context, locked title, prior `*_used` arrays |
| 1 | `content/pieces/{slug}/script.md` | this segment's skeleton section (its job, anchors, tension role), the prior segment's closing line (the handoff this segment inherits), the `## Blocks to capture` list |
| 1 | `content/pieces/{slug}/brain-dump.md` | the raw material and the creator's actual words |
| 1 | `content/pieces/{slug}/async-block-notes.md` IF it exists | notes tagged to this segment from earlier writing sessions |
| 1 | `knowledge/format-planners/{format}.md` | how THIS format weights the bricks (full parable+principle, lean principle-only steps, or case-study one-arc) |
| 2 | `references/parable-principle-shapes.md` | the structural shapes for the two bricks |
| 2 | `knowledge/parable-decision-matrix.md` | picking the parable type (visual demo / story / metaphor) |
| 2, on demand | ONE bank folder at a time as the segment queries it, plus that bank's filter file: `story-bank/` → `knowledge/story-pulling-criteria.md`; `proof-bank/` and `testimonial-bank/` → `knowledge/proof-placement-rules.md`; `metaphor-bank/` → `knowledge/metaphor-integration.md`; `framework-bank/` → `knowledge/framework-builder.md` (also the 5-step build when the bank has no match) | candidates for the block types this segment actually uses. Never load all the banks up front |
| 2, conditional | `knowledge/visual-demo-builder.md` | only when the parable is a Visual Demo (inline 3-step brainstorm; there is no visual-demo bank) |
| 2 | `banks/transition-bank.md` | Section 2 patterns for the structure draft's handoff; Section 4 banned phrases re-checked at prose time |
| 3 | `foundation/voice-profile.md` + `foundation/reference-pieces/{voice_context}.md` | the guardrail and the voice engine (see fallback below) |
| 3 | `knowledge/voice-rhythm.md` + `knowledge/voice-pressure-test.md` | the by-ear rhythm lens and the pre-save voice check |
| 3, conditional | `knowledge/visual-proof-callouts.md` | only when the principle carries a claim the editor must put on screen |
| 4 | nothing | the save contract is embedded in Phase 4; the vault rules live in the workspace CLAUDE.md |

## Prerequisites

- `content/pieces/{slug}/piece.md` with `format` and `goal`, plus `brain-dump.md` (the material). Both missing → hard stop, route to `vid-intake` / `vid-framing`.
- `content/pieces/{slug}/script.md` skeleton from `vid-structure` (this segment's section exists). No skeleton → run `vid-structure` first.
- `foundation/voice-profile.md` + `foundation/reference-pieces/`: load if present. If missing, anchor voice entirely in the brain dump's verbatim phrasing plus the universal hard rules (no em-dashes, no AI-isms, no hedging), note "Run `vid-voice-capture` for sharper voice fit," and continue. Voice is never a blocker.

**Invoked by the pipeline:** prerequisites are verified and the caller names the segment; skip re-checking and skip questions the caller already answered. Never skip the creator locks (structure lock, read-aloud). Saves are identical in both modes.

## Phase 1: Frame the segment

Read this segment's skeleton section in script.md: its job ("step 2 of 5", "the case-study Action beat"), its material anchors and block candidates, and its tension role (whether it carries the title-promise payoff or opens/closes a thread; vid-structure already decided, read it, don't re-derive). Check async-block-notes for anything tagged to this segment.

Confirm the frame with the creator in one short message: the segment's job, the format, this segment's payoff. **Wait, lock it.** If the format planner's shape conflicts with what the creator confirms, surface the conflict; don't silently override either.

## Phase 2: Structure pass

**Shape before slots.** The format planner already decided this segment's shape; honor it. A listicle point runs the full parable-principle cycle. A short-process or deep-dive step defaults to NO parable: state the step, teach it, move on. A parable enters a lean step only when that step is complex or the viewer would be skeptical it matters; then it earns its place, otherwise it's drag. Case study is one arc across the whole body, not per-segment cycles. The first question is never "which parable?", it's "does this segment need one at all?"

The segment must work AS A UNIT before any prose exists. A structure draft is bullets and slot fills:

1. **Parable (the show), when the shape calls for one.** The emotional open: visual demo, story, or metaphor, picked via the decision matrix, anchored in the brain dump's material.
2. **Principle (the tell).** The actionable lesson: the framework and its components, proof placed AFTER the framework lands, one sharp takeaway line.
3. **Transition (the handoff).** Signals the shift AND promises a result the viewer cares about: "here's step 4" is dead, "step 4 is the one that got me consistent leads" lives. Patterns in transition-bank Section 2, or the body-to-ending bridge if this is the last segment.

**Bank pulling** (this skill's differentiator). Query only the banks this segment's block types need, by their match keys (story `illustrates`, proof `proof_type` + what it proves, metaphor `concept`, framework name, testimonial claim-match). Surface 0-3 candidates per type, each as: slug + one line + WHY it matches this segment's job. More than 3 is choice paralysis. Testimonials are seasoning inside a segment, never its spine.

**When the banks come up empty, do not invent.** Three paths:
1. Route to `vid-capture` mid-flow (it returns the new wikilink and this skill continues). For a missing framework: walk the 5-step build inline per `framework-builder.md`, then save through vid-capture Stage F.
2. Tell the creator the bank is empty for this slot; swap block type or pause to capture.
3. Visual Demo has no bank: always brainstorm inline per `visual-demo-builder.md` (name the point, pick the sub-type, 2-3 candidates, creator picks).

**Clear the gap manifest.** If `## Blocks to capture` has a row tagged to this segment, it names exactly what to capture. Capture it or consciously cut it, then delete the row and replace the skeleton's placeholder with the real `[[wikilink]]`.

**Mid-write ideas for OTHER segments** don't break flow: jot one line into `async-block-notes.md` (`- [Segment M, block type]: idea`) and keep going.

**The segment test.** Before surfacing the draft, run three silent pass/fail checks on the plan, judged through the avatar's eyes. NEW: would they say "heard it before"? EASY: is this the vital 20% that gets 80% of the result, with nothing that makes their brain strain? INSPIRING: does it make them want to act, not just understand? The target feeling is the viewer coming away feeling smart: "that was easy, this person's a genius, I'm coming back." A fail is a structure problem; fix it here, not in prose.

Surface the structure draft as a compact block (segment label, parable pick + bank candidates, principle + framework/proof candidates, transition pattern) and ask: lock it, swap a block, pull a different candidate, sharpen the payoff, or scrap. **Loop until the structure locks. No prose before lock.**

## Phase 3: Prose pass

Write the locked structure in the creator's voice. Three anchors, in order:

1. **Brain dump phrasing wins.** If the creator's actual words exist for this idea, use them. Don't polish into "better" prose; the brain dump IS the voice.
2. **Reference pieces are the seed.** Read the `## ` sections together to internalize cadence (sentence variation, paragraph shape, opener move; `voice-rhythm.md` is the lens). Write fresh prose in that grain; never echo a passage's words. Voice only, not structure: if a passage's arc conflicts with the locked structure, the structure wins.
3. **Guardrail constrains.** Anti-patterns and creator hard rules are hard rejects (rewrite); words-avoided get the paired swap; a signature phrase appearing once in long-form is healthy, but never pad to hit it.

Per block: the parable opens the segment, verbatim brain-dump lines where possible, short (1-3 sentences in tight formats, 3-6 in listicle/deep-dive); metaphors drop clean with no "let me give you an analogy" announcement; visual demos put the spoken layer in prose and the shown layer in a `> [!note] visual:` callout. The principle names the framework, walks the components, then drops the proof. Any CLAIM (number, named outcome, before/after) gets a `> [!important] Visual proof needed` callout immediately after its line, per `visual-proof-callouts.md`. Close with the one-sentence takeaway (short punch after a longer line), then the transition, checked against Section 4 banned phrases.

**Anti-fabrication.** Every number, name, claim, story moment, or specific phrasing traces to the brain dump, piece.md, or a bank entry pulled in Phase 2. If the bank says "$8,400 to $74,000", the prose does not say "$10K to $100K".

**Voice check before showing:** run voice-pressure-test Pass 1 silently (guardrail), then surface the draft as clean prose (parable, principle, takeaway, transition; callouts where they belong) and ask the creator to read it aloud: anything they'd reword? Loop until confirmed. A reword that sounds like a permanent rule ("never use X", "I'd never say that") goes through `vid-voice-update` first (permanence gate, not a logger); one-time edits just get applied.

## Phase 4: Save and update banks

Always, both modes:

- **Append** the locked prose to `content/pieces/{slug}/script.md` under the segment's heading. Preserve all prior sections; never overwrite. One exception: if this segment's opening made the prior segment's closing transition land wrong, adjust that one inherited line and tell the creator.
- Update piece.md frontmatter: append the pulled `[[wikilinks]]` to whichever of `stories_used` / `proofs_used` / `metaphors_used` / `testimonials_used` / `frameworks_used` apply; append this segment's label to `segments_completed` (the pipeline's body-progress counter); bump `last_updated` to today. Append only; never touch another skill's fields.
- Update every pulled bank entry, both sides of the link: its `used_in` gets `[[{piece-slug}]]`, its `status` flips `captured` → `used`.
- Surface in chat: the voice-check result (real, not scripted) and any `bank_link: null` visual-proof callouts so the creator can capture the proof before filming or rephrase.

**STOP.** Do not write the next segment. The creator or the orchestrator re-invokes per segment.
