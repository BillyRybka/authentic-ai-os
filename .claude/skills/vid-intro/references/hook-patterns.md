---
type: reference
scope: skill-local
loaded_by: [vid-intro]
status: active
tags: [reference, hooks, patterns]
---

# Hook Patterns

Fill-in-the-blank hook patterns plus worked examples. Used by `vid-intro` at runtime to seed candidate hooks for the 5-second opener (step 2 of the 6-part architecture in [[intro-architecture]]). Patterns are templates with `[X]` `[Y]` `[Z]` slots. Worked examples show how each pattern lands; near-misses show how it fails.

The 5 canonical hook types are defined in [[intro-architecture]]: Question, Contrarian, Statement, Fact, Credibility. Patterns below are organized by type. A creator's `voice-profile.md` field `preferred_hook_types` filters which types `vid-intro` weights heavier when generating candidates.

This is reference material for Claude to think with, not paste at the creator. `vid-intro` reads it silently, picks 2-3 candidate patterns, fills the slots from the video's brain dump, and surfaces options.

---

## Type 1. Question Hook

A question the avatar has asked themselves. Pulls them in by promising the answer. The question must be one the avatar genuinely wonders. Generic curiosity questions miss.

### Patterns

**Q-1.** Have you ever wondered why [X] [happens / doesn't work]?
- Worked: "Have you ever wondered why one of your videos pulls 100k views and the next one barely cracks 1k?" Lands because the question matches a real pain creators feel weekly.
- Worked: "Have you ever wondered why your morning workouts feel impossible while afternoon ones feel easy?" Lands for fitness avatar; specific enough to feel personal.
- Near-miss: "Have you ever wondered why people are the way they are?" Too broad. Reads as philosophical opening, not promise of an answer.

**Q-2.** Are you making this [X] mistake [right now / every day]?
- Worked: "Are you making this pricing mistake right now?" Tight, accusatory in a useful way, opens loop.
- Worked: "Are you making this resume mistake every job application?" Lands because most viewers would worry they are.
- Near-miss: "Are you making mistakes with your business?" Generic. No specificity. Reads as filler.

**Q-3.** Do you ever feel like [X] no matter how hard you [Y]?
- Worked: "Do you ever feel like your channel is stuck no matter how many videos you publish?" Names a specific pain plus a specific futile action.
- Worked: "Do you ever feel like you're broke no matter how much you earn?" Resonant with money-mindset avatar.
- Near-miss: "Do you ever feel like things just don't go your way?" Too vague to grip a specific avatar.

**Q-4.** What would you do if [improbable scenario]?
- Worked: "What would you do if your biggest client emailed you tomorrow saying they're cancelling?" Concrete enough to make the viewer simulate the answer.
- Worked: "What would you do if you woke up tomorrow and lost the ability to write?" Forces a real mental rehearsal.
- Near-miss: "What would you do if you could do anything?" Floats. No tension.

**Q-5.** Why is [X] doing [Y]?
- Worked: "Why is the entire creator economy quietly switching to LinkedIn this year?" Naming a real shift the viewer half-noticed.
- Worked: "Why is every fitness coach suddenly recommending zone 2 cardio?" Lands when the trend is real and visible.
- Near-miss: "Why is YouTube the way it is?" Too abstract; reads as rant opener.

**Q-6.** Why is nobody talking about [X]?
- Worked: "Why is nobody talking about the fact that 60% of YouTube channels die before they hit 1k subscribers?" Implies hidden truth. Lands when the stat is real.
- Worked: "Why is nobody talking about the diet that's quietly outperforming keto in long-term studies?" Curiosity gap.
- Near-miss: "Why is nobody talking about the truth?" Conspiracy-flavored without specifics. Wastes a hook.

**Q-7.** Do you struggle to [X]? Well, it's not your fault.
- Worked: "Do you struggle to keep clients past 6 months? Well, it's not your fault." Validating; opens permission to listen.
- Worked: "Do you struggle to lose the last 10 pounds? Well, it's not your fault." Removes shame, invites the lesson.
- Near-miss: "Do you struggle? Well, it's not your fault." Too generic. The pain has to be named.

**Q-8.** Can I tell you a secret?
- Worked: "Can I tell you a secret? I made $90k last year using one tool you've never heard of." Pulls the viewer into a confession frame.
- Worked: "Can I tell you a secret? Most YouTube growth advice is written by people who have never grown a channel." Implies insider POV.
- Near-miss: "Can I tell you a secret about success?" The "secret" needs a specific noun on the other side, not an abstract category.

---

## Type 2. Contrarian Hook

Goes against the grain of common advice. Pairs naturally with cognitive-dissonance thumbnails. The contrarian claim must be one the creator can defend in the body. Pure contrarianism without substance burns the hook.

### Patterns

**C-1.** I'm a [credible role] and I don't [common practice everyone in that role does].
- Worked: "I'm a multi-millionaire and I don't own my house." Real shock, sets up real reasoning.
- Worked: "I'm a fitness coach and I don't do cardio." Clean inversion of an expectation.
- Worked: "I'm a copywriter and I don't write headlines first." Trade-secret reveal.
- Near-miss: "I'm a YouTuber and I don't make videos." Comically inverted; viewer assumes joke and bounces.

**C-2.** Stop doing [common action everyone recommends] right now.
- Worked: "Stop posting on LinkedIn three times a day." Anti-frequency advice in a frequency-obsessed niche.
- Worked: "Stop drinking 8 glasses of water a day." Counter-conventional wisdom.
- Near-miss: "Stop doing things that don't work." Vague. Doesn't name what.

**C-3.** [Widely accepted idea] is completely wrong.
- Worked: "Niching down is completely wrong for new creators." Frames a popular truism as a trap.
- Worked: "The 80/20 rule is completely wrong for content." Provocative; promises argument.
- Near-miss: "Most advice is wrong." No teeth. The bigger the claim, the more specific the target needs to be.

**C-4.** You don't need [common tool / advice everyone pushes] to [outcome].
- Worked: "You don't need a niche to grow a YouTube channel past 100k subs." Inverts a sacred cow.
- Worked: "You don't need to wake up at 5 a.m. to be productive." Counter-productivity-bro angle.
- Near-miss: "You don't need anything to succeed." Too cute. Hooks need to deny a specific thing.

**C-5.** Why [popular thing in the niche] is holding you back.
- Worked: "Why morning routines are holding you back." Inverts a positive default.
- Worked: "Why your CRM is holding back your sales." Specific tool, specific harm.
- Near-miss: "Why the things you love are holding you back." No specifics. Reads as cliché.

**C-6.** Here's why [popular opinion] is wrong.
- Worked: "Here's why the 'just be authentic' advice is wrong if you're under 1k subscribers." Specific qualifier earns the contrarian claim.
- Worked: "Here's why retiring early is the worst financial advice for most people." Specific group.
- Near-miss: "Here's why everything you've been told is wrong." Hyperbole. Loses credibility.

**C-7.** Everyone says [X]. They're wrong, and here's why.
- Worked: "Everyone says batch your content. They're wrong, and here's why." Inversion of a productivity default.
- Worked: "Everyone says ditch sugar. They're wrong, and here's why." Health niche provocation.
- Near-miss: "Everyone says success is hard. They're wrong, and here's why." Truism vs truism. No edge.

---

## Type 3. Statement Hook

Strong, bold opinion delivered as fact. High conviction tone. Works when the creator can defend the statement in the body. Statement hooks demand authority; weak delivery kills them.

### Patterns

**S-1.** I have found the [X] that nobody seems to be talking about.
- Worked: "I have found the YouTube growth lever that nobody seems to be talking about." Promises insider find.
- Worked: "I have found the ad-creative format that nobody seems to be talking about." Specific niche, specific find.
- Near-miss: "I have found the secret to life nobody knows." Too grand to back up.

**S-2.** The second your video loads, [bad thing happens] and [worse outcome].
- Worked: "The second your video loads, viewers judge it, and if they don't like what they see they leave forever." Stakes named instantly.
- Worked: "The second your sales page loads, the prospect decides if you're cheap or expensive." Vivid stakes for a marketer.
- Near-miss: "The second your video loads, things start happening." No stakes. Reads as filler.

**S-3.** This one [thing] transformed my entire approach to [topic].
- Worked: "This one routine change transformed my entire approach to writing." Personal, definite, specific change.
- Worked: "This one prompt structure transformed my entire approach to AI." Tool plus topic specificity.
- Near-miss: "This one thing transformed my life." Vague "thing", vague "life", no traction.

**S-4.** You've been doing [X] wrong all along.
- Worked: "You've been doing your morning routine wrong all along." Personal accusation that hooks.
- Worked: "You've been writing emails wrong all along." Tight, specific.
- Near-miss: "You've been doing things wrong all along." Generic.

**S-5.** [Outcome] doesn't come from luck. it comes from [specific thing].
- Worked: "Wealth doesn't come from luck. It comes from boring repetitive systems most people abandon by week 3." Specific replacement.
- Worked: "Six-pack abs don't come from genetics. They come from one variable most people miscalculate." Inverts assumption.
- Near-miss: "Success doesn't come from luck. It comes from hard work." Truism. Wasted line.

**S-6.** It's time to rethink everything you know about [subject].
- Worked: "It's time to rethink everything you know about YouTube thumbnails." Specific subject; promises a rebuild.
- Worked: "It's time to rethink everything you know about cold DMs." Specific tactic.
- Near-miss: "It's time to rethink everything." No subject; reads as fortune cookie.

**S-7.** Here's a truth no one wants to admit about [X].
- Worked: "Here's a truth no one wants to admit about freelancing in 2026." Names taboo; promises honesty.
- Worked: "Here's a truth no one wants to admit about parenting in your 30s." Niche-specific taboo.
- Near-miss: "Here's a truth nobody wants to admit." Without an X, the line floats.

**S-8.** [Specific tweak] can dramatically improve your [skill / outcome].
- Worked: "Recording your hooks last can dramatically improve your retention rate." Specific tweak, specific KPI.
- Worked: "Switching your meal-prep day from Sunday to Wednesday can dramatically improve adherence." Counter-default specificity.
- Near-miss: "A small change can dramatically improve your life." Same hook everyone writes. Dead.

---

## Type 4. Fact Hook

A surprising fact. Two hard rules: it must be surprising, and it must be relevant to the video's topic. A boring fact wastes the hook. A surprising-but-irrelevant fact destroys trust within 10 seconds.

### Patterns

**F-1.** On average, [audience group] [does surprising thing] [unexpected frequency / number].
- Worked: "On average, you make 35,000 decisions per day." Surprising scale; pairs with decision-fatigue topic.
- Worked: "On average, professionals check Slack 74 times per workday." Pairs with focus/productivity content.
- Near-miss: "On average, people do many things every day." Vague. No specificity.

**F-2.** Almost [percentage] of [group] [counterintuitive trait or action].
- Worked: "Almost 80% of the world's millionaires are self-made." Pairs with wealth-building content.
- Worked: "Almost 73% of YouTubers quit before their channel earns its first dollar." Pairs with creator-resilience content.
- Near-miss: "Almost a lot of people give up." No number, no specificity.

**F-3.** Did you know that [most people] [are most likely to / least likely to] [X] on [specific time / day]?
- Worked: "Did you know you are most likely to die from a heart attack on a Monday between 8 and 9 a.m.?" Specific, surprising, sets up health-systems content.
- Worked: "Did you know your highest-converting email of the week is the Tuesday afternoon one?" Pairs with email-marketing content.
- Near-miss: "Did you know things happen at certain times?" Vague.

**F-4.** Studies show that [counterintuitive finding].
- Worked: "Studies show that people who write down their goals are 42% more likely to achieve them." Concrete number, replicable claim.
- Worked: "Studies show that creators who post once a week outperform daily posters by 3x in subscriber growth past month 6." Pairs with cadence content.
- Near-miss: "Studies show many things about success." Where? When? By whom?

**F-5.** [Percentage] of [group] are [common mistake] right now without realizing it.
- Worked: "80% of YouTubers are using thumbnails that score below 4% click-through without realizing it." Stat plus problem plus implied promise.
- Worked: "63% of dieters are tracking calories that don't actually exist." Specific niche.
- Near-miss: "Many people are doing things wrong." No stat, no group.

**F-6.** Most [audience group] don't realize this about [X].
- Worked: "Most freelancers don't realize this about pricing: the highest-paying clients are the ones who reply slowest." Specific surprising rule.
- Worked: "Most marathoners don't realize this about pacing: their fastest miles should be the last three." Counter-intuitive niche fact.
- Near-miss: "Most people don't realize things." Empty.

**F-7.** Here's a number that will change how you think about [topic]: [X].
- Worked: "Here's a number that will change how you think about YouTube: only 0.4% of channels ever cross 100k subscribers." Real stat, real frame-shift.
- Worked: "Here's a number that will change how you think about hiring: 86% of hiring managers reject resumes in under 8 seconds." Pairs with job-hunt content.
- Near-miss: "Here's a number you'll find interesting." Telegraphs the move; viewer disengages.

---

## Type 5. Credibility Hook

Lead with massive result or experience. Cold viewers distrust unknown creators, so this hook only works when the credibility is loud enough to override that distrust. Small/new channels generally underperform with this hook (viewers don't trust an unknown "I" yet): flag the risk to the creator at runtime, but allow if a single dramatic claim earns the trust.

### Patterns

**Cr-1.** I've been [doing thing] for [significant time] and [scale of result / accomplishment].
- Worked: "I've been in business for 13 years, sold 9 companies, and my last one went for 46 million." Stack of receipts that buys 30 seconds.
- Worked: "I've been writing daily for 12 years and built three businesses to seven figures off it." Time plus output plus result.
- Near-miss: "I've been doing this for a long time." No numbers. Cold viewers leave.

**Cr-2.** After [doing X] [number] times, here's what I learned.
- Worked: "After making 500 cakes over three years, here's what finally made them moist." Volume of repetition plus delivery promise.
- Worked: "After running 137 sales calls in 18 months, here's the one objection that closes deals." Specific volume, specific promise.
- Near-miss: "After doing this many times, here's what I learned." No specifics. Burns hook.

**Cr-3.** We've [done thing] on [number] [people / cases] and [result happened] every time.
- Worked: "We've used this on over 40 clients and revenue went up within 90 days every time." Sample size plus consistent result.
- Worked: "We've tested this routine on 200 clients and bedtime resistance dropped 80% every time." Specific test, specific result.
- Near-miss: "We've used this on a lot of people and it works." Hand-waving. No proof.

**Cr-4.** [Specific personal action] made me $[number] in [timeframe].
- Worked: "Fixing my thumbnail made me $90,000 in 4 months." Causal chain with hard number.
- Worked: "Switching my outreach script generated $24,000 in new revenue in 8 weeks." Specific, traceable.
- Near-miss: "Doing this made me a lot of money." Generic. No urgency to listen.

**Cr-5.** My last client went from [X] to [Y] in [timeframe].
- Worked: "My last client went from 80 hours a week to 15 in 90 days." Concrete starting state, concrete end state, real timeframe.
- Worked: "My last client went from 200 followers to 12,000 in 6 weeks." Volume plus time plus outcome.
- Near-miss: "My last client got better results." Vague. No specificity.

**Cr-6.** I [analyzed / studied] [number] [things] and here's the pattern.
- Worked: "I analyzed 500 resumes and the ones that landed jobs all had this in common." Effort signal plus pattern promise.
- Worked: "I read 247 sales pages this month and the ones that converted had three sections nobody else uses." Effort plus contrarian-feeling result.
- Near-miss: "I looked at a bunch of stuff and noticed something." No effort signal. Viewer doesn't credit it.

---

## Anti-patterns (every type)

These hooks fail across every type. Watch for them in candidates and reject.

**A-1.** Bolted-on self-introduction.
- Failed: "Hi, I'm Bob. I've been doing this for 10 years. Today we're going to talk about YouTube growth."
- Why it fails: cold viewers don't care about Bob yet. Credibility belongs woven into the moment a claim is made, not at the front. See [[intro-architecture]] step 6.

**A-2.** Generic curiosity bait.
- Failed: "You won't believe what happened next."
- Why it fails: telegraphs the move; viewer recognizes the formula and disengages.

**A-3.** Empty promise.
- Failed: "This will change everything you know about life."
- Why it fails: every category claim with no specific noun reads as filler. The viewer's brain reads "no information here, skip."

**A-4.** Surprising-but-irrelevant fact.
- Failed: "Did you know duck quacks don't echo? Anyway, today we're talking about how to lose weight."
- Why it fails: hook landed but the bridge to the topic shows zero relevance. Viewer feels manipulated.

**A-5.** Hedge in the hook.
- Failed: "Maybe you've been making a small mistake with your YouTube thumbnails."
- Why it fails: hedge ("maybe", "small") undermines stakes. Hooks earn attention through claim, not caveat.

**A-6.** Topic-label dressed as hook.
- Failed: "Today's video is about how to grow on YouTube."
- Why it fails: announces a topic. Doesn't earn attention. Topic labels are descriptions, not hooks.

**A-7.** Multi-hook stacking.
- Failed: "Have you ever wondered why YouTube is hard? Here's a fact: 80% of channels die. Stop doing what you're doing. I'll show you my system."
- Why it fails: trying to use four hooks in five seconds. Viewer can't process. Pick one.

---

## How vid-intro uses this file

At runtime, `vid-intro`:

1. Reads `voice-profile.md` `preferred_hook_types` to weight which patterns to draw from
2. Reads `Content/pieces/{slug}/brain-dump.md` (or `reference-block.md`) for the actual material
3. Picks 2-3 candidate patterns across the allowed types (filtered by format planner per [[intro-architecture]] format adaptation map)
4. Fills the slots from the video's specific material, never inventing numbers or claims
5. Surfaces candidates as a numbered list with hook-type annotation
6. Creator picks one or pushes back

Same anti-fabrication discipline as [[vid-title|the title skill]]: only use numbers and claims that appear in the brain dump or foundation docs.

---

