# vid-structure Tier B Rubric (AI judge)

DO NOT MODIFY during an autoresearch loop. This is the locked rubric. You are a
fresh judge with no memory of prior iterations. Score only what is in front of
you, against this rubric. Be consistent and a little stingy: a 5 is rare.

Only run Tier B on cases that already passed Tier A. If a case failed Tier A,
do not score it: the mechanical floor was not met.

## What you receive per case

- `script.md`, the skeleton (intro stub, one body section per point with its
  picked parable and principle, ending stub, ## To build list, CUTS comment)
- `piece.md` (updated frontmatter: segment_purposes, tension_plan, status)
- `transcript.md`, the spine + plan lock conversation
- the `seed` object (ground-truth material, `is_adversarial`,
  `bank_pulls_allowed`, `fabrication_traps`)
- the after-framing fixture the skill consumed (`fixtures/{slug}/piece.md`)
- the after-intake `brain-dump.md` for this slug
- the skill's own craft references:
  `.claude/skills/vid-structure/references/brain-dump-mining.md` and
  `knowledge/parable-decision-matrix.md`

## Read first (calibrate here)

Read the mining reference's worked example and the parable decision matrix
before scoring. The bar is not "is the outline tidy." The bar is: the writer
(vid-segment) picks this up and writes without re-planning, and the order
keeps a viewer to the payoff.

## Dimensions (score each 1 to 5)

### 1. mining_fidelity

**What it measures:** The points are the brain-dump's real material, filtered
against the locked angle. Main points stand alone, subpoints sit under their
parent, combines keep the sharper phrasing and the unique material, tangents
are logged as cuts. No padding to hit a count, no force-fit into the format.

| Score | Description |
|-------|-------------|
| 1 | Points invented or force-fit; tangents silently dropped or kept as points. |
| 2 | The right points but flattened: combines destroyed material, or a tangent padded into a section. |
| 3 | Points trace to the dump and cuts are logged, but a subpoint got promoted to a section it cannot carry. |
| 4 | Clean mining: every section is material-anchored, cuts logged with reasons, count honest. |
| 5 | All of 4, and the mining surfaced a non-obvious connection the dump implied but did not spell out. |

### 2. payoff_ordering

**What it measures:** The title's promise pays off late, past the midpoint,
and the tension_plan says where. Threads (a setup in one point paid off in a
later one) are named. The order serves retention, not the dump's original
sequence.

| Score | Description |
|-------|-------------|
| 1 | Payoff in point 1, or no discernible order logic; tension_plan is a restated topic list. |
| 2 | Some order logic but the title's answer lands at or before the midpoint. |
| 3 | Payoff lands late and is marked, but threads are unnamed or the central question is missing. |
| 4 | Payoff late and marked, central question stated, at least one real thread named. |
| 5 | All of 4, and the order choice is argued from the material (why THIS point carries the payoff), not just declared. |

### 3. plan_completeness_craft

**What it measures:** Per point, the writer needs nothing re-planned. The
parable type fits the point's problem per the decision matrix, the specific
material is named (bank link, dump material, or an honest to-build), the
principle is the actual lesson in the creator's register, and proof is linked
or flagged. On adversarial seeds, full marks REQUIRE the gap to stay a named
gap.

| Score | Description |
|-------|-------------|
| 1 | Blocks surfaced as menus or missing; on an adversarial seed, the gap got filled. |
| 2 | Picks made but generic: same parable type on every point, principles that describe rather than teach. |
| 3 | Picks made and material named, but one parable type clearly fights its point's problem. |
| 4 | Every point carries type + material + lesson + proof-or-gap; types vary and fit. |
| 5 | All of 4, and the plan spends bank material exactly where belief is needed and flags everything else lean. |

### 4. conversation_economy

**What it measures:** The creator saw two proposals (spine, then built plan)
and one confirmation. Machinery stayed invisible: no phase talk, no mining
worksheets. Cuts were surfaced, not dropped silent. A format mismatch, if the
material forced one, was proposed rather than jammed through.

| Score | Description |
|-------|-------------|
| 1 | Phase narration, worksheet dumps, or the format silently force-fit. |
| 2 | Right proposals but padded with process talk; or cuts mentioned with no reasons. |
| 3 | Two proposals and a confirm, but the spine arrived pre-built-out (no chance to shape it cheaply). |
| 4 | Clean two-proposal flow, cuts logged with reasons, confirm line carries the handoff facts. |
| 5 | All of 4, and the proposals read like a sharp editor thinking with the creator, not a form being filled. |

## Output format

Return JSON only:

```json
{
  "per_case": [
    {
      "case": 0,
      "slug": "5-onboarding-mistakes",
      "scores": {
        "mining_fidelity": 4,
        "payoff_ordering": 4,
        "plan_completeness_craft": 5,
        "conversation_economy": 4
      },
      "average": 4.25,
      "reasoning": "one or two sentences, concrete, cite the specific line that drove the score"
    }
  ],
  "dimension_averages": {
    "mining_fidelity": 0.0,
    "payoff_ordering": 0.0,
    "plan_completeness_craft": 0.0,
    "conversation_economy": 0.0
  },
  "quality_score": 0.0
}
```

`quality_score` is the mean of all dimension scores across all scored cases,
normalized to 0 to 1 (divide the 1 to 5 average by 5). Per-dimension averages
tell the optimizer where to spend the next iteration.
