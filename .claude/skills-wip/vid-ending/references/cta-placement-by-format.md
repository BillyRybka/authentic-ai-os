---
type: reference
scope: skill-local
loaded_by: [vid-ending]
status: active
tags: [reference, ending, cta, format-aware]
---

# CTA Placement By Format

Examples-first reference for which goal-and-format combinations work, which tank, and where the CTA actually goes within the close. Sourced from format-planner observations and the conversion playbook.

This file is reference material for Claude to think with at draft time, not to paste at the creator.

## The principle

Goal × format determines CTA shape. Get the pairing wrong and a strong close still under-performs. Get it right and a weaker close still converts.

The goal is set in `content/pieces/{slug}/piece.md` (`goal: sales | emails | views`). The format is set there too. The ending uses both fields to pick CTA shape.

**Hard rule:** one goal per video. Sales OR emails OR views. Never two. A close that pitches sales AND a lead magnet AND end-screens to views is three signals fighting each other; viewers pick none.

---

## 1. Format-goal compatibility matrix

The format planners encode pairings that work and pairings that tank. Pulled here for fast lookup at draft time.

### Sales-friendly formats

- **Case Study (sales recommended).** Direct CTA at end ("If you want this for yourself, here's the link") OR stealth CTA woven through. The receipt in the body IS the proof; close converts the warm viewer.
- **Deep Dive (sales recommended for established creators).** Aggressive CTA at end. Viewers who finished a 60-min video are buyers. Leaving them without a path is a missed conversion.
- **Roast (sales recommended).** The fix IS the conversion ("if you want this for yourself, here's the link"). Direct CTA at end. Submission CTA also lives in close (mandatory).
- **Short Process (sales acceptable).** CTA at ~90s, middle, end. Sales page link in description.
- **Listicle (sales acceptable).** Embed CTA mid-video right after a strong point, then again in close.

### Email-friendly formats

- **Short Process (emails acceptable).** Lead magnet directly tied to video content (if step 3 is a checklist, give them the checklist). Mention 3x: early, middle, end.
- **Listicle (emails recommended).** Lead magnet related to the list (the printable cheat sheet). Mention 3x.
- **Case Study (emails acceptable).** Lead magnet tied to the methodology used. Mention 3x.
- **Deep Dive (emails acceptable).** Lead magnet is the "shortcut version" of the deep dive.
- **News (emails acceptable).** Lead magnet tied to the news ("the checklist for navigating [thing]"). Mention 2x.
- **Roast (emails acceptable).** Lead magnet: "the 7 things I look for when reviewing [thing]". Submission funnel doubles as email list.

### Views-only formats

- **News (views recommended).** NO external links in description (kills algorithm recommendations). End-screen to non-news evergreen.
- **Interview (views recommended).** NO external links in description. End-screen to a video where the CREATOR is the expert (per interview planner, host credibility doesn't transfer from guest).
- **Listicle (views recommended).** NO external links. End-screen to another listicle (binge) or related deep dive.

### Format-goal pairings to refuse

- **Interview + sales.** Interviews almost never convert. A documented case is a 300k-view interview producing zero sales. If the creator picks interview + sales, surface the warning and recommend switching to emails or views.
- **News + sales.** Viewers came for the story, not the offer. News for sales tanks. Refuse and recommend deep-dive or case-study format if sales is the goal.

---

## 2. CTA shapes by goal

### Goal = Sales

The CTA is a direct or stealth pointer to the offer. The Bridge to the next video lives alongside it.

**Direct CTA worked example:**

> "You now have everything you need to land your first 3 clients without a website. The next problem is delivery, once client three signs, the bottleneck moves. I cover the full delivery system inside [program name], link in the top of the description. And while you're deciding whether that's right for you, watch this next where I show you the methodology in action."

Pivot → Gap → Sales pitch → Bridge to next video. The sales pitch is direct, lives in the description, the next-video Bridge maintains the chain-reaction effect.

**Stealth CTA worked example:**

> "That's how the system works. The next problem most creators hit is one of the things [program name] members solve in week one. I'll show you the full system in action in this next video, watch it next."

Stealth: program name mentioned in passing, no direct pitch, the next video that walks the system is positioned as the path. Works on creators whose voice avoids hard-sell.

**Anti-pattern:**

> "If you liked this video, please consider checking out my program. The link is somewhere in the description if you want to."

Why this misses: hedge words ("please consider", "if you want to", "somewhere in"), no Bridge, no Gap. The whole close collapsed into a tentative ask.

### Goal = Emails

The CTA is a lead-magnet pointer. The lead magnet must be directly related to the video's content.

**Worked example:**

> "Those are the 7 brutal truths. The one most people miss until year three is systemization, how to capture what you've learned so it compounds. The full checklist for the 7 truths is the top link in the description. And watch this next where I walk through the systemization piece step by step."

Pivot → Gap (the "until year three" twist) → Email CTA (lead magnet that delivers the list as a takeaway) → Bridge to next video.

**The tied-to-content rule:** if the body uses a spreadsheet, the lead magnet IS the spreadsheet. If the body teaches a 7-step checklist, the lead magnet IS the checklist. Tied lead magnets convert; generic ones don't.

**Anti-pattern:**

> "If you want my free 30-day course on YouTube growth, sign up below."

Why this misses: free course is a poor lead magnet (signup rates tank, viewers know free courses gather dust). Also unrelated to the video unless the video taught a 30-day system. A simple checklist or tool tied to the video content converts far better.

### Goal = Views

No external links in description. The Bridge is the entire CTA. Goal is to convert the viewer to channel audience.

**Worked example:**

> "So that's the system. The next thing on your stack is making sure the package, title and thumbnail, pulls the right viewer in the first place. Watch this next."

Pivot → Gap → Bridge. No external links. End-screen card lands as the line is spoken.

**Anti-pattern:**

> "Like, subscribe, and check out my course. Also follow me on Instagram, Twitter, and TikTok."

Why this misses: pulls viewers off YouTube, kills algorithm recommendation. Adds links, not a single confident next-step. Viewers given five options click none.

---

## 3. Where the CTA goes inside the close

The 3-Part Formula is Pivot → Gap → Bridge. The CTA placement varies by goal:

- **Sales:** CTA goes BETWEEN Gap and Bridge (or stealth CTA woven into Gap)
- **Emails:** Lead-magnet pointer goes BETWEEN Gap and Bridge (single mention; the body already mentioned 1-2 times per format planner)
- **Views:** No CTA between Gap and Bridge. The Bridge IS the CTA.

The Bridge always lands last. It's the line that triggers the end-screen click. Don't put anything after it.

### Worked example, sales close (CTA between Gap and Bridge):

> "You now have everything you need to write a hook that stops scrolling. [PIVOT] The reason most creators still don't see retention through the body is the body itself doesn't pay off the hook's promise. [GAP] If you want the full system that handles both, the link's at the top of the description. [SALES CTA] And watch this next where I show you exactly what a body that pays off looks like. [BRIDGE]"

### Worked example, views close (no CTA, Bridge is the CTA):

> "You now have everything you need to write a hook that stops scrolling. [PIVOT] The reason most creators still don't see retention through the body is the body itself doesn't pay off the hook's promise. [GAP] Watch this next where I show you exactly what a body that pays off looks like. [BRIDGE]"

Same Pivot, same Gap, no sales CTA. Bridge does the whole job.

---

## 4. Mid-video CTA carry-through

For email-goal videos, the body has already mentioned the lead magnet 1-2 times. The close adds the third mention. For sales-goal videos, the body may have a stealth CTA woven through (per case-study and short-process planners). The close decides whether to do another stealth mention or shift to direct.

**Pattern: stealth → direct in close.** Body weaves "this is what we do in [program]" naturally during a step. Close lands a direct pitch ("if you want this for yourself, here's the link"). The stealth pre-warms; the direct close converts.

**Pattern: direct early → reinforce in close.** Body lands a direct pitch around the 90-second mark (per short-process planner). Close reinforces ("the link is still in the description, and here's the next step on your stack"). Two mentions, escalating confidence.

The skill doesn't write the body's CTA placement, that's vid-segment's job. The skill reads what the body did and aligns the close so the cumulative pattern feels designed, not stacked.

---

## 5. CTA tone calibration

Tone scales with format and creator's voice profile.

- **Roast and Deep Dive:** higher energy CTA acceptable. Audiences are warmer.
- **Case Study and Short Process:** medium energy. Direct but not loud.
- **News and Listicle:** quieter CTA. The format itself is the engagement; CTA shouldn't compete.
- **Interview:** quietest. The whole format hinges on the guest's gravitas, not the host's pitch.

The voice profile overrides the format default. A calm-voiced creator running a roast still closes calmly, the format suggests aggressive, the voice profile says "loud isn't me." Voice profile wins. Better to under-pitch in the creator's voice than over-pitch in someone else's.

---

## 6. Anti-patterns

- **Multi-goal close.** Sales pitch + lead magnet + view CTA = three signals fighting. Pick one. Refuse to draft a multi-goal close even if the creator asks for one.
- **CTA without Pivot/Gap.** "Subscribe, like, comment" with no recap or Gap is the failure mode the formula exists to prevent. Always insist on Pivot + Gap before the CTA.
- **Begging.** "If you have time", "I'd really appreciate it if", "Please consider", all hedge the close into a request. The Bridge should sound like the next step is obvious, not optional.
- **Generic next-video positioning.** "Check out this other video I made" is a bare CTA. The Bridge has to name the SPECIFIC outcome the next video delivers.
- **Mismatched goal and format.** Interview + sales, news + sales, refuse and re-route. The format planner's warnings are load-bearing, not advisory.
