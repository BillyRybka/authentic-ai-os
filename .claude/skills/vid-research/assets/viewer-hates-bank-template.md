---
type: bank
kind: viewer-hates
project: youtube-content-os
status: active
last_refreshed: {YYYY-MM-DD}
total_patterns: {N}
---

# Viewer Hates Bank

What tanks for this audience. Sourced from flop analysis on own channel + niche channels (not adjacent — flop patterns don't transfer cleanly across audiences).

Loaded by `vid-framing` to filter out angles the audience has rejected. Loaded by `vid-title` to avoid title patterns associated with flops. Loaded by `vid-pressure-test` (future) as a checklist of failure modes to scan against.

## How to read this bank

Each entry is a FLOP PATTERN — a recurring quality across underperforming videos (videos at 50% or less of channel median). For each pattern:
- The pattern label
- 2-3 example flop titles
- The hypothesis on WHY this fails for this audience
- Implications for content decisions

Flop signals are AVOIDANCE rules. They tell vid-framing, vid-title, and vid-segment what NOT to do.

## Curated flop patterns

### Flop F-1: Vague motivational without specifics

**Pattern:** titles promise mindset shifts without naming concrete techniques or programming changes

**Confidence:** {HIGH | MEDIUM | LOW} (observed in {N} flops across {M} channels)

**Member flop titles:**
- "How to Stay Consistent in Your Training" — @CoachX, 8k views (median 80k = 10% performance)
- "The Mindset That Changed My Lifting" — @CoachY, 12k views

**Why it fails for this audience:** intermediate-to-advanced audience wants programming/technique specifics. Mindset content reads as beginner-tier and gets skipped.

**Implications:**
- Vid-framing: don't surface "mindset" as a primary angle for this creator
- Vid-title: avoid the structure "How to [vague mindset state]"
- Vid-segment: motivational-only segments without concrete action steps will hurt retention

---

### Flop F-2: Beginner basics

**Pattern:** titles cover content the audience has long since mastered

**Confidence:** {populated}

**Member flop titles:**
- "How to Squat Properly (Beginner Guide)"
- "What Is Progressive Overload?"

**Why it fails:** audience moved past these topics years ago. Channel's audience is intermediate/advanced; beginner content misses the level entirely.

**Implications:**
- Vid-intake Mode 1: if creator's idea is beginner-level, flag the audience-level mismatch before saving brain-dump
- Vid-framing: surface alternate angles that re-pitch beginner topics for the actual audience level

---

### Flop F-3: {populated as research surfaces flop patterns}

---

## Phrase-level avoid list

Specific phrases observed in flops that the audience apparently dislikes. Vid-title and vid-intro should AVOID these.

| Phrase | Reason | Source |
|---|---|---|
| "{phrase}" | {why it fails} | {flop title where it appeared} |

## Title structures associated with flops

Some title structures correlate with underperformance for this audience.

### Anti-pattern: {structure label}

**Template:** `{template that flops}`

**Why it fails:** {hypothesis}

**Member flops:**
- "{flop title}"

**What to use instead:** {if a working alternative pattern exists, point at title-patterns-bank.md}

## Format-level flop signals

Some formats correlate with flops on this channel even if the format works for the niche.

- {format}: creator's own attempts in this format have flopped at {N} of {M} attempts. Audience may not respond to this creator in this format. Consider: creator weakness vs audience-format mismatch.

## Considered + dropped

Flop patterns AI proposed that the creator pushed back on (e.g., "that's not actually a flop, the topic was just early — re-test later").

> [!quote] Dropped flop pattern: {label}
> Rationale: {one-liner from creator}
> Date: {YYYY-MM-DD}

