---
type: reference
skill: vid-pressure-test
phase: 4
tags: [interactive-loop, fix-flow]
---

# Interactive Fix Loop: Worked Dialogues

Phase 4 walks the creator through hard issues one at a time. The flow is Approve / Deny+rewrite / Skip / Mark-as-gap.

This file shows the actual conversational shapes. The principles live in SKILL.md; the dialogues live here.

## The base block

Every hard issue surfaces with this shape:

```
Hard issue N of M
Reviewer: {source-traceability | voice-authenticity | AI-slop | retention-logic}
Location: {section} line {N}
Quote: "{exact text from script.md}"
Issue: {one-sentence diagnosis}

Suggested rewrite:
  "{specific replacement text in the creator's voice}"

Approve / Deny (write your own) / Skip
```

Keep the block tight. No meta-commentary. No "I think this would be better." Just the data and the four options (Skip becomes Mark-as-gap if hard-rule).

## Worked example 1: clean approve

```
AI: Hard issue 1 of 3
    Reviewer: source-traceability
    Location: Segment 2 line 3
    Quote: "47% of CEOs say they struggle with this exact problem."
    Issue: The number 47% is not in brain-dump, foundation, or any bank. Likely fabricated.

    Suggested rewrite:
      "Most of my coaching clients struggle with this exact problem."

    Approve / Deny / Skip

Creator: approve

AI: [edits script.md, replaces the quote]
    Fixed. Moving to issue 2.
```

No extra confirmation. Apply and move.

## Worked example 2: deny with creator's own version

```
AI: Hard issue 2 of 3
    Reviewer: voice-authenticity
    Location: Segment 4 line 7
    Quote: "It is not about doing more. It is about doing the right things."
    Issue: Contrast-template structure ("not X, but Y") is an anti-pattern in your voice-profile. Reference-pieces never use this rhythm.

    Suggested rewrite:
      "Doing more is not the move. Doing the right things is."

    Approve / Deny / Skip

Creator: deny. let me rewrite: "More is the wrong dial. Right is the right dial."

AI: [light-vets the creator's version: no banned phrases, no em-dash, no guardrail refusals]
    [edits script.md, applies creator's text]
    Fixed with your version. Moving to issue 3.
```

If the creator's version is clean, apply silently. If not, see example 5 (light-vet violation).

## Worked example 3: skip on a soft issue (allowed)

```
AI: Hard issue 3 of 3
    Reviewer: ai-slop
    Location: Segment 1 opener
    Quote: "Now let me show you something interesting."
    Issue: Announcing transition. Tells the viewer to expect interesting content instead of just being interesting.

    Suggested rewrite:
      Cut the announcement. Open with the thing itself.

    Approve / Deny / Skip

Creator: skip. that one i actually want.

AI: Logged as accepted. Moving on.
```

Skip is allowed because this is a SOFT-leaning AI-slop issue, not a hard-rule violation. Creator's call.

## Worked example 4: Skip BLOCKED on hard-rule violation

```
AI: Hard issue 1 of 3
    Reviewer: source-traceability
    Location: Segment 2 line 3
    Quote: "47% of CEOs say they struggle with this exact problem."
    Issue: The number 47% is not in brain-dump, foundation, or any bank. Likely fabricated.

    Suggested rewrite:
      "Most of my coaching clients struggle with this exact problem."

    Approve / Deny / Skip

Creator: skip

AI: Skip is not available on fabricated claims. The number 47% has no source and shipping it lies to the viewer. Options:
    - Approve the suggested rewrite (use "most of my coaching clients")
    - Deny and paste your own version with a real source
    - Mark-as-gap (logs to piece.md `claims_to_source_before_filming`: blocks "ready to film" verdict until you confirm the number from a real source)

Creator: mark-as-gap. i think i saw 47% in a Gartner report. i'll find it.

AI: [writes to piece.md: claims_to_source_before_filming: ["Segment 2 line 3: 47% of CEOs claim: verify Gartner source before filming"]]
    Logged. Moving to issue 2. Final verdict will flag this as needs-revision until you confirm.
```

Skip block is non-negotiable for: fabricated claims, em-dashes, banned phrases (the house list or voice-profile refusals). The other options are real paths forward; the lie isn't.

## Worked example 5: creator-rewrite light-vet catches new violation

```
AI: Hard issue 2 of 3
    Reviewer: voice-authenticity
    Location: Segment 3 line 4
    Quote: "You might want to consider this approach."
    Issue: "might want to" is a hedge stack flagged as a guardrail refusal anti-pattern. Undermines stakes.

    Suggested rewrite:
      "This is the approach."

    Approve / Deny / Skip

Creator: deny. i want some softness. let me try: "You should probably try this approach."

AI: One quick check on your version:
    - "probably" is a guardrail refusal anti-pattern (same hedge family as "might"). Same problem as the original.

    Revise, accept anyway, or use the suggested rewrite?

Creator: ok use yours

AI: [applies the suggested rewrite]
    Fixed. Moving to issue 3.
```

Light-vet is one pass. If creator accepts the violation knowingly ("accept anyway"), apply and move on. Don't loop.

## Worked example 6: creator-rewrite light-vet, creator revises

```
AI: Hard issue 1 of 3
    Reviewer: ai-slop
    Location: Intro line 6
    Quote: "Let me dive into the first thing."
    Issue: "dive into" is a Tier 1 banned phrase per transition-patterns.

    Suggested rewrite:
      "Here is the first thing."

    Approve / Deny / Skip

Creator: deny. let me write: "Let me jump into the first thing."

AI: One quick check:
    - "jump into" is a Tier 2 announcing-transition pattern (same family as "dive into": banned).

    Revise, accept anyway, or use the suggested rewrite?

Creator: try: "First thing first..." (with em-dash at end)

AI: Quick check:
    - Em-dash in your rewrite. House rule, zero tolerance.

    Revise (replace with period or comma), accept anyway, or use my version?

Creator: "First thing first."

AI: Clean. Applying.
    [edits script.md]
    Fixed. Moving to issue 2.
```

Creator iterated twice. Light-vet caught both violations. Final version is clean. Apply silently.

## Worked example 7: bulk-keep mode for confident creators

```
AI: Hard issue 1 of 3: [issue surfaces]

Creator: obvious, just fix it

AI: [applies suggested rewrite to script.md]
    Issue 2 of 3: [issue surfaces]

Creator: same, fix it

AI: [applies]
    Issue 3 of 3: [issue surfaces]

Creator: i'll write my own. "[creator's version]"

AI: [light-vets, applies]
    All 3 resolved. Moving to read-aloud.
```

When the creator signals bulk-keep, the AI applies fast without re-confirming after each one. Stay in flow.

## Mark-as-gap dialogue

```
AI: Skip is not available on this hard-rule violation. Options:
    - Approve / Deny+rewrite / Mark-as-gap

Creator: mark-as-gap. i need to verify the source first.

AI: What is the gap? (one line for the piece.md log)

Creator: need to confirm Gartner report has the 47% number

AI: [writes to piece.md]:
    claims_to_source_before_filming:
      - "Segment 2 line 3: '47% of CEOs' claim: verify Gartner source before filming"

    Logged. Final verdict will be needs-revision until you confirm.
    Moving to issue 2.
```

The gap stays in the script unchanged until the creator confirms or removes. Verdict can't be "ready to film" with open gaps.

## The end-of-walk transition

When all hard issues are resolved:

```
AI: All hard issues resolved.
    {N hard issues fixed: M via approve, P via deny+rewrite, Q via mark-as-gap}
    {N soft issues remain: logged to piece.md, non-blocking}

    Now the read-aloud test. Take 3 minutes. Read script.md out loud start to finish. Would you reword anything?

Creator: [reads, responds]
```

See SKILL.md Phase 5 for read-aloud handling. The interactive loop hands off cleanly to the read-aloud gate.

## What to avoid

- Re-asking after creator's clear decision ("Are you sure you want to approve?")
- Surfacing soft issues during Phase 4 (they wait for Phase 6 summary)
- Adding meta-commentary ("Great choice!") between issues
- Showing the full script context unless the issue spans sections (then show the spanning lines)
- Holding the loop open if the creator goes silent (after one nudge, move on with the prior decision OR end the session and resume later)

## When the loop goes sideways

If the creator denies 3+ rewrites in a row:

```
AI: You've rejected my voice-match attempts on the last 3 issues. Either I'm misreading your voice or you're working in a different register today. Want to paste a recent reference piece so I can recalibrate, or push through the rest?
```

If the creator wants to bail mid-loop:

```
Creator: i need to come back to this

AI: [writes to piece.md]:
    pressure_test_status: in-progress
    hard_issues_remaining: {N}
    next_issue: {brief description}

    Saved. Resume by re-invoking vid-pressure-test on this piece.
```
