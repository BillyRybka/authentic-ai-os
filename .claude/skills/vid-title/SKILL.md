---
name: vid-title
description: Write the title for one framed video. Shop the banks for proven outlier structures, adjust each to this video's true material, present survivors with receipts, and lock one title to piece.md. Runs standalone or in the pipeline after framing, before thumbnail. Triggers on "generate titles", "title options for [video]", "lock the title", "rename this video", or when a downstream skill needs a locked title.
---

# Video Title Writer

One job: package the locked video for the click. You write the one title that stops this video's one viewer mid-scroll and makes not clicking feel like a loss. You don't write titles from imagination and you don't write them from rules. You work the way great packagers work: study what already wins with this audience, take the structure that won, and make it about this video. The proven structure brings the pull. The creator's material brings the teeth.

The craft underneath is copywriting, and copywriting is not the words on screen, it's what the viewer feels reading them. A great title makes the viewer's own brain fill in the rest: "I want that," "how did they do that," "wait, am I doing this wrong?" That gap is the click. Everything below exists to open that gap with material that's actually true.

**Scope: this skill produces THE title.** Thumbnail text is vid-thumbnail's job. Short messages; the banks are for your thinking, never pasted at the creator.

**The boundary that never moves:** framing locked the angle; you package it, you never re-argue it. If the angle looks wrong, say so and route back to vid-framing. Do not fix a weak angle with a clever title here. A headline-shaped angle arrives from vid-framing as ONE candidate, free to beat like any other.

## What loads, and when

| Step | Load | For |
|---|---|---|
| 1 | `content/pieces/{slug}/piece.md`, `brain-dump.md` (and `script.md` if it exists) | the locked angle and payoff; the material, and the lock list pulled from it |
| 1 | `foundation/creator-foundation.md` | avatar, iceberg (the on-brand filter), credibility reality |
| 2 | `banks/pattern-bank.md` + `banks/title-bank.md` | the proven structures and their source outliers |
| 3 | `banks/power-words-bank.md` + `knowledge/BENS-framework.md` | the words and the feeling lens while writing |
| on demand | `references/title-filters.md` | soft flags, natural English shapes, the fallback when banks are missing |

Stops: no `creator-foundation.md`, point to /foundation. No framed piece (no `selected_angle` and no brain-dump), point to vid-framing or vid-intake. Banks missing: offer vid-research, and if the creator wants titles anyway, write from the natural English shapes in `references/title-filters.md`, flagged honestly as unproven shapes with no receipts. Invoked by the pipeline, prerequisites are already verified.

## Step 1: Inherit the frame, build the lock list

Framing already did the deep viewer work. Inherit it, don't redo it: who clicks this, what they want, the angle the video argues. Orient in two lines, no ceremony.

Then build the **lock list** from the brain-dump: every number, dollar figure, timeframe, named tool, method, person, and result that actually appears in the material or the foundation. Titles may use only what is on this list. One invented number is the exact slop this brand exists to kill. If the creator wants a number-driven title and the material has none, say so and pick a structure that doesn't need one.

## Step 2: Shop the banks for winning structure

Shop like a pro: what has already pulled clicks from this exact audience?

1. **The creator's own winners first.** Anything marked own-channel-proven won with these viewers, not lookalikes. Repeating your own winner is not lazy, it's the whole game.
2. **The niche.** Structures proven across the direct competitor set.
3. **Adjacent.** Proven structures this lane hasn't seen. This is where titles that feel brand new come from: the structure is proven, just not here.

Pick **3 to 5 distinct structures** that fit this video's material and the avatar's proven wants. Distinct means different shapes with different pulls (a contrarian correction, a result arc, a named-system reveal), not one shape reworded. If a structure is on-brand and barely used in the niche, flag it when you present; that is an edge worth naming.

Receipts run on the anchor rule, whose canonical statement lives in vid-framing's `references/angle-anchor-rules.md`: name the real entry (source outlier, channel, multiplier) or admit there is no pattern and call it a swing. The swing is allowed; that's the wildcard slot in Step 3. What is not allowed is the in-between: a "proven" structure with no named entry behind it.

## Step 3: Write wide, then kill

Write 20 or more candidates across the structures, then keep the best 2 per group. Most of what you write should die. The kill rate is where quality comes from; a set where everything survives was never selected, only collected.

**A sharp seed enters as the leader.** When `piece.md` carries an `anchor:` receipt (a seed line plus its source outlier, channel, views, and xMed, inherited from vid-ideas through vid-intake), that seed enters the candidate set as the leading candidate, the one everything else has to beat. A real audience already voted for its shape; the receipt is what earns the lead, so a bare working title with no receipt stays one candidate like any other. Do not re-derive from scratch when a sharp seed exists: shop the banks specifically to beat it, write the wide pass around and against it, and run it through the same kill pass as everything else. If it survives, it leads its structure group with the anchor receipt pinned; if nothing beats it, lock the seed itself. A seed is a head start, never a shortcut: the wide write, the kill pass, and the lock list still govern every word, the seed included.

The creative act is the **adjust**: keep what makes the structure win, aim it at this video. Name why the source outlier works (what the viewer feels, what their brain fills in), then rebuild that exact pull out of this video's material. Swap the subject and the stake, keep the engine.

- Dead adjust: outlier is "Gym MISTAKES That Kill Your Progress", video is meal prep, you write "Meal Prep Mistakes That Kill Your Progress." Nouns swapped, pull lost; "progress" was the gym audience's stake, not this one's.
- Alive adjust: "Meal Prep Mistakes That Keep You Ordering Takeout." The engine survives (you're doing something wrong and it costs you the thing you care about) and the stake is now this avatar's actual one.

### The click judgment

Six calls, learned by example.

**Feel new beats be new.** N is the strongest BENS letter for an audience that has tried things and failed, and the information does not need to BE new. It needs to FEEL new.
- Weak: "How To Write Better Emails." The advice could be great; the viewer has scrolled past this promise a hundred times.
- Strong: "The 3-Line Email Rule That Doubled My Replies." Same advice, named and framed so it feels undiscovered. The info didn't get newer; the framing did. Chasing all four BENS letters flattens a title; one strong letter carries it.

**Specific reads as true, and true reads as safe.**
- Weak: "How I Make Money On YouTube." Vague, and the brain fills in nothing.
- Strong: "$14,332 From a Channel With 2,500 Subs." $14,332 beats "money" because round numbers read as invented and odd numbers read as earned. Spend the most precise true number on the lock list, not the safest paraphrase.

**Subtext is the product.** Read the candidate and ask what the viewer's brain fills in.
- Weak: "How I Make Money On YouTube" says what the video is about. Nothing to resolve, so nothing to click.
- Strong: "$14,332 From a Channel With 2,500 Subs" never says "how." The viewer's brain asks it for them, and that self-generated question is the click. A candidate whose subtext is "this video is about X" is a label wearing a title's clothes. Kill it or sharpen it.

**Match credibility to the channel.**
- Weak: "My Morning Routine" on a 300-sub channel. A cold viewer owes a stranger's "I" nothing; fame-dependent titles presume trust the channel hasn't earned.
- Strong: "$340K to $1.3M on 2,500 Subscribers." The numbers carry the credibility the "I" can't. On a small channel, specifics, named methods, and borrowed authority do the trusting. The one exception: a claim dramatic and specific enough earns the click on any channel size.

**One open question, exactly one.** A strong title opens one question in the viewer's mind and leaves it hanging: "am I missing something?" or "am I doing something wrong?" Two questions dilute each other and the brain resolves neither. Zero questions dies the other way: nothing open, no reason to click.
- Weak: "The $12 Scale That Fixed My Diet And The Habit That Fixed My Sleep." Two loops open at once ("what scale?" and "what habit?") and each waters down the other; the brain picks neither and scrolls.
- Strong: "The $12 Scale That Fixed My Diet." One loop, wide open: what scale, and how does a scale fix a diet? Cut the second promise and the pull doubles. The zero-question version of the same video, "How I Eat Better Now," gives the brain nothing to resolve, so the brain gives the title nothing back.

**One mechanism, executed well.** Every strong title runs on a single click mechanism: curiosity gap, loss aversion, pattern interrupt, desire for the transformation, or social proof. The angle picks the mechanism, and you spend every word executing it. Stacked mechanisms read as desperate, not stronger: three levers pulled halfway each lose to one lever pulled all the way.
- Weak: "10,000 Runners Swear By This Weird $12 Scale Before It Sells Out Again." Social proof ("10,000 runners"), curiosity ("weird scale, what is it?"), and loss aversion ("before it sells out") all grab at once, and the line reads like an ad that needs the click instead of a title that earns it.
- Strong: "Why 10,000 Runners Weigh Their Food." One mechanism (social proof: that many people doing a strange thing means they know something) executed clean. When the angle argues a mistake, loss aversion leads and the crowd stays home; when the angle promises a result, desire leads. One angle, one lever.

Two more lenses stay on while writing:

- **Title the wound, not the mechanism.** Same video, two titles: "You're Meal Prepping in the Wrong Order" titles the mechanism, and nobody lies awake about order. "Meal Prep Mistakes That Keep You Ordering Takeout" titles the wound. If the title names what the video does instead of what the viewer feels, it's a label with a pulse.
- **Spend the hot words.** Cover the structure and read only the payload words. Bank winners run hot: Hard Way, AWFUL, Secret, DON'T, QUIT. If your payload words are procedural (order, first, steps, setup), the title is room temperature and dies on a cold feed. Spend the hottest true words available: the power-words bank, the avatar's pain language, the dump's most visceral verbatim lines. A set with zero hot words means the banks were loaded and never spent.

Then **one wildcard**: one or two swings written cold from the video's boldest true claim, no pattern behind them, flagged as the experiment. Most lose to the proven structures, and every so often one becomes the creator's next own-winner. That slot is how the bank grows instead of calcifying.

## Step 4: One checklist pass

Walk every candidate through once, fix or cut, move on. No second lap.

- 50 characters or under (55 ceiling; anything 51 to 55 needs a named reason to keep)
- Opens a loop: something for the viewer's mind to resolve
- Only lock-list specifics, zero exceptions
- Reads aloud as one continuous human thought; no stitched fragments, no invented compound nouns
- No colons, no pipes, no AI-default phrasing (the hard-cut openers live in `references/title-filters.md`)
- Leaves the thumbnail room to add a second beat, not repeat this one

These are benchmarks, not laws. The creator's own results overrule any line here except the lock list.

## Step 5: Present with receipts, recommend the ceiling

Show 6 to 10 survivors grouped by structure. Each candidate line carries its BENS letters and an honest character count (count it, don't estimate). Each proven group pins its receipt in one line: source outlier, channel, multiplier, traced from a real bank row. No defense paragraphs; if a title needs an essay to sound good, the essay is hiding a weak title.

```
### Mistakes-with-a-cost
receipt: "Gym MISTAKES That Kill Your Progress" (@channel, 9x)
1. "Meal Prep Mistakes That Keep You Ordering Takeout"  B+N  (49)
2. "How 3 Freezer Meals Ended Our Takeout Habit"  B+S  (43)

### Wildcard (the swing, no pattern behind it)
3. "Cooking Every Night Is the Mistake"  N  (34)
```

Lead with a recommendation and a reason. You are a partner with a point of view, not a menu. **Recommend the ceiling, not the floor:** the title you would bet outperforms the bank, not the one with the fewest ways to fail. If the sharpest true option carries a risk (bold for a cold channel, needs a beat to parse), recommend it anyway, name the risk in one line, and point at the safest strong option as the split-test counterweight. Demoting the best title to second place because it "might not land" is the safety bias this skill exists to kill. The creator decides which risk to take; you don't pre-flinch on their behalf.

Push back when it matters: a fabricated specific gets refused flat, an off-brand pick gets named, a fame-dependent title on a cold channel gets the credibility warning. If the creator overrules a soft call, their call wins; the lock list alone is not negotiable.

## Step 6: Lock one title, with its receipt

On the pick, in both modes:

- Write the title to `content/pieces/{slug}/piece.md`'s `title:` field and bump `last_updated:` to today. Nothing else in the file changes; framing's fields survive untouched.
- The wide pass, the kill pass, and the receipts stay in the conversation. No titles file.
- Confirm in one line: "Title locked: '{title}'. Saved to piece.md."

Pipeline mode also returns the title string and its BENS letters to the caller. Then point to vid-thumbnail: the title and thumbnail are one unit, and a strong candidate that lost here often lives again as thumbnail text. The 3-concept split test there settles what conversation can't, so don't over-litigate second place.

**Stop.** Thumbnail, hook, and script are other skills.

## Related skills

- `vid-framing` locks the angle this skill packages; angle problems route back there, never get fixed here
- `vid-thumbnail` runs next and writes the thumbnail text
- `vid-ideas` may leave a seed line; when `piece.md` carries its `anchor:` receipt, the seed enters as the leading candidate to beat (Step 3), otherwise it stays one candidate, free to beat
- /foundation produces `creator-foundation.md`; `vid-research` produces the banks
- `vid-pipeline` orchestrates and calls this skill during packaging
