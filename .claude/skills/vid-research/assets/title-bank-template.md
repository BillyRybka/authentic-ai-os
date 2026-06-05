---
type: bank
kind: title
project: authentic-ai-os
status: active
last_refreshed: {YYYY-MM-DD}
total_patterns: {N}
---

# Title Bank

Fill-in-the-blank title shapes for the creator's audience. Each pattern is a STRUCTURE with [SLOT] placeholders for the variable parts, plus worked examples and near-miss anti-patterns.

This file is both the research output (vid-research writes patterns it surfaced across the outlier set) AND the creator's curated set (the creator edits this file in place, deleting patterns they would not use). One file, one source of truth.

Loaded by `vid-title` for headline candidate generation and by `vid-intro` for hook construction (since hook openers often mirror title structures).

## How to read this bank

Each pattern is a STRUCTURE, not a specific phrase. The [SLOTS] get filled with the creator's actual content (from the current piece's brain-dump or script lock list). Worked examples show how the pattern lands when filled correctly. Near-miss examples show how it fails. Confidence is HIGH / MEDIUM / LOW based on how broadly the structural pattern held across the research set, not raw frequency.

## Curated patterns

### Pattern T-1: Authority Reversal

**Template:** `Why I [reversal action] [specific subject] After [time/quantity]`

**Pattern shape:** authority figure publicly changing their mind about a previously-held position.

**Confidence:** HIGH

**Why this lands:** audience trusts authority figures who admit being wrong; reversals signal active learning rather than dogma.

**Worked examples:**
- "Why I Cut My Squat 20% After Coaching 100+ Lifters" → [[pattern-bank#outlier-row]]
- "Why I Stopped Running 5x a Week After 12 Years" → [[pattern-bank#outlier-row]]
- "Why I Quit Tracking Macros After 8 Years" → [[pattern-bank#outlier-row]]

**Near-miss anti-pattern:**
- "Why I Changed My Mind". Too vague, missing the specific subject and time/quantity slots, doesn't signal authority

**When NOT to use this pattern:** if the creator hasn't actually changed their position on the subject. Authority Reversal requires real reversal; fabricating one collapses trust.

### Pattern T-2: Contrarian Command

**Template:** `STOP [common practice] (Do This)`

**Pattern shape:** direct command against a prevalent practice, often with a parenthetical "do this" promise.

**Confidence:** HIGH

**Why this lands:** sophisticated audiences are ready to question what they are doing if given a credible reason.

**Worked examples:**
- "STOP Following This Outdated Programming Advice" → [[pattern-bank#outlier-row]]
- "STOP Resting 3 Minutes Between Sets (Do This)" → [[pattern-bank#outlier-row]]

**Near-miss anti-pattern:**
- "STOP Doing Your Workouts". Too broad, no specific common practice named, no replacement promised

**When NOT to use:** for audiences that respond to authoritative analytical tone rather than direct commands. May feel aggressive for sophisticated B2B or professional-niche audiences.

### Pattern T-3: Authority Diagnosis

**Template:** `The [Specific Thing] [Mistake/Trap/Problem] [Audience Descriptor] Makes`

**Pattern shape:** authority identifying a specific failure mode the audience is making.

**Confidence:** HIGH

**Worked examples:**
- "The Programming Mistake Every Intermediate Lifter Makes" → [[pattern-bank#outlier-row]]
- "The Texas Method Trap (And What I Run Instead)" → [[pattern-bank#outlier-row]]

**Near-miss anti-pattern:**
- "5 Mistakes Every Lifter Makes". Too generic, no specific failure mode named, slips into listicle territory

### Pattern T-4: {add patterns as research surfaces them}

{populated}

## Considered + dropped

Title patterns AI proposed during research or the creator surfaced and dropped after consideration. Rationale captured so future quarterly refreshes do not re-surface them.

> [!quote] Dropped pattern: {label}
> Template: `{template}`
> Rationale: {one-liner}
> Bucket: {tone-mismatch | audience-sophistication | brand-off-axis | authority-conflict | trend-chasing | other}
> Date: {YYYY-MM-DD}

## Pattern combinations

Some patterns combine. Worked examples of combinations the creator's audience responds to:

- T-1 + T-3: "Why I Quit [Mistake] After Coaching 100+ Lifters". Combines reversal authority with diagnosis
- {others as discovered}

## Field reference

- **Template**: the fill-in-the-blank structure. [SLOTS] are variables.
- **Pattern shape**: what the structure DOES (the narrative or psychological hook).
- **Confidence**: HIGH / MEDIUM / LOW. How broadly the structural pattern held across the research set. No raw counts (the count anchors the AI on frequency rather than fit).
- **Why this lands**: the psychological or narrative reason the pattern resonates.
- **Worked examples**: real titles from the research set, linked back to their outlier rows in `pattern-bank.md` for full context (view count, multiplier, thumbnail).
- **Near-miss anti-pattern**: broken example showing how the pattern fails when slots are missing or vague.
- **When NOT to use**: explicit guard against misuse (creator authenticity, audience fit).
