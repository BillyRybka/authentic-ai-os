# vid-title Tier B Rubric (AI judge)

DO NOT MODIFY during an autoresearch loop. This is the locked rubric. You are a
fresh judge with no memory of prior iterations. You do not know how many times
the skill has been edited or which version this is. Score only what is in front
of you, against this rubric. Be consistent and a little stingy: a passing score
requires the criterion to be clearly met, not arguably met.

## What you receive per case

- `titles.md`, the note the skill produced: YAML frontmatter (slug,
  locked_title, locked_bens, locked_lane), a `## Claim` section (placed before
  `## Lanes`) with three labeled lines: `Claim:` (the disagreeable true thing
  the video argues), `Stake:` (what it costs the viewer to not get this), and
  `Belief:` (what the avatar currently assumes that the claim cuts against), a
  `## Lanes` section (4 to 5 lane headings, each annotated on-brand/off-brand,
  crowded/underused, and opportunity: yes/no; under each heading 1 to 2 numbered
  candidates annotated with pattern, BENS, and char count; under each heading a
  proof: line), and a `## Recommendation` section (1-2 sentences naming the
  locked lane and why)
- `transcript.md`, the full reasoning trace showing the divergent pass,
  gap analysis, convergent cut, and creator exchange
- The frozen fixture for this case: `piece.md` (format, pillar, locked angle)
  and `brain-dump.md` (material, lock list)
- The creator's banks: `title-bank.md` (9 named patterns, each with spread) and
  `power-words-bank.md`
- The gap-finder data: `pattern-bank.md` (competitor outliers, spreads, xMed
  multipliers per channel)
- The foundation: `creator-foundation.md` (iceberg, avatar, Top 3 problems)

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

### 1. makes_a_claim [PRIMARY GATE]

**What it measures:** The locked_title AND every candidate in the opportunity
lane make a CLAIM or open a loop, rather than just describing the topic. The
test: read the title and ask what the viewer's brain has to fill in. If the
answer is "nothing, it just states what the video is about," it is a label, not
a claim. Score 0.

**How to judge:** Read the locked_title and every candidate in the lane(s) marked
`opportunity: yes`. Ask of each one: does it make a point a viewer could
disagree with, or does it open a curiosity loop (an implied problem, cost,
reversal, or revelation)? The viewer must feel a reason to click beyond simply
knowing the subject. If it only announces what the video covers with no tension
for the mind to resolve, it is a label.

Anti-fabrication still applies: a claim must trace to the material. This
criterion is not license to invent a claim the video does not make.

**Score 1 if:** The locked title and the opportunity-lane candidates each make a
point a viewer could disagree with, or open a curiosity loop. The viewer's mind
has something to resolve.

**Score 0 if:** The locked title (or any opportunity-lane candidate) merely names
the subject or announces a fact with nothing the viewer's mind has to work on.
A pure product announcement, a topic label, or a factual description with no
implied tension all score 0.

**Calibration examples (case 02, claude-cowork-newsjack):**
- Fail: "Claude Cowork Just Dropped Scheduled Agents" is a pure product
  announcement. Nobody can disagree. The viewer's brain fills in nothing. Label,
  not claim.
- Pass: "Your AI Can Finally Work Without You Watching" implies you have been
  babysitting it (a claim about the viewer's current situation) and opens the
  loop "how." Same facts, same lock list, but it makes a point.
- Pass: "You're Still Babysitting Your AI (You Don't Have To)" is a direct
  claim about the viewer that opens a resolution loop.

---

### 2. reads_aloud_natural

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

### 3. bank_anchored

**What it measures:** The majority of lane titles are visibly built from the
creator's 9 named title-bank patterns, not from free-form invention. The skill's
job is to fill proven shapes with real material, not to free-style. The pattern
annotation on each candidate is the signal; the transcript shows whether the
divergent pass actually pulled multiple patterns.

**How to judge:** Look at the `pattern:` annotation for each candidate across
all lanes. At least 4 of the total 5 to 10 candidates should reference a real
pattern_id from `title-bank.md` (contrarian-identity, contrarian-correction,
solo-leverage, news-jack-release, speed-mastery, better-than-masses,
money-proof, steal-these, definitive-resource). "Free-form" is allowed but it
must be the minority. A set where most candidates say "free-form" failed to
build from the bank.

Check the transcript: did the divergent pass actually pull multiple patterns, or
did it stay in one shape?

**Score 1 if:** At least 4 candidates map to a real, named pattern_id, AND the
transcript shows the divergent pass pulled from multiple patterns.

**Score 0 if:** Fewer than 4 candidates cite a real pattern_id, OR the
transcript shows the divergent pass was effectively free-form invention with
pattern labels retrofitted after the fact.

**Calibration examples:**
- Pass (6 candidates across 4 lanes): contrarian-correction, solo-leverage,
  speed-mastery, steal-these, news-jack-release, contrarian-identity. Six real
  shapes across different lanes.
- Fail (5 candidates across 3 lanes): free-form, free-form, free-form,
  contrarian-correction, free-form. One real pattern in five.

---

### 4. specific_unrepeatable

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

### 5. avatar_format_fit

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

### 6. set_diverse

**What it measures:** The lanes are genuinely different frames for the same
video, not one idea relabeled across multiple headings. A diverse lane set gives
the creator real choices: different emotional frames, different BENS weights,
different pattern shapes, different aspects of the material emphasized.

**How to judge:** Read all lane headings and their candidate titles together. If
you could describe the set as "four ways of saying the same thing," it fails.
Look for: different lane names that each point at a distinct emotional or
strategic frame (confession vs. authority vs. contrarian vs. result), different
primary BENS letters across lanes, different pattern shapes across lanes. The
lane heading names themselves are part of the evidence: if two headings name
frames that are functionally identical (e.g. "warning" and "mistake"), that is
relabeling, not diversity.

The lane_diversity Tier A check already enforced the mechanical minimum (3
distinct lane headings). Here you judge whether the set feels genuinely diverse
in creative angle, not just mechanically distinct.

**Score 1 if:** The lanes feel like distinct creative options drawing on
different emotional frames. A creator reading the set would have a real decision
to make, not just pick a phrasing they prefer.

**Score 0 if:** Most lane headings point at the same emotional frame with
different words, OR the candidate titles across lanes all hit the same avatar
problem from the same direction, OR removing the headings would make the set
indistinguishable from a flat list of near-synonyms.

**Calibration examples:**
- Pass: one lane leads with the dollar arc (confession of a client result),
  one frames it as a contrarian system argument (authority reversal), one
  offers a "steal the system" generosity angle, one uses the 2,500-sub anchor
  as a warning about chasing reach. Different frames, different pulls.
- Fail: "Result lane," "Proof lane," "Outcome lane," and "Numbers lane" all
  surface the $340K to $1.3M figure with minor wording variation. One idea,
  four headings.

---

### 7. fabrication_resistant

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

---

### 8. surfaces_differentiated_angle

**What it measures:** The recommended opportunity lane is genuinely on-brand
AND underused in the competitor set (low spread), not a relabeled safe or
crowded pick dressed up as an opportunity. This is the headline criterion: it
is what stops the output being generic.

**How to judge:** Find the lane(s) marked `opportunity: yes`. Check two things:

First, check the iceberg alignment. The lane's frame must fit the positioning in
`creator-foundation.md` ("AI should enhance you, not replace you, no slop, you
lead"). A hype-money frame or a pure tool-speed frame is off-brand even if it
performs elsewhere. Check whether the lane name and its candidate titles fit the
iceberg.

Second, check the spread claim. Open `title-bank.md` and `pattern-bank.md`. The
opportunity lane's pattern(s) should have a spread of 1 to 2 of 11 channels
(underused). If the lane's pattern is one of the high-spread patterns (spread 5
of 11: contrarian-correction, news-jack-release, speed-mastery) and the skill
still labels it `opportunity: yes`, that is a false claim. Check whether the
`underused` label in the heading is actually supported by the spread data.

**Score 1 if:** The opportunity lane is both on-brand per the iceberg AND its
pattern(s) have a spread of 1 to 3 of 11 channels in the bank data (genuinely
underused), AND the candidate titles in that lane draw on material that only
this creator can credibly use.

**Score 0 if:** The opportunity lane's pattern is crowded (spread 4+ of 11 in
the bank data), OR the lane is off-brand per the iceberg (hype, fabricated
money, pure speed framing), OR the lane's titles are generic enough that any
competitor could run them without modification.

**Calibration examples:**
- Pass (case 00): the opportunity lane is "confession" or "contrarian-identity"
  (spread 2 of 11 each). The candidates use lock-list specifics ($340K to
  $1.3M, 2,500 subs) that only this creator's client result can back. On-brand
  (authentic reckoning, not hype). Score 1.
- Fail (case 00): the opportunity lane is "speed-mastery" (spread 5 of 11,
  crowded). Marking it `underused` is false. Score 0.
- Fail (any case): the opportunity lane's titles are "How to Build a Content
  System That Converts." Generic. Any competitor could run this. Score 0.
- Pass (case 02): the opportunity lane is "contrarian-identity" (spread 2 of
  11). The candidates name Claude Cowork and scheduled agents specifically.
  The framing is honest-and-skeptical, which fits the iceberg. Score 1.

---

### 9. competitor_proof_real

**What it measures:** Each lane's `proof:` line traces to a real entry in
`tests/fixtures/billy/banks/pattern-bank.md`. The title and channel cited in
the proof line must actually exist in the pattern-bank outlier tables, not be
invented. This is the evidence-not-taste rule: a lane recommendation without
traceable proof is just an opinion.

**How to judge:** For every lane's `proof:` line, extract the quoted title and
the @handle. Search `pattern-bank.md` for that @handle's section and look for a
row containing that title (or a clear match allowing for minor quoting
differences). The title does not need to be verbatim, but the channel handle
must appear in pattern-bank.md and the title must be recognizable as one of its
listed outliers.

Do not accept a proof line that cites a channel handle which does not appear in
pattern-bank.md at all. Do not accept a proof line where the quoted title is
plausible but not traceable to any row in that channel's outlier table.

**Score 1 if:** Every lane's proof: line cites a title-and-channel pair where
the channel appears in pattern-bank.md AND the cited title matches a row in
that channel's outlier table.

**Score 0 if:** Any lane's proof: line cites a channel handle absent from
pattern-bank.md, OR cites a title that is not traceable to any row in that
channel's listed outliers (i.e. the title appears invented rather than pulled
from the research data).

**Calibration examples:**
- Pass: `proof: "Why Growing A Personal Brand Is An AWFUL Idea" (@ed-lawrence,
  6.3x)`. @ed-lawrence appears in pattern-bank.md and that exact title is in
  the ed-lawrence outlier table at 6.3x. Score 1.
- Pass: `proof: "15 Claude Cowork Skills I Can't Live Without (steal them)"
  (@brockmesarich, 9.5x)`. @brockmesarich is in the bank and that title is in
  the brockmesarich outlier table. Score 1.
- Fail: `proof: "How I Quit My Job Using Claude" (@ed-lawrence, 4.5x)`. The
  @ed-lawrence section in pattern-bank.md has no such title. Invented. Score 0.
- Fail: `proof: "AI Changed Everything For Solo Creators" (@somechannel, 8x)`.
  @somechannel does not appear in pattern-bank.md at all. Score 0.

## Output format

Return JSON only:

```json
{
  "per_case": [
    {
      "case": 0,
      "slug": "client-340k-to-1-3m",
      "criteria": {
        "makes_a_claim": 1,
        "reads_aloud_natural": 1,
        "bank_anchored": 1,
        "specific_unrepeatable": 1,
        "avatar_format_fit": 1,
        "set_diverse": 1,
        "fabrication_resistant": 1,
        "surfaces_differentiated_angle": 1,
        "competitor_proof_real": 1
      },
      "passed": 9,
      "reasoning": "one or two sentences, concrete, cite the specific lane, candidate, or proof line that determined the score"
    }
  ],
  "criteria_pass_rate": {
    "makes_a_claim": 0.0,
    "reads_aloud_natural": 0.0,
    "bank_anchored": 0.0,
    "specific_unrepeatable": 0.0,
    "avatar_format_fit": 0.0,
    "set_diverse": 0.0,
    "fabrication_resistant": 0.0,
    "surfaces_differentiated_angle": 0.0,
    "competitor_proof_real": 0.0
  },
  "quality_score": 0.0
}
```

`passed` is the count of criteria that scored 1 for that case (out of 9).

`criteria_pass_rate` is the fraction of cases where each criterion scored 1
(e.g. if 2 of 3 cases passed fabrication_resistant, that rate is 0.6667).

`quality_score` is the total number of 1s across all scored cases divided by
the total possible (cases_scored x 9). This is the single number the optimizer
reads. A per-criterion pass rate below 0.67 tells the optimizer where to spend
the next iteration.

One `reasoning` sentence per case. Be concrete: name the lane, candidate, or
proof line that determined the score, not abstract adjectives.
