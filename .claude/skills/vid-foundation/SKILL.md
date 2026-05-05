---
name: vid-foundation
description: One-time creator setup for the YouTube Content OS. Walks a YouTube business owner through positioning, avatar, credibility, backstory, voice profile, and packaging system to produce the foundational documents every downstream skill loads. Use this whenever a creator is new to the system, is pivoting positioning, or needs to refresh their foundation. Triggers on "set up my channel", "I'm starting a new channel", "build my creator foundation", "create positioning", "define my avatar", "set up YouTube Content OS", or when any other vid- skill tries to run without foundation docs in place.
---

# Video Foundation

One-time setup that produces the three documents every other YouTube Content OS skill loads. Without these docs, downstream skills (ideation, scripting, packaging, measurement) have no creator context to work against.

**At session start, load `knowledge/vault-integration.md`.** It defines the frontmatter schema, wikilink contracts, tag conventions, file naming rules, and callout patterns that every entry this skill produces must match. Non-negotiable — it's the contract that makes downstream skills find and link entries correctly.

## What this produces

Two documents in the creator's workspace:

1. **`foundation/creator-foundation.md`** — positioning statement, avatar (top 3 problems), credibility brags, backstory (Problem-Action-Outcome)
2. **`foundation/packaging-system.md`** — Gift Framework commitment, BENS title bank orientation, thumbnail strategy test plan, 3+1 format rotation pick

Plus folder structure for banks and per-video content.

**Voice profile is NOT produced here.** It has its own dedicated skill (`vid-voice-capture`) because the canonical schema has two layers (cross-context patterns + per-format context maps) and the extraction is too load-bearing to fit inside this walkthrough. Stage 5 is a handoff that tells the creator to run `vid-voice-capture` next.

## When to run this

- First time a creator is using the YouTube Content OS
- Creator is pivoting their channel's positioning
- Six months have passed and it's time to refresh voice profile
- A downstream skill reports foundation docs missing

## Folder structure this creates

At the repo/project root the skill is run from:

```
foundation/
  creator-foundation.md
  voice-profile.md
  packaging-system.md
banks/
  story-bank/          (README ships with template)
  proof-bank/          (README ships with template — creator's own evidence)
    assets/            (screenshots, charts, video clips referenced by proof entries)
  testimonial-bank/    (README ships with template — other people's words about the creator)
  metaphor-bank/       (README ships with template)
  framework-bank/      (README ships with template — creator's OWN named frameworks)
Content/
  pieces/
```

If any of these already exist, leave them alone. Do NOT overwrite banks, READMEs, or pieces folders. The bank READMEs ship with the product template — the skill does not need to regenerate them. If a README is missing, flag it and ask whether to regenerate rather than silently creating one.

## The walkthrough (6 stages, sequential)

**This skill is a conversation, not a document.** Hard rules for every stage:

- Keep messages SHORT. 3-5 lines is usually right. Never dump multiple paragraphs upfront.
- The reference file is for CLAUDE to think with — NOT to paste at the creator. Use it to judge their draft silently. Only quote from it when comparison actively helps the creator fix something.
- Do not pre-teach. Do not lecture. Do not list all the good/bad pairs before the creator has answered anything. The pairs are ammunition you pull ONE at a time when a draft needs correction.
- Ask one or two focused questions. Wait. React.

### The per-stage flow

1. **CHECK silently** for the relevant file/section at its known path. Silent file read, no announcement.
   - If it exists → surface the first line or two and ask: "Want to refresh, keep, or replace?"
   - If nothing exists → go straight into the work. Do not ask "do you want to start fresh."
2. **Open briefly** — one or two lines of context, in the creator's language. What we're building, why it matters, the formula or prompt. Not a mini-essay.
3. **Ask the core question(s).** One or two, short, direct. Then stop and wait.
4. **Load the reference in your head** (not into the chat). Use it to judge what the creator sends back.
5. **React conversationally.**
   - Strong answer → confirm, refine one detail if needed, move toward locking it.
   - Weak answer → push back specifically. If comparison helps, pull ONE good/bad pair from the reference that directly maps to their weakness. Never dump more than one.
6. **Iterate in short exchanges** until it's specific and differentiated.
7. **Approve + save** to the right file.
8. **STOP.** Do not preview the next stage. Say the save happened, ask if they're ready to continue.

Do not batch stages. The existence check is a silent `Read`, not a vault scan — you're looking at ONE known path.

### Stage 1: Positioning

**Silent check:** read `foundation/creator-foundation.md` if it exists. Positioning section exists → surface it and ask refresh/keep/replace. Otherwise proceed.

**Load** `references/positioning-framework.md` for your own use. Do not paste it into chat.

**Brief opener:**

> "Starting with positioning — one sentence that tells a viewer who you help and what problem you solve. Four quick questions to get there. Don't overthink — first instincts are usually right."

Then ask Q1. One at a time. Wait for each answer before moving on.

---

**Q1: Name one real person.**

Ask:
> "Think of ONE real person you've helped (or watched someone like you help). Client, past colleague, a viewer who wrote you — or yourself three years ago. What's their name, and what do they do day-to-day?"

Probe if vague:
> "Walk me through their week. What's on their calendar, what's their revenue, how big is their team? I need one specific human, not a segment."

Offer if stuck:
> "Doesn't matter if it's a current or past client. Goal is specificity. 'Business owners' is too abstract; 'Sarah, solo consultant, $150k/year, working from her kitchen table' is right."

---

**Q2: What were they stuck on — in their words?**

Ask:
> "What did [Q1's person] say the problem was? Not your diagnosis — the actual phrase they used when they vented."

Probe if vague:
> "When they described it, were they saying 'I'm overwhelmed' or 'I'm the bottleneck' or 'nothing works without me'? Pull the exact language if you can."

If too broad ("struggling with growth"):
> "That's the category. What specifically was blocking them — a person, a habit, a missing system, a decision?"

---

**Q3: What did they get out of it?**

Ask:
> "After it worked — what changed? Numbers, timeframe, a moment that told you it landed."

Probe:
> "Is there a number? Revenue change, hours saved, how fast? Something you'd put on a testimonial."

If vague ("they felt better"):
> "Better how? Give me a before/after a stranger would believe."

---

**Q4: What axis does your niche compete on — that you deliberately ignore?**

Ask:
> "In your niche, what do most people compete on? Speed, price, ease, credentials, aesthetics? Which one do you refuse to play on — and what do you own instead?"

Probe if blank:
> "Volvo doesn't compete on horsepower; they own safety. Red Bull doesn't compete on taste; they own energy. What's your lane nobody else is willing to take?"

If generic ("quality"):
> "Everyone says quality. What's the unusual, harder, or less sexy axis you're willing to own?"

If the creator truly doesn't know their niche yet: don't grind. Note it and move on — we can sharpen on the second pass.

---

**Synthesis.**

Draft the statement:

> *"I help [Person from Q1] [result from Q3] by [solving Q2's problem]."*

Read it back. Ask: "Does that land, or does it need a word swap?"

Iterate 2-3 passes. If after iteration the statement still sounds like every other creator in the niche, fire the **stretch probe**:

> "If someone showed up wanting [adjacent thing], who would you tell them to go to instead? Sharpen by exclusion — who is this NOT for?"

Use their exclusion answer to re-tighten the Person or Problem.

**Professional edge case.** If the creator never had the viewer's problem (doctor, physio, consultant), swap "you" for "a real client" in Q1-Q3 — real problem, real actions, real outcome. Attribute clearly. Never fabricate.

**Only pull a good/bad pair from `references/positioning-framework.md` if the creator is stuck on what "specific" actually looks like.** One pair, not four. Frame it as "here's a version that almost works next to one that does."

**Approve + save** to `foundation/creator-foundation.md` as the Positioning section (final lock after Stage 2).

**STOP.** Say: "Positioning saved. Ready for the avatar?" Wait.

### Stage 2: Avatar

**Silent check** `foundation/creator-foundation.md` for an Avatar section. Exists → refresh/keep/replace.

**Load** `references/avatar-guide.md` for your own use.

**Brief opener:**

> "Now the avatar. Five attributes, but the three core problems do the heavy lifting — they drive every future video. 5 quick questions."

---

**Q1: Data source or memory?**

Ask:
> "Do you have client intake notes, survey responses, YouTube comments, or Reddit threads I can pull real language from? Or are we working from memory?"

If they point to data → ask for it, extract from there. If memory only → flag it: "MVP's fine on guesses; we'll refine once videos publish."

---

**Q2: Picture ONE real viewer.**

Ask:
> "Picture ONE specific person who'd watch you. Age, what they do, life situation. Not a segment — one human."

Probe if they give a segment:
> "Who's the single person you thought of first? Narrow to them."

---

**Q3: Their #1 complaint — in their words.**

Ask:
> "What's the #1 thing [Q2's person] would vent about over a beer? The exact sentence, their words."

Push back on expert language:
> "'They lack systems thinking' is the diagnosis. What would THEY say out loud? More like 'I'm drowning in emails' or 'I keep forgetting things.'"

---

**Q4: Complaint #2 — different domain.**

Ask:
> "A second complaint — ideally in a different area. If #1 was time-related, #2 might be team-related, money-related, or identity-related. What else do they vent about?"

If it's the same problem in different words:
> "That still sounds like a variation of #1. What's genuinely separate?"

---

**Q5: Complaint #3 — sanity check.**

Ask:
> "One more. And then the sanity check: are #1, #2, #3 actually three distinct problems, or are they three flavors of one thing?"

If they're three flavors of one → keep the strongest and dig for two more in other domains.

---

**Synthesis.**

Assemble avatar:
- Age range (8-15 year span, not "18-60")
- Sex
- Location
- Type (job title / life role / lifestyle label)
- Top 3 (in their language, three distinct domains)

Read it back. Re-verify the Positioning statement from Stage 1 against the avatar. If the Person in the statement doesn't match → tighten the statement now.

**Only pull a good/bad pair from `references/avatar-guide.md` if they're stuck.** One pair.

**Approve + save** to `foundation/creator-foundation.md`.

**STOP.** Say: "Avatar locked, positioning re-verified. Ready for credibility brags?" Wait.

---

### Stage 3: Credibility brags

**Silent check** for a Credibility section. Exists → refresh/keep/replace.

**Load** `references/credibility-brags-guide.md` for your own use.

**Brief opener:**

> "Three credibility brags for your intros. Specific wins your viewer cares about — not years, not credentials. Three questions."

---

**Q1: Your biggest personal result.**

Ask:
> "What's the biggest result you've personally achieved that the avatar wants? Number + timeframe."

Push back on years or credentials:
> "'10 years of experience' tells me nothing. What did 10 years PRODUCE? A number."

---

**Q2: Your most impressive client win.**

Ask:
> "Most impressive client win you can cite with real numbers. Name (if allowed), before/after, how long."

Push back on vague scale:
> "'I've helped many businesses' = I can't use that. How many specifically? What was the result for the best one?"

---

**Q3: Your volume number.**

Ask:
> "Volume. How many clients, how many dollars, how many cases? Specific integer."

Push back on hedges:
> "Declarative past tense — 'I built, I served, I made.' Not 'I've been working on building.'"

---

**Synthesis.**

Draft three brag sentences. Each one: Big + Specific + Personal.

Check for anti-proof framing — if a brag makes the creator the source of failure (e.g. "I've built systems for 50 businesses, and the #1 reason those systems fail..."), hard push back. Reframe to "the #1 mistake business owners make before they come to me..."

If the creator genuinely doesn't have big numbers yet, fall back to: consumption ("read 300 books on..."), transformation ("went from X to Y myself"), or education ("spent 2 years studying..."). Flag as weaker; real results will replace these.

**Approve + save** as the Credibility section.

**STOP.** Say: "Three brags locked. Ready for the backstory?" Wait.

---

### Stage 4: Backstory

**Silent check** for a Backstory section. Exists → refresh/keep/replace.

**Load** `references/backstory-structure.md` for your own use.

**Brief opener:**

> "Backstory — 1-2 paragraphs: the journey from the viewer's problem to their outcome. Problem → Action → Outcome. Four questions to build it."

---

**Q1: Starting state.**

Ask:
> "Before things changed — what was the state? Numbers, what a bad week looked like, what specifically was broken."

Push back on vague struggle:
> "'I struggled for years' doesn't land. What did a bad Tuesday look like? What were the numbers at your lowest point?"

---

**Q2: The trigger.**

Ask:
> "What was the specific moment or realization that made you change direction? Not 'I decided to improve' — the actual trigger."

---

**Q3: The moves.**

Ask:
> "What did you STOP doing and START doing? List the concrete moves — not the summary. What did you stop? What did you replace it with? What did you try first that didn't work?"

This is the #1 place backstories fail. Push back hard:
> "'I built a system' is a summary. Someone reading this doesn't know what you actually did. What did you document? Who did you hire first? What ritual did you install? What did you remove from your calendar?"

Run the Action-test:
> "Read your action list out loud. Could someone else do what you did from what's written? If not, keep drilling."

---

**Q4: The outcome.**

Ask:
> "Outcome. Real numbers, real timeframe, what's different now."

Push back on vagueness:
> "'Now I help others' isn't an outcome. What changed for YOU? Subscribers, revenue, time, weight, relationships — something measurable."

---

**Synthesis.**

Assemble 1-2 paragraphs. Conversational tone. Contractions OK. No corporate jargon — if you see "leveraged" or "proprietary methodology," push back: "Say it like you're telling a friend."

If the creator never had the viewer's problem, swap "I" for a real client — attribute clearly. Never fabricate.

**Approve + save** the full `foundation/creator-foundation.md` now — Positioning + Avatar + Credibility + Backstory. Use `assets/creator-foundation-template.md`.

**STOP.** Say: "creator-foundation.md locked. Ready for voice profile?" Wait.

---

### Stage 5: Voice profile (handoff to vid-voice-capture)

Voice profile is its own dedicated skill — `vid-voice-capture` — because the canonical schema has two layers (cross-context patterns + per-format context maps) and benefits from a deeper extraction pass than vid-foundation has room for. Doing a thin version here would produce a partial doc that downstream writing skills can't load cleanly.

**Silent check** for `foundation/voice-profile.md`. If it already exists, surface the first line and ask refresh/keep/replace — but the refresh path still routes through vid-voice-capture.

**What to say to the creator:**

> "Voice profile is a dedicated skill (`vid-voice-capture`) because it's the most load-bearing doc downstream — every script depends on it. It needs 2-3 transcripts, past writing, or a 10-minute live riff to do it justice. After this stage we'll lock packaging, then you'll run `vid-voice-capture` separately. That keeps each session focused and produces a profile that every writing skill can load without surprises."

**Do NOT extract voice here.** Do not write to `foundation/voice-profile.md` from this skill. The creator runs vid-voice-capture as the next step after vid-foundation finishes.

**STOP.** Say: "Got it — voice profile gets its own session via `vid-voice-capture` after we wrap. Last stage is packaging — six quick sub-steps. Ready?" Wait.

### Stage 6: Packaging system

**Silent check** for `foundation/packaging-system.md`. Exists → refresh/keep/replace (sub-section or whole).

Six sub-stages. Run one at a time. Each sub-stage: brief opener, one or two questions, react, iterate. Load the knowledge ref only when you reach that sub-stage. Don't dump the knowledge ref into chat.

**6a: Gift Framework.** Load `knowledge/gift-framework.md`. Ask in plain language:

> "Three things about your avatar: their favorite thumbnail style, their favorite video format, and the kind of content they keep coming back for (systems, tactics, stories, frameworks). If you have competitor videos or thumbnails you admire, share them and we'll reverse-engineer."

Push back on vague answers ("professional-looking" → which specific strategy?).

**6b: Format rotation (3+1).** Load `knowledge/format-rotation-guide.md`. Ask:

> "Pick 3 proven formats to rotate plus 1 experimental slot. The seven options are Short Process, Case Study, Roast, Deep Dive, Interview, News, Listicle. Which three fit your avatar best?"

Push back if picks don't match the avatar. News-fit vs Tutorial-fit vs Story-fit.

**6c: Title Bank orientation.** Load `knowledge/BENS-framework.md`. The workspace already has `banks/title-bank.md` with validated patterns. Brief orientation only — walk them through Big / Easy / New / Safe in one or two sentences each and point them at the bank. No draft needed at this stage.

**6d: Thumbnail strategy.** Load `knowledge/thumbnail-strategy-menu.md`. Ask:

> "Pick 2 thumbnail strategies to test first. Cognitive Dissonance is a strong default. Commit to 2+ videos per strategy before judging."

If they have past thumbnails, use that data to inform.

**6e: Design guardrails.** Short: color palette (2-3 max), font, hero element (face/object/text), expression rules, text limit (4-5 words max). If brand style guide exists, pull from it.

**6f: Creation path.** Pick one: Photoshop/DIY, AI workflow, Batch-shoot photos, Outsource.

**Approve + save** `foundation/packaging-system.md` using `assets/packaging-system-template.md`.

**STOP.** Say: "Packaging system locked. All six stages complete." Then wrap up.

## Wrap up

After all 6 stages:
1. Confirm `foundation/creator-foundation.md` and `foundation/packaging-system.md` both exist
2. Confirm banks folders exist (empty is fine)
3. Report to creator: "Foundation complete. Next steps in order: (a) run `vid-voice-capture` to build the voice profile — that doc is load-bearing for every script, give it a real session. (b) Run `vid-capture` anytime you have a story or proof point. (c) When ready to make a video, run `vid-pipeline`."

## Principles

- **Conversation, not document.** Every stage runs like a 15-minute coaching conversation — sharp questions, short messages, one exchange at a time. The reference files are ammunition for Claude, not handouts for the creator.
- **Stay close to the framework.** Reference files are proven. Use them to judge what the creator sends back, not to lecture.
- **Specificity or nothing.** Push back whenever an answer is vague, generic, hedged, or in expert language rather than viewer language. Weak work at any stage corrupts every downstream doc.
- **Creator drives, Claude structures.** Claude extracts and organizes. Claude does not generate positioning, avatar, brags, or backstory FOR the creator.
- **MVP principle.** First version will need refinement after real videos publish. Don't grind for perfection — lock the best the creator can articulate today.

## Reference index

**Skill-local** (setup guides for the foundation docs, live in `references/`):

| Stage | Reference | Why |
|-------|-----------|-----|
| 1 | `references/positioning-framework.md` | Person → Problem → Positioning model + examples |
| 2 | `references/avatar-guide.md` | Avatar definition, top 3 problems extraction |
| 3 | `references/credibility-brags-guide.md` | How to extract viewer-relevant wins |
| 4 | `references/backstory-structure.md` | Problem-Action-Outcome format with examples |
| 5 | (handoff to `vid-voice-capture` — no local reference) | Voice profile is its own skill |

**Shared** (concepts used by multiple skills, live in `knowledge/`):

| Stage | Reference | Why |
|-------|-----------|-----|
| 6a | `gift-framework.md` | Packaging philosophy (wrapping, box, gift) |
| 6b | `format-rotation-guide.md` | Rule of 3+1 + the 7 formats |
| 6c | `BENS-framework.md` | Title system (Big/Easy/New/Safe) |
| 6d | `thumbnail-strategy-menu.md` | The 6 strategies + when to use each |

Templates live in `assets/`:
- `creator-foundation-template.md`
- `packaging-system-template.md`

Voice profile template lives in `vid-voice-capture/assets/voice-profile-template.md` (canonical, two-layer).
