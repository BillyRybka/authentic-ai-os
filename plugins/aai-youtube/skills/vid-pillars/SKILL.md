---
name: vid-pillars
description: Locks the 8 to 12 content pillars that deliver on the creator's Iceberg Statement. The bottom of the iceberg, categories of teaching not video titles. Runs after vid-positioning. Triggers on "build my content pillars" or "what should I teach".
---

# Pillars

Lock the 8 to 12 content pillars that deliver on the Iceberg Statement.

The Iceberg Statement (built by `vid-positioning`) is the top of the iceberg: the one-sentence promise. The pillars are the bottom: the categories of teaching that prove the promise across every video. Pillars are not videos. They're the menu.

## Contract

**Inputs (required):** `foundation/iceberg.md` with the Iceberg Statement locked. Also needs `foundation/avatar.md` (Avatar and Top 3 problems) to validate that pillars solve the right problems.

**Inputs (optional):** `foundation/voice-profile.md`, `foundation/offer.md`.

**Outputs:** Content pillars (bottom of the iceberg) section written to `foundation/iceberg.md`. 8 to 12 pillars, numbered.

**Downstream consumers:** every per-video skill. `vid-framing` checks that a video idea maps to a pillar. `vid-research` uses the pillars to anchor pattern banks. `vid-title` and `vid-thumbnail` test alignment against the pillar a video sits in.

## Load at session start

1. `${CLAUDE_PLUGIN_ROOT}/knowledge/interview-posture.md`. Shared posture. Non-negotiable.
2. `${CLAUDE_PLUGIN_ROOT}/knowledge/vault-integration.md`. Frontmatter schema.
3. `foundation/iceberg.md` and `foundation/avatar.md`. Read the Iceberg Statement, Avatar, and Top 3 problems. Add `foundation/offer.md` when proposing the starter list.
4. `foundation/voice-profile.md` if it exists.

## Pre-check (silent)

Migration first: if `foundation/creator-foundation.md` exists, the breakup into the five foundation files hasn't finished. Follow `${CLAUDE_PLUGIN_ROOT}/knowledge/foundation-migration.md`, then resume this pre-check after the migration completes.

Then read `foundation/iceberg.md`. Three states:

- **No Iceberg Statement.** Stop. Tell the creator: "Run `vid-positioning` first. The pillars deliver on the Iceberg Statement, and I need the locked statement to map them."
- **Iceberg Statement present, no pillars yet.** Fresh run.
- **Pillars already locked.** Surface the list and ask: "Pillars locked (count of them). Refresh, keep, or replace?"

## What a pillar is

A pillar is another problem that, when broken in the avatar's life, prevents them from getting the result the Iceberg Statement promises. The channel teaches across these pillars. Each pillar is a root cause of the BIG problem named in the statement.

That framing matters. Pillars are not "categories of teaching that sound like the niche." They are sub-problems that cause the main problem. The content under each pillar teaches the fix for that sub-problem.

Example logic (not for the creator to copy, just to calibrate the thinking):

If the Iceberg Statement is "I help [avatar] [get result] using [method] without [tension]," then the pillars are: "what are all the other problems that block [avatar] from [result]?"

When one of those sub-problems is fixed, the avatar moves closer to the result. When several are fixed in combination, the result lands.

### Pillars are NOT

- Video titles ("How to write a hook in 5 minutes").
- Single tactics or tools ("Use the 3-2-1 hook formula", "Claude Code tutorials").
- Categories named after the niche ("YouTube growth", when the Iceberg promise IS YouTube growth, the pillar is something that's blocking it).
- One-off insights or stories.

### Pillars ARE

- Root-cause sub-problems ("Their videos look generic", "They have no content system", "They have no offer to convert views into revenue").
- Recurring lenses on those sub-problems that the creator can teach across many videos.
- Things the avatar would say are blocking them, even if those things don't sound like the niche on the surface.

A good pillar can fuel 5 or more distinct videos because each sub-problem has many angles. A bad pillar is either a video, a tactic, or just the niche's name repeated back.

### The root-cause test

For every pillar proposed, ask silently: "If the avatar fixed THIS, would they be closer to [Iceberg Statement promise]?" If yes, it's a pillar. If no, it's something else.

## How this skill runs

This is a discovery interview. Run the absorb-first protocol from `${CLAUDE_PLUGIN_ROOT}/knowledge/interview-posture.md`. Short messages. One question at a time. Don't form-fill.

### Step 1: Propose a starter list

Read the Offer, Avatar, Top 3 problems, and Iceberg Statement. Then ask yourself the root-cause question:

> "What problems, when broken in this avatar's life, BLOCK them from getting [the Iceberg Statement promise]?"

Generate 8 to 12 starter pillars by mining for those root-cause problems. Look in three places:

1. **The Top 3 problems.** Each one is already a root cause the avatar named. Expand each into the broader sub-problem behind it.

2. **Other problems the creator hinted at.** Scan the Offer and Avatar sections for problems the creator described that didn't make it into Top 3. Those are still valid pillars.

3. **Standard root causes for the promise.** Things the creator may not have said out loud but probably knows about. If the Iceberg promises revenue, "offers" is a root cause whether named or not. If the promise is consistency, "content systems" is a root cause.

The pillars should NOT all sound like the niche. If the Iceberg promises YouTube growth, "YouTube growth" is not a pillar. The pillars are the OTHER problems that, when broken, cause YouTube growth to fail. Storytelling. Offers. Email. Productivity. Mindset. The teaching is what fixes those problems.

**Format: each pillar is 1 to 4 words. A short label. Not a sentence. Not a video title.**

Right format:
- Storytelling
- Packaging
- Retention
- Offers
- Mindset
- AI voice
- Content systems

Wrong format:
- "How to get AI to sound like you, not slop"
- "Retention and storytelling. Keeping viewers past 30 seconds."

Shape of the message:

> "Reading your foundation. Iceberg Statement: '[the statement].'
>
> Starter pillars. 8 to 12 root-cause sub-problems that block your avatar from getting that result. Short labels, drafts to react to.
>
> 1. [label]
> 2. [label]
> 3. [label]
> 4. [label]
> 5. [label]
> 6. [label]
> 7. [label]
> 8. [label]
> 9. [label]
> 10. [label]
>
> Which land, which are duds, what's missing?"

The creator reacts. Drop, replace, add. Iterate until 8 to 12 short labels are locked.

### Step 2: Push back on tactics posing as pillars

When the creator's reaction adds a pillar that's actually a tactic or a single tool, push back. The pillar definition is sharp: it can fuel 5+ distinct videos for years.

If they say "AI prompts for thumbnails" or "Claude Co-Work tutorials," that's a tactic OR a tool category. The pillar might be "AI plus thumbnail design" or "AI tool walkthroughs for content." The tool is the example, not the category.

Push back with a concrete probe:

> "'[Tactic the creator named]' is one video, or maybe a tactic inside a bigger pillar. Could you make 10 videos on it without repeating yourself? If yes, what's the broader category it sits inside?"

If they say yes 10 videos easily, lock as the pillar. If they hedge, the pillar is the parent category.

### Step 3: Apply the through-line if the creator gives you one

If the creator says something like "every pillar should be AI plus a content thing," that's a through-line. Apply it to every pillar in the list. Rewrite the ones that drift.

Example: a list that has "Mindset for creators" gets rewritten to "Mindset for the business-owner creator working with AI" so the through-line holds.

### Step 4: Pressure-test the list

Three checks. Apply them silently as you iterate. Push back when a pillar fails.

**Check 1: Pillar vs video vs tactic.**

If a "pillar" is really one tactic, one insight, or one tool tutorial, push back:

> "'How to use Claude for thumbnails' is a video or a tactic. The pillar would be 'AI plus thumbnail design' or 'AI tool walkthroughs for creators.' What's the category this lives in?"

**Check 2: Is this a root cause of the big problem?**

The pillar should be a problem that, when broken, blocks the Iceberg Statement promise. If a pillar can't pass that test, it's something else.

> "If the avatar fixed [pillar], would they be closer to [Iceberg promise]? If not, it might be a different channel."

If the answer is "yes but only loosely," push for sharper. The pillars that matter are the ones with the tightest causal line to the promise.

**Check 3: Can the creator teach this for years?**

A pillar that runs out after 2 videos isn't a pillar. The 10-videos test:

> "Could you make 10 videos on this without repeating yourself? If yes, it's a pillar. If no, it's a tactic, and we need to find the broader category it sits inside."

### Step 5: Validate the full list

Once the list hits 8 to 12, validate the whole set against the root-cause test:

> "If the avatar fixed all of these, would they get [the Iceberg Statement's promise]? Or is there a sub-problem still blocking them?"

If yes, lock. If a gap exists, ask:

> "What sub-problem isn't covered yet? If [avatar] still struggled to [Iceberg promise] after fixing all of these, what would the missing block be?"

Add the missing pillar. Re-validate.

### Step 6: Save

Write the pillars to `foundation/iceberg.md` in the Content pillars section. Numbered list. Each pillar is the short label only, 1 to 4 words. No sub-descriptions, no teaching-focus bullets, no parentheticals explaining the pillar. The label IS the pillar.

If the creator handed you longer phrasing during iteration, compress to the short label before saving. The longer phrasing was for negotiation, the saved version is the working title.

Use the creator's words for the label where they gave you good phrasing. Sharpen only by trimming filler.

## Closing the skill

Announce the lock and auto-advance to `vid-credibility`. No friction step.

> "Pillars locked. (count) of them. Moving to vid-credibility for your three brags."

Then immediately invoke `vid-credibility` via the Skill tool. If the creator explicitly says they want to stop, respect that.

## Edge cases

**Creator gives 15+ pillars and won't pick.** That's not unusual at first. Force-rank: "Pick the 12 most valuable for [avatar] over the next 6 months. The others stay on a parking-lot list. We can add them later when one of the original 12 thins out."

**Creator only has 4 to 6 pillars and can't think of more.** Two paths. Either the Iceberg Statement is too narrow (revisit `vid-positioning`) or the creator hasn't mined adjacent topics yet. Ask: "What do clients ask you about that you don't usually teach publicly, but you could?"

**Creator's pillars all sound the same.** Three flavors of one topic. Push back: "These three all live in 'hook writing.' Either combine them into one pillar, or split into three distinct angles (hooks for cold viewers, hooks for warm viewers, hooks for hot viewers). Which is real?"

**Brand-new creator with no teaching history.** MVP fine. Flag it: "This is the starting menu. After you publish 6 to 10 videos, you'll see which pillars actually resonate and which need replacing. Refresh in 3 months."

**Professional creator who never had the avatar's problem.** Pillars can still include the creator's own expertise plus client cases. "Stories from clients I've worked with" is a valid pillar. Don't fabricate client stories. Use real ones.

## Anti-patterns

- Writing video titles instead of pillars. Categories, not videos.
- Letting a tactic or insight pose as a pillar.
- Three pillars that are flavors of one umbrella.
- Locking pillars without showing the creator the exact proposed list first.
- Asking the creator to re-confirm the Iceberg Statement. That was locked by `vid-positioning`. Move forward.
- Form-style listing of all prompts at once. Pull prompts one at a time.
- Letting the list lock at 5 or 6 pillars. The minimum is 8.
- Saving pillars in marketing language ("Revolutionary Hook System"). Use plain phrasing.
