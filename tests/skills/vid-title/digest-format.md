# Iteration digest (the human window)

Every autoresearch iteration writes `digest-iter-NN.md` next to the outputs.
This is the file the creator actually reads. Thirty seconds, titles only, each next
to the winner it was modeled on. No lanes, no reasoning, no scores.

The judge never sees this file. It exists so a human can catch what the
rubric misses, and human verdicts become rubric corrections at the next lock.

## Format

```markdown
# vid-title digest, iteration NN (quality_score: 0.83)

## Case 00: ruined-boards-first-sale
LOCKED  "11 Ruined Boards, Then a $2,400 Table in 90 Days" (B+S, 48)
        modeled on: "From 9 Ruined Boards to a $3,800 Table in 90 Days" (@twoboardtom, 14.6x)
  2nd   "Why 11 Ruined Boards Beat a Dream Shop"           (N+B, 38)
        modeled on: "Why Beginners Build the BEST Furniture (Nobody Talks About This)" (@wrenhalloran, 21.4x)
  WILD  "Every Board Dana Ruined Paid for the Table"       (B+N, 42)

## Case 01: ...
```

One block per case: the locked title, the strongest runner-up, the wildcard.
Each proven title carries its receipt on the line below. Nothing else.

## The verdict pass

The creator marks each locked title with one of:
- `CLICK` (I would click this next to the receipt title)
- `PASS` (I would scroll past)
- `BOX` (technically fine, feels like every other title)

Any PASS or BOX on a case the judge scored 5+ out of 6 is a rubric miss.
Collect those and bring them to the next rubric lock as calibration examples.
