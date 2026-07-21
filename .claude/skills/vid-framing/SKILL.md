---
name: vid-framing
description: Pick the angle for one video. Get into the head of the one viewer it is for, name the main problem and the transformation they want, then find the angle that makes the idea feel new and ground it in what has actually worked. Anti-fabrication, never invent an outlier, number, or result. Writes the locked angle, core payoff, format, and goal to piece.md, then hands to vid-title. Runs standalone or via vid-pipeline. Use whenever the creator needs the angle picked, even if they don't say "frame": "frame the video", "pick the angle", "what's the angle for this", "what should this video be about", "lock the framing", "re-frame this piece", "what angles do I have on [topic]".
---

# Video Framing

Pick the angle for one video that will create genuine intrigue in the viewer and force them to click based off of a need, want, fear, pain, or desire. Understand the one viewer first (the main problem they are stuck on, the transformation they want), name the core payoff, then find the angle that makes the idea feel new and ground it in what has worked. The creator confirms the read before any angle is built, picks the final angle and the format it implies, and you write it to piece.md for vid-title to package.

## Core principles

These govern every step below.

- **Psychology first, evidence second.** The angle comes out of understanding the person. The pattern bank shapes and grounds it; it never generates it. An angle pulled from a bank with no viewer behind it is the generic AI angle this brand is built against.
- **The frame, not the facts.** Interesting is the angle, not the information. A line that only restates the topic is a label. The frame is the idea, not the title; vid-title turns it into the click, so do not force a headline here.
- **Anti-fabrication.** Never invent an outlier, number, result, or bank entry. Name the gap instead. A withheld proof point becomes a one-line TODO in the body, never a number in the angle.
- **Creator drives, you structure.** You bring the read and the angles with a point of view. The creator decides; "does this fit MY audience" is theirs to answer. Every dropped angle gets a one-line reason so it never comes back.
- **Read aloud, in their voice.** If the creator would reword it saying it out loud, it is wrong. The core payoff is spoken straight to the viewer (second person), never a description of them. No em-dashes, and none of the brand's banned words: leverage, optimize, unlock, unleash, utilize, supercharge, empower, methodology, streamline.

## What loads, and when

Load each file at the step that needs it. Do not front-load everything.

| File | Step | For |
|---|---|---|
| `content/pieces/{slug}/brain-dump.md` | 1 | the raw material and the problem it circles |
| `foundation/creator-foundation.md` | 2 | the avatar and iceberg: who this is for, the lane they serve |
| `references/reframe-toolkit.md` | 3 | the five moves that make a known idea feel new |
| `knowledge/BENS-framework.md` | 3 | the Big and New lens to judge the reframe |
| `banks/pattern-bank.md` | 3 | what has worked for this audience (grounds the angle) |
| `knowledge/format-index.md` | 4 | the seven formats and their jobs, to lock the format |

Stops: no `brain-dump.md`, point to vid-intake. No `creator-foundation.md`, point to /foundation. No `pattern-bank.md`, say so and offer vid-research, or shape the angle from the material alone and flag it as ungrounded.

Re-frame: if piece.md already has a `selected_angle`, ask whether to re-frame from scratch or refine the existing one. Do not resurface previously dropped angles unless the creator asks.

## The workflow

1. **Read the brain-dump.** What is the material, what problem does it keep circling, what does the creator want this video to do.

2. **Get into the viewer's head, then confirm.** This is the work, not a warm-up. From the avatar and the material, go deep on the one person this is for: what they want, the main problem they are stuck on, the tension underneath it, the transformation they are after. Name the core payoff (what they walk away able to do). Lay the read back in a few plain lines (the viewer, the problem, the transformation, the payoff) and wait for a yes or a sharpen. Build nothing until they confirm "that's the video." A whole session aimed at the wrong problem is the expensive mistake this gate prevents.

3. **Hunt the reframe, then ground it.** Find the angle that makes the known idea feel new. Reach for one of the five moves in `references/reframe-toolkit.md`: a fresh comparison or metaphor, a contrarian flip, a named system, the creator's own story, a visual framework. Judge each against BENS (`knowledge/BENS-framework.md`), weighting N, because feel-new beats be-new. Then pull the pattern bank: where a real outlier backs the angle, name it (title, channel, views), so it is a hypothesis, not a guess. A gut swing with nothing behind it is welcome, flagged as the gut pick.

4. **Frame it, lock the format.** The creator picks the angle. Name the goal (sales, emails, or views), what this video is for. Then lock the format the frame implies (a client transformation is a case study, a launch reaction is news, a set of disconnected tips is a listicle), sanity-checked against the goal in `knowledge/format-index.md` and confirmed with the creator. Lock one of the seven; that is the shape vid-structure builds on, and framing does not touch emotion density or brick placement. Capture any dropped angles with a one-line reason.

5. **Save and hand off.** Write the locked fields to piece.md, append the dropped angles and any proof TODOs, confirm in one line (angle, format, goal), and point to vid-title.

## Output and handoff

vid-framing appends to the existing piece.md (created by vid-intake). It never overwrites another skill's fields; the field-ownership map lives in `knowledge/vault-integration.md`, and the exact append protocol is in `assets/piece-framing-additions.md`.

Frontmatter it writes:
- `selected_angle` one clean sentence a person would say out loud, in the creator's voice. No explanation clause, no colon-summary, no TODO inside.
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

- The read was confirmed before any angle was built.
- `selected_angle` is one clean voiced line; `core_payoff` is a second-person instruction.
- Every claimed pattern is a real bank entry; every gap is a TODO, nothing invented.
- `format` is one of the seven planners and `goal` is set.
- No em-dashes, no banned words, and it reads aloud.

See `references/reframe-toolkit.md` for the five reframe moves, `knowledge/format-index.md` for the seven formats and their jobs, `references/angle-anchor-rules.md` for real grounding versus hand-waving, and `references/framing-conversation-examples.md` for worked dialogues.
