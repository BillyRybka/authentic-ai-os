---
type: reference
scope: skill-local
loaded_by: [vid-intake]
status: active
tags: [reference, vid-intake, drilling, conversational-pacing]
---

# Push vs Pause Rules

When to drill, when to save with TODOs, how to bail without burning the conversation. Examples-first. The hardest part of vid-intake is knowing when to push for a sharper answer vs when to let it go and mark a TODO. This file gives you the calibration.

## The default

**Default to fewer questions.** When in doubt, save with a TODO. Downstream skills (vid-framing, vid-segment) will surface the gap when they hit it. vid-intake does not have to be perfect.

The intake's job is to capture enough material that vid-framing can pick the angle and vid-structure can build the skeleton. It is NOT to write the script. Push only where the gap will block downstream work.

## When to push

Push the creator on a thin spot if any of these is true:

### 1. A claim has no proof attached

**Push:** "Where's that number from?" or "Is this in your proof bank already?"

Worked example:
> Creator: "I cut a client's onboarding from 2 weeks to 90 minutes."
> Skill: "Where's that number from? Recording, doc, or just from memory?"
> Creator: "I have the Loom from the call. It's in raw/transcripts/2026-04-12-aaron-onboarding.md."
> Skill: "Wikilinked. Continue."

Why push here: claims without proof become liabilities downstream. vid-segment will need the proof for the credibility line, vid-ending may use it for the recap. Surfacing the source now saves time later.

### 2. A story is referenced but not told

**Push:** "Tell me the moment, not the lesson."

Worked example:
> Creator: "I had this thing happen with a client last week that proves the point."
> Skill: "Tell me the moment, not the lesson. What happened?"
> Creator: "She emailed me Sunday night, said she's quitting the program. Monday morning we got on a call. By Tuesday she'd booked her first 3 calls of the year."

Why push here: a referenced story without specifics is dead weight in the brain dump. Downstream writing skills can't do anything with "there's this thing that happened." 30 seconds of drill turns it into voice fuel.

If the first push doesn't unlock the moment, route through `knowledge/story-capture-guide.md` 6 prompts. Pick the prompt that fits the topic. If 2 prompts don't unlock, mark TODO and move on.

### 3. The viewer outcome is mushy

**Push:** "What does the viewer go and DO after watching?"

Worked example:
> Creator: "Viewers learn that depth beats frequency."
> Skill: "What does the viewer go and DO after watching? Specific behavior."
> Creator: "Cut their posting schedule from 3x a week to 1x a month, double the time per video, anchor each one to a real client transformation."

Why push here: vid-ending needs a concrete behavior change for the Bridge. "Learn that depth beats frequency" is a tagline, not an outcome. The actual DO is the lever for the close.

### 4. Iceberg or Top 3 alignment is unclear

**Push:** "Which Top 3 fits better?" or "Is this maybe an outlier?"

Worked example:
> Skill (Phase 4): "Inside your iceberg. Lands on Problem 2, cardio-bias. Sound right?"
> Creator: "Hmm, kind of. But it's also about Problem 3, inconsistency."
> Skill: "Which is the primary thread? The video can hit both, but vid-framing picks one as the anchor."
> Creator: "Cardio-bias is the spike. Inconsistency is a downstream consequence I'll mention."
> Skill: "Locked. Problem 2 primary, Problem 3 secondary in `aligned_with`."

Why push here: the alignment field drives downstream skill behavior. Vague alignment leads to vague framing.

## When NOT to push

Stop drilling if any of these is true:

### 1. The dump is rich and clear

If the creator handed you 5 specific points, a story with a date and a number, a claim with a source, and a clear outcome — STOP. Confirm what landed, run the alignment check, save. Drilling for the sake of drilling burns the conversation.

Bad pattern:
> Creator: [delivers a complete, specific brain dump]
> Skill: "Great. Now, let's deepen each point. Point 1: tell me more about why you believe..."

Don't do that. The creator already gave you what they have. Save it.

### 2. The creator already said "I'll come back to that"

If the creator flagged something as deliberate ("I want to dig into that later" or "skip that for now"), respect it. Mark a TODO in `Open questions` and move on. Pushing past a deliberate skip annoys the creator and trains them to skip the skill in future.

Worked example:
> Creator: "Don't worry about the third point right now. I want to chase it after I've thought more."
> Skill: "Got it. Adding to TODOs as 'point 3 placeholder, expand next session.' Continuing."

### 3. Two rounds of drilling have not unlocked

If you pushed once, the creator gave a thin response, you pushed again with a different angle, and it's still thin — STOP. Mark a TODO, move on. The memory or proof isn't there right now. Forcing it produces fabricated material the creator will reject later.

Worked example:
> Skill: "Where's that number from?"
> Creator: "I think I read it somewhere. Maybe a podcast?"
> Skill (push 2 with different angle): "Approximate range you trust? Even 'roughly 60-80%' is more honest than a specific number you can't source."
> Creator: "Honestly I'm not sure."
> Skill: "Pulling the specific number, marking as 'unverified claim, needs source before script.' We can replace with a range or your own data later."

### 4. The creator said "stop, just save"

Hard stop. Save with TODOs flagging whatever is incomplete. Never push past a direct stop request. The skill should feel pleasurable, not extractive. A creator who feels grilled won't run the skill again.

Worked example:
> Creator: "Stop, just save what we have."
> Skill: "Saving. Flagging open questions in TODO list: [list]. Run vid-framing when you're ready."

## How to bail mid-conversation

If the conversation is going sideways (mode misdetected, creator distracted, alignment can't lock, banks are empty for the angle), bail cleanly:

```
Skill: "I'm going to save what we have so far. The dump captures [X, Y]. Open questions for next session: [list]. 
Want me to flag this draft for revisit, or save and let vid-framing pick up from here?"
```

Two valid paths from there:

- **Flag for revisit:** save brain-dump.md with `status: incomplete` in frontmatter. Creator runs vid-intake again later to extend the dump before vid-framing fires.
- **Save and continue:** save with TODOs, hand off to vid-framing. vid-framing may surface gaps that come back to vid-intake.

Either is fine. The point is to never trap the creator in a conversation that isn't working.

## The pacing rhythm (for tone calibration)

Conversation cadence to aim for:

- **Skill messages: short.** 1-3 sentences. Never paste reference content. Never lecture.
- **Creator dumps: long.** Whatever they bring. The skill listens, doesn't interrupt.
- **Mirroring: tight.** The reflection back to the creator after the dump should fit in 4-6 lines.
- **Drill questions: surgical.** One question at a time. Not "tell me about X, Y, and Z."
- **Confirmations: micro.** "Sound right?" — yes or no in one word.

Aim for the conversation to feel like a sharp friend taking notes, not a form being filled out.

## Sample full pacing for a Mode 1 idea + dump

Reference target: under 5 minutes of conversation, 8-12 messages total.

1. Creator: opens with idea
2. Skill: confirms mode (1 line)
3. Skill: opens the door for dump (1 line)
4. Creator: dumps freely
5. Skill: mirrors back what landed (4-6 lines)
6. Creator: confirms or corrects (1-2 lines)
7. Skill: alignment surface (2 lines)
8. Creator: yes (1 word)
9. Skill: drill on 1 thin spot (1 line) [optional, skip if dump is rich]
10. Creator: gives the specific (1-2 lines)
11. Skill: proposes slug (1 line)
12. Creator: yes (1 word)
13. Skill: confirms save and hands off (1 line)

13 turns. 5 minutes. Done.

If you find yourself at turn 20 and still drilling, you've over-pushed. Bail.
