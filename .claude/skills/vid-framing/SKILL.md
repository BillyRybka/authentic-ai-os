---
name: vid-framing
description: Pick the angle for one video. Get into the head of the one viewer it is for, confirm the read with the creator, then find the angle that makes the idea feel new and ground it in what has worked. Writes the locked angle, core payoff, format, and goal to piece.md, then hands to vid-title. Use whenever the creator needs the angle picked, even if they don't say "frame". Triggers include "frame the video", "pick the angle", "what should this video be about", "re-frame this piece".
---

# Video Framing

Pick the angle for one video that will create genuine intrigue in the viewer and force them to click based off of a need, want, fear, pain, or desire. Understand the one viewer first (the main problem they are stuck on, the transformation they want), confirm the read with the creator, then find the angle that makes the idea feel new and ground it in what has worked. The creator picks the final angle and the format it implies, and you write the lock to piece.md for vid-title to package.

## Core principles

These govern every step below.

- **Psychology first, evidence second.** The angle comes out of understanding the person. The pattern bank shapes and grounds it; it never generates it. An angle pulled from a bank with no viewer behind it is the generic AI angle this brand is built against.
- **The frame, not the facts, and not the headline.** Interesting is the angle, not the information; a line that only restates the topic is a label. Do not work the headline here, wording-for-the-click is vid-title's job. If an angle comes out headline-shaped on its own, capture it as written and hand it to vid-title as one candidate, free to beat.
- **Anti-fabrication.** Never invent an outlier, number, result, or bank entry. Name the gap instead. A withheld proof point becomes a one-line TODO in the body, never a number in the angle.
- **Creator drives, you structure.** You bring the read and the angles with a point of view. The creator decides; "does this fit MY audience" is theirs to answer. Every dropped angle gets a one-line reason so it never comes back.
- **Read aloud, in their voice.** If the creator would reword it saying it out loud, it is wrong. The core payoff is spoken straight to the viewer (second person), never a description of them. No em-dashes, and no hype verbs or consulting-speak; the creator's banned words live in the `refusals` list in `foundation/voice-profile.md`.

## What loads, and when

Load each file at the step that needs it. Do not front-load everything.

| File | Step | For |
|---|---|---|
| `content/pieces/{slug}/brain-dump.md` | 1 | the raw material and the problem it circles |
| `foundation/creator-foundation.md` | 2 | the avatar and iceberg: who this is for, the lane they serve |
| `references/reframe-toolkit.md` | 3 | the five moves that make a known idea feel new |
| `knowledge/BENS-framework.md` | 3 | the Big and New lens to judge the reframe |
| `banks/pattern-bank.md` | 3 | what has worked for this audience (grounds the angle) |
| `foundation/voice-profile.md` | 4 | the refusals list, so the locked lines carry no banned words |
| `references/format-index.md` | 4 | the seven formats and their jobs, to lock the format |

Stops: no `brain-dump.md`, point to vid-intake. No `creator-foundation.md`, point to /foundation. No `pattern-bank.md`, say so and offer vid-research, or shape the angle from the material alone and flag it as ungrounded.

Re-frame: if piece.md already has a `selected_angle`, ask whether to re-frame from scratch or refine the existing one. Do not resurface previously dropped angles unless the creator asks.

## The workflow

1. **Read the brain-dump.** What is the material, what problem does it keep circling, what does the creator want this video to do.

2. **Get into the viewer's head, then confirm.** This gate is the reason the skill exists. From the avatar and the material, go deep on the one person this is for: what they want, the main problem they are stuck on, the tension underneath it, the transformation they are after. Name the core payoff (what they walk away able to do). Lay the read back in a few plain lines (the viewer, the problem, the transformation, the payoff) and wait for a yes or a sharpen. Build nothing until they confirm "that's the video."

   The expensive mistake is a thin read, and it is expensive because it confirms easily. The creator hears their own topic said back and says yes. Nothing looks wrong until the title has no tension to work with and the video restates what the viewer already believes. By then the session, the filming, and the upload are spent. The read is the whole video at its cheapest, so fix it here.

   Thin read (a label, not a read): "The viewer is an ADHD entrepreneur. The problem is planning. The transformation is a system that works. The payoff is a weekly plan." Every word is true and none of it helps. Angles built on it come out as "how to plan your week with ADHD," which the viewer has scrolled past a hundred times.

   Strong read: "The viewer has bought the planners and tried the apps. She thinks she needs to plan harder, but every system she tries fights her brain, so she quits by week two and decides she is the broken one. The transformation is she stops blaming herself. The payoff is a week plan that still works on a bad brain day." Now the angle has something to push against: the enemy is "plan harder," and the frame is "your system fights your brain."

   One more, compressed. "The viewer wants more subscribers; the problem is nobody signs up" is a label. "The viewer ships every week and the list barely moves, because the letter promises tips and nobody forwards tips" is a read.

   The tell: watch how the creator confirms. A strong read gets a lean-in, a "yes, exactly" plus a sharpen, or a "wait, it is more that..." A polite instant yes usually means the read was thin. Stay in it until the read carries something the creator has not said out loud yet.

3. **Hunt the reframe, then ground it.** Find the angle that makes the known idea feel new. Reach for one of the five moves in `references/reframe-toolkit.md`: a fresh comparison or metaphor, a contrarian flip, a named system, the creator's own story, a visual framework. Judge each against BENS (`knowledge/BENS-framework.md`), weighting N, because feel-new beats be-new. Then pull the pattern bank and run the anchor rule from `references/angle-anchor-rules.md`: name the real entry (title, channel, views) so the angle is a hypothesis, or call it a gut pick. Nothing in between.

4. **Frame it, lock the format.** The creator picks the angle. Name the goal (sales, emails, or views), what this video is for. Then lock the format the frame implies (a client transformation is a case study, a launch reaction is news, a set of disconnected tips is a listicle), sanity-checked against the goal in `references/format-index.md` and confirmed with the creator. Lock one of the seven; that is the shape vid-structure builds on. Capture any dropped angles with a one-line reason.

5. **Save and hand off.** Write the locked fields to piece.md, append the dropped angles and any proof TODOs, confirm in one line (angle, format, goal), and point to vid-title.

## Output and handoff

vid-framing appends to the existing piece.md (created by vid-intake). It never overwrites another skill's fields; the field-ownership map lives in `knowledge/vault-integration.md`, and the exact append protocol is in `assets/piece-framing-additions.md`.

Frontmatter it writes:
- `selected_angle` one clean sentence a person would say out loud, in the creator's voice. No explanation clause, no colon-summary, no TODO inside. Headline-shaped is allowed; vid-title decides whether it survives as the title.
- `core_payoff` the one move the viewer should make, spoken to them (second person): "pick the one task only you can do this week and write down every step." Never "the viewer does X."
- `format` short-process | case-study | roast | deep-dive | interview | news | listicle
- `goal` sales | emails | views
- `voice_context` default `youtube-script`; another medium only if this piece genuinely is one
- `last_updated` today

Body it appends:
- `## Considered + Dropped Angles`, one line each (angle + why), append-only and sticky across re-frames
- any withheld proof as a one-line `> [!todo]`, kept out of the angle and payoff

Then confirm in one line and point to vid-title.

## Before you save

- The read carried something the creator had not said out loud, and they confirmed it before any angle was built.
- `selected_angle` is one clean voiced line; `core_payoff` is a second-person instruction.
- Every claimed pattern is a real bank entry; every gap is a TODO, nothing invented.
- `format` is one of the seven planners and `goal` is set.
- No em-dashes, no banned words, and it reads aloud.

References for depth: `references/reframe-toolkit.md` (the five reframe moves), `references/format-index.md` (the seven formats and their jobs), `references/angle-anchor-rules.md` (the canonical grounding rule: name the real entry or call it a gut pick), `references/framing-conversation-examples.md` (worked dialogues).
