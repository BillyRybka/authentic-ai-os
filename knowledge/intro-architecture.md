---
type: reference
doc: intro-architecture
project: authentic-ai-os
status: active
last_refreshed: 2026-05-02
tags: [reference, intro, hook, scripting, packaging]
---

# Intro Architecture

The universal 6-part architecture every video intro draws from. Loaded by `vid-intro` and any other writing skill that needs to produce or evaluate an intro. Format planners (`knowledge/format-planners/{format}.md`) specify HOW each format adapts this template: which parts apply, which trim out, which expand.

This is reference material for Claude. Do not paste it into chat. Use it to think with.

## Top-line numbers

- **Hook:** under 5 seconds
- **Whole intro:** under 30 seconds, 15 seconds is ideal
- **Setup:** maximum 3 things teased
- **Top 3 viewer questions:** 3 (the basis for the Setup)

## The 6-step architecture

The full intro contains 6 elements. Steps 1-5 are produced in order. Step 6 (credibility line) gets woven into the Hook, the Problem/Result, or the Setup (steps 2-4), matching the diagram below.

```
1. TOP 3 VIEWER QUESTIONS (derived from thumbnail + title, drives Setup)
   ↓
2. HOOK (one of 5 types, under 5 seconds)
   ↓
3. PROBLEM / RESULT (one of 3 options, poke / tease / combine)
   ↓
4. SETUP (max 3 things, answers the Top 3 viewer questions)
   ↓
5. TRANSITION (hook forward + orientation cue → first point)
   ↓
+  CREDIBILITY LINE (woven into Hook, Problem/Result, or Setup, never bolted on)
+  VISUAL PROOF (any time a claim is made in the intro)
```

### Step 1: Top 3 viewer questions

Before writing the intro, identify the top 3 questions a viewer would have answered in this video, derived from the locked title plus thumbnail combination.

**How to derive them:**
- Read the title and the locked thumbnail text together (piece.md `title` + `thumbnail_text`)
- Imagine the cold viewer just clicked
- What does the viewer most want to know in the next 30 seconds?
- The 3 questions feed directly into the Setup (step 4)

**Quick method:** drop the thumbnail plus title into a generative-AI prompt and ask "what are the top three questions someone would want answered if they click this?" Use the answers as a draft, then refine.

**Example (thumbnail-text "MAKE BORING THUMBNAILS" plus a related title):**
1. What's the trick?
2. Why should I make boring thumbnails?
3. How will this help my business?

These three questions become the three things the Setup promises.

### Step 2: Hook (5 types)

The first line. Under 5 seconds. Three jobs:
1. Instantly grab attention
2. Create curiosity
3. Signal clear value or relevance

Pick ONE of the 5 hook types based on the video's content and the creator's voice. Different videos warrant different types.

**Type 1: Question Hook**
Ask the viewers a question they've always wanted the answer to.

> "Have you ever wondered why one of your videos gets a load of views and then the next one doesn't do as well?"

When to use: when the avatar's pain point can be stated as a direct question.

**Type 2: Contrarian Hook**
Go against the grain of common advice. Pairs naturally with cognitive-dissonance thumbnails.

> "I'M A MULTI-MILLIONAIRE AND I DON'T OWN MY HOUSE and I don't invest in any property."

When to use: when the video's central insight contradicts conventional wisdom in the niche.

**Type 3: Statement Hook**
Blast a strong, bold opinion.

> "The second your video loads, people judge you, and if they don't like what they see, they're gonna leave and you're never gonna generate views and sales."

When to use: when the video makes a definitive claim and the creator can defend it. High-conviction tone.

**Type 4: Fact Hook**
Open with a surprising fact. Two hard rules:
1. The fact MUST be surprising. Boring facts are dead.
2. The fact MUST be relevant to the video. ("Did you know duck quacks don't echo? So in this video I'm going to teach you how to hit a home run." REJECT, no relevance.)

> "American millennials spend more than three and a half hours on their phone every day."

When to use: when there's a real, surprising data point in the niche that primes the video's topic.

**Type 5: Credibility Hook**
Lead with a massive result.

> "I've been in business for 13 years, I've sold 9 companies. My last company I sold for 46.2 million."

When to use: when the creator's credibility is loud enough to stop cold viewers in their tracks. The default pattern: **small or new channels usually under-perform with this hook** because cold viewers don't trust an unknown "I" yet. They'd rather see what the value is than hear about the creator. If `foundation/credibility.md` shows a small channel, the skill should flag this hook as risky and propose one of the other 4 as the safer default. The creator can choose to use it anyway. Sometimes a single dramatic result IS the value, even on a small channel. Their call, not the skill's.

### Step 3: Problem / Result (3 options)

After the hook, give the viewer a reason to care about the rest of the video. Choose ONE of 3 options.

**Option 1: Poke the Problem**
Describe the problem the avatar is living. Make them feel seen.

> "Do you hate making thumbnails? Every YouTuber I know does. The thing is, they're the most important part of your video, because if you can't get a click, nobody watches and you won't generate any sales. And all that time you spent writing, filming, editing is wasted."

The pivot phrase is "The thing is...", which introduces the cost of the problem.

When to use: when the avatar's pain is acute and the video's value is removing the pain.

**Option 2: Tease the Result**
Describe the outcome the viewer wants. Make them feel hope.

> "Do you hate making thumbnails? I used to until I figured out a simple thumbnail formula that generated millions of views and $6 million from YouTube in just two years."

When to use: when the video delivers a transformation and the receipt is impressive enough to drive belief.

**Option 3: Combine Both**
Poke the problem first, then tease the result.

> "Do you hate making thumbnails? Every YouTuber I know does, because they take so flipping long. The thing is, they're the most important part of your video. If you don't get a click, nobody watches or enters your sales funnel, so all that time you put in goes to waste. But there's a special formula for thumbnails that's fast and easy to produce, and it's blowing up channels right now."

The pivot is "But..." which signals the resolution after the problem is established.

When to use: when both sides matter. The problem is high-emotion AND the result is impressive. Most powerful option, longest.

**The problem you're poking should be a real problem the avatar actually has.** Usually that's one of the Top 3 from `foundation/avatar.md`, but a fresh angle on a related problem the avatar genuinely feels works too. The test is resonance, not a checklist match. The video's problem was already chosen at framing, so you're poking THAT, not re-picking from the list. If the intro pokes a problem the avatar doesn't actually have, the viewer feels disconnected and leaves.

### Step 4: Setup (max 3 things)

The Setup tells viewers exactly what they're going to get in the video. The structure is:

> "So in this video, I'm going to show you [Q1], [Q2], [Q3]."

Where Q1-Q3 are the Top 3 viewer questions from Step 1. Maximum 3. If the format suggests fewer, fewer is fine. More than 3 equals overwhelming.

**Example (continuing the boring-thumbnails video):**

Top 3 viewer questions:
1. What's the trick?
2. Why should I make boring thumbnails?
3. How will this help my business?

Setup that ticks them off:

> "So in this video, I'm going to show you what this simple formula is, why it's critical you make boring thumbnails for it to work, and how to use it to make your sales explode."

Color-coded mentally: each clause maps to one viewer question.

### Step 5: Transition (the cement)

A transition connects the intro to the first point of the video. Without it, the first point feels like waffle. The viewer doesn't know why they need to listen.

A transition does two things simultaneously:
1. **Hook forward**: tease the value ahead. Frame the next section as the solution to the problem this video addresses.
2. **Orientation cue**: signal that the intro is over and the content has started.

**Example:**

> "Okay, so step one is critical if you want to bring viewers back and turn them into buyers, and it works like this."

That single sentence signals movement (orientation cue) AND positions step one as solving a problem the viewer cares about (hook forward).

**Banned transition phrases (AI tells):**

| Banned | Why | Use instead |
|---|---|---|
| "Let's dive in" | AI default closer, meaningless | "All right, so let me show you..." |
| "Let's talk about..." | "Talk about" is passive. Viewers don't watch to be talked to | Replace with "show you" or "walk you through" |
| "Let me tell you..." | Signals a list of boring information | "Here's what's actually happening..." |
| "Without further ado..." | Filler phrase | Just transition |
| "Now, before we begin..." | The intro is over by definition, this re-opens it | Just transition |

The verb to default to is **"show"**. Viewers come to YouTube to be shown, not told.

### Step 6: Credibility line (woven, not bolted)

Cold viewers distrust unknown creators. At some point in the intro, signal that the creator knows what they're talking about. **Weave it into the Hook, Problem/Result, or Setup. Never as a separate self-introduction.**

**5 ways to signal credibility:**
1. **Vast experience:** "After making 500 cakes over three years, here's what finally made them moist."
2. **Volume of people helped:** "We've used this on over 40 people and it's worked every time."
3. **Big personal result:** "Fixing this made me $90,000."
4. **Big client result:** "My last client went from 80 hours a week to 15 in 90 days."
5. **Effort signal:** "I analyzed 500 resumes, and this is what got people employed."

**Example of weaving (sits inside the Problem/Result section):**

> "This video is one of the fastest and easiest videos I've ever made [hook], and one of the best performing for sales. And the framework I used to make it didn't just work once. It blew up sales multiple times from multiple videos AND got hundreds of emails too [problem/result + credibility woven in]. So now I'm going to give you every step to make your own so you can just copy it [setup]."

The "blew up sales multiple times AND got hundreds of emails too" reads as proof of the claim, not as a CV bullet. That's the move.

**The bolted-on failure mode:**

> "Hi, I'm Bob. I've been doing this for 10 years and have helped 200 people. Today we're going to talk about..."

Cold viewers don't care about Bob yet. The credit goes in the moment Bob makes a claim. Not before.

### + Visual proof (whenever a claim is made)

Any time a claim is made in the intro, show visual proof immediately:
- Screenshots of the result
- Testimonials on screen
- Stripe revenue dashboard
- Analytics graph
- Before/after comparison

A claim with no visual proof creates doubt. A claim with visual proof creates trust. This is a production note for the editor, but the script should call out where visuals are required.

## Visual matching rule (the production-quality match)

The first SHOT of the video must match the visual expectations the thumbnail set. Otherwise the viewer leaves before the hook lands.

| Thumbnail style | First shot expectation |
|---|---|
| Cinematic / polished | Cinematic / polished open. Camera, lighting, framing all match. |
| Scrappy / DIY / no-frills | Scrappy / DIY open. Whiteboard, casual setup, real lighting. |
| Studio plus face | Same studio plus face in the open |
| Outdoor / location | Same location in the open |

**Rule:** if the thumbnail is cinematic and the first shot is webcam, the viewer feels lied to and leaves. If the thumbnail is webcam and the first shot is cinematic, the viewer feels confused. Wrong channel.

This is a constraint the writing skills surface, the creator/editor enforces.

## Length and pacing

- **Hook:** under 5 seconds
- **Whole intro:** under 30 seconds maximum, 15 seconds ideal
- **Setup:** 1 sentence per question, 3 max. Not paragraphs
- **Transition:** 1-2 sentences

If the intro runs over 30 seconds, the creator is teaching in the intro instead of hooking. **The intro is for hooking, not educating.** Move teaching content into the body.

## Format-specific adaptation

This is the universal architecture. Each format trims, expands, or reorders it to fit its own audience expectations, and those per-format changes live in exactly one place: `knowledge/format-planners/{format}.md` (each planner owns an "Intro adaptation" section). `vid-intro` loads the matching planner before assembling the intro. No per-format rules live in this file.

## How vid-intro uses this file

When `vid-intro` runs, it should:

1. Load this file silently (Claude-internal reference)
2. Load the matching format planner from `knowledge/format-planners/{format}.md` for adaptation rules
3. Load `foundation/voice-profile.md` for creator-specific preferences (which hook types they default to, transitions they avoid, energy level)
4. Load the locked title and `thumbnail_text` from piece.md to derive the Top 3 viewer questions
5. Generate options at each step:
   - Top 3 questions: usually 1 set, surface for creator approval
   - Hook: 2-3 candidates across allowed hook types (filtered by format, voice, credibility-match check)
   - Problem/Result: 2-3 candidates across the 3 options
   - Setup: 1 draft using the Top 3 questions in the standard template
   - Transition: 1-2 candidates with no banned phrases
   - Credibility line: identify which of Hook/Problem-Result/Setup gets it, and which of the 5 credibility forms applies
6. Creator picks at each step
7. Assemble the full intro
8. Save to `content/pieces/{slug}/script.md` (the intro section) OR return to caller (vid-pipeline) when invoked as sub-skill

Same Q-script discipline as `vid-title` and `vid-thumbnail`: short messages, ask-and-wait, no reference dumping, push back on weak options, anti-fabrication enforced (every claim must trace to script or foundation).

## Anti-patterns and friction points

These are patterns that under-perform. The skill should flag them and explain why. Not auto-reject. The creator can override if they have reason to.

**Hard friction (almost always wrong):**
- Vague claims without visual proof. Viewers don't trust unverifiable claims
- Bolted-on self-introduction ("Hi, I'm X. I've been doing this for Y years..."). Cold viewers tune out
- Setup that doesn't answer any of the Top 3 viewer questions. The intro is misaligned with the title/thumbnail promise
- Banned transition phrases (table above). These read as AI defaults to viewers

**Soft friction (often suboptimal, creator may have reason):**
- Credibility Hook on small/new channels. Usually fails the cold-trust test, a single dramatic result can earn it
- Setup with more than 3 things. Usually overwhelms, a complex methodology may need it
- Hook longer than 5 seconds. Usually wastes attention, a story-driven open can run longer if it earns the time
- Whole intro over 30 seconds. Usually means teaching crept in, some formats (Deep Dive) earn longer setup
- Teaching content inside the intro. Usually a hook-killer, contextual setup that LOOKS like teaching can land
- Problem-poking that doesn't match one of the avatar's Top 3 problems. Usually misses the audience, a fresh angle on a related problem can work

The pattern: present the friction as a flag, explain WHY it tends to fail, let the creator decide. Defaults exist because they pattern-match what works most often. They aren't laws. Locking everything as "REJECT" stifles creativity and produces formulaic output.

## The single most important principle

**The intro is for HOOKING, not EDUCATING.** If the intro starts teaching the lesson before the Setup, the viewer's brain switches to evaluation-mode instead of curiosity-mode, and most leave. Curiosity is the fuel for the rest of the video. Don't burn it in the intro.
