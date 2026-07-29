---
type: reference
scope: shared
loaded_by: [vid-ideas, vid-framing, vid-title, vid-thumbnail, vid-structure, vid-intro, vid-segment, vid-ending, vid-capture]
status: active
tags: [reference, craft, writing]
---

# Prose Craft

The floor for any line this system writes. Not voice, which is whose it sounds like and lives in [[voice-profile-schema]]. Not pacing, which is how long a beat may live and lives in [[attention-craft]]. This is whether the sentence is any good, and it applies in every skill, for every creator, whether or not a voice profile exists.

Reference material to think with, never to paste at the creator. Examples lead, principles follow. Each move pairs a near-miss with the fix so the boundary is visible.

Seven moves. Each one is here because this system produces its failure. A rule that catches nothing is a rule the model satisfies while writing beige, so nothing gets added here without a near-miss written from real output.

## 1. The plain noun exists. Use it.

When a real word for the thing exists, reaching past it is always a downgrade.

**Near-miss:** "an automated pre-output validation layer"

**Worked:** "autocorrect for AI"

The tell is a noun phrase with modifiers stacked in front of it. Count the words before the head noun. Three or more usually means the plain word was available and got avoided.

## 2. Show the cost from inside. Don't report it from outside.

A cost described from a distance is information. A cost the reader stands inside is a reason to keep going.

**Near-miss:** "The reading is the real tax."

**Worked:** "Every draft comes back looking clean, so they read all forty pages to find the one number that's wrong."

The fix is always the same shape: name what the person does, when they do it, and what it costs them the week it slips. Abstraction is what gets written when the specific isn't in hand.

## 3. The verb does the work.

A nominalization plus a weak verb is the most reliable AI tell in this system. Find the action and make it the verb.

**Near-miss:** "The dashboard provides visibility into project status."

**Worked:** "The dashboard tells you which project is late."

**Near-miss:** "This enables creators to achieve consistency."

**Worked:** "This makes them post every week."

Watch for provides, enables, allows, facilitates, ensures, delivers, achieves, drives. Each one is a real verb wearing a coat.

## 4. Sentence length varies on purpose.

Long sentences carry reasoning. Short ones land blows. A run of same-length sentences reads as a summary no matter how good the content is.

**Near-miss (uniform):**

> "The problem is that most trackers require manual updates. This means someone has to remember to move the cards. When they forget, the board no longer matches reality."

**Worked (varied):**

> "Most trackers need someone to remember. They forget. Now the board says one thing and the work says another, and the first time it's wrong, nobody trusts it again."

Same content. The second has a rhythm to lock onto. When a passage escalates, tighten as it climbs: the last consequence should hit in four or five words.

For matching a specific creator's variation rather than merely having one, see [[voice-rhythm]] section 1.

## 5. One image per unit.

Two fresh constructions in the same breath don't compound. The second steals attention from the first and both read as reaching.

**Near-miss:** "The tracker becomes a graveyard, a second job bolted onto the first, and the whole thing collapses like a house of cards."

**Worked:** "The tracker becomes a second job bolted onto the first. Nobody signed up for two."

Pick the image that lands. Say the rest straight.

## 6. Cut the clause that didn't earn its length.

**Near-miss:** "In order to make sure that the board stays accurate, what you really need to do is make the update a byproduct of the work itself."

**Worked:** "Make the update a byproduct of the work."

Twenty-five words to eight, and the eight are stronger. Standing throat-clears: *in order to, what you need to do is, the thing about X is, it's worth noting that, at the end of the day, when it comes to.*

The test runs per clause: cut it, read the sentence again. If nothing was lost, nothing was there. Shorter and better beats longer. Long is fine when every clause earns it.

This is clause-level. For a whole beat that overstays after its point already landed, see [[attention-craft]] section 1.

## 7. Name the specific thing.

The general version of a claim is always weaker than the specific one, and the specific one is available whenever the material is real.

**Near-miss:** "They lose revenue."

**Worked:** "They discount to close, and the client who paid the least emails the most."

If the specific isn't there, that is not a writing problem. The material is thin, and the honest move is a `> [!todo]`, never a vaguer sentence that hides the gap. Every skill in this system bans invention; a general sentence written to cover a missing number is invention with better manners.

## The read-aloud test outranks all seven

Every move here can pass and the line can still be wrong. Read it as if the creator were saying it to one person. If they would pause and reword it, rewrite it. This is rule 8 in [[CLAUDE]] and it is the final gate everywhere.

## When this loads

**At session start, not at the step that writes the saved artifact.** Most of what a creator ever reads from this system is conversational: the reflect-back, the question that opens a stage, the recommendation and the reason under it, the ceiling call, the confirm line. All of it is written prose, and it starts in the first message. Loading at the step that produces the file means every line before it was written without a floor.

This is a deliberate exception to the "never front-load" convention in the skill load tables. That rule exists to keep large references out of context until they are needed. This file is short and needed from message one, the same call `vid-capture` already makes for `bank-contract.md`.

The one exception: a skill with a genuinely silent setup phase loads it at the phase that generates its first line instead. `vid-ideas` Phase 1 is silent loading plus one fixed question, so it loads at Phase 2.

## Where this fires

Craft is judged at two moments, and both matter:

1. **While drafting.** The moves are how a line gets written, not a filter applied afterward. A draft written flat and then sharpened keeps the flat structure underneath.
2. **Before save.** Every skill's own pre-save checklist already ends on read-aloud. These seven are what to look for when a line fails that test and the reason isn't obvious.

Reference files and skill documentation are held to the same floor. A near-miss written into an examples file teaches the near-miss.

## What this file does not do

- It does not carry any creator's voice. That is [[voice-profile-schema]] and the reference pieces in `foundation/reference-pieces/`.
- It does not own beat length, pattern interrupts, or energy direction. That is [[attention-craft]].
- It does not own cross-segment tension. That is [[script-tension-architecture]].
- It does not enforce banned words or em-dashes. Vale and [[CLAUDE]] handle those. They are hard rules, not craft.
- It does not replace a skill's own examples. Each skill shows how its own artifact fails. This shows how any sentence fails.
- It does not license rewriting the creator's words. A brain-dump line stays in their phrasing; these moves govern what the system writes, not what the creator said.
