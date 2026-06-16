---
type: bank
project: authentic-ai-os
kind: patterns
status: active
tags: [bank, hooks, patterns]
---

# Hook Bank

Fill-in-the-blank hook patterns plus worked examples. Used by `vid-intro` at runtime to seed candidate hooks for the 5-second opener (step 2 of the 6-part architecture in [[intro-architecture]]). Patterns are templates with `[X]` `[Y]` `[Z]` slots.

The 5 canonical hook types are defined in [[intro-architecture]]: Question, Contrarian, Statement, Fact, Credibility. Patterns below are organized by type. A creator's `voice-profile.md` field `preferred_hook_types` filters which types `vid-intro` weights heavier.

> **This is a starter you grow.** creator-setup scaffolds this file into your `banks/`. It is yours from here. Delete patterns you would never say, rewrite the worked examples in your own voice and niche, and add new patterns as you find hooks that land. The skill reads whatever is in your vault, not the plugin default. The examples below are generic on purpose. Replace them with your own.

This is reference material for Claude to think with, not paste at the creator. `vid-intro` reads it silently, picks 2-3 candidate patterns, fills the slots from the video's brain dump, and surfaces options.

---

## Type 1. Question Hook

A question the avatar has asked themselves. Pulls them in by promising the answer. The question must be one the avatar genuinely wonders. Generic curiosity questions miss.

### Patterns

**Q-1.** Have you ever wondered why [X] [happens / doesn't work]?
- Worked: "Have you ever wondered why one piece of content takes off and the next one flops?" Lands because it names a pain the avatar feels often.
- Near-miss: "Have you ever wondered why people are the way they are?" Too broad. Reads as a philosophical opener, not a promise of an answer.

**Q-2.** Are you making this [X] mistake [right now / every day]?
- Worked: "Are you making this pricing mistake right now?" Tight, usefully accusatory, opens a loop.
- Near-miss: "Are you making mistakes in your business?" Generic. No specificity.

**Q-3.** Do you ever feel like [X] no matter how hard you [Y]?
- Worked: "Do you ever feel stuck no matter how much you publish?" Names a specific pain plus a specific futile action.
- Near-miss: "Do you ever feel like things don't go your way?" Too vague to grip a specific avatar.

**Q-4.** What would you do if [improbable scenario]?
- Worked: "What would you do if your biggest client emailed tomorrow to cancel?" Concrete enough to make the viewer simulate an answer.
- Near-miss: "What would you do if you could do anything?" Floats. No tension.

**Q-5.** Why is [X] doing [Y]?
- Worked: "Why is everyone in [niche] suddenly switching to [thing]?" Names a real shift the viewer half-noticed.
- Near-miss: "Why is [platform] the way it is?" Too abstract; reads as a rant opener.

**Q-6.** Why is nobody talking about [X]?
- Worked: "Why is nobody talking about the fact that [real, specific stat]?" Implies a hidden truth. Lands when the stat is real.
- Near-miss: "Why is nobody talking about the truth?" Conspiracy-flavored without specifics.

**Q-7.** Do you struggle to [X]? Well, it's not your fault.
- Worked: "Do you struggle to keep clients past six months? It's not your fault." Validating; opens permission to listen.
- Near-miss: "Do you struggle? It's not your fault." The pain has to be named.

**Q-8.** Can I tell you a secret?
- Worked: "Can I tell you a secret? [Specific result] came from one thing you have never heard of." Pulls the viewer into a confession frame.
- Near-miss: "Can I tell you a secret about success?" The secret needs a specific noun on the other side, not a category.

---

## Type 2. Contrarian Hook

Goes against the grain of common advice. Pairs naturally with cognitive-dissonance thumbnails. The contrarian claim must be one you can defend in the body. Pure contrarianism without substance burns the hook.

### Patterns

**C-1.** I'm a [credible role] and I don't [common practice everyone in that role does].
- Worked: "I'm a [role] and I never [the thing everyone in that role swears by]." Lands when the body proves it.
- Near-miss: "I'm a [role] and I do things differently." No specific claim to grip.

**C-2.** Stop doing [common action everyone recommends] right now.
**C-3.** [Widely accepted idea] is completely wrong.
**C-4.** You don't need [common tool / advice everyone pushes] to [outcome].
**C-5.** Why [popular thing in the niche] is holding you back.
**C-6.** Here's why [popular opinion] is wrong.
**C-7.** Everyone says [X]. They're wrong, and here's why.

- Worked (C-4): "You don't need [expensive tool everyone pushes] to [outcome]." Lands when you then show the cheaper path that works.
- Near-miss (any): a contrarian claim you cannot back up in the body. The hook writes a check the script cannot cash.

---

## Type 3. Statement Hook

A flat, confident claim that opens a loop. Works when the statement is specific and the body delivers.

### Patterns

**S-1.** I have found the [X] that nobody seems to be talking about.
**S-2.** The second your [thing] loads, [bad thing happens] and [worse outcome].
**S-3.** This one [thing] transformed my entire approach to [topic].
**S-4.** You've been doing [X] wrong all along.
**S-5.** [Outcome] doesn't come from luck. It comes from [specific thing].
**S-6.** It's time to rethink everything you know about [subject].
**S-7.** Here's a truth no one wants to admit about [X].
**S-8.** [Specific tweak] can dramatically improve your [skill / outcome].

- Worked (S-5): "[Outcome] doesn't come from luck. It comes from [the specific lever you teach]." Lands because it promises a controllable cause.
- Near-miss: "This will change your life." No specific noun, no loop. Empty.

---

## Type 4. Fact Hook

Opens on a real, surprising number or finding. The fact must be true and must connect to the video's payoff.

### Patterns

**F-1.** On average, [audience group] [does surprising thing] [unexpected frequency / number].
**F-2.** Almost [percentage] of [group] [counterintuitive trait or action].
**F-3.** Did you know that [most people] [are most likely to / least likely to] [X] on [specific time / day]?
**F-4.** Studies show that [counterintuitive finding].
**F-5.** [Percentage] of [group] are [common mistake] right now without realizing it.
**F-6.** Most [audience group] don't realize this about [X].
**F-7.** Here's a number that will change how you think about [topic]: [X].

- Worked (F-2): "Almost [real percentage] of [group] [do the counterintuitive thing]." Lands when the number is real and the video explains it.
- Near-miss: a surprising-but-irrelevant fact that the body never pays off. Curiosity spent, no return.

---

## Type 5. Credibility Hook

Opens on earned authority. Only works when the credibility is real; a borrowed or vague claim reads as bragging.

### Patterns

**Cr-1.** I've been [doing thing] for [significant time] and [scale of result / accomplishment].
**Cr-2.** After [doing X] [number] times, here's what I learned.
**Cr-3.** We've [done thing] on [number] [people / cases] and [result happened] every time.
**Cr-4.** [Specific personal action] made me $[number] in [timeframe].
**Cr-5.** My last client went from [X] to [Y] in [timeframe].
**Cr-6.** I [analyzed / studied] [number] [things] and here's the pattern.

- Worked (Cr-5): "My last client went from [real before] to [real after] in [real timeframe]." Lands because it is specific and verifiable.
- Near-miss: "I'm kind of an expert at this." Vague authority reads as a hedge, not credibility.

---

## Anti-patterns (every type)

- **A-1. Bolted-on self-introduction.** "Hey guys, welcome back to my channel." Burns the 5-second window on nothing.
- **A-2. Generic curiosity bait.** "You won't believe what happened next." No specific promise.
- **A-3. Empty promise.** A hook the body never pays off.
- **A-4. Surprising-but-irrelevant fact.** A number that has nothing to do with the payoff.
- **A-5. Hedge in the hook.** "This might help you maybe improve a little." Confidence is the hook.
- **A-6. Topic-label dressed as hook.** "Today's video is about email marketing." A label, not a hook.
- **A-7. Multi-hook stacking.** Three hooks in a row. Pick one and commit.

---

## How vid-intro uses this file

1. Reads the locked hook type lane (from `references/hook-type-selection-flow.md` + the video's framing).
2. Pulls 2-3 candidate patterns from that type.
3. Fills the slots from the brain dump's real material (numbers, named methods, specific moments). NO fabrication. If a slot cannot be filled from the lock list, skip that pattern.
4. Surfaces the filled candidates to the creator. The creator picks or pushes back.
