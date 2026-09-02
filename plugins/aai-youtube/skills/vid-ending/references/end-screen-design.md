---
type: reference
scope: skill-local
loaded_by: [vid-ending]
status: active
tags: [reference, ending, end-screen, next-video, chain-reaction]
---

# End Screen Design

Examples-first reference for picking which video to Bridge to, why the chain-reaction effect matters, and the two-option decision rule that takes 20-30 seconds. Sourced from the source-backed playbook that took end-screen click-through from 0.9% to 20%+.

This file is reference material for Claude to think with at draft time, not to paste at the creator.

---

## 1. The chain-reaction principle

Every video on the channel is a node in a connected system, not a standalone piece. The end-screen is the edge between nodes. Done well:

- One viewer entering the system gets pulled through 4-6 videos before they exit
- A single video that blows up drags the chain up with it (one creator's chain produced 700,000+ views from one viral entry)
- A flop video that converts (sales, emails) becomes a sales tool, point future videos at it from THEIR end-screens; you control the traffic

The Bridge is what activates this. A weak Bridge breaks the chain. A strong Bridge keeps the viewer inside the system.

The benchmark: 20%+ end-screen click-through is achievable on warm audience (already watching this video). It's nearly impossible on cold YouTube traffic. The end-screen is the single highest-CTR placement on YouTube, if the Bridge is built right.

---

## 2. The 20-30 second decision rule

Picking the next-video should take 20-30 seconds, not 20-30 minutes. Two options. Pick one. Move.

### Option 1: Point to what converts best for the goal

Goal=sales: which past video converted best for sales (per RevTrack data or whatever conversion-tracking the creator uses)?
Goal=emails: which past video drove the most email signups?
Goal=views: which past evergreen video pulls the strongest watch-time?

Pick that one. Bridge to it. Done.

### Option 2: Point to the previous high-performer in the same format

If this video is the latest in a series (the third review, the fifth success story, the second deep-dive on a topic):

Bridge to the previous video in the same format that hit the goal. NOT automatically the most recent one. If the most recent was a flop, skip it. Always link to one that got results.

### When neither option works

- **First video on the channel.** No previous video. Don't link to a video, point to subscribe. End-screen card is the subscribe button. Source-backed: "we all have to start the chain somewhere."
- **Repositioned channel.** The old videos don't fit the new positioning. Don't link to them. Subscribe-pointer until the new chain starts.
- **No converter yet.** Goal is sales but nothing has converted yet. Pick the strongest watch-time video on the channel. The viewer hasn't seen it; weak conversion data doesn't matter for them.

---

## 3. The "do not link to" rules

These are non-negotiable. If the creator picks a Bridge target that violates one, refuse and explain.

### R-1. Never link to an underperforming video.

Even if it's the most recent in this format, even if it's "the obvious next step", even if the creator made it last week. If it underperformed, it carries the underperformance forward. Pick a different one.

The exception: a video with low VIEWS but strong CONVERSION (per Option 1 above) is NOT underperforming, it's a sales tool waiting to be pointed at. Use it.

### R-2. Never link to a video you haven't made yet.

Source-backed rule. Confuses viewers, who can't watch what doesn't exist. By the time the new video drops, this video's audience is gone. Future-promise Bridges burn the click moment.

If the creator says "but I'm filming it next week", still no. Either pick a different existing video or hold the close as subscribe-pointer.

### R-3. Never link off YouTube for views-goal videos.

External links kill algorithm recommendations. For views goal, the entire close stays on YouTube. Bridge to next video, end-screen card, no external link in description.

For sales/emails goal, external links are fine in description but the Bridge itself should still point to a YouTube video. The Bridge is about retention; description links are about conversion. Different jobs.

### R-4. Never link to "more news" from a news video.

Per news format planner. News-to-news links turn the channel into a news channel, audience comes for news, not for the creator. Channel never grows on the creator's brand.

News videos always Bridge to non-news evergreen content. Convert the news algorithm spike into channel audience for the durable content.

### R-5. Never link to "another interview" from an interview video.

Per interview format planner. Same failure mode as R-4, interview-to-interview turns the channel into a podcast where the host has zero credibility transfer. Always Bridge to a video where the CREATOR is the expert.

---

## 4. Verification before lock

Before saving the Bridge, verify:

1. **Target video exists.** Check that `[[next-video-slug]]` resolves to a real piece in `content/pieces/` OR that the creator confirms the published URL exists.
2. **Target video matches goal.** If goal=sales, the target is a sales-converting video. If goal=emails, an email-converting one. If goal=views, an evergreen with strong watch-time.
3. **Target video is not in violation of R-1 through R-5.** Run the rule checks.
4. **Wikilink target resolves.** If `content/pieces/{next-slug}/piece.md` doesn't exist, surface to the creator: "wikilink doesn't resolve. Want me to (a) ask for the right slug, (b) leave as plain text and you fix later, or (c) skip the Bridge until the next video is created?"

If verification fails, do not lock. Ask the creator to fix or pick a different target.

---

## 5. The Bridge sentence relationship to the end-screen card

The end-screen card appears on screen during the Bridge sentence. The line and the card are designed to land together, the creator says "watch this next" while the card animates in. Click-through happens in the 5-10 seconds the card is visible.

Implications:

- Bridge sentence should NAME the card's content (or strongly imply it). The card title and the Bridge content should match.
- Don't put the Bridge sentence too early in the close. The Pivot and Gap have to land first; the card animation is timed to the Bridge.
- Don't put anything after the Bridge. Once the card is visible, every additional second of speech is a chance the viewer clicks before you finish, silence after the Bridge is fine, more talking isn't.

The creator's editor (or the creator if they edit themselves) will time the card to the Bridge. The skill doesn't write timing instructions into the script, it just makes sure the Bridge sentence is the LAST thing said.

---

## 6. Worked decision examples

### Example 1: Step-by-Step video, sales goal, established channel

Creator's strongest sales-converting past video is "The 5-Step Onboarding System That Books Calls", a deep dive that walks the methodology.

Bridge: "Watch this next where I show you the full 5-step system in action."

Why this works: matches Option 1 (best converter for goal). The Pivot recapped a tactic, the Gap revealed the system gap, the Bridge points to the full system video. Viewer gets sequential value.

### Example 2: Review video, sales goal, established channel

This is the third review in a review series. The previous review (review #2) flopped on conversions. Review #1 was the strongest sales-converting review.

Bridge: point to review #1 (Option 2, previous high-performer in same format, NOT the most recent).

Why this works: per R-1, skip the underperformer. Format-loyal audiences want more reviews; route them to the strongest one.

### Example 3: News video, views goal, small channel

This is breaking news in the niche. No previous news video has converted strongly because the channel is new. The creator's strongest evergreen is a deep-dive on a related topic.

Bridge: point to the evergreen deep-dive (per R-4, never news-to-news; per format planner, end-screen to non-news evergreen).

Why this works: converts the news algorithm spike into channel audience. The deep-dive demonstrates the channel's actual value to a viewer who arrived for one news story.

### Example 4: Interview video, views goal, established channel

The guest is a notable creator. Viewers came for the guest. Per interview format planner, Bridge has to point to a video where the CREATOR is the expert, not another interview.

Bridge: point to the creator's strongest evergreen step-by-step or deep-dive on the same topic the guest discussed.

Why this works: per R-5, never interview-to-interview. The end-screen converts guest-arrived viewers into creator's audience.

### Example 5: First video on a repositioned channel

Creator has 50 old videos that don't fit the new positioning, plus one new video (this one). No previous video matches.

Bridge: subscribe-pointer (per source rule for first videos / repositioning).

Why this works: starts the chain at this video. Future videos in the new positioning will Bridge to this one.

---

## 7. Default Bridge phrasing patterns

When the creator picks a target, draft the Bridge using one of these patterns. Match the creator's voice profile.

- **"Watch this next, where I'll show you exactly how to {outcome}."** Specific outcome named, "show" verb.
- **"I made a video on it. Watch this next."** Short, confident, lets the card carry the rest.
- **"That's what I'm going to show you next."** Works when the Gap already named the topic.
- **"The next thing on your stack is {topic}. Watch this next."** Stack-language reads as a checklist.
- **"Here's where to find the answer."** Works when Gap was framed as a question.

If none of these fit the creator's voice, draft from scratch using the creator's voice profile defaults. The patterns are starting points, not gates.

---

## 8. Logging the Bridge for measurement

When the close is locked, the Bridge target gets logged in `piece.md`:

```yaml
ending_locked: true
next_video: "[[slug-of-next-video]]"
```

When `vid-measurement` is built, it will re-introduce a pattern-log field (the Bridge shape used) and read it alongside the actual end-screen click-through rate, so wins (CTR > threshold) can be logged back into the channel's research. Until that reader exists, the ending does not journal its pattern into piece.md.

The skill doesn't run measurement, it produces the structured data that measurement reads. This is what enables the channel to learn which Bridge shapes work over time.
