---
type: reference
scope: shared
loaded_by: [vid-intro, vid-segment, vid-ending]
status: active
tags: [reference, voice, rhythm, writing]
---

# Voice Rhythm

The lens for hearing rhythm in the creator's reference pieces and in your own draft. Loaded by every writing skill at startup. Reference material to think with, never to paste at the creator. Read [[voice-profile-schema]] first for what is stored and the load contract.

Rhythm is judged by ear against `foundation/reference-pieces/{voice_context}.md` (one file per context, passages as `## ` sections), not against stored numbers. There are no target distributions anywhere in this system. This file teaches you how to hear the difference. Examples lead. Principles follow. Every section pairs a worked example with a near-miss so the boundary is clear.

## Why rhythm needs its own lens

The guardrail in `foundation/voice-profile.md` catches literal things: refusals, words avoided, POV. It does not catch rhythm: the cadence of sentence lengths, the ratio of short paragraphs to longer ones, the punctuation feel, energy modulation across a section. A draft can pass every word-level rule and still feel wrong because the rhythm is off.

The reference pieces carry the real cadence. This file is the connective tissue: the way you read rhythm in the reference pieces and check your draft against that feel during [[voice-pressure-test]] Pass 2.

## 1. Sentence length variation

Real voice mixes short punchy sentences with medium explanatory ones. A draft that runs all-medium reads as a research summary; all-short reads as Twitter; the actual voice lives in the variation. Hear it in the reference pieces, then match the variation, not a number.

**Worked (mixed rhythm):**

> "Most creators don't have a content problem. They have a memory problem. They forgot what they actually know, so they ask AI for ideas, and AI gives them the same beige list it gave everyone else."

Why this lands: short opener, short follow-up, then a longer compound sentence that earns its length by carrying the consequence. Two beats of setup before the explanation arrives.

**Near-miss (uniform medium):**

> "The problem most creators face is that they have forgotten what they actually know. This causes them to turn to AI for ideas. The result is generic content that reads like everyone else's."

Why this misses: three sentences, all a similar length, no variation. Rhythm is flat. Same content, reads as informational instead of voiced.

**Worked (short-short-long, snap back):**

> "I tried it. It worked. The next time a client asked me how I built the system in 90 minutes instead of three weeks, I didn't have a tidy answer. I had a tested one. Easy."

Short. Short. Long with substance. Snap back short. The pattern signals confidence.

## 2. Paragraph structure ratio

Most creator voices skew toward single-sentence paragraphs in long-form prose. A wall of three-sentence paragraphs reads as essay; a wall of single-sentence paragraphs reads as Twitter. The right ratio is whatever the reference pieces for this `voice_context` do. Read them and match the shape.

**Worked (single-beat paragraphs carrying the pivot):**

> Most creators ask the wrong question.
>
> They ask "what should I post next?" when the better question is "what do I already know that nobody else knows?"
>
> The first question optimizes for output. The second one optimizes for ownership. Output without ownership is treadmill. Ownership without output is potential.
>
> Pick ownership.

Why this lands: opening is one beat. Second is one tight setup. Third is the only multi-sentence block and it earns the weight because it carries the contrast the piece pivots on. Closing is one beat for the punch.

**Near-miss (uniform multi-sentence):**

> Most creators ask the wrong question. They ask "what should I post next?" when the better question is "what do I already know that nobody else knows?" The first question optimizes for output. The second one optimizes for ownership.
>
> Output without ownership is a treadmill. Ownership without output is wasted potential. So the question becomes: how do you build ownership? You start by listing what you know.

Why this misses: every paragraph is the same shape. The eye finds no rhythm to lock onto. Same content, lower retention.

## 3. Opener pattern

What does the creator naturally do in the first line? Question, declaration, anecdote, data-first, contrarian? Most have a dominant default. It shows in the reference pieces. Match it unless there is a reason to break it. (The optional `preferred_hook_types` in voice-profile.md, if populated, names it; the reference pieces show it.)

**Worked (declaration opener, for a creator whose reference pieces lean declarative):**

> "Most YouTube channels die at 1,000 subscribers because the creator started solving a different problem than the one they validated."

Specific, declarative, sets up the whole piece in one beat.

**Near-miss (question opener for the same creator):**

> "Have you ever wondered why most YouTube channels die at 1,000 subscribers?"

Why this misses: question openers can work, but if the creator's own pieces are mostly declarative, leading with a question reads as off-creator on a feel level even though it is grammatically fine. The pattern is a fingerprint, not a rule. Match it unless there is a reason to break it.

**Worked (anecdote opener for a story-heavy creator):**

> "A client paid me $4,500 last month for a system she could have built herself in a weekend. She knows that. I told her. She paid anyway."

Drops in mid-action, no setup, full attention.

## 4. Punctuation feel

Punctuation is voice fingerprint. Em-dashes are a HARD NO across this product (vale-enforced; see [[CLAUDE]]). Use commas, periods, parens, and rare ellipses to do the work. Do not count punctuation. Hear whether the draft breathes where the reference pieces breathe.

**Worked (commas and parens, no em-dashes):**

> "Most coaches teach a thing they learned three years ago, dressed up in new language, sold as a new system. The work hasn't changed. The packaging has."

Why this lands: commas slow the first sentence into a rhythm, period snaps it shut, then two short period-only beats finish the thought. No em-dashes. Readable on screen and natural out loud.

**Near-miss (clause pileup):**

> "Most coaches teach a thing they learned three years ago, dressed up in new language, sold as a new system, the work hasn't changed, the packaging has."

Why this misses: the clauses run together with no breath. Periods and commas placed for the ear break it into actual phrases.

**Worked (parenthetical aside doing the heavy lifting):**

> "The system runs every Sunday at 6 a.m. (yes, automatically) and drops a Slack message with last week's metrics."

Why this lands: parens carry the voiced aside without breaking the sentence's spine, and without inviting the dash habit.

## 5. Word swaps the creator avoids

Per-creator avoided words live in `foundation/voice-profile.md` under `refusals`. The product also has a brand-level hard-no list (see CLAUDE.md word-swap conventions). Common swaps creators want enforced:

- ship to post
- dive in to go through, walk through, show
- leverage to use
- eats / eating (as a metaphor) to takes, consumes, burns
- unlock to open, give you, get you to
- transform to change, rebuild, swap, replace
- elevate to raise, lift, take up
- game changer to just say what changed

**Worked:** "Here's what I'd post first" instead of "Here's what I'd ship first."

**Near-miss:** "Let me dive in to how this works." (Both "let me" and "dive in" miss; rewrite as "Here's how it works" or "Walk through it with me.")

The principle: a word in `refusals` means the creator has explicitly rejected the original. Do not override on a single piece. Do not pile alternatives. Pick the closest match and move on.

## 6. Energy modulation

Same creator, different `voice_context`, different energy floor. A talking-head script dials up to performer mode. Email drops below baseline to direct and dry. The reference pieces for each context carry the right energy. Match the context you are writing for.

**Worked (script energy):**

> "Stop. Look at your last three videos. I bet two of them are the same idea wearing different hats."

Punchy. Direct address. Short imperative beats. Reads as someone fired up at camera.

**Near-miss (email energy on a script):**

> "I want to share an observation that I think might be worth considering. If you look at your last three videos, you may notice that two of them are essentially the same idea presented in different ways."

Why this fails on a script: pacing too patient, too many hedges, energy floor too low. The same insight in a newsletter would land, where patient pacing reads as thoughtful. On camera it reads as boring.

**Worked (email energy on email):**

> "I want to flag something I noticed in your last three videos. Two of them are the same idea, different hat. Worth a re-read before you publish #4."

Why this lands: same idea, calmer pacing, ends on a quiet recommendation. The reader's brain does not fight the energy.

## How writing skills use this file

At startup, every writing skill loads, per the contract in [[voice-profile-schema]]:

1. `foundation/voice-profile.md` for the guardrail (fingerprint, signature phrases, refusals).
2. `foundation/reference-pieces/{voice_context}.md` for the real cadence.
3. This file, as the lens for hearing rhythm in both.

When a draft section is finished, run [[voice-pressure-test]] before saving. Pass 2 uses this lens to judge whether the cadence matches the reference pieces.

## What this file does not do

- It does not enumerate any creator's exact patterns. The reference pieces carry those.
- It does not store or imply target numbers. Rhythm is heard, not measured.
- It does not replace the read-aloud test. If the creator reads the draft and would reword it, the rhythm is wrong even if it feels close.
- It does not catch literal banned words. Vale and the word-swap layer handle that.
