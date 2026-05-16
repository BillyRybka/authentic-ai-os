---
type: working-notes
skill: vid-pressure-test
status: in-development
audience: dev-only
not-shipped: true
tags: [source-citations, design-decisions]
---

# vid-pressure-test — WORKING NOTES (dev-only)

Not shipped. Source citations and design decisions for the dev process. Productized files (SKILL.md, references, asset) have zero attribution leaks.

## Audit-build-audit history

### Pre-build audit-1 (2026-05-14)

3 audit agents pressure-tested the contract sketch before build:

- **Workflow Simulator:** found 5 friction points, top 3 marked `[FIX]`. Key catches:
  - Mode-prompt at start ("multi-agent or single-agent?") felt academic when creator is in verdict-brain at 8:30pm before filming
  - Skip on unsourced claims would let broken facts ship
  - Creator-rewrites aren't light-vetted before logging, can introduce new violations
- **Over-engineering Hawk:** flagged 7 trims. Most aggressive: cut multi-agent toggle, cut pressure-test.md file, cut Phase 5 re-audit, trim rubric conditioning, reduce 4 reviewers to 3.
- **Source Fidelity Critic:** flagged 4 findings. Most load-bearing:
  - `[GAP]` Creator read-aloud missing as final gate (source's central pre-filming discipline)
  - `[GAP]` Retention-logic reviewer under-specified the cross-segment tension arc
  - `[OVER]` 4 separate reviewers formalize what source teaches as one creator read-aloud (honest extension, name in WORKING-NOTES)

### Locked decisions after audit-1

- **Kill multi-agent TOGGLE, keep multi-agent DEFAULT.** Billy's call. All 4 reviewers always spawn as parallel Task subagents with fresh context. No mode prompt. Independence is the discipline.
- **Replace Phase 5 re-audit with creator read-aloud.** Source-taught. The reviewers can pass clean and the script can still fail the creator's mouth. The mouth is the truth test.
- **Skip restricted on hard-rule violations.** Fabricated claims, em-dashes, brand.md banned phrases cannot Skip. Must Approve, Deny+rewrite, or Mark-as-gap. Mark-as-gap writes to `claims_to_source_before_filming` and blocks "ready to film" verdict.
- **Light-vet creator rewrites.** When creator pastes their own version (Deny path), scan for banned phrases / words_avoided / em-dashes BEFORE writing to script.md. One-pass check, surface inline, then move on.
- **Drop pressure-test.md file.** Log audit results to piece.md frontmatter + chat summary. The script is the deliverable, the frontmatter is the receipt.
- **Keep rubric conditioning** by goal / format / viewer_stage. Audits pushed back (5% lift for complexity); Billy's earlier YES stands.

## Source citations (for dev reference only)

Source material at `c:/Users/billr/projects/business-os/Resources/references/ed-lawrence-ygs/` (read-only, never shipped, never attributed in productized files).

### What source teaches about pre-filming review

Source teaches pre-filming as a **read-aloud moment plus a structure validation pass**. The creator reads the script tight, marks pauses for the teleprompter, then warms up before filming. The discipline is single-pass and creator-final.

- Teleprompter lesson (Phase 2 Lesson 3): "When you follow the system I'll teach you, it's gonna change your life." Word-for-word script on teleprompter with intentional pauses. Read-aloud is the test.
- Phase 5 Lesson 2 (early payoff): "If you give away the point too early, there's no tension that remains... They stop paying attention or comment 'get to the point.'" Retention-logic reviewer's Gate 2 source.
- Phase 2 Lesson 4 (Presenting 101): physical warm-up before take one. Body language, energy, emphasis drills. The script is the input to presenting, not the deliverable.

### Honest extensions (named here, not in productized files)

- **4 independent reviewers** = honest extension. Source teaches one unified creator read-aloud. The productized system uses 4 fresh-context agents to compensate for Claude not being the creator's ear. Independence keeps each lens honest.
- **Top-3-per-reviewer cap** = honest extension. Source doesn't teach issue-volume management; the cap is a context-budget constraint that keeps the interactive fix loop tractable.
- **Rubric conditioning by goal/format/viewer_stage** = honest extension. Source teaches one unified check regardless of format. Conditioning is system-level adaptation to the format-aware writing skills.
- **Skip restriction on hard-rule violations** = pure system addition. Source assumes the creator's judgment is enough. Productized system enforces "you can't ship a lie even if you want to."
- **Interactive approve/deny/skip loop** = AI-workflow addition. Source treats fix-it as "rewrite and re-read." The interactive loop is efficiency optimization for the Claude-mediated flow.

### What source teaches that this skill UNDER-implements (intentionally)

- **Teleprompter scriptability check.** Source teaches marking pauses, catch-up points, and natural rhythm for the teleprompter (Phase 2 Lesson 3 of the underlying study material). This skill does not verify scriptability for presentation. Reason: not a script-quality issue at this stage; the presenting phase is downstream of the audit.
- **Camera-presence and energy match per segment.** Source teaches energy modulation per body-segment (Phase 2 Lesson 4). Voice-authenticity reviewer touches energy lightly but does not verify section-by-section presentation demand. Same reason: belongs to the presenting phase, not the script audit.

These are deliberate scope cuts. Not gaps to backfill.

## Architecture decisions

- **4 reviewers, not 3.** Hawk wanted 3 (Structural / Voice / Momentum). Workflow Sim and Source Fidelity didn't push back. Billy locked multi-agent because "each has its own job." Kept 4: source-traceability, voice-authenticity, AI-slop, retention-logic. The split is defensible:
  - source-traceability and voice-authenticity overlap occasionally (a fake quote IS a voice issue), but mostly catch different failure modes
  - retention-logic is genuinely separate (structural, not prose)
  - AI-slop is a prose pattern check that voice can miss when voice-profile is permissive

- **All 4 always run.** No skip-a-reviewer logic. Conditioning only changes ranking, never skips checks.

- **Hard cap top-3 per reviewer.** Forces severity discipline. After dedup, usually 6-9 unique issues total. Walking 9 issues interactively is the upper bound of what a creator will tolerate before filming.

- **Soft issues never walked interactively.** Hard limit. Surface as a list in piece.md + chat summary at end. Walking 12 issues kills creator energy before filming.

## File inventory

- `SKILL.md` (target <500 lines) — 284 lines
- `references/reviewer-source-traceability.md` (target <300) — ~115 lines
- `references/reviewer-voice-authenticity.md` — ~140 lines
- `references/reviewer-ai-slop.md` — ~155 lines
- `references/reviewer-retention-logic.md` — ~180 lines
- `references/rubric-conditioning.md` — ~125 lines
- `references/interactive-fix-loop.md` — ~250 lines
- `assets/pressure-test-frontmatter.md` — ~170 lines
- `WORKING-NOTES.md` (this file) — dev-only, not shipped

All productized files: 0 em-dashes, 0 attribution leaks.

## Open questions for real-world testing

- Does the read-aloud test actually fire reliably, or do creators rush past it? If creators consistently say "yes, looks good" without reading aloud, add a friction step (e.g., "paste the line you read aloud last").
- Does the light-vet catch enough creator-rewrite violations to justify the inline check, or is it mostly silent? Track via the rate of light-vet flags per session.
- Are the 4 reviewers genuinely independent in practice? If post-build audit shows reviewers reading each other's findings (context bleed), the parallel Task spawn isolation may not be working as designed.
- Is the hard cap top-3 the right number? Real creators may want 5 or want 1. Watch the friction.

## Post-build audit-2 (pending)

Will spawn 3 agents (workflow simulator / over-engineering hawk / source fidelity) against the built implementation to verify the trim held.
