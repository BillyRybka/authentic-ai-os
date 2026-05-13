---
type: reference
scope: shared
loaded_by: [vid-intro, vid-segment, vid-ending]
status: active
tags: [reference, voice, rhythm, writing]
---

# Voice Rhythm

Loaded by every writing skill at startup. Teaches Claude how to read and preserve the creator's natural rhythm at the line level. This is reference material to think with, never to paste at the creator. Read [[voice-profile-schema]] first for the rules; this file teaches the feel.

Examples lead. Principles follow. Every section pairs a worked example with a near-miss so the boundary is clear.

## Why rhythm matters separately from voice rules

Voice rules ([[voice-profile-schema]]) catch literal patterns: banned words, required swaps, anti-patterns, POV defaults. They miss rhythm: the cadence of sentence lengths, the ratio of single-sentence paragraphs to longer ones, the punctuation signature, the modulation of energy across a section. A draft can pass every word-level rule and still feel wrong because the rhythm is off.

Voice profile loaded with reference pieces in `foundation/reference-pieces/` covers this: the profile gives the rules, the reference pieces show real cadence. This file is the connective tissue, the lens Claude uses to see rhythm in both.

## 1. Sentence length variation

Real voice mixes short punchy sentences with medium explanatory ones. A draft that runs all-medium reads as a research summary; all-short reads as Twitter; the actual voice lives in the variation.

**Worked (mixed rhythm):**

> "Most creators don't have a content problem. They have a memory problem. They forgot what they actually know, so they ask AI for ideas, and AI gives them the same beige list it gave everyone else."

Why this lands: short opener (7 words), short follow-up (6 words), then a longer compound sentence (28 words) that earns its length by carrying the consequence. The reader's ear gets two beats of setup before the explanation arrives.

**Near-miss (uniform medium):**

> "The problem most creators face is that they have forgotten what they actually know. This causes them to turn to AI for ideas. The result is generic content that reads like everyone else's."

Why this misses: three sentences, all 14-19 words, no variation. Rhythm is flat. Even though the content is the same, the line reads as informational instead of voiced.

**Worked (short-short-long, snap back):**

> "I tried it. It worked. The next time a client asked me how I built the system in 90 minutes instead of three weeks, I didn't have a tidy answer. I had a tested one. Easy."

Short. Short. Long with substance. Snap back short. The pattern signals confidence.

## 2. Paragraph structure ratio

Most creator voices skew toward single-sentence paragraphs in long-form prose. A wall of three-sentence paragraphs reads as essay; a wall of single-sentence paragraphs reads as Twitter. The ratio depends on context (newsletter vs. script vs. LinkedIn). Read off [[voice-profile-schema]] Layer 2 context maps.

**Worked (newsletter context, 70/30 single/multi):**

> Most creators ask the wrong question.
>
> They ask "what should I post next?" when the better question is "what do I already know that nobody else knows?"
>
> The first question optimizes for output. The second one optimizes for ownership. Output without ownership is treadmill. Ownership without output is potential.
>
> Pick ownership.

Why this lands: opening is one beat. Second paragraph is one tight setup. Third is the only multi-sentence block, and it earns the weight because it carries the contrast that the whole piece pivots on. Closing is one beat for the punch.

**Near-miss (uniform multi-sentence):**

> Most creators ask the wrong question. They ask "what should I post next?" when the better question is "what do I already know that nobody else knows?" The first question optimizes for output. The second one optimizes for ownership.
>
> Output without ownership is a treadmill. Ownership without output is wasted potential. So the question becomes: how do you build ownership? You start by listing what you know.

Why this misses: every paragraph is the same shape. Reader's eye finds no rhythm to lock onto. Same content, lower retention.

## 3. Opener pattern

What does the creator naturally do in the first line? Question? Declaration? Anecdote? Data-first? Contrarian? Most creators have a dominant default. Match it.

**Worked (declaration opener, for a creator whose voice profile says 70% declaration):**

> "Most YouTube channels die at 1,000 subscribers because the creator started solving a different problem than the one they validated."

Specific, declarative, sets up the whole piece in one beat.

**Near-miss (question opener for the same creator):**

> "Have you ever wondered why most YouTube channels die at 1,000 subscribers?"

Why this misses: question openers can work, but if the creator's own pieces are 70% declaration, leading with a question reads as off-creator on a feel level even though it's grammatically fine. The voice-profile pattern isn't a rule. It's a fingerprint. Match it unless there's a reason to break it.

**Worked (anecdote opener for a story-heavy creator):**

> "A client paid me $4,500 last month for a system she could have built herself in a weekend. She knows that. I told her. She paid anyway."

Drops in mid-action, no setup, full attention.

## 4. Punctuation signature

Punctuation is voice fingerprint. Em-dashes are a HARD NO across this product (vale-enforced; see [[CLAUDE]]). Use commas, periods, parens, and rare ellipses to do the work. A creator's per-1000-word counts of these are captured in voice-profile Layer 2; respect them.

**Worked (commas and parens, no em-dashes):**

> "Most coaches teach a thing they learned three years ago, dressed up in new language, sold as a new system. The work hasn't changed. The packaging has."

Why this lands: commas slow the first sentence into a rhythm, period snaps it shut, then two short period-only beats finish the thought. No em-dashes anywhere. The pattern feels readable on screen and natural out loud.

**Near-miss (em-dash overuse, banned at the brand level):**

> "Most coaches teach a thing they learned three years ago, dressed up in new language, sold as a new system, the work hasn't changed, the packaging has."

(Picture that with em-dashes between every clause. That is what we never ship. Em-dashes pile up the same beat over and over and the reader loses where the breath should be.) Periods and commas break the rhythm into actual phrases.

**Worked (parenthetical aside doing the heavy lifting):**

> "The system runs every Sunday at 6 a.m. (yes, automatically) and drops a Slack message with last week's metrics."

Why this lands: parens carry the voiced aside without breaking the sentence's spine. Em-dashes would have done the same job, but parens preserve the read-aloud rhythm without inviting the dash habit.

## 5. Word swaps the creator avoids

Per-creator rules live in [[voice-profile-schema]] under `words_avoided` and `anti_patterns`. The product also has a hard-no list at the brand level (see CLAUDE.md word-swap conventions). Common swaps creators tend to want enforced:

- ship → post
- dive in → go through, walk through, show
- leverage → use
- eats / eating (as a metaphor) → takes / consumes / burns
- unlock → open, give you, get you to
- transform → change, rebuild, swap, replace
- elevate → raise, lift, take up
- game changer → just say what changed

**Worked:** "Here's what I'd post first" instead of "Here's what I'd ship first."

**Near-miss:** "Let me dive in to how this works." (Both "let me" and "dive in" miss; rewrite as "Here's how it works" or "Walk through it with me.")

The principle: a word swap that fires in voice-profile means the creator has explicitly rejected the original. Don't override on a single piece. Don't pile alternatives. Pick the closest match and move on.

## 6. Energy modulation

Same creator, different formats, different energy floor. YouTube scripts dial up to performer mode. Email drops below baseline to direct/dry. LinkedIn matches baseline. Capture this in voice-profile Layer 2 and modulate accordingly.

**Worked (YouTube script energy):**

> "Stop. Look at your last three videos. I bet two of them are the same idea wearing different hats."

Punchy. Direct address. Short imperative beats. Reads as someone fired up at camera.

**Near-miss (same content, email energy on a YouTube script):**

> "I want to share an observation that I think might be worth considering. If you look at your last three videos, you may notice that two of them are essentially the same idea presented in different ways."

Why this fails on YouTube: pacing is too patient, too many hedges, energy floor too low. The exact same insight in a newsletter would land. There the patient pacing reads as thoughtful. On YouTube it reads as boring.

**Worked (email energy on email):**

> "I want to flag something I noticed in your last three videos. Two of them are the same idea, different hat. Worth a re-read before you publish #4."

Why this lands: same idea, calmer pacing, ends on a quiet recommendation. Reader's brain doesn't fight the energy.

## How writing skills use this file

At startup, every writing skill (`vid-intro`, `vid-segment`, `vid-ending`) loads:

1. [[voice-profile-schema]] for the rules
2. `foundation/voice-profile.md` for the creator's specific values
3. `foundation/reference-pieces/*.md` for live rhythm exemplars
4. This file, as the lens for reading both

When a draft section is finished, run [[voice-pressure-test]] before saving. The pressure test references this rhythm guidance to judge whether the cadence matches.

## What this file does NOT do

- It does not enumerate every creator's exact patterns. That's [[voice-profile-schema]] plus the creator's `voice-profile.md`.
- It does not replace the read-aloud test. If the creator reads the draft and would reword it, the rhythm is wrong even if it pattern-matches the profile.
- It does not catch literal banned words. Vale and the word-swap layer handle that.
