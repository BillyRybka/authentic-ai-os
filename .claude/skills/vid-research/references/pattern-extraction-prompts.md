---
type: reference
scope: skill-local
loaded_by: [vid-research]
status: active
tags: [reference, vid-research, pattern-extraction, prompts]
---

# Pattern Extraction Prompts

LLM prompt templates vid-research uses to extract patterns from outlier data. Load this when running pattern extraction in Phase 1, 2, or 3. These are for the AI to think with — never paste at the creator.

## Prompt 1 — Channel theme summary

**Purpose:** summarize a channel's primary themes from its last 30 video titles. Feeds the fluke filter.

**Input:** array of last 30 titles.

**Prompt:**

```
Below are the last 30 video titles from a YouTube channel, most recent first.

{numbered titles}

Output the channel's 2-4 primary themes as specific noun phrases (not "fitness" — "strength training programming for intermediate-to-advanced lifters"). Add a 1-2 sentence audience note.

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

## Prompt 2 — Fluke filter

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
- ON_NICHE — topic clearly fits the themes
- BORDERLINE — in the channel's space but covers an angle the channel doesn't usually cover (surface to creator)
- FLUKE — topic is clearly off-niche (algorithmic spike, cross-promotion, etc.)

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

## Prompt 3 — Power word extraction

**Purpose:** extract power words classified as Global (work everywhere) vs Audience-Specific (work for THIS audience).

**Input:** array of confirmed-outlier titles + audience description.

**Prompt:**

```
Outlier titles:
{numbered list}

Audience: {description}

Identify:
1. GLOBAL power words appearing in these titles (transcend niches): "easy," "fast," "secret," "stop," "never," "fix," "real," "mistake," "new" — and any similar.
2. AUDIENCE-SPECIFIC power words: domain jargon or terms that resonate only for this audience.

Pull only from the actual titles. Never invent.

Format:
Global:
- "{word}" — {N} occurrences — example: "{title}"

Audience-specific:
- "{word}" — {N} occurrences — example: "{title}"
```

**Worked output (strength-programming niche):**

```
Global:
- "STOP" — 2 — "STOP Following This Outdated Programming Advice"
- "MISTAKE" — 1 — "The Programming Mistake Every Intermediate Lifter Makes"

Audience-specific:
- "PROGRAMMING" — 3 — "STOP Following This Outdated Programming Advice"
- "PLATEAU" — 1 — "The Bench Cue That Fixed My Plateau"
- "TEXAS METHOD" — 1 — "The Texas Method Trap"
- "CUE" — 1 — "The Bench Cue That Fixed My Plateau"
```

**Fails when:** AI hallucinates power words not in the input ("amazing," "great," "best"). Always pull from actual titles.

## Prompt 4 — Title pattern extraction

**Purpose:** identify fill-in-the-blank title shapes recurring across outliers.

**Input:** array of confirmed-outlier titles.

**Prompt:**

```
Outlier titles:
{numbered list}

Identify pattern shapes appearing in 2+ titles. Express each as a template with [SLOT] placeholders.

Format per pattern:
Pattern T-{N}: "{template}"
Pattern shape: {descriptive label}
Examples:
- "{title}"
- "{title}"
```

**Worked output:**

```
Pattern T-1: "Why I [reversal action] [specific subject] After [time/quantity]"
Pattern shape: Authority Reversal
Examples:
- "Why I Cut My Squat 20% After Coaching 100+ Lifters"
- "Why I Stopped Running 5x a Week After 12 Years"
- "Why I Quit Tracking Macros (And What Replaced It)"

Pattern T-2: "STOP [common practice] (Do This)"
Pattern shape: Contrarian Command
Examples:
- "STOP Following This Outdated Programming Advice"
- "STOP Resting 3 Minutes Between Sets (Do This)"
```

## Prompt 5: RETIRED (format is a menu pick, not a mined pattern)

Format cannot be reliably classified from title + duration + thumbnail without watching or transcribing every outlier (infeasible at research scale). Format is NOT extracted here. It is a creator menu pick from the fixed 7-format menu in `knowledge/format-rotation-guide.md`, handled in vid-research Phase 7. Prompt number kept stable so downstream references do not shift; this step does nothing.

## Prompt 6 — Topic cluster extraction (own + niche only)

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

## Prompt 7: RETIRED (flop analysis is post-publish, not pre-research)

The source teaches flop diagnosis AFTER a video underperforms (why did THIS video tank: positioning, packaging, script, execution), not as a pre-research bank of "what the audience hates." That belongs to future vid-measurement, fed by the creator's own published data. It is not collected during research. Prompt number kept stable; this step does nothing.

## Where outputs land

- Prompt 1 (themes) → per-channel section in pattern-bank.md
- Prompt 2 (fluke) → skip/study decision, no direct bank entry
- Prompt 3 (power words) → power-words-bank.md (global + audience-specific)
- Prompt 4 (title patterns) → title-patterns-bank.md
- Prompt 5 (format) → RETIRED, format is a menu pick in knowledge/format-rotation-guide.md
- Prompt 6 (topics) → topic-cluster section inside pattern-bank.md (own + niche only), not a standalone bank
- Prompt 7 (flops) → RETIRED, post-publish flop diagnosis is future vid-measurement

All entries start `status: draft-pending-curation` until Theory of One curation pass promotes them.

## Common mistakes (apply across all prompts)

- **Hallucinating content not in the input.** If a word, theme, or pattern doesn't appear in the actual titles provided, don't invent it. Mark "no pattern found" if true.
- **Generic outputs.** "Fitness" isn't a theme. "Intermediate-to-advanced strength programming critique" is. Specificity is the whole job.
- **Including adjacent niche topics in Prompt 6.** Hard rule — never. Topics never enter the bank from adjacent. Structures yes, topics no.
- **Confidence inflation.** A pattern appearing in 2 of 5 channels is LOW-MEDIUM, not HIGH. Reserve HIGH for 4+ channels or convergent across niche AND adjacent.
- **Forcing patterns where none exist.** Sometimes 5 outliers don't share a structural pattern. Output "no pattern found" if true rather than inventing.
