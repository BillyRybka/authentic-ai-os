# vid-title Tier B Rubric (AI judge)

DO NOT MODIFY during an autoresearch loop. This is the locked rubric. You are a
fresh judge with no memory of prior iterations. You do not know how many times
the skill has been edited or which version this is. Score only what is in front
of you, against this rubric. Be consistent and a little stingy: a passing score
requires the criterion to be clearly met, not arguably met.

This rubric grades for offense. The mechanical floor (fabrication, character
ceiling, em-dashes, banned words, AI-default phrasings, receipts present) is
Tier A's job and is already enforced before you see a case. Your job is the
question Tier A cannot answer: would these titles win the click next to the
real winners in the pattern bank? A title that passes every safety gate and
still sits flat is a failing title here.

## What you receive per case

- `piece.md`, the vault file the skill saved: the upstream framed piece with
  the locked title written to the `title:` frontmatter field and
  `last_updated:` bumped. This is the artifact. The locked title is the
  `title:` field. The current skill produces NO `titles.md`; anything grading
  a `titles.md` is grading the old contract.
- `transcript.md`, the full working trace: the lock list build, the bank
  shopping, the wide pass, the kill pass, the checklist pass, the presented
  set, and the creator exchange. The sections that matter for scoring:
  `## Lock list` (the specifics the titles were allowed to use), `## Options`
  (3 to 5 proven structure groups plus one wildcard group; each proven group
  opens with a `receipt:` line naming the source outlier title, @channel, and
  multiplier, followed by 1 to 2 numbered candidates annotated with BENS
  letters and char count; the wildcard group is flagged in its heading,
  carries no receipt, and holds 1 to 2 swings), and `## Recommendation`
  (names the recommended candidate and the reason, ceiling not floor)
- The frozen fixtures for this case: the upstream `piece.md` (suite-local
  `fixtures/{slug}/piece.md`: format, goal, frame, core_payoff) and
  the shared billy `brain-dump.md` (material, the lock-list ground truth)
- The creator's banks: `pattern-bank.md` (competitor outliers with views and
  multipliers per channel), `title-bank.md` (named structures with worked
  examples), `power-words-bank.md`
- The foundation: `creator-foundation.md` (iceberg, avatar, Top 3 problems)

Only run Tier B on cases that already passed Tier A. If a case failed Tier A,
do not score it. The mechanical floor was not met.

## Calibration anchor (do this before scoring)

Open `pattern-bank.md` and read the outlier rows for the three or four
channels closest to this case's topic. Read the titles out loud in your head.
Those titles pulled 2x to 30x their channel's normal views from this exact
audience. That is the bar. Hold five of them in mind while you score. You are
not comparing candidates to an abstract standard of "good copy." You are
comparing them to these.

Voice is NOT part of this rubric. Titles are packaging, not prose. The only
voice-shaped floor (one continuous human thought, no AI tells) is enforced in
Tier A. Do not reward a title for sounding like the creator and do not punish
a title for sounding like the niche's winners.

## Scoring system

Each criterion is scored 0 or 1 (no partial credit).
- 1 = the criterion is clearly and fully met
- 0 = the criterion is not met, or there is genuine doubt

This is binary. "Mostly yes" is a 0. Score what is in front of you.

## Criteria

### 1. lineup_test [PRIMARY GATE]

**What it measures:** The locked title survives sitting in a lineup with the
real winners. This is the criterion that stops the skill producing safe,
compliant titles that grade well and click badly.

**How to judge:** From `pattern-bank.md`, pick the five outlier titles nearest
this case by topic and promise. Write the locked title into that list as a
sixth row. Two questions, both must be yes:

1. **Does it belong?** Same class of click power. If the five bank titles
   would visibly out-pull it on a home page (bigger claim, sharper stake,
   stronger loop), it does not belong.
2. **Does it stand out?** It is not a near-duplicate of any row in the lineup.
   It brings its own stake or claim, so a viewer who has seen the other five
   still has a reason to click this one.

Name the five lineup titles in your reasoning.

**Score 1 if:** The locked title belongs in the lineup AND stands out from it.

**Score 0 if:** It reads visibly weaker than the lineup, OR it is one of the
lineup titles with the nouns swapped, OR you find yourself arguing it "would
probably do fine." Fine is a 0.

Watch for the room-temperature failure: a title whose payload words name the
video's mechanism (order, first, steps, setup) instead of the viewer's wound
or desire. Bank winners run hot (Hard Way, AWFUL, Secret, QUIT). Cover the
structure and read only the payload words; if none of them carries heat, the
title reads visibly weaker in any lineup and scores 0 no matter how proven
its shape is.

**Calibration (case 00, client-340k-to-1-3m):**
- Pass: "$340K to $1.3M on 2,500 Subscribers" holds its own next to
  money-arc outliers because the small-channel anchor is a stake none of them
  carry.
- Fail: "How to Build a Content System That Converts" dies in any lineup.
  No bank winner sounds like that, because it makes no one feel anything.
- Fail: a locked title that is a bank winner with only the topic word changed.
  It belongs, but it does not stand out.

---

### 2. teeth [PRIMARY GATE]

**What it measures:** The locked title opens a loop AND takes a stand. Both.
An open loop with no stand is trivia. A stand with no loop is a thesis
statement. Safe language and thesis-stating titles both fail, no matter how
clean they are.

**How to judge:** Read the locked title and answer two questions:

1. **The loop:** is there something the viewer's mind must resolve (a how, a
   what, a wait-really)?
2. **The stand:** does the title commit to a position someone could disagree
   with, or press a cost the viewer does not want to admit? "Interesting" is
   not a stand. A stand has an edge: it says you're doing it wrong, this
   thing you trust is costing you, the common path is the trap.

Anti-fabrication still holds: the stand must be one the video actually
argues, per piece.md and the brain-dump. A borrowed stand the material never
makes is a 0 here and a Tier A fabrication besides.

**Score 1 if:** Loop and stand are both present in the locked title.

**Score 0 if:** Either is missing. A neutral curiosity title ("Why a 2,500-Sub
Channel Hit $1.3M in a Year") opens a loop but takes no stand: 0. A flat
declaration ("Consistency Matters More Than Reach") takes a stand but opens
no loop: 0.

**Calibration (case 00):**
- Pass: "Why Chasing Subscribers Kept This Channel Broke" (loop: what were
  they doing instead; stand: the growth advice you follow is the problem),
  provided the material argues it.
- Fail: "Why a 2,500-Sub Channel Hit $1.3M in a Year" (loop, no stand).
- Fail: "Small Channels Can Out-Earn Big Ones" (stand, no loop, and stated
  as a thesis).

---

### 3. adjust_quality

**What it measures:** The proven options are real adjusts, not noun swaps.
The skill's engine is: keep what makes the source outlier win, swap in this
video's subject and this avatar's stake. This criterion checks the engine
survived the swap.

**How to judge:** For each structure group in `## Options`, look up its
`receipt:` in `pattern-bank.md` (Tier A confirmed it exists; you judge the
craft). Ask of each candidate: what makes the SOURCE title pull, and does the
candidate reproduce that pull with this case's material? A dead adjust keeps
the source's words but loses its stake: the source's stake belonged to the
source's audience, and the candidate never replaced it with this avatar's.
Check the transcript: the skill should articulate why each source wins before
adjusting it.

**Score 1 if:** Every structure group's candidates keep the source's engine
with this avatar's stake swapped in, AND the transcript shows the skill named
why each source wins before writing.

**Score 0 if:** Any group's candidates are noun-swaps that lose the stake, OR
the receipts read as retrofitted labels on titles that were actually written
free-form (the transcript shows no adjust reasoning).

**Calibration:**
- Pass: source "Gym MISTAKES That Kill Your Progress" adjusted to "Meal Prep
  Mistakes That Keep You Ordering Takeout." Engine kept (you're doing it
  wrong and it costs you the thing you care about), stake localized.
- Fail: same source adjusted to "Meal Prep Mistakes That Kill Your Progress."
  "Progress" was the gym audience's stake. Nouns swapped, pull lost.

---

### 4. subtext_set

**What it measures:** The option set makes the viewer's brain do the work.
For each candidate, reading it should make the viewer fill in a want, a how,
or an am-I-wrong. A candidate whose honest fill-in is "nothing, it says what
the video is about" is a label wearing a title's clothes.

**How to judge:** For the locked title and every candidate in `## Options`,
write the fill-in: the unspoken sentence the viewer's mind completes. Judge
the fill-ins, not the titles. "I want that," "how did they do that," "wait,
am I doing this wrong?" pass. "This video is about X" fails that candidate.

**Score 1 if:** The locked title and all but at most one candidate produce a
real fill-in.

**Score 0 if:** Two or more candidates (or the locked title itself) produce
no fill-in beyond a description of the video.

**Calibration (case 02, claude-cowork-newsjack):**
- Fail: "Claude Cowork Just Dropped Scheduled Agents." Fill-in: nothing, it
  is a product announcement.
- Pass: "You're Still Babysitting Your AI (You Don't Have To)." Fill-in: am
  I? What would it mean to stop?

---

### 5. unrepeatable

**What it measures:** The locked title is pinned to this video. It carries at
least one lock-list specific (a number, a named tool or method, a timeframe,
a named outcome) or a stake so particular to this material that the title
cannot front a different video in the niche.

**How to judge:** Read the locked title and ask: could a competitor paste
this onto their own video about the same general topic without changing a
word? If yes, it is generic. Cross-check any specific against the
`## Lock list`: only listed specifics count (an invented one is a Tier A
failure, but if one slipped through, score 0 here too).

**Score 1 if:** The locked title carries a lock-list specific or a
material-particular stake that ties it to this video alone.

**Score 0 if:** The locked title could front any video in the niche, or its
only specific is not on the lock list.

**Calibration (case 00, lock list: $340K, $1.3M, 1 year, 2,500 subscribers):**
- Pass: "$340K to $1.3M on 2,500 Subscribers." Three lock-list specifics.
- Fail: "How to Build a Content System That Converts." Paste-on-anything.
- Fail: "The $500K Content System." The figure is not on the lock list.

**Calibration (case 02, lock list has NO numbers):** a candidate with any
digit fails; "Claude Cowork" and "scheduled agents" are the legal specifics.

---

### 6. set_range

**What it measures:** The set gives the creator a real decision plus a real
swing. The structure groups pull in genuinely different ways, and the
wildcard is an actual experiment, not a proven option with the receipt
removed.

**How to judge:** Read the full set. First, the groups: do they run different
engines (a contrarian correction pulls differently than a result arc, which
pulls differently than a named-system reveal)? If every group presses the
same button with different words, the set is one idea photocopied. Second,
the wildcard: is at least one swing present, flagged, and structurally unlike
every proven option? A tame wildcard (a shorter variant of option 2) fails.

**Score 1 if:** At least two structure groups run clearly different engines,
AND a flagged wildcard exists that is not a variant of any proven option.

**Score 0 if:** The groups are one engine relabeled, OR the wildcard is
missing, unflagged, or a disguised variant of a proven option.

**Calibration:**
- Pass: a mistakes-with-a-cost group, a result-arc group, a named-system
  group, and a wildcard that reframes the whole premise ("Cooking Every
  Night Is the Mistake").
- Fail: "Result lane," "Proof lane," and "Numbers lane" all surfacing the
  same dollar arc, wildcard absent.

## Output format

Return JSON only:

```json
{
  "per_case": [
    {
      "case": 0,
      "slug": "client-340k-to-1-3m",
      "criteria": {
        "lineup_test": 1,
        "teeth": 1,
        "adjust_quality": 1,
        "subtext_set": 1,
        "unrepeatable": 1,
        "set_range": 1
      },
      "passed": 6,
      "reasoning": "one or two sentences, concrete: name the lineup titles used, the fill-in that decided subtext_set, or the candidate that decided the score"
    }
  ],
  "criteria_pass_rate": {
    "lineup_test": 0.0,
    "teeth": 0.0,
    "adjust_quality": 0.0,
    "subtext_set": 0.0,
    "unrepeatable": 0.0,
    "set_range": 0.0
  },
  "quality_score": 0.0
}
```

`passed` is the count of criteria that scored 1 for that case (out of 6).

`criteria_pass_rate` is the fraction of cases where each criterion scored 1.

`quality_score` is the total number of 1s across all scored cases divided by
the total possible (cases_scored x 6). This is the single number the
optimizer reads. A per-criterion pass rate below 0.67 tells the optimizer
where to spend the next iteration.

One `reasoning` sentence per case. Be concrete: name the lineup titles, the
candidate, or the fill-in that determined the score, not abstract adjectives.
