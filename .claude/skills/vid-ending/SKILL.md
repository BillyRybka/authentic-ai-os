---
name: vid-ending
description: Write the close of a YouTube video using Pivot/Gap/Bridge, recap the transformation, reveal the new problem, position the next video as the fix. Format-aware CTA placement by goal. Never "ends" a video, every close pivots forward to a real, already-published video. Runnable standalone or invoked by vid-pipeline during the script phase. Triggers on "write the ending", "close this video", "outro for [video]", "what's the CTA", or when a downstream pipeline needs a locked close.
---

# Video Ending Writer

Writes the close of one video with the 3-Part End Formula: **Pivot** (recap the transformation in one sentence) → **Gap** (reveal the new problem they still have) → **Bridge** (position a specific next video as the fix). CTA placement comes from goal and format, never bolted on. A video never announces it is ending; it hands the viewer their next step.

**Scope: the close only.** No hooks, no body points, no titles, no end-screen visuals. It does not pick the next video for the creator; it asks.

**This is a conversation, not a document.** Short messages. References are for your thinking; never paste them at the creator.

## What loads, and when

Load each file at the phase that needs it. Do not front-load.

| Phase | Load | For |
|---|---|---|
| 1 | `content/pieces/{slug}/piece.md` | format, goal, pillar, locked title, selected_angle |
| 1 | `content/pieces/{slug}/script.md` | the body's actual transformation language, and the `## Intro` verbatim (Setup contract, hook type, poked problem, woven credibility) for the callback rules |
| 1 | `foundation/creator-foundation.md` | avatar + Top 3 problems (the Gap names a real one) |
| 1 | `knowledge/format-planners/{format}.md` | this format's close shape; the planner is authoritative |
| 1 | `references/end-screen-design.md` | how to pick the next video (converts for this goal, logical next watch) |
| 2 | `foundation/voice-profile.md` + `foundation/reference-pieces/{voice_context}.md` | the guardrail and the voice engine. Voice only, not structure: if a passage's arc conflicts with Pivot/Gap/Bridge, the spec wins |
| 2 | `references/pivot-gap-bridge-shapes.md` | the formula's worked shapes and contrasts |
| 2 | `knowledge/transition-patterns.md` Sections 3 + 4 | BE-1..BE-8 close patterns, banned-phrase tiers |
| 2 | `references/cta-placement-by-format.md` | which goal x format CTA combinations work, which tank |
| 2 | `references/ending-anti-patterns.md` | banned phrases and the failure mechanism behind each |
| 2, conditional | `knowledge/story-pulling-criteria.md` / `proof-placement-rules.md` (+ `visual-proof-callouts.md`) / `metaphor-integration.md` / `parable-decision-matrix.md` | only if the close actually pulls a story, cites proof, frames with a metaphor, or opens on a fresh emotional beat. Endings are claim-light; most runs skip all four |
| 4 | `knowledge/voice-pressure-test.md` + `knowledge/voice-rhythm.md` | the two-pass voice check, judged by ear |
| 4 | `knowledge/vault-integration.md` | update-both-sides rule for any bank pull |

## Prerequisites

- `content/pieces/{slug}/script.md` has the FULL body written and a non-stub `## Intro`. Partial body → hard stop: "Run `vid-segment` for every section first." Stub intro → hard stop: "Run `vid-intro` first; the close calls back to the opening."
- `content/pieces/{slug}/piece.md` with `format`, `goal`, `pillar`.
- `foundation/creator-foundation.md` with the Top 3 problems.
- `foundation/voice-profile.md`: load if present. If missing, fall back to the universal hard rules (no em-dashes, no AI-isms, no hedging), note it, continue. Voice is never a blocker.

**Invoked by the pipeline:** prerequisites are verified; skip re-checking and skip questions the caller already answered (goal, transformation, next-video if passed). Never skip the creator's pick. The saves are identical in both modes.

## Phase 1: Read the video, pick the next one

**Build the lock list:** every number, dollar figure, percentage, timeframe, and named method that appears in the script. The Gap and any receipt in the close use ONLY these.

**Read the format planner's close shape.** It is authoritative for how this format closes (a roast's submission CTA, an interview recapping the GUEST's transformation, news bridging to evergreen). If the planner's default conflicts with the creator's goal, surface it: "Format=interview defaults to views or emails. You picked sales, which this format tends to tank (credibility flows to the guest). Switch or override?"

**Pick the next video first, then derive the Gap from it.** Look at what the creator has ALREADY published, favoring what converts for this goal and reads as the logical next watch. Ask the creator to confirm. Then write the Gap as the problem THAT video solves: what they just learned isn't enough on its own, and the next thing in their way is what the next video covers. Never invent a problem to fit an unmade video. If nothing published is a close-enough next step, fall back to a subscribe pointer instead of forcing a bridge. The Gap does not have to be the same problem the intro poked; it has to be the logical next step from what this video taught.

**CTA shape from goal:** sales → strong direct (or stealth woven) CTA, top link in description, bridge to a past sales-converter. emails → lead magnet tied to THIS video's content, top link, bridge to a past email-converter. views → NO external links, bridge to an evergreen channel asset, retention through the close itself.

**Callback rules** (read from the script's `## Intro`, so the close feels like the same video closing):

1. **Pay off the Setup contract.** The Pivot recaps what the Setup promised, near-verbatim. Mismatched recap reads as a different video.
2. **Coherent pivot, not a topic jump.** The Gap may move to a different problem than the intro poked, but it must read as the logical next step from what the video taught. The bridge to a real video carries the coherence.
3. **Don't reopen with the intro's hook lane.** Question-hook intro → the close doesn't open on another question. The Bridge stays declarative.
4. **Don't re-cite the credibility receipt.** The intro's number or client name already landed; the close references the lesson, not the same receipt.
5. **Echo, don't remix.** Riffing on intro language for resonance is good; a cosmetic remix that loses the meaning is not. Read both aloud back to back.

## Phase 2: Draft 2 candidates

Draft 2 complete closes (Pivot + Gap + Bridge + CTA), differing in shape and rhythm (different BE patterns from transition-patterns Section 3), same Gap problem and next video. Slots filled from the script's actual material and the creator's voice; receipts from the lock list only.

**Length: 30-60 seconds read aloud (roughly 60-150 words).** Longer is a recap (banned). Shorter is a bare CTA (banned).

**Hard filters, auto-reject before the creator sees:**

1. **Fabrication.** Any number not on the lock list.
2. **Tier 1 banned phrases.** "And finally" / "Lastly" / "Thanks for watching" / anything that signals the video is ending. Substitute silently.
3. **Recap dump.** "We covered X, then Y, then Z." The Pivot is one sentence, not a table of contents.
4. **Bare CTA.** "Subscribe" or "check the link" with no Pivot or Gap around it.
5. **Em-dashes.** Universal hard rule.
6. **Read-aloud failure.** If it doesn't flow as continuous spoken speech, restructure.

**Soft friction, flag and let the creator decide:** Tier 2 phrases ("if you liked this please subscribe", "smash that like button", "stay tuned") with their failure mechanism and override case per transition-patterns Section 4; a 3+ sentence Pivot (reads as a wind-down); a bridge to a video that flopped (name the trade-off); a CTA mismatched to goal per the placement reference; hedge words in the Bridge ("maybe", "I think you should"), the Bridge is confident.

Present the 2 candidates as a numbered list, each annotated with its BE pattern, estimated read-aloud time, goal, and any soft flags. The candidate text comes from THIS video's material; do not model closes on remembered examples.

## Phase 3: Pick and refine

Ask which one, or what to change. Regenerate by lever: different Gap (means a different next video and the problem it solves), different next video (verify it exists and converted), shorter, different rhythm, harder or softer CTA.

Push back on weak picks: a next video that isn't published yet (reject: bridging to an unmade video loses the viewer), the most recent video when it underperformed (flag: point to what converted), a vague Gap ("there's still more to learn": too weak to drive a click, name the specific problem), "thanks for watching" (Tier 1, reject).

**Voice check, two passes** per `knowledge/voice-pressure-test.md`: Pass 1 guardrail (anti-patterns and hard rules = restructure; words-avoided = propose the swap). Pass 2 grain: read a reference-piece passage aloud, then the close, judge by ear. No reference piece for this context → skip and note.

**Read-aloud test:** the creator reads the close out loud. Any reword → fix that beat, preserving their phrasing. A reword that sounds like a permanent rule goes through `vid-voice-update` first (permanence gate, not a logger); one-time edits just get applied.

## Phase 4: Lock and save

Always, both modes:

- Read `assets/ending-block-template.md` and fill its slots ({Pivot}, {Gap}, {CTA}, {Bridge}, {{next-video-slug}}). If `goal=views`, omit the CTA block per the template's note.
- Replace any existing close in `content/pieces/{slug}/script.md` with the filled block under `## Ending`.
- Update piece.md: `ending_locked: true`, `next_video: "[[slug]]"`, bump `last_updated:`.
- If the next-video wikilink target doesn't resolve, do NOT save a broken link. Ask: right slug, plain text for now, or skip the Bridge until the video exists?
- Any bank pull updates both sides per `knowledge/vault-integration.md` (piece's `stories_used`/`proofs_used`/`testimonials_used` AND the entry's `used_in` + `status`).
- Confirm in chat with the real voice-check result, one line.

**STOP.** The script is now body-complete with intro and close; `vid-pressure-test` is the next gate.
