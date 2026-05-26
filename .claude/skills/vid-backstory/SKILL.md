---
name: vid-backstory
description: Lock the creator's Problem-Action-Outcome backstory in 1 to 2 conversational paragraphs, plus a 3-sentence compressed version for quick intros. Concrete actions, real numbers, no corporate tone. 5th foundation skill, runs after `vid-credibility`. Triggers on "build my backstory", "write my origin story", "what's my journey", "lock my PAO", "write the about section", or whenever the creator needs the story that gets reused across videos, channel banners, welcome emails, and case studies.
---

# Backstory

Lock the creator's Problem-Action-Outcome backstory. 1 to 2 conversational paragraphs. Concrete actions. Real numbers. No corporate tone.

The backstory establishes how the creator went from the avatar's problem to the avatar's outcome. It gets reused across video intros, channel banners, welcome emails, and case study scripts.

## Contract

**Inputs (required):** `foundation/creator-foundation.md` with Avatar and Iceberg Statement sections locked. The backstory has to match the positioning, so positioning has to exist first.

**Inputs (optional):** `foundation/voice-profile.md`.

**Outputs:** Backstory section written to `foundation/creator-foundation.md`. 1 to 2 short paragraphs plus a 3-sentence compressed version for quick intros.

**Downstream consumers:** `vid-intro` (pulls the 3-sentence version), case study scripts, channel banner copy, welcome email sequences.

## Load at session start

> **Resolving `knowledge/` paths.** Any path written `knowledge/X.md` is a plugin reference file. Load it from `${CLAUDE_PLUGIN_ROOT}/knowledge/X.md` when running as an installed plugin. If `${CLAUDE_PLUGIN_ROOT}` is unset or that path does not exist (running from the source repo during development), load `knowledge/X.md` relative to the repo root instead.

1. `knowledge/interview-posture.md`. Shared posture. Non-negotiable.
2. `knowledge/vault-integration.md`.
3. `foundation/creator-foundation.md`. Read Avatar and Iceberg Statement.
4. `foundation/voice-profile.md` if it exists.
5. `references/backstory-method.md` when drafting starts. Holds the Problem-Action-Outcome structure, the Action-section test, examples, and good/bad pairs.

## Pre-check (silent)

Read `foundation/creator-foundation.md`. Three states:

- **No Avatar or no Iceberg Statement.** Stop. Tell the creator: "Run `vid-avatar` and `vid-positioning` first. Your backstory has to match the avatar and the promise, so I need those locked before I can shape this."
- **Avatar plus Iceberg present, no Backstory yet.** Fresh run.
- **Backstory already locked.** Surface the first sentence and ask: "Backstory locked. Refresh, keep, or replace?"

## The structure

Problem-Action-Outcome. Three parts. One short paragraph for Problem. One slightly longer paragraph for Action plus Outcome.

- **Problem.** What the creator (or their real client) struggled with. Same problem the avatar has now. Specific numbers, specific moments, what a bad week looked like.
- **Action.** What they DID. Concrete verbs. Not summary. Not "I built a system." List the moves: what they stopped doing, what they started, what they tried first that didn't work, what they kept.
- **Outcome.** The transformation. Real numbers, real timeframe, what's different now.

Length: 1 to 2 short paragraphs. Conversational tone. Contractions OK.

## How this skill runs

Four-question interview. Apply the absorb-first protocol from `knowledge/interview-posture.md`. Short messages. One question at a time. Push hard on Q3 (the Action section is where most backstories fail).

### Opener

> "Backstory. 1 to 2 paragraphs: how you (or a real client) went from the avatar's problem to the outcome. Four questions to build it."

### Question 1: The starting state

> "Before things changed, what was the state? Numbers, what a bad week looked like, what specifically was broken."

**Push back on vague struggle:**

> "'I struggled for years' doesn't land. What did a bad Tuesday look like? What were the numbers at the lowest point?"

**Push back on corporate tone:**

> "Say it like you'd say it to a friend at dinner. 'I had been practicing physiotherapy when I noticed' is press release. 'I'd been a physio for 15 years and kept seeing the same thing' is human."

### Question 2: The trigger

> "What specific moment or realization made you change direction? Not 'I decided to improve.' The actual trigger."

The trigger anchors the story. It's the moment the audience can feel.

### Question 3: The moves (this is where most backstories fail)

> "What did you STOP doing and START doing? List the concrete moves. Not the summary. What did you stop? What did you replace it with? What did you try first that didn't work?"

**Push back hard:**

> "'I built a system' is a summary. Someone reading this doesn't know what you actually did. What did you document? Who did you hire first? What ritual did you install? What did you remove from your calendar?"

**Run the Action-test:**

> "Read your action list out loud. Could someone else do what you did from what's written? If not, keep drilling."

This step usually needs 2 to 3 rounds. Don't move on until the Action section reads like a list of moves a stranger could follow.

### Question 4: The outcome

> "Outcome. Real numbers, real timeframe, what's different now."

**Push back on vagueness:**

> "'Now I help others' isn't an outcome for YOU. What changed for you? Subscribers, revenue, time, weight, relationships. Something measurable."

If the journey had a setback or a "first videos flopped" moment, capture it. That makes the outcome more believable, not less:

> "Did you have a moment where it almost didn't work? People trust an outcome more when the path wasn't a straight line."

### Synthesis

Assemble Problem, Action, Outcome into 1 to 2 paragraphs. Use the creator's words. Light cleanup only. If you see "leveraged" or "proprietary methodology" anywhere, push back:

> "Read it back. If that word would sound weird coming out of your mouth in a real conversation, change it."

Show the draft to the creator:

> "Here's the draft. Read it out loud. Anything you'd reword?"

Iterate on rewords. Lock when they read it without stumbling.

### The 3-sentence compressed version

After the full backstory locks, build the 3-sentence version for quick intros:

- Sentence 1: one sentence of context (who they were before).
- Sentence 2: one sentence of the proof (number + result).
- Sentence 3: one sentence of the promise tying to the channel.

> "Last step. Compress this into 3 sentences for video intros. Context, proof, promise. One sentence each."

### Save

Write the full backstory and the 3-sentence version to `foundation/creator-foundation.md` in the Backstory section. Preserve the creator's phrasing. Light cleanup only.

## Closing the skill

Backstory is the last foundation interview in this release. Announce the lock and that foundation identity is complete. Do NOT auto-invoke any next skill: the released foundation chain ends here.

> "Backstory locked. Full version plus the 3-sentence intro version. That completes your foundation identity. More skills are coming for voice capture, content production, and pattern research. For now, this is your foundation."

Stop. Do not point at unreleased skills.

## Edge cases

**Creator never had the avatar's problem.** Doctors, physios, consultants. Swap "you" for "a real client." Same Problem-Action-Outcome structure. Attribute clearly: "A client came to me with..." or "I worked with a patient who..."

If a client is named by name, create or update `People/{Full Name}.md` (stub if missing) and wikilink the name. Per the project's vault rule, every human mentioned gets a profile.

**Creator's Action section keeps coming back as summary.** Three rounds of push-back didn't crack it. Two paths:

- Ask: "Walk me through one specific day during the change. What did you do that morning? Who did you call? What did you write down?" The specific-day cut-through usually unlocks concrete verbs.
- Or: "If a friend texted you tomorrow asking 'how did you actually do this?' what would you tell them step by step? Not the polished version. The actual messy one."

**Creator wants the backstory to be brand new and impressive.** Push back. "The backstory's job is trust, not polish. A path with a setback in it earns more trust than a perfect arc. Don't dress this up."

**Brand-new creator with no big numbers yet.** Two fallback paths:

- Borrow a real client's story (with attribution). The Problem-Action-Outcome is theirs, not the creator's.
- Use the creator's own personal transformation, even at smaller scale. "I went from 4 inbox bankruptcies a year to zero" is real and lands even without a million-dollar outcome.

Flag MVP. Real client wins replace this when they exist.

## References

- `references/backstory-method.md`. Problem-Action-Outcome structure in depth. Action-section test. Good/bad pairs by trap type. Examples by niche.

## Anti-patterns

- Accepting a summary in place of an Action section. "I built a system" is not a backstory.
- Corporate tone ("leveraged", "proprietary methodology", "ecosystem"). Conversational or rewrite.
- Outcomes without numbers ("now I help others"). A real number or rewrite.
- Fabricating details. Never invent. If the creator can't recall it, leave it out.
- Mixing creator backstory and client backstory in one story. Pick one per story.
- Polishing away the setback. "First videos flopped" earns trust. Don't sand it off.
- Locking the backstory without showing the creator the exact proposed text first.
- Asking for the avatar or Iceberg Statement. Those were locked upstream. Read them.
