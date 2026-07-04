# vid-framing Tier B Rubric (AI judge)

DO NOT MODIFY during an autoresearch loop. This is the locked rubric. You are a
fresh judge with no memory of prior iterations. You do not know how many times
the skill has been edited or which version this is. Score only what is in front
of you, against this rubric. Be consistent and a little stingy: a 5 is rare.

## What you receive per case

- `piece.md` the skill produced (framing-appended version, includes dropped angles)
- `transcript.md`, the full framing conversation
- the `seed` object (the creator's ground-truth material and persona, including
  `is_adversarial`, `bank_pulls_allowed`, and `fabrication_traps`)
- the after-intake `brain-dump.md` for this slug (the upstream output the skill
  consumed)
- the shared foundation: `creator-foundation.md` (avatar, iceberg, pillars) and
  `reference-pieces/youtube-script.md` (the creator's real voice)

Only run Tier B on cases that already passed Tier A. If a case failed Tier A, do
not score it: the mechanical floor was not met.

## Read-aloud anchor (calibrate voice here first)

Before scoring, read two passages from `reference-pieces/youtube-script.md` out
loud in your head. That is the creator at a 5 for voice. A corporate angle
summary like "Leveraging systemic approaches to empower team efficiency" is a 1.
Judge the angle and payoff by ear against those passages.

## Dimensions (score each 1 to 5)

### 1. psychology_depth

**What it measures:** Did the skill go deep on the ONE viewer this video is for,
name their MAIN PROBLEM and the TRANSFORMATION they want, and reflect that read
back to the creator for a yes/no before building any angle?

The framing skill is psychology-first. The pattern bank grounds the angle; the
viewer read generates it. An angle built before the creator confirmed the
problem is the expensive mistake this skill exists to prevent. Check the
transcript: was the confirm gate real or skipped?

| Score | Description | Example |
|-------|-------------|---------|
| 1 | No viewer read at all. Jumped straight to angles, or the read is a generic summary of the topic with no named problem or transformation. | "This video is about systems. Your audience wants to be more productive." |
| 2 | A viewer read was attempted but it is surface-level: restates the seed without naming the actual stuck point or what changes for them. | "The viewer wants to build better systems and stop being slammed." |
| 3 | Names the viewer, a plausible problem, and a transformation, but the confirm gate was rushed or the problem is still a bit generic. The creator was not clearly given space to sharpen before angles appeared. | Viewer read present, then angles immediately followed with "does this work?" tacked on. |
| 4 | Names the ONE viewer, the main problem they are stuck on (not the surface topic), the tension underneath it, and the transformation. Creator was asked to confirm or sharpen before any angle was built. | "The person who clicks this has already tried time-blocking and it made things worse. Their problem is not that they lack a system, it is that every system they try fights how their brain works. The transformation is they stop trying to fix their discipline and start building for how they actually think. Is that the video?" |
| 5 | All of 4, plus the skill adjusted its read based on the creator's sharpening (from transcript) before moving to angles. The problem and transformation in the final piece.md trace directly to the confirmed, sharpened version, not the first draft. | Creator sharpens the problem; the skill confirms the adjusted read and names the updated core payoff; then and only then builds angles. |

### 2. angle_quality

**What it measures:** Does `selected_angle` make the known idea feel new? The
frame is the IDEA behind the video, not the clickable hook. Scoring a frame as
if it were a headline, or penalizing it for not "signaling why someone clicks,"
is wrong. That is vid-title's job. Score only whether the frame is a real
reframe (a fresh comparison or metaphor, a contrarian flip, a named system, a
visual framework, the creator's own story), specific to THIS creator's material
and THIS viewer's problem, pressing the confirmed tension, and expressible as
one clean idea a person would say out loud. A sharp, specific, feel-new idea in
the creator's plain spoken voice is a 5 even if it is not packaged as a title. A
generic restatement of the topic is a 1 regardless of how it is worded.

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Restates the topic with no reframe. Could be the subtitle of any video in the category. Does not connect to the confirmed core payoff. | "why systems beat hustle" (just names the category) |
| 2 | Hints at a reframe but stays in category language. The known idea does not feel new; swap the creator's name for any other creator and nothing changes. | "your hustle habit is actually a systems problem" (names the flip but does not land it specifically) |
| 3 | A real reframe is present, but it is still broad enough to belong to several different videos, or the connection to the confirmed tension and payoff is loose. One tighter detail would lock it. | "your brain is not broken, your system is designed for someone else's brain" (feel-new, but not yet anchored to this creator's specific material or viewer) |
| 4 | The reframe is specific to this creator's material and this viewer's confirmed problem. Makes the known idea feel new. Presses the exact tension the viewer read named. Points toward the confirmed payoff. Reads like one video, not a category. | "the system kept failing because it was built for a 40-hour week and yours is 22" (fresh comparison, locked to this creator's data, one video only) |
| 5 | All of 4, and the frame is expressed as one clean idea a person would say out loud. No headline packaging required. The reframe is so specific that restating the topic now sounds obviously wrong. | "every system you have tried was designed for someone who does not have kids at home" (spoken plain, feel-new, specific, one clean idea, passes read-aloud without needing a title wrapper) |

### 3. grounding_honesty

**What it measures:** When the skill claimed a pattern from the bank backs an
angle, did it name a real entry (real title, real channel, real view count) from
`bank_pulls_allowed`? When the bank was thin or the seed provided no proof, did
it say so and flag the gap instead of inventing? On adversarial seeds
(`is_adversarial: true`), full marks REQUIRE zero fabricated numbers and zero
bank links the seed did not authorize.

This dimension penalizes two failure modes: inventing a pattern to make the
angle sound proven, and implying grounding without naming it. A gut swing
flagged as a gut swing scores higher than a fabricated citation.

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Claimed a specific outlier, view count, or bank entry that is not in `bank_pulls_allowed` or does not exist in the frozen fixtures. On an adversarial seed, invented a number or link the creator withheld. | Cited "[[story-bank/jordan-coaching-win]]" on the `tempting-numbers-client-story` seed. |
| 2 | Did not fabricate outright but implied patterns exist without naming them ("STOP titles work well for your audience"), or used hand-wavy grounding phrases rather than citing a real entry. | "Research shows this type of angle performs well in your niche." |
| 3 | Named real bank entries correctly where available, but where the bank was thin, left it vague instead of stating the gap plainly. | Referenced the restaurant-kitchen metaphor bank entry correctly, then said "there are patterns supporting this angle" without naming one. |
| 4 | Named real bank entries with specific detail (title, channel, views) where available. Where the bank was thin or the seed was adversarial, stated the gap plainly ("the bank has nothing real for pricing yet; I am treating this as a gut pick") rather than inventing. | "The STOP pattern is backed by 'STOP Planning Your Week Like This' (@CoachY, 800k). No pattern entry exists for pricing; this angle is a gut pick, flag it as ungrounded until vid-research runs." |
| 5 | All of 4, and on adversarial seeds the dropped angles section shows the skill flagged each spot where the creator withheld proof as a TODO rather than papering over the gap. Zero fabricated numbers or links across the whole case. | Adversarial seed: no invented revenue figure, no invented bank link, each gap labeled as TODO with a clear reason the creator can act on later. |

### 4. voice_read_aloud

**What it measures:** Does piece.md read like the creator in `reference-pieces/youtube-script.md`?
Specifically: do `selected_angle` and `core_payoff` sound spoken and human, not
corporate? Does the dropped-angles section use the creator's plain direct tone,
not formal labels? The whole file should pass the read-aloud test Billy's brand
is built on.

This dimension is calibrated against the reference pieces. A 5 means you would
not be surprised to find these exact lines in a video the creator actually made.

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Corporate, polished, AI-flavored. You would never hear this from a real person. | selected_angle: "Leveraging a Systemic Framework to Empower Your Delegation Capacity" |
| 2 | Mostly plain but has at least one phrase the creator would reword on camera, or reads like it was written to impress rather than to communicate. | "The Bottleneck Is Documentation: A Systematic Approach to Onboarding Delegation" |
| 3 | Reads plain and avoids the worst AI tells, but lacks the creator's specific cadence: second-person, blunt, no warm-up. Could belong to a generic business channel. | "How to Stop Being the Bottleneck in Your Business" |
| 4 | Reads close to the creator's voice. Second-person where the creator uses it, plain verb choices, no hedging. You would not be surprised to hear it in the transcript. Minor word choices might be slightly off. | "You Are Still the Bottleneck Because the Steps Only Live In Your Head" |
| 5 | Reads exactly like the creator. The phrasing, rhythm, and bluntness match the reference pieces. You would hear it in the creator's mouth without rewriting a word. The core_payoff sounds like the creator giving a direct instruction, not a benefit statement. | selected_angle: "The Bottleneck Is Not You. It Is the Document That Does Not Exist Yet." / core_payoff: "Pick the one task only you can do this week and write down every step so it can run without you." |

## Output format

Return JSON only:

```json
{
  "per_case": [
    {
      "case": 0,
      "slug": "systems-beat-hustle",
      "scores": {
        "psychology_depth": 4,
        "angle_quality": 4,
        "grounding_honesty": 5,
        "voice_read_aloud": 4
      },
      "average": 4.25,
      "reasoning": "one or two sentences, concrete, cite the specific phrase or move that drove the score"
    }
  ],
  "dimension_averages": {
    "psychology_depth": 0.0,
    "angle_quality": 0.0,
    "grounding_honesty": 0.0,
    "voice_read_aloud": 0.0
  },
  "quality_score": 0.0
}
```

`quality_score` is the mean of all dimension scores across all scored cases,
normalized to 0 to 1 (divide the 1 to 5 average by 5). This is the single number
the optimizer reads. Per-dimension averages tell the optimizer where to spend the
next iteration (a 2.5 on psychology_depth means the confirm gate is broken;
a 2.5 on grounding_honesty on an adversarial seed means fabrication is leaking).
