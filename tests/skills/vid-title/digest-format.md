# Iteration digest (the human window)

Every autoresearch iteration writes `digest-iter-NN.md` next to the outputs.
This is the file Billy actually reads. Thirty seconds, titles only, each next
to the winner it was modeled on. No lanes, no reasoning, no scores.

The judge never sees this file. It exists so a human can catch what the
rubric misses, and human verdicts become rubric corrections at the next lock.

## Format

```markdown
# vid-title digest, iteration NN (quality_score: 0.83)

## Case 00: client-340k-to-1-3m
LOCKED  "$340K to $1.3M on 2,500 Subscribers"            (B+S, 38)
        modeled on: "How This Mom Makes $48K/Month With Claude" (@sabrina_ramonov, 17x)
  2nd   "Why Chasing Subscribers Kept This Channel Broke" (N+B, 48)
        modeled on: "Why Introverts Make the BEST Content Creators" (@thisisnickys, 22.0x)
  WILD  "You Don't Need an Audience. You Need a System."  (N, 46)

## Case 01: ...
```

One block per case: the locked title, the strongest runner-up, the wildcard.
Each proven title carries its receipt on the line below. Nothing else.

## The verdict pass

Billy marks each locked title with one of:
- `CLICK` (I would click this next to the receipt title)
- `PASS` (I would scroll past)
- `BOX` (technically fine, feels like every other title)

Any PASS or BOX on a case the judge scored 5+ out of 6 is a rubric miss.
Collect those and bring them to the next rubric lock as calibration examples.
