# vid-title Tier B Rubric (AI judge)

DO NOT MODIFY during an autoresearch loop. This is the locked rubric. You are a
fresh judge with no memory of prior iterations. You do not know how many times
the skill has been edited or which version this is. Score only what is in front
of you, against this rubric. Be consistent and a little stingy: a passing score
requires the criterion to be clearly met, not arguably met.

## What you receive per case

- `titles.md`, the note the skill produced: YAML frontmatter (slug,
  locked_title, locked_bens), a `## Candidates` section (5-8 numbered
  candidates, each annotated with pattern, BENS, and char count), and a
  `## Recommendation` section (1-2 sentences naming the pick and why)
- `transcript.md`, the full reasoning trace showing the divergent pass,
  convergent cut, and creator exchange
- The frozen fixture for this case: `piece.md` (format, pillar, locked angle)
  and `brain-dump.md` (material, lock list)
- The creator's banks: `title-bank.md` (9 named patterns) and
  `power-words-bank.md`
- The foundation: `creator-foundation.md` (avatar, Top 3 problems) and
  `voice-profile.md` (refusals and fingerprint)

Only run Tier B on cases that already passed Tier A. If a case failed Tier A,
do not score it. The mechanical floor was not met.

## Read-aloud anchor (calibrate here first)

Before scoring any case, read the `reference-pieces/youtube-script.md` passage
out loud in your head. That is Billy's voice at its clearest: short declarative
punches, direct second-person, no warm-up, no hedging. Then read two of the
title-bank worked examples aloud. Those are the shapes that feel like natural
English. Hold both in mind as your calibration when you judge whether a title
reads as one continuous human thought.

The voice refusals in `voice-profile.md` are hard guards: no em-dashes, no
AI-isms, no hedging, no neutrality. A title that violates a refusal fails the
criterion that touches it.

## Scoring system

Each criterion is scored 0 or 1 (no partial credit).
- 1 = the criterion is clearly and fully met
- 0 = the criterion is not met, or there is genuine doubt

This is binary. "Mostly yes" is a 0. Score what is in front of you.

## Criteria

### 1. reads_aloud_natural

**What it measures:** Every candidate in the set reads as one continuous human
thought said out loud, not as stitched fragments, invented compound nouns, or a
mid-title smash-up of two sentences.

**How to judge:** Say each candidate aloud in your head. A passing title sounds
like a person said the whole thing in one breath. A failing title makes you
pause mid-way, trip over an invented phrase ("unsticks 365s"), or arrive at two
grammatically separate statements forced into one line.

**Score 1 if:** Every candidate passes the read-aloud test. Not a single one
stumbles.

**Score 0 if:** Even one candidate contains a fragment smash-up ("I Tried It.
Revenue Dropped."), an invented compound that is not real English, or a
parenthetical tag-on that turns a flowing title into a stop-start structure
("My 7 Skills (Steal Them) (No Employees)").

**Calibration examples:**
- Pass: "DON'T Hire a Content Team. Use These 7 Skills Instead" reads as one
  contrarian command with a completion. One breath.
- Pass: "Claude Cowork Just Changed How Solo Creators Work" is a complete
  subject-verb-object sentence.
- Fail: "340K To 1.3M: Content System Did It (1 Year)" is three fragments plus
  a parenthetical tag-on.
- Fail: "The Babysitting-Problem Solver Cowork Dropped" has an invented
  compound noun that is not real English.

---

### 2. bank_anchored

**What it measures:** The majority of the candidate set is visibly built from
the creator's 9 named title-bank patterns, not from free-form invention. The
skill's job is to fill proven shapes with real material, not to free-style.

**How to judge:** Look at the `pattern:` annotation for each candidate. At
least 4 of the 5-8 candidates should reference a real pattern_id from
`title-bank.md` (contrarian-identity, contrarian-correction, solo-leverage,
news-jack-release, speed-mastery, better-than-masses, money-proof, steal-these,
definitive-resource). "Free-form" is allowed but it must be the minority. A set
where most candidates say "free-form" failed to build from the bank.

Check the transcript: did the divergent pass actually pull multiple patterns, or
did it stay in one shape?

**Score 1 if:** At least 4 candidates map to a real, named pattern_id, AND the
transcript shows the divergent pass pulled from multiple patterns.

**Score 0 if:** Fewer than 4 candidates cite a real pattern_id, OR the
transcript shows the divergent pass was effectively free-form invention with
pattern labels retrofitted after the fact.

**Calibration examples:**
- Pass (6 candidates): contrarian-correction, solo-leverage, speed-mastery,
  steal-these, news-jack-release, contrarian-identity. Six real shapes.
- Fail (5 candidates): free-form, free-form, free-form, contrarian-correction,
  free-form. One real pattern in five.

---

### 3. specific_unrepeatable

**What it measures:** The locked title carries at least one concrete specific
from the case's lock list that makes it impossible to paste onto a different
video. Generic titles that could front any video in the niche fail this test.

**How to judge:** Read the locked_title. Ask: "Could this title front a
different video about the same general topic?" If yes, it is generic. If the
title contains a specific from the lock list (a dollar figure, a count, a named
tool, a named feature, a specific timeframe, a named outcome) that is unique to
this video's material, it passes.

Do not credit a specific that is not in the lock list. If the title says "$500K"
and the lock list has "$340K" and "$1.3M", the $500K is a fabrication, not a
specific (Tier A should have caught this; if it somehow passed, still score 0
here on specificity grounds).

**Score 1 if:** The locked title contains at least one concrete, lock-list item
that makes it uniquely tied to this video's content.

**Score 0 if:** The locked title is generic enough to paste onto any video in
the niche, OR the only "specific" is an invented one not present in the lock list.

**Calibration examples (case 00, client-340k-to-1-3m lock list: $340K, $1.3M,
1 year, 2,500 subscribers):**
- Pass: "How a 2,500-Sub Channel Went From $340K to $1.3M" contains three
  lock-list specifics. Unrepeatable.
- Pass: "$340K to $1.3M on 2,500 Subscribers (No Viral Moment)" has the arc.
- Fail: "How to Build a Content System That Converts" could front any content
  system video. No lock-list specific.
- Fail: "The $500K Content System" has an invented dollar figure.

**Calibration examples (case 02, claude-cowork-newsjack: NO numbers in lock
list):**
- Pass: "Claude Cowork Just Dropped Scheduled Agents" names the exact release
  and feature. The named items are in the lock list.
- Fail: "Claude Cowork Now Saves 3 Hours a Week" invents a time-saving number.

---

### 4. avatar_format_fit

**What it measures:** The locked title hooks one of the avatar's Top-3 problems
AND fits the case format's natural BENS bias. Both conditions must hold.

**How to judge:**

Avatar's Top-3 problems (from creator-foundation.md):
1. "My AI content sounds like AI, and the slop is breaking trust."
2. "I am prompting my way through everything instead of building real systems."
3. "I keep refining the system instead of posting, and I am not sure it is
   even authentic to me."

Also in scope: the reach myth (the belief you need a big audience to earn).
The piece.md for each case names the avatar problem in play.

Format BENS bias (from SKILL.md and packaging-system.md):
- Case Study: S + B (specific receipts plus transformation size)
- Listicle: E + N (numbered and digestible, fresh tools or approach)
- News: N + B (timely, stakes for how you work)

The locked_bens field shows what the skill annotated. Judge whether it actually
fits the format's bias, not just whether the annotation says the right letters.

**Score 1 if:** The locked title clearly speaks to the case's avatar problem
(as named in piece.md) AND its primary BENS weight matches the format's natural
bias. Both must be true.

**Score 0 if:** The title misses the avatar problem (it answers a different
fear than the one the video addresses), OR the BENS weight is out of alignment
with the format (e.g. a Listicle locked on S with no E, a News title locked on
E with no N).

**Calibration examples:**
- Case 00 (Case Study, reach-myth problem, BENS bias S+B): "How a 2,500-Sub
  Channel Went From $340K to $1.3M" hits the reach myth (small channel, big
  result) and is anchored on S (specific receipts) and B (transformation size).
  Score 1.
- Case 00: "Build a Content System That Converts Your Audience" misses the
  reach-myth hook and has no S or B weight. Score 0.
- Case 02 (News, time-problem, BENS bias N+B): "Claude Cowork Just Dropped
  Scheduled Agents" is timely (N) and stakes-raising for solo workflows (B).
  Score 1.
- Case 02: "7 Ways to Use Cowork's New Feature" converts a News piece into a
  Listicle shape and has E weight, not N. Score 0.

---

### 5. set_diverse

**What it measures:** The candidate set spans genuinely different angles, not
one idea reworded across 5-8 lines. A diverse set gives the creator real
choices: different BENS weights, different avatar problems, different pattern
shapes, different specifics.

**How to judge:** Read all candidates together. If you could describe the set
as "six ways of saying the same thing," it fails. Look for: different primary
BENS letters, different pattern shapes (not just different fill words in one
template), different aspects of the video's material emphasized.

The pattern_diversity Tier A check already enforced the mechanical minimum (3
distinct patterns, no more than 2 candidates sharing a primary BENS letter).
Here you judge whether the set feels genuinely diverse in creative angle, not
just mechanically distinct.

**Score 1 if:** The set feels like distinct creative options. A creator reading
it would have a real decision to make, not just pick a phrasing they prefer.

**Score 0 if:** Most candidates are one template with different fill words, OR
the angles all hit the same avatar problem from the same direction, OR the set
reads as "one idea, six phrasings."

**Calibration examples:**
- Pass: one candidate leads with the dollar arc (B+S), one frames it as a
  contrarian system argument (N), one offers a "steal the system" angle (E),
  one uses the 2,500-sub anchor (S), one is a "why X is wrong" reversal (N).
  Different directions.
- Fail: all six candidates start with "$340K to $1.3M" and vary only in the
  trailing phrase. Same anchor, same direction, six phrasings.

---

### 6. fabrication_resistant

**What it measures:** No candidate invents a number, name, tool, or claim
absent from the lock list. For the adversarial News case this is the primary
test: the lock list has no numbers, so any digit in any candidate is a
fabrication.

**How to judge:** Read every candidate title and the locked_title. Cross-check
each specific (dollar figures, percentages, counts, timeframes, named tools,
named methods) against the lock list in brain-dump.md. If a specific is present
in a candidate but absent from the lock list, the criterion fails.

Tier A's anti_fabrication check is the mechanical gate. This criterion judges
whether the skill stayed clean across the WHOLE set, including any edge cases
Tier A's regex might miss (e.g. a named method that sounds plausible but is not
in the material).

For the adversarial case (claude-cowork-newsjack): the lock list has Claude,
Cowork, and "scheduled agents" but NO numbers. A candidate that says "cuts 3
hours a week" or "10x your output" or "in 30 minutes" invents a number the
creator explicitly refused to provide. Score 0 if any candidate does this.

**Score 1 if:** Every candidate and the locked title contain only specifics
traceable to the lock list. No invented numbers, no invented tool names, no
invented methods.

**Score 0 if:** Even one candidate contains a specific not in the lock list, OR
the adversarial case has any digit in any candidate title.

**Calibration examples:**
- Case 00 pass: all candidates use "$340K," "$1.3M," "2,500 subscribers," or
  "1 year," all of which are in the lock list.
- Case 00 fail: a candidate says "From $0 to $1.3M" when the lock list has
  $340K as the starting figure, not $0.
- Case 02 pass: "Claude Cowork Just Dropped Scheduled Agents" uses only
  named items from the lock list, no digits.
- Case 02 fail: "Cowork's New Feature Saves 2 Hours a Day" invents "2 Hours"
  which does not exist in the lock list.

## Output format

Return JSON only:

```json
{
  "per_case": [
    {
      "case": 0,
      "slug": "client-340k-to-1-3m",
      "criteria": {
        "reads_aloud_natural": 1,
        "bank_anchored": 1,
        "specific_unrepeatable": 1,
        "avatar_format_fit": 1,
        "set_diverse": 1,
        "fabrication_resistant": 1
      },
      "passed": 6,
      "reasoning": "one or two sentences, concrete, cite the specific candidate or move that determined the score"
    }
  ],
  "criteria_pass_rate": {
    "reads_aloud_natural": 0.0,
    "bank_anchored": 0.0,
    "specific_unrepeatable": 0.0,
    "avatar_format_fit": 0.0,
    "set_diverse": 0.0,
    "fabrication_resistant": 0.0
  },
  "quality_score": 0.0
}
```

`passed` is the count of criteria that scored 1 for that case (out of 6).

`criteria_pass_rate` is the fraction of cases where each criterion scored 1
(e.g. if 2 of 3 cases passed fabrication_resistant, that rate is 0.6667).

`quality_score` is the total number of 1s across all scored cases divided by
the total possible (cases_scored x 6). This is the single number the optimizer
reads. A per-criterion pass rate below 0.67 tells the optimizer where to spend
the next iteration.

One `reasoning` sentence per case. Be concrete: name the candidate or the move
that determined the score, not abstract adjectives.
