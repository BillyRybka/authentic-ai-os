---
type: worksheet
project: youtube-content-os
status: in-progress
date: YYYY-MM-DD
session: voice-capture
tags: [worksheet, voice, scratch]
---

# Voice Capture Extraction Worksheet

Scratch workspace for the multi-stage voice extraction session. Final patterns from this worksheet feed `foundation/voice-profile.md`. This file can be archived or deleted after the profile is saved.

## Stage 1: Source intake

### Available sources by context

**`youtube-script`:**
- [ ] [Source name, length, date]
- [ ] [Source name, length, date]
- [ ] [Source name, length, date]

**`newsletter`:**
- [ ] [Source name, word count, date]
- [ ] [Source name, word count, date]

**`linkedin`:**
- [ ] [Source name, word count, date]

**`twitter`:**
- [ ] [Source name, word count, date]

**`podcast`:**
- [ ] [Source name, length, date]

**`casual`:**
- [ ] [Source name, length, date]

**`talk`:**
- [ ] [Source name, length, date]

### Coverage check

- Total contexts with ≥3 pieces or ≥5,000 words: [N]
- Contexts deferred (insufficient material): [list]
- Single-format limitation? [yes/no — if yes, only core profile builds]

## Stage 2: Quantitative pass per context

### `[context-name]`

**Sentence length:**
- Median: [N words]
- Range: [shortest – longest]
- Distribution: [%] short / [%] medium / [%] long
- Pattern observation: [free text]

**Paragraph structure:**
- [%] single-sentence / [%] 2-3 sentence / [%] 4+ sentence

**Punctuation per 1000 words:**
- Em-dashes: [N]
- Ellipses: [N]
- Parentheticals: [N]
- Semicolons: [N]
- Exclamations: [N]
- Questions: [N]

**Opener clusters across pieces:**
- Question: [%]
- Declaration: [%]
- Anecdote: [%]
- Data-first: [%]
- Contrarian: [%]
- Other: [%]

**Closing clusters across pieces:**
- None: [%]
- Direct ask: [%]
- Callback: [%]
- Community invite: [%]
- Question back: [%]
- Series teaser: [%]

*Repeat the above block per context.*

## Stage 3: Qualitative pass

### Cross-context patterns (feed Layer 1 core)

**Recurring phrases (appear in 2+ contexts):**
- "[phrase]" — appears in [contexts]
- "[phrase]" — [contexts]
- "[phrase]" — [contexts]

**Words avoided (universal):**
- [word] → [replacement]
- [word] → [replacement]

**Anti-patterns (universal):**
- "[phrasing]" — reason
- "[phrasing]" — reason

**POV defaults:**
- "I" for: [usage]
- "You" for: [usage]
- "We" for: [usage or "never as plural"]

**Energy baseline:**
- [one-phrase descriptor]

**Rhetorical baseline:**
- Metaphor: [observation]
- Rhetorical question: [observation]
- Callback: [observation]
- Other: [observation]

### Per-context patterns (feed Layer 2 maps)

**`[context-name]`:**
- Format-specific phrases: [list]
- Format-specific transitions: [list]
- Energy modulation vs baseline: [up / down / matches, with note]

*Repeat per context.*

## Stage 4: Cross-validation sort

### Promote to core (Layer 1)
*Patterns that hold across 2+ contexts AND 2+ sources within each.*

- [pattern] → core
- [pattern] → core

### Keep in context map (Layer 2)
*Patterns strong in one context, weak elsewhere.*

- [pattern] → `[context-name]` map
- [pattern] → `[context-name]` map

### Drop or low-confidence
*Single-source patterns. Note for creator review.*

- [pattern] — drop, anomaly
- [pattern] — flag low-confidence for review

## Stage 5: Profile diff (if refresh)

### New patterns added since last build
- [pattern]
- [pattern]

### Patterns retired since last build
- [pattern] — reason

### Conflicts to surface for creator review
- Old: [pattern]. New evidence: [pattern]. Decision: [creator's call]

### New context maps populated this run
- [context-name]

## Stage 6: Read-aloud results

For each pattern below, did the creator confirm when reading aloud? If they reworded, the pattern is wrong — note the actual phrasing they used instead.

**Recurring phrases tested:**
- "[phrase]" — [confirmed / reworded as: "[actual phrasing]"]

**Sample CTA tested:**
- "[CTA line from profile]" — [confirmed / reworded]

**Sample opener tested:**
- "[opener]" — [confirmed / reworded]

**Per-context lines tested:**
- `[context]`: "[line]" — [confirmed / reworded]

### Patterns demoted from read-aloud rejection
- [pattern] — creator pushed back, demoted to [low-confidence / dropped]

## Stage 7: Final profile fields ready to save

Checklist before writing to `foundation/voice-profile.md`:

- [ ] Core fields populated with cross-validated patterns
- [ ] Each populated context map has all required fields
- [ ] Confidence flags applied where data was thin
- [ ] Sources analyzed list updated
- [ ] Update log entry drafted (date, what changed)
- [ ] Read-aloud results incorporated (rejected patterns dropped or demoted)

When all boxes checked, write the profile. Archive or delete this worksheet.
