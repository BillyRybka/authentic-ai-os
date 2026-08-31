---
name: vid-avatar
description: Locks who the viewer is via a three-phase interview producing the offer, avatar, and Top 3 perceived problems in viewer language. First foundation skill. Triggers on "build my avatar", "who is my audience", or "start my channel foundation".
argument-hint: "(optional: any starting context)"
---

# Avatar

Lock who the viewer is. Three things, in order:

1. **Offer.** What the creator currently sells or plans to sell.
2. **Avatar.** Who the offer is for, in a few plain sentences.
3. **Top 3 perceived problems.** What the avatar says when they complain.

This is the first skill in the foundation sequence. Without it, `vid-positioning` can't draft a sharp Iceberg Statement.

## Contract

**Inputs (required):** none. This is the first foundation skill. Creator brings their own context.

**Inputs (optional):** existing `foundation/offer.md` and `foundation/avatar.md` for refresh runs.

**Outputs:** the Offer written to `foundation/offer.md`; the Avatar and Top 3 perceived problems written to `foundation/avatar.md`. Both files use their templates in `${CLAUDE_PLUGIN_ROOT}/knowledge/foundation-templates.md`.

**Downstream consumers:** `vid-positioning` (reads all three sections), `vid-pillars`, `vid-credibility`, `vid-backstory`, `vid-research`, every per-video skill in the pipeline. `vid-voice-capture` (in development) will also read all three sections when it ships.

## Load at session start

1. `${CLAUDE_PLUGIN_ROOT}/knowledge/interview-posture.md`. The shared interview posture every foundation interview skill follows. Conversation shape, voice rules, how to handle messy answers, how to use the creator's exact words. Non-negotiable.
2. `${CLAUDE_PLUGIN_ROOT}/knowledge/vault-integration.md`. Frontmatter schema, wikilink contracts.
3. `foundation/voice-profile.md` if it exists. Its anti-patterns override the voice rules in `${CLAUDE_PLUGIN_ROOT}/knowledge/interview-posture.md`.

## What this produces

Two foundation files:

- **`foundation/offer.md`.** One paragraph describing what they sell and the result the buyer walks away with.
- **`foundation/avatar.md`.** The Avatar (a few sentences describing the viewer, not a structured field list) plus the Top 3 perceived problems (three problems in viewer language, equally weighted).

If a file doesn't exist, create it from its template in `${CLAUDE_PLUGIN_ROOT}/knowledge/foundation-templates.md`.

## What this skill is NOT

This skill does NOT produce:

- The Iceberg Statement → that's `vid-positioning`
- Content pillars (bottom subtopics) → that's `vid-pillars`
- Credibility brags → that's `vid-credibility`
- Backstory → that's `vid-backstory`
- Voice profile → that's `vid-voice-capture` (in development, not shipped yet)

If the creator asks for positioning, pillars, credibility, or backstory, finish the avatar work first, then point them at the right skill. If they ask for voice capture, tell them it is in development and coming in a future release.

## Pre-check (silent)

Migration first: if `foundation/creator-foundation.md` exists, the breakup into the five foundation files hasn't finished. Follow `${CLAUDE_PLUGIN_ROOT}/knowledge/foundation-migration.md`, then resume this pre-check after the migration completes.

Then read `foundation/offer.md` and `foundation/avatar.md` if they exist.

- **Both missing** → fresh run. Create each from its template in `${CLAUDE_PLUGIN_ROOT}/knowledge/foundation-templates.md` at its first save. Open Phase 1.
- **Offer + Avatar + Top 3 all present** → ask refresh / keep / replace. Surface the avatar back.
- **Partial** → resume. Tell the creator: "Picking up where you left off. Locked: [filled sections]. Next: [first unfilled]." Skip to the first unfilled phase.

## The three phases

Run in order. One question at a time. Short messages. Follow the posture in `${CLAUDE_PLUGIN_ROOT}/knowledge/interview-posture.md`.

### Phase 1: Offer

The offer answers what the avatar walks away with. Everything else triangulates against this.

**Opener:**

> "Let's lock who you're building this channel for. First: what product or service do you currently sell, or plan to sell?"

The creator's answer often spills into Phase 2 and 3 too. That's good. Use the absorb-first protocol from `${CLAUDE_PLUGIN_ROOT}/knowledge/interview-posture.md`. Mirror back what you heard, name the pattern, then ask the next useful question.

**Show-before-save (required).** Before writing the Offer section, show the proposed paragraph to the creator in a blockquote. Ask: "Lock this for the Offer section, or push?" Save only on explicit lock. If they push, iterate, show again, ask again.

**Save:** on lock, write the Offer to `foundation/offer.md` (create from its template if missing). One paragraph. The creator's words where possible.

### Phase 2: Avatar

**Goal:** know who this person is well enough to write for them. That's it. Not a structured form. A description.

**Opener (if Phase 1 didn't already surface enough signal):**

> "Who is this for? Describe them like you're telling a friend."

**If Phase 1 already painted the avatar,** absorb-first protocol applies. Surface what you heard:

> "Sounds like this is for [paraphrased avatar]. Is that right?"

Wait for the answer before probing further.

**When the creator stays broad:**

Broad labels like "business owners," "entrepreneurs," "creators" can be real. First confirm the read-back and wait for the answer. Then, in the next message, ask for the specifics plainly:

> "Let's get more specific about who this is for. The details that matter:
>
> - Stage they're at
> - Industry
> - What they call themselves"

If they narrow, lock the narrower version. If they don't, accept the broad label. The specificity moves into the Iceberg Statement (via `vid-positioning`) through the tension and mechanism. Don't keep fighting for a label the creator would never say.

**When they hand you a paragraph:**

Don't restructure it into fields. Absorb it as a description. Read it back:

> "So this is [a few sentences capturing what they said]. Right?"

If yes, lock the avatar as those few sentences. Save it as written, no field-by-field decomposition.

**When multiple audiences come up:**

> "Two options: pick one for the channel, or name what unites them. The channel speaks to one voice. The offer can still serve both."

Pick one. The other can run through this skill again later.

**Edge case: creator is a professional who never had the avatar's problem** (doctor, physio, consultant). The avatar is still real. The creator works with this avatar, just doesn't share their problem personally. Note this in the avatar description so `vid-backstory` knows to use a client's story instead of the creator's.

**Show-before-save (required).** Before writing the Avatar section, show the proposed description to the creator in a blockquote. Ask: "Lock this as your avatar, or push?" Save only on explicit lock. If they push, iterate, show again, ask again. Never lock the avatar without the creator seeing the exact text first.

**Save:** on lock, write the Avatar section in `foundation/avatar.md` (create from its template if missing). A few sentences. Plain description. No fields.

### Phase 3: Top 3 perceived problems

**Goal:** Three perceived problems in the avatar's words. Equally weighted.

**Opener (if not already covered):**

> "What specific problem keeps [avatar] from getting what they want?"

**If problems already came up in Phase 1 or Phase 2:** use the absorb-first protocol. Don't re-ask. Surface them back and ask the creator to confirm or refine.

> "I heard three problems while you were describing them: [problem 1], [problem 2], [problem 3]. These three feel right, or do any need a different framing?"

**The disappearance probe:**

Creators reflexively list solutions ("they need confidence," "they need systems"). Solutions aren't problems. Probe:

> "If they already HAD that, what would disappear from their day? That's the actual problem."

**When the answer sounds expert-framed:**

"Lack of systems thinking." "Operational inefficiency." Push toward viewer language:

> "How would they say it in their own words? Closer to 'I'm drowning' or 'I keep forgetting things.'"

Sanity-check against the viewer-voice bank in `references/avatar-guide.md`. Expert-column phrasing means send it back. Viewer-column phrasing means it locks.

**Three actually-different problems:**

Once one problem is clear, surface the other two:

> "Two more problems they vent about. What else keeps them stuck?"

Sanity check: three actually-different problems, not three names for the same thing. "Communication issues / emotional dysregulation / unhealthy relationship dynamics" is one problem written three ways.

**Lock-and-move rule:**

After 2 sharpening rounds on any problem, lock the usable version and move. Don't grind. MVP. The Top 3 refines as the creator publishes videos and sees what real viewers comment.

**Show-before-save (required, this is where the skill most often fails).** Before writing the Top 3 to the file, show all three proposed problems to the creator in a numbered list, in the exact wording that will land in the file. Ask: "Saving these three. Lock as written, or any of them need a different wording?" Save only on explicit lock.

Example shape:

> "Three problems. Saving these as written:
>
> 1. [exact problem 1]
> 2. [exact problem 2]
> 3. [exact problem 3]
>
> Lock as written, or push on any of them?"

Never lock the Top 3 without the creator seeing the proposed wording first. Even if the problems came up in earlier turns and seem obvious to you, the creator has to see and approve the exact text.

**Save:** on lock, write them to the Top 3 section of `foundation/avatar.md` verbatim, in the creator's quoted viewer language. Never paraphrase. Three numbered lines.

## Closing the skill

When all three sections are saved, announce the lock and auto-advance to `vid-positioning`. No friction step.

> "Avatar locked. Three problems saved. Moving to vid-positioning to draft your Iceberg Statement."

Then immediately invoke `vid-positioning` via the Skill tool. The creator doesn't need to type another command. If they want to stop, they say "stop here" or close the chat.

If the creator explicitly says they want to stop after the avatar lock ("hold here", "let me come back to this later", "stop"), respect that and don't invoke the next skill.

## Edge cases

**Brand-new creator with no clients yet.** Educated guesses are fine for MVP. Flag it:

> "We're guessing for now. The avatar and problems sharpen once you publish 3 or 4 videos and see what real comments come in."

**Creator wants to refresh an existing avatar.** Surface the current avatar and Top 3 back. Ask which sections they want to refresh. Edit in place, don't overwrite sections they want to keep.

**Creator gives a list of 12 problems and refuses to pick three.** Force-rank by urgency. Top 3 wins. Tell them:

> "We can come back to the others. The Iceberg Statement focuses on one, and the content pillars can teach all 12. The Top 3 is just what we'll lead with."

## References

- `references/avatar-guide.md`. Avatar examples plus viewer-voice problem bank organized by niche. Use it for calibration when a draft Top 3 sounds expert-framed.

## Anti-patterns

- Speaking field names aloud ("public label, fit qualifier, internal context"). These don't exist anymore. The avatar is a plain description.
- Multiple-choice questions when the creator already gave you the answer.
- Long lists of probes in one message. One question, wait, react.
- Locking the avatar as a structured field set. Description only.
- Locking Top 3 in expert language. Viewer language or send it back.
- Running `vid-positioning` inside this skill. That's a separate skill with its own posture.
