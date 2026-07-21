# vid-capture Tier B Rubric (AI judge)

DO NOT MODIFY during an autoresearch loop. This is the locked rubric. You are a
fresh judge with no memory of prior iterations. Score only what is in front of
you, against this rubric. Be consistent and a little stingy: a 5 is rare.

> Status: STUB. Dimensions and anchors are defined; per-score example tables
> are intentionally thinner than the vid-framing rubric. Flesh them out before
> the first real Tier B run.

## What you receive per case

- the bank entry the skill produced (`{entry_type}-{slug}.md`), if any
- any people stub (`people-{Full-Name}.md`)
- `transcript.md`, the full capture conversation
- the case object from `test_cases.json` (stage, expectations, dedup targets)
- the seed object (raw material, persona reveals/withholds, adversarial flag)
- the shared fixture tree (existing banks, `people/`, reference pieces)

Only run Tier B on cases that already passed Tier A. If a case failed Tier A,
do not score it: the mechanical floor was not met.

## Read-aloud anchor (calibrate voice here first)

Read two passages from `fixtures/shared/foundation/reference-pieces/youtube-script.md`
before scoring. That is the creator at a 5 for voice. A bank entry polished
into marketing copy is a 1 on voice no matter how clean the schema is.

## Dimensions (score each 1 to 5)

### 1. dig_deeper_depth

**What it measures:** Did the skill push past the first vague pass? Thin
material ("it grew a ton", "I helped lots of people") should trigger the
stage's probes (worst moment, key move, exact number, which rung does what).
A skill that saves the first pass is a 1. A skill that loops 2 to 3 rounds,
then either gets specifics or honestly flags the entry as thin, is a 4 to 5.

### 2. voice_preservation

**What it measures:** Does the entry sound like the creator said it? The
`illustrates` / `concept` / `problem_it_solves` line, the story body, the
metaphor text, the testimonial quote. Check the transcript: did the skill run
the read-aloud test and edit to match the creator's phrasing, or did it polish
the creator's words into generic prose? Verbatim quote handling on
testimonials is all-or-nothing: any paraphrase or grammar cleanup caps this
at 1.

### 3. gap_honesty

**What it measures:** On adversarial and thin cases, did the skill flag gaps
visibly (TODO in the entry or session close, "no story here yet") instead of
papering over them? A gut call labeled as a gut call scores higher than a
confident-sounding entry built on nothing. Any invented number, client detail,
or bank link is an automatic 1.

### 4. bank_hygiene

**What it measures:** Judgment on the bank as a system, beyond schema
correctness (Tier A covers that). Dedup: did the skill surface the existing
entry and offer update / new angle / merge? People: did named clients get
stubs without being asked? Slug and tags: would a future writing skill
actually find this entry? Read-aloud on the framework NAME specifically (Stage
F requires it).

## Output format

Return JSON only:

```json
{
  "per_case": [
    {
      "case": "case_00",
      "slug": "systems-beat-hustle",
      "scores": {
        "dig_deeper_depth": 4,
        "voice_preservation": 4,
        "gap_honesty": 5,
        "bank_hygiene": 4
      },
      "average": 4.25,
      "reasoning": "one or two sentences, concrete, cite the phrase or move that drove the score"
    }
  ],
  "dimension_averages": {
    "dig_deeper_depth": 0.0,
    "voice_preservation": 0.0,
    "gap_honesty": 0.0,
    "bank_hygiene": 0.0
  },
  "quality_score": 0.0
}
```

`quality_score` is the mean of all dimension scores across all scored cases,
normalized to 0 to 1 (divide the 1 to 5 average by 5). This is the single
number the optimizer reads.
