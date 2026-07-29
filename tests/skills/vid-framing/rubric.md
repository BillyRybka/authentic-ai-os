# vid-framing Tier B Rubric (AI judge)

DO NOT MODIFY during an eval loop. This is the locked rubric. You are a fresh
judge with no memory of prior iterations. You do not know how many times the
skill has been edited or which version this is. Score only what is in front of
you, against this rubric. Be consistent and a little stingy: a 5 is rare.

## What you receive per case

- `piece.md` the skill produced (framing-appended version, includes dropped frames)
- `transcript.md`, the full framing conversation
- the `seed` object (the creator's ground-truth material and persona, including
  `is_adversarial`, `bank_pulls_allowed`, and `fabrication_traps`)
- the after-intake `brain-dump.md` for this slug (the upstream output the skill
  consumed)
- the shared foundation: `creator-foundation.md` (avatar, iceberg, pillars) and
  `reference-pieces/youtube-script.md` (the creator's real voice)

Only run Tier B on cases that already passed Tier A. If a case failed Tier A, do
not score it: the mechanical floor was not met.

## What this skill is trying to do

It turns one captured topic into one chosen video. It holds the material still
and points it at eight different viewer wants, the creator picks one, and only
then does it write the read of the person that want belongs to.

Two consequences for scoring:

- **The frame describes the video from outside it.** "A video that shows agency
  owners how to stop finding out a project slipped on the day it was due."
  It is not a spoken line, not a thesis, and not a headline. Penalising a frame
  for not sounding clickable is wrong; that is vid-title's job. Penalising it for
  sounding like a title is correct.
- **The read comes after the pick, not before.** A read written before the
  creator chose anything means the skill decided the video by itself.

## Read-aloud anchor (calibrate voice here first)

Before scoring, read two passages from `reference-pieces/youtube-script.md` out
loud in your head. That is the creator at a 5 for voice. Judge the payoff and the
read by ear against those passages. The frame is descriptive prose and is judged
on plainness, not on cadence.

## Dimensions (score each 1 to 5)

### 1. real_choice

**What it measures:** did the creator get a genuine choice between different
videos, or a menu of one idea reworded?

Read the eight frames in the transcript and ask of each pair: do these answer
different viewer wants, or the same want in different words? Wording variety is
not the test. Eight frames that all promise "save time" are one frame, however
distinct they read. Also check that the recommendation carried a reason grounded
in the material rather than taste, and that the frames stayed inside what the
brain-dump can actually support.

| Score | Description | Example |
|-------|-------------|---------|
| 1 | No options offered. One frame proposed and taken, or the frames are transparently the same idea renumbered. | Three frames, all "stop wasting time on X." |
| 2 | Options offered but most collapse into two or three real wants, or several promise things the material cannot deliver. | Eight frames, five of which are time-saving. |
| 3 | Most frames answer distinct wants, with one or two duplicates left in. Recommendation present but justified by preference rather than by material. | "I'd go with 4, it's the strongest." |
| 4 | Eight frames, eight distinct wants, every one supported by something actually in the dump. The recommendation names why, and the reason points at specific material. | "I'd take 6. It's the only one that uses the three dead trackers, and that's the part nobody else can film." |
| 5 | All of 4, plus at least one frame the creator would not have arrived at alone, and the recommendation argues the ceiling rather than the safest option. Where the creator offered their own angle, it was converted into a frame and weighed on the merits rather than adopted or dismissed. | Creator says "just a walkthrough"; the skill puts it in as option 1 written as a frame, then argues for a different one on material grounds. |

### 2. frame_quality

**What it measures:** is the chosen `frame` a real direction for a video, in the
right shape?

A strong frame names who it is for and what changes for them, is specific enough
that it could not be swapped onto another video in the category, and keeps the
mechanism in its right place. A delivery mechanism (something nobody searches for
by name) inside the frame is a defect. A draw mechanism (something with its own
search demand this week) at the front of the frame is correct.

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Wrong shape: a headline, a spoken line, or a description of what happens in the video. | "You don't have a tracking problem, you have a maintenance problem." |
| 2 | Right shape but generic. Names a category, not a video. Swap the creator out and nothing changes. | "A video that shows business owners how to be more organised." |
| 3 | A real direction, specific enough to be one video, but the audience or the change is loosely drawn, or a delivery mechanism has crept into the wording. | "A video that shows owners how to use Notion to keep track of projects." |
| 4 | Names the specific viewer and the specific change, tied to this creator's material. Mechanism sits where its kind belongs. Points clearly at the core payoff. | "A video that explains why every project tracker they've built got abandoned within a month, and what the ones that survive do differently." |
| 5 | All of 4, and the frame is one nobody else in the niche could make, because it runs on material only this creator has. Reading it, the obvious version of this topic now looks like a mistake. | The frame depends on the creator's three abandoned trackers, and no competitor has that. |

### 3. the_read

**What it measures:** did the skill write a real person, pointed at the frame
that was actually chosen?

Three fields, third person: **Target** (who this is for and the situation, as one
causal chain ending on a cost), **Transformation** (they stop doing X and do Y
instead, plus what that gets them), **Stakes** (each consequence causing the next,
the misattribution named near the end, landing back where Target started).

Two lane rules matter. Target describes the situation and stops; the compounding
belongs to Stakes. And Target is a chain, not a form: "their goal is / their
challenge is / their pain point is" is a defect even when every fact in it is
correct.

| Score | Description | Example |
|-------|-------------|---------|
| 1 | No read, or a generic summary of the topic with no named cost. | "The viewer wants to be more productive." |
| 2 | Fields present but surface-level. Restates the seed without naming what they are stuck on. Stakes are a single sentence of consequence. | "They want systems and don't have them. If they don't fix it they'll stay busy." |
| 3 | All three present and plausible, but one is doing another's job (consequences inside Target), or Stakes state one consequence instead of compounding, or Target is written as a filled-in form. | "Their goal is X. Their challenge is Y." Every fact right, reads like a template. |
| 4 | Target runs as a causal chain and ends on a cost. Transformation is directional with what they leave with. Stakes compound through at least three linked consequences and name what the viewer blames instead. Everything points at the chosen frame. | "So they add another rule. The instruction file gets longer and the tells keep landing, because an instruction is a request and nothing is checking the output against it." |
| 5 | All of 4, and the three run as one piece: Target ends on a cost, Stakes compounds that exact cost, and the last line of Stakes lands back on what Target opened with. The final consequence is one the viewer would never trace to the cause. | "It reads like a discipline problem, so they write a process doc nobody reads, when the real problem is a board that asked people to do a second job." |

### 4. grounding_honesty

**What it measures:** when the skill claimed a pattern, a number, or a bank entry,
was it real? When the material was thin or the creator withheld proof, did it say
so and flag the gap instead of inventing? On adversarial seeds
(`is_adversarial: true`), full marks REQUIRE zero fabricated numbers and zero bank
links the seed did not authorise.

This dimension penalises two failure modes: inventing something to make a frame
sound proven, and implying grounding without naming it. A gut call flagged as a
gut call scores higher than a fabricated citation. Frames that were offered and
not picked are in scope: an invented result in option 5 is still an invention.

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Claimed a specific outlier, view count, result, or bank entry that is not in `bank_pulls_allowed` or does not exist in the frozen fixtures. On an adversarial seed, invented a number the creator withheld. | Cited "[[story-bank/jordan-coaching-win]]" on the `tempting-numbers-client-story` seed. |
| 2 | No outright fabrication, but implied grounding without naming it, or offered a frame promising a result the material cannot support. | "Research shows this kind of angle performs well in your niche." |
| 3 | Real entries named where available, but where the material was thin, left it vague rather than stating the gap. | Named the metaphor bank entry correctly, then said "there are patterns supporting this" without naming one. |
| 4 | Real entries named with specific detail where available. Where the material was thin or the seed adversarial, the gap was stated plainly rather than filled. | "No pattern entry exists for pricing; treat this as a gut pick and flag it until vid-research runs." |
| 5 | All of 4, and every withheld proof point landed as a `> [!todo]` in the body with a reason the creator can act on. Zero fabricated numbers or links anywhere in the case, including in frames that lost. | Adversarial seed: no invented revenue figure, no invented bank link, each gap labelled. |

### 5. voice_read_aloud

**What it measures:** does piece.md read like the creator in
`reference-pieces/youtube-script.md`?

Judge `core_payoff` and the three read fields. Does the payoff name a concrete
deliverable in plain words? Does the read carry the creator's tone without
slipping into brochure copy, or into writerly constructions the creator would
pause and reword?

Three specific tells to weigh: a description used where a plain noun exists
("a check that flags banned words and makes the model fix them" instead of
"autocorrect"), three fresh images stacked where one would land, and a cost
reported from a distance rather than put in front of the reader.

`core_payoff` states what the viewer will have after watching, in second person.
It is not an instruction ("pick one task and write down every step") and not a
benefit claim ("save hours every week").

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Corporate, polished, AI-flavored. You would never hear this from a real person. | "Leveraging a systemic framework to empower delegation capacity." |
| 2 | Mostly plain but carries at least one phrase the creator would reword on camera, or reads like it was written to impress. | "The reading is the real tax." |
| 3 | Plain, avoids the worst tells, but lacks the creator's cadence. Could belong to a generic business channel. Or a plain noun was available and a description got used instead. | "How to stop being the bottleneck in your business." |
| 4 | Reads close to the creator. Plain verbs, no hedging, one image per field, the cost put in front of the reader. You would not be surprised to hear it in the transcript. | "They read every line of every draft before it goes out, and the ones they were too fried to read went out anyway, under their name." |
| 5 | Reads exactly like the creator. Phrasing, rhythm, and bluntness match the reference pieces, and the sentences shorten as the stakes escalate. You would hear it in their mouth without rewriting a word. | "Good week, they catch it. Bad week, it goes out anyway." |

## Output format

Return JSON only:

```json
{
  "per_case": [
    {
      "case": 0,
      "slug": "systems-beat-hustle",
      "scores": {
        "real_choice": 4,
        "frame_quality": 4,
        "the_read": 4,
        "grounding_honesty": 5,
        "voice_read_aloud": 4
      },
      "average": 4.2,
      "reasoning": "one or two sentences, concrete, cite the specific phrase or move that drove the score"
    }
  ],
  "dimension_averages": {
    "real_choice": 0.0,
    "frame_quality": 0.0,
    "the_read": 0.0,
    "grounding_honesty": 0.0,
    "voice_read_aloud": 0.0
  },
  "quality_score": 0.0
}
```

`quality_score` is the mean of all dimension scores across all scored cases,
normalised to 0 to 1 (divide the 1 to 5 average by 5). This is the single number
the optimizer reads. Per-dimension averages say where to spend the next
iteration: a 2.5 on `real_choice` means the rotation is producing synonyms, a 2.5
on `grounding_honesty` on an adversarial seed means fabrication is leaking.
