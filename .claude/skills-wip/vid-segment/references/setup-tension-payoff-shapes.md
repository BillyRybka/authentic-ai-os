---
type: reference
scope: vid-segment
status: active
tags: [reference, setup-tension-payoff, segment, format-aware]
---

# Setup / Tension / Payoff Shapes

Per-format examples of how a segment opens, raises tension, and pays off. Examples lead. Principles follow. Every shape pairs a worked example with a near-miss so the boundary is clear.

This file is reference material for Claude to think with at structure-pass time (Phase 2 of vid-segment). The format planner says WHICH shape to use; this file shows WHAT each shape looks like in practice.

## Why STP shapes vary by format

Setup / Tension / Payoff is the universal arc, but every format compresses or expands the three blocks differently. A 7-minute news segment can't carry a 90-second story setup. A 60-minute deep dive can't run on tight news-shape segments without losing tension. The shape has to match the format's energy.

The seven format shapes below pull from `knowledge/format-planners/{format}.md`. If a planner conflicts with anything here, the planner wins. Surface the conflict to the creator.

---

## Shape 1: Deep Dive segment (heavy STP)

Each step in a deep dive has its OWN Setup / Tension / Payoff. Proof gets woven in after the framework lands. Length per segment: 3-8 minutes typical, occasionally longer.

**Worked (heavy STP, Step 5 of a system-build deep dive):**

> SETUP: "By this point, you've built the offer and you've built the audience. But there's a third lever most people skip. The lever that took my client Steve from 4 calls a month to 4 calls a week."
>
> TENSION (story parable): Tells Steve's story. The one Wednesday afternoon he tried his usual outbound script and got six no-shows. The action: he changed one line in the follow-up email. The outcome: 4 calls booked the next 8 days, all from the same email list.
>
> TENSION (principle): Names the framework: "the Re-engagement Trigger." Walks the components (what triggers the message, what the message says, what happens after). Drops in proof: a Loom screenshot of Steve's calendar going from 4/month to 4/week.
>
> PAYOFF: "So when your outbound dries up, you're not the problem. The trigger is. Build the trigger and the calendar fills."
>
> TRANSITION OUT: "Which brings us to the next big problem: the calls book, but they don't close."

Why this lands: Setup names the lever AND tags Steve immediately so the story has a hook before it starts. Tension uses both a parable (Steve's story, P-A-O) AND a principle (named framework + proof asset placed AFTER the framework, not before). Payoff is one sharp sentence the viewer can repeat. Transition forward-hooks the next segment by naming the new problem.

**Near-miss (deep dive segment running flat):**

> SETUP: "Now we're going to talk about outbound."
> TENSION: "Outbound is important because it brings in calls. There are several ways to do it. The first way is..."
> PAYOFF: "And that's outbound."
> TRANSITION: "Now let's talk about the next thing."

Why this misses: Setup is a topic label, not an emotional or stakes-based open. Tension is description, not show-then-tell, with no story, no proof, no framework name. Payoff is the topic-label closing. Transition is "let's talk about" (banned phrase B-2). Every block is a dead block.

---

## Shape 2: Short Process segment (lean, principle-only by default)

Short Process has ONE big STP up front in the intro. Body segments default to lean principle-only steps. Add a mini parable INSIDE a step ONLY when that step is hard or the viewer won't believe it.

**Worked (lean Step 3 in a 5-step process):**

> SETUP (one sentence): "Step 3 is where most creators stall, so this is the one to slow down on."
>
> TENSION (principle-only): "Open your editor and find the rough cut from yesterday. Drag the audio waveform up so you can see the spikes. Cut every spike that doesn't have a word attached."
>
> PAYOFF: "That's it. Three minutes shaved off every video, every time."
>
> TRANSITION OUT: "Step 4 is going to make sure those cuts don't sound jumpy."

Why this lands: Setup names the stall risk in one line, which earns the lean structure. Tension is direct action with concrete verbs (find, drag, cut). Payoff is the receipt (3 minutes shaved). Transition forward-hooks Step 4 by naming the new risk (jumpy audio).

**Worked (lean step UPGRADED with mini parable because step is hard):**

> SETUP (one sentence): "Step 4 is the one nobody wants to do, but skipping it is why everyone's videos sound like a knife fight in a phone booth."
>
> MINI PARABLE (visual demo, 30 seconds): "Listen to this." [plays cut audio with no smoothing, jumpy and jarring] "Now this." [plays the same audio with crossfades] "Same cuts, totally different feel."
>
> TENSION (principle): "On every cut, drag the right edge of the previous clip 0.3 seconds into the next. That's the crossfade. Do it on every cut."
>
> PAYOFF: "Audio that sounds like a person talking, not a glitch."
>
> TRANSITION OUT: "Step 5 is the export setting that makes or breaks YouTube quality."

Why this lands: Hard step earns the parable. The parable is a 30-second visual demo (Show-the-Problem then Contrast). The principle stays tight because the parable already did the emotional work. Payoff names the qualitative receipt.

**Near-miss (every step gets a block, which flatlines the format):**

A 5-step short process where every single step opens with a story and a metaphor and a principle.

Why it misses: Short process is meant to be FAST. Blocks at every step double the runtime, dilute the emotion (every block is a "this matters!" signal, and five "this matters!"s in one video means none of them matter), and contradict the format's identity. Save blocks for the steps that genuinely need them.

---

## Shape 3: Listicle segment (full STP per point)

Each point gets parable-then-principle. Strong transitions are the lifeline. Different block types across points (don't reuse the same block type for every point).

**Worked (Point 4 of "12 mistakes that kill consistent leads"):**

> SETUP: "Mistake number 4 is the one I made for two years and didn't even notice."
>
> TENSION (story parable): "I had a lead magnet. People were signing up. Open rates looked fine. But conversion to call was 0.4%. I kept swapping the lead magnet, kept rewriting the welcome email, nothing moved." [Action] "Then a friend asked to see my list and pointed at one line. The CTA in the welcome email said 'reply with your biggest challenge' instead of pointing them to a booking link." [Outcome] "I changed one line. Conversion went to 4.1% the next week."
>
> TENSION (principle): "The mistake: a CTA that gathers information instead of moving to action. Reply-to-me CTAs feel friendly but they put you in support mode. Booking-link CTAs put the prospect in commitment mode."
>
> PAYOFF: "Lead magnet didn't have a problem. The CTA did."
>
> TRANSITION OUT: "Mistake number 5 is going to fix something even more upstream: the form itself."

Why this lands: Setup is a personal-confession framing (humanizes the mistake). Tension uses a fully-played story (Problem-Action-Outcome with specific numbers, 0.4% to 4.1%). The principle explains WHY it worked (info-gathering vs. action-driving). Payoff is one sentence. Transition forward-hooks Point 5 by naming what's even more upstream.

**Worked (Point 5 with a DIFFERENT block type, same listicle):**

> SETUP: "Mistake number 5 is everywhere, but a metaphor will make it click."
>
> TENSION (metaphor parable): "Most lead-magnet forms are like a bouncer at a club: the more questions they ask at the door, the longer the line gets, and the fewer people make it inside."
>
> TENSION (principle): "Every additional form field drops conversion by roughly 5-15% depending on niche. Three fields is the comfortable ceiling for most B2B lead magnets. Five is the warning line. Seven is the bouncer who's never letting anyone in."
>
> PAYOFF: "Cut your form to three fields. Watch the conversion."
>
> TRANSITION OUT: "Mistake number 6 is what happens AFTER they convert, and it's the one that decides whether they actually buy."

Why this lands: Different block type than Point 4 (metaphor vs. story), so the listicle's energy varies. Bouncer metaphor is everyday-familiar (clubs, queues). The principle has a specific number range. Transition pivots to the post-conversion phase.

**Near-miss (every point opens "Lesson number X is..."):**

Why it misses: Pure announcement. No forward hook. No promise. Listicle viewers get bored fast and bounce. See `banks/transition-bank.md` Section 2 for forward-hook patterns.

---

## Shape 4: Case Study segment (one big STP across the whole body)

Case study's body IS the story arc. There's typically one segment, not many. The whole body answers the 5 case study questions (what was the problem / why did they need to fix it / what actions / what outcome / where's the proof). The principle (the takeaway) lands AT THE END of the body, not per-segment.

**Worked (full case-study body as one segment):**

> SETUP: "When [Client] came to me, his agency was billing $42k a month, all of it tied to himself, and he hadn't taken a Saturday off in three years."
>
> TENSION (the story IS the parable, Problem-Action-Outcome at full length):
>   - Problem: His delivery was bottlenecked on him because every project required custom strategy. Stakes: his wife had just told him "if this doesn't change, I'm raising the kid alone."
>   - Action: We rebuilt his delivery into three productized engagements with named deliverables. We trained one senior contractor on the framework. We changed the sales conversation from "tell me about your problem" to "here are the three engagements, which one fits."
>   - Failure mid-arc: First contractor delivered the framework wrong on engagement 2 and a client churned in month 3. We wrote the SOP that would've prevented it.
>   - Outcome: 9 months later, $74k MRR, two-week vacation, contractor handling 60% of delivery.
>   - Proof: Stripe screenshot, calendar screenshot, contractor's Slack name (anonymized).
>
> TENSION (principle, the lesson): "What this proves: productized engagements aren't a marketing move. They're a delivery move. The marketing follows the delivery, not the other way around."
>
> PAYOFF (the 1-3 actionable steps): "Three things you can do this week. Pick one engagement type from your past 10 clients. Write its named deliverable. Practice the new sales conversation in your next call."
>
> TRANSITION OUT (this is the only body segment, so transition is to the ending): "You now have everything you need to start productizing your delivery. The next problem is hiring the contractor without losing the quality, and I made a video on that. Watch it next."

Why this lands: One arc, one segment, one transformation. Specific numbers ($42k to $74k). Failure mid-arc (the contractor mistake) makes the story trustworthy. Lesson + 3 steps lands at the end. Transition pivots to the next problem (hiring) because the case study is one body segment.

**Near-miss (case study chopped into multi-segment listicle):**

Treating the case study like a listicle, where every action gets its own segment with its own STP, flattens the arc. The viewer needs ONE story they're following, not 7 mini-stories. If the body has multiple segments, the format is wrong (probably should be deep-dive instead).

---

## Shape 5: News segment (compressed STP)

Tight cycle: what happened (setup), why it matters (tension), what to do (payoff). 30-90 seconds per segment max. Speed beats depth.

**Worked (news segment on a platform policy change):**

> SETUP: "YouTube just updated the monetization policy on long-form content. Specifically: any video over 8 minutes now gets 6 mid-roll slots automatically, up from 4."
>
> TENSION (why it matters): "If you're running ads, this is a 50% increase in inventory per video without you doing anything. If you're a viewer, this is why the next 12-minute video you watch is going to feel like watching cable. Either way: more ads."
>
> PAYOFF (what to do): "Two moves. If you're a creator, audit your cuts. Pre-positioning a natural break around minute 4, 6, and 8 stops the algorithm from interrupting mid-thought. If you're a viewer, the new YouTube Premium discount drops in 2 weeks. Time to lock it in."
>
> TRANSITION OUT (or end of video, since news runs short, often 1-2 segments): "And the second update from this week is the one nobody's talking about, even though it changes how Shorts get recommended."

Why this lands: Setup gives the specific change (6 slots up from 4, the actual numbers). Tension explains stakes for both creator and viewer (covers two avatars). Payoff is two concrete moves. Transition to next segment (or signal that's the only news of weight this week).

**Near-miss (news segment with no POV):**

> SETUP: "YouTube changed something."
> TENSION: "It might affect creators."
> PAYOFF: "Watch closely."

Why it misses: No specifics. No POV. No stakes. This is a press release, and viewers don't watch press releases.

---

## Shape 6: Roast / Review segment (per-review STP)

Per contestant: show what they have (setup), show what's wrong (tension), show the fix (payoff). 3-7 minutes per review. Tone: stern-but-kind 7/10, never 10/10.

**Worked (review of a thumbnail, contestant 2 of 3):**

> SETUP: "Contestant two: [Channel Name]. Their video is about morning routines. Here's their current thumbnail." [shows thumbnail on screen]
>
> TENSION (problem identification): "Three things going wrong. The text says 'Daily Routine Hacks' which is generic and tells me nothing about THIS routine. The face has no expression, just a stock smile. And the colors are washed out so the thumbnail disappears in the feed."
>
> TENSION (the fix shown): "Here's what I'd do." [shows a redesigned mockup] "Text: '5am Without Caffeine.' Specific. Tells me the angle. Face: hand on chin, slight grimace, a real human reacting. Colors: pumped saturation by 30% so it pops in the feed. Same person, same niche, totally different click."
>
> PAYOFF: "The principle: text should name the angle, not the topic. Faces should react, not pose. Colors should pop, not blend."
>
> TRANSITION OUT: "Contestant three has the opposite problem: way too much going on, no clear focal point."

Why this lands: Setup is the contestant's actual material on screen. Tension splits into problem identification (3 specific things) AND the fix shown (mockup + 3 specific changes). Payoff names the principle so viewers can apply to their own thumbnails. Transition contrasts with contestant 3's opposite problem.

**Near-miss (review without the fix):**

> SETUP: "Contestant two has a bad thumbnail."
> TENSION: "It's bad because of these reasons."
> PAYOFF: "Don't do that."

Why it misses: Showing the problem without the fix proves nothing. Roast format converts because viewers see the fix work. Without the fix, you've just been mean.

---

## Shape 7: Interview segment (per-question STP)

Each question = one segment. Setup is the host's framing line. Tension is the guest's story (parable). Payoff is the guest's actionable insight (principle). Edit aggressively. Most footage gets cut.

**Worked (one question segment):**

> SETUP (host framing line, scripted, recorded separately): "I asked [Guest] about the moment her agency hit $1M ARR and what almost broke it 6 months before that."
>
> TENSION (guest's story, edited): [Guest] tells the story. Problem: lost two anchor clients in the same month. Action: instead of replacing them, she raised her prices 60% on the next three pitches. Outcome: two of three closed, agency was net-up within 90 days.
>
> PAYOFF (guest's actionable insight, edited): [Guest] names the principle. "Most agencies replace lost revenue. The move is to up-level the next pitch instead. The market's been telling you you're underpriced; the loss is the signal."
>
> TRANSITION OUT (host, scripted): "The next question I asked her was about the hiring decision that came out of that, and her answer surprised me."

Why this lands: Host's setup gives the question's frame in one line. Guest's story is fully P-A-O with specific numbers. Guest's payoff is the named principle. Host's transition is a forward hook (what answer surprised the host).

**Near-miss (long, unedited guest answer):**

A 4-minute guest monologue with no edits. Guest rambles, hits the point at minute 3, repeats it at minute 4.

Why it misses: Most guests aren't media-trained. They take 90 seconds to land a 15-second point. Edit aggressively. Pull the 30 seconds that contain the actual story and the actual insight. Cut the rest.

---

## Common cross-format mistakes

These fail across every format shape. If you see them in a structure draft, restructure before writing prose.

- **Setup that announces a topic instead of opening on emotion or stakes.** "Now we're going to talk about X" is the topic-label trap. Replace with the actual emotional or stakes-based hook for THIS segment.
- **Tension without a parable AND a principle.** Most segments need both. Pure principle = research summary. Pure emotion = drama without lesson. (Lean-segment exception below.)
- **Payoff that's a topic-label echo of the setup.** "And that's outbound" closes nothing. The payoff names what the viewer walks AWAY with: the lesson, not the topic.
- **Transition that's pure announcement ("now point 4").** See `banks/transition-bank.md` Section 2 for forward-hook patterns. Pure announcement loses 5-10% retention per transition.
- **Blocks where the format planner says no blocks.** Every step of a short process getting its own block contradicts the format's identity (fast action). Trust the planner.

---

## Lean segments and early payoff (source-backed exception)

Most segments need both a parable and a principle to land. But two source-backed cases relax this:

**Case 1: Early payoff with a new setup (rehook).**

Source quote (lesson-16): "Don't worry if you pay something off early. If you pay something off early and then you keep explaining it, that's a problem. If you pay something off early and then you instantly set up something else, you've rehooked them. It's fine."

Translated: a segment can compress to setup → quick payoff → new setup, without a full parable + principle pair, IF the payoff lands and immediately sets up the next thing the viewer needs to know. The danger is paying off early and then continuing to explain the same thing the viewer already understood. That's where retention breaks. The fix is the rehook, not adding a forced second block.

Worked example: a Short Process segment lands the lesson in 12 seconds with a one-line metaphor payoff, then immediately sets up the friction in step 2 ("but the second you try this with a cold list, it falls apart, here's what's actually going on..."). No story or stat block needed. The rehook IS the next block.

Near-miss: a Short Process segment lands the lesson in 12 seconds and then keeps explaining the same lesson with three more variations. Retention drops because the viewer's brain already moved on.

**Case 2: Intro setups can be paid off anywhere in the video.**

Source quote (lesson-16): "Intro setups don't have to be paid off immediately. They can be resolved anywhere in the video."

Translated: a segment can deliberately leave a thread from the intro hanging until later. Don't force every body segment to fully resolve the intro's promise. Sometimes the right move is to introduce a sub-piece in segment 2 and pay off the original intro thread in segment 4. The full-video arc is the unit, not the segment.

The rule: when a segment looks lean (short, missing a block), check whether (a) a rehook is doing the block's job, or (b) the missing payoff is intentionally deferred to a later segment. If neither, the segment is genuinely thin and needs structural work. If either, the segment is fine.

---

## How vid-segment uses this file

At Phase 2 (structure pass), vid-segment reads:

1. The matched format planner from `knowledge/format-planners/{format}.md`
2. This file's matching shape section
3. The relevant references for the block type chosen (story / proof / metaphor / etc.)

The structure draft surfaced to the creator pulls its skeleton from the matching shape. Bank candidates surfaced for each block slot get filtered through the per-shape examples. A story that lands in a deep-dive segment may not land in a tight news segment.

If the format planner conflicts with this file, the planner wins (it's loaded by all writing skills, this file is vid-segment-local).
