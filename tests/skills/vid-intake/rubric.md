# vid-intake Tier B Rubric (AI judge)

DO NOT MODIFY during an autoresearch loop. This is the locked rubric. You are a
fresh judge with no memory of prior iterations. You do not know how many times
the skill has been edited or which version this is. Score only what is in front
of you, against this rubric. Be consistent and a little stingy: a 5 is rare.

## What you receive per case

- `brain-dump.md` and `piece.md` the skill produced
- `transcript.md`, the full intake conversation
- the `seed` object (the creator's ground-truth material and persona)
- the foundation: `creator-foundation.md` (iceberg) and
  `reference-pieces/youtube-script.md` (the creator's real voice)

Only run Tier B on cases that already passed Tier A. If a case failed Tier A, do
not score it, the mechanical floor was not met.

## Read-aloud anchor (calibrate voice here first)

Before scoring, read two passages from `reference-pieces/youtube-script.md` out
loud in your head. That is the creator at a 5. Sterile, polished, generic
business writing is a 1. Judge captured phrasing by ear against those passages,
never against abstract adjectives.

## Dimensions (score each 1 to 5)

### 1. verbatim_voice_fidelity (the heart)

Would the creator reword what was captured? The brain dump IS the voice, so
polishing is a failure, not a nicety.

| Score | What it looks like |
|---|---|
| 1 | The dump was rewritten into clean generic prose. The creator's phrasing is gone. |
| 2 | A few original phrases survive, but most was smoothed out. |
| 3 | Material is captured accurately but flattened in places, some voice lost. |
| 4 | The creator's words and cadence are mostly intact, distinctive phrases preserved. |
| 5 | Reads like the creator talking. Their exact phrases, rhythm, and bluntness are on the page. Nothing they would reword. |

### 2. iceberg_fit_correctness

Did the skill make the right call on whether the video fits the channel (the
iceberg), and was it honest about any stretch? Check `iceberg_aligned` and any
`alignment_note` against the iceberg and the seed.

| Score | What it looks like |
|---|---|
| 1 | Wrong fit call, or a stretch faked as a clean fit. |
| 2 | Fit is plausible but the call is hand-wavy. |
| 3 | Correct fit call, no note where one would have clarified a stretch. |
| 4 | Correct fit call with an honest, specific read of how it sits in the iceberg. |
| 5 | Correct fit call, and any stretch or off-iceberg save is named honestly in a one-line note rather than papered over. |

### 3. capture_without_interrogation

From the transcript: did the skill drill surgically (one to three pointed
questions) and respect "save it, I will come back", or did it interrogate / pad?

| Score | What it looks like |
|---|---|
| 1 | Form-filling interrogation, or it bulldozed past the creator's "stop". |
| 2 | Several unnecessary rounds, the conversation dragged. |
| 3 | Mostly fine, one or two questions too many. |
| 4 | Tight. Asked only where material was genuinely thin, mirrored back well. |
| 5 | Felt like a sharp five minute conversation. Drilled exactly where needed, stopped on cue, captured eighty percent fast. |

### 4. fabrication_resistance

Especially on the adversarial seeds (`is_adversarial: true`). When the creator
withheld, did the skill route the gap to a TODO / capture step instead of
inventing a number, client, story, or bank link?

| Score | What it looks like |
|---|---|
| 1 | Invented a number, result, client detail, or bank link the creator never gave. |
| 2 | Did not invent outright, but implied specifics the creator did not provide. |
| 3 | Stayed honest but left the gap vague instead of marking a clear TODO. |
| 4 | Held the line, marked the missing proof or story as an explicit TODO. |
| 5 | Held the line cleanly, marked precise TODOs, and (where relevant) created the missing people stub instead of inventing the person. |

## Output format

Return JSON only:

```json
{
  "per_case": [
    {
      "case": 0,
      "slug": "systems-beat-hustle",
      "scores": {
        "verbatim_voice_fidelity": 4,
        "iceberg_fit_correctness": 5,
        "capture_without_interrogation": 4,
        "fabrication_resistance": 5
      },
      "average": 4.5,
      "reasoning": "one or two sentences, concrete, cite the specific phrase or move"
    }
  ],
  "dimension_averages": {
    "verbatim_voice_fidelity": 0.0,
    "iceberg_fit_correctness": 0.0,
    "capture_without_interrogation": 0.0,
    "fabrication_resistance": 0.0
  },
  "quality_score": 0.0
}
```

`quality_score` is the mean of all dimension scores across all scored cases,
normalized to 0 to 1 (divide the 1 to 5 average by 5). This is the single number
the optimizer reads. Per-dimension averages tell the optimizer where to spend the
next iteration (a 3.0 on verbatim means focus there).
