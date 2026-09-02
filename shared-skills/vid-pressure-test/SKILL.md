---
name: vid-pressure-test
description: Catch-and-fix the script before filming. Runs 4 parallel adversarial reviewers (source-traceability, voice-authenticity, AI-slop, retention-logic) against the assembled script. Each returns top 3 issues only. Walks hard issues with the creator in an interactive approve/deny/skip loop, applies approved rewrites to script.md in place, then ends with a creator read-aloud as the final gate. Goal-aware, format-aware. Output is a script ready to film. Trigger on "pressure test", "audit the script", "review before filming", "check the script", "is this ready to film", "find what's wrong", "stress test this", or any downstream pipeline that needs the script audited before recording.
---

# Video Pressure Test

Last-mile audit of the assembled script before filming. Catches emergent cross-section problems individual writing skills can't see (title-promise pays off too early, threads that never close, intro promises body doesn't deliver, fabricated claims). Fixes them in place. Ends with creator read-aloud as the final gate.

**Scope boundary:** this skill audits a fully-written script. It does not write segments (`vid-segment`), endings (`vid-ending`), titles (`vid-title`), thumbnails (`vid-thumbnail`), or intros (`vid-intro`). If the script is stubbed, hard-stop and tell the creator to finish writing first.

## What this produces

A script.md that is filmable. The skill EDITS the script in place during the interactive loop. piece.md gets a `pressure_test_audit` block written to frontmatter (run date, hard/soft counts, verdict, soft issues list). No separate pressure-test.md file. The script is the deliverable; the frontmatter block is the receipt.

## When to run this

- The full script (intro + all segments + ending) is written and the creator is preparing to film
- The creator wants to rewrite specific sections after critique and re-verify
- `vid-pipeline` invokes after `vid-ending` completes and before filming

## Prerequisites

Hard requirements:
- `content/pieces/{slug}/script.md` exists with intro + all body segments + ending all written (no stub sections)
- `content/pieces/{slug}/piece.md` exists with `frame`, `format`, `goal` locked
- `content/pieces/{slug}/brain-dump.md` exists (claim traceability source)
- `foundation/avatar.md`, `foundation/credibility.md`, `foundation/voice-profile.md` (the refusals section carries the banned phrases and required swaps)

Soft requirements:
- `foundation/reference-pieces/{voice_context}.md` (the gold-standard passages as `## ` sections, loaded by `vid-voice-audit` when reviewer 2 runs, matched to piece.md `voice_context`)
- `raw/voice-sources/` (optional; if present, `vid-voice-audit` samples 2-3 raw passages per run for calibration)
- `banks/story-bank/`, `banks/proof-bank/`, `banks/metaphor-bank/`, `banks/testimonial-bank/`, `banks/framework-bank/` (used material traceability)

## Invocation modes

**Standalone:** creator invokes with a slug ("pressure test the ADHD planning piece"). Skill runs the audit, walks hard issues interactively, ends with read-aloud.

**Sub-skill:** `vid-pipeline` invokes after vid-ending completes. Same flow. Returns a status packet on completion (`{verdict, hard_issues_resolved, soft_issues_count}`).

**Re-audit mode:** detected when piece.md already has `pressure_test_audit` from a prior run. Surface prior soft issues + ask "audit fresh, or focus on the previously-flagged soft issues?" Default to fresh audit if the script has been edited since the prior run.

## The 6 phases

### Phase 1: Load + condition rubrics

Silent loads (do NOT paste into chat):

1. `content/pieces/{slug}/script.md` (the full audit target)
2. `content/pieces/{slug}/piece.md` (goal, format, voice_context drive rubric weighting)
3. `content/pieces/{slug}/brain-dump.md` (traceability source)
4. `foundation/avatar.md` (avatar, Top 3) and `foundation/credibility.md` (the three proof points)
5. `foundation/voice-profile.md` (the thin guardrail: refusals, signature phrases, POV/energy. Contract in `knowledge/voice-profile-schema.md`)
6. `foundation/reference-pieces/{voice_context}.md` (the voice engine: real intact passages as `## ` sections, matched to piece.md `voice_context`, default `youtube-script`. The gold standard for the read-aloud test)
7. `knowledge/script-tension-architecture.md` (retention-logic source)

Deferred loads: `knowledge/format-planners/{format}.md` and `knowledge/attention-craft.md` (beat pacing, pattern interrupts, mid-beat re-engagement) load only when the retention-logic reviewer fires in Phase 2 (they are its only consumers; no point loading at Phase 1).

**Hard friction checks during load:**

- script.md has any stub section (e.g. `## Segment 3` with empty body) → reject. "Script not complete. Finish writing segment N first."
- piece.md missing `frame` or `format` → reject. "Run vid-framing first."
- brain-dump.md missing → reject. "Run vid-braindump first."
- foundation docs missing → reject. "Run /foundation sequence first."

**Rubric weighting from piece.md:**

Adjust each reviewer's emphasis based on piece context. Weights are not numbers; they are which checks fire harder.

- `goal: sales` → source-traceability and retention-logic weighted heavier (claim accuracy matters for buyer trust; ending CTA clarity scrutinized)
- `goal: views` → retention-logic and AI-slop weighted heavier (cold viewers leave fast on slop and on flat retention curves)
- `goal: emails` → retention-logic + ending lead-magnet specificity scrutinized
- `format: success-story` → narrative arc retention rules apply (one rising arc, outcome lands late, story traceability strict)
- `format: list-video` → item-progression retention rules apply (N+1 > N expectation; named lesson lands late)
- `format: step-by-step` → step compounding retention rules (each step a small payoff; full method at step-end)
- `format: deep-dive` → cross-lesson thread tracking strict (concept threads layered)
- `format: news` → tight retention compression (named answer can't wait as long)
- Audience temperature is DERIVED, not read from a field: judge cold/warm/hot from the finished script itself (topic breadth, how much trust the framing assumes, whether the CTA presumes the viewer knows the creator). Cold → AI-slop tighter (cold viewers have no trust to spend on weak prose). Hot → CTA scrutiny tighter (hot viewers need a clear next step).

See `references/rubric-conditioning.md` for the full conditioning matrix.

### Phase 2: Run 4 reviewers in parallel

Always multi-agent. No mode prompt. Each reviewer is a fresh-context Task spawn with its own rubric and scope. Reviewers do not see each other's findings.

**Reviewer 1: source-traceability** (`references/reviewer-source-traceability.md`)

Every claim, number, name, story, metaphor, framework, statistic, and quoted phrase in the script must trace to brain-dump.md, foundation docs, or banks. Untraceable = flag. Returns top 3 unsupported items with quote + location + suggested fix.

**Reviewer 2: voice-authenticity** (invokes `vid-voice-audit` as a sub-skill)

Invoke `vid-voice-audit`. It loads `foundation/reference-pieces/{voice_context}.md` (the gold standard for grain) and the voice-profile.md guardrail (the refusals carry the creator's banned words and required swaps, plus signature phrases and POV/energy), and optionally samples 2-3 raw passages from `raw/voice-sources/`. It returns the full findings list ranked by severity plus a per-beat verdict map (hook / segment_N / ending → passes / soft-flag / would-reword). Take the top 3 hard findings (severity-ordered, preferring hard over soft) for this reviewer slot in Phase 3 consolidation. Preserve the audit's per-beat verdict map and the remaining findings; the verdict map appears in the chat summary in Phase 6 and the remaining findings go to `soft_issues_list` in piece.md frontmatter.

**Reviewer 3: AI-slop** (`references/reviewer-ai-slop.md`)

Scans for banned phrases (transition-patterns Tier 1 + the house banned-word rules + voice-profile.md refusals), vague hedges, announcing transitions, AI tells (em-dashes, three-item-list crutch, generic value language). Returns top 3 worst offenders with quote + suggested removal or replacement.

**Reviewer 4: retention-logic** (`references/reviewer-retention-logic.md`)

Reads script against script-tension-architecture.md and format-planners/{format}.md. Checks: intro Setup's Top 3 questions are actually delivered in the body, title-promise resolves at the segment `tension_plan` assigns (format-table fallback when the plan is absent), opened threads close, each segment serves the locked frame, ending pivots correctly per goal and the audience temperature derived from the script. Returns top 3 retention risks with location + diagnosis + suggested restructure.

**Hard cap: top 3 per reviewer.** Forces severity ranking. Soft cap discipline is the discipline that keeps the audit tractable.

**Anti-fabrication:** every flagged issue cites a specific quote and line location from script.md. No "the segment feels off" hand-waving.

### Phase 3: Consolidate + rank

Merge all 4 reviewer outputs. Dedup overlaps (same line caught by voice + AI-slop merges; keep both attributions for context). Classify each issue:

- **Hard issue:** factual break (fabricated claim), banned-phrase violation, retention-killer (early payoff, orphaned promise), voice violation against a guardrail refusal (word avoided, anti-pattern, or breached creator hard rule)
- **Soft issue:** stylistic preference, hedge to consider, minor rhythm tweak, retention risk worth flagging but not blocking

Rank hard issues by severity (factual breaks first, then voice violations, then retention).

### Phase 4: Walk hard issues interactively

One at a time. Surface to creator with a clean block:

```
Hard issue 1 of N
Reviewer: {source-traceability | voice-authenticity | AI-slop | retention-logic}
Location: {section} line {N}
Quote: "{exact text}"
Issue: {diagnosis in one sentence}

Suggested rewrite:
  "{specific replacement text in the creator's voice}"

Approve / Deny (write your own version) / Skip
```

**Approve** → edit script.md, replace the quote with the suggested rewrite. Move to next issue.

**Deny** → creator pastes their own version. Skill applies that text to script.md. Move to next issue.

**Skip** → accept as written, move to next issue.

**Skip restriction on hard-rule violations.** If the issue is a factual break (fabricated number, named claim with no source) OR a banned-phrase violation (a house banned word or a voice-profile refusal) OR an em-dash, Skip is NOT allowed. Creator must Approve, Deny+rewrite, OR Mark-as-gap. Mark-as-gap writes the issue to piece.md frontmatter under `claims_to_source_before_filming: [...]` and blocks the "ready to film" verdict until resolved.

**Light-vet creator rewrites before applying.** When the creator Denies and pastes their own version, scan that text BEFORE writing to script.md:

- Any house-banned word or phrase → surface inline: "Your rewrite has '{phrase}' which is on the house banned list. Want to revise, or skip?"
- Any word avoided from the guardrail refusals → surface inline: "'{word}' is a refusal in your voice guardrail. Revise or accept?"
- Em-dashes → surface inline: "Your rewrite has an em-dash. Replace with period/comma/parentheses?"
- Hedges from voice-profile anti-patterns → surface inline: "'{hedge}' undermines stakes per your voice-profile. Tighten or accept?"

One-pass check. If creator accepts the violation knowingly, apply and move on. Don't loop.

See `references/interactive-fix-loop.md` for worked dialogues.

### Phase 5: Creator read-aloud (the final gate)

After all hard issues resolved, the script has been edited. Now the source-taught discipline fires.

Ask the creator:

> "Read script.md aloud start to finish. Take 3 minutes. Would you reword anything?"

Wait. Three possible answers:

- **No, would not reword anything** → script is filmable. Proceed to Phase 6.
- **Yes, would reword X** → creator names the section/sentence. Apply their version to script.md. Ask again: "Reread it. Anything else?" Loop until clean.
- **Yes, but I want to think on it overnight** → save state with `pressure_test_status: read-aloud-pending` in piece.md. Skill ends. Resume on next invocation.

**Soft cap on re-read cycles.** After 2 re-read cycles where the creator keeps finding rewordings, the script is signaling deeper structural drift. Surface proactively: "You've reworded twice. Sometimes the third read reveals it is the frame or the format, not the lines. Want to save state and come back tomorrow, or push through one more?" Creator picks. Avoids 10:30pm spiral.

The read-aloud test is non-negotiable. If the creator would reword anything when speaking, the script is not ready. This is the final arbiter; not the reviewers.

### Phase 6: Update piece.md + surface soft issues + verdict

Write the audit block to piece.md frontmatter (append, do not overwrite other fields):

```yaml
pressure_test_audit:
  ran_at: {YYYY-MM-DD}
  mode: multi-agent
  hard_issues_caught: {N}
  hard_issues_resolved: {N}
  soft_issues: {N}
  verdict: ready-to-film | needs-revision | read-aloud-pending
  read_aloud_passed: true | false
  claims_to_source_before_filming: []
  soft_issues_list:
    - reviewer: voice-authenticity
      location: Segment 3 line 4
      quote: "..."
      diagnosis: "..."
pressure_test_status: passed | issues-flagged | resolved
pressure_tested_at: {YYYY-MM-DD}
status: filming-ready              # ONLY when the verdict is ready-to-film. Leave status: drafting for needs-revision or read-aloud-pending.
last_updated: {YYYY-MM-DD}
```

`status: filming-ready` is the pipeline's done signal: vid-pipeline reads it and stops. Set it only when the verdict is ready-to-film. For needs-revision or read-aloud-pending, leave `status: drafting` and bump `last_updated` only.

Then surface a clean chat summary:

```
Pressure test complete.

Hard issues: {N} caught, {N} resolved.
Soft issues: {N} logged in piece.md (not blocking).
Read-aloud: {passed | pending}.

Verdict: Script ready to film.
```

OR:

```
Verdict: Script needs revision.
- {issue} (you marked it to defer; resolve before filming)
- claims_to_source_before_filming: {list}
```

**STOP.** Do not move to vid-pipeline next phase. Do not auto-publish. Filming is the creator's action.

## Sub-skill mode handoff

vid-pipeline reads `pressure_test_audit` from piece.md frontmatter directly. No separate output packet; the frontmatter block IS the structured handoff.

## Conversational discipline

- **Listen during dumps.** If the creator pushes back on a flagged issue with 3+ sentences of reasoning, hear it all before responding.
- **One issue at a time.** Don't batch hard issues into a 12-item list and ask "which to fix?" That breaks focus and creates decision paralysis.
- **Surface rewrite candidates that match the creator's voice.** Every suggested rewrite passes the read-aloud test in your head before you show it. If you'd reword it on camera, don't suggest it.
- **No NPC ticking.** When the creator says "obvious, just fix it," apply without re-prompting. Bulk-keep mode for confident creators.
- **The read-aloud test is the final word.** Even if all 4 reviewers passed, if the creator would reword a line when speaking, the script failed. Restructure without argument.

## Hard friction (auto-flag, stop)

1. script.md incomplete (any stub section) → redirect to vid-segment, vid-intro, or vid-ending
2. piece.md missing frame or format → redirect to vid-framing
3. brain-dump.md missing → redirect to vid-braindump
4. Foundation docs missing → redirect to /foundation
5. Em-dashes in any productized output (this skill's chat, suggested rewrites, frontmatter)
6. Attribution leaks in productized output (no named-source language)
7. Fabricated issue surfacing (reviewer cites a quote that isn't in script.md) → fail and re-run reviewer
8. Skip attempted on hard-rule violation → block, force Approve or Deny+rewrite or Mark-as-gap

## Soft friction (surface and explain, creator decides)

1. All 4 reviewers passed clean → flag suspicious silence ("audit ran, zero issues caught. Either the script is exceptional, or one of the reviewers is reading too generously. Read aloud anyway to confirm.")
2. Creator denies 3+ suggested rewrites in a row → flag pattern ("you're rejecting my voice-match attempts. Want to paste a reference piece so I can recalibrate?")
3. Re-audit mode invoked but script unchanged → flag ("script hasn't changed since last pressure test. Same issues will surface. Run anyway, or revise first?")
4. Read-aloud pending and skill re-invoked → flag ("you have a pressure test in read-aloud-pending state. Resume that, or start fresh?")

## Reference index

| File | When to read it |
|---|---|
| `references/reviewer-source-traceability.md` | Phase 2, reviewer 1 rubric and worked examples for claim-tracing failures |
| `vid-voice-audit` (skill, invoked by name as a sub-skill) | Phase 2, reviewer 2. Voice check with full findings + per-beat verdict |
| `references/reviewer-ai-slop.md` | Phase 2, reviewer 3 rubric, banned-phrase list pointers, AI-tell examples |
| `references/reviewer-retention-logic.md` | Phase 2, reviewer 4 rubric, format-aware retention checks |
| `references/rubric-conditioning.md` | Phase 1, the goal × format weighting matrix (temperature is derived from the script, not a stored field) |
| `references/interactive-fix-loop.md` | Phase 4, worked dialogues for Approve / Deny / Skip / Mark-as-gap / light-vet violations |
| `assets/pressure-test-frontmatter.md` | Phase 6, the exact YAML block appended to piece.md |
| `knowledge/script-tension-architecture.md` | Phase 1 + Phase 2 reviewer 4, cross-segment tension rules |
| `knowledge/attention-craft.md` | Phase 2 reviewer 4, beat pacing, pattern interrupts, and re-engagement ear tests |
| `knowledge/format-planners/{format}.md` | Phase 2 reviewer 4, format-native retention arc |
| `foundation/voice-profile.md` `refusals` | Phase 2 reviewer 2 + reviewer 3, the creator's banned words and required swaps |

## Principles (the why)

- **The audit's success metric is a better script, not a longer report.** No pressure-test.md file. The script is the deliverable.
- **4 independent reviewers catch what 1 unified pass misses.** Each fresh-context spawn focuses on one rubric without bleed. Multi-agent isn't ceremony; it's the discipline that makes the audit honest.
- **Top 3 per reviewer is severity discipline.** Surfacing every issue creates nitpick fatigue. The 3 worst per lens force the creator's attention to what actually matters.
- **Creator read-aloud is the final arbiter.** Reviewers can pass clean and the script can still fail the creator's mouth. The mouth is the truth test.
- **Skip is restricted on hard-rule violations.** A skipped fabricated claim ships a lie. The audit refuses to call that "ready to film."
- **Light-vet creator rewrites before applying.** A creator's fix can introduce a new violation. Catch it once, inline, then move on. Don't re-loop.
- **Anti-fabrication applies to reviewers too.** Every flagged issue cites a specific quote and line. Reviewers don't invent problems.

## Related skills

- `vid-segment`, `vid-intro`, `vid-ending` write the script this skill audits
- `vid-structure` writes the skeleton that the body skills filled
- `vid-framing` locks the frame the reviewers test against
- `vid-braindump` produced the brain-dump that source-traceability checks
- The `/foundation` chain produced the `foundation/` files; `vid-voice-capture` produced voice-profile; `vid-research` produced packaging-system
- `vid-pipeline` invokes this skill after vid-ending completes
- `vid-measurement` (future) reads pressure-test results post-publish to correlate with retention data
