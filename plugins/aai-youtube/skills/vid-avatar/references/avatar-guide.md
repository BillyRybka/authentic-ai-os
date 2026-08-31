# Avatar Guide

The avatar is the specific person a creator is talking to. Every downstream artifact (titles, hooks, thumbnails, scripts, CTAs) gets validated against this avatar.

## What an avatar looks like

The avatar is a description, not a structured field list. A few sentences that capture who this person is, what stage they're at, and why the problem is urgent for them.

What downstream skills need from the avatar:

- Enough specificity to write titles, hooks, thumbnails, scripts, and CTAs to a recognizable viewer.
- The avatar's actual language, not the expert's diagnosis.
- A signal of who this isn't for (often implicit in how the creator describes who it is for).

What downstream skills don't need:

- Demographic fields filled out when they don't change writing decisions.
- Multiple paragraphs of psychographic theory.
- A label, a fit qualifier, and a context separated into pieces. Just describe the person.

If the creator gives you a paragraph that already describes the avatar, lock the paragraph. Don't restructure it. Don't decompose it into fields. The Iceberg Statement (built by `vid-positioning`) uses whatever language the creator already used.

## Top 3 perceived problems is the most important attribute

This is the one the creator will spend the most time on, and the one downstream skills will reference most. Every video idea gets pressure-tested against these three problems.

Perceived problems are what the viewer says when they complain. Not the therapist's version. Not the expert's diagnosis.

**Expert says:** "Small business owners struggle because they lack systems thinking."
**Viewer says:** "I'm drowning in emails and can't keep up."

Write the viewer's version.

## How to extract the top 3 problems

Three ways:

1. **Past client intake forms or call notes.** Look for recurring complaints. The thing you heard 5 clients say in their own words is a perceived problem.
2. **Reddit, Quora, YouTube comments in the niche.** What do people complain about unprompted?
3. **Survey the email list or community.** Ask one open question: "What's the #1 thing stopping you from [desired result]?"

Target 25-30+ responses for survey data to be meaningful. Fewer than that is educated guessing.

**Educated guessing is fine for the MVP.** Refine with real data over the next 6 months.

## How to read the examples below

The good/bad pairs that follow use a structured format (Age, Sex, Location, Type, Top 3). That structure is reference data for Claude's calibration. It is NOT the saved output format.

When you save the avatar to `foundation/avatar.md`, write it as a plain description that captures whichever of those signals actually matter for the creator's voice and writing decisions. If age range changes voice and references, mention age. If location is irrelevant, leave it out. If "type" maps to a single tight description ("first-time dads working out between feedings"), use that phrase, not seven fields.

The Top 3 perceived problems ARE saved as a list, in the avatar's exact viewer-language. Those translate one-to-one between the examples below and the saved output.

## Good vs bad: paired examples

Show the creator these pairs. The Top 3 Problems is where almost every draft drifts. The most common failure is expert-framed problems instead of viewer-spoken ones.

### Pair 1: Physiotherapy audience

**Good:**
- Age: 35-55
- Sex: Mostly female (60-65%)
- Location: English-speaking countries
- Type: Fitness-conscious professionals, runners, gym-goers who've hit an injury plateau
- Top 3 perceived problems:
  1. "My knee pain won't go away no matter what I try"
  2. "I don't want to stop running, but I'm scared of making it worse"
  3. "Every physio I see just gives me generic exercises that don't work"

Why it works:
- Age range is 20 years wide. Tight enough to inform voice and references
- Type is layered (fitness-conscious + specific activities + current state)
- Top 3 are in the viewer's exact complaint language
- Three problems are genuinely distinct (pain, fear, dissatisfaction with care), not three angles of one thing

**Bad:**
- Age: 25-65
- Sex: Both
- Location: English-speaking countries
- Type: Fitness enthusiasts
- Top 3 perceived problems:
  1. Chronic musculoskeletal dysfunction
  2. Lack of compliance with rehabilitation protocols
  3. Insufficient movement optimization

Why it fails:
- Age range of 40 years means voice/examples won't land for either end
- "Fitness enthusiasts" is broad and undifferentiated
- Top 3 are in expert/clinician language. Viewers don't complain in those words
- "Chronic musculoskeletal dysfunction" is one umbrella; the three entries are really aspects of that same thing

### Pair 2: Solo founder audience

**Good:**
- Age: 28-42
- Sex: Both (slightly more male)
- Location: English-speaking
- Type: Solo founders running service businesses doing $200k-$2M/year
- Top 3 perceived problems:
  1. "I'm the bottleneck in every process"
  2. "Hiring people hasn't made things easier, it's made it worse"
  3. "I built the business I hate"

Why it works:
- Type has stage markers (solo, service, revenue band). Signals exactly who it isn't (not employees, not agencies, not $10M+)
- Top 3 are what the viewer would actually say out loud to a friend
- Problems are three actually-different ones (time/workflow, team/hiring, identity/satisfaction), not three angles of the same thing

**Bad:**
- Age: 25-55
- Sex: Both
- Location: Worldwide
- Type: Entrepreneurs
- Top 3 perceived problems:
  1. Scaling issues
  2. Operational inefficiency
  3. Leadership development

Why it fails:
- "Entrepreneurs" includes tech founders, Etsy sellers, franchise owners, solopreneurs, Fortune 500 CMOs
- Top 3 are MBA textbook categories, not human complaints
- Viewer would never Google "operational inefficiency". They'd search "why can't I get through my inbox"

### Pair 3: New-dad fitness audience

**Good:**
- Age: 28-40
- Sex: Male
- Location: US + UK
- Type: First-time or early-stage dads who worked out consistently pre-kids, now fitting it in between feedings and sleep deprivation
- Top 3 perceived problems:
  1. "I don't have an hour for the gym anymore"
  2. "My back hurts all the time from carrying the baby"
  3. "I'm watching myself get soft and I can feel my energy tanking"

Why it works:
- Type captures the before/after transition, the trigger that changed their life
- Problems are concrete moments (the gym, the back, the mirror), not abstractions
- Time, body, energy. Three separate problems

**Bad:**
- Age: 25-45
- Sex: Male
- Location: Global
- Type: Busy men
- Top 3 perceived problems:
  1. Time management issues
  2. Declining physical health
  3. Low motivation

Why it fails:
- "Busy men" is 80% of adult men. No trigger, no life stage.
- "Time management issues" could mean anything from missing meetings to never exercising
- "Low motivation" is a symptom, not a problem the viewer complains about directly

### Pair 4: Narcissistic-relationships audience

**Good:**
- Age: 25-45
- Sex: Women
- Location: English-speaking
- Type: Ambitious but recovering. Dating, or stuck in toxic relationships
- Top 3 perceived problems:
  1. "I keep attracting the wrong men"
  2. "I can't trust myself anymore"
  3. "I don't know how to spot the red flags"

Why it works:
- Type pairs an identity ("ambitious") with a current state ("recovering"). Captures the self-image gap
- Problems are spoken in the voice of someone telling a friend over coffee, not a therapist's intake form
- Three actually-different problems (pattern-matching, self-trust, pattern-spotting), not three angles of one issue

**Bad:**
- Age: 18-65
- Sex: Both
- Location: Worldwide
- Type: People in relationships
- Top 3 perceived problems:
  1. Communication issues
  2. Emotional dysregulation
  3. Unhealthy relationship dynamics

Why it fails:
- "People in relationships" includes everyone from teens to retirees with completely different problems
- "Emotional dysregulation" is a clinician's phrase. Viewers complain in stories, not diagnoses
- The three are all aspects of one umbrella ("my relationship is hard"), not distinct problems

### Pair 5: Busy-professional weight-loss audience

**Good:**
- Age: 32-48
- Sex: Both (slightly more female)
- Location: US + UK + Canada + Australia
- Type: Professionals who used to be in shape, now 15-30 pounds heavier after a decade of work travel, takeout dinners, and skipped workouts
- Top 3 perceived problems:
  1. "Every diet I try fails by week three"
  2. "I don't have time for long workouts"
  3. "I can lose 5 pounds and gain 8 back the second I stop"

Why it works:
- Type names the trigger arc (used to be in shape, now 15-30 lbs heavier) so the viewer recognizes themselves
- Problems are about the failure pattern (not the desired result). That's where viewers actually live
- Three different failure modes: diet attrition, time scarcity, yo-yo cycle

**Bad:**
- Age: 25-55
- Sex: Both
- Location: Global
- Type: Adults who want to lose weight
- Top 3 perceived problems:
  1. Slow metabolism
  2. Lack of willpower
  3. Poor diet choices

Why it fails:
- "Adults who want to lose weight" is the entire fitness niche
- "Slow metabolism" is a self-blame story, not the problem they complain about ("I tried keto and it didn't stick")
- "Lack of willpower" and "poor diet choices" are framed as the viewer's fault. They don't say that out loud

### Pair 6: Course-creator-from-freelancer audience

**Good:**
- Age: 28-45
- Sex: Both
- Location: English-speaking
- Type: Freelancers (designers, copywriters, consultants) doing $80k-$200k/year, fully booked, can't take on more clients without breaking
- Top 3 perceived problems:
  1. "If I stop working for a week, I stop earning"
  2. "I keep saying no to good clients because I'm at capacity"
  3. "I've been told to make a course for years but I have no idea where to start"

Why it works:
- Type has a profession band, a revenue band, and a constraint signal (fully booked)
- Problems are spoken in the actual reasoning the viewer has at the kitchen table on a Sunday night
- Income, capacity, inertia. Three different blocks, not one problem with three names

**Bad:**
- Age: 22-60
- Sex: Both
- Location: Worldwide
- Type: Online business owners
- Top 3 perceived problems:
  1. Scaling challenges
  2. Time management
  3. Course creation

Why it fails:
- "Online business owners" includes dropshippers, course creators, agencies, freelancers. Totally different operating models
- "Course creation" is a topic, not a problem
- These are MBA categories, not human complaints

### Pair 7: Investing-for-retirement audience

**Good:**
- Age: 35-50
- Sex: Mostly female
- Location: US + Canada + UK
- Type: Mid-career professionals who started saving late, watched friends retire and panicked
- Top 3 perceived problems:
  1. "I started too late and I'm scared the math doesn't work anymore"
  2. "Every finance YouTuber is a 25-year-old crypto bro and I can't relate to any of them"
  3. "My 401k is invested in something but I have no idea what or whether it's any good"

Why it works:
- Type names the trigger event (watched friends retire), the emotional entry point
- Problems include a meta-problem about the niche itself (can't find content that fits them). That's a real viewer complaint
- Math fear, representation gap, opacity. Three real failure modes

**Bad:**
- Age: 25-65
- Sex: Both
- Location: Global
- Type: Investors
- Top 3 perceived problems:
  1. Asset allocation optimization
  2. Tax efficiency
  3. Portfolio diversification

Why it fails:
- "Investors" includes day traders, retirees, crypto bros, indexers. Completely different mindsets
- All three problems are CFP-curriculum phrases. Viewers say "I don't know if my 401k is doing anything"
- Three angles of one umbrella ("am I invested correctly?"), not three problems

### Pair 8: Solo founder audience (additional)

**Good:**
- Age: 30-45
- Sex: Both
- Location: English-speaking
- Type: Service-business owners doing $300k-$1M/year, running everything themselves, working 60+ hour weeks
- Top 3 perceived problems:
  1. "I'm drowning in emails and can't keep up"
  2. "I keep forgetting things. Clients are noticing"
  3. "Every system I try takes more time to set up than it saves"

Why it works:
- Type stacks profession + revenue band + workload signal. Paints a precise person
- Problems are concrete moments (the inbox, the dropped ball, the failed automation)
- Each problem maps to a different content axis (workflow, memory, systems)

**Bad:**
- Age: 25-55
- Sex: Both
- Location: Worldwide
- Type: Small business owners
- Top 3 perceived problems:
  1. Productivity issues
  2. Workflow optimization
  3. Strategic planning

Why it fails:
- "Small business owners" includes e-commerce, agencies, brick-and-mortar, freelancers
- "Productivity issues" is a vague header for hundreds of different problems
- The third one is a category, not a complaint. No viewer says "I have strategic planning problems"

Notice the pattern: the viewer's exact language wins. If the creator wrote it, it's probably expert-framed. Pull from real complaints, client intake, comments, Reddit, surveys.

## Bank: viewer-voice problem language by niche

When auditing a draft, sanity-check against this bank. If the creator's Top 3 problems read like the **left** column, send them back. If they read like the **right** column, they're locked.

**Fitness / weight loss:**
- Expert: "Caloric deficit non-compliance" / Viewer: "Every diet I try fails by week three"
- Expert: "Inadequate progressive overload" / Viewer: "I'm working out and seeing nothing happen"
- Expert: "Time-constrained training adherence" / Viewer: "I don't have time for long workouts"
- Expert: "Metabolic adaptation" / Viewer: "I can lose 5 pounds and gain 8 back the second I stop"
- Expert: "Postural compensation patterns" / Viewer: "My back hurts all the time from carrying the baby"

**Business / freelancing:**
- Expert: "Scaling bottlenecks" / Viewer: "I'm the bottleneck in every process"
- Expert: "Hiring inefficiency" / Viewer: "Hiring people hasn't made things easier, it's made it worse"
- Expert: "Founder identity misalignment" / Viewer: "I built the business I hate"
- Expert: "Capacity constraint" / Viewer: "If I stop working for a week, I stop earning"
- Expert: "Operational inefficiency" / Viewer: "I'm drowning in emails and can't keep up"
- Expert: "Process documentation gap" / Viewer: "I keep forgetting things. Clients are noticing"

**Relationships:**
- Expert: "Pattern recognition deficits" / Viewer: "I keep attracting the wrong men"
- Expert: "Compromised self-trust" / Viewer: "I can't trust myself anymore"
- Expert: "Limited red-flag literacy" / Viewer: "I don't know how to spot the red flags"

**Physiotherapy / injury:**
- Expert: "Chronic musculoskeletal dysfunction" / Viewer: "My knee pain won't go away no matter what I try"
- Expert: "Activity modification resistance" / Viewer: "I don't want to stop running, but I'm scared of making it worse"
- Expert: "Generic protocol limitations" / Viewer: "Every physio I see just gives me generic exercises that don't work"

**Investing / retirement:**
- Expert: "Late-stage compounding catch-up" / Viewer: "I started too late and I'm scared the math doesn't work anymore"
- Expert: "Demographic content mismatch" / Viewer: "Every finance YouTuber is a 25-year-old crypto bro and I can't relate"
- Expert: "Portfolio opacity" / Viewer: "My 401k is invested in something but I have no idea what"

**Course creation / digital products:**
- Expert: "Productization friction" / Viewer: "I've been told to make a course for years but I have no idea where to start"
- Expert: "Capacity utilization at peak" / Viewer: "I keep saying no to good clients because I'm at capacity"
- Expert: "Recurring revenue infrastructure" / Viewer: "If I take a week off, my income goes to zero"

## How to use the avatar downstream

The Top 3 is positioning. It decides the lane and the kind of problems the channel keeps solving. It earns its keep at three moments: picking what to make (the ideas step), locking once that a video fits the lane (intake), and the ending, where you bridge to your most logical next video (which sets up the next of those problems).

It is NOT a filter that every title, hook, thumbnail, script, and CTA has to pass. Front-loading the Top 3 into every writing step is how originality dies. Everything starts bending toward the same three pains. Between the lane lock and the ending, the writing runs on the creator's actual material and the per-video viewer questions.

That's why the top 3 has to be locked early and changed only when there's strong reason.

## If the creator has multiple audiences

Pick one. The foundation is built for ONE avatar. If the creator genuinely serves multiple, ask them to pick the most profitable or highest-potential one for the channel. Run foundation separately later for other audiences.

Channels that serve 3 avatars at once never build with any of them. This is the "only 1 in 4 videos lands" problem.

## Validation against positioning

Once the avatar is locked, read the positioning statement back against it:

*"I help [this specific Person] [achieve this result] by [solving this problem]."*

If the Person in the statement doesn't match the avatar, one of them is wrong. Usually the positioning statement needs tightening.

## Common mistakes

- "Busy professionals" (too broad. What industry? what level?)
- "People who want to be healthy" (too broad. How? why haven't they been?)
- "Entrepreneurs" / "Creators" / "Investors" / "Service providers": single-word categories that span ten different operating models
- "Adults who want to lose weight" / "People in relationships" / "Online business owners": too general to inform a single video
- Top 3 problems that are actually one problem with three angles (e.g., "communication issues / emotional dysregulation / unhealthy relationship dynamics" = all "my relationship is hard")
- Top 3 problems that the viewer wouldn't say out loud (expert-framed: "operational inefficiency," "metabolic adaptation," "asset allocation optimization")
- Top 3 problems that are categories rather than complaints ("strategic planning," "course creation," "communication")
- Top 3 problems that are symptoms ("low motivation," "lack of willpower") rather than the situation the viewer complains about
- Top 3 problems framed as the viewer's fault ("poor diet choices," "lack of discipline"). Viewers don't blame themselves out loud
- Top 3 problems that diagnose root cause ("you lack systems thinking") instead of capturing what the viewer actually says ("I'm drowning in emails")
- Inventing the avatar from theory rather than pulling from real humans
