---
type: reference
scope: skill-local
loaded_by: [post-write]
status: active
tags: [reference, post-write, anti-slop, hooks, editorial]
---

# Anti-Slop

The quality bar. Every post passes this before it is shown to the creator. Slop is the reason most AI content gets ignored, and the audience can feel it. When a reader senses no human is really in the writing, trust cracks. This file is how you keep the human in.

These are the universal tells. The creator's `voice-profile.md` adds their own refusals and avoided words on top. Honor both. When they conflict, the creator's profile wins.

## What slop actually is

Slop is writing that says almost nothing and hides it behind polish. It is vague where it should be specific. It hedges instead of committing. It reaches for impressive words instead of true ones. It restates the same point three ways and calls it depth. It could have been written by anyone about anything, which is why it builds no trust. Clean is not the same as credible. A post can be grammatically perfect and still be slop.

The fix is almost always the same: more specific, more committed, more grounded in something real.

## The tells to strip

Run the draft against this list and cut every hit.

- **Em-dashes. Never.** Not in the post, not in these files. Replace with a period, a comma, parentheses, or a line break. This is a hard rule, the single most common AI tell. If a sentence reads worse without one, the sentence is wrong, rewrite it.
- **Hedging.** Not a word list. Hedging is non-commitment: a claim blurred by qualifiers, a position raised and never answered, reflex both-sides, a takeaway so vague it cannot be wrong. The test: strip the soft phrase and check if a disagreeable claim remains. If it does, it is voice ("I think about it like this:" framing a clear position is fine). If the claim dissolves, it is a hedge. Full definition and the 10-pattern checklist are in `knowledge/ai-hedging.md`. Run that test before you cut any soft phrase.
- **Corporate and marketing filler.** Swap for plain words: "unlock," "leverage," "elevate," "amplify," "supercharge," "game-changer," "dive in," "in today's world," "harness the power," "take it to the next level," "robust," "seamless," "foster," "empower." If you would not say it to one person across a table, cut it.
- **Phrasal hyphens.** "Cry it out," not "cry-it-out." "Try it out," not "try-it-out." If you would pause between the words when speaking, drop the hyphen. Genuine compound modifiers ("check-in," "follow-up") are fine.
- **Vague claims with no anchor.** Every claim needs a number, a name, an example, or a specific moment. "Training consistency matters" is nothing. "The client who trained 25 minutes twice a week beat his old 5-day self" is a claim.
- **Invented numbers.** Never introduce a number the creator's source did not give: no invented percentage, dollar amount, year, count, or multiplier, not even in a CTA or a throwaway illustration. This is the most common fabrication leak. The proof gets correctly left as a TODO, then a "raise it 30%" or an "if you wrote it in 2022" sneaks into a closing line. This includes round hypotheticals and spelled-out figures: "onboarding should not take ten hours per client" invents "ten hours" even though it reads as a generality, and spelling it out does not make it real. If the source did not give the figure, make the point without it ("onboarding should not eat your whole week"), cut the number, or mark it a TODO. Specificity has to be real, not manufactured.
- **Constructed warm-up openers.** No "Here is what I keep thinking about," "Here is the thing," "Let me tell you something," "Here is what happens." Open on the actual line. The warm-up is throat-clearing the creator would cut reading it aloud.
- **Subject-facing flat openings.** The first line introduces a character, a topic, or a scene instead of facing the reader. "Marcus ran a content agency." "Today I want to talk about pricing." That is information, not a hook. Nothing is at stake for the reader, so they scroll. Open on the reader's belief, pain, or a gap they need closed, then bring the subject in as proof. This is the most common reason a finished post reads flat. Full standard in `references/hooks.md`.
- **Listicle with no substance.** "Here are 7 things about training" where each thing is a platitude. Fewer points, each one real, beats a long list of air.
- **Circling.** Saying the same point three times in slightly different words to fill space. Make the point once, sharp, move on.
- **Fake balance.** "There are pros and cons to both" that commits to nothing. Take the side the idea is actually on.
- **Generic CTAs.** "Let me know your thoughts," "what do you think," "drop a comment below" tacked on by reflex. A CTA is earned and specific, or it is absent. "What would you cut if you only had 25 minutes to train" beats "thoughts?"
- **Repeated openers across a batch.** The "Most people..." trap. One or two posts opening the same way is fine. A batch where every post opens the same way reads as a machine, even when each post is fine alone. This is the loudest batch-level tell. Vary the hook (see below).

## The hook rotation library

Variety is one half of the hook. Strength is the other, and it comes first: a varied set of weak openers is still a set of weak openers. Get the first line to face the reader and open a gap (`references/hooks.md`), then use this library to keep the batch from repeating itself.

A batch needs varied openings. Track which hook types you have used as you go. Do not let any single hook type appear more than twice across a batch. These are the nine, each with an illustrative opener in the strength-coach niche (they teach the move, not the topic).

- **Contrarian** (name the wrong belief, replace it): "Cardio is the worst use of a busy founder's 30 minutes."
- **Observation** (a pattern you keep seeing): "The founders who stay lean are not the ones with more time. They skip fewer sessions."
- **Story** (open mid-moment): "My most consistent client trains 25 minutes, twice a week. He used to train five days and quit every quarter."
- **Diagnostic** (a symptom points to a cause): "If your training falls apart the week a launch hits, the problem is not discipline. It is program length."
- **Rule** (one sharp operating principle): "Never add a training day to fix inconsistency."
- **Tension** (two true things that pull against each other): "The shorter I made his program, the faster he progressed."
- **Direct command** (tell them to stop or start): "Stop training for a photo you are not taking."
- **Comparison** (two things, sharp line between): "A 90-minute session is a hobby. A 25-minute session is a system."
- **Question** (a real one that opens a gap): "What would you cut if you only had 25 minutes to train?"

The hook serves the idea. Do not bolt a contrarian opener onto an idea that is really a story. Pick the hook that fits the unit, then check it against what the batch has already used. If the natural hook is taken twice already, find the second-best fit.

## The editorial pass (run on every post before showing it)

A yes to all of these, or fix it:

1. **One clear idea.** If you can name two points, split or cut.
2. **Specific, not generic.** At least one number, name, or concrete example the reader could not have guessed.
3. **Grounded in real material.** Every story, number, client, and example comes from the creator's source. Nothing invented to make it land.
4. **Strong, fresh hook.** The first line faces the reader and opens a gap (the hook test in `references/hooks.md`), and it is not a repeat of an opener the batch already used more than twice.
5. **No AI tells.** No em-dashes, no hedging, no corporate filler, no phrasal hyphens.
6. **Clean publishable body.** No wikilinks, no markdown internal links. It pastes straight to the platform.
7. **Read-aloud passes.** Read it out. If the creator would reword a line when speaking it, the line is wrong.
8. **Platform-native.** It fits this platform's rhythm. It is not another platform's post reflowed.
9. **CTA earned or absent.** No reflex sign-off. A specific ask, or none.

## Adaptation, not recycling

The same idea becomes a LinkedIn argument and an Instagram carousel by being rebuilt for each, not by being pasted across. Keep the idea, change the delivery. A LinkedIn post dropped into carousel slides, or a transcript relabeled as a caption, is recycling. The reader can tell. Good adaptation keeps the point and changes everything about how it arrives.
