---
type: worksheet
project: authentic-ai-os
status: in-progress
date: YYYY-MM-DD
session: voice-capture
tags: [worksheet, voice, scratch]
---

# Voice Capture Worksheet

Scratch workspace for the curation session. This feeds `foundation/reference-pieces/{voice_context}.md` (one file per context, passages as `## ` sections) and the thin guardrail `foundation/voice-profile.md`. Archive or delete after save. Nothing in here is a shipped artifact.

## Stage 1: Sources grouped by voice_context

List sources under the context (medium/mode) they were produced in. A context needs ~3 pieces or ~5,000 words to earn a reference set.

**`youtube-script`:**
- [ ] [source, length, date]

**`tutorial`:**
- [ ] [source, length, date]

**`shorts`:**
- [ ] [source, length, date]

**`newsletter` / `linkedin` / `twitter` / `podcast` / `casual` / `talk`:**
- [ ] [source, length, date, which context]

### Coverage

- Contexts with enough material (get a reference set): [list]
- Contexts deferred (no folder, noted in context_flex): [list]
- Single-context only? [yes/no. If yes, guardrail only, all contexts deferred]

## Stage 2: Passage selection (per context)

For each context with enough material, pick 3 to 5 passages for stylistic range, not frequency, not topic. Quant noticing (sentence-length, openers) is scaffolding only, it never gets written anywhere.

### `[context-name]`

- **High-energy peak:** [source + the trimmed passage, verbatim] / demonstrates: [one line]
- **Conversational baseline:** [passage, verbatim] / demonstrates: [one line]
- **Signature move:** [passage, verbatim] / demonstrates: [one line]
- [optional 4th/5th]

Excluded (improvised, creator-designated, becomes a refusal not a piece): [e.g. a personal never-scripted beat the creator always delivers live]

*Repeat per context.*

## Stage 3: Guardrail candidates (cross-validated)

Only things that hold across sources and contexts go here.

**voice_fingerprint (2 to 4 sentences):**
- [draft]

**signature_phrases (verbatim, cross-context):**
- "[quote]", seen in [contexts]

**refusals:**
- Anti-patterns: [phrasing, reason] (plus global: em-dashes, real profanity if applicable)
- Words avoided: [word] to [swap]
- Creator hard rules: [named rule, e.g. never script the {improvised moment}; never cadence-place {device}]

**pov_and_energy:**
- [short prose: pronoun defaults + energy floor]

**vid-intro orientation (only if clearly observed, else leave blank):**
- preferred_hook_types / transition_style_preferences / intro_pacing: [or blank]

**Single-source, dropped or flagged low-confidence:**
- [pattern], [drop / flag for creator review]

## Stage 4: Refresh diff (refresh runs only)

- New passages added to existing contexts: [context: passages]
- Contexts whose sources no longer validate (mark deprecated, keep folder): [list]
- New contexts this run: [list]
- New guardrail patterns (tag added YYYY-MM-DD): [list]
- Conflicts to surface to creator (do not auto-resolve): [old vs new, creator's call]

## Stage 5: Read-aloud results

For each item read back, did the creator confirm? If reworded, capture the actual phrasing; the original is wrong.

- Passage [context/slug]: [confirmed / swap for: ...]
- Signature phrase "[quote]": [confirmed / reworded as: ...]
- Refusal [name]: [confirmed / adjusted: ...]
- Rejected and removed: [list. If 3+ rejections, the source mix is wrong, regather]

## Stage 6: Ready-to-save checklist

- [ ] Reference passages written as `## ` sections inside `foundation/reference-pieces/{voice_context}.md` (one file per context, intact passages, one `> Demonstrates:` line each)
- [ ] Improvised moments excluded from reference pieces, captured as refusals
- [ ] Guardrail has fingerprint, signature_phrases, refusals, pov_and_energy
- [ ] vid-intro orientation fields populated only where observed
- [ ] context_flex line per populated and per deferred/deprecated context
- [ ] sources_analyzed + single update_log drafted
- [ ] No rhythm or punctuation numbers written into any file
- [ ] Everything saved was confirmed by the creator out loud

When all boxes are checked, write the files. Archive or delete this worksheet.
