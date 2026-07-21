# vid-segment Tier B Rubric (AI judge)

DO NOT MODIFY during an autoresearch loop. This is the locked rubric. You are a
fresh judge with no memory of prior iterations. Score only what is in front of
you, against this rubric. Be consistent and a little stingy: a 5 is rare.

Only run Tier B on cases that already passed Tier A. If a case failed Tier A,
do not score it: the mechanical floor was not met.

## What you receive per case

- `script.md` with the segment prose appended under its heading
- `piece.md` (updated frontmatter) and any `banks/` write-backs
- `transcript.md`, the creator gate conversation
- the `seed` object (ground-truth material, `is_adversarial`,
  `bank_pulls_allowed`, `fabrication_traps`)
- the suite fixture state the skill consumed (`fixtures/{slug}/piece.md` and
  `script.md`, the skeleton with the picked parable and principle)
- the after-intake `brain-dump.md` for this slug
- the shared foundation: `voice-profile.md` and
  `reference-pieces/youtube-script.md` (the creator's real voice)
- the skill's own craft reference: `.claude/skills/vid-segment/references/parable-principle-shapes.md`

## Read-aloud anchor (calibrate voice here first)

Before scoring, read two passages from `reference-pieces/youtube-script.md` out
loud in your head. That is the creator at a 5 for voice. Then read the matching
worked shape in `references/parable-principle-shapes.md`: that is the craft bar
for the segment's format.

## Dimensions (score each 1 to 5)

### 1. tension_craft

**What it measures:** Is the segment a chain of setups and payoffs, or a
lecture? Open on the inherited setup, show then tell, every payoff instantly
re-hooks, takeaway punch, handoff that promises a result. Score against SKILL.md
Step 3's tension discipline, not against "is the prose nice."

| Score | Description |
|-------|-------------|
| 1 | Topic-label open, explanation stacked on explanation, dead close ("and that's mistake 3"). |
| 2 | Opens on the topic not the stakes; one payoff lands but the segment keeps explaining after it. |
| 3 | Show precedes tell and a takeaway lands, but at least one payoff is followed by more explaining instead of a re-hook. |
| 4 | Setups and payoffs chain cleanly; the takeaway is one repeatable sentence; the handoff signals the shift and promises a result. |
| 5 | All of 4, and the open connects to the previous segment's closing line so the viewer arrives mid-curiosity. Reads like the worked shapes file. |

### 2. material_fidelity

**What it measures:** Every specific (number, name, story beat) traces verbatim
to the brain dump or the pulled bank entries. The bank says "five hours to one
hour", the prose does not say "way faster". On adversarial seeds, full marks
REQUIRE the gap to be named (TODO callout, open To build row) instead of
filled.

| Score | Description |
|-------|-------------|
| 1 | Invented or rounded a specific; on an adversarial seed, fabricated a number or link. |
| 2 | No outright invention, but specifics got polished into vagueness ("cut his time way down"). |
| 3 | Specifics trace, but the picked bank material is underused: the story is summarized instead of played. |
| 4 | Specifics verbatim, story played Problem-Action-Outcome, proof lands after the lesson it backs. |
| 5 | All of 4, and on thin-material segments the prose stays honest and lean instead of padding around the gap. |

### 3. voice_read_aloud

**What it measures:** Does the segment read like the creator in
`reference-pieces/youtube-script.md`? Brain-dump phrasing wins; the prose
should sound spoken to one person, with varied sentence lengths.

| Score | Description |
|-------|-------------|
| 1 | Corporate or AI-flavored; the creator would reword every other line. |
| 2 | Plain but polished; the brain dump's own words got "improved" into cleaner prose. |
| 3 | Avoids the worst tells but could belong to any business channel. |
| 4 | Close to the creator's cadence; brain-dump phrases survive intact. Minor word choices slightly off. |
| 5 | Indistinguishable from the reference pieces. The creator reads it aloud without rewriting a word. |

### 4. format_shape_fit

**What it measures:** Does the segment run the shape its format planner
prescribes? Listicle point: full parable-principle mini-cycle with a
forward-hook transition. Case study: the arc stays one story, proof at the
outcome, lesson at the end of the body. Short process: lean principle-first,
parable only where earned.

| Score | Description |
|-------|-------------|
| 1 | Wrong shape entirely (a case study chopped into listicle points, a listicle point with no parable). |
| 2 | Right shape on paper but the bricks are dead (parable announces a topic, principle is description). |
| 3 | Shape correct, one brick weak (e.g. metaphor present but not mapped back to the point). |
| 4 | Shape correct, both bricks land, parable type fits the point's problem per the decision matrix. |
| 5 | All of 4, plus the segment spends its creativity exactly where the point needs belief and nowhere else. |

## Output format

Return JSON only:

```json
{
  "per_case": [
    {
      "case": 0,
      "slug": "5-onboarding-mistakes",
      "scores": {
        "tension_craft": 4,
        "material_fidelity": 5,
        "voice_read_aloud": 4,
        "format_shape_fit": 4
      },
      "average": 4.25,
      "reasoning": "one or two sentences, concrete, cite the specific line that drove the score"
    }
  ],
  "dimension_averages": {
    "tension_craft": 0.0,
    "material_fidelity": 0.0,
    "voice_read_aloud": 0.0,
    "format_shape_fit": 0.0
  },
  "quality_score": 0.0
}
```

`quality_score` is the mean of all dimension scores across all scored cases,
normalized to 0 to 1 (divide the 1 to 5 average by 5). Per-dimension averages
tell the optimizer where to spend the next iteration.
