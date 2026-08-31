---
name: vid-segment
description: Write one body segment of a YouTube script, filming-ready, in the creator's voice, from the locked outline in script.md. Standalone OR invoked by vid-pipeline once per body segment in the script phase. Triggers on "write segment", "draft point", "build the next point", "write point [N]", "expand step [N]", "next body segment", or when an orchestrator asks for one segment of script body.
---

# Video Segment Writer

Co-write ONE body segment of a bingeworthy script in the creator's voice. One point, made so well the viewer feels smart and stays. The craft rides on tension: a segment is a chain of setups and payoffs wearing a lesson. Scope is one segment at a time: intro, ending, title, thumbnail, and the outline are other skills, and a multi-segment body runs this skill once per segment.

**This is a conversation, not a document.** Short messages. References are for your thinking; never paste them at the creator. **Read as you go:** no up-front load list; each step names its own reads and nothing loads before the step that needs it.

## Prerequisites

- `content/pieces/{slug}/piece.md` with `format` and `goal`, plus `brain-dump.md`. Both missing → hard stop, route to `vid-braindump` / `vid-framing`.
- `content/pieces/{slug}/script.md` skeleton from `vid-structure`, with this segment's section and its blocks picked. No skeleton → run `vid-structure` first.
- `foundation/voice-profile.md` + `foundation/reference-pieces/`: load if present. If missing, anchor voice in the brain dump's verbatim phrasing plus the universal hard rules (no em-dashes, no AI-isms, no hedging), note "Run `vid-voice-capture` for sharper voice fit," and continue. Voice is never a blocker.

**Invoked by the pipeline:** prerequisites are verified and the caller names the segment; skip re-checking and skip questions the caller already answered. Never skip the creator gate. Saves are identical in both modes.

## Step 1: Read the plan, verify the materials

A writer doesn't start drafting with research missing. Read `piece.md` (format, goal, voice_context, tension_plan, prior `*_used` arrays), this segment's skeleton section in `script.md` (its job, the picked parable and principle, any `> [!todo]` notes), the prior segment's closing line (the handoff this segment inherits), `brain-dump.md` behind this point, `knowledge/format-planners/{format}.md` for the shape, and the full text of every bank entry the skeleton picked. For where this segment sits in the larger arc (is it the title-promise payoff? does it open or close a thread?), `knowledge/script-tension-architecture.md` is the lens. `knowledge/prose-craft.md` carries the seven moves every line is held to; load it before drafting, not as a filter after.

Verify every slot has real material behind it: entries readable and specific enough to write from, `## To build` rows for this segment visible. Then orient the creator in one line, no ceremony: "Segment 3 of 5: [job]. Plan is [story] into [framework]. Writing it now."

## Step 2: Repair what verification flagged

Usually skipped. Fires on exactly three triggers: a `## To build` row names something missing for this segment; a picked entry is absent or too thin to write from; or the creator wants to change the plan.

Repairs, creator deciding: route to `vid-bank` mid-flow (it returns the new wikilink and this skill continues); build inline (the framework 5-step per `knowledge/framework-builder.md`, saved via vid-bank Stage F; a visual demo per `references/visual-demo-builder.md`); re-pick via `knowledge/parable-decision-matrix.md` plus ONE bank query, max 3 candidates surfaced with a one-line why each; or consciously cut the slot. Never invent material to fill a hole.

## Step 3: Draft fast, for tension

Fill the plan top to bottom in one pass, no editing, no polishing. The shape comes from the format planner: a listicle point runs the full parable-principle cycle; a short-process or deep-dive step states the step and teaches it, earning a parable only where the step is complex or doubted; a case study is one arc. `references/parable-principle-shapes.md` holds the per-format worked segments to calibrate against. Some points are one line and move on. Spend the creativity where the point needs belief, and take the first demo or metaphor idea that fits instead of grinding for clever.

The seven tension disciplines, the spine of the draft:

**1. Open on the inherited setup.** The viewer arrives mid-curiosity; keep them there. No cold restarts.

**2. Show, then tell.** Never name the lesson and then explain it; the explanation is what kills the "get to the point" viewer. Set it up, play it out, land it.

- Dead: "Now we're going to talk about outbound. Outbound is important because it brings in calls. The first way is..."
- Alive: "The lever that took my client Steve from 4 calls a month to 4 calls a week." [the story plays out] "The framework is the Re-engagement Trigger. Here is how it works."

**3. Payoff, then re-hook instantly.** The instant anything pays off, set up the next thing. An early payoff is fine IF it instantly re-hooks; a payoff followed by more explaining is the sin.

- Dead: "Step three is to batch your filming days. See, when you batch, what happens is you save time because..."
- Alive: "Step three put four working days a month back into my calendar, and it is the one everyone skips." [the story plays out] "So: batch your filming days. Which creates a new problem, because batching only works if..."

**4. Calibrate the payoff to what the avatar already knows.** Read what the intro, the prior segments, and the avatar's world already taught them. If the answer is old news to this avatar, pay it off in one line and re-hook; do not build a cathedral around something they banked two minutes ago. If the answer is genuinely new to them, you may draw the payoff out, showing the evidence before you name it, so they feel the reveal.

**5. The curiosity-spiking payoff.** The strongest re-hook costs zero words: craft the payoff itself to open the next loop. Name something the viewer now wants explained. "The third thing they all do is something I call the two-word test." The viewer banked the answer AND carries a new question in the same line.

**6. The Minimum Viable Story.** Two or three sentences can be a complete belief-shifting story: drop into the worst moment, one action, the outcome. "My Airbnb was making a loss. I swapped the main photo for one that actually showed the space. Booked three times that week, never empty since." Do not skip the story slot because the bank has no epic, and do not inflate a small one into a saga it never was.

**7. Close on the takeaway punch, then the handoff.** Signal the shift and promise the next point's result.

- Dead: "Here's step 4."
- Alive: "Step 4 is the one that got me consistent leads."

Proof drops after the lesson lands, answering the "has this actually worked?" the viewer is silently asking. Handoff patterns: `knowledge/transition-patterns.md` Section 2, supplemented by the creator's own `banks/transition-bank.md` when it exists (missing bank is fine; it grows as the creator keeps transitions that worked). Section 4's banned phrases never appear.

Voice anchors while drafting, in order: brain dump phrasing wins (the creator's words ARE the voice, don't polish them into "better" prose); reference pieces set the cadence (write fresh in that grain, never echo a passage); the guardrail rejects. Every specific stays verbatim; if the bank says "$8,400 to $74,000", the prose does not say "$10K to $100K".

Mid-draft ideas for OTHER segments don't break flow: drop a `> [!todo]` callout under that segment's heading in script.md and keep writing. Visual demos put the spoken layer in prose and the shown layer in a `> [!note] visual:` callout. When a beat runs long or the energy sags mid-draft, the pacing, interrupt, and re-engagement moves live in `knowledge/attention-craft.md`.

## Step 4: Edit out loud

A separate pass, after the draft is done, never during. Walk the draft as spoken word and answer these questions, yes or no, silently. Any no gets fixed before the creator sees a word:

1. Does every line serve exactly ONE point?
2. Does the opening connect to what the previous transition promised, no cold restart?
3. Does a new setup land within a line or two of every payoff? Walk it: list every setup, confirm its payoff; find every payoff, confirm its re-hook.
4. Is everything set up here paid off here, or explicitly handed to a later segment?
5. Does it show before telling where belief is needed, and stop the moment the point has landed? Anything still explaining after it's clear gets cut.
6. The NEI filter. New: would the avatar call this fresh, or heard-it-before? Heard-it-before means the angle, demo, or story is not specific enough to this creator's material. Easy: could a tired viewer follow it on first listen, one idea per line? Inspiring: does the viewer leave believing they can do it, holding a receipt they can picture running themselves?
7. Does every number, name, and story beat trace verbatim to the brain dump or a bank entry?
8. Does proof land after the lesson it backs?
9. Is the takeaway one sentence the viewer could repeat to a friend?
10. Does the closing transition signal the shift AND promise a result the viewer cares about?
11. Read aloud, is it the creator talking to one person: their phrasing, varied sentence lengths (`knowledge/voice-rhythm.md` is the lens), words a 10 year old follows? Does any beat overstay its welcome (`knowledge/attention-craft.md` Section 1 is the ear test)?
12. Could any line be deleted without losing meaning? Then delete it.

Then the mechanical tail: claims get their `> [!important] Visual proof needed` callouts (`knowledge/visual-proof-callouts.md`), and the guardrail scan (`knowledge/voice-pressure-test.md` Pass 1) runs before anything is shown.

A no that traces to the plan (wrong parable, two points fused into one segment) is a structure problem: fix the structure, don't sand the prose.

## Step 5: The creator gate

Present the segment as clean spoken prose with its callouts in place. The creator reads it aloud: anything they'd reword loops back in. A reword that sounds like a permanent rule ("never use X", "I'd never say that") goes through `vid-voice-update` first; one-time edits just get applied. Nothing saves without approval.

## Step 6: Save and update the graph

On approval, always, both modes:

- **Append** the locked prose to script.md under the segment's heading. Preserve all prior sections. One exception: if this segment's opening made the prior segment's closing transition land wrong, adjust that one inherited line and tell the creator. Delete any `> [!todo]` callout this segment consumed and its cleared `## To build` row.
- Update piece.md frontmatter: append this segment's label to `segments_completed`, append the pulled `[[wikilinks]]` to the matching `*_used` arrays, bump `last_updated`. Append only; never touch another skill's fields.
- Update every pulled bank entry per the update-both-sides rule in `knowledge/bank-contract.md`: `status` flips to `used`, `used_in` gains `[[{piece-slug}]]`.
- Surface in chat: what saved, and any proof callouts with no bank link so the creator can capture the proof before filming or rephrase.

The next segment starts only when the creator says go.

Last-segment handoff: when `segments_completed` now matches `segment_purposes`, the body is done and `vid-ending` is next (the pipeline re-routes there on its own; standalone, tell the creator to run `vid-ending` when ready).
