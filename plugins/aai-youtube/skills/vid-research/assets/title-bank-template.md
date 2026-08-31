---
type: bank
kind: title
project: authentic-ai-os
status: active
last_refreshed: {YYYY-MM-DD}
total_patterns: {N}
---

# Title Bank

Fill-in-the-blank title shapes for the creator's audience. Each heading IS the template. One template, one pattern. Worked examples come from the [[pattern-bank]] outlier set. Loaded by `vid-title`.

This file is both the research output (vid-research writes the shapes it surfaced) AND the creator's curated set (the creator edits in place, deleting shapes they would not use). One file, one source of truth.

## How to read this bank

Each heading is a STRUCTURE, not a phrase. The `[SLOTS]` get filled with the creator's actual content. The heading is backticked so the `[SLOT]` brackets render as code, not as broken links. Spread (how many of the analyzed channels used the pattern) and the channels that used it show repeatability. One template equals one pattern: any "or" variant is its own pattern with its own `pattern_id`. No confidence rank; the spread is the signal.

## Patterns

### `Why I [reversal action] [specific subject] After [time/quantity]`

- pattern_id: authority-reversal
- spread: 4 of 11 channels
- channels: [[@CoachX]], [[@CoachY]], [[@CoachZ]], [[@CoachW]]
- own_channel_proven: false

**Why it lands:** the audience trusts an authority who admits being wrong; a reversal signals active learning, not dogma.

**Worked examples:**
- "Why I Cut My Squat 20% After Coaching 100+ Lifters" → [[pattern-bank]] (@CoachX)
- "Why I Stopped Running 5x a Week After 12 Years" → [[pattern-bank]] (@CoachY)

**Near-miss:** "Why I Changed My Mind." No specific subject, no time/quantity, no authority signal.

**When not to use:** if the creator hasn't actually changed their position. A faked reversal collapses trust.

### `STOP [common practice] (Do This)`

- pattern_id: stop-do-this
- spread: 6 of 11 channels
- channels: [[@CoachX]], [[@CoachY]], [[@CoachZ]], [[@CoachW]], [[@CoachV]], [[@CoachU]]
- own_channel_proven: false

**Why it lands:** a sophisticated audience will question a default if given a credible reason and a replacement.

**Worked examples:**
- "STOP Following This Outdated Programming Advice" → [[pattern-bank]] (@CoachX)
- "STOP Resting 3 Minutes Between Sets (Do This)" → [[pattern-bank]] (@CoachY)

**Near-miss:** "STOP Doing Your Workouts." No specific practice named, no replacement promised.

**When not to use:** audiences that prefer analytical authority to direct commands; can read aggressive for professional niches.

### `The [Specific Thing] Mistake [Audience Descriptor] Makes`

- pattern_id: authority-diagnosis
- spread: 2 of 11 channels
- channels: [[@CoachX]], [[@CoachZ]]
- own_channel_proven: false

**Why it lands:** an authority names a specific failure mode the audience is making, which feels diagnostic and personal.

**Worked examples:**
- "The Programming Mistake Every Intermediate Lifter Makes" → [[pattern-bank]] (@CoachX)
- "The Deload Mistake Most Powerlifters Make" → [[pattern-bank]] (@CoachZ)

**Near-miss:** "5 Mistakes Every Lifter Makes." No specific failure mode named, slips into listicle territory.

**When not to use:** when the diagnosis is generic. The specific failure mode is the whole pattern.

### `{next template string as research surfaces it}`

- pattern_id: {kebab-slug}
- spread: {N} of {M} channels
- channels: {wikilinks}
- own_channel_proven: {true|false}

{why it lands / worked examples / near-miss / when not to use}

## Considered + dropped

Title patterns the creator dropped after consideration. Rationale captured so future refreshes don't re-surface them.

> [!quote] Dropped: `{template}`
> pattern_id: {slug}
> Rationale: {one-liner}
> Bucket: {tone-mismatch | audience-sophistication | off-positioning | authority-conflict | trend-chasing | other}
> Date: {YYYY-MM-DD}

## Pattern combinations

Some patterns combine. Worked examples (by pattern_id):

- `authority-reversal` + `authority-diagnosis`: "Why I Quit [Mistake] After Coaching 100+ Lifters." Combines reversal authority with a named diagnosis.
- {others as discovered}

## Field reference

- **Heading**: the template itself, backticked. `[SLOTS]` are the variables you fill.
- **pattern_id**: a stable kebab slug. Survives heading edits and slot changes, and is what `pattern-bank.md` outlier rows link to (heading-anchor links break once headings carry `[SLOT]` brackets).
- **spread**: `{N} of {M} channels`. How broadly the structure held across the research set. The repeatability signal. No HIGH/MEDIUM/LOW label; the count is the truth.
- **channels**: Obsidian wikilinks to the channels where the pattern appeared. Attribution.
- **own_channel_proven**: `true | false`. Whether it is proven on the creator's own channel. The strongest signal.
- **Why it lands**: the one reason the shape pulls.
- **Worked examples**: real titles from [[pattern-bank]], cited with channel.
- **Near-miss / When not to use**: how the shape breaks when a slot is vague, and the authenticity guard.

Fields deliberately not captured: `confidence` rank, raw frequency. The popularity of a shape in the set is not its fit for the next title; fit is judged at curation.
