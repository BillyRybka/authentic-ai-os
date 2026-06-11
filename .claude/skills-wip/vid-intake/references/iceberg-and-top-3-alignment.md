---
type: reference
scope: skill-local
loaded_by: [vid-intake]
status: active
tags: [reference, vid-intake, alignment, iceberg, top-3]
---

# Iceberg and Top 3 Alignment

The 2-layer sanity check vid-intake runs at Phase 4 before saving brain-dump.md. Examples-first. Worked example, near-miss, and decision flow per case.

## Why this exists

A channel solves the same 3 problems repeatedly across 20+ videos. A video that lands outside the iceberg breaks channel coherence. A video that fits the iceberg but doesn't address one of the Top 3 problems is an outlier the creator can ship deliberately, but most should hit a Top 3.

This check exists to catch wrong-channel videos early so the creator doesn't burn 60 minutes scripting something that won't grow the channel. Takes 10 seconds when the fit is clean. Takes 1 minute when alignment needs a conversation.

It does NOT exist to gate every video. Creator overrides allowed. The frontmatter records what was deliberate.

## The 2 layers

Layer 1: **Iceberg fit.** Is this video INSIDE the iceberg? Does it match who this channel is for and what they come back for? Sourced from `foundation/creator-foundation.md` iceberg statement.

Layer 2: **Top 3 fit.** Does it address one of the 3 specific problems the audience comes back for? Sourced from `foundation/creator-foundation.md` Top 3 problems list.

Run both. Surface both. Lock both in frontmatter.

## The 4 outcomes

Every alignment check lands in one of 4 outcomes. Decision flow:

```
Iceberg fit? Top 3 fit?
   YES        YES       → CLEAN FIT. Lock and move on.
   YES        NO        → OUTLIER WITHIN ICEBERG. Flag, ask rationale, allow override.
   NO         YES       → Rare and impossible by definition (Top 3 is inside iceberg). 
                          If you're in this state, you misread one of the layers. Re-check.
   NO         NO        → WRONG CHANNEL. Hard flag. Ask if iceberg shifted or video is wrong-fit.
```

## Worked: clean fit (YES + YES)

**Foundation context:**
- Iceberg: "I help busy founders build sustainable strength training habits in 30 minutes a day."
- Top 3 problems: (1) Time scarcity makes routines collapse, (2) Cardio-bias misallocates effort, (3) Inconsistency under stress.

**Brain dump topic:** "Why founders shouldn't run for cardio. Strength is higher leverage."

**Skill surfacing:**
> "Inside your iceberg, busy founders + sustainable strength habits. Lands on Problem 2: cardio-bias misallocates effort. Sound right?"

**Creator:** "Yes."

**Frontmatter saved:**
```yaml
problem_addressed: 2
iceberg_aligned: true
aligned_with: "Reinforces strength-as-highest-leverage-workout for time-poor founders"
```

**Why this works:** the topic clearly hits one of the 3 named problems. The iceberg statement mentions strength, the topic is about strength vs cardio. 10-second confirmation, no friction.

## Worked: outlier within iceberg (YES + NO)

**Same foundation context.**

**Brain dump topic:** "How to pick a barbell for a home gym setup. Bumper plates vs iron, knurling, sleeve length."

**Skill surfacing:**
> "Inside your iceberg, this fits busy founders setting up sustainable home strength. But this isn't one of your Top 3 problems specifically. Your 3 are time scarcity, cardio-bias, inconsistency. This is more equipment-selection. Want to ship it as an outlier within the iceberg, or would the angle land cleaner against one of the Top 3?"

**Creator:** "It's an outlier. I want to make it because clients keep asking. The angle would force-fit if I tied it to time scarcity."

**Skill:** "Got it. Capturing as `outlier_within_iceberg`. One-line rationale for the frontmatter?"

**Creator:** "Equipment-decision video, requested 6+ times by clients in the last month, channel-coherent because it's still busy-founder home strength."

**Frontmatter saved:**
```yaml
problem_addressed: outlier_within_iceberg
iceberg_aligned: true
aligned_with: "Equipment-decision video for busy-founder home strength setup, 6+ client requests in 30 days"
```

**Why this works:** skill flagged the soft mismatch, gave the creator the option to force-fit or ship as outlier, captured rationale. Channel coherence stays intact (still iceberg-aligned), but the creator's deliberate outlier is on record.

## Worked: wrong channel (NO + NO)

**Same foundation context.**

**Brain dump topic:** "How to fix lower back pain from sitting at a desk all day. Stretches and posture fixes."

**Skill surfacing:**
> "This doesn't clearly fit your iceberg, busy founders + sustainable strength training in 30 minutes. Lower back pain and posture is adjacent (rehab / mobility) but not strength. Two paths. Either your iceberg has shifted (do you cover rehab now?), or this video belongs on a different channel or as a guest piece somewhere else."

**Creator (option A):** "My iceberg has shifted, I do cover rehab now for founders specifically."
**Skill:** "OK. Recommend running vid-foundation refresh after this video to update the iceberg statement and Top 3 problems. For now I'll flag this as `outlier` and capture rationale that iceberg may be evolving."

**Creator (option B):** "No, you're right, this should go on my email list as a free resource, not a channel video."
**Skill:** "Bailing on save. Want me to capture the dump anyway as a draft you can pull from later, or drop it?"

**Why this works:** skill caught the wrong-channel case before 60 minutes of scripting wasted on a video that won't grow the channel. Creator gets two clean paths: refresh iceberg, or move the material to a different surface.

## Near-miss: forcing a fit that isn't there

**Same foundation context.**

**Brain dump topic:** "How to fix lower back pain from sitting at a desk."

**Skill surfacing (BAD):**
> "This kind of fits Problem 3, inconsistency under stress, because back pain breaks consistency. Lock that?"

**Why this fails:** the skill stretched the alignment to avoid surfacing the mismatch. Channel coherence drops over time when stretches stack. The honest move is to flag the mismatch, not paper over it.

The fix: surface the mismatch. Let the creator decide. Either they have a real angle that DOES connect to Problem 3 (and they'll tell you it), or they don't, and you save as outlier or bail.

## Near-miss: hard-blocking the creator

**Same foundation context.**

**Brain dump topic:** [equipment-selection video]

**Skill surfacing (BAD):**
> "REJECTED. This video doesn't address any of your Top 3 problems. Cannot save until you refine the angle to fit one of: time scarcity, cardio-bias, inconsistency under stress."

**Why this fails:** vid-intake never blocks a save. The creator's call. Surface the flag, explain the consequence, ask for rationale, save with the flag in frontmatter. Hard-blocking turns the skill into a gate the creator works around or stops using.

## How to phrase the alignment surface

Same shape every time. Two lines max.

> "[Iceberg fit verdict in one phrase]. [Top 3 fit verdict with the specific problem named]. Sound right?"

Example:
> "Inside your iceberg. Lands on Problem 2, cardio-bias. Sound right?"

Don't over-explain. The creator wrote the iceberg + Top 3 themselves. They know what they mean. The skill just confirms the fit.

If the creator says "no" or "not exactly", ask one short question to find the actual fit:

> "Which Top 3 fits better?"
> OR
> "What thread does this actually run on?"
> OR
> "Is this maybe an outlier video?"

Then capture and save. Do not run a 5-minute alignment debate.

## What gets saved

The 4 frontmatter fields after the alignment check:

```yaml
problem_addressed: 1 | 2 | 3 | outlier_within_iceberg | outlier
iceberg_aligned: true | false
aligned_with: "{one-line rationale: this video reinforces the iceberg by ___}"
source_internal_only: "{Mode 4 only: brief source note. Empty for other modes.}"
```

`aligned_with` is the most important field for downstream skills. vid-framing reads it to understand the chosen angle. vid-segment reads it to constrain bank pulls. vid-ending reads it to pick the next-problem Gap. Make it specific and concrete.

Bad `aligned_with`: "fits the channel"
Good `aligned_with`: "Reinforces strength-as-highest-leverage-workout for time-poor founders"
