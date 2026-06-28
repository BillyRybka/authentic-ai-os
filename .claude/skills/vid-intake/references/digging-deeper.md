---
type: reference
scope: skill-local
loaded_by: [vid-intake]
status: active
tags: [reference, vid-intake, drilling, conversational-pacing]
---

# Digging Deeper

When to drill, when to save with a TODO, and how to bail without burning the conversation. The hardest part of vid-intake is knowing when to push for a sharper answer and when to let it go. This is the calibration.

These describe what each move should uncover, not the words to say. Phrase your own short, sharp question in the moment. The creator-side lines below illustrate the gap; they are not a script for you.

## The default

Always offer one deeper pass, never interrogate. After you mirror the dump back, name the 2-3 spots where a little more would most sharpen the video and offer to push there. The creator takes it or saves. Never silently accept the dump, and never grind a question battery. One offer, their call.

When they decline, or a spot does not unlock in two rounds, save with a TODO. Downstream skills (vid-framing, vid-segment) surface the gap when they hit it. Intake captures enough that vid-framing can pick the angle and vid-structure can build the skeleton. It is not writing the script. But it is a co-writer: it pulls more out of the creator with pointed questions and never settles for the shallow version just to move fast.

## When to push

Push a thin spot when any of these is true. Aim your question at the gap named.

### 1. A claim has no proof attached

The creator states a result or number with no source ("I cut a client's onboarding from 2 weeks to 90 minutes"). Find where it comes from: a recording, a doc, the proof bank, or memory. If the claim is a principle rather than a number, push on the mechanism instead, the reason it is actually true.

Why: claims without proof become liabilities downstream. vid-segment needs the source for the credibility line, vid-ending may use it for the recap. Surfacing it now saves time.

### 2. A story is referenced but not told

The creator gestures at a story without the scene ("I had this thing happen with a client that proves the point"). Draw out the moment, not the lesson: the specific beat, when it turned, what was said.

Why: a referenced story without specifics is dead weight; downstream skills can do nothing with "there's this thing that happened." Drawing out the scene turns it into voice fuel. If it does not unlock, route through `knowledge/story-capture-guide.md`; if two prompts do not land, TODO and move on.

### 3. The viewer outcome is mushy

The creator names a takeaway, not a behavior ("viewers learn that depth beats frequency"). Pull the concrete thing the viewer goes and DOES after watching.

Why: vid-ending needs a real behavior change for the Bridge. A tagline is not an outcome.

### 4. Iceberg fit is unclear

The fit check comes back hedged ("kind of, it's more of a mindset thing than a training thing"). Settle whether it is inside the lane they serve or a deliberate stretch. Either way the video saves; you just note it.

Why: the fit flag tells downstream skills whether the channel-fit was deliberate. A vague fit leads to vague framing.

### 5. The viewer's objection is unanswered

The argument carries no counter. Pull the strongest pushback a skeptical viewer would raise, and the creator's answer to it.

Why: a teaching video that never names the objection reads naive. The objection-and-answer is what makes the argument land, and vid-segment wants it for the tension beat.

### 6. The contrarian edge is under-sharpened

The claim is hedged into something safe and forgettable ("most founders should probably post a bit less"). Pull the disagreeable version, the part people actually argue with.

Why: the sharp claim is usually the hook and the title. Surfacing it at intake hands vid-title and vid-framing the real angle.

## When NOT to push

Stop drilling when any of these is true.

### 1. The dump is already rich and clear

Five specific points, a story with a date and a number, a sourced claim, a clear outcome. Confirm what landed, run the fit check, save. Drilling a complete dump for the sake of it burns the conversation.

### 2. The creator deliberately parked something

They flagged a point as "I'll chase it later" or "skip that for now." Respect it, mark a TODO in Open questions, move on. Pushing past a deliberate skip trains them to skip the skill.

### 3. Two rounds have not unlocked

You pushed, got thin, pushed from a different angle, still thin. Stop. Mark the gap as a precise TODO (for example "unverified claim, needs a source before script"). The memory or proof is not there right now, and forcing it produces material they will reject later.

### 4. They said stop

Hard stop. Save with TODOs flagging whatever is incomplete. Never push past a direct stop request. The skill should feel pleasurable, not extractive. A creator who feels grilled will not run it again.

## How to bail mid-conversation

If it is going sideways (creator distracted, fit cannot lock, banks empty for the angle), save what you have cleanly: name what the dump captured, list the open questions for next session, and offer two paths.

- **Flag for revisit:** leave `status: ideating`, log the open questions, and leave the fit unset (`iceberg_aligned` blank). That unfinished fit is the signal: the creator runs vid-intake again later to extend the dump before vid-framing fires.
- **Save and continue:** save with TODOs and hand to vid-framing, which may surface gaps that route back here.

Either is fine. Never trap the creator in a conversation that is not working.

## Pacing

Aim for the feel of a sharp friend taking notes, not a form being filled out.

- Your messages: short, one or two sentences, one move each. Never paste reference content, never lecture.
- Their dump: as long as they want. Listen, do not interrupt.
- The mirror-back: tight, a few lines.
- Drill questions: one at a time, surgical, never a batch.
- Confirmations: micro.

A simple idea dump runs clean: they open, you open the door, they dump, you mirror back, they confirm, you run the fit check, one optional drill on the thinnest spot, you propose the slug, you save and hand off. If the drilling keeps going and nothing new is surfacing, you have over-pushed. Bail.
