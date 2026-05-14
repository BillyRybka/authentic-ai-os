---
name: vid-credibility
description: Lock three viewer-relevant credibility brags the creator can use in intros. Specific numbers, real wins, declarative past tense. Big plus Specific plus Personal. Runs as the 4th foundation skill after `vid-pillars`. Triggers on "build my credibility brags", "intro proof", "what should I say about myself in intros", "lock my three brags", "credibility statement", or whenever the creator needs trust-builders for their hook section.
---

# Credibility

Lock three viewer-relevant credibility brags. Each one: Big, Specific, Personal. Declarative past tense. No years, no credentials, no anti-proof.

These are the sentences the creator says in nearly every intro to signal "I know what I'm talking about on THIS topic." They are NOT a resume. They are NOT a client list. They are three sharp wins the viewer cares about.

## Contract

**Inputs (required):** `foundation/creator-foundation.md` with Avatar and Top 3 problems sections locked. The brags have to match what the avatar actually cares about.

**Inputs (optional):** `foundation/voice-profile.md`.

**Outputs:** Credibility brags section written to `foundation/creator-foundation.md`. Three numbered brag sentences.

**Downstream consumers:** `vid-intro` (rotates brags through hook sections), `vid-script`, every per-video skill that touches the intro.

## Load at session start

1. `knowledge/interview-posture.md`. Shared posture. Non-negotiable.
2. `knowledge/vault-integration.md`.
3. `foundation/creator-foundation.md`. Read Avatar and Top 3 problems.
4. `foundation/voice-profile.md` if it exists.
5. `references/credibility-method.md` when drafting starts. Holds the Big plus Specific plus Personal rule, the anti-proof check, and the good/bad pairs.

## Pre-check (silent)

Read `foundation/creator-foundation.md`. Three states:

- **No Avatar or no Top 3.** Stop. Tell the creator: "Run `vid-avatar` first. I need to know who you're building credibility WITH before I can tell what proof actually lands."
- **Avatar plus Top 3 present, no Credibility brags yet.** Fresh run.
- **Credibility brags already locked.** Surface them and ask: "Three brags locked. Refresh, keep, or replace?"

## What a brag is

A credibility brag answers: "Why should I trust THIS person on THIS topic?"

It does NOT answer: "Why should I respect this person?"

### A brag IS

- "I made $4M from my YouTube channel in 2025."
- "I went from 400 subscribers to 358,000 in just over a year."
- "I've treated 3,000+ patients in my clinic."

Three things: Big, Specific, Personal. Past tense. Number attached.

### A brag is NOT

- "I've been doing this for 10 years." (years say nothing about what was produced)
- "I have an MBA from Stanford." (credential, not result)
- "I've worked with Fortune 500 companies." (name-drop, not viewer outcome)
- "I've helped many businesses become more efficient." (no number, no scale, no result)

## How this skill runs

This is a three-question interview. Apply the absorb-first protocol from `knowledge/interview-posture.md`. Short messages. One question at a time. Push back hard when an answer hedges.

### Opener

> "Three credibility brags for your intros. Specific wins your viewer cares about. Not years, not credentials. Each one: a number plus a past-tense verb. Three questions."

### Question 1: Biggest personal result

> "What's the biggest result you've personally hit that your avatar wants? Number plus timeframe."

**Push back on years or credentials:**

> "'10 years of experience' tells me nothing. What did 10 years produce? A number."

**Push back on hedges:**

> "'I've been building' is in-progress. 'I built' is proof. Past tense."

### Question 2: Most impressive client win

> "Most impressive client win you can cite with real numbers. Name them if you have permission, before plus after, and how long it took."

**Push back on vague scale:**

> "'I've helped many businesses' doesn't work. How many specifically? What was the result for the best one?"

**If the creator names a client by name:** create or update `People/{Full Name}.md` (stub if missing) and wikilink the name in the brag. Per the project's vault rule, every human mentioned gets a profile. Backlinks make the brag traceable to a real person.

### Question 3: Volume number

> "Volume. How many clients, how many dollars, how many cases, how many videos? One specific integer."

**Push back on softeners:**

> "Declarative past tense. 'I built, I served, I made.' Not 'I've been working on building.'"

### Synthesis

Once the three raw answers are in, draft three brag sentences. Each one: Big plus Specific plus Personal. Show all three back to the creator:

> "Three brags. Read each one out loud. Anything that sounds off or that you'd reword?"

Iterate on whatever they reword. Lock when they read all three without stumbling.

### Anti-proof check (mandatory before lock)

For each brag, ask silently: "Does this make the CREATOR the source of failure?"

Example of accidental anti-proof:

> "Since 2022, I've built systems for over 50 businesses. The #1 reason those systems fail..."

That reads like the creator's systems fail. Reframe to:

> "Since 2022, I've built systems for over 50 businesses. The #1 mistake business owners make before they come to me..."

The creator is the expert. The mistake is the viewer's, the avatar's, or the niche default. NOT the creator's own work.

If any brag triggers anti-proof, push back:

> "Read that one again. Listen for whether it sounds like YOU produced the failure, or like the avatar produced the failure before finding you. The frame matters."

Lock only after every brag passes the anti-proof check.

## When the creator has no big numbers yet

Brand-new creator. No client wins. Three fallback angles, ranked weakest to strongest:

- **Education:** "I spent 2 years studying [specific thing]."
- **Consumption:** "I've read 300+ books on [topic]."
- **Personal transformation:** "I went from [bad state with numbers] to [good state with numbers] myself."

Personal transformation is strongest because it's a result, just the creator's own.

Flag the MVP caveat:

> "These are MVP brags. They work for cold viewers. As soon as you produce real client wins, replace them. Stronger proof always wins."

## Save

Write the three brags to `foundation/creator-foundation.md` in the Credibility brags section. Three numbered lines. Use the creator's words verbatim where possible. Sharpen only by trimming filler or fixing tense.

## Closing the skill

Announce the lock and auto-advance to `vid-backstory`. No friction step.

> "Three brags locked. Moving to vid-backstory for your Problem-Action-Outcome story."

Then immediately invoke `vid-backstory` via the Skill tool. If the creator explicitly says they want to stop, respect that.

## Edge cases

**Creator gives all three brags as one type (e.g. all personal results, no client wins).** Push back once:

> "All three are your own results. The avatar trusts personal proof plus client proof plus volume. Do you have a client win you can swap in for one of these?"

If they genuinely don't have a client win, lock as-is and flag MVP.

**Creator gives a brag in the wrong topic.** A creator helping people quit smoking shouldn't lead with "I sold $1M in t-shirts." Push back:

> "That's a real number, but the avatar here is trying to quit smoking. Is there a brag closer to that result, even a smaller one?"

**Creator gives a name-drop ("I worked with Brand X").** Convert to a result:

> "Working with Brand X is the setup. What did you actually produce for them? A number, a result, a before-after?"

**Creator wants more than three brags.** Three is the rotation set. More brags get used in different videos, but the locked set is three. Tell them:

> "Three for the foundation. Extra wins can live in your story bank for video-specific intros. The Top 3 is the rotation that signals trust on every video."

## References

- `references/credibility-method.md`. Big plus Specific plus Personal rule. Good/bad pairs by trap type. Anti-proof check in depth. Fallback brags for new creators.

## Anti-patterns

- Locking a brag without running the anti-proof check.
- Letting "I've been doing this for X years" pass as a brag. Years aren't proof.
- Accepting credentials ("MBA from X") in place of results.
- Locking a hedged brag ("I've been working on building..."). Past tense or rewrite.
- Locking a name-drop ("I worked with Fortune 500"). Result or rewrite.
- Locking brags without showing the creator the exact proposed text first.
- Asking for the avatar or Top 3. Those were locked by `vid-avatar`. Read them.
