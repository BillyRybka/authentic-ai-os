---
type: reference
scope: skill-local
loaded_by: [vid-research]
status: active
tags: [reference, vid-research, pattern-extraction, prompts]
---

# Pattern Extraction Prompts

LLM prompt templates vid-research uses to extract patterns from outlier data. Load this when running pattern extraction in Phase 1, 2, or 3. These are for the AI to think with, never paste at the creator.

## Prompt 1: Channel theme summary

**Purpose:** summarize a channel's primary themes from its last 30 video titles. Feeds the fluke filter.

**Input:** array of last 30 titles.

**Prompt:**

```
Below are the last 30 video titles from a YouTube channel, most recent first.

{numbered titles}

Output the channel's 2-4 primary themes as specific noun phrases (not "fitness", "strength training programming for intermediate-to-advanced lifters"). Add a 1-2 sentence audience note.

Format:
Primary themes:
1. {specific theme}
2. {specific theme}

Audience: {who this channel targets, what they expect}
```

**Worked output:**

```
Primary themes:
1. Strength programming critique and revision
2. Lift technique cues and form fixes
3. Programming framework comparison

Audience: intermediate-to-advanced lifters running existing programs. Expects strong opinions and specific programming changes, not beginner basics.
```

**Fails when:** themes are too generic ("fitness," "working out"). Generic themes break the fluke filter downstream.

## Prompt 2: Fluke filter

**Purpose:** determine if a candidate outlier is on-niche or a fluke.

**Input:** outlier title + view count + channel's primary themes from Prompt 1.

**Prompt:**

```
Channel themes:
{from Prompt 1}

Candidate outlier:
Title: "{title}"
Views: {count} ({N}x channel median)

Classify:
- ON_NICHE, topic clearly fits the themes
- BORDERLINE, in the channel's space but covers an angle the channel doesn't usually cover (surface to creator)
- FLUKE, topic is clearly off-niche (algorithmic spike, cross-promotion, etc.)

Format:
Classification: {one of three}
Reasoning: {one sentence}
```

**Worked outputs:**

```
ON_NICHE: "Why I Cut My Squat 20% After Coaching 100+ Lifters" on a strength-programming channel.
Reasoning: outlier covers programming critique with authority claim, fitting primary themes directly.

FLUKE: "I Tried Sewing for 30 Days" on a thumbnail-strategy/retention channel.
Reasoning: sewing has no overlap with the channel's YouTube-strategy themes; pattern data won't transfer.

BORDERLINE: "Why I Quit My 9-to-5 to Coach" on a strength-programming channel.
Reasoning: personal-brand content sits adjacent to programming focus; recommend creator confirms whether to study or skip.
```

## Prompt 3: Power word extraction

**Purpose:** extract power words classified as Global (work everywhere) vs Audience-Specific (work for THIS audience).

**Input:** array of confirmed-outlier titles + audience description.

**Prompt:**

```
Outlier titles:
{numbered list}

Audience: {description}

Identify:
1. GLOBAL power words appearing in these titles (transcend niches): "easy," "fast," "secret," "stop," "never," "fix," "real," "mistake," "new", and any similar.
2. AUDIENCE-SPECIFIC power words: domain jargon, tool names, or identity terms that resonate only for this audience.
3. RECURRING BOLT-ONS: phrases that attach to many different titles without changing their structure, usually a tail or a parenthetical. Time boxes ("in 11 Minutes"), completeness promises ("Step-by-Step", "full tutorial"), duration stamps ("10+ Hour Course"), year stamps ("(2026)"), constraint flexes ("No Employees", "No Code"), free assets ("(Free Template)"), permission tags ("(steal them)"). These are power words even though they are several words long. They belong here, never in the title-shape list.

Pull only from the actual titles. Never invent. Be comprehensive: pull EVERY recurring power word, not a token few. A large outlier set (100-plus titles) should yield 20 or more global and 10 or more audience-specific. A short list means you under-mined the set.

Output one word or phrase per entry. NEVER combine two distinct things in one entry. Split on slashes ("fast/easy" becomes "fast" and "easy"). Split product variants into separate entries: "Claude", "Claude Code", and "Claude Cowork" are three different products and three entries. "No Employees" and "No Code" are two. "Content Creators" and "Content Team" are two. Distinct terms land differently and downstream title generation pulls a single term per slot, so a combined entry gives it nothing clean to select.

Give each entry one real example title, verbatim. No when-it-lands or when-it-fails commentary; the example carries it.

Format:
Global:
- "{word}", example: "{title}"

Audience-specific:
- "{word}", example: "{title}"
```

**Worked output (strength-programming niche):**

```
Global:
- "STOP", example: "STOP Following This Outdated Programming Advice"
- "MISTAKE", example: "The Programming Mistake Every Intermediate Lifter Makes"
- "in [N] Minutes", example: "Fix Your Deadlift Setup in 6 Minutes"
- "(Free Template)", example: "My 12-Week Peaking Block (Free Template)"

Audience-specific:
- "PROGRAMMING", example: "STOP Following This Outdated Programming Advice"
- "PLATEAU", example: "The Bench Cue That Fixed My Plateau"
- "TEXAS METHOD", example: "The Texas Method Trap"
- "CUE", example: "The Bench Cue That Fixed My Plateau"
```

**Fails when:** AI hallucinates power words not in the input ("amazing," "great," "best"). Always pull from actual titles.

**Also fails when:** it promotes a bolt-on to a title shape. If a phrase attaches to several structurally different titles, it is a power word, not a shape. See Prompt 4's fill test.

## Prompt 4: Title pattern extraction

**Purpose:** identify fill-in-the-blank title shapes recurring across outliers.

**Input:** array of confirmed-outlier titles.

**Prompt:**

```
Outlier titles:
{numbered list}

Identify pattern shapes appearing in 2+ titles. One template = one pattern; split any "or" variant into its own pattern. Express each as a template with [SLOT] placeholders.

APPLY THE FILL TEST TO EVERY SHAPE. Fill its slots with arbitrary content from this niche and read the result. If you get a title worth publishing, the shape is right-sized. If you get generic mush, the shape is too loose: the fixed words are only connective tissue and the slots are doing all the work. Tighten it or drop it.

Worked failure: "[Outcome] in [N] Minutes" fills to "Get More Clients in 15 Minutes", which is a nothing title. The only fixed words are "in" and "minutes". It is too loose, and it wrongly merges at least three real shapes: "Master [N]% of [Tool] in [N] Minutes" (the percentage promises near-complete mastery while admitting it is not all of it), "How I Use [Tool] To [Outcome] In [N] Minutes" (first-person demo of a named tool), and "[Topic] Fundamentals In [N] Minutes" (curriculum promise). Keep the fixed words that carry the mechanism; turn only the genuinely varying parts into slots.

Being specific is not the same as being too granular. "Master [N]% of [Tool] in [N] Minutes" is correct because the percentage IS the mechanism. It would only be too granular if you froze the number ("Master 95% of [Tool]").

A phrase that attaches to structurally different titles is a bolt-on, not a shape. "in [N] Minutes" rides on all three shapes above, so it goes to Prompt 3 as a power word and never becomes a shape of its own.

Format per pattern:
Template: "{template}"
Pattern shape: {descriptive label}
spread: {N} of {M} channels
Fill test: "{slots filled with arbitrary niche content}" → publishable or mush
Examples:
- "{title}"
- "{title}"
```

**Worked output:**

```
Template: "Why I [reversal action] [specific subject] After [time/quantity]"
Pattern shape: Authority Reversal
spread: 4 of 11 channels
Fill test: "Why I Dropped Barbell Rows After 8 Years Coaching" → publishable
Examples:
- "Why I Cut My Squat 20% After Coaching 100+ Lifters"
- "Why I Stopped Running 5x a Week After 12 Years"
- "Why I Quit Tracking Macros (And What Replaced It)"

Template: "STOP [common practice] (Do This)"
Pattern shape: Contrarian Command
spread: 6 of 11 channels
Fill test: "STOP Warming Up With Static Stretches (Do This)" → publishable
Examples:
- "STOP Following This Outdated Programming Advice"
- "STOP Resting 3 Minutes Between Sets (Do This)"
```

## Prompt 5: Topic cluster extraction (own + niche only)

**Purpose:** identify topic clusters in own-channel and niche-channel outliers.

**HARD RULE:** never run this prompt on adjacent niche outliers. Topics from adjacent niches don't transfer.

**Input:** confirmed-outlier titles from own + niche channels only.

**Prompt:**

```
Outlier titles:
{numbered list}

Group titles by topic cluster (related subject matter, not just structural similarity). Output 2-5 clusters, each with 2+ titles.

Format per cluster:
Cluster {N}: {label}
Topic substance: {what subject matter}
Members:
- "{title}"
- "{title}"
Why this pulls: {one-sentence hypothesis}
```

**Worked output:**

```
Cluster 1: Programming reversals
Topic substance: creator changing their mind about an approach they previously taught
Members:
- "Why I Cut My Squat 20% After Coaching 100+ Lifters"
- "Why I Stopped Running 5x a Week After 12 Years"
- "Why I Quit Tracking Macros (And What Replaced It)"
Why this pulls: audience trusts authorities who admit being wrong; reversals signal active learning rather than dogma.
```

## Where outputs land

- Prompt 1 (themes) → the Channels table in research-log.md
- Prompt 2 (fluke) → skip/study decision, no direct bank entry
- Prompt 3 (power words) → power-words-bank.md (global + audience-specific)
- Prompt 4 (title patterns) → title-bank.md as blocks where the heading IS the template string and the body carries spread + own_channel_proven + why it lands + worked examples
- Prompt 5 (topics) → topic clusters under Findings in research-log.md (own + niche only), not a standalone bank

All entries start `status: draft-pending-curation` until Theory of One curation pass promotes them.

## Common mistakes (apply across all prompts)

- **Hallucinating content not in the input.** If a word, theme, or pattern doesn't appear in the actual titles provided, don't invent it. Mark "no pattern found" if true.
- **Generic outputs.** "Fitness" isn't a theme. "Intermediate-to-advanced strength programming critique" is. Specificity is the whole job.
- **Including adjacent niche topics in Prompt 5.** Hard rule, never. Topics never enter the bank from adjacent. Structures yes, topics no.
- **Inflating spread.** Report the channel count honestly: a pattern on 2 of 5 channels is thin spread, not convergence. Convergence is 4+ channels OR convergent across niche AND adjacent. Never round the count up, and never stamp a HIGH/MEDIUM/LOW label; the spread is the signal.
- **Forcing patterns where none exist.** Sometimes 5 outliers don't share a structural pattern. Output "no pattern found" if true rather than inventing.
