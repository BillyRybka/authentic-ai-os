---
name: vid-framing
description: Read the one viewer as Target, Transformation, Stakes, and Core Payoff, confirm the read with the creator, then name the argument the video makes, digging for it when the material arrives flat. Writes the argument, core payoff, format, and goal to piece.md, then hands to vid-title. Use whenever the creator needs the angle picked, even if they don't say "frame". Triggers include "frame the video", "pick the angle", "what should this video be about", "re-frame this piece".
---

# Video Framing

Read the one viewer, and lock what this video argues. Write the read as four fields (Target, Transformation, Stakes, Core payoff), confirm it with the creator, then name the argument that closes the gap between where they are and where they land. The creator picks it, you lock the format and goal, and vid-title packages it for the click.

**Scope: the argument, never the words.** Wording for the click is vid-title's job, and it has the banks, the lock list, and the kill pass to do it properly. Framing hands over what the video says, not how it is sold.

## Core principles

- **Nothing at stake, nothing to click.** Interest is not a technique applied to a topic. It is a thing the viewer stands to lose or has already lost without noticing. Find it, or name that it is missing.
- **The angle is an argument, not a headline.** `selected_angle` says what is true and what it costs. If it reads like a title, it is the wrong shape; rewrite it as the argument underneath.
- **Creator drives, you structure.** You bring the read and a point of view. They decide. Every dropped angle gets a one-line reason so it never comes back.
- **Anti-fabrication.** Never invent a number, result, client, or outcome. A gap is a TODO in the body, never a claim in the angle.
- **Read aloud, in their voice.** If the creator would reword it saying it out loud, it is wrong. The read is written about the viewer in third person; the payoff names what they end up holding, not what you tell them to do. No em-dashes, no hype verbs; the creator's banned words live in the `refusals` list in `foundation/voice-profile.md`.

## What loads, and when

Load each file at the step that needs it. Do not front-load.

| File | Step | For |
|---|---|---|
| `content/pieces/{slug}/brain-dump.md` | 1 | the raw material and the problem it circles |
| `foundation/creator-foundation.md` | 2 | the avatar and iceberg: who this is for, the lane they serve |
| `references/stake-finder.md` | 2 | the four blind-spot shapes, the dig questions, when to call the ceiling |
| `foundation/voice-profile.md` | 4 | the refusals list, so the locked lines carry no banned words |
| `references/format-index.md` | 4 | the seven formats and their jobs |

Stops: no `brain-dump.md`, point to vid-intake. No `creator-foundation.md`, point to /foundation.

Re-frame: if piece.md already has a `selected_angle`, ask whether to re-frame from scratch or refine it. Do not resurface previously dropped angles unless the creator asks.

## The workflow

1. **Read the brain-dump.** What is the material, what problem does it keep circling, what does the creator want this video to do.

2. **Read the viewer, then confirm.** Open `references/stake-finder.md` first: Target's blind spot and the Stakes are the two hardest fields here, and it holds the shapes they take plus the dig questions for when the dump comes up flat. Then write four fields, about them, in third person.

   - **Core payoff.** Write this one first; the other three anchor to it. "By the end of this video you'll have [the one concrete thing], [and what that means you stop doing]." Second person, one deliverable, named in plain words. A bonus asset or a second feature is not part of the payoff, and jamming one in is the fastest way to make the line unsayable.

     - Flat: "learn a better discovery call framework."
     - Also flat: "a structured diagnostic conversation framework that surfaces latent objections, plus the question bank that powers it." Two deliverables, and abstraction where a plain word would do.
     - Sharp: "By the end of this video you'll have a discovery call that surfaces the real objection while the prospect is still on the line, instead of hearing 'let me think about it' and never finding out why."

   - **Target.** Who this video is for and the situation they are in, written as one causal chain. They want something, but this keeps happening, so they end up doing this, which costs them that. **There is no template here.** Do not write "their goal is / their challenge is / their pain point is"; that scaffold reads as a form being filled in. The connectives are what carry it: *but*, *so*, *which means*.

     Add the blind spot only when the material actually has one. The test is traceability: point at the line in the brain-dump, or the thing the creator said in this conversation, that it came from. If you cannot, you invented it. A launch reaction or a straight tutorial often has none, and when the creator says outright there is nothing deeper here, believe them.

     - Flat: "coaches who want more clients."
     - Sharp: "They get plenty of discovery calls booked and they want to convert more of them. But they spend the call proving they're good, running credentials and case studies and the method, so the prospect leaves informed and unconvinced. So they hear 'let me think about it,' and they never find out what the hesitation actually was. Which means every call teaches them nothing and the next one goes the same way."

   - **Transformation.** They stop doing X and do Y instead, plus what that gets them. Directional, and the test is whether something actually changed or they just felt something for a few minutes.

     - Flat: "they close more calls."
     - Sharp: "They stop performing credibility and start running a diagnosis instead. The prospect does most of the talking, and by the time there's a pitch it's aimed at the thing the prospect actually said, not the thing the coach assumed."

   - **Stakes.** Open with "if they keep working the old way," then run a chain where each consequence causes the next. Let the sentences get short as it escalates; that rhythm is the escalation. Near the end, name the **misattribution**: the thing they blame and try to fix instead, because the real cause is invisible to them. Then land it back where Target started.

     - Flat: "they lose revenue."
     - Sharp: "If they keep running calls the old way, the close rate stays where it is and they blame the leads. So they buy more leads. More calls, same conversion, more hours on Zoom for the same money. And because every call ends in a polite maybe, they never hear a real objection, so they never fix the offer either. They start discounting to get someone over the line, which brings in clients who pay less and expect more. Eventually they're working more for less, and it reads like a soft market, when the real problem is a call that never asked a question."

   Written well, the four run as one piece: Target ends on a cost, Stakes takes that cost and compounds it, and the last line of Stakes lands back on the thing Target opened with. Keep the lanes clean while you do it. Target describes the situation and stops; the compounding belongs to Stakes. Transformation is the shift itself, not the tactic that delivers it.

   **How it is written matters as much as what is in it.** All four fields can be correct and still be dead on the page, and a dead read hands vid-title and vid-intro nothing to work with. Five habits kill it:

   - **Say it the way they would say it.** Read each line as if the creator were saying it to one person. If they would pause and reword it, it is wrong. "The output announcing itself as AI" and "handing work off has never held" are both true and neither is sayable.
   - **Use the plain noun.** When a real word for the thing exists, use it. "A check that flags banned words and makes the model fix them" is what you write when you are avoiding the word "autocorrect." The plain noun is almost always sharper than a description of it.
   - **One image per field.** Three or four fresh constructions stacked into two sentences reads as reaching, and each one steals attention from the last. Pick the one that lands and say the rest straight.
   - **Make the cost felt, not reported.** "The reading is the real tax" reports it from a distance. "They read every line of every draft before it goes out, and the ones they were too fried to read went out anyway, under their name" puts them in it.
   - **Vary the sentence length on purpose.** Long sentences carry reasoning; short ones land blows. Stakes especially wants to tighten as it escalates, so the last consequences hit in four or five words each.
   - **Shorter and better beats longer.** Cutting a sentence usually sharpens a field. Length is never the quality signal; if a field is long because every clause earns it, keep it, and otherwise cut.

   Lay it back plainly, one field per short paragraph, labeled. Then stop: "is that the video, or do you want to sharpen the target or the transformation?" Naming the two sharpenable parts is what gets a real correction back instead of a polite yes. Build nothing until they say "that's the video."

   Watch how they confirm. A strong read gets a lean-in or a "wait, it's more that..." A polite instant yes usually means the read was thin.

3. **Name the argument.** The read already carries the gap: where they are in Target, where they land in Transformation, what it costs them in Stakes. The argument is the one sentence that closes that gap. Where the Target has a blind spot, the argument is usually its correction: they think it is X, it is actually Y.

   If the read came back thin at the gate, this is the second chance to dig, using the questions already open in `stake-finder.md`. One question at a time, in flow, never as a battery. If two rounds surface nothing, say so plainly and give them the three honest options there rather than manufacturing tension. Framing does not kill videos; it names the ceiling out loud.

4. **Lock the format and the goal.** The creator picks the argument; write it in one line they would say out loud, argument-shaped and never headline-shaped. Name the goal (sales, emails, or views). Then lock the format the frame implies (a client transformation is a case study, a launch reaction is news, disconnected tips are a listicle), sanity-checked against the goal in `references/format-index.md`. Lock one of the seven; that is the shape vid-structure builds on. Capture dropped angles with a one-line reason.

5. **Save and hand off.** Write the locked fields and the read to piece.md, confirm in one line (argument, format, goal), and point to vid-title.

## Output and handoff

vid-framing appends to the existing piece.md (created by vid-intake). It never overwrites another skill's fields; the ownership map lives in `knowledge/piece-contract.md`, and the append protocol is in `assets/piece-framing-additions.md`.

Frontmatter it writes:

- `selected_angle` one clean sentence naming what the video argues, in the creator's voice. Argument-shaped. No explanation clause, no colon-summary, no TODO inside.
- `core_payoff` the deliverable: what the viewer will have, know, or be able to do after watching. One or two sentences, specific enough that they know exactly what they are getting. "By the end of this video, coaches will have a discovery call structure that surfaces the real objection while the prospect is still on the line." Not a diagnosis of their problem, not a thesis. The same sentence as the Core payoff field in `## The Read`, verbatim.
- `format` short-process | case-study | roast | deep-dive | interview | news | listicle
- `goal` sales | emails | views
- `voice_context` default `youtube-script`; another medium only if this piece genuinely is one
- `last_updated` today

Body it appends:

- `## The Read`, the four fields (Target, Transformation, Stakes, Core payoff). vid-title presses on the Stakes, vid-intro mines them for hooks, and vid-structure builds toward the Transformation. Without it on disk the read dies in the conversation.
- `## Considered + Dropped Angles`, one line each (angle plus why), append-only and sticky across re-frames
- any withheld proof as a one-line `> [!todo]`, kept out of the angle and payoff

## Before you save

- All four fields are there. Target, Transformation, and Stakes are about them in third person; the Core payoff speaks to them in second person.
- Every line is sayable. Read the four fields aloud; anything the creator would pause and reword gets rewritten before saving.
- Target runs as a causal chain, not a filled-in form. If the words "their goal is" or "their pain point is" appear, rewrite it.
- Plain nouns where the thing has a name. One image per field, not three. The cost is felt, not reported.
- Stakes escalate, name the misattribution, and land back where Target started. Any blind spot in Target traces to a real line in the dump or the conversation.
- `core_payoff` is one deliverable in plain words, and it does not carry a bonus asset.
- `selected_angle` is argument-shaped, not a title. `core_payoff` is a deliverable, not an instruction, and matches the read's Core payoff verbatim.
- Nothing invented. Every gap is a TODO.
- `format` is one of the seven planners and `goal` is set.
- No em-dashes, no banned words, and it reads aloud.

References for depth: `references/stake-finder.md` (the four blind-spot shapes, the dig questions, the ceiling call), `references/format-index.md` (the seven formats and their jobs), `references/framing-conversation-examples.md` (worked dialogues, a full composed read, and a dig).
