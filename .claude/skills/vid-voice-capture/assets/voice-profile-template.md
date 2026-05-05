---
type: foundation
doc: voice-profile
project: youtube-content-os
status: active
date: YYYY-MM-DD
last_refreshed: YYYY-MM-DD
contexts_populated: []
tags: [foundation, voice, creator-identity]
---

# Voice Profile

This profile is a preservation checklist. It captures how the creator already speaks. Writing skills load it to validate that their output still sounds like the creator. The profile is descriptive, not prescriptive — if the creator would reword any output line when reading it aloud, the profile hasn't been applied correctly.

Two layers below: **Core** holds across every format the creator uses. **Context Maps** capture per-format flex. Writing skills load Core always, and the relevant Context Map if one exists for what they're producing.

---

## Layer 1: Core profile

Patterns that hold across every format.

### Recurring phrases

5 to 10 phrases the creator uses across formats. Real quotes pulled from sources.

- "[phrase 1]" — appears in [contexts where seen]
- "[phrase 2]" — [contexts]
- "[phrase 3]" — [contexts]
- "[phrase 4]" — [contexts]
- "[phrase 5]" — [contexts]

### Words avoided

Words the creator does not use, paired with what they use instead.

- [word] → use [replacement]
- [word] → use [replacement]
- [word] → use [replacement]

### Anti-patterns

Phrasings the creator would never write. Stronger than words-avoided. Hard reject if they appear in any output.

- "[phrasing 1]" — reason if known
- "[phrasing 2]" — reason
- "[phrasing 3]" — reason

### POV default

- "I" for: [what they use I for]
- "You" for: [what they use you for]
- "We" for: [what they use we for, or "never used as plural"]
- Other rules: [any specific POV rules]

### Energy baseline

[One phrase that captures the floor energy. Examples: "quiet confidence," "dry wit with directness," "high conviction, low volume," "performer with vulnerable beats."]

### Rhetorical baseline

Devices the creator uses across formats with frequency notes.

- Metaphor: [frequency observation]
- Rhetorical question: [frequency observation]
- Callback: [frequency observation]
- Rule of three: [yes/no, frequency]
- Understatement: [yes/no, contexts]
- Hyperbole: [yes/no, contexts]

### Sources analyzed

Every source that fed the profile, with date and context tag. Refresh runs use this to know what's already been processed.

- [Source 1, type, date]
- [Source 2, type, date]
- [Source 3, type, date]

---

## Layer 2: Context Maps

Per-format sub-profiles. Only contexts with sufficient source material are populated. Others get a stub.

### Context: `youtube-script`

*Stub note if not populated: "Context map deferred — needs more youtube-script source material before patterns can be validated."*

**Sentence rhythm:**
- Median: [N words]
- Distribution: [%] short (≤8) / [%] medium (9-20) / [%] long (21+)
- Pattern: [observed alternation pattern]

**Paragraph structure:**
- [%] single-sentence / [%] 2-3 sentence / [%] 4+ sentence

**Punctuation signature** (per 1000 words):
- Em-dashes: [N]
- Ellipses: [N]
- Parentheticals: [N]
- Semicolons: [N]
- Exclamations: [N]
- Questions: [N]

**Opener pattern:**
- [%] question / [%] declaration / [%] anecdote / [%] data-first / [%] contrarian / [%] other

**Closing pattern:**
- Style: [none / direct ask / callback / community invite / question back / series teaser]

**Energy modulation:**
- [How the creator dials energy in this context vs. baseline]

**Format-specific phrases:**
- "[phrase]" — appears in this context, absent or rare elsewhere

**Format-specific transitions:**
- [How they move between ideas in this format]

---

### Context: `newsletter`

*Same field structure as above. Populate if source material is sufficient.*

---

### Context: `linkedin`

*Same field structure as above. Populate if source material is sufficient.*

---

### Context: `twitter`

*Same field structure as above. Populate if source material is sufficient.*

---

### Context: `podcast`

*Same field structure as above. Populate if source material is sufficient.*

---

### Context: `casual`

*Same field structure. DMs, Slack, raw conversational voice.*

---

### Context: `talk`

*Same field structure. Keynotes, webinars, live talks.*

---

## Read-aloud test

After producing any output, the creator reads it aloud. If they would reword any line, the profile didn't catch what was off. Update the profile.

This is the final arbiter. Numbers can pass while the output still feels wrong. The creator's mouth knows.

## Update log

- YYYY-MM-DD: Initial profile built from [list sources]. Core populated. Context maps populated: [list].
- YYYY-MM-DD: Refresh. Added patterns from [new sources]. New context maps: [list]. Retired patterns: [list with reasons]. Conflicts surfaced for review: [list].
