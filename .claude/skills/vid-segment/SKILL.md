---
name: vid-segment
description: Write one body segment of a YouTube script, filming-ready, in the creator's voice, from the locked outline in script.md. Bingeworthy craft, tension held with setups and payoffs, show before tell, format-aware shape, real material from the brain dump and banks. Standalone OR invoked by vid-pipeline once per body segment in the script phase. Triggers on "write segment", "draft point", "build the next point", "write point [N]", "expand step [N]", "next body segment", or when an orchestrator asks for one segment of script body.
---

# Video Segment Writer

Co-write ONE body segment of a bingeworthy script in the creator's voice. One point, made so well the viewer feels smart and stays. The craft rides on tension: a segment is a chain of setups and payoffs wearing a lesson.

**Scope: one segment at a time.** Intro, ending, title, thumbnail, and the outline are other skills. For a multi-segment body, this skill runs once per segment.

**This is a conversation, not a document.** Short messages. References are for your thinking; never paste them at the creator.

## What loads, and when

| Step | Load | For |
|---|---|---|
| 1 | `content/pieces/{slug}/piece.md` | format, goal, voice_context, locked title, prior `*_used` arrays |
| 1 | `content/pieces/{slug}/script.md` | this segment's skeleton section (its job, the picked parable and principle, any `> [!todo]` notes left for it), the prior segment's closing line, the `## To build` list |
| 1 | `content/pieces/{slug}/brain-dump.md` | the creator's actual words behind this point |
| 1 | `knowledge/format-planners/{format}.md` | this segment's shape |
| 1 | the bank entries the skeleton picked, full text | the material the prose is written from |
| 2, only when repair fires | `knowledge/parable-decision-matrix.md`, then ONE bank folder + its filter file (`story-bank/` → `knowledge/story-pulling-criteria.md`; `proof-bank/` and `testimonial-bank/` → `knowledge/proof-placement-rules.md`; `metaphor-bank/` → `knowledge/metaphor-integration.md`; `framework-bank/` → `knowledge/framework-builder.md`, also the 5-step build) | re-pick or fill an open slot |
| 2, conditional | `knowledge/visual-demo-builder.md` | build out a visual demo |
| 3 | `foundation/voice-profile.md` + `foundation/reference-pieces/{voice_context}.md` | the guardrail and the voice engine (see fallback below) |
| 3 | `references/parable-principle-shapes.md` | worked segments to calibrate against |
| 3 | `knowledge/transition-patterns.md` | Section 2 handoff patterns; Section 4 banned phrases |
| 4 | `knowledge/voice-rhythm.md` + `knowledge/voice-pressure-test.md` | edit-pass lenses |
| 4, conditional | `knowledge/visual-proof-callouts.md` | claims the editor must put on screen |
| 5-6 | nothing | the gate and the save need nothing new; the save contract is embedded in Step 6 |

## Prerequisites

- `content/pieces/{slug}/piece.md` with `format` and `goal`, plus `brain-dump.md`. Both missing → hard stop, route to `vid-intake` / `vid-framing`.
- `content/pieces/{slug}/script.md` skeleton from `vid-structure`, with this segment's section and its blocks picked. No skeleton → run `vid-structure` first.
- `foundation/voice-profile.md` + `foundation/reference-pieces/`: load if present. If missing, anchor voice entirely in the brain dump's verbatim phrasing plus the universal hard rules (no em-dashes, no AI-isms, no hedging), note "Run `vid-voice-capture` for sharper voice fit," and continue. Voice is never a blocker.

**Invoked by the pipeline:** prerequisites are verified and the caller names the segment; skip re-checking and skip questions the caller already answered. Never skip the creator gate. Saves are identical in both modes.

## Step 1: Read the plan, verify the materials

A writer doesn't start drafting with research missing. Read this segment's skeleton section (its job, its picked parable and principle, its tension role, any `> [!todo]` notes earlier sessions left under its heading), the prior segment's closing line (the handoff this segment inherits), and the format planner's shape for this format. Then pull the actual material: the full text of every bank entry the skeleton picked, and the brain dump lines behind this point.

Verify every slot has real material behind it: entries readable and specific enough to write from, `## To build` rows for this segment visible. Then orient the creator in one line, no ceremony: "Segment 3 of 5: [job]. Plan is [story] into [framework]. Writing it now."

## Step 2: Repair what verification flagged

Usually skipped. Fires on exactly three triggers: a `## To build` row names something missing for this segment; a picked entry is absent or too thin to write from; or the creator wants to change the plan.

Repairs, creator deciding: route to `vid-capture` mid-flow (it returns the new wikilink and this skill continues); build inline (the framework 5-step per `framework-builder.md`, saved via vid-capture Stage F; the visual demo build-out per `visual-demo-builder.md`); re-pick via the decision matrix plus ONE bank query, max 3 candidates surfaced with a one-line why each; or consciously cut the slot. Never invent material to fill a hole.

## Step 3: Draft fast, for tension

Fill the plan top to bottom in one pass, no editing, no polishing. The shape comes from the format planner: a listicle point runs the full parable-principle cycle; a short-process or deep-dive step states the step and teaches it, earning a parable only where the step is complex or doubted; a case study is one arc. Some points are one line and move on. Spend the creativity where the point needs belief, and take the first demo or metaphor idea that fits instead of grinding for clever.

The tension discipline, the spine of the draft:

- Open on the inherited setup; the viewer arrives mid-curiosity, keep them there.
- Show, then tell. Never name the lesson and then explain it; the explanation is what kills the "get to the point" viewer. Set it up, play it out, land it.
- The instant anything pays off, set up the next thing. An early payoff is fine IF it instantly re-hooks; a payoff followed by more explaining is the sin.
  - Dead: "Step three is to batch your filming days. See, when you batch, what happens is you save time because..."
  - Alive: "Step three put four working days a month back into my calendar, and it's the one everyone skips." [the story plays out] "So: batch your filming days. Which creates a new problem, because batching only works if..."
- Proof drops after the lesson lands, answering the "has this actually worked?" the viewer is silently asking.
- Close on the takeaway punch, then the handoff: signal the shift and promise the next point's result. "Here's step 4" is dead; "step 4 is the one that got me consistent leads" lives.

Voice anchors while drafting, in order: brain dump phrasing wins (the creator's words ARE the voice, don't polish them into "better" prose); reference pieces set the cadence (write fresh in that grain, never echo a passage); the guardrail rejects. Every specific stays verbatim; if the bank says "$8,400 to $74,000", the prose does not say "$10K to $100K".

Mid-draft ideas for OTHER segments don't break flow: drop a `> [!todo]` callout under that segment's heading in script.md and keep writing. Visual demos put the spoken layer in prose and the shown layer in a `> [!note] visual:` callout.

## Step 4: Edit out loud

A separate pass, after the draft is done, never during. Walk the draft as spoken word and answer twelve questions, yes or no, silently. Any no gets fixed before the creator sees a word:

1. Does every line serve exactly ONE point?
2. Does the opening connect to what the previous transition promised, no cold restart?
3. Does a new setup land within a line or two of every payoff? Walk it: list every setup, confirm its payoff; find every payoff, confirm its re-hook.
4. Is everything set up here paid off here, or explicitly handed to a later segment?
5. Does it show before telling where belief is needed, and stop the moment the point has landed? Anything still explaining after it's clear gets cut.
6. Does every number, name, and story beat trace verbatim to the brain dump or a bank entry?
7. Does proof land after the lesson it backs?
8. Is the takeaway one sentence the viewer could repeat to a friend?
9. Does the closing transition signal the shift AND promise a result the viewer cares about?
10. Read aloud, is it the creator talking to one person: their phrasing, varied sentence lengths (`voice-rhythm.md` is the lens), words a 10 year old follows?
11. Could any line be deleted without losing meaning? Then delete it.
12. Could the avatar say "heard this exact thing before"? Then the angle, demo, or story isn't specific enough to this creator's material.

Then the mechanical tail: claims get their `> [!important] Visual proof needed` callouts, and the guardrail scan (`voice-pressure-test.md` Pass 1) runs before anything is shown.

A no that traces to the plan (wrong parable, two points fused into one segment) is a structure problem: fix the structure, don't sand the prose.

## Step 5: The creator gate

Present the segment as clean spoken prose with its callouts in place. The creator reads it aloud: anything they'd reword loops back in. A reword that sounds like a permanent rule ("never use X", "I'd never say that") goes through `vid-voice-update` first; one-time edits just get applied. Nothing saves without approval.

## Step 6: Save and update the graph

On approval, always, both modes:

- **Append** the locked prose to script.md under the segment's heading. Preserve all prior sections. One exception: if this segment's opening made the prior segment's closing transition land wrong, adjust that one inherited line and tell the creator. Delete any `> [!todo]` callout this segment consumed and its cleared `## To build` row.
- Update piece.md frontmatter: append the pulled `[[wikilinks]]` to whichever of `stories_used` / `proofs_used` / `metaphors_used` / `testimonials_used` / `frameworks_used` apply; append this segment's label to `segments_completed`; bump `last_updated`. Append only; never touch another skill's fields.
- Update every pulled bank entry, both sides of the link: `used_in` gets `[[{piece-slug}]]`, `status` flips `captured` → `used`.
- Surface in chat: what saved, and any `bank_link: null` proof callouts so the creator can capture the proof before filming or rephrase.

The next segment starts only when the creator says go.
