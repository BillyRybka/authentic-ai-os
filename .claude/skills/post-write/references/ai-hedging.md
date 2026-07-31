---
type: reference
scope: shared
loaded_by: [post-write]
status: active
tags: [reference, voice, anti-slop, hedging]
---

# AI Hedging

The shared reference for spotting and killing hedging, one of the loudest AI tells. Any writing or voice skill can load this. The point is precision: hedging is a behavior, not a word list, and a naive ban on words like "I think" or "kind of" punishes legitimate conversational voice. This doc draws the line.

## What hedging actually is

Hedging is refusing to commit to a position so the writing cannot be wrong. The move is risk avoidance. The writer declines to plant a flag, so no reader can catch them out. It shows up as five underlying behaviors:

- **Dodging the stance.** The piece raises a question and never answers it. It describes the territory instead of taking a side.
- **Blurring the claim.** A statement gets wrapped in enough qualifiers that it no longer asserts anything falsifiable.
- **Fake balance.** Both sides get equal weight as a reflex, not because the writer actually weighed them. "There are pros and cons" used to avoid choosing.
- **Over-qualification.** So many "in some cases / depending on / it varies" clauses that the reader cannot extract an actionable claim.
- **Vague generality.** Retreating to a statement so broad it is unfalsifiable and useless ("it depends on your situation").

The defining trait: you cannot disagree with it, because it never said anything. That is the tell, not any specific word.

## The principle that separates hedging from voice

> Hedging removes the claim. Conversational softening keeps the claim and only changes its tone. Ask: after the soft words, is there still a clear position a reader could disagree with? If yes, it is voice. If the softening dissolved the position, it is a hedge.

"I think about it like this: charge for outcomes, not hours" is committed (clear position, casual frame). "I think it sort of depends on what works for you" is a hedge (no position survives). Same opening words, opposite move.

## Detection checklist

Examples are in a freelance / consulting voice. Each pattern has a genuine hedge (BAD) and a committed near-twin (GOOD) using similar words or register, so the contrast is the commitment, not the vocabulary.

### Pattern 1: The position that never lands
- **BAD:** "There are a lot of ways to price your services, and it really depends on what you're comfortable with."
- **GOOD:** "There are a lot of ways to price, and most of them are wrong. Charge for the outcome, not the hour."
- Tell: BAD surveys options and exits. GOOD surveys, then picks.

### Pattern 2: Qualifier stacking
- **BAD:** "In most cases, raising your rates can often, depending on the client, lead to better results for some freelancers."
- **GOOD:** "Raise your rates 20%. You'll lose your worst two clients and net more from the rest."
- Tell: Count the qualifiers gating the claim. Three or more on one assertion is mush.

### Pattern 3: Reflex both-sides
- **BAD:** "Niching down has its advantages and disadvantages, and going broad does too, so it's really up to you."
- **GOOD:** "Going broad feels safer and pays worse. Niche down. The narrow specialist out-earns the generalist every time."
- Tell: BAD weighs nothing and assigns the decision back to the reader. GOOD names the tradeoff and still commits.

### Pattern 4: The "I think" that softens a claim vs the one that frames it
- **BAD:** "I think a retainer might be a decent option, but I'm not totally sure it's right for everyone."
- **GOOD:** "I think about retainers like a gym membership: predictable income, and the client values it more because they're paying for access."
- Tell: "I think" is fine when it introduces a committed framing or analogy. It is a hedge when it discounts the claim that follows.

### Pattern 5: "kind of / sort of" as analogy-softener vs as escape hatch
- **BAD:** "A discovery call is kind of, I guess, sort of a way to maybe see if you're a fit."
- **GOOD:** "A discovery call is kind of like a first date. You're both deciding if there's a second one."
- Tell: "kind of like" introducing a deliberate analogy is committed register. "kind of, I guess" wrapped around the core claim is a dodge.

### Pattern 6: Vague generality as the takeaway
- **BAD:** "At the end of the day, success as a consultant comes down to finding what works for you and staying consistent."
- **GOOD:** "Success as a consultant comes down to one thing: say no to the wrong clients fast enough that you have room for the right ones."
- Tell: BAD is unfalsifiable and applies to anyone. GOOD makes a specific, disagreeable claim.

### Pattern 7: The disclaimer that retracts the advice
- **BAD:** "Fire the client. But of course, every situation is different and you know your business better than I do."
- **GOOD:** "Fire the client. If the relationship costs you sleep, the revenue isn't worth it. You already know which one this is."
- Tell: A trailing "but everyone's different / your mileage may vary" that cancels the advice just given. Acknowledging context that sharpens the advice is fine.

### Pattern 8: Burying the answer in process
- **BAD:** "Whether you should incorporate depends on a range of factors worth carefully considering with a professional."
- **GOOD:** "Incorporate once you clear about 40k in profit. Below that the paperwork costs more than it saves. Above it, the tax math flips."
- Tell: BAD defers to "factors" and an unnamed professional. GOOD gives the threshold and the reasoning.

### Pattern 9: Hypothetical hiding vs honest conditional
- **BAD:** "You could potentially consider possibly testing a higher price point at some point."
- **GOOD:** "If your close rate is above 80%, you're priced too low. Raise it until you're losing one in four deals."
- Tell: Stacked modals ("could potentially consider possibly") signal nobody is home. A real conditional ("if X, then do Y") is a committed, testable instruction.

### Pattern 10: "Tends to" as observed pattern vs as cowardice
- **BAD:** "Cheaper clients tend to maybe be a bit more demanding sometimes, generally speaking."
- **GOOD:** "Cheaper clients tend to be the most demanding. The less someone pays, the more they expect. That is not a rule, but it is close."
- Tell: "tends to" stating a real observed pattern is committed. "tends to maybe sometimes generally" hedging the same observation into nothing is not.

## Rubric criterion: commitment / no hedging (0 to 5)

> Score how willing the writing is to take and hold a position. Look for claims a reader could actually disagree with: stated stances, specific thresholds, named tradeoffs, clear instructions. Penalize the underlying move of non-commitment, not the presence of any word. Penalize: positions raised and never answered, claims buried under three or more qualifiers, reflex both-sides balance that hands the decision back to the reader, trailing disclaimers that retract the advice just given, and vague unfalsifiable takeaways ("find what works for you"). Do NOT penalize committed conversational voice: "I think" or "I think about it like this" introducing a clear position or framing; "kind of like / sort of like" used as a deliberate analogy softener; "tends to" stating a genuinely observed pattern; casual register inside an otherwise committed sentence; or a single honest conditional ("if X, do Y"). The test for each soft phrase: strip the softener and check if a clear, disagreeable claim remains. If it does, that is voice, score it up. If the claim dissolves, that is a hedge, score it down. 5 = takes clear positions throughout, soft language only adds tone or framing. 3 = mostly committed but one or two real hedges blur a key claim. 0 = the piece never plants a flag a reader could argue with.

## How skills use this

- A writing skill loads this during its anti-slop or voice pass and runs the strip-the-softener test on any soft phrase before deciding it is a hedge.
- The rubric criterion above drops straight into an eval or a pressure-test as the "commitment" score.
- Pairs with [[voice-pressure-test]] (the read-aloud test) and any skill's anti-slop reference.
