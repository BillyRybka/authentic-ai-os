---
name: vid-voice-audit
description: Pre-publish voice check. Reads the finished script against the creator's reference pieces, the voice-profile guardrail (its refusals carry the creator's banned words and required swaps), and optional raw transcript samples, and returns every line that fails the read-aloud test with severity, location, quote, and a suggested rewrite in the creator's voice. Plus a per-beat verdict (passes / soft-flag / would-reword) so the creator sees at a glance which beats are clean. Callable standalone as the last gate before filming, or invoked as a sub-skill by vid-pressure-test in place of an inline voice reviewer. Triggers on "audit my voice", "check the voice", "voice audit", "does this sound like me", "is the voice right", "run voice audit", "voice check before filming", or whenever a writing skill or orchestrator needs a deep voice check.
---

# Voice Audit

The voice check. One source of voice-truth for the whole system. Reads the assembled draft against the creator's actual past sentences and flags any line that fails the read-aloud test.

This skill exists because parallel quick reviewers drift. A 137-line top-3-capped reviewer inside a multi-agent pressure-test is fast, but it has to compete with three other reviewers for the same finding budget. The audit drops that cap, loads more material, samples raw transcripts to keep the curated set honest, and returns a per-beat verdict alongside the flat finding list.

> **Resolving `knowledge/` paths.** Any path written `knowledge/X.md` is a plugin reference file. Load it from `${CLAUDE_PLUGIN_ROOT}/knowledge/X.md` when running as an installed plugin. If `${CLAUDE_PLUGIN_ROOT}` is unset or that path does not exist (running from the source repo during development), load `knowledge/X.md` relative to the repo root instead.

## What this produces

Two structured outputs per run:

1. **Findings list.** Every line that fails the rubric, ranked by severity. No top-3 cap. Each finding: `severity`, `location`, `quote`, `issue`, `suggested_rewrite`. Format spec in `references/voice-fault-rubric.md`.
2. **Per-beat verdict map.** Every named beat (hook, each segment by index, ending) gets one of: `passes` / `soft-flag` / `would-reword`. The creator sees at a glance which beats are clean and which need attention.

Nothing else is written. No file is created. The audit is a read-and-report operation; pressure-test or the creator decides what to do with the findings.

## Invocation modes

**Standalone.** The creator runs it directly. Last gate before filming when they want a deeper check than pressure-test's batch run. Returns findings + verdict in chat.

**Sub-skill.** `vid-pressure-test` invokes it as one of its parallel reviewers (replacing the inline voice-authenticity rubric). Returns findings in the same structured shape pressure-test's Phase 3 consolidator already expects (location, quote, issue, suggested rewrite). Pressure-test does the dedup-merge across reviewers and the interactive walk.

## When to run

- After the full script (intro + body + ending) is assembled and before filming.
- Inside `vid-pressure-test` Phase 2 as the voice reviewer.
- After a `vid-voice-update` hard-rule append, to confirm the in-progress draft now picks up the new refusal.
- When the creator says "does this sound like me?" or "something feels off about the voice."

## Prerequisites

Hard requirements:
- `content/pieces/{slug}/script.md` exists with no stub sections (intro + all segments + ending all written)
- `foundation/voice-profile.md` exists (the guardrail: refusals, including words-avoided and any required swaps, plus signature phrases and POV/energy)

Soft requirements:
- `foundation/reference-pieces/{voice_context}.md` exists for the piece's voice_context. If absent, voice-fingerprint and refusals carry the audit alone and the gap is noted in the output (the creator needs to capture sources for that context).
- `raw/voice-sources/` exists with at least one transcript matching the piece's voice_context. If present, the audit samples 2-3 random passages per run. If absent, that step is skipped silently.

If the hard requirements are missing, the audit refuses to run and tells the creator which file is missing.

## Load at session start

Silent loads (do NOT paste into chat):

1. `content/pieces/{slug}/piece.md` (for `voice_context`, default `youtube-script`)
2. `content/pieces/{slug}/script.md` (the audit target)
3. `foundation/voice-profile.md` (the guardrail)
4. `foundation/reference-pieces/{voice_context}.md` (the gold-standard passages, `## ` sections inside; the seed for rhythm comparison)
5. `knowledge/voice-profile-schema.md` (refusal shape, signature-phrase definition)
6. `references/voice-fault-rubric.md` (severity tiers, output schema, worked examples)

Deferred load: raw-source sampling happens in Stage 1 only if `raw/voice-sources/` exists.

## FIRST ACTION: create the task list

After loads:

1. Optional raw-source sample (pick 2-3 if folder exists, varies between runs)
2. Stage 1: Line-by-line scan against rubric
3. Stage 2: Per-beat verdict
4. Stage 3: Suggested rewrites for every finding
5. Stage 4: Return findings + verdict map

Mark `in_progress` on start, `completed` when the creator has the report (standalone) or pressure-test has consumed the result (sub-skill).

## Optional raw-source sampling

If `raw/voice-sources/` exists, list the files matching the piece's `voice_context` (by filename prefix or content tag if available, otherwise all .txt/.md files in the folder). Pick 2-3 at random. Read a 1-3 paragraph passage from each.

The point is not to compare every line of the script against every raw passage. The point is to keep the curated reference set honest. Curated passages can drift toward what the creator likes to see; raw transcripts are unfiltered. If the script's rhythm and word choice match the curated set but feels off against a raw sample, that is a calibration signal for the rubric pass.

Use the samples as background context during Stage 1, not as a separate scoring axis. If they reveal a fault the rubric missed (a word the creator routinely uses that the script avoided, a rhythm habit absent from the curated set), surface it.

If the folder is missing or empty, skip silently. Note in the output: "raw-source sampling: skipped (no raw/voice-sources/ for {voice_context})."

## Stage 1: Line-by-line scan

Read `script.md` sentence by sentence. For each sentence, apply the `references/voice-fault-rubric.md` checks:

**Hard severity** (voice violation; would fail a pressure-test gate):
- Word from `voice-profile.md` `refusals` words-avoided used in the line
- Anti-pattern from `voice-profile.md` `refusals` present (contrast-template, hedge stack, etc.)
- Creator hard rule breached (a never-script moment scripted, a peak intensity device carpet-bombed)
- Word with a required swap in `voice-profile.md` `refusals` used without applying the swap
- Em-dash anywhere

**Soft severity** (worth flagging, creator may keep):
- Rhythm mismatch against reference pieces (uniform sentence length where the references vary; clipped where the references breathe; run-on where the references stay tight)
- Energy mismatch (line is flat where references hit harder, or amped where references stay calm)
- AI-default phrasing (reads like a Claude default rather than something the creator would say out loud)
- Generic phrasing where the creator usually goes specific

Every flagged sentence gets the four-field finding shape: `severity`, `location` (section + line number), `quote` (exact text from script.md), `issue` (one-sentence diagnosis). No hand-waving. No "this segment feels off" without a quote.

No cap. Surface every line that fails. Ranking happens in Stage 4.

## Stage 2: Per-beat verdict

The script has named beats: hook (the opener line of the intro), each segment by index, ending. For each beat, judge the whole beat (not individual lines):

- **passes**: zero hard findings; soft findings if any are minor or stylistic
- **soft-flag**: one or more soft findings affecting the beat's overall feel; no hard findings
- **would-reword**: at least one hard finding, OR the beat as a whole reads like the creator would reword it on camera

The verdict is a gestalt judgment over the rubric findings + the raw-sample calibration + the read-aloud feel. Not just a sum of severities. A beat with no rubric findings can still be `would-reword` if the rhythm is plainly the creator's defaulted-to AI cadence, not theirs.

## Stage 3: Suggested rewrites

For every finding from Stage 1, write a suggested rewrite. The rewrite must itself pass the read-aloud test: read it in your head as if the creator is speaking it on camera. If you would reword it, do not suggest it.

Rewrites preserve the structural role of the line (a hook stays a hook; a transition stays a transition; a CTA stays a CTA). Only the voice changes.

If you cannot find a rewrite that passes the read-aloud test, write `suggested_rewrite: "REWRITE NEEDED, pull from the creator's brain-dump or reference pieces"` and the creator will supply it.

## Stage 4: Return findings + verdict

Output schema (consumed by pressure-test in sub-skill mode and rendered for the creator in standalone mode):

```yaml
findings:
  - severity: hard | soft
    location: "{section} line {N}"
    quote: "{exact text}"
    issue: "{one-sentence diagnosis}"
    suggested_rewrite: "{the line in the creator's voice}"
verdict_map:
  hook: passes | soft-flag | would-reword
  segment_1: passes | soft-flag | would-reword
  segment_2: ...
  ending: passes | soft-flag | would-reword
raw_source_sampled: true | false
voice_context: youtube-script | tutorial | shorts | newsletter | linkedin | twitter | podcast | casual | talk
notes:
  - "reference set absent for {voice_context}; fingerprint + refusals only"
  - "raw-source sampling: skipped (no raw/voice-sources/)"
```

Standalone mode: render the schema as a clean report in chat. Hard findings first, then soft, grouped by beat. Per-beat verdict map summarized at top. Notes at the bottom.

Sub-skill mode: return the schema as-is to the caller. No chat output.

## Closing the skill

Standalone mode: after rendering, stop. The audit reports; the creator decides what to fix. Do not auto-edit script.md. The pressure-test interactive walk is where edits happen.

Sub-skill mode: hand the schema back to pressure-test and exit. Pressure-test consolidates with the other reviewers and runs Phase 4.

## Failure modes

- **No reference pieces for voice_context.** Pass 2 grain comparison is partial. Flag in `notes` and run anyway from fingerprint + refusals.
- **No raw/voice-sources/.** Sampling skipped silently. Curated set carries the rhythm check.
- **Script has stub sections.** Refuse to run. "Script not complete. Finish writing first." (Pressure-test catches this in Phase 1 too; the audit is defensive.)
- **All findings clean.** Suspicious silence. Flag in `notes`: "audit ran, zero findings. Either the script is exceptional or one rubric class is reading too generously. Recommend creator read-aloud anyway."
- **The creator disputes a finding.** Do not argue. The read-aloud test is the final arbiter. If the creator says the line is fine, it is fine. Note the disagreement and move on. Repeated disagreements on the same fault class are a signal the reference set or rubric needs a refresh.

## Anti-patterns

- Capping findings at top 3 (that was the parallel-reviewer pattern; the audit drops the cap)
- Reading the curated reference set as gospel without the raw-sample sanity check
- Flagging "this segment feels off" without a specific quote
- Suggesting a rewrite that itself fails the read-aloud test
- Auto-editing script.md from inside this skill (the audit reports; pressure-test or the creator edits)
- Inventing findings to hit a quota (anti-fabrication: every flag cites a real quote and line)
- Treating all soft findings as equal (rank within severity; a flat opener in a hook beat is graver than a generic word in a body line)

## References

- `references/voice-fault-rubric.md`: severity tiers, sources of truth, worked examples, suggested-rewrite discipline, output schema.
- `knowledge/voice-profile-schema.md`: the voice-profile.md contract (refusal shape, signature phrases).
- `knowledge/voice-pressure-test.md`: how validation works system-wide (this skill is the validation, but the broader contract lives there).
- `knowledge/voice-rhythm.md`: the by-ear lens for judging rhythm mismatch.

## Related skills

- `vid-voice-capture` builds the voice this skill reads against
- `vid-voice-update` writes a new refusal mid-draft; this skill picks it up on the next run
- `vid-pressure-test` invokes this skill as reviewer 2 in Phase 2
- `vid-intro`, `vid-segment`, `vid-ending` write the script this skill audits
