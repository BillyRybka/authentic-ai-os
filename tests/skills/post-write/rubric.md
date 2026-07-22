# post-write Tier B Rubric (AI judge)

DO NOT MODIFY during an autoresearch loop. This is the locked rubric. You are a
fresh judge with no memory of prior iterations. You do not know how many times
the skill has been edited or which version this is. Score only what is in front
of you, against this rubric. Be consistent and a little stingy: a 5 is rare.

## What you receive per case

- `post.md`, the note the skill produced: a `## Core` piece plus `## Publishable:
  <platform>` blocks (LinkedIn, Instagram carousel, Instagram caption) and a
  `## Provenance` block
- `transcript.md`, the full repurpose conversation
- the `seed` object (the creator's ground-truth material and persona)
- the foundation: `creator-foundation.md` (iceberg, Top 3 problems) and
  `reference-pieces/youtube-script.md` (the creator's real voice)

Only run Tier B on cases that already passed Tier A. If a case failed Tier A, do
not score it, the mechanical floor was not met.

## Read-aloud anchor (calibrate voice here first)

Before scoring, read two passages from `reference-pieces/youtube-script.md` out
loud in your head. That is the creator at a 5. Blunt, plain, direct, talks like a
person. Sterile, polished, generic business writing is a 1. Judge voice by ear
against those passages, never against abstract adjectives.

## Dimensions (score each 1 to 5)

### 1. voice_fidelity

Does the post sound like Sam talking, or like a generic content account? The
core and the platform versions should carry the creator's blunt, plain register
and their distinctive phrases, not smoothed-out marketing prose.

| Score | What it looks like |
|---|---|
| 1 | Generic LinkedIn-influencer voice. None of the creator's grain. |
| 2 | A couple of real phrases survive, but most is smoothed into generic prose. |
| 3 | Recognizably on-topic but flattened, some voice lost. |
| 4 | The creator's words and cadence are mostly intact, distinctive phrases preserved. |
| 5 | Reads like the creator wrote it. Their phrasing, rhythm, and bluntness are on the page. Nothing they would reword. |

### 2. commitment_no_hedging

Use the definition in `.claude/skills-wip/post-write/references/ai-hedging.md`. Score how willing the post is to
take and hold a position. Penalize the underlying move of non-commitment (claims
dissolved by qualifiers, positions raised and never answered, reflex both-sides,
vague unfalsifiable takeaways), NOT the presence of any soft word. Do not penalize
committed conversational voice ("I think about it like this:", "kind of like" as
an analogy, "tends to" stating a real pattern). The test: strip the soft phrase
and check if a clear, disagreeable claim remains.

| Score | What it looks like |
|---|---|
| 1 | The post never plants a flag a reader could argue with. All hedge, no claim. |
| 2 | A position is there but buried under qualifiers and both-sides balance. |
| 3 | Mostly committed, but one or two real hedges blur a key claim. |
| 4 | Takes a clear position and holds it; any soft language is tone, not retreat. |
| 5 | Sharp, committed throughout. Every claim is one a reader could disagree with, and the post owns it. |

### 3. specificity_grounded

Is the post concrete, and is the concreteness drawn from the creator's REAL
material (the seed and reveals), not invented and not generic? A specific detail
that the creator never gave is a fabrication, not a strength (Tier A catches
invented numbers; here, judge whether specificity is real and earned).

| Score | What it looks like |
|---|---|
| 1 | Generic throughout. Could be pasted under any post in the niche. |
| 2 | One vague gesture at specificity, nothing a reader could not have guessed. |
| 3 | Some real detail, but leans on general advice to fill space. |
| 4 | Anchored in the creator's actual material: a real moment, named situation, or concrete step from the seed. |
| 5 | Every post earns its specificity from the creator's real material. Sharp, concrete, and honest about what was thin. |

### 4. platform_adaptation

Did the skill write a platform-agnostic core and then genuinely ADAPT it per
platform, or did it reflow one version across all of them? Check that the core
reads as a complete standalone piece, the LinkedIn version is hook-first short
paragraphs, the carousel is decomposed so each slide carries one idea in two
short sentences or fewer (a slide with three sentences or a whole paragraph is a
fail) with a cover that earns the swipe and a text visual brief, and the caption
is a warmer single thread. A carousel forced onto an idea that is really a single
story or one belief, which should be a caption, scores lower. Same idea, different
delivery, not the same text three times, and never the core sliced at its
paragraph breaks. If the skill correctly declined to build a carousel for a single
story or one belief and delivered a strong caption instead, that is correct
behavior: judge the adaptation across the blocks that exist and do not penalize
the absent carousel.

| Score | What it looks like |
|---|---|
| 1 | The same block of text pasted under every platform. No real adaptation. |
| 2 | Minor trimming between platforms, but structurally identical. |
| 3 | Some adaptation, but one platform is just the core reflowed, or the carousel slides are wordy paragraphs instead of one idea each. |
| 4 | Each platform is genuinely shaped for its delivery; the carousel is sliced with a visual brief. |
| 5 | The core is complete and platform-agnostic, and every version is a true translation: LinkedIn argues, the carousel teaches slide by slide, the caption talks. Nothing is reflowed. |

### 5. one_idea_clarity

Does each post make exactly one clear point? You should be able to state the
single takeaway in one sentence. A post that tries to teach three things at once
scores low.

| Score | What it looks like |
|---|---|
| 1 | Several ideas crammed together, no single point. |
| 2 | One main idea, but cluttered with tangents. |
| 3 | One idea, but the takeaway is fuzzy. |
| 4 | One clear point, stated cleanly. |
| 5 | One sharp point, every line serving it, an obvious one-sentence takeaway. |

### 6. hook_strength

Does the first line earn the read? On social the opener decides whether anyone
sees the rest, so a flat first line sinks an otherwise good post. A strong hook
faces the reader (a belief they hold, a pain they feel, a thing they are doing
wrong) and opens a gap they have to keep reading to close. A weak hook faces the
subject (introduces a character, a topic, or a scene) and reads as information.
Judge the first line of the core AND of each platform version. A story that opens
"So-and-so did X" is subject-facing and scores low even when the rest is strong.

| Score | What it looks like |
|---|---|
| 1 | Flat, subject-facing openers throughout ("Marcus ran an agency", "Today I want to talk about X"). No gap, no reason to read on. |
| 2 | Opener states a topic or a fact. Faintly relevant, but nothing is at stake for the reader. |
| 3 | One version hooks, the others open flat, or the hook gestures at tension without really opening a gap. |
| 4 | Most openers face the reader and open a gap. The first line earns the second. |
| 5 | Every version opens on the reader with a real gap. You cannot not read line two. The story comes in as proof, never as the doorway. |

## Output format

Return JSON only:

```json
{
  "per_case": [
    {
      "case": 0,
      "slug": "systems-beat-hustle",
      "scores": {
        "voice_fidelity": 4,
        "commitment_no_hedging": 5,
        "specificity_grounded": 4,
        "platform_adaptation": 4,
        "one_idea_clarity": 5,
        "hook_strength": 3
      },
      "average": 4.17,
      "reasoning": "one or two sentences, concrete, cite the specific phrase or move"
    }
  ],
  "dimension_averages": {
    "voice_fidelity": 0.0,
    "commitment_no_hedging": 0.0,
    "specificity_grounded": 0.0,
    "platform_adaptation": 0.0,
    "one_idea_clarity": 0.0,
    "hook_strength": 0.0
  },
  "quality_score": 0.0
}
```

`quality_score` is the mean of all dimension scores across all scored cases,
normalized to 0 to 1 (divide the 1 to 5 average by 5). This is the single number
the optimizer reads. Per-dimension averages tell the optimizer where to spend the
next iteration (a 3.0 on voice_fidelity means focus there).
