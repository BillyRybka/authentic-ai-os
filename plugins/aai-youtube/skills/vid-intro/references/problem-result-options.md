---
type: reference
scope: skill-local
loaded_by: [vid-intro]
status: active
tags: [reference, problem-result, decision-flow]
---

# Problem/Result Options Decision Flow

How `vid-intro` picks between the 3 Problem/Result options after the Hook lands. The 3 options (Poke / Tease / Combine), their pivot phrases, and per-format defaults live in [[intro-architecture]] Step 3 and each `knowledge/format-planners/{format}.md`'s intro-adaptation Problem/Result row. This file does NOT restate either. It teaches the runtime intensity-matching decision: how to read pain-acuteness and result-drama against each other to pick the option for a specific video.

Examples-first contrastive: every option pairs a worked match with a near-miss.

## The three inputs that decide

`vid-intro` cross-references three things:

1. **Avatar pain intensity** (for the problem this video addresses): how acute is it? The avatar's Top 3 in `foundation/avatar.md` are a useful gauge, but score the actual problem the video pokes, even an adjacent one.
2. **Result drama** (from brain dump's lock list): how impressive is the receipt?
3. **Format identity** (from format planner): what does the format expect?

When pain is acute and the result is moderate, Poke. When pain is moderate and the result is dramatic, Tease. When both are high, Combine.

## Worked: Poke the Problem (acute pain, moderate result)

**Setup:** Short Process video on writing follow-up emails. Avatar problem #1 is "I forget to follow up on warm leads and they go cold." The result is "you'll send better follow-ups," which is real but not dramatic.

**Output (after a Question Hook):**

> "Do you ever close a discovery call feeling great, then forget to follow up for a week, then never hear from the prospect again? Every freelancer I know does this. The thing is, the gap between the call and the follow-up is where 60% of deals die. You don't have a sales problem. You have a memory problem."

**Why this lands:**

- The pain is acute and the avatar feels seen
- The "every freelancer I know does this" line normalizes it (avatar isn't alone in failing)
- The "the thing is" pivot drops the hidden cost (60% of deals die in the gap)
- The "memory problem" reframe sets up the body's solution

The result tease is implicit ("solve the memory problem"). Poke alone is enough because the pain is the engine.

## Worked: Tease the Result (moderate pain, dramatic result)

**Setup:** Case Study video. The client made $250k in their first year off a single offer. Avatar feels mild frustration with their current revenue but isn't desperate. The receipt is huge.

**Output (after a Statement Hook):**

> "Six months ago Steve was making $4k a month grinding on Upwork. Now he's making $25k a month with three retainer clients and zero Upwork. He didn't change skills. He didn't add a niche. He changed one thing about how he packaged the offer."

**Why this lands:**

- Tease leads with the receipt because the receipt is the engine
- "He didn't change X. He didn't add Y. He changed one thing." is the curiosity pivot. Same job as "I used to until..." but tighter
- The viewer feels hope (they could be Steve) without needing the pain poked first

When the result is dramatic enough on its own, Poke wastes time. Just tease.

## Worked: Combine Both (high pain AND dramatic result)

**Setup:** Deep Dive video on YouTube growth for businesses. Avatar problem #2 is "I've spent six months making videos and have 200 subscribers, this isn't working." Brain dump has a $4M YouTube revenue receipt.

**Output (after a Statement Hook):**

> "Most YouTube channels for businesses die at 1,000 subscribers because the creator started solving a different problem than the one they validated. Every creator I know has been there: six months in, 200 subs, asking 'is this even working?'. The thing is, the channels that DON'T die do three things differently. I've used these three to generate over $4 million from YouTube in two years. So I'm going to give you each one so you can stop guessing."

**Why this lands:**

- Pokes the pain ("six months in, 200 subs, asking 'is this even working?'")
- The "thing is" pivot introduces the lever (three things)
- Then the "But..." style pivot teases the result ($4 million)
- Closes with the contract ("give you each one")

When both halves are loud, Combine carries the weight. Most powerful, longest of the three. Reserve for formats that earn the runtime (Deep Dive, sometimes Case Study, sometimes Listicle).

## Near-miss: Poke when the avatar's pain is mild

**Setup:** Listicle video on Photoshop shortcuts. Avatar problem isn't really acute. They're fine, just slow.

**Wrong move:** open with a heavy Poke ("Do you ever stare at Photoshop wondering if you'll ever stop fighting the tools? Every designer I know does. The thing is, slow editing is killing your rate-per-hour and you don't even realize it.").

**Why this fails:** the avatar reads it and thinks "I mean, sure, but I'm not THAT frustrated." The poke overshoots, the viewer feels manipulated, and the stakes feel manufactured. Tease the result ("These 10 shortcuts cut my edit time from 30 minutes to 8") would land cleaner because the avatar wants the relief, they don't need the pain inflated first.

**The rule:** match the Poke intensity to the avatar's actual pain level. If you have to manufacture stakes, the option is wrong.

## Near-miss: Tease when the result is generic

**Setup:** Short Process video on writing better LinkedIn posts. The "result" is "you'll get more engagement on LinkedIn." Real, but not dramatic.

**Wrong move:** open with a heavy Tease ("I used to write LinkedIn posts that got 12 likes. Then I figured out a five-step formula that makes every post hit 200+ likes.").

**Why this fails:**

- "12 likes to 200 likes" isn't dramatic enough to carry a Tease. It's a normal improvement
- Without a Poke, the viewer doesn't feel the OLD pain (writing posts that flop), so the relief feels weak
- The result ("more engagement") is generic; the receipt isn't strong enough to drive belief alone

**The rule:** Tease only works when the receipt is strong enough to drive belief on its own. Mild improvements need to be paired with a Poke to feel valuable.

## Near-miss: Combine when neither half is loud

**Setup:** Listicle video on productivity habits. Avatar pain is "I want to be more productive" (mild). Result is "you'll have better habits" (mild).

**Wrong move:** open with a Combine ("Do you ever feel like you're not as productive as you could be? Every busy person I know does. The thing is, your habits are the lever. But there are five habits that compound, so I'm going to give you each one.").

**Why this fails:** the Combine inflates both halves to fill the runtime, but neither half can carry weight. The viewer reads it and tunes out because nothing is high-stakes. Tease alone ("Here's the 5 habits that turned my Sundays from chaos into the most productive day of the week") would land cleaner because at least one beat is concrete.

**The rule:** Combine is the most powerful and longest option. Reserve it for videos where BOTH halves are loud. If only one half is loud, use that half alone.

## Format-specific defaults

Each format planner's intro-adaptation Problem/Result row gives the format default. Read `knowledge/format-planners/{format}.md` for the matched format. When the planner says "often X," use X as the starting point. When the planner says "skip," skip. When in doubt, the format planner overrides the avatar/result intensity intuition above.

## The decision short-list (run silently in Phase 2)

1. **Identify the problem this video addresses.** It was chosen at framing, usually one of the avatar's Top 3 (in `foundation/avatar.md`), sometimes an adjacent one. Score its pain intensity for the avatar (acute / moderate / mild)
2. **Read the brain dump's lock list.** Score the result drama (dramatic / moderate / mild)
3. **Read the format planner's Problem/Result default.** Note what the format usually does
4. **Cross-reference:** acute-pain + moderate-result → Poke. moderate-pain + dramatic-result → Tease. acute-pain + dramatic-result → Combine. mild-pain + mild-result → reconsider whether the video is worth making
5. **Generate 2-3 candidates** across the chosen option. If two options score similarly, generate one of each so the creator can compare

Surface options as a numbered list with annotation:

```
PROBLEM/RESULT candidates
A. Poke: "Do you ever close a discovery call feeling great, then forget to follow up..." (Top 3 problem #1, pain-intensity high)
B. Combine: "Do you ever close a call feeling great then forget? Every freelancer does. The thing is, that gap kills 60% of deals. But there's a 3-step follow-up template that..." (Top 3 problem #1, both halves anchored)
```

Creator picks. Push back on weak combinations (acute-pain matched with mild-result Tease, mild-pain matched with heavy Poke).

## What this file does NOT do

- It does not pick the actual content (the specific words). The brain dump and `foundation/avatar.md` supply that
- It does not enforce one option as universal. Each format has its own default; the creator can override
- It does not handle the credibility weave inside the Problem/Result. That's [[credibility-line-weaving]]
