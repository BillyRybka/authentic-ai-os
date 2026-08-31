---
name: vid-ending
description: Write the close of a YouTube video with Pivot/Gap/Bridge. Recap the transformation, reveal the new problem the lesson created, point at a real already-published video that converts for this video's goal. The video never announces it is ending. Format-aware CTA placement. Runnable standalone or inside vid-pipeline during the script phase. Triggers on "write the ending", "close this video", "outro for [video]", "what's the CTA", or when a pipeline needs a locked close.
---

# Video Ending Writer

Writes the close of one video under the golden rule: the video never ends. The close is Pivot (recap the transformation in one sentence) → Gap (reveal the problem the lesson just created) → Bridge (point at a real, already-published video that fixes it). The viewer never hears "the end"; they hear their next step.

Energy direction decides the close. A close that decelerates dies: "alright, so to wrap up" says the value is over, and the viewer leaves. A close that holds level, then points forward, carries them into the next video. Level, then forward. Never down, then out.

**Scope: the close only.** No hooks, no body points, no titles, no end-screen visuals. It does not pick the next video for the creator; it asks.

**This is a conversation, not a document.** Short messages. References are for your thinking; never paste them at the creator.

## What loads, and when

Read each file when its phase starts. Never front-load.

- **Phase 1:** `content/pieces/{slug}/piece.md` (format, goal, frame) · `content/pieces/{slug}/script.md` (full body, plus the `## Intro` verbatim for the callback rules) · `foundation/avatar.md` (avatar + Top 3 problems) · `knowledge/format-planners/{format}.md` (close shape, authoritative) · `references/end-screen-design.md` (picking the next video).
- **Phase 2:** `foundation/voice-profile.md` + the matching `foundation/reference-pieces/{voice_context}.md` (voice only; the spec wins any conflict with Pivot/Gap/Bridge) · `knowledge/transition-patterns.md` Sections 3 + 4 (BE-1..BE-8 close patterns, banned tiers) · `banks/transition-bank.md` if the vault has it (creator-grown supplement; missing is fine) · `knowledge/attention-craft.md` (energy + pacing calibration) · `knowledge/prose-craft.md` (the seven moves, loaded before drafting rather than as a filter after it) · `references/pivot-gap-bridge-shapes.md` · `references/cta-placement-by-format.md` · `references/ending-anti-patterns.md`. Conditional: the story/proof/metaphor/parable files, only if the close pulls one (rare).
- **Phase 4:** `knowledge/voice-pressure-test.md` + `knowledge/voice-rhythm.md` (the two-pass voice check) · `knowledge/bank-contract.md` (update-both-sides on bank pulls).

## Prerequisites

- `content/pieces/{slug}/script.md` has the FULL body written and a non-stub `## Intro`. Partial body → hard stop: "Run `vid-segment` for every section first." Stub intro → hard stop: "Run `vid-intro` first; the close calls back to the opening."
- `content/pieces/{slug}/piece.md` with `format`, `goal`; `foundation/avatar.md` with the Top 3 problems.
- `foundation/voice-profile.md`: load if present; if missing, note it and continue on the universal hard rules. Voice is never a blocker.

**Invoked by the pipeline:** prerequisites are verified; skip re-checking and questions the caller already answered. Never skip the creator's pick. The saves are identical in both modes.

## Phase 1: Read the video, pick the next one

**Build the lock list:** every number, dollar figure, percentage, timeframe, and named method in the script. The Gap and any receipt in the close use ONLY these.

**Read the format planner's close shape.** It is authoritative for how this format closes (a roast's submission CTA, an interview recapping the GUEST's transformation, news bridging to evergreen). If the planner's default conflicts with the creator's goal, surface it (an interview defaults to views or emails; a sales goal tanks there, credibility flows to the guest).

**Pick the next video first, then derive the Gap from it.** Scan what the creator has ALREADY published, favor what converts for this goal and reads as the logical next watch, and confirm the pick. Then write the Gap as the problem THAT video solves. Never invent a problem to fit an unmade video. If nothing published is a close-enough next step, fall back to a subscribe pointer.

**CTA shape from goal:** sales → strong direct (or stealth woven) CTA, top link in description, bridge to a past sales-converter. emails → lead magnet tied to THIS video's content, top link, bridge to a past email-converter. views → NO external links, bridge to an evergreen channel asset, retention through the close itself.

**Callback rules** (from the script's `## Intro`, so the close feels like the same video closing):

1. **Pay off the Setup contract.** The Pivot recaps what the Setup promised, near-verbatim. A mismatched recap reads as a different video.
2. **Coherent pivot, not a topic jump.** The Gap may name a different problem than the intro poked, but it has to follow from what the video taught.
3. **Don't reopen the intro's hook lane.** Question-hook intro → the close doesn't open on another question. The Bridge stays declarative.
4. **Don't re-cite the credibility receipt.** The intro's number or client name already landed; the close references the lesson.
5. **Echo, don't remix.** Riff on intro language for resonance; a cosmetic remix that loses the meaning is not. Read both aloud back to back.

## The Gap: name the dependency the lesson created

The Gap is not a new topic and not a retraction. It is the problem the viewer has NOW because this lesson worked. Three families cover almost every close:

1. **Second-order consequence.** The lesson lands and exposes the next weakness. "A hook that stops scrolling won't keep them past minute three if your first body shot doesn't match."
2. **Next-on-the-stack.** The viewer is working a checklist; this video checked one item off. "The next thing on your stack is keeping retention through the middle."
3. **Bottleneck shift.** Solving this problem moves the constraint somewhere else. "The day client three signs, the bottleneck moves to delivery."

Pick the family by asking: what does the viewer need now that they did not before this lesson? It ships only if a real published video solves it; otherwise, subscribe pointer.

Weak vs great, same video:

> **Weak:** "So we covered hooks, then intros, then transitions. There's still more to learn. If you have time, you might want to check out this next video."

Recap dump (the value is over, leave), a Gap that names nothing, a Bridge that asks. Energy falls off a cliff.

> **Great:** "You now have everything you need to land your first 3 clients without a website. The next problem is keeping them past month two, and that's where most coaches get stuck. I made a video on it. Watch this next."

One-breath transformation, a named next-on-the-stack problem, a confident point. Energy holds level, then points forward.

More worked shapes per beat: `references/pivot-gap-bridge-shapes.md`.

## Phase 2: Draft 2 candidates

Draft 2 complete closes (Pivot + Gap + Bridge + CTA), different BE patterns, same Gap problem and next video. Slots fill from THIS video's material and the creator's voice; receipts from the lock list only. Never model closes on remembered examples.

**Length: 30-60 seconds read aloud (roughly 60-150 words).** Longer is a recap (banned). Shorter is a bare CTA (banned).

**Hard filters:** auto-reject before the creator sees a candidate: fabrication (any number off the lock list), em-dashes, and everything in `references/ending-anti-patterns.md`. That file owns the list: banned phrases and structural failures, each with the why. A candidate it rejects does not ship.

**Soft friction, flag and let the creator decide:** Tier 2 phrases per transition-patterns Section 4 (surface with the failure mechanism and the override case); a 3+ sentence Pivot (reads as a wind-down); a bridge to a video that flopped (name the trade-off); a CTA mismatched to goal per the placement reference; hedge words in the Bridge ("maybe", "I think you should").

Present them numbered, annotated with BE pattern, read-aloud time, and soft flags.

## Phase 3: Pick and refine

Ask which one, or what to change. Regenerate by lever: different Gap (means a different next video and the problem it solves), different next video (verify it exists and converted), shorter, different rhythm, harder or softer CTA.

Push back on weak picks: a next video that isn't published yet (reject: an unmade video can't be watched), the most recent video when it underperformed (flag: point to what converted), a vague Gap ("there's still more to learn" is too weak to drive a click; name the specific problem), "thanks for watching" (Tier 1, reject).

**Voice check, two passes** per `knowledge/voice-pressure-test.md`: Pass 1 guardrail (anti-patterns and hard rules = restructure; words-avoided = propose the swap). Pass 2 grain: read a reference-piece passage aloud, then the close, judge by ear. No reference piece → skip and note.

**Read-aloud test:** the creator reads the close out loud. Any reword → fix that beat, preserving their phrasing. A reword that sounds like a permanent rule goes through `vid-voice-update` first (permanence gate, not a logger); one-time edits get applied.

## Phase 4: Lock and save

Write the close into `content/pieces/{slug}/script.md` under `## Ending`, replacing any existing close, in this shape:

```markdown
## Ending

<!-- PIVOT -->
{one-sentence transformation recap}

<!-- GAP -->
{the new problem, traceable to the Top 3}

<!-- CTA (omit when goal=views) -->
{sales pitch or lead-magnet pointer}

<!-- BRIDGE -->
{confident point at the next video; nothing spoken after}

<!-- END SCREEN CARD CUE -->
[END SCREEN: {next-video-slug}, card animates in during the Bridge]
```

The comment markers are load-bearing: the editor times the end-screen card to them; `vid-pressure-test` reads beats by them.

Then:

- Update piece.md: `ending_locked: true`, `next_video: "[[slug]]"`, bump `last_updated:`.
- If the next-video wikilink target doesn't resolve, do NOT save a broken link. Ask: right slug, plain text for now, or skip the Bridge until the video exists?
- Any bank pull updates both sides per `knowledge/bank-contract.md`.
- Confirm in chat with the real voice-check result, one line.

**STOP.** The script is now body-complete with intro and close; `vid-pressure-test` is the next gate.
