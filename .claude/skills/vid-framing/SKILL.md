---
name: vid-framing
description: Turn a captured topic into a chosen video. Names what the material is about and what merely delivers it, offers eight frames that point the same video at eight different viewer wants, then writes the read (Target, Transformation, Stakes) on the one the creator picks. Writes the frame, core payoff, format, and goal to piece.md and hands to vid-title. Use whenever a piece needs its direction decided, even if the creator never says "frame". Triggers include "frame the video", "pick the angle", "what should this video be about", "what's the angle here", "re-frame this piece", "I don't know how to position this one".
---

# Video Framing

One captured brain-dump goes in. One chosen video comes out: the frame it runs on, the core payoff it promises, the read of the person it is for, and the format and goal it gets built to. The creator chooses from multiple frames that would be intriguing to their audience. 

## Core principles

- **The frame is the viewer's reason, not the video's contents.** A walkthrough is a format. A tool is a mechanism. Removing the thing they hate is a frame. Describe contents and you answer "what happens in this video," which nobody clicks for.

- **The same source makes eight different frames.** Interest is not a technique applied to a topic. It is which want the topic gets pointed at, and pointing is a choice. Rotate the want and the video changes without a word of the material changing.

- **Choosing beats approving.** One proposal gets a polite yes and a video aimed at the wrong person. Eight real alternatives get a real preference, and that preference is information nothing else in this skill can produce.

- **Depth serves the choice, it does not make it.** The read of the viewer is written after the frame is locked, because the person in Target changes depending on which want the video points at. Written first, it decides the frame by accident.

- **Nothing at stake, nothing to click.** A frame promises something the viewer stands to gain or stop losing. When the material genuinely has neither, name the ceiling out loud instead of manufacturing one.

- **Anti-fabrication constrains generation.** A frame the material cannot support never gets offered, so there is nothing to walk back later. A missing number is a TODO in the body, never a promise in the frame.

- **Read aloud, in their voice.** Frames and the read both. Anything the creator would pause and reword is wrong. Their banned words live in the `refusals` list in `foundation/voice-profile.md`.

## What loads, and when

| File | Step | For |
|---|---|---|
| `content/pieces/{slug}/brain-dump.md` | 1 | the material, and what in it is topic versus mechanism |
| `foundation/creator-foundation.md` | 3 | the avatar and the iceberg: whose wants the lenses rotate through |
| `references/frame-lenses.md` | 3 | the eight lenses, what each sounds like, and when each does not apply |
| `foundation/voice-profile.md` | 6 | the refusals list, so the locked lines carry no banned words |
| `references/format-index.md` | 6 | the seven formats and their jobs |

Stops: no `brain-dump.md`, point to vid-intake. No `creator-foundation.md`, point to /foundation.

Re-frame: if piece.md already carries a `frame`, surface it and ask whether to rotate fresh or sharpen that one. Never re-offer something already in `## Considered + Dropped Angles` unless the creator asks for it.

## The eight lenses at a glance

The same video, pointed at eight different wants. Depth on each, and when each fails, is in `references/frame-lenses.md`.

| Lens | The want underneath |
|---|---|
| Control | Stop adapting to the thing. Make it adapt to you. |
| Time savings | Stop spending hours on this. |
| Familiarity | Understand the new thing through one they already know. |
| Frustration | Kill the one specific thing they hate. |
| Identity | Have the output be theirs, and recognisably so. |
| Curiosity | Find the piece they are missing. |
| Convenience | Get the result without it becoming another job. |
| Repetition | Never do this particular thing again. |

## The workflow

### 1. Separate what the video is about from what delivers it

1. **Read the dump.** What material is actually here: the demo, the story, the numbers, the thing the creator keeps circling.

2. **Name the topic.** What this is broadly about, in plain words, with no tool in it.

3. **Name the mechanism and call which kind it is.** The mechanism is whatever produces the result. The test is whether the viewer would search for it by name.

  - **Delivery.** Nobody searches for it. It stays out of every frame and shows up in the video body, once they already care.

  - **The draw.** It has its own audience and its own search demand, usually because it is new or already trending. It can carry the frame, and the format is usually `news`.

  - **A qualifier.** Known, not hot. It narrows a frame without carrying one.

4. **State the three lines back.** Topic, mechanism plus its kind, material. Not a question. This is the header on the next message.

Getting this wrong is expensive in both directions. A mechanism treated as the draw produces a video about a tool nobody asked about. A mechanism buried when it *is* the draw throws away the exact thing people are searching for this week.

### 2. Ask for their angle first

One line, before offering anything: do they already have an angle in mind.

If they do, it joins the list in the next step and gets weighed against the rest on the same terms. **It does not skip the rotation.** A creator's first instinct is usually the most obvious frame on the topic, which makes it the one worth comparing against alternatives rather than the one worth adopting unexamined. If it wins on the merits, say so plainly and pick it.

### 3. Offer eight real choices, not eight rewordings

1. **Hold the video fixed and rotate the lens.** Same material, same demo, same story. Only the want changes.
2. **Write each frame in third person, describing the video.** "A video that shows {who} how to {what changes for them}." Never a spoken line, never a pitch, never a headline.
3. **Give each frame its own core payoff.** One deliverable, in plain words. Third person here, because eight second-person lines in a row do not scan.
4. **Cut duplicates by lens, not by wording.** Two frames tracing to the same want are one frame written twice, however different they read.
5. **Recommend one and say why.** You are a partner with a point of view, not a menu. Recommend the ceiling, not the floor: the frame you would bet on, not the one with the fewest ways to fail.
6. **Offer the dial in one line.** More, a different lens, sharper, or rotate again.

The shape, one blank line between entries:

```
3. **{short handle, for talking about it}**
   Frame: A video that shows {who} how to {the change}, {the condition that makes it theirs}.
   Core payoff: The viewer {ends up holding one concrete thing}.
```

The handle is a conversational label so the creator can say "the second one." It is never saved: a handle is title-shaped, and putting one on disk anchors vid-title on a line written before the banks are open.

Rules that fire here:

- **Plain nouns, always.** When a real word for the thing exists, use it. Reaching for "an automated pre-output validation layer" is what happens when the plain word was available and got avoided.
- **The lens stays internal.** It is what guarantees the eight are genuinely different. The creator never sees the label.
- **Technical language belongs later in the video, never in the frame.** The viewer does not need to be excited about the tool. They need to be excited about what stops happening to them.
- **A frame the material cannot support never gets written.** No invented number, client, or result, not even in a frame nobody picks.

**If all eight come out flat**, that is the strongest evidence available that there is nothing at stake here, and far better evidence than a single failed dig. Say it plainly and give three honest options: narrow to the one part that does have a stake, let a real number carry it, or film it as a fast utility video with the ceiling named going in. Framing does not kill videos. Measurement does.

### 4. The creator picks

**Stop here.** Nothing gets built until a frame is chosen.

The pick locks the frame and its core payoff together, and it doubles as the excitement check, so there is no separate question about whether they like the direction. Choosing it is liking it. Offer a payoff tweak in the same breath rather than as another stop.

Watch how they pick. A clean choice with a reason attached means the rotation landed. Picking the recommendation with no comment usually means none of the eight opened anything, which is a signal to rotate again rather than to proceed.

### 5. Write who this is for, what changes for them, and what it costs if it doesn't

The chosen frame names a want. This step writes the person who has it. Three fields, about them, in third person, all pointed at the locked lens.

- **Target.** Who this video is for and the situation they are in, as one causal chain. They want something, but this keeps happening, so they end up doing this, which costs them that. **There is no template here.** Writing "their goal is / their challenge is / their pain point is" produces a form, not a person. The connectives carry it: *but*, *so*, *which means*.

  The middle of the chain is usually the move they make that keeps them stuck: they add another rule, they fix it themselves, they buy the next tool. It comes out of the material or it does not exist. Never invent one to give the chain a turn.

- 

  - Flat: "coaches who want more clients."

  - Sharp: "They get plenty of discovery calls booked and they want to convert more of them. But they spend the call proving they're good, running credentials and case studies and the method, so the prospect leaves informed and unconvinced. So they hear 'let me think about it,' and they never find out what the hesitation actually was. Which means every call teaches them nothing and the next one goes the same way."

- **Transformation.** They stop doing X and do Y instead, plus what that gets them. The test is whether something actually changed or they just felt something for a few minutes.

  - Flat: "they close more calls."

  - Sharp: "They stop performing credibility and start running a diagnosis instead. The prospect does most of the talking, and by the time there's a pitch it's aimed at the thing the prospect actually said, not the thing the coach assumed."

- **Stakes.** Open with "if they keep working the old way," then run a chain where each consequence causes the next. Let the sentences get short as it escalates; that rhythm is the escalation. Near the end, name the **misattribution**: what they blame and try to fix instead, because the real cause is invisible to them. Then land it back where Target started.

  A cost worth escalating is almost always one of four things: a bill that arrives late enough that nobody connects it to the cause, a fix that costs more than the problem it solves, a thing that quietly stops happening, or a number they are watching that says everything is fine. If the cost you have is none of those, it is probably a symptom and the real one is further down.

- 
  - Flat: "they lose revenue."
  - Sharp: "If they keep running calls the old way, the close rate stays where it is and they blame the leads. So they buy more leads. More calls, same conversion, more hours on Zoom for the same money. And because every call ends in a polite maybe, they never hear a real objection, so they never fix the offer either. They start discounting to get someone over the line, which brings in clients who pay less and expect more. Eventually they're working more for less, and it reads like a soft market, when the real problem is a call that never asked a question."

Keep the lanes clean. Target describes the situation and stops; the compounding belongs to Stakes. Transformation is the shift itself, not the tactic that delivers it. Written well the three run as one piece: Target ends on a cost, Stakes compounds that cost, and the last line of Stakes lands on the thing Target opened with.

**How it is written matters as much as what is in it.** All three fields can be correct and still be dead on the page, and a dead read hands vid-title and vid-intro nothing to work with.

- **Say it the way they would say it.** Read each line as if the creator were saying it to one person. If they would pause and reword it, rewrite it.
- **Make the cost felt, not reported.** "The reading is the real tax" describes it from a distance. Put them in it instead: what they do, when, and what it costs them the week it slips.
- **One image per field.** Three fresh constructions stacked into two sentences reads as reaching, and each one steals attention from the last. Pick the one that lands and say the rest straight.
- **Vary the sentence length on purpose.** Long sentences carry reasoning, short ones land blows. Stakes wants to tighten as it escalates, so the last consequences hit in four or five words each.
- **Shorter and better beats longer.** Cutting a sentence usually sharpens a field. If a field is long because every clause earns it, keep it. Otherwise cut.

**If Stakes will not come**, the cost is usually in the creator's head and never made it into the dump, because they have held the position long enough to forget it was ever contested. Ask one question, in flow, in your own words, and stop the moment one opens:

- What do people get wrong about this?
- What did you believe before? (Their old position is the viewer's current one. This one lands most often.)
- What does it cost them to keep doing it the way they do now?
- Who pushed back on this, and what did they say?

Never run all four. That is an interrogation, it makes the creator defensive, and it closes the door you are opening. If two rounds surface nothing, the video has a modest cost and that is honest: Target runs its chain and stops, Stakes stay small, and the ceiling gets named the same way it would at step 3.

Lay the three fields back, one short paragraph each, and save in the same move. The creator can sharpen after; nothing waits on it.

### 6. Set the format and the goal

State both, do not ask. "Short-process, goal emails. Say the word if either's wrong."

- **Format** follows the material and the frame. A client transformation is a case study, a launch reaction is news, disconnected tips are a listicle. Sanity-check against the goal in `references/format-index.md` and lock one of the seven, because that is the shape vid-structure builds on.
- **Goal** follows audience temperature. Cold wants views, warm wants emails, hot wants sales.

Both are derivations from decisions already made. Turning them into questions spends the creator's attention on something they have effectively already answered.

### 7. Save and hand off

Write everything to piece.md per `assets/piece-framing-additions.md`, confirm in one line (frame, format, goal), and point to vid-title.

## Output and handoff

vid-framing appends to the piece.md that vid-intake created and never touches another skill's fields. Ownership lives in `knowledge/piece-contract.md`; the exact shape lives in `assets/piece-framing-additions.md`.

Frontmatter it writes: `frame`, `core_payoff`, `mechanism`, `format`, `goal`, `voice_context`, `last_updated`.

Body it writes:

- `## The Read`, three fields (Target, Transformation, Stakes). vid-title presses on the Stakes, vid-intro mines them for hooks, vid-structure builds toward the Transformation.
- `## Considered + Dropped Angles`, the frames that lost, one terse line each, sticky across re-frames.
- Any withheld proof as a one-line `> [!todo]`, kept out of the frame and the payoff.

Prerequisite: vid-intake. Handoff: vid-title.

## Before you save

- The frame describes a video in third person. If it could be read aloud as a line in the video, or pasted in as a title, it is the wrong shape.
- The mechanism sits where its kind says it belongs: out of the frame if it is delivery, in the frame if it is the draw.
- `core_payoff` is one deliverable in plain words, in second person, with no bonus asset bolted on.
- Target is a causal chain, not a filled-in form. If "their goal is" or "their pain point is" appears, rewrite it.
- Stakes escalate, name the misattribution, and land back where Target started.
- Every claim in the read traces to a real line in the dump or something the creator said in this session.
- Every line is sayable. Read them aloud; anything the creator would reword gets rewritten first.
- Nothing invented. Every gap is a `> [!todo]`.
- `format` is one of the seven planners and `goal` is set.
- No em-dashes, no banned words.

## References for depth

- `references/frame-lenses.md`: the eight lenses, the want under each, what a frame in it sounds like, and the conditions where it does not apply. Open it at step 3, every time.
- `references/format-index.md`: the seven formats with their views, sales, and trust scores, and how to pick against the goal. Open it at step 6.
- `references/framing-conversation-examples.md`: one worked session from dump to saved piece, plus a dig and a ceiling call. Read it once to calibrate pacing, not on every run.
