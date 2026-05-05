---
name: vid-foundation
description: One-time creator setup for the YouTube Content OS. Walks a YouTube business owner through positioning, avatar, credibility, backstory, voice profile, and packaging system to produce the foundational documents every downstream skill loads. Use this whenever a creator is new to the system, is pivoting positioning, or needs to refresh their foundation. Triggers on "set up my channel", "I'm starting a new channel", "build my creator foundation", "create positioning", "define my avatar", "set up YouTube Content OS", or when any other vid- skill tries to run without foundation docs in place.
---

# Video Foundation

One-time setup that produces the three documents every other YouTube Content OS skill loads. Without these docs, downstream skills (ideation, scripting, packaging, measurement) have no creator context to work against.

**At session start, load `knowledge/vault-integration.md`.** It defines the frontmatter schema, wikilink contracts, tag conventions, file naming rules, and callout patterns that every entry this skill produces must match. Non-negotiable — it's the contract that makes downstream skills find and link entries correctly.

## What this produces

Two documents in the creator's workspace:

1. **`foundation/creator-foundation.md`** — the iceberg (top positioning statement + bottom subtopic angles), Person details, Top 3 perceived problems, axis-of-differentiation, credibility brags, backstory (Problem-Action-Outcome)
2. **`foundation/packaging-system.md`** — Gift Framework commitment, BENS title bank orientation, thumbnail strategy test plan, 3+1 format rotation pick

Plus folder structure for banks and per-video content.

**Voice profile is NOT produced here.** It has its own dedicated skill (`vid-voice-capture`) because the canonical schema has two layers (cross-context patterns + per-format context maps) and the extraction is too load-bearing to fit inside this walkthrough. Stage 4 is a handoff that tells the creator to run `vid-voice-capture` next.

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
  voice-profile.md   (NOT produced here — vid-voice-capture writes this)
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

## The walkthrough (5 stages, sequential)

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

### Stage 1: Iceberg Discovery

The biggest stage. Produces the channel's iceberg — top (positioning statement) + bottom (8-12 subtopic angles) + Person details + Top 3 perceived problems + axis owned + (optionally) the single word the creator wants to be known for.

**Silent check:** read `foundation/creator-foundation.md` if it exists. Iceberg sections exist → surface them and ask refresh/keep/replace. Otherwise proceed.

**Load three files for your own use:**

- `references/iceberg-discovery-method.md` — the conversation backbone. Drives the entire stage.
- `references/positioning-framework.md` — paired good/bad examples for the top. Pull ONE pair when the creator is stuck on what "specific" looks like.
- `references/avatar-guide.md` — paired good/bad examples for Person details + Top 3 perceived problems. Pull ONE pair when needed.

Do not paste any of them into chat. Use them to think with.

**Brief opener:**

> "Let's build the iceberg for your channel. Top = the one-sentence umbrella every video lives under. Bottom = the subtopic angles you can teach that solve the top problem. We work top-down. Doesn't have to be perfect — we sharpen as we go."

**Drive the conversation per `references/iceberg-discovery-method.md`.** That file specifies the 6 phases (Opening → Audience Narrowing → Problem Discovery → Iceberg Top → Iceberg Bottom → Final Validation), the questions per phase, the common-issue handlers, when to pull a good/bad pair, and the validation checks before locking. Run the phases sequentially. Don't skip. Don't batch.

**Conversation rules (every phase):**

- One question at a time. Wait for each answer.
- Short messages — 3-5 lines.
- Distinguish problems from solutions actively. When the creator names a solution ("they need confidence"), run the disappearance probe: "If they already HAD that, what would disappear?"
- Push back on vague Person, Problem, Result. One specific probe first; only if still vague, pull ONE good/bad pair from the supporting reference.
- Read-aloud test on the locked top: if the creator rewords anything when reading it back, that reworded version is closer — use it.

**Professional edge case.** Creator never had the avatar's problem (doctor, physio, consultant) — swap "you" for "a real client" throughout problem discovery. Real client, real problem, real outcome. Attribute clearly. Never fabricate.

**Brand-new creator with no clients yet** — educated guessing is fine for MVP. Flag it: "We're guessing for now; the iceberg refines once you publish 3-4 videos and see what real comments come in."

**Approve + save** to `foundation/creator-foundation.md` using `assets/creator-foundation-template.md`. Output sections: Iceberg Top, Iceberg Bottom, Person, Top 3 perceived problems, Axis owned, (optionally) Known-for word.

**STOP.** Say: "Iceberg locked. Ready for credibility brags?" Wait.

---

### Stage 2: Credibility brags

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

### Stage 3: Backstory

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

### Stage 4: Voice profile (handoff to vid-voice-capture)

Voice profile is its own dedicated skill — `vid-voice-capture` — because the canonical schema has two layers (cross-context patterns + per-format context maps) and benefits from a deeper extraction pass than vid-foundation has room for. Doing a thin version here would produce a partial doc that downstream writing skills can't load cleanly.

**Silent check** for `foundation/voice-profile.md`. If it already exists, surface the first line and ask refresh/keep/replace — but the refresh path still routes through vid-voice-capture.

**What to say to the creator:**

> "Voice profile is a dedicated skill (`vid-voice-capture`) because it's the most load-bearing doc downstream — every script depends on it. It needs 2-3 transcripts, past writing, or a 10-minute live riff to do it justice. After this stage we'll lock packaging, then you'll run `vid-voice-capture` separately. That keeps each session focused and produces a profile that every writing skill can load without surprises."

**Do NOT extract voice here.** Do not write to `foundation/voice-profile.md` from this skill. The creator runs vid-voice-capture as the next step after vid-foundation finishes.

**STOP.** Say: "Got it — voice profile gets its own session via `vid-voice-capture` after we wrap. Last stage is packaging — six quick sub-steps. Ready?" Wait.

### Stage 5: Packaging system

**Silent check** for `foundation/packaging-system.md`. Exists → refresh/keep/replace (sub-section or whole).

Six sub-stages. Run one at a time. Each sub-stage: brief opener, one or two questions, react, iterate. Load the knowledge ref only when you reach that sub-stage. Don't dump the knowledge ref into chat.

**5a: Gift Framework.** Load `knowledge/gift-framework.md`. Ask in plain language:

> "Three things about your avatar: their favorite thumbnail style, their favorite video format, and the kind of content they keep coming back for (systems, tactics, stories, frameworks). If you have competitor videos or thumbnails you admire, share them and we'll reverse-engineer."

Push back on vague answers ("professional-looking" → which specific strategy?).

**5b: Format rotation (3+1).** Load `knowledge/format-rotation-guide.md`. Ask:

> "Pick 3 proven formats to rotate plus 1 experimental slot. The seven options are Short Process, Case Study, Roast, Deep Dive, Interview, News, Listicle. Which three fit your avatar best?"

Push back if picks don't match the avatar. News-fit vs Tutorial-fit vs Story-fit.

**5c: Title Bank orientation.** Load `knowledge/BENS-framework.md`. The workspace already has `banks/title-bank.md` with validated patterns. Brief orientation only — walk them through Big / Easy / New / Safe in one or two sentences each and point them at the bank. No draft needed at this stage.

**5d: Thumbnail strategy.** Load `knowledge/thumbnail-strategy-menu.md`. Ask:

> "Pick 2 thumbnail strategies to test first. Cognitive Dissonance is a strong default. Commit to 2+ videos per strategy before judging."

If they have past thumbnails, use that data to inform.

**5e: Design guardrails.** Short: color palette (2-3 max), font, hero element (face/object/text), expression rules, text limit (4-5 words max). If brand style guide exists, pull from it.

**5f: Creation path.** Pick one: Photoshop/DIY, AI workflow, Batch-shoot photos, Outsource.

**Approve + save** `foundation/packaging-system.md` using `assets/packaging-system-template.md`.

**STOP.** Say: "Packaging system locked. All five stages complete." Then wrap up.

## Wrap up

After all 5 stages:
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
| 1 | `references/iceberg-discovery-method.md` | Conversation backbone for the iceberg stage (drives all 6 phases) |
| 1 | `references/positioning-framework.md` | Paired good/bad examples for the iceberg top + Volvo/Red Bull + Known For One Thing |
| 1 | `references/avatar-guide.md` | Paired good/bad examples for Person details + Top 3 perceived problems |
| 2 | `references/credibility-brags-guide.md` | How to extract viewer-relevant wins |
| 3 | `references/backstory-structure.md` | Problem-Action-Outcome format with examples |
| 4 | (handoff to `vid-voice-capture` — no local reference) | Voice profile is its own skill |

**Shared** (concepts used by multiple skills, live in `knowledge/`):

| Stage | Reference | Why |
|-------|-----------|-----|
| 5a | `gift-framework.md` | Packaging philosophy (wrapping, box, gift) |
| 5b | `format-rotation-guide.md` | Rule of 3+1 + the 7 formats |
| 5c | `BENS-framework.md` | Title system (Big/Easy/New/Safe) |
| 5d | `thumbnail-strategy-menu.md` | The 6 strategies + when to use each |

Templates live in `assets/`:
- `creator-foundation-template.md`
- `packaging-system-template.md`

Voice profile template lives in `vid-voice-capture/assets/voice-profile-template.md` (canonical, two-layer).
