---
type: reference
skill: vid-pressure-test
phase: 1
tags: [rubric-weighting, conditioning]
---

# Rubric Conditioning Matrix

How piece.md fields (goal, format) plus the audience temperature the retention reviewer derives from the script shape what each reviewer weights heavier. Weights are not numbers; they are which checks fire harder when conditions align. Reviewers still run full rubrics; weighting only affects ranking and severity.

## By goal

- **sales** → source-traceability heavier (claim accuracy = buyer trust). retention-logic Gate 5 heavier (ending CTA must reference offer; vague closes fail).
- **views** → retention-logic Gates 1-4 heavier (hold attention across whole video). AI-slop heavier (cold view-seeking viewers leave fastest on slop).
- **emails** → retention-logic Gate 5 heavier (lead magnet specificity in CTA). source-traceability heavier (lead magnet promises must match delivery).

## By format

- **case-study** → retention-logic: title-promise lands at Outcome beat; story traceability strict. source-traceability: story-bank entry for protagonist must exist; outcome numbers must trace to proof-bank.
- **listicle** → retention-logic: each item N+1 > N expectation; named lesson lands at last item; item count promised matches item count delivered. voice-authenticity: item openers match creator's listicle rhythm.
- **short-process** → retention-logic: each step a small payoff that compounds; full method = full step list. source-traceability: each step's mechanism traces to creator experience.
- **deep-dive** → retention-logic: cross-segment thread tracking strict; concepts open early, deepen mid, resolve at synthesis. source-traceability: stricter on cited research/studies (invites "studies show" failure).
- **news** → retention-logic: compressed arc; named answer lands earlier than other formats. source-traceability: news claims need source URLs/screenshots traceable to brain-dump.
- **roast** → retention-logic: each call-out serves the central premise. AI-slop: stricter on hedge stacks (roasts cannot hedge).
- **interview** → retention-logic: questions promised get answered by guest; host setups hand off cleanly. source-traceability: guest credibility traces to guest's actual bio.

## By audience temperature (derived from the script, not a stored field)

Judge cold/warm/hot from the finished script itself: topic breadth, how much prior trust the framing assumes, whether the CTA presumes the viewer already knows the creator.

- **cold** → AI-slop tighter (zero trust to spend on weak prose). retention-logic Gate 1 tighter for first segment (cold viewers leave when Setup promise isn't visibly being delivered). voice-authenticity: rhythm matters more (off-rhythm reads as inauthentic to first-time viewers).
- **warm** → all reviewers run at standard weight.
- **hot** → retention-logic Gate 5 tighter (hot viewers came for the next step; vague CTA wastes their intent). source-traceability slightly relaxed but factual breaks still fail.

## How conditioning gets passed to reviewers

When spawning each reviewer in Phase 2, include in its system prompt:

```
You are reviewing a video script for {goal}, format {format}. (The retention reviewer derives audience temperature from the script itself.)

Apply your standard rubric, but tighten on these checks:
- {tightened check 1}
- {tightened check 2}
```

## Rules

- Conditioning never skips a reviewer or adds checks. All 4 always run their full rubric.
- Top-3 cap holds. Conditioning only affects which 3 surface.
- If reviewer flags a soft issue that conditioning says should be hard (e.g., sales-goal piece with weak CTA), elevate to hard.
- Hard rubric violations stay hard regardless of conditioning.
