# vid-package spec (FOR REVIEW, not built)

A proposal to merge `vid-framing` + `vid-title` + `vid-thumbnail` (text) into one
staged packaging skill. This is a spec for Billy to review: the flow, the stages, the
output, and exactly when each reference loads. Nothing is built from this yet.

Build principle (Billy's guardrail): **port the best parts of the three existing skills
into stages. Do NOT rewrite from scratch. Do NOT make it messy.** Each stage loads its
own context when that stage runs, never all up front.

## One job

Package one video so it gets the click and is clear: the **frame** (the fresh angle),
the **title**, and the **thumbnail text**, as one coherent promise. Title and thumbnail
are literally the package; the frame is the idea behind it. All three are one decision.

Out of scope (stays its own skill): the thumbnail **visual** generator. Packaging
decides the words and the promise. The generator renders the image from the locked
thumbnail text. Different craft (image generation), different skill.

## Pipeline change

Before: `vid-intake -> vid-framing -> vid-title -> vid-thumbnail -> vid-structure -> ...`
After:  `vid-intake -> vid-package -> vid-structure -> ...`

Three packaging gates collapse into one. vid-pipeline routes: piece has no `title` yet
-> `vid-package`. The staged skill can resume mid-way (frame locked but no title, etc.),
so a creator can stop after any stage and pick up later, same as the pipeline does now.
The future thumbnail-visual skill runs separately from the locked thumbnail text.

## The staged flow

Three stages, each a short mini-flow. The creator can stop after any stage; re-running
resumes at the first unlocked stage. Internal stage names are not announced to the
creator (invisible machinery).

### Stage 1 - FRAME  (ported from the new vid-framing + Ed's reframe doctrine)

1. Read the brain-dump.
2. Get into the viewer's head: their existing belief/frustration on this topic, the main
   problem, the transformation they want. Name the **core payoff**.
3. Find the **frame**: the reframe that makes the known idea feel new. Toolkit: a fresh
   comparison/metaphor, a contrarian flip, a named system/rule, the creator's own story,
   a visual framework. One line, in the creator's voice. (Interesting is the frame, not
   the information.)
4. Lay the read + frame back to the creator, WAIT for a yes or a sharpen. Nothing past
   here until they confirm.
5. Confirm format (lead with the packaging rotation, override allowed) and goal
   (sales/emails/views).

Locks: `selected_angle`, `core_payoff`, `format`, `goal`.

**What loads, and when (Stage 1):**

| File | When | For |
|---|---|---|
| `content/pieces/{slug}/brain-dump.md` | step 1 | the material and the problem it circles |
| `foundation/creator-foundation.md` | step 2 | avatar + iceberg: who it is for, the lane, the belief to flip |
| `banks/pattern-bank.md` | step 3 | which frames/outliers have worked (grounds the reframe) |
| `foundation/packaging-system.md` | step 5 | the format rotation to default from |

### Stage 2 - TITLE  (ported from vid-title, built ON the frame)

The one real fix vs today: the title is built ON the locked frame. It does NOT re-derive
the claim cold. The frame IS the claim; the viewer read is already done in Stage 1 and is
reused, not repeated.

1. Take the locked frame as the claim. Build the lock list (every verifiable specific in
   the material; titles may use only what is on it).
2. Write title options that make the viewer FEEL the frame, varied across emotional
   framings (the lanes): problem, correction, confession, revelation, cost, identity.
3. Open the banks as the filter (quarantined until options are written, so the output is
   not derivative). Map each lane to proven patterns; pin real competitor proof; label
   crowded (high spread) vs underused (low spread) and on-brand vs off-brand.
4. Name the opportunity: the on-brand AND underused lane is the recommendation.
5. Craft gates on every survivor: claim not label, touches the driver, lock-list only
   (anti-fabrication), 50-char aim / 55 ceiling, hits a BENS letter, read-aloud, and the
   title/thumbnail unit check (leave the thumbnail room, do not say the same beat twice).
6. Present opportunity-first. Creator picks the title.

Locks: `title`, `title_lane`.

**What loads, and when (Stage 2):**

| File | When | For |
|---|---|---|
| (Stage 1 context is already in hand) | - | frame, viewer read, material, lock list |
| `banks/title-bank.md` | step 3 (after options written) | proven title patterns + spread |
| `banks/power-words-bank.md` | step 3 | word choice, land/fail notes |
| `knowledge/BENS-framework.md` | step 5 | the Big/Easy/New/Safe craft filter |
| `references/title-filters.md` | on demand in step 2-3 | the lane menu + pattern shapes |

### Stage 3 - THUMBNAIL TEXT  (ported from vid-thumbnail, text-only)

Now the title/thumbnail coordination is internal, no cross-skill seam.

1. Craft 3-5 word thumbnail text picks as a UNIT with the locked title: one promise, no
   repeated words, the thumbnail adds a beat the title does not.
2. BENS on the picks; one-line why each lands.
3. Creator picks 1-2 winners.

Locks: a thumbnail brief (locked text picks + rationale). Text only. No layout, hero,
expression, color, or AI prompt (those live in the future visual generator).

**What loads, and when (Stage 3):**

| File | When | For |
|---|---|---|
| (title + frame already in hand) | - | the promise to complement, the words to avoid |
| `knowledge/thumbnail-text-patterns.md` | step 1 | proven thumbnail-text shapes + the text-only boundary |

## Merged output

One packaged `piece.md`, fields appended across the stages (never overwriting another
skill's fields; ownership map in `knowledge/vault-integration.md`):

- Stage 1: `selected_angle`, `core_payoff`, `format`, `goal`
- Stage 2: `title`, `title_lane`
- Stage 3: thumbnail text picks

Open question: keep the thumbnail picks in a sibling `thumbnail-brief.md` (clean input
for the visual generator) or fold into `piece.md`. Leaning sibling file, so the visual
skill has one obvious thing to read.

`voice_context` stays a silent default (`youtube-script`) as today. Hands to
vid-structure.

## What is preserved from each skill (the best parts, ported not rewritten)

- **From new vid-framing:** the psychology-first spine, the confirm-before-building gate,
  anti-fabrication, the lean lazy-load structure. ADD Ed's reframe toolkit to Stage 1.
- **From vid-title:** the claim-first engine (claim = the locked frame, not re-derived),
  the emotional-framing lanes, the competitor-gap crowded-vs-underused analysis, all the
  craft gates (char ceiling, BENS, read-aloud, lock-list, title/thumbnail unit check),
  bank quarantine until options are written.
- **From vid-thumbnail:** the thumbnail-text planning (3-5 words, BENS, why it lands), the
  strict text-only boundary, the coordination with the title (now internal).

Nothing good gets dropped. The merge removes the seams (title re-deriving the frame;
title and thumbnail coordinating across files), not the craft.

## What changes elsewhere

- **vid-pipeline:** three routing rows collapse to one packaging gate. Simpler state
  machine.
- **The eval:** the vid-framing suite I built becomes the Stage-1 slice of a vid-package
  eval. The after-intake fixtures + corpus still apply. Tier A gains title + thumbnail
  frontmatter/enum/handoff checks; Tier B gains title-quality and thumbnail-quality
  dimensions alongside the frame ones. The isolated eval-agent extends the grader.
- **vid-thumbnail-gen (visual, future):** unchanged, separate. Reads the locked thumbnail
  text.

## What we do NOT do

- No from-scratch rewrite. Port the existing logic into stages.
- No touching the visual generator.
- No loading everything up front. Each stage loads its own context when it runs (the
  tables above).
- No announcing stage names to the creator. Packaging feels like one conversation.

## Open questions for Billy's review

1. Name: `vid-package` or `vid-pack`.
2. Thumbnail picks: sibling `thumbnail-brief.md` (my lean) or inside `piece.md`.
3. Is packaging one continuous conversation, or do we want explicit stop points the
   creator confirms between stages (frame locked -> continue to title? etc.)? Staged
   either way; question is how much we pause.
4. References: three skills' reference files come along. Which stay separate (loaded per
   stage, per the tables) vs consolidate. My default: keep them separate and lazy-loaded,
   so nothing bloats and each stage pulls only what it needs.
5. Scope/sequencing: this is a 3-skill merge. Do it as one build, or land Stage 1
   (framing + the reframe doctrine) first under the new structure, then fold in title,
   then thumbnail, re-running the eval at each fold so it never gets messy?

## Recommended build sequence (once approved)

Incremental, so it never turns into a big-bang mess:
1. Stand up `vid-package` with Stage 1 = the current vid-framing logic + the reframe
   doctrine. Re-run the eval (now the packaging eval, Stage 1 only). Green.
2. Port vid-title into Stage 2, built on the frame. Extend the eval. Green.
3. Port vid-thumbnail into Stage 3. Extend the eval. Green.
4. Update vid-pipeline routing. Retire the three old skills (or leave thin shims).
5. Delete the business-os temp copy. Commit when Billy approves.

Each step is reviewable and independently green before the next.
