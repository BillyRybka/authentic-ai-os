---
type: bank
kind: title-patterns
project: youtube-content-os
status: active
last_refreshed: {YYYY-MM-DD}
total_patterns: {N}
---

# Title Patterns Bank

Fill-in-the-blank title shapes that recur across outliers. Each pattern has [SLOT] placeholders for the variable parts plus worked examples and near-miss anti-patterns.

Loaded by `vid-title` for headline candidate generation and by `vid-intro` for hook construction (since hook openers often mirror title structures).

## How to read this bank

Each pattern is a STRUCTURE, not a specific phrase. The [SLOTS] get filled with the creator's actual content. Worked examples show how the pattern lands when filled correctly. Near-miss examples show how it fails.

## Curated patterns

### Pattern T-1: Authority Reversal

**Template:** `Why I [reversal action] [specific subject] After [time/quantity]`

**Pattern shape:** authority figure publicly changing their mind about a previously-held position.

**Confidence:** HIGH ({N} of {M} channels)

**Why this lands:** audience trusts authority figures who admit being wrong; reversals signal active learning rather than dogma.

**Worked examples:**
- "Why I Cut My Squat 20% After Coaching 100+ Lifters" — @CoachX, 145k views
- "Why I Stopped Running 5x a Week After 12 Years" — @CoachY, 92k views
- "Why I Quit Tracking Macros After 8 Years" — @CoachZ, 124k views

**Near-miss anti-pattern:**
- "Why I Changed My Mind" — too vague, missing the specific subject and time/quantity slots, doesn't signal authority

**When NOT to use this pattern:** if the creator hasn't actually changed their position on the subject. Authority Reversal requires real reversal — fabricating one collapses trust.

### Pattern T-2: Contrarian Command

**Template:** `STOP [common practice] (Do This)`

**Pattern shape:** direct command against a prevalent practice, often with a parenthetical "do this" promise.

**Confidence:** HIGH ({N} channels)

**Why this lands:** sophisticated audiences are ready to question what they're doing if given a credible reason.

**Worked examples:**
- "STOP Following This Outdated Programming Advice" — @CoachX, 145k
- "STOP Resting 3 Minutes Between Sets (Do This)" — @CoachY, 88k

**Near-miss anti-pattern:**
- "STOP Doing Your Workouts" — too broad, no specific common practice named, no replacement promised

**When NOT to use:** for audiences that respond to authoritative analytical tone rather than direct commands. May feel aggressive for sophisticated B2B or professional-niche audiences.

### Pattern T-3: Authority Diagnosis

**Template:** `The [Specific Thing] [Mistake/Trap/Problem] [Audience Descriptor] Makes`

**Pattern shape:** authority identifying a specific failure mode the audience is making.

**Confidence:** HIGH

**Worked examples:**
- "The Programming Mistake Every Intermediate Lifter Makes" — @CoachX, 95k
- "The Texas Method Trap (And What I Run Instead)" — @CoachY, 78k

**Near-miss anti-pattern:**
- "5 Mistakes Every Lifter Makes" — too generic, no specific failure mode named, slips into listicle territory

### Pattern T-4: {add patterns as research surfaces them}

{populated}

## Considered + dropped

Title patterns AI proposed that the creator dropped. Rationale captured.

> [!quote] Dropped pattern: {label}
> Template: `{template}`
> Rationale: {one-liner}
> Bucket: {tone-mismatch | etc}
> Date: {YYYY-MM-DD}

## Pattern combinations

Some patterns combine. Worked examples of combinations the creator's audience responds to:

- T-1 + T-3: "Why I Quit [Mistake] After Coaching 100+ Lifters" — combines reversal authority with diagnosis
- {others as discovered}

