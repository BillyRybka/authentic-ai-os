---
name: vid-voice-capture
description: Build or refresh the creator's voice profile by analyzing their existing content (transcripts, scripts, emails, posts) and extracting the patterns that make their voice distinctive. The profile is a preservation checklist, not a generation seed. Downstream writing skills load it to validate that structured output still sounds like the creator. Triggers on "build my voice profile", "deepen voice profile", "refresh voice profile", "extract my voice patterns", "analyze my writing voice", "voice capture", "voice analysis", "my voice profile is outdated", or when a writing skill flags voice drift in published content.
---

# Voice Capture

Builds the creator's voice profile from real source material. Multi-source extraction, cross-format pattern validation, refresh-aware. The output is `foundation/voice-profile.md`. `vid-foundation` does not write this file.

This skill loads `knowledge/vault-integration.md` at session start. The voice profile follows the foundation doc schema in that contract.

> **Resolving `knowledge/` paths.** Any path written `knowledge/X.md` (this skill also loads `knowledge/voice-extraction-methods.md` and `knowledge/voice-pressure-test.md` later) is a plugin reference file. Load it from `${CLAUDE_PLUGIN_ROOT}/knowledge/X.md` when running as an installed plugin. If `${CLAUDE_PLUGIN_ROOT}` is unset or that path does not exist (running from the source repo during development), load `knowledge/X.md` relative to the repo root instead.

## What this produces

A `foundation/voice-profile.md` with a **two-layer structure**:

**Layer 1: Core profile.** Patterns that hold across every format. The creator's true voice fingerprint:
- Recurring phrases (real quotes)
- Words they avoid plus specific word swaps
- Anti-patterns (phrasings they would never use)
- Energy level baseline
- POV default
- Rhetorical device baseline (metaphor habit, rhetorical question habit, understatement, callback)
- Sources analyzed (with dates)

**Layer 2: Context maps.** Per-format/per-platform sub-profiles where the creator's voice flexes. Each captures:
- Sentence rhythm distribution (short vs long, alternation)
- Opener patterns
- Paragraph structure ratio (single-sentence vs multi-sentence)
- Punctuation signatures (em-dash, ellipsis, parenthetical asides, semicolons)
- CTA and closing style
- Energy modulation (does the creator dial up or down here?)

Context maps are created per format the creator uses: YouTube script, email/newsletter, LinkedIn post, Twitter/X thread, podcast/talk, casual DM, and others. Only formats with enough source material to validate get their own map. Others fall back to core.

The profile is a preservation checklist. Writing skills load it, look up the right context map for what they're writing, and pressure-test their output: would the creator say this, in this way, in this format, when reading aloud?

## Invocation modes

**Standalone.** Creator runs it directly. Either the first voice-profile build after `vid-foundation`, or a refresh when the profile gets stale.

**Sub-skill.** Another skill (vid-pipeline, vid-segment) detects voice drift in produced content and invokes vid-voice-capture to rebuild from updated sources. Returns a wikilink to the refreshed profile.

## When to run this

- After `vid-foundation` completes and tells the creator to build the voice profile
- Quarterly refresh as the creator publishes more content
- After a voice shift (new audience, format, platform, tone change)
- When a writing skill has flagged repeated voice drift in output
- When the creator says "this AI doesn't sound like me anymore"

## Prerequisites

- `foundation/creator-foundation.md` must exist (positioning plus avatar drive how voice is interpreted in context)
- Source material to analyze. Minimum viable corpus:
  - 3-5 transcripts OR 30-60 minutes of recorded speech, OR
  - 15,000-20,000 words of written content (mix of formats), OR
  - Both (preferred, since cross-format patterns are the strongest signals)

If sources are thin, the skill will still run but flags low-confidence patterns in the output.

## Stages

Sequential. Each stage ends with creator approval before moving on.

**FIRST ACTION: create the task list.** Before opening Stage 1, after loading `knowledge/vault-integration.md` and silent-checking for an existing `foundation/voice-profile.md`, create a TodoWrite list with these stages:

1. Source intake and context grouping
2. Layer 1 extraction: core profile (cross-context patterns)
3. Layer 2 extraction: per-context sub-profiles
4. Pressure-test the profile (read-aloud plus simulated drafts)
5. Lock and save to `foundation/voice-profile.md`

Mark each `in_progress` when starting, `completed` when the creator confirms and you move on. Keeps the sequence honest and shows the creator what's coming.

### Stage 1: Source intake and context grouping

Ask the creator what content is available. As sources come in, group them by **context** (the format/platform/situation they were produced in). Common contexts:

- `youtube-script`: long-form video scripts and transcripts
- `newsletter`: email newsletters, long-form prose
- `linkedin`: LinkedIn posts and short essays
- `twitter`: Twitter/X threads and standalone posts
- `podcast`: interview or podcast transcripts
- `casual`: DMs, Slack messages, raw conversational
- `talk`: keynote, webinar, live talk transcripts

Confirm at least 2-3 different contexts have enough source material to validate (~3 pieces or 5,000 words each, minimum). Contexts without enough material fall back to core profile only.

Record source list and context grouping in the worksheet (`assets/extraction-worksheet-template.md`).

### Stage 2: Quantitative pass (per context)

Load `knowledge/voice-extraction-methods.md`.

For EACH context group separately, extract:

- Sentence length distribution (median, range, % short ≤8 words / % medium 9-20 / % long 21+)
- Paragraph structure ratio (% single-sentence paragraphs vs multi-sentence)
- Punctuation frequency per 1000 words (em-dash, ellipsis, parenthetical, semicolon, exclamation)
- Opener pattern clusters (% questions / declarations / anecdotes / data-first / contrarian)
- CTA/closing pattern (none / direct ask / callback / community invite / question back / series teaser)

Record numbers per context in the worksheet. These will populate per-context maps in Layer 2.

### Stage 3: Qualitative pass (cross-context first, then per-context)

Same source list, two passes:

**Cross-context pass** (feeds Layer 1 core):
- Recurring phrases the creator uses across ALL contexts (5-10 real quotes that appear in YouTube AND email AND LinkedIn)
- Words they avoid universally (jargon, hedges, pet peeves)
- Anti-patterns (phrasings they would never use anywhere, collected from corrections, edits, voice-rule-capture history)
- POV default that holds everywhere
- Energy level baseline (the floor, what's true even in their lowest-energy context)
- Rhetorical baseline (do they use metaphors everywhere? rhetorical questions everywhere?)

**Per-context pass** (feeds Layer 2 maps):
- Context-specific recurring phrases (a phrase that's huge in their newsletter but absent in YouTube)
- Energy modulation (do they dial up in YouTube performances vs dial down in casual DMs?)
- Format-specific transitions (how they move between ideas in newsletter vs how in YouTube script)

Quote real lines from sources where possible. Paraphrasing the creator's voice misses the point of the profile.

### Stage 4: Core vs context separation

Walk through every pattern from Stages 2 and 3. Sort each pattern into one of three buckets:

- **Core** (Layer 1): pattern holds across 2+ contexts AND across formats. This is true voice.
- **Context-specific** (Layer 2): pattern is strong in one context but absent or weak elsewhere. Goes in that context's map.
- **Single-piece anomaly**: pattern appeared once. Drop it.

Promote cross-context patterns to core. Keep context-specific patterns in their respective maps. The profile only includes patterns that survived this filter OR are tagged `low-confidence` for the creator to review.

### Stage 5: Assemble the profile

Use `assets/voice-profile-template.md` as the shape. Fill the Core section with cross-context patterns. Fill each context map (only the contexts that had enough source material) with context-specific patterns. Cite source quotes inline where possible.

Contexts without enough source material get a stub note: "Context map deferred. Needs more `{context}` source material before patterns can be validated."

If the existing `foundation/voice-profile.md` already has content (this is a refresh), diff sections:

- New patterns appear with `(added YYYY-MM-DD)`
- Patterns retired since last build appear in the Update log section with reason
- Conflicts between old and new are flagged for creator review, not auto-resolved
- Context maps that didn't exist before get added, not replacing core

### Stage 6: Read-aloud validation

Load `knowledge/voice-pressure-test.md`.

Pull sample lines from the Core profile and from each populated context map. Read them aloud to the creator. Ask: "Does this sound like you in this context? Anything you'd reword?"

For context maps specifically, also ask: "If you were writing a {context} piece right now, would these patterns be the right defaults?" Catches drift between captured voice and current voice in a specific format.

If the creator pushes back on a pattern, demote it. The profile only includes patterns the creator confirms when said out loud.

### Stage 7: Save

Save to `foundation/voice-profile.md`. Update the source list and update log. Confirm to the creator:

"Voice profile updated. Core profile holds {N} cross-context patterns. Context maps populated for {list contexts}. Writing skills will load the relevant context map for what they're producing. Run `vid-voice-capture` again every 20-30 published pieces or when audience/format shifts. To add a new context map, gather 3+ pieces in that format and re-run."

## Refresh triggers

The skill prompts a refresh when invoked if any of these are true:

- Last update >90 days ago
- Creator has published 20+ new pieces since last update
- Creator-foundation.md was updated (audience or positioning shift)
- Writing skill logged repeated voice drift (flagged via per-piece piece.md `voice_drift: true` field, future)

Standalone invocation always runs the full flow. Sub-skill invocation can short-circuit if profile is fresh.

## Failure modes

- **No source material.** Hard stop. Tell creator to bring transcripts, scripts, emails, or do a 10-minute live monologue. Profile cannot be built from nothing.
- **Single-context only.** Build core profile only. No context maps. Flag every pattern with `confidence: single-context` for creator review. Tell creator: "Add sources from other formats and re-run to populate context maps."
- **Two contexts but conflicting patterns.** This is exactly when context maps earn their keep. Don't average. Capture each context's patterns separately. The contradiction is the signal.
- **Read-aloud rejection of multiple patterns.** If creator rejects 3+ patterns during Stage 6, the extraction missed something fundamental. Restart with different sources or ask creator what feels off.
- **Existing profile is locked or read-only.** Do not overwrite silently. Show diff, ask permission.
- **Context map gets stale faster than core.** Core voice is stable; context maps drift as platforms evolve (e.g., LinkedIn voice in 2026 is not LinkedIn voice in 2024). Refresh context maps independently if creator says "my LinkedIn voice has evolved."

## Principles

- **The profile preserves, it does not generate.** Every field exists to help Claude validate that structured output still sounds like the creator. If a field doesn't help with that validation, it doesn't belong here.
- **Patterns from real quotes, not paraphrases.** When the profile says "the creator opens with questions," it's because we counted question-openers and have receipts. Don't write descriptions when you can write quotes.
- **Cross-validation is the bar.** Single-piece patterns are noise. Patterns that survive across formats are voice.
- **The read-aloud test is final.** If the creator wouldn't say it, the profile is wrong. Doesn't matter what the data showed.
- **Source-faithful, not creative.** This skill never invents a voice for the creator. It surfaces what's already there.

## Reference index

References live in `knowledge/` because every writing skill loads them too:

- `voice-extraction-methods.md`: multi-source extraction techniques, examples of pattern-spotting from raw text
- `voice-profile-schema.md`: every field, what it captures, why it matters for preservation
- `voice-pressure-test.md`: how writing skills validate output against the profile

Templates live in `assets/` (skill-local, only vid-voice-capture uses them):

- `voice-profile-template.md`: output shape for `foundation/voice-profile.md`
- `extraction-worksheet-template.md`: scratch workspace for the multi-stage extraction session
