# vid-thumbnail Tier B Rubric (AI judge)

DO NOT MODIFY during an autoresearch loop. This is the locked rubric. You are a
fresh judge with no memory of prior iterations. Score only what is in front of
you, against this rubric. Be consistent and a little stingy: a 5 is rare.

## What you receive per case

- `piece.md` with `thumbnail_text` + `thumbnail_shape` locked
- `transcript.md`, the full thumbnail-text conversation (the shown package
  lives here: the title line plus the numbered candidates)
- the `seed` object (ground-truth material, `is_adversarial`,
  `bank_pulls_allowed`, `fabrication_traps`)
- the after-title stage files for this slug (locked title + framing fields in
  piece.md, material in brain-dump.md)
- `knowledge/thumbnail-text-patterns.md` (the craft standard: the 5 patterns,
  the anti-patterns, the title-pairing rules, the examples library)

Only run Tier B on cases that already passed Tier A.

## Calibration (do this first)

Read the "Quick example: same video, full-spectrum option set" section and the
four pairing patterns (A through D) in thumbnail-text-patterns.md. That is the
bar: candidates shaped from THIS video's material, each carrying a different
hook than the title, every one a real option a creator would test.

## Dimensions (score each 1 to 5)

### 1. click_pull

**What it measures:** Does each shown candidate make the ideal buyer think
what, why, or how? Curiosity or clickable provocation the video honors
(patterns file hard rule 3). Penalize spoilers that pre-deliver the
resolution, labels instead of hooks ("THE 12-SOP RULE" failure mode), and soft
imperatives (CONSIDER, TRY, LEARN).

| Score | Description |
|-------|-------------|
| 1 | No candidate pulls a click. Labels, spoilers, or filler. |
| 3 | Some candidates pull, but at least one shown option is dead weight. |
| 5 | Every shown candidate earns its spot. Cutting any one would hurt. |

### 2. package_pairing

**What it measures:** Do the title and each candidate work as ONE package?
Each carries a different hook (pairing patterns A-D), the tone matches or
productively contrasts (rule 4), and no candidate repeats the title's hook.
A positive-result text against a failure-framed title is a tone clash.

| Score | Description |
|-------|-------------|
| 1 | Candidates restate the title or fight its tone. Two hooks collapse into one beat. |
| 3 | Pairing works but is flat: the text adds information, not a second hook. |
| 5 | Title plus text together create more curiosity than either alone, in the same emotional register. |

### 3. material_grounding

**What it measures:** Is every candidate shaped from THIS video's actual
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

**What it measures:** The shape of the shown set. 3-5 candidates ranked
strongest first, spread across at least 3 of the 5 patterns (no clustering),
no padded or self-flagged weak options, no anti-patterns. If only survivors
are shown, the filtering was done right.

| Score | Description |
|-------|-------------|
| 1 | Padded list, one-pattern cluster, or candidates shown with their own caveats. |
| 3 | Right count and ranking, but the set leans on one pattern or carries a filler option. |
| 5 | Tight ranked set, real pattern spread, every option a survivor. |

### 5. conversation_economy

**What it measures:** This is a conversation, not a document. Short messages.
The package shown as the title plus numbered lines, each line the text in
quotes plus its pattern name, nothing else. No rationale paragraphs, no
self-grading, no reference material pasted at the creator. The pick step is
one question, the save is one line.

| Score | Description |
|-------|-------------|
| 1 | Essay-mode. Rationale dumps, lecture material, or options the creator cannot scan. |
| 3 | Scannable package, but wrapped in justification the creator did not ask for. |
| 5 | The creator scans and picks in seconds. Every message earns its pixels. |

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
