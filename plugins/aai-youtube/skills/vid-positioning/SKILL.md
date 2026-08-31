---
name: vid-positioning
description: Drafts the Iceberg Statement, the one-sentence channel promise. Uses WHO plus WHAT plus HOW plus TENSION with the creator's literal language preserved. Runs after vid-avatar. Triggers on "write my Iceberg Statement", "draft my positioning", or "top of my iceberg".
---

# Positioning

Draft the Iceberg Statement. One sentence. The channel's promise.

This is the second skill in the foundation sequence. It runs after `vid-avatar` and produces the single sharpest line a creator owns. Everything downstream (titles, thumbnails, hooks, scripts) gets pressure-tested against this statement.

## Contract

**Inputs (required):** `foundation/offer.md` and `foundation/avatar.md` with the Offer, Avatar, and Top 3 perceived problems populated. If those don't exist, stop and point the creator at `vid-avatar`.

**Inputs (optional):** `foundation/voice-profile.md` (its anti-patterns override the voice rules in `${CLAUDE_PLUGIN_ROOT}/knowledge/interview-posture.md`).

**Outputs:** the Iceberg Statement and Machinery sections written to `foundation/iceberg.md`, created from its template in `${CLAUDE_PLUGIN_ROOT}/knowledge/foundation-templates.md` if missing.

**Downstream consumers:** `vid-pillars` (uses the locked statement to validate content pillars), every per-video skill (uses the statement for title and thumbnail alignment).

## Load at session start

1. `${CLAUDE_PLUGIN_ROOT}/knowledge/interview-posture.md`. Shared conversation posture. Non-negotiable.
2. `${CLAUDE_PLUGIN_ROOT}/knowledge/vault-integration.md`. Frontmatter schema.
3. `foundation/offer.md` and `foundation/avatar.md`. Read the Offer, Avatar, and Top 3 sections.
4. `foundation/voice-profile.md` if it exists.
5. `references/positioning-method.md`. The WHO + WHAT + HOW + TENSION method this skill uses to draft.
6. `references/positioning-examples.md`. Locked Iceberg Statement examples for calibration. Read one or two closest to the creator's niche, not all of them. Never pattern-match the shape.

## Pre-check (silent)

Migration first: if `foundation/creator-foundation.md` exists, the breakup into the five foundation files hasn't finished. Follow `${CLAUDE_PLUGIN_ROOT}/knowledge/foundation-migration.md`, then resume this pre-check after the migration completes.

Then read `foundation/offer.md`, `foundation/avatar.md`, and `foundation/iceberg.md`. Three states:

- **No Offer/Avatar/Top 3.** Stop. Tell the creator: "Run `vid-avatar` first. I need your offer, avatar, and Top 3 problems before I can draft a sharp Iceberg Statement."
- **Has Offer/Avatar/Top 3 but no Iceberg Statement.** Fresh run. Open with the absorb-first protocol.
- **Has Iceberg Statement locked.** Surface it and ask: "Iceberg Statement locked. Refresh, keep, or replace?"

## The four parts of a sharp Iceberg Statement

A sharp statement has four components. All four are required. Missing one means the line isn't sharp yet.

- **WHO.** The avatar, in their words. Pulled from the Avatar section of `foundation/avatar.md`.
- **WHAT.** The result the avatar walks away with. Concrete, not a category. "Revenue-generating content," not "content." "Thirty pounds lighter," not "healthier."
- **HOW.** The mechanism. What the method actually does. "Turn their expertise into," "automate the inbox," "spot red flags before the first date." This is the differentiator. It's what distinguishes this creator from every other one in the niche.
- **TENSION.** An enemy, refused axis, or specific stakes that makes the line bite. Without this, the statement reads like 1000 other channels.

The classic shape:

> "I help [WHO] [HOW] to get [WHAT] without [TENSION]."

Example: "I help new managers lead high-performing teams without becoming micromanagers."

- WHO: new managers
- HOW: (implicit method, learned across the channel)
- WHAT: high-performing teams
- TENSION: named enemy ("becoming micromanagers")

The connectors flex. "Without" can become "before," "instead of," "the way that," or drop entirely. The four components have to be present in some form.

Full method including the literal-words rule, the three places tension can live, and what to do when a draft is bland: see `references/positioning-method.md`.

## How this skill runs

This is a drafting skill, not a discovery skill. The creator already locked the inputs via `vid-avatar`. Your job is to read those inputs, find the four components, draft two candidate statements, and iterate with the creator until one lands.

### Step 1: Absorb the inputs

Read the Offer from `foundation/offer.md` and the Avatar and Top 3 from `foundation/avatar.md`. Don't ask the creator to repeat them.

Run the absorb-first protocol from `${CLAUDE_PLUGIN_ROOT}/knowledge/interview-posture.md`. The four components (WHO, WHAT, HOW, TENSION) are YOUR internal scaffolding. Don't speak the labels aloud. Mirror back what the inputs gave you, in prose, then ask the one useful question.

Shape of the opener:

> "Reading your foundation. Sounds like this is for [paraphrased avatar], and the thing they walk away with is [WHAT in your read]. Your mechanism is [HOW in your words]. The loudest tension I see is '[literal phrase or refused axis, in the creator's words]'.
>
> Locking that read, or push on any of it before I draft?"

If the creator pushes on a piece, adjust before drafting. If they confirm or stay quiet, move to Step 2.

### Step 2: Draft two candidates

After WHO, WHAT, HOW, and TENSION are clear, draft 2 candidate statements.

**The two drafts vary the TENSION. Same WHO, same WHAT, same HOW. Different enemy or different tension type.** This is the hard rule. Three rewordings of the same template is the wrong move.

Show both:

> "Two drafts. Which is closer, and what's wrong with it?
>
> **Draft 1:** [statement]
>
> **Draft 2:** [statement]
>
> Draft 1 leans on [the first tension move]. Draft 2 leans on [the second]. Both use your words."

Don't show more than two. Don't show three rewordings of the same template.

### Step 3: Iterate

The creator reacts. You rewrite using whatever language they gave you. Show the new version. Keep going until they read it aloud without rewording.

If they get stuck choosing between drafts, offer the two-option fork from `${CLAUDE_PLUGIN_ROOT}/knowledge/interview-posture.md`:

> "Two paths. Lock Draft 1 and refine, or scrap both and try a different tension. Which fits how you'd actually say it?"

### Step 4: Read-aloud test

Final filter. When a draft feels close, ask:

> "Read it out loud. Does it sound like something you'd naturally say when someone asks what you do?"

If they reword anything, the reworded version IS the statement. Use it.

### Step 5: Save

Write the locked Iceberg Statement to `foundation/iceberg.md` in the Iceberg Statement section (create the file from its template in `${CLAUDE_PLUGIN_ROOT}/knowledge/foundation-templates.md` if missing). Fill the Machinery section with the four components in the creator's words: Who, How, What, Tension.

If a longer version surfaced naturally during the conversation ("...so they can [deeper reason]"), save it as the Optional longer version. Don't manufacture a longer version if it didn't come up organically.

## Closing the skill

Announce the lock and auto-advance to `vid-pillars`. No friction step.

> "Iceberg Statement locked. Moving to vid-pillars to map your content pillars."

Then immediately invoke `vid-pillars` via the Skill tool. If the creator explicitly says they want to stop ("hold here", "stop", "let me come back to this"), respect that and don't invoke the next skill.

## When the draft is bland

Three checks. If a draft fails one, swap the tension or sharpen the WHAT.

- **Could 1000 other channels in the niche say this exact sentence?** If yes, the tension isn't strong enough or the result is too generic.
- **Can the viewer picture themselves searching this on YouTube?** If no, replace abstract nouns with concrete moments.
- **Does the creator read it aloud without rewording?** If they reword, the reworded version is the version.

Reject bland drafts silently. Don't show "this was too generic." Show the sharper version.

## Use the creator's literal words for TENSION

If the creator named the enemy in 1 to 3 words, especially if they said it more than once, use those exact words. Don't paraphrase.

- "Cry it out" stays "cry it out." Not "extinction-based sleep training."
- "Fake gurus" stays "fake gurus." Not "people pretending to be experts."
- "Hourly-rate model" stays "hourly-rate model." Not "trading time for money."

Why: a phrase the creator already says becomes a brand asset. A paraphrase loses it. Full rule in `references/positioning-method.md` and `${CLAUDE_PLUGIN_ROOT}/knowledge/interview-posture.md`.

## Edge cases

**Avatar is broad ("business owners," "creators").** Accept it as WHO. The specificity moves into the TENSION and the HOW. Don't try to renarrow the avatar inside this skill. That was `vid-avatar`'s job.

**Creator dislikes both drafts.** Two paths. Either run the absorb-first read again with a different angle (if you missed a tension the creator was sitting on), or ask: "Give me the line you'd say if you only had 30 seconds with someone. Don't make it pretty. Just say it." Their unpolished version usually has the WHAT and TENSION you need.

**Creator wants a longer statement.** The longer version is optional, not the goal. If they want it, append "so they can [deeper reason]" using their actual words. Don't pad with marketing language.

**Brand-new creator with no clients yet.** Educated guesses for HOW and TENSION are fine. Flag it: "We're working with what you've said so far. The statement sharpens once you publish 3 or 4 videos and see what real comments come in."

## References

- `references/positioning-method.md`. The WHO + WHAT + HOW + TENSION drafting method. The literal-words rule. Three places the tension can live (named enemy, refused axis, specific stakes). What to do when a draft is bland.
- `references/positioning-examples.md`. 10+ locked Iceberg Statements with the four components broken out. Plus good/bad pairs by niche. Read 1 or 2 closest to the creator's niche for calibration. Don't read all of them. Don't pattern-match the shape.

## Anti-patterns

- Asking the creator to draft the statement themselves. Claude drafts. Creator reacts.
- Drafting before the four components (WHO, WHAT, HOW, TENSION) are visible in the inputs.
- Showing three rewordings of the same template instead of two structurally different drafts.
- Paraphrasing a literal enemy phrase the creator named.
- Pattern-matching the shape of an example in `positioning-examples.md` instead of using the creator's actual language.
- Locking a draft missing WHO, WHAT, HOW, or TENSION.
- Skipping the read-aloud test.
- Running `vid-pillars` inside this skill. The bottom subtopics are a separate skill.
- Asking for the offer, avatar, or Top 3 problems. Those were locked by `vid-avatar` and live in `foundation/offer.md` and `foundation/avatar.md`.
