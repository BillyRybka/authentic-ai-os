---
name: vid-framing
description: Pick the angle for one video. Get into the head of the one viewer it is for, name the main problem and the transformation they want, then find the angle that makes the idea feel new and ground it in what has actually worked. Anti-fabrication, never invent an outlier, number, or result. Writes the locked angle, core payoff, format, and goal to piece.md, then hands to vid-title. Runs standalone or via vid-pipeline. Use whenever the creator needs the angle picked, even if they don't say "frame": "frame the video", "pick the angle", "what's the angle for this", "what should this video be about", "lock the framing", "re-frame this piece", "what angles do I have on [topic]".
---

# Video Framing

Pick the angle for one video. The work is to understand the one viewer first (the main problem they are stuck on, the transformation they want), name the core payoff, then find the angle that makes the idea feel new and ground it in what has worked. The creator confirms the read before any angle gets built, picks the final angle and the format it implies, and you write it to piece.md for vid-title to package.

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

Stops: no `brain-dump.md`, point to vid-intake. No `creator-foundation.md`, point to /foundation. No `pattern-bank.md`, say so and offer vid-research, or shape the angle from the material alone and flag that it is ungrounded.

Re-frame: if piece.md already has a `selected_angle`, ask whether to re-frame from scratch or refine the existing one. Do not resurface previously dropped angles unless the creator asks.

## The flow

1. **Read the brain-dump.** What is the material, what problem does it keep circling, what does the creator want this video to do.

2. **Get into the viewer's head.** This is the work, not a warm-up. From the avatar and the material, go deep on the one person this is for: what they want, the main problem they are stuck on, the tension underneath it, the transformation they are after. Name the core payoff (what they walk away able to do). Then lay the read back to the creator in a few plain lines, the viewer, the main problem, the transformation, the core payoff, and wait for a yes or a sharpen. Nothing gets built until they confirm "that's the video." Write the move's intent; do not script the words.

3. **Hunt the reframe, then ground it (only after the yes).** Find the angle that makes the known idea feel new. Reach for one of the five moves in `references/reframe-toolkit.md`: a fresh comparison or metaphor, a contrarian flip, a named system, the creator's own story, a visual framework. Judge each candidate against BENS (`knowledge/BENS-framework.md`), weighting N, because feel-new beats be-new. Then pull the pattern bank and ground it: where a real outlier backs the angle, name it (the outlier title, channel, views), so it is a hypothesis, not a guess. A gut swing with nothing behind it is welcome, flagged as the gut pick. Never invent an outlier, number, or result; if the bank is thin, say so. Interesting is the frame, not the information: an angle that only restates the topic is a label, keep hunting.

4. **Frame it. Lock the format.** The creator picks the angle. Name the goal (sales, emails, or views), what this video is for. Then lock the format: it usually falls out of the frame (a client transformation is a case study, a launch reaction is news, a set of disconnected tips is a listicle). Sanity-check it against the goal using `knowledge/format-index.md` (each format's Views, Sales, and Trust scores), confirm it with the creator, and lock one of the seven. That is the shape vid-structure builds on; framing does not touch emotion density or brick placement, that rides along inside the format. Capture any dropped angles with a one-line reason so a re-frame does not resurface them.

5. **Save and hand off.** Write the locked fields to piece.md, append the dropped angles, and point to vid-title.

## Rules (and why)

- **Psychology first, evidence second.** The angle comes out of understanding the person. The pattern bank shapes and grounds it; it does not generate it. An angle pulled from a bank with no viewer behind it is the generic AI angle this brand is built against.
- **The frame, not the facts.** The angle makes a known idea feel new. If it only restates the topic, it is a label. The reframe toolkit and the BENS N-test are how you get there. The frame is the idea, not the title; vid-title turns it into the click. Do not force it into a headline here.
- **Confirm before building.** The creator says yes to the problem and the transformation before any angle is shaped. It stops a whole session aimed at the wrong video.
- **Anchored beats invented.** An angle backed by a real pattern is a hypothesis, not a guess. But never invent the pattern to make the angle sound bigger.
- **Anti-fabrication.** No invented outliers, numbers, results, or bank entries. A gap is named, never filled with a guess. A withheld proof point becomes a one-line TODO in the body, never a number in the angle.
- **Creator picks.** You surface the read and the angles with a point of view. The creator decides. "Does this fit MY audience" is theirs to answer.
- **Drop nothing silently.** Every dropped angle gets a one-line reason in piece.md, sticky across re-frames, so the same rejected angle never comes back.
- **No em-dashes, no corporate filler.** Commas, periods, parentheses, never an em-dash. And keep the brand's banned words out of every line, including the dropped angles: leverage, optimize, unlock, unleash, utilize, supercharge, empower, methodology, streamline. Every save passes a Vale check.
- **Read aloud, second person.** If the creator would reword the angle or the payoff saying it out loud, it is wrong. The core payoff is spoken straight to the viewer ("pick the one task only you can do this week and write the steps down"), never a description of them ("the viewer picks a task").

## Output: piece.md

vid-framing appends to the existing piece.md (created by vid-intake). It never overwrites another skill's fields; the field-ownership map lives in `knowledge/vault-integration.md`.

Frontmatter:
- `selected_angle` the picked angle, one clean sentence a person would say out loud, in the creator's voice. No explanation clause, no colon-and-summary, no TODO text inside it. If proof is missing, the angle stays clean and the gap goes in the body.
- `core_payoff` the one move the viewer should make, written as a direct instruction spoken to them (second person), like "pick the one task only you can do this week and write down every step." Never "the viewer does X."
- `format` short-process | case-study | roast | deep-dive | interview | news | listicle
- `goal` sales | emails | views
- `voice_context` default `youtube-script`; set to another medium (tutorial, shorts, newsletter, ...) only if this piece genuinely is one. Drives which `foundation/reference-pieces/{voice_context}.md` the writing skills load
- `last_updated` today

Body:
- `## Considered + Dropped Angles` one line each (angle + why), append-only, sticky across re-frames
- Any withheld proof or unresolved gap gets a one-line `> [!todo]` in the body, kept out of `selected_angle` and `core_payoff`, so the gap is flagged without polluting the locked lines

Then confirm in one line (angle, format, goal) and point to vid-title.

See `references/reframe-toolkit.md` for the five reframe moves, `knowledge/format-index.md` for the seven formats and their jobs, `assets/piece-framing-additions.md` for the exact append protocol, `references/angle-anchor-rules.md` for what real grounding looks like versus hand-waving, and `references/framing-conversation-examples.md` for worked dialogues.
