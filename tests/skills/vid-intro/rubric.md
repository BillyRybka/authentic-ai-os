# vid-intro Tier B Rubric (AI judge)

DO NOT MODIFY during an autoresearch loop. This is the locked rubric. You are a
fresh judge with no memory of prior iterations. Score only what is in front of
you, against this rubric. Be consistent and a little stingy: a 5 is rare.

## What you receive per case

- `script.md` with the locked intro written under `## Intro`
- `piece.md` with `intro_locked`, `viewer_questions`, and used tracking
- `transcript.md`, the full intro-building conversation
- the `seed` object (ground-truth material, `is_adversarial`,
  `bank_pulls_allowed`, `fabrication_traps`)
- the after-structure stage files for this slug (brain-dump, framed piece,
  outline)
- the shared foundation: `creator-foundation.md` (avatar, Top 3, credibility)
  and `reference-pieces/youtube-script.md` (the creator's real voice)

Only run Tier B on cases that already passed Tier A.

## Read-aloud anchor (calibrate voice here first)

Read two passages from `reference-pieces/youtube-script.md` out loud in your
head before scoring. That is the creator at a 5 for voice. Judge the intro as
spoken words: it will be read on camera, word for word.

## Dimensions (score each 1 to 5)

### 1. hook_strength

**What it measures:** Does the first line earn the next 30 seconds? One hook,
one type, filled from the lock list only, sayable by THIS creator. Penalize
multi-hook stacking, generic curiosity bait, topic-label openers, and hedged
hooks (hook-patterns.md anti-patterns A-2 through A-7).

| Score | Description |
|-------|-------------|
| 1 | Topic-label opener or stacked hooks. No tension, no specificity. |
| 3 | A real hook of one clear type, but generic enough to open a competitor's video. |
| 5 | One hook, one type, specific to this video's material, in the creator's voice. You would not change a word. |

### 2. question_setup_alignment

**What it measures:** Does the Setup pay off the exact Top 3 viewer questions
locked with the creator? Each clause maps to one locked question, max 3 (or the
format planner's trim), verbs are "show you" / "walk you through". News format:
score whether the compressed intro (no Setup) still signals what the viewer
gets.

| Score | Description |
|-------|-------------|
| 1 | Setup promises things the outline never delivers, or maps to no locked question. |
| 3 | Setup roughly matches the questions but a clause drifts or promises body content that is not in the outline. |
| 5 | Every clause ticks a locked question in order, the outline visibly pays each one, and the contract reads as one spoken sentence. |

### 3. credibility_weave

**What it measures:** Is the credibility line woven into a claim moment (Hook,
Problem/Result, or Setup per credibility-line-weaving.md), pulled from real
foundation or brain-dump material, and matched to the avatar's stage? Bolted-on
self-introduction is a 1 (and already a Tier A fail). Formats that skip
credibility (news) are scored on the discipline of skipping.

| Score | Description |
|-------|-------------|
| 1 | Bolted-on self-intro, or a fabricated brag. |
| 3 | Real material, but the line floats next to the claim instead of earning it. |
| 5 | The receipt arrives inside the claim moment, ties to what comes next, and the avatar can see themselves in the starting state. |

### 4. transition_forward_pull

**What it measures:** Does the Transition do both jobs (orientation cue plus
hook forward) and land on the outline's actual FIRST body point with a result
the avatar cares about? Announcement transitions ("now point one") are a 1-2.

| Score | Description |
|-------|-------------|
| 1 | Pure announcement or filler. No forward pull. |
| 3 | Signals movement but the payoff is generic ("let me show you how it works"). |
| 5 | Names the first body point's specific payoff in the avatar's language and clearly closes the intro. |

### 5. voice_read_aloud

**What it measures:** Does the assembled intro read like the creator in
`reference-pieces/youtube-script.md`? Second person, blunt, no warm-up, short
sentences that land then a longer one that explains. The whole block should
pass the read-aloud test.

| Score | Description |
|-------|-------------|
| 1 | Corporate, polished, AI-flavored. Nobody talks like this. |
| 3 | Plain but generic. Could belong to any business channel. |
| 5 | Reads exactly like the creator. You would hear it in their mouth without rewriting a word. |

## Output format

Return JSON only:

```json
{
  "per_case": [
    {
      "case": 0,
      "slug": "systems-beat-hustle",
      "scores": {
        "hook_strength": 4,
        "question_setup_alignment": 4,
        "credibility_weave": 4,
        "transition_forward_pull": 4,
        "voice_read_aloud": 4
      },
      "average": 4.0,
      "reasoning": "one or two sentences, concrete, cite the specific line that drove the score"
    }
  ],
  "dimension_averages": {
    "hook_strength": 0.0,
    "question_setup_alignment": 0.0,
    "credibility_weave": 0.0,
    "transition_forward_pull": 0.0,
    "voice_read_aloud": 0.0
  },
  "quality_score": 0.0
}
```

`quality_score` is the mean of all dimension scores across all scored cases,
normalized to 0 to 1 (divide the 1 to 5 average by 5).
