---
name: vid-packaging
description: Lock the creator's starting video defaults. Gift Framework (wrapping, box, gift), 3+1 format rotation, title-bank seeding, starting thumbnail strategy, design guardrails, and creation path. 6th and final foundation skill. Triggers on "build my packaging system", "lock my video defaults", "format rotation", "thumbnail strategy", "title bank setup", "channel design system", or whenever the creator needs the per-video defaults that downstream skills consume (vid-title, vid-thumbnail, vid-framing).
---

# Packaging

Lock the creator's starting video defaults. Six sub-stages in order. Each one updates a section of `foundation/packaging-system.md`.

These are STARTING defaults. They change once real videos publish and `vid-research` plus `vid-measurement` surface evidence. The point is to give downstream skills a confident place to start, not pretend the final formats are already known.

## Contract

**Inputs (required):** `foundation/creator-foundation.md` with Avatar, Top 3 problems, Iceberg Statement, and Content pillars locked. The packaging defaults have to map to a known avatar and a locked promise.

**Inputs (optional):** `foundation/voice-profile.md`, `banks/pattern-bank.md` (if `vid-research` has run), `banks/packaging-bank/` (if winners exist), past published videos.

**Outputs:** `foundation/packaging-system.md` populated per `knowledge/packaging-system-template.md`. Plus `banks/title-bank.md` seeded from `assets/title-bank-seed.md` if missing.

**Downstream consumers:** `vid-title` (BENS plus title bank), `vid-thumbnail` (strategy plus design guardrails plus creation path), `vid-framing` (starting format rotation), every per-video skill.

## Load at session start

1. `knowledge/interview-posture.md`. Shared posture. Non-negotiable.
2. `knowledge/vault-integration.md`.
3. `foundation/creator-foundation.md`. Read Avatar, Top 3, Iceberg Statement, Content pillars.
4. `foundation/voice-profile.md` if it exists.
5. `knowledge/packaging-system-template.md`. The schema for the output file.
6. Per-sub-stage references load only when that sub-stage opens. Don't load all of them up front.

## Pre-check (silent)

Read `foundation/creator-foundation.md`. Three states:

- **Missing Iceberg Statement or Content pillars.** Stop. Tell the creator: "Run `vid-positioning` and `vid-pillars` first. Packaging defaults map to the locked statement and pillars, so I need both before I can shape this."
- **Foundation complete, no packaging yet.** Fresh run.
- **`foundation/packaging-system.md` already exists.** Surface the current state and ask: "Packaging system exists. Refresh which sub-stage, or replace the whole thing?"

## What this skill is NOT

- Per-video work. Title generation, thumbnail design, format picking for one specific video. Those are `vid-title`, `vid-thumbnail`, `vid-framing`.
- Image generation. Visual design lives in `vid-thumbnail-gen` (optional, not required).
- A research skill. If the creator wants competitor patterns and outliers, run `vid-research` first and come back.

## The six sub-stages

Run in order. One at a time. Each sub-stage: brief opener, focused question or proposal, react, lock, save, move on.

Apply the absorb-first protocol from `knowledge/interview-posture.md` throughout. Short messages. Don't speak structured-field jargon aloud. Use plain language.

### Sub-stage 1: Packaging mode (evidence level)

Before choosing formats or thumbnails, identify the evidence level. This decides whether choices are anchored in data or in creator judgment.

> "Before we pick formats and thumbnails, two questions. Do you have published videos with useful performance data yet? And if you do, has `vid-research` built your pattern banks?"

**If they have published data plus pattern banks:** "Good, we'll use what already has signals instead of guessing."

**If they have published data but no pattern banks:** offer the choice. "Fast version: tell me what's worked so far, I'll save temporary defaults at low confidence. Better version: run `vid-research` first and come back with real outliers and competitor patterns. Which fits today?"

**If they have no useful data (new channel or new pivot):** "Since there's no channel data yet, we'll pick first defaults based on your avatar, your proof, and what you can actually make. These change once real data shows what to keep."

The evidence level is a routing decision, not a saved field. Use it to set the confidence and watch-for values attached to each sub-stage's saves below.

### Sub-stage 2: Starting packaging defaults (thumbnail style, format preference, content type)

Load `knowledge/gift-framework.md` now. The framework names three layers: wrapping paper (thumbnail style), box (format), gift (content type). Those are internal labels. Don't speak them aloud. Ask plain questions.

Three answers, built one at a time. Propose-don't-interrogate where possible (if the avatar or pillars hint at the answer, surface it back instead of asking cold).

**Question 1: thumbnail style the avatar clicks**

> "What thumbnail style does your avatar actually click? Plain words. If you have 1 or 2 competitor thumbnails you admire, share them."

Push back on vague answers:

> "'Professional-looking' doesn't tell `vid-thumbnail` what to make. Is it face plus big contradiction text, clean object shot, messy whiteboard, before-and-after, or something else?"

**Question 2: format the avatar already opens most**

> "What video format does your avatar already open most often? Short how-to, case study, teardown, deep dive, interview, news, or list?"

**Question 3: what they come back for from this creator specifically**

> "What do they come back for from you specifically? Systems, tactics, stories, frameworks, opinion, examples, or something else?"

Save the three answers to the Starting Packaging Defaults section of `packaging-system.md`. Use the creator's phrasing where it carries useful constraints. Don't turn the answers into marketing copy.

For each of the three layers saved, include the same metadata downstream skills expect from sub-stages 3 and 5:

- Evidence basis: creator judgment, source-backed default, own channel data, or pattern-bank research.
- Confidence: low, medium, or high.
- Watch for: what would tell us to refine this (e.g. "thumbnails in this style underperform after 4 videos", "avatar comments suggest a different format actually lands").

These three answers drive `vid-thumbnail`, `vid-framing`, and `vid-segment`. Tracking what's anchored vs guessed matters.

### Sub-stage 3: Starting format rotation (3+1)

Load `knowledge/format-rotation-guide.md` now.

Don't ask the creator to pick from all seven formats cold. Infer the first rotation using:

- channel evidence if available
- pattern-bank evidence if available
- the Gift Framework (wrapping plus box plus gift)
- creator capability and available proof
- source-backed format-fit defaults

Propose:

> "Here's the first rotation I'd test: [Format 1], [Format 2], [Format 3], with [Format X] as the every-fourth-video experiment. I picked these because [plain reasons in 1 to 2 sentences]. What feels wrong?"

For each format saved, include:

- Why this is a good first test (one sentence)
- Evidence basis: creator judgment, source-backed default, own channel data, or pattern-bank research
- Confidence: low, medium, or high
- Watch for: what would tell us to keep, adjust, or drop it

Push back if the picks don't match the avatar, the creator's proof, or what they can actually produce. Plain words, not source language.

Save to the Starting Format Rotation section.

### Sub-stage 4: Title bank seed plus BENS orientation

Load `knowledge/BENS-framework.md` now.

Silent check `banks/title-bank.md`:

- **Exists already:** leave it alone. Tell the creator: "Title bank already exists. We'll use it downstream and add winners over time."
- **Missing:** create `banks/` if needed, copy `assets/title-bank-seed.md` to `banks/title-bank.md`. Tell the creator: "Title bank seeded. `vid-title` will adapt these patterns to your real video material, and your own winners will replace the generic seed over time."

BENS orientation. One or two sentences in chat:

> "BENS is the title test. Big, Easy, New, Safe. Each title should hit at least one. `vid-title` enforces this every video."

Don't ask the creator to draft titles in this skill. That's `vid-title`'s job.

### Sub-stage 5: Starting thumbnail strategy

Load `knowledge/thumbnail-strategy-menu.md` now.

Don't ask the creator to pick from the menu cold. Propose 2 strategies based on:

- avatar
- Gift Framework
- existing evidence
- starting format mix

Propose:

> "For the first thumbnail tests, I'd use [Strategy 1] and [Strategy 2]. I picked those because [plain reasons]. What feels wrong?"

If the creator has past thumbnails, use that data to inform the picks.

For each strategy saved, include why this is a good first test, evidence basis, confidence, what to watch for.

Save to the Thumbnail Strategy Test Plan section.

### Sub-stage 6: Design guardrails plus creation path

Load `knowledge/thumbnail-strategy-menu.md` already in context.

**Design guardrails (quick):**

- Color palette: 2 or 3 max.
- Font: one primary.
- Hero element: face, object, or text.
- Expression rules: which expressions are allowed for face thumbnails, which are off-limits.
- Text limit: 4 to 5 words max in the thumbnail.

> "Quick guardrails. Color palette (2 or 3 max). Font. Hero element (face, object, or text). Expression rules. Text limit (4 to 5 words)."

If the creator has a brand style guide, pull from it. Otherwise infer from the Gift Framework's wrapping-paper answer.

**Creation path (pick one):**

> "Last piece. How do you actually make thumbnails? Photoshop or DIY, AI workflow, batch-shoot photos, or outsource?"

Save Design Guardrails and Creation Path sections.

## Save (final)

Once all six sub-stages lock, confirm:

- `foundation/packaging-system.md` exists with all sections populated.
- `banks/title-bank.md` exists (seeded or pre-existing).

Every saved field must change a downstream decision. If a section feels like fluff, push back: "What downstream skill uses this? If nothing, we don't need it."

## Closing the skill

> "Packaging system locked in `foundation/packaging-system.md`. Title bank at `banks/title-bank.md`. That completes the foundation. Next: run `vid-voice-capture` to build your voice profile. That doc is critical for every script. Give it a real session with 2 to 3 transcripts or a 10-minute live riff."

Don't run `vid-voice-capture` automatically.

## Edge cases

**Creator wants to skip sub-stages.** Each sub-stage feeds a different downstream skill. Skipping creates gaps. Push back: "Which downstream skill is this for? Skipping [sub-stage] means `vid-thumbnail` (or whichever) won't have the input it needs. Want to do a fast version with low confidence instead?"

If they still want to skip, mark the section as `[not set, fill later]` with a note about which downstream skill is blocked.

**Creator says "I'll figure it out as I go."** Two paths. Either lock low-confidence MVP defaults now and refresh after 4 to 6 published videos, or run `vid-research` first to anchor in real patterns. Don't lock an empty packaging system.

**Brand-new creator, no proof, no published videos.** Default to source-backed format fits at low confidence. Flag MVP. Tell them: "These are working defaults. After 4 to 6 videos, `vid-measurement` will surface what to keep, adjust, or drop."

**Creator already has a complete packaging system from outside this tool.** Surface what they have, ask which sub-stages to keep and which to refresh. Don't overwrite without explicit confirmation.

## References

This skill uses shared knowledge files from `knowledge/`:

- `knowledge/gift-framework.md` (sub-stage 2).
- `knowledge/format-rotation-guide.md` (sub-stage 3).
- `knowledge/BENS-framework.md` (sub-stage 4).
- `knowledge/thumbnail-strategy-menu.md` (sub-stages 5 and 6).
- `knowledge/packaging-system-template.md` (the output schema).

Plus skill-local asset:

- `assets/title-bank-seed.md`. Seeds `banks/title-bank.md` on first run if the bank is missing.

## Anti-patterns

- Loading all five knowledge files at session start. Load per sub-stage, when needed.
- Asking the creator to pick formats or thumbnail strategies cold from a menu. Propose 2 based on avatar plus evidence, react.
- Saving a section without evidence basis, confidence level, and watch-for. The MVP nature of these defaults means future skills need to know what's anchored vs guessed.
- Locking an empty packaging system. Either fill or mark as pending with downstream impact noted.
- Overwriting an existing `banks/title-bank.md`. If it exists, leave it alone.
- Auto-running `vid-voice-capture` at the end.
- Speaking jargon ("3+1 rotation", "BENS", "wrapping paper") at the creator without context. Translate to plain words.
- Treating these defaults as final. They're starting points. The skill saves "watch for" criteria for a reason.
