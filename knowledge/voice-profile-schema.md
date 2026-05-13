---
type: reference
scope: shared
loaded_by: [vid-voice-capture, vid-foundation, vid-segment, vid-intro, vid-ending, vid-structure]
status: active
tags: [reference, voice, schema]
---

# Voice Profile Schema

Defines what fields go in `foundation/voice-profile.md`, why each one exists, and how downstream writing skills use them. The profile is structured in two layers.

## Why a schema (not freeform notes)

The voice profile is loaded by every writing skill. They need predictable fields to look up. Freeform notes get scanned inconsistently, lose patterns, and drift away from the read-aloud test. The schema prevents that.

## Two-layer structure

**Layer 1: Core profile.** Patterns that hold across every format the creator uses. Their true voice fingerprint.

**Layer 2: Context maps.** Per-format sub-profiles. Each captures the patterns that flex for a specific platform/format. Only formats with enough source material get their own map.

When a writing skill produces (say) a YouTube script, it loads Layer 1 (always) plus the YouTube context map (if it exists). Both apply during the read-aloud pressure-test.

## Layer 1: Core fields

### `recurring_phrases` (required, list)

5 to 10 phrases the creator uses across formats. Real quotes, not paraphrases. These are the strongest preservation anchors. If a draft doesn't contain at least one or echo one closely, voice drift is likely.

### `words_avoided` (required, list)

Words and phrasings the creator does not use. Often: corporate jargon, hedges, AI-tells, academic filler. Each entry pairs with its preferred replacement.

### `anti_patterns` (required, list)

Phrasings the creator would never write. Stronger than "words avoided." Examples: "Let's dive in," "But here's where it got interesting," any AI-tell. Captured from corrections, edits, or voice-rule-capture history.

### `pov_default` (required, string plus notes)

Which pronoun dominates and when. "I" for X. "You" for Y. "We" for Z. Includes any rules ("never use 'one' as a generic pronoun").

### `energy_baseline` (required, string)

The energy floor. What's true even in their lowest-energy context. Examples: "quiet confidence," "dry wit," "directness without aggression," "high conviction."

### `rhetorical_baseline` (required, list)

Devices the creator uses across formats: metaphor habit, rhetorical question habit, understatement, callback, rule-of-three, hyperbole. With frequency notes ("metaphor every 3-4 paragraphs in long-form" or "rhetorical question once per intro").

### `sources_analyzed` (required, list)

Every source that fed the profile, with date and context tag. Refresh runs need this to know what's already been processed.

### `preferred_hook_types` (optional, list)

Which of the canonical 5 hook types the creator naturally defaults to: `question`, `contrarian`, `statement`, `fact`, `credibility`. Populated when `vid-voice-capture` notices a clear pattern across captured sources. Used by `vid-intro` to weight candidate generation toward the creator's natural opening style. Empty list means no preference established yet — generate across all 5 and let the creator pick.

### `transition_style_preferences` (optional, free-form text)

How the creator naturally bridges between ideas. Examples: "uses 'Here's the thing' a lot", "rarely uses 'so' as a transition", "leans on rhetorical questions to pivot". Populated from observed patterns. Used by `vid-intro` and (later) `vid-segment` to filter candidate transitions toward the creator's voice and against patterns they don't use.

### `intro_pacing` (optional, descriptor)

Pace of the creator's opening 30 seconds. Examples: `fast` (lots of cuts, quick beats), `measured` (steady, conversational), `slow-burn` (builds tension before payoff). Used by `vid-intro` to calibrate hook length, problem/result depth, and setup tightness against the creator's natural feel.

## Layer 2: Context map fields

Each context map is a sub-section per format the creator uses. Formats without enough source material get a stub note instead.

Common context keys:

- `youtube-script`
- `newsletter`
- `linkedin`
- `twitter`
- `podcast`
- `casual` (DMs, Slack, raw conversational)
- `talk` (keynote, webinar, live talk)

Each populated context map contains:

### `sentence_rhythm` (required per context)

Short/medium/long distribution. Example: "60% short (≤8 words), 25% medium (9-20), 15% long (21+). Pattern: short-short-long, then snap back short."

### `paragraph_structure` (required per context)

Single-sentence vs multi-sentence ratio. Example: "70% single-sentence paragraphs, 30% 2-3 sentence. No 4+ sentence paragraphs in this context."

### `punctuation_signature` (required per context)

Per 1000 words: em-dash count, ellipsis count, parenthetical count, semicolon count, exclamation count. Example: "Newsletter: 8 em-dashes per 1000 words, 0 semicolons, 2 parentheticals, 1 exclamation."

### `opener_pattern` (required per context)

What % of pieces in this context open with question / declaration / anecdote / data-first / contrarian / quote. Example: "YouTube script: 70% question-opener, 20% declaration, 10% anecdote."

### `closing_pattern` (required per context)

CTA style for this format. Options: none, direct ask, callback, community invite, question back, series teaser. Example: "Newsletter: callback to opener, no direct ask. LinkedIn: question back to invite comments."

### `energy_modulation` (required per context)

Does the creator dial up or down here vs. their baseline? Example: "YouTube: dials up to performer. Email: drops below baseline to direct/dry. LinkedIn: matches baseline."

### `format_specific_phrases` (optional per context)

Phrases that are strong in this context but absent elsewhere. Example: "newsletter: 'I'll be honest with you' (7x in 12 newsletters, never appears in YouTube scripts)."

### `format_specific_transitions` (optional per context)

How they move between ideas in this format specifically. Example: "Newsletter: 'Here's the thing.' YouTube: 'But.' or 'So.' Twitter: just a line break."

## Confidence flags

Every field can carry a confidence tag:

- `confidence: high`: pattern survived cross-validation across multiple sources
- `confidence: medium`: pattern strong in 2+ sources but limited corpus
- `confidence: low`: pattern from 1-2 sources, surface for creator review
- `confidence: format-specific`: pattern only validates in one context, treat as context-map-only
- `confidence: deprecated`: pattern was true at last build but doesn't hold in new sources, kept for diff history

## How writing skills use the schema

When vid-segment, vid-intro, or any other writing skill produces output, it:

1. Loads Layer 1 (core profile). Always
2. Determines what context it's writing for (YouTube script, newsletter, etc.)
3. Loads matching Layer 2 context map if it exists, falls back to core only if not
4. Pressure-tests output against both layers
5. Flags any output line that contradicts a high-confidence pattern

See `voice-pressure-test.md` for the validation flow.

## Read-aloud test

Every section in the profile is final only when the creator says it sounds like them out loud. If the schema says "70% question-opener" but the creator reads three of their own questions and reworks them, the data is wrong (or the sources were wrong). The read-aloud test overrides the data.
