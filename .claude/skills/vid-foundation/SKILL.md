---
name: vid-foundation
description: One-time creator setup for Authentic AI OS. Walks a creator-business owner through positioning, avatar, credibility, backstory, packaging system, title-bank setup, and the handoff to voice capture. Use this whenever a creator is new to the system, is pivoting positioning, or needs to refresh their foundation. Triggers on "set up my channel", "I'm starting a new channel", "build my creator foundation", "create positioning", "define my avatar", "set up Authentic AI OS", or when any other vid- skill tries to run without foundation docs in place.
---

# Video Foundation

One-time setup for creator foundation and packaging. It creates the Authentic AI OS files downstream skills need for positioning and packaging decisions, then sends the creator to `vid-voice-capture` for the one full voice-profile build.

**At session start, load two files:**

1. `knowledge/vault-integration.md`. Frontmatter schema, wikilink contracts, tag conventions, file naming, callout patterns. Non-negotiable. This is the contract that lets downstream skills find and link entries.
2. `foundation/voice-profile.md`, IF it exists. Its anti-patterns and recurring phrases override default writing. If it's missing, the hard voice rules below are the floor.

## Voice rules (hard, override default writing)

These apply to every word this skill writes. Drafts, summaries, sharpening attempts, anything the creator sees.

- **No em-dashes. Ever.** Use periods, commas, or line breaks. Em-dashes are an AI tell.
- **Declarative. No hedging.** Cut "kind of," "sort of," "I think," "maybe," "tends to."
- **No contrast or comparison templates.** Sentences like "X. I'm already running the first one." force a shape that isn't the creator's voice. Don't invent that shape unsolicited.
- **Use the creator's exact words.** When the creator gives you words, sharpen by cutting filler ONLY. Don't reinterpret. Don't switch perspective (third to first person, "they" to "I"). Don't rearrange to fit a template. Their words ARE the brand.
- **Plain beats clever.** Do not invent labels like "doom loop," "trust killer," "wedge," "business gets loud," or "audience can smell it" unless the creator used those words first. Use the creator's phrasing or boring domain words like time, money, trust, consistency, revenue, clients.
- **Pre-output scan.** Before every message to the creator, silently scan for em-dashes, clever labels, generic AI phrases, invented metaphors, and over-polished marketing language. Rewrite before sending.

If `foundation/voice-profile.md` is loaded, its rules and anti-patterns beat these defaults.

## What this produces

Core docs in the creator's workspace:

1. **`foundation/creator-foundation.md`**: the iceberg (Iceberg Statement + bottom subtopics), Person, Top 3 perceived problems, credibility brags, backstory (Problem-Action-Outcome).
2. **`foundation/packaging-system.md`**: Gift Framework defaults, BENS title bank orientation, thumbnail strategy test plan, 3+1 format rotation pick.
3. **`banks/title-bank.md`**: seeded once from `assets/title-bank-seed.md` if missing. Never overwrite an existing creator-owned title bank.

Plus folder structure for banks and per-video content.

**Voice profile is NOT produced here.** It has one owner: `vid-voice-capture`. This skill finishes the foundation and packaging first, then the final stage sends the creator into one full voice-profile run with real source material.

## When to run this

- First time a creator uses Authentic AI OS
- Creator is pivoting their channel's positioning
- Creator needs to refresh their creator foundation or packaging system
- A downstream skill says foundation docs are missing

## Folder structure this creates

At the repo or project root the skill runs from:

```
foundation/
  creator-foundation.md
  voice-profile.md   (NOT produced here. vid-voice-capture writes this)
  packaging-system.md
banks/
  title-bank.md        (seeded once from assets/title-bank-seed.md if missing)
  story-bank/          (README ships with template)
  proof-bank/          (README ships with template. Creator's own evidence)
    assets/            (screenshots, charts, video clips referenced by proof entries)
  testimonial-bank/    (README ships with template. Other people's words about the creator)
  metaphor-bank/       (README ships with template)
  framework-bank/      (README ships with template. Creator's OWN named frameworks)
Content/
  pieces/
```

If any of these already exist, leave them alone. Don't overwrite banks, READMEs, title-bank.md, or pieces folders. The bank READMEs ship with the product template, so the skill doesn't need to regenerate them. If a README is missing, flag it and ask before regenerating. If `banks/title-bank.md` is missing, scaffold it from `assets/title-bank-seed.md`, but only after confirming the path is empty.

## The walkthrough (5 stages, in order)

**FIRST ACTION: read state, then create the task list.** Before opening Stage 1, after loading `knowledge/vault-integration.md` and any existing `foundation/voice-profile.md`, do a silent check on `foundation/creator-foundation.md`:

- **File missing → fresh run.** Create the TodoWrite list with all 5 stages pending. Open Stage 1.
- **File exists, fully populated → ask refresh/keep.** Surface the Iceberg Statement and ask "Refresh, keep, or replace?"
- **File exists, partly populated → RESUME.** Read what's filled. Tell the creator: "Picking up where you left off. Locked: [list filled sections]. Next: [first unfilled section]." Mark completed phases done in the TodoWrite list. Skip to the first unfilled phase.

Then create the TodoWrite list with these five items:

1. Iceberg Discovery: produce Iceberg Statement + bottom (subtopics) + Person + Top 3 perceived problems
2. Credibility brags: three specific viewer-relevant wins
3. Backstory: Problem-Action-Outcome, 1-2 paragraphs
4. Packaging system: Gift framework + format rotation + title-bank seed + thumbnail strategy + design guardrails + creation path
5. Voice profile handoff: tell the creator to run `vid-voice-capture` next

Mark each `in_progress` when you start, `completed` when the save lands and the creator moves on.

## Context absorption + incremental save

Two rules that hold across every stage and phase. They protect the creator's time and the creator's work.

### 1. Absorb context before asking

Before opening any phase's question, scan earlier turns. If the creator already gave you 70%+ of the answer in a prior reply, surface it back instead of asking blind:

> "Here's what I picked up from earlier: [paraphrased]. Confirm, or sharpen?"

If they confirm, lock the phase. If they refine, fold it in. Only ask the blind opener when nothing prior is relevant.

This matters most for:

- **Phase 2 (audience):** often answered when the creator described their offer in Phase 1.
- **Phase 3 (problems):** often shows up while describing the avatar.
- **Phase 4 (Iceberg Statement transformation):** often implicit in the offer.
- **Phase 5 (subtopics):** sometimes mentioned as "things I teach."

The creator's time is the resource. Don't ask them to repeat what they just said.

### 2. Save at every phase lock

Don't wait until Stage 1 finishes to write to disk. Each phase locks, that section gets written right then. If chat closes mid-stage, the work is on disk and the next session resumes clean.

Use `AskUserQuestion` for the lock confirmation. If `AskUserQuestion` is not in your tool list, load it via ToolSearch first.

The lock prompt:

- Question: "Lock the [Person / Top 3 / Iceberg Statement / Bottom]?"
- Options: "Yes, lock" or "Refine"

On "Yes, lock":

- If the creator's confirmation includes new substantive information, do NOT save yet. Absorb the new signal, revise the section, and ask for lock confirmation again.
- If `foundation/creator-foundation.md` doesn't exist: create it from `assets/creator-foundation-template.md` with placeholders for unfilled sections. Fill in the locked section.
- If it exists: in-place edit (with the Edit tool) to update only the locked section. Leave every other section alone.
- Move to the next phase.

On "Refine": iterate the draft, then re-confirm.

By Phase 4, the file already has Person + Top 3 written. By Phase 5 it has those plus the Iceberg Statement. By Phase 6 it's complete and the final "save" is just the read-aloud approval.

Same save pattern for Stages 2, 3, 4. Stages 2 and 3 update `foundation/creator-foundation.md`; Stage 4 updates `foundation/packaging-system.md`. Lock confirmation via `AskUserQuestion`. Write to disk on Yes.

**This skill is a conversation, not a document.** Hard rules for every stage:

- Keep messages SHORT. 3-5 lines is usually right. Never dump multiple paragraphs upfront.
- The reference file is for CLAUDE to think with. Don't paste it at the creator. Use it to judge their draft silently. Only quote from it when comparison helps the creator fix something.
- Don't pre-teach. Don't lecture. Don't list all the good/bad pairs before the creator has answered anything. The pairs are ammunition you pull ONE at a time when a draft needs correction.
- Ask one focused question. Wait. React. Only ask two if the second is a tiny clarification needed to answer the first.

### The per-stage flow

1. **CHECK silently** for the file or section at its known path. Silent file read, no announcement.
   - If it exists, surface the first line or two and ask: "Refresh, keep, or replace?"
   - If nothing exists, go straight into the work. Don't ask "do you want to start fresh."
2. **Open briefly.** One or two lines of context, in the creator's language. What we're building, why it matters, the formula or prompt. Not a mini-essay.
3. **Ask the core question.** One short, direct question. Then stop and wait.
4. **Load the reference in your head** (not into the chat). Use it to judge what comes back.
5. **React conversationally.**
   - Strong answer: confirm, refine one detail if needed, move toward locking.
   - Weak answer: push back specifically. If comparison helps, pull ONE good/bad pair from the reference that maps to their weakness. Never dump more than one.
6. **Iterate in short exchanges** until it's specific and differentiated.
7. **Approve + save** to the right file. Keep previous approved sections as-is. Don't rewrite an earlier section unless the creator changed it.
8. **STOP.** Don't preview the next stage. Say the save happened, ask if they're ready to continue.

Don't batch stages. The existence check is a silent `Read` on ONE known path, not a vault scan.

### Stage 1: Iceberg Discovery

The biggest stage. Produces:

- **Iceberg Statement** (the top, one sentence, the channel's promise)
- **Bottom of the iceberg** (8-12 subtopics that deliver on the promise)
- **Person** (clean public label + structured qualifiers. Never a paragraph-only Person)
- **Positioning Inputs** (surface problem, deeper blocker, method, raw material, named enemy, stakes, creator phrases. Internal signals, not public copy)
- **Top 3 perceived problems** (main + 2 supporting, in viewer language)

**Silent check:** read `foundation/creator-foundation.md` if it exists. If the iceberg sections exist, surface them and ask refresh/keep/replace. Otherwise proceed.

**Load three files for your own use:**

- `references/iceberg-discovery-method.md`: the conversation backbone, drives the entire stage.
- `references/positioning-framework.md`: locked Iceberg Statement examples + good/bad pairs. **Examples-first:** read these BEFORE drafting any Iceberg Statement. Find the closest niche or shape. Write IN that shape using the creator's actual words. Not "consult if stuck." This is "consult before writing."
- `references/avatar-guide.md`: locked Person + Top 3 problem examples (viewer-voice phrasing bank by niche) + good/bad pairs. **Examples-first:** read the viewer-voice bank BEFORE drafting Top 3 problems. Find the niche closest to the creator's avatar. Match the shape: short declarative sentences, viewer's actual phrasing, three distinct domains.

Don't paste them into chat. Use them to think with.

**The skill EXECUTES. It doesn't teach.** The creator already knows the iceberg model from outside context. Don't explain the metaphor. Don't refresh definitions. Just run the production flow.

**Opener (short):**

> "Let's build your iceberg. We'll lock the top first, then the bottom. First: what product or service do you currently sell, or plan to sell?"

**Drive the conversation per `references/iceberg-discovery-method.md`.** That file holds the 6 phases (Opening, Audience Narrowing, Problem Discovery, Iceberg Statement, Bottom, Final Validation), the questions per phase, the common-issue handlers, when to pull a good/bad pair, and the validation checks before locking. Run the phases in order. Don't skip. Don't batch.

**Conversation rules:**

- One question at a time. Wait for each answer.
- Short messages, 3-5 lines.
- Tell problems from solutions. When the creator names a solution ("they need confidence"), run the disappearance probe: "If they already HAD that, what would disappear?"
- Push back on vague Person, Problem, Result. One specific probe first. Only if still vague, pull ONE good/bad pair from the reference.
- **Examples-first when drafting.** Read the locked examples in `positioning-framework.md` and `avatar-guide.md` before writing any draft. Match the shape. Use the creator's actual words.
- **Use the creator's exact words.** When the creator gives you specific words, sharpen by cutting filler. Don't reinterpret. Don't switch perspective ("they" stays "they"). Don't force a contrast or comparison shape.
- **Internal Sharp Angle Pass before drafting.** Before writing the Iceberg Statement, silently identify: Person, fit qualifier, desired result, business/life consequence, surface problem, deeper blocker, method, creator-owned raw material, named enemy, stakes, and exact creator phrases worth preserving. Infer what is already present. Ask only for 1 missing piece at a time if the statement cannot be drafted without it.
- **Propose, don't interrogate.** If the named enemy, result, method, or raw material is already visible, propose it back for confirmation instead of asking from scratch.
- **Reject generic drafts silently.** Do not show "this draft was too generic" unless the creator asks. Throw weak drafts away internally and show the sharpest plain-language version.
- **Three shapes, not three rewords.** If giving multiple Iceberg Statement candidates, use structurally different shapes from `positioning-framework.md`, not tiny rewordings of one template.
- **Lock and move.** After 2 sharpening rounds on a sub-artifact, lock the best version and move on. The Iceberg Statement is the goal of Stage 1, not perfectly polished sub-bullets.
- Read-aloud test on the locked Iceberg Statement: if the creator rewords anything when reading it back, that reworded version is closer. Use it.

**Professional edge case.** Creator never had the avatar's problem (doctor, physio, consultant). Swap "you" for "a real client" through problem discovery. Real client, real problem, real outcome. Attribute clearly. Never fabricate.

**Brand-new creator with no clients yet.** Educated guesses are fine for MVP. Flag it: "We're guessing for now. The iceberg refines once you publish 3-4 videos and see what real comments come in."

**Approve + save each locked section right away** to `foundation/creator-foundation.md` using `assets/creator-foundation-template.md`.

- When Person locks, write the structured Person fields and leave everything else pending. Public label must be a clean noun phrase the Iceberg Statement can actually use. Rich detail goes in Internal context.
- When Top 3 perceived problems lock, write those exact viewer-language problems.
- When the Iceberg Statement locks, write it before moving to the bottom. Also write Positioning Inputs if they surfaced during the Sharp Angle Pass.
- When the bottom of the iceberg locks, write the 8-12 subtopics.

Leave Credibility Brags and Backstory as `[pending Stage 2]` / `[pending Stage 3]` placeholders if not done yet. The partial file has to make sense if the chat closes at any point in the iceberg stage.

**STOP.** Say: "Iceberg locked. Ready for credibility brags?" Wait.

---

### Stage 2: Credibility brags

**Silent check** for a Credibility section. If it exists, refresh/keep/replace.

**Load** `references/credibility-brags-guide.md` for your own use.

**Brief opener:**

> "Three credibility brags for your intros. Specific wins your viewer cares about. Not years, not credentials. Three questions."

---

**Q1: Your biggest personal result.**

Ask:
> "What's the biggest result you've personally hit that the avatar wants? Number + timeframe."

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
> "Declarative past tense. 'I built, I served, I made.' Not 'I've been working on building.'"

---

**Synthesis.**

Draft three brag sentences. Each one: Big + Specific + Personal.

Check for anti-proof framing. If a brag makes the creator the source of failure (e.g. "I've built systems for 50 businesses, and the #1 reason those systems fail..."), push back hard. Reframe to "the #1 mistake business owners make before they come to me..."

If the creator genuinely doesn't have big numbers yet, fall back to: consumption ("read 300 books on..."), transformation ("went from X to Y myself"), or education ("spent 2 years studying..."). Flag as weaker. Real results will replace these.

**Approve + save** as the Credibility section in `foundation/creator-foundation.md`. Keep the locked iceberg sections exactly unless the creator changes them.

**STOP.** Say: "Three brags locked. Ready for the backstory?" Wait.

---

### Stage 3: Backstory

**Silent check** for a Backstory section. If it exists, refresh/keep/replace.

**Load** `references/backstory-structure.md` for your own use.

**Brief opener:**

> "Backstory. 1-2 paragraphs: the journey from the viewer's problem to their outcome. Problem, Action, Outcome. Four questions to build it."

---

**Q1: Starting state.**

Ask:
> "Before things changed, what was the state? Numbers, what a bad week looked like, what specifically was broken."

Push back on vague struggle:
> "'I struggled for years' doesn't land. What did a bad Tuesday look like? What were the numbers at your lowest point?"

---

**Q2: The trigger.**

Ask:
> "What was the specific moment or realization that made you change direction? Not 'I decided to improve.' The actual trigger."

---

**Q3: The moves.**

Ask:
> "What did you STOP doing and START doing? List the concrete moves. Not the summary. What did you stop? What did you replace it with? What did you try first that didn't work?"

This is the #1 place backstories fail. Push back hard:
> "'I built a system' is a summary. Someone reading this doesn't know what you actually did. What did you document? Who did you hire first? What ritual did you install? What did you remove from your calendar?"

Run the Action-test:
> "Read your action list out loud. Could someone else do what you did from what's written? If not, keep drilling."

---

**Q4: The outcome.**

Ask:
> "Outcome. Real numbers, real timeframe, what's different now."

Push back on vagueness:
> "'Now I help others' isn't an outcome. What changed for YOU? Subscribers, revenue, time, weight, relationships. Something measurable."

---

**Synthesis.**

Assemble 1-2 paragraphs. Conversational tone. Contractions OK. No corporate jargon. If you see "leveraged" or "proprietary methodology," push back: "Say it like you're telling a friend."

If the creator never had the viewer's problem, swap "I" for a real client. Attribute clearly. Never fabricate.

**Approve + save** the full `foundation/creator-foundation.md` now: Iceberg + Person + Top 3 problems + Credibility + Backstory. Use `assets/creator-foundation-template.md`. Keep the creator's messy-but-useful phrasing. Light cleanup only.

**STOP.** Say: "creator-foundation.md locked. Ready for packaging?" Wait.

---

### Stage 4: Packaging system

**Silent check** for `foundation/packaging-system.md`. If it exists, refresh/keep/replace (sub-section or whole).

Stage 4 sets starting video defaults. It does not pretend to know the final winning formats or thumbnail strategy. The point is to give downstream skills a clear first place to start, with evidence, confidence, and what to watch for.

Seven sub-stages. Run one at a time. Each sub-stage: brief opener, one focused question, react, iterate. Load the knowledge ref only when you reach that sub-stage. Don't dump the knowledge ref into chat.

**4a: Packaging mode.** Before choosing formats or strategies, identify the evidence level.

Ask:
> "Do you already have published videos with useful performance data, or are we setting first defaults for a new channel?"

If they have useful published videos:
- Check for `banks/pattern-bank.md`, especially `banks/format-patterns-bank.md` and `banks/packaging-bank/`.
- If banks exist, use them as evidence. Say: "Good, we'll use what already has signals instead of guessing."
- If banks are missing, offer the clean choice: "Fast version: tell me what has worked so far and I'll save temporary defaults. Better version: run `vid-research` first so we can use your own outliers and competitor patterns, then come back."
- If they choose the fast version, mark confidence as low or medium and note the evidence basis as creator judgment.

If they are new or do not have useful data:
- Say: "Since there is no channel data yet, we'll pick first defaults based on your audience, your proof, and what you can actually make. These change once real data shows what to keep."
- Use source-backed format fit rules plus creator judgment. Mark confidence as low or medium unless the fit is obvious.

**4b: Gift Framework.** Load `knowledge/gift-framework.md`. Build the three layers one at a time.

Ask:
> "First, wrapping paper: what thumbnail style does your avatar actually click? Plainspoken examples are better than style words. If you have 1-2 competitor thumbnails you admire, share them."

Push back on vague answers:
> "'Professional-looking' doesn't tell `vid-thumbnail` what to make. Is it face + big contradiction text, clean object shot, messy whiteboard, before/after, or something else?"

Then ask:
> "Box: what video format do they already open most often? Short how-to, case study, teardown, deep dive, interview, news, or list?"

Then ask:
> "Gift: what do they come back for from you specifically? Systems, tactics, stories, frameworks, opinion, examples, or something else?"

Save the three answers as wrapping paper, box, and gift. Don't turn them into marketing copy. Use the creator's phrasing where it gives useful constraints.

**4c: Starting format rotation (3+1).** Load `knowledge/format-rotation-guide.md`.

Do not ask the creator to pick from all seven cold. First infer the best first rotation using:
- existing channel evidence, if available
- pattern-bank evidence, if available
- avatar appetite from the Gift Framework
- creator capability and available proof
- source-backed format fit rules

Then propose:
> "Here is the first rotation I would test: {Format 1}, {Format 2}, {Format 3}, with {Format X} as the every-fourth-video experiment. I picked these because {plain reasons}. What feels wrong?"

For each format saved, include:
- Why this is a good first test
- Evidence basis: creator judgment, source-backed default, own channel data, or pattern-bank research
- Confidence: low, medium, or high
- Watch for: what would tell us to keep, adjust, or drop it

Push back if the picks don't match the avatar, the creator's proof, or the creator's actual production ability. Use plain words, not source language.

**4d: Title Bank seed + orientation.** Load `knowledge/BENS-framework.md`.

Silent check `banks/title-bank.md`.
- If it exists, leave it alone. Say: "Title bank already exists. We'll use it downstream and add winners over time."
- If missing, create `banks/` if needed and copy `assets/title-bank-seed.md` to `banks/title-bank.md`. Then say: "Title bank seeded. Downstream `vid-title` will adapt these patterns to your real video material, and your own winners will replace the generic seed over time."

Keep the BENS orientation tight: Big, Easy, New, Safe in one or two sentences total. Don't ask the creator to draft titles in foundation.

**4e: Starting thumbnail strategy.** Load `knowledge/thumbnail-strategy-menu.md`.

Do not ask the creator to pick from the menu cold. Propose 2 strategies based on the avatar, Gift Framework, existing evidence, and starting format mix.

Ask:
> "For the first thumbnail tests, I would use {Strategy 1} and {Strategy 2}. I picked those because {plain reasons}. What feels wrong?"

If they have past thumbnails, use that data to inform.

For each strategy saved, include why this is a good first test, evidence basis, confidence, and what to watch for.

**4f: Design guardrails.** Short: color palette (2-3 max), font, hero element (face/object/text), expression rules, text limit (4-5 words max). If a brand style guide exists, pull from it.

**4g: Creation path.** Pick one: Photoshop/DIY, AI workflow, Batch-shoot photos, Outsource.

**Approve + save** `foundation/packaging-system.md` using `assets/packaging-system-template.md`. Every saved field has to change a downstream packaging decision: `vid-title` uses format/BENS/title-bank context, `vid-thumbnail` uses strategy/design guardrails/creation path, `vid-framing` uses the starting format rotation.

**STOP.** Say: "Starting video defaults saved. Last step is the voice-profile handoff." Wait.

### Stage 5: Voice profile handoff

The voice profile belongs to `vid-voice-capture`. This stage does not extract voice, summarize voice, or write `foundation/voice-profile.md`.

**Silent check** for `foundation/voice-profile.md`.
- If missing, tell the creator to run `vid-voice-capture` next.
- If present, surface the first line and say it already exists. If they want to refresh it, the refresh still runs through `vid-voice-capture`.

**What to say to the creator:**

> "Foundation and packaging are done. Now run `vid-voice-capture` for the voice profile. Bring 2-3 transcripts, past writing, or a 10-minute live riff. That skill builds `foundation/voice-profile.md` once, from real material, so scripts sound like you instead of a generic AI draft."

**Do not write to `foundation/voice-profile.md` from this skill.**

**STOP.** Say: "All five stages complete." Then wrap up.

## Wrap up

After all 5 stages:
1. Confirm `foundation/creator-foundation.md` and `foundation/packaging-system.md` both exist
2. Confirm banks folders exist (empty is fine)
3. Confirm `banks/title-bank.md` exists or clearly say why it wasn't seeded
4. Report to creator: "Foundation complete. Next steps in order: (a) run `vid-voice-capture` to build the voice profile. That doc is critical for every script. Give it a real session. (b) Run `vid-capture` anytime you have a story or proof point. (c) When ready to make a video, run `vid-pipeline`."

## Principles

- **Conversation, not document.** Every stage runs like a 15-minute coaching conversation. Sharp questions, short messages, one exchange at a time. The reference files are ammunition for Claude, not handouts for the creator.
- **Stay close to the framework.** Reference files are tested. Use them to judge what the creator sends back, not to lecture.
- **Specificity or nothing.** Push back on vague, generic, hedged, or expert-language answers. Weak work at any stage poisons every downstream doc.
- **Creator drives, Claude structures.** Claude extracts and organizes. Claude does NOT generate positioning, avatar, brags, or backstory FOR the creator.
- **MVP principle.** First version will need refinement after real videos publish. Don't grind for perfection. Lock the best the creator can articulate today.

## Reference index

**Skill-local** (setup guides for the foundation docs, in `references/`):

| Stage | Reference | Why |
|-------|-----------|-----|
| 1 | `references/iceberg-discovery-method.md` | Conversation backbone for the iceberg stage (drives all 6 phases) |
| 1 | `references/positioning-framework.md` | Paired good/bad examples for the iceberg top + Volvo/Red Bull + Known For One Thing |
| 1 | `references/avatar-guide.md` | Paired good/bad examples for Person details + Top 3 perceived problems |
| 2 | `references/credibility-brags-guide.md` | How to extract viewer-relevant wins |
| 3 | `references/backstory-structure.md` | Problem-Action-Outcome format with examples |
| 5 | (handoff to `vid-voice-capture`, no local reference) | Voice profile is built by its own skill |

**Shared** (concepts used by multiple skills, in `knowledge/`):

| Stage | Reference | Why |
|-------|-----------|-----|
| 4a | `gift-framework.md` | Packaging philosophy (wrapping, box, gift) |
| 4b | `format-rotation-guide.md` | Rule of 3+1 + the 7 formats |
| 4c | `BENS-framework.md` | Title system (Big/Easy/New/Safe) |
| 4d | `thumbnail-strategy-menu.md` | The 6 strategies + when to use each |

Templates live in `assets/`:
- `creator-foundation-template.md`
- `packaging-system-template.md`
- `title-bank-seed.md`

Voice profile template lives in `vid-voice-capture/assets/voice-profile-template.md`. Only `vid-voice-capture` writes that file.
