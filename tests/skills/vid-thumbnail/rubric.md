# vid-thumbnail-v2 Tier B Rubric (AI judge)

DO NOT MODIFY during an autoresearch loop. This is the locked rubric. You are a
fresh judge with no memory of prior iterations. Score only what is in front of
you, against this rubric. Be consistent and a little stingy: a 5 is rare.

## What you receive per case

- `piece.md` with exactly three aligned `thumbnail_text` and `thumbnail_shape` values locked
- `transcript.md`, the full thumbnail-text conversation (the shown package
  lives here: the title line plus exactly ten numbered options and the
  creator's three selections)
- the `seed` object (ground-truth material, `is_adversarial`,
  `bank_pulls_allowed`, `fabrication_traps`)
- the after-title stage files for this slug (locked title + framing fields in
  piece.md, material in brain-dump.md)
- `.claude/skills/vid-thumbnail-v2/references/title-thumbnail-calibration.md`
  (the mandatory real-pair calibration set)
- `knowledge/thumbnail-text-patterns.md` (the craft standard: the 5 patterns,
  the anti-patterns, the title-pairing rules, the examples library)

Only run Tier B on cases that already passed Tier A.

## Calibration (do this first)

Read the V2-owned title-thumbnail calibration reference first. Then read the
"Quick example: same video, full-spectrum option set" section and the four
pairing patterns (A through D) in thumbnail-text-patterns.md. The real pairs
set the semantic package bar without supplying formulas or facts. Judge ten
options shaped from THIS video's material, each creating a meaningful learning
signal, with three creator-selected tests saved verbatim. Shared title words
are allowed when the combined package gives the right viewer a stronger reason
to click.

## Dimensions (score each 1 to 5)

### 1. click_pull

**What it measures:** Does each shown option make the ideal buyer think
what, why, or how? Curiosity or clickable provocation the video honors
(patterns file hard rule 3). Penalize spoilers that pre-deliver the
resolution, true-but-inert facts, unsupported scarcity, unexplained tool names,
implementation caveats, standalone labels, and soft imperatives (CONSIDER,
TRY, LEARN). A fact, warning, exception, tool, setup detail, or problem earns
credit only when the title-plus-thumbnail pair creates a clear hook.

| Score | Description |
|-------|-------------|
| 1 | No option pulls a click. Labels, spoilers, or filler. |
| 3 | Several options pull, but the ten include visible dead weight. |
| 5 | Every shown option earns its place in the decision set. |

### 2. package_pairing

**What it measures:** Does each option, beside this exact title, give the right
viewer a stronger reason to click? It may reinforce, complicate, prove, or
create a question, and its tone may match or productively contrast. Shared
words are neutral. Judge semantic pairing, not literal overlap. Truth and
specificity are necessary but do not rescue a pair that gains no clarity,
curiosity, proof, force, or compelling expectation.

| Score | Description |
|-------|-------------|
| 1 | Options merely echo the title, fight its tone, or add no reason to click. |
| 3 | Pairing works but is flat: the text adds information without making the exact package more clickable. |
| 5 | Title plus text together create more curiosity than either alone, in the same emotional register. |

### 3. material_grounding

**What it measures:** Is every option shaped from THIS video's actual
material (numbers verbatim from the brain dump, named systems, the dramatic
moment), and distinctive to this story rather than the niche (rule 5:
"BOTTLENECK" fails, "BACKWARDS" passes)? Generic niche text and invented
material both score low. On adversarial seeds, score the discipline of
building pull with zero numbers.

| Score | Description |
|-------|-------------|
| 1 | Generic thumbnail lines that would fit 100 other videos, or material the creator never said. |
| 3 | Real material, but the strongest asset in the dump went unused. |
| 5 | The set mines the dump's best assets, numbers land verbatim, and each text signals this specific story. |

### 4. set_discipline

**What it measures:** The decision and save flow. Exactly ten strong,
meaningfully distinct options are shown. The creator chooses exactly three,
and those three save verbatim with aligned measurement labels. Patterns are
optional private lenses, never a quota.

| Score | Description |
|-------|-------------|
| 1 | Wrong shown or saved count, cosmetic variants, padding, or unchosen options saved. |
| 3 | Ten options and three saved, but the decision set clusters or carries filler. |
| 5 | Ten strong distinct options are shown, and exactly the creator's three choices save with aligned labels. |

### 5. conversation_economy

**What it measures:** This is a conversation, not a document. Short messages.
The package is the title plus exactly ten numbered lines, each with one short
useful description. No pattern names, research notes, self-grading, or source
material pasted at the creator. Selection is one clear question and the save
confirmation is one line.

| Score | Description |
|-------|-------------|
| 1 | Essay-mode. Rationale dumps, lecture material, or options the creator cannot scan. |
| 3 | Scannable package, but wrapped in justification the creator did not ask for. |
| 5 | The creator scans ten options, chooses three, and gets one clean save confirmation. |

## Output format

Return JSON only:

```json
{
  "per_case": [
    {
      "case": 0,
      "slug": "systems-beat-hustle",
      "scores": {
        "click_pull": 4,
        "package_pairing": 4,
        "material_grounding": 4,
        "set_discipline": 4,
        "conversation_economy": 4
      },
      "average": 4.0,
      "reasoning": "one or two sentences, concrete, cite the specific line that drove the score"
    }
  ],
  "dimension_averages": {
    "click_pull": 0.0,
    "package_pairing": 0.0,
    "material_grounding": 0.0,
    "set_discipline": 0.0,
    "conversation_economy": 0.0
  },
  "quality_score": 0.0
}
```

`quality_score` is the mean of all dimension scores across all scored cases,
normalized to 0 to 1 (divide the 1 to 5 average by 5).
