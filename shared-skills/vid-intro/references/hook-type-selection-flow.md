---
type: reference
scope: skill-local
loaded_by: [vid-intro]
status: active
tags: [reference, hook, selection-flow]
---

# Hook Type Selection Flow

The decision flow `vid-intro` runs to pick which of the 5 canonical hook types to lean on for THIS video. The 5 types and their patterns live in [[intro-architecture]] Step 2 and [[hook-patterns]]; per-format hook-lane defaults live in each `knowledge/format-planners/{format}.md`'s intro-adaptation table. This file does NOT restate any of those. It teaches the runtime decision: how `vid-intro` cross-references those sources to pick the lane for a specific video.

Examples-first contrastive: every rule shows a worked match plus a near-miss with one-line "why this lands / why this doesn't."

## The four inputs

`vid-intro` cross-references four things to pick the lane:

1. **Format** (from `content/pieces/{slug}/piece.md`'s `format:` field) → consult the format planner's intro-adaptation table for recommended hook lanes
2. **Voice profile** (from `foundation/voice-profile.md`'s `preferred_hook_types`) → which lanes the creator naturally lands
3. **Channel size and creator credibility** (from `foundation/credibility.md`) → whether Credibility Hook is safe
4. **Video material** (from `brain-dump.md` / `piece.md`) → does the actual content support the lane (e.g. a Fact Hook needs a real surprising stat in the material)

When all four agree, lock the lane. When they disagree, the format planner usually wins because the format's identity is the audience's expectation. Voice profile breaks ties between two format-allowed lanes.

## Worked: Format and voice agree

**Setup:** Step-by-Step video on Photoshop shortcuts. Voice profile says `preferred_hook_types: [question, statement]`. Brain dump has no surprising stat (rules out Fact). Channel is 8k subscribers (too small for naked Credibility).

**Decision:** Lock lane = Question or Statement. Two candidates, one each, surface to creator.

**Why this lands:** format and voice both pull toward the same two lanes; brain dump and channel size eliminate the others cleanly. Single short message to the creator with two distinct candidates.

## Worked: Format and voice disagree, format wins

**Setup:** Success Story video. Voice profile says `preferred_hook_types: [question, fact]`. Format planner recommends Question or Statement (lead with outcome). Brain dump has a $250k client outcome.

**Decision:** Lock lane = Question or Statement. The Success Story format's "lead with the receipt" identity overrides the creator's natural Fact preference because the receipt IS the engine of the format. Surface a Question candidate AND a Statement candidate that both lead with the outcome.

**Why this lands:** format identity dominates because audience expectation for success stories is "show me the outcome up front." A Fact Hook here would feel like a misfiled video.

## Worked: Channel size flags Credibility risk

**Setup:** Deep Dive video. Voice profile says `preferred_hook_types: [credibility, statement]`. Channel has 800 subscribers. Brain dump has a personal result of $40k from a single video.

**Decision:** Flag the Credibility risk to the creator: "Credibility hooks tend to under-perform on small channels because cold viewers don't trust an unknown 'I' yet. The $40k claim could earn it as a single dramatic line, OR we can use a Statement Hook that bakes the same number in. Want to keep Credibility as a candidate, or shift?"

Creator's call. If they keep Credibility, surface one Cr candidate alongside one Statement candidate so they can see both in context. If they shift, lock Statement.

**Why this lands:** the risk is named (cold-trust failure), the alternative is offered (Statement Hook still uses the $40k), and the creator decides. The skill doesn't auto-reject because a single dramatic claim CAN earn a Credibility Hook even on small channels (per [[intro-architecture]] step 2).

## Near-miss: Picking Fact when the brain dump has no real fact

**Setup:** List video on productivity habits. Voice profile says `preferred_hook_types: [fact, statement]`. Brain dump has the 10 habits but no surprising stat.

**Wrong move:** generate a Fact Hook anyway and invent a plausible-sounding stat ("Studies show 73% of people quit their habits in week 3").

**Why this fails:** anti-fabrication is a hard rule. The "73%" doesn't exist in the brain dump or in any cited study. Even if it sounds plausible, it lies to the viewer. The generated Fact Hook gets blocked at candidate generation. Lane shifts to Statement (next preference) which can build a hook from the brain dump's actual material without invention.

**The rule:** if the lane requires material the brain dump doesn't have, the lane is wrong for this video. Don't fabricate to fill a slot.

## Near-miss: Forcing Question lane when format identity rejects it

**Setup:** News video on a tool that just shipped a new feature. Voice profile says `preferred_hook_types: [question, fact]`.

**Wrong move:** lead with a Question Hook ("Have you ever wondered why your AI tool keeps forgetting context?") because the creator's voice profile prefers it.

**Why this fails:** News format identity is speed. Question Hooks burn 3-5 seconds setting up a question the news itself answers. The format planner explicitly says "Question hooks waste seconds." Lane shifts to Fact ("This shipped today: [tool] now keeps context across all your chats. Here's why it matters.") or Statement ("[Tool] just changed how memory works for every AI chat.").

**The rule:** format identity beats voice preference when they conflict. Voice profile breaks ties, not overrides.

## The decision short-list (run silently in Phase 1)

Run through these in order:

1. **Read the format planner's intro-adaptation table.** List the format's recommended hook lanes.
2. **Read the voice profile's `preferred_hook_types`.** Note which of the format's lanes match the creator's preferences.
3. **Check channel size and credibility.** If Credibility Hook is in the format's recommended set AND the channel is small or new AND the brain dump doesn't have a single dramatic claim, flag it.
4. **Check brain dump material.** If the format prefers Fact but brain dump has no surprising stat, eliminate Fact. If the format prefers Credibility but brain dump has no usable receipt, eliminate Credibility.
5. **Lock 1-2 lanes.** Pick the intersection of format-recommended AND voice-preferred AND material-supported. Generate 2-3 candidates inside those lanes.

Surface only the locked lanes to the creator. Don't show them the elimination process. That's noise.

## When to override the flow

These are the cases where the creator deliberately breaks the default and the override usually works:

- **Single dramatic claim on a small channel.** A creator with 200 subscribers but a $1.2M sale of their last business CAN lead with Credibility. The dramatic claim earns the cold-trust override.
- **Statement-Confession blend on a List Video.** A Statement Hook delivered as a personal confession ("Did you think this would be easy? I did.") still counts as Statement lane but shifts the energy. The format planner allows it.
- **Contrarian in a niche where every other channel preaches the conventional wisdom.** Even if the creator's voice profile leans Question, the contrarian advantage outweighs the voice preference when the niche is starved for inversions.

When the creator wants to override, the skill confirms once ("Going with Credibility on a smaller channel: the $1.2M sale should earn the cold-trust override. Cool to proceed?") then locks the lane. Don't argue twice.

## What this file does NOT do

- It does not list every hook pattern. That's [[hook-patterns]].
- It does not make the final creative call. The creator picks among 2-3 candidates.
- It does not enforce voice preferences as laws. Voice profile is a fingerprint, not a rule. Match it unless format identity overrides.
