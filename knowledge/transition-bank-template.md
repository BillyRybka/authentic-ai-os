---
type: bank
project: authentic-ai-os
kind: patterns
status: active
tags: [bank, transitions, patterns]
---

# Transition Bank

Fill-in-the-blank transition patterns plus banned phrases. Used by `vid-intro` (intro to first point), `vid-segment` (point to point), and `vid-ending` (final point to CTA) to forward-hook one beat into the next without dead-air filler. Patterns are templates with `[X]` slots.

> **This is a starter you grow.** creator-setup scaffolds this file into your `banks/`. It is yours from here. Cut patterns you would never say, rewrite the examples in your own voice, and add transitions that work for you. The skills read whatever is in your vault, not the plugin default. The examples below are generic on purpose. Replace them.

The forward-hook rule: every transition raises a question, names a gap, or teases the next beat so the viewer keeps watching. A transition that just says "next" leaks retention.

---

## Section 1. Hook-forward transitions (intro to first point)

Used by `vid-intro` for the move from the opening into the first body beat.

### Patterns

**HF-1.** To start, I'm going to show you how to [solve big problem the viewer feels].
**HF-2.** To start, I'm going to show you how to [reach big result the viewer wants].
**HF-3.** But how do you actually do that? Let me show you so you can [big result].
**HF-4.** So step one is critical if you want to [outcome], and it works like this.
**HF-5.** This first part of my system will [solve big problem / deliver big result].
**HF-6.** Most people fail right here because of [common mistake]. But when you do this next step, [outcome].
**HF-7.** Starting with #[1] (or "the first one"), [result the count's first item delivers].
**HF-8.** Now you know [setup recap, one phrase], let me show you how to [first point's payoff].
**HF-9.** [Topic-specific bridge phrase], because [the reason the next section matters].

- Worked (HF-6): "Most people stall right here because of [mistake]. Do this next step and [outcome]." Names the failure, then promises the fix.

---

## Section 2. Segment-to-segment transitions (point to point)

Used by `vid-segment` for the outbound handoff at the end of each body section.

### Patterns

**SS-1.** Which brings us to the next big problem: [the next point's named pain].
**SS-2.** Most people fail right here because [specific mistake]. The next step fixes it.
**SS-3.** Next, I'm going to show you how to avoid [specific bad outcome].
**SS-4.** Next, I'm going to show you how to [specific micro-result].
**SS-5.** [Point N+1] is going to [result the avatar cares about], even if [common excuse the avatar uses].
**SS-6.** That leads us into how to [next point's central action verb plus outcome].
**SS-7.** Now you know [recap of point N's lesson], let me show you [point N+1's promise].
**SS-8.** And the result of doing it that way? [Specific receipt or stat]. Now let me show you the next piece.
**SS-9.** Most creators stop here. The ones who don't get [specific result] do this next.
**SS-10.** This next part is the one most people get wrong, and it costs them [specific consequence].
**SS-11.** What happened next completely [result], so now I'll show you how to do the same.
**SS-12.** To prove this point, let me show you [example or demo].

- Worked (SS-9): "Most creators stop here. The ones who get [result] do this next." Forward-hooks with a status gap.

---

## Section 3. Body-to-ending transitions (final point to CTA)

Used by `vid-ending` for the bridge from the last body beat into the Pivot/Gap/Bridge close. Every one reveals the NEXT problem so the close can point to the next video.

### Patterns

**BE-1.** So now you know how to [recap of transformation], but here's the thing: [the next problem they now have].
**BE-2.** That's the [N] [things you teach]. But here's the gap most people hit next: [specific new problem].
**BE-3.** You now have everything you need to [primary outcome of the video]. The next problem is [the new problem the next video solves].
**BE-4.** [Strong recap line]. The reason most still don't get the result is [the new lever]. That's what I'm going to show you next.
**BE-5.** Look, [specific tool / pattern / system you taught] is real. But it only works if [the dependency you teach next]. Watch this next.
**BE-6.** Here's the thing nobody warns you about [the topic you just taught]: [the second-order problem]. I'll show you how to handle it next.
**BE-7.** That's how you [recap line in plain language]. The next thing on your stack is [specific named next problem]. I made a video on it. Watch it next.
**BE-8.** Quick recap: [one phrase]. Now the question becomes [the next-video question]. Here's where to find the answer.

- Worked (BE-3): "You now have everything you need to [outcome]. The next problem is [named new problem]." Closes one loop, opens the next video's loop.

---

## Section 4. Banned phrases

Auto-reject or soft-friction phrases. `vid-intro`, `vid-segment`, `vid-ending`, and `vid-pressure-test` all check outbound transitions against this list.

### Tier 1: auto-reject

- **B-1. "Let's dive in."**
- **B-2. "Let's talk about..."**
- **B-3. "Let me tell you..."**
- **B-6. "And finally..." / "And lastly..."**

### Tier 2: soft friction (creator decides)

- **B-4. "Without further ado..."**
- **B-5. "Now, before we begin..."**
- **B-7. "But here's where it got interesting..."**
- **B-8. "You won't believe what happened next."**
- **B-9. "Now let me tell you a quick story."**
- **B-10. "Stay tuned for..."**
- **B-11. "Today's video is about..."**
- **B-12. "Anyway, moving on..."**
- **B-13.** The default verb "tell" instead of "show." Prefer "let me show you."

---

## How skills use this file

- `vid-intro` pulls a Section 1 pattern for the intro-to-first-point handoff, slot-fills from the brain dump, and checks it against Section 4.
- `vid-segment` pulls a Section 2 pattern for each segment's outbound transition (or a Section 3 pattern if it is the final body segment), then checks Section 4.
- `vid-ending` pulls a Section 3 pattern for the body-to-ending bridge.
- `vid-pressure-test` audits every transition against Section 4 banned phrases.
