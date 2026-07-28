---
name: vid-framing
description: Read the one viewer in five beats (viewer, main problem, tension underneath, transformation, payoff), confirm the read with the creator, then pressure that tension into what the video argues, digging for it when the material arrives flat. Writes the argument, core payoff, format, and goal to piece.md, then hands to vid-title. Use whenever the creator needs the angle picked, even if they don't say "frame". Triggers include "frame the video", "pick the angle", "what should this video be about", "re-frame this piece".
---

# Video Framing

Find what is at stake for the one viewer, and lock what this video argues. Understand the person first (what they are stuck on, what they believe about it, what it is costing them), confirm the read with the creator, then name the argument the video makes. The creator picks it, you lock the format and goal, and vid-title packages it for the click.

**Scope: the argument, never the words.** Wording for the click is vid-title's job, and it has the banks, the lock list, and the kill pass to do it properly. Framing hands over what the video says, not how it is sold.

## Core principles

- **Nothing at stake, nothing to click.** Interest is not a technique applied to a topic. It is a thing the viewer stands to lose or has already lost without noticing. Find it, or name that it is missing.
- **The angle is an argument, not a headline.** `selected_angle` says what is true and what it costs. If it reads like a title, it is the wrong shape; rewrite it as the argument underneath.
- **Creator drives, you structure.** You bring the read and a point of view. They decide. Every dropped angle gets a one-line reason so it never comes back.
- **Anti-fabrication.** Never invent a number, result, client, or outcome. A gap is a TODO in the body, never a claim in the angle.
- **Read aloud, in their voice.** If the creator would reword it saying it out loud, it is wrong. The payoff is spoken straight to the viewer in second person, never a description of them. No em-dashes, no hype verbs; the creator's banned words live in the `refusals` list in `foundation/voice-profile.md`.

## What loads, and when

Load each file at the step that needs it. Do not front-load.

| File | Step | For |
|---|---|---|
| `content/pieces/{slug}/brain-dump.md` | 1 | the raw material and the problem it circles |
| `foundation/creator-foundation.md` | 2 | the avatar and iceberg: who this is for, the lane they serve |
| `references/stake-finder.md` | 3 | where the stake lives, how to dig for it, when to call the ceiling |
| `foundation/voice-profile.md` | 4 | the refusals list, so the locked lines carry no banned words |
| `references/format-index.md` | 4 | the seven formats and their jobs |

Stops: no `brain-dump.md`, point to vid-intake. No `creator-foundation.md`, point to /foundation.

Re-frame: if piece.md already has a `selected_angle`, ask whether to re-frame from scratch or refine it. Do not resurface previously dropped angles unless the creator asks.

## The workflow

1. **Read the brain-dump.** What is the material, what problem does it keep circling, what does the creator want this video to do.

2. **Read the viewer, then confirm.** From the avatar and the material, go deep on the one person this is for. Five beats, in this order:

   - **The viewer.** The audience is already known, so this beat names the cut: which slice of them this video is for, and what state they are in that makes it theirs and not everyone's. "A business owner on a personal brand who already uses Claude daily and is past does-this-work" is a cut. "A business owner" is the avatar restated.
   - **The main problem.** What they are actually stuck on, not the surface topic.
   - **The tension underneath.** What being stuck there feels like. The part they would not say out loud.
   - **The transformation.** What changes for them by the end.
   - **The core payoff.** The one thing they walk away able to do, spoken to them.

   Lay it back plainly, one beat per short paragraph, labeled. Then stop: "is that the video, or do you want to sharpen the problem or the transformation?" Naming the two sharpenable parts is what gets a real correction back instead of a polite yes. Build nothing until they say "that's the video."

   The tension and the transformation are the two beats that carry the video. Cut either and the read is a diagnosis: every line true, nothing anyone wants to watch. Tension is what it feels like now, transformation is what it looks like fixed, and the angle lives in the gap between them.

   The expensive mistake is a thin read, and it is expensive because it confirms easily. Thin: "the viewer is an ADHD entrepreneur, the problem is planning, the payoff is a weekly plan." Every word true, none of it useful. Strong: "she has bought the planners and tried the apps, she thinks she needs to plan harder, and every system she tries fights her brain, so she quits by week two and decides she is the broken one." Now there is something to push against.

   Watch how they confirm. A strong read gets a lean-in or a "wait, it's more that..." A polite instant yes usually means the read was thin.

3. **Pressure the tension into the argument.** The read already surfaced the tension. This step turns it into what the video argues. Open `references/stake-finder.md` and name which kind it is: a belief that is costing them, a cost they cannot see, a thing they feel and cannot name, or a scoreboard they are wrong about. One is enough.

   If the tension beat came up thin, dig for it here. Most brain-dumps arrive as accurate information with no conflict in them; the tension is usually in the creator's head and never made it to the page. One question at a time, in flow, never as a battery. If two rounds surface nothing, say so plainly and give them the three honest options in `stake-finder.md` rather than manufacturing tension. Framing does not kill videos; it names the ceiling out loud.

4. **Name the argument, lock format and goal.** Write the argument in one line the creator would say out loud. Argument-shaped, never headline-shaped. Confirm the core payoff. Name the goal (sales, emails, or views). Then lock the format the frame implies (a client transformation is a case study, a launch reaction is news, disconnected tips are a listicle), sanity-checked against the goal in `references/format-index.md`. Lock one of the seven; that is the shape vid-structure builds on. Capture dropped angles with a one-line reason.

5. **Save and hand off.** Write the locked fields and the read to piece.md, confirm in one line (argument, format, goal), and point to vid-title.

## Output and handoff

vid-framing appends to the existing piece.md (created by vid-intake). It never overwrites another skill's fields; the ownership map lives in `knowledge/piece-contract.md`, and the append protocol is in `assets/piece-framing-additions.md`.

Frontmatter it writes:

- `selected_angle` one clean sentence naming what the video argues, in the creator's voice. Argument-shaped. No explanation clause, no colon-summary, no TODO inside.
- `core_payoff` the one move the viewer should make, spoken to them in second person: "pick the one task only you can do this week and write down every step." Never "the viewer does X."
- `format` short-process | case-study | roast | deep-dive | interview | news | listicle
- `goal` sales | emails | views
- `voice_context` default `youtube-script`; another medium only if this piece genuinely is one
- `last_updated` today

Body it appends:

- `## The Read`, the five beats (viewer, main problem, tension underneath, transformation, payoff). This is the ore vid-title, vid-intro, and vid-structure pull from; without it the read dies in the conversation.
- `## Considered + Dropped Angles`, one line each (angle plus why), append-only and sticky across re-frames
- any withheld proof as a one-line `> [!todo]`, kept out of the angle and payoff

## Before you save

- All five beats are there, tension and transformation included, and the read carried something the creator had not said out loud before they confirmed it.
- The angle has a real stake in it, or the ceiling was named plainly and the creator chose to proceed anyway.
- `selected_angle` is argument-shaped, not a title. `core_payoff` is a second-person instruction.
- Nothing invented. Every gap is a TODO.
- `format` is one of the seven planners and `goal` is set.
- No em-dashes, no banned words, and it reads aloud.

References for depth: `references/stake-finder.md` (where the stake lives, the dig questions, the ceiling call), `references/format-index.md` (the seven formats and their jobs), `references/framing-conversation-examples.md` (worked dialogues, including a full dig).
