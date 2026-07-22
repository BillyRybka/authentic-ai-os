---
type: reference
skill: vid-voice-audit
tags: [reference, voice, audit, rubric]
---

# Voice Fault Rubric

The rubric `vid-voice-audit` reads against. Severity tiers, sources of truth, worked examples, suggested-rewrite discipline, output schema. This file is loaded by the audit; it does not run on its own.

## What to scan

Read `script.md` sentence by sentence. For each sentence, ask:

1. Would the creator say this out loud on camera, exactly as written?
2. Does the phrasing match the grain of the reference pieces for this piece's `voice_context`?
3. Does it use any word from the voice-profile guardrail's `refusals` (words avoided)?
4. Does it match any anti-pattern or breach a creator hard rule in the guardrail's `refusals`?
5. Does it use a word that the guardrail's `refusals` marks for a required swap, without applying the swap?

## Sources of truth

In priority order:

1. **`foundation/reference-pieces/{voice_context}.md`**: the creator's real intact passages for this delivery medium, as `## ` sections. The gold standard and the seed. Read `voice_context` from `piece.md` (default `youtube-script`). If a line reads sharper or weaker than the reference pieces in the same context, that is a calibration signal. Rhythm is judged by ear against them, never against stored numbers.
2. **Raw transcript samples from `raw/voice-sources/`**: if the audit sampled 2-3 raw passages for this run, use them as a calibration check against the curated set. Curated passages can drift toward what the creator likes to see; raw transcripts are unfiltered. A rhythm habit absent from the curated set but present in the raw samples is a real signal.
3. **`foundation/voice-profile.md`**: the thin guardrail (fingerprint, signature phrases, refusals including words-avoided and required swaps, POV/energy). Constraints only. Contract in `knowledge/voice-profile-schema.md`. Global hard rules that apply to every creator (em-dashes above all) are stated in the severity tiers, not read from a file.

## Severity tiers

### Hard severity (voice violation, would block a pressure-test gate)

- Word from the voice-profile `refusals` words-avoided used in the script
- Anti-pattern from voice-profile `refusals` present (contrast-template, hedge stack, cadence-placed emphasis, scripted improvised moment, etc.)
- Creator hard rule breached (a never-script moment scripted, a peak-only intensity device carpet-bombed)
- Word marked for a required swap in the voice-profile `refusals` used without applying the swap
- Em-dash anywhere

### Soft severity (worth flagging, creator may keep)

- Rhythm mismatch against reference pieces (uniform sentence length where the references vary; clipped where the references breathe; run-on where the references stay tight)
- Energy mismatch (line is flat where references hit harder, or amped where references stay calm)
- AI-default phrasing (reads like a Claude default rather than something the creator would say out loud)
- Generic phrasing where the creator usually goes specific

## Output schema (per finding)

```
severity: hard | soft
location: "{section} line {N}"
quote: "{exact text from script.md}"
issue: "{one-sentence diagnosis: what voice rule failed and why}"
suggested_rewrite: "{the line rewritten in the creator's voice, itself passing the read-aloud test}"
```

Anti-fabrication: every flag cites a real quote and line from `script.md`. No "this segment feels off" without a specific quote. If the auditor cannot point at a line, the finding does not exist.

## Suggested-rewrite discipline

The rewrite must itself pass the read-aloud test. Read it in your head as if the creator is speaking it on camera. If you would reword it, do not suggest it.

Rewrites preserve the structural role of the line. A hook stays a hook. A transition stays a transition. A CTA stays a CTA. Only the voice changes.

When a rewrite would require content not in the brain-dump or reference pieces, use the placeholder `suggested_rewrite: "REWRITE NEEDED, pull from the creator's brain-dump or reference pieces"` instead of inventing.

## Worked examples

### Example 1: words-avoided violation (HARD)

voice-profile `refusals` words-avoided: `leverage`, `unlock`, `elevate`, `ecosystem`.

Script line: "...so you can leverage this for any video."

```
severity: hard
location: "Segment 1 line 12"
quote: "...so you can leverage this for any video."
issue: "'leverage' is a words-avoided refusal. The creator never uses it in the reference pieces."
suggested_rewrite: "...so you can use this on any video."
```

### Example 2: required swap from the refusals missed (HARD)

voice-profile `refusals` require the swap `ship` to `post` for content references.

Script line: "When you ship your next video..."

```
severity: hard
location: "Ending line 5"
quote: "When you ship your next video..."
issue: "'ship' must swap to 'post' per the voice-profile required swaps (software metaphor for content)."
suggested_rewrite: "When you post your next video..."
```

### Example 3: contrast-template anti-pattern (HARD)

voice-profile `refusals` include the anti-pattern "contrast-template (not X, but Y)".

Script line: "It is not about doing more. It is about doing the right things."

```
severity: hard
location: "Segment 3 line 1"
quote: "It is not about doing more. It is about doing the right things."
issue: "Classic contrast-template structure (not X, but Y). Anti-pattern in voice-profile refusals. Creator does not use this rhythm in reference pieces."
suggested_rewrite: "Doing more is not the move. Doing the right things is."
```

If a clean rewrite is not obvious from the surrounding context, prefer the REWRITE NEEDED placeholder over a Claude-defaulted shape.

### Example 4: rhythm mismatch from reference pieces (SOFT)

reference-pieces show the creator opens body segments with short declarative sentences (5-9 words).

Script segment 2 opens: "There are a few things I want to walk through here that took me a while to figure out, and I think they will save you a lot of time."

```
severity: soft
location: "Segment 2 line 1"
quote: "There are a few things I want to walk through here that took me a while to figure out, and I think they will save you a lot of time."
issue: "30-word run-on opener. Reference pieces show 5-9 word openers for body segments. Rhythm is off."
suggested_rewrite: "Here is what took me three years to figure out."
```

### Example 5: AI-default phrasing (HARD)

Script line: "Let me show you exactly how to dive into this strategy."

```
severity: hard
location: "Intro line 6"
quote: "Let me show you exactly how to dive into this strategy."
issue: "'dive into' is a banned transition phrase per transition-patterns Tier 1 AND a voice-profile refusal anti-pattern."
suggested_rewrite: "Here is exactly how this works."
```

## Per-beat verdict (the audit-specific layer)

After the line-by-line scan, judge each named beat as a whole:

- **passes**: zero hard findings; soft findings (if any) are minor or purely stylistic
- **soft-flag**: one or more soft findings affecting the beat's overall feel; no hard findings
- **would-reword**: at least one hard finding, OR the beat as a whole reads like the creator would reword it on camera even if no specific finding fired

The verdict is a gestalt judgment over the rubric findings + raw-sample calibration + the read-aloud feel. Not a sum of severity counts. A beat with zero rubric findings can still be `would-reword` if the rhythm is plainly a Claude default rather than the creator's.

Named beats: `hook` (the opener line of the intro), each `segment_N` by index, `ending`. Use the script.md section headers to identify boundaries.

## What this rubric does NOT catch

- Fabricated claims or unsupported numbers (that is source-traceability, a separate reviewer)
- Banned generic phrases like "in this video" that are AI tells rather than voice violations (AI-slop reviewer)
- Setup-payoff structure or thread closure (retention-logic reviewer)

If a phrase is BOTH a banned phrase (AI-slop) AND a voice violation (a voice-profile refusal), it will be caught by both in pressure-test consolidation. That is fine; pressure-test dedups and preserves both attributions for context.

## The read-aloud test as the meta-check

After surfacing findings and the verdict map, the audit asks itself: "Would the creator agree with these flags when they read the script aloud?" If two or more findings feel debatable, the audit is reading too aggressively. Re-rank. Surface only the lines that clearly fail.

The creator's mouth is the final arbiter. The audit can pass clean and the script can still fail when the creator reads it. The audit's job is to catch what the creator's first read would miss; the final read-aloud catches what the audit missed.
