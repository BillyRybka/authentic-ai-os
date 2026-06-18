---
name: vid-intake
description: Capture raw video material into a structured brain-dump.md for one video. Auto-detects which of 7 intake modes the creator is in (idea + dump, outline paste, own transcript, inspired-by, news-jacking, client win, story-first), runs the matching short conversation, confirms iceberg fit and Top 3 problem alignment, saves to content/pieces/{slug}/brain-dump.md. The creator's exact phrasing is preserved verbatim because the brain dump IS the voice for every downstream writing skill. Anti-fabrication. Adaptive drilling. Target time 5-10 minutes per video, never an interrogation. Runnable standalone OR invoked by vid-pipeline at the start of the SCRIPT phase. Use this skill whenever a creator brings video material that has not yet been captured into a piece folder, even if they don't explicitly say "intake". Phrases like "I want to make a video about X", "I have a brain dump for this video", "here's a transcript I want to turn into a video", "I saw this competitor video and want my own take", "I had this thing happen and want to make a video", "I want to do a video on my client win", "there's a new feature I want to cover", "let's start a new video", "let's plan this one out", or any downstream pipeline that needs the raw material captured should fire this skill.
---

> 🔄 **Pre-flight (mandatory).** Before doing anything else, read `${CLAUDE_PLUGIN_ROOT}/knowledge/update-check.md` and follow it. If a newer version exists, halt and tell the creator. If you're up to date, continue with the skill below.

# Video Intake

Captures whatever raw material the creator brings and produces a structured `content/pieces/{slug}/brain-dump.md` that downstream skills (`vid-framing`, `vid-structure`, `vid-segment`, `vid-intro`, `vid-ending`) read at runtime. Seven intake modes covering the realistic ways a creator starts a video. Auto-detects mode, runs the matching short conversation, locks iceberg fit and Top 3 problem alignment, saves.

**Scope boundary:** vid-intake captures raw material only. It does NOT pick the format (`vid-framing` does that), does NOT generate angle framings (`vid-framing`), does NOT write any script content (`vid-intro`, `vid-segment`, `vid-ending`). Light alignment check (iceberg + Top 3) happens here so downstream skills don't waste time on a video that does not fit the channel. Full angle framing and Core Payoff selection happen in `vid-framing` next.

## What this produces

`content/pieces/{slug}/brain-dump.md` with creator's exact phrasing preserved, plus the iceberg fit and Top 3 problem alignment locked. Voice fuel for every downstream writing skill.

When invoked as a sub-skill (e.g. by vid-pipeline to start a new piece), it also returns the brain-dump packet to the caller. The save (the piece folder, brain-dump.md, and piece.md) still happens here, in both modes.

## When to run this

- Creator has a video to start and the piece folder does not exist yet
- Creator wants to dump material for a video they have been thinking about
- Orchestrator (`vid-pipeline`) invokes at the start of the SCRIPT phase
- Creator just had an experience or got a client win and wants to capture it before it fades
- `vid-ideas` hands over a picked-idea seed packet (the front-door, when the creator started blank). Run the matching mode (usually idea + dump) seeded from `{idea_title, pillar, top_3_problem, iceberg_fit, anchor}`, then drill for the material.

## Prerequisites

Hard requirements:

- `foundation/creator-foundation.md` exists (iceberg + Top 3 problems + audience). vid-intake reads these to run the alignment check.
- `foundation/voice-profile.md` exists. vid-intake reads opener pattern, energy baseline, words avoided so it mirrors back in the creator's voice.

If foundation is missing, tell the creator to run `/foundation` first. If foundation exists but voice-profile.md does not, tell them to run `vid-voice-capture` next so downstream writing skills have voice context, but proceed with intake (it can run on creator-foundation alone).

## Invocation modes

**Standalone:** creator invokes directly. Skill runs the full conversation, creates the piece folder, saves brain-dump.md, hands off to `vid-framing` next.

**Sub-skill:** another skill (`vid-pipeline`) invokes. Same conversation. The save (piece folder, brain-dump.md, piece.md) still happens here, in both modes; it also returns the brain-dump packet to the caller for assembly awareness.

If invoked with context from a caller (e.g. "intake for piece={slug}, mode=inspired-by, source-internal=[transcript text]"), skip the mode detection question and go straight to the matching conversation flow.

## The 7 modes (auto-detected)

1. **Idea + dump**: creator has a topic plus things they want to say. Most common entry point.
2. **Outline / notes paste**: creator brings half-formed bullet points or a doc.
3. **Own transcript**: creator pastes their own Loom, voice memo, call transcript, or past video transcript.
4. **Inspired-by**: creator wants to make their own evidence-based take on a topic they saw covered elsewhere (competitor video, transcript, article, podcast). Source is INVISIBLE in productized output. The creator never references the original source.
5. **News-jacking**: fresh feature, release, or event the creator wants to cover. Faster flow.
6. **Client win**: creator wants a video around a specific result. Skill captures the proof and forces the pivot to a teaching arc, not a client biography.
7. **Story-first**: creator opens with a moment they had. Skill captures the moment, then locates the lesson that fits the channel.

Mode detection happens from the creator's opening message. If ambiguous, surface a short menu and ask. See `references/mode-conversation-examples.md` for full mock dialogues showing each mode in action with worked examples and near-misses.

## The walkthrough

Same shape every mode runs. The body of each mode varies (see references), but the spine is universal.

Every quoted line below shows register and length, not a script. Respond to what the creator actually said. Never paste one verbatim. The point is the feel: short, human, one move per message.

### Phase 1: Detect mode and load context

Silent loads (do NOT paste into chat):

1. `foundation/creator-foundation.md` (iceberg statement, Top 3 problems, audience)
2. `foundation/voice-profile.md` (opener pattern, words avoided, energy)
3. `knowledge/vault-integration.md` (frontmatter schema for brain-dump.md)
4. `knowledge/story-capture-guide.md` (the 6 dynamic story prompts, used in story-first mode and to drill thin stories in any mode)
5. `references/mode-conversation-examples.md` (your calibration anchors per mode)
6. `knowledge/iceberg-and-top-3-alignment.md` (the 2-layer alignment gate)
7. `references/push-vs-pause-rules.md` (when to drill vs when to save with TODOs)

Detect the mode from the creator's first message. If they paste a wall of text → Mode 2 or Mode 3 (ask: yours or someone else's?). If they describe an idea conversationally → Mode 1. If they drop a URL or describe an outside source → Mode 4. If they open with "this thing happened" → Mode 7. If they open with a number or client name → Mode 6. If they reference a fresh feature/release → Mode 5.

Confirm the detected mode in one short message before running the full flow:

> "Mode 1, idea dump. Brain dump whenever you're ready, I'll capture as you go."

When the mode is obvious, fuse the confirm into the dump opener like that and skip the separate Phase 2 line. Only split them when the mode is genuinely ambiguous and you need a yes before opening the door.

### Phase 2: Brain dump

Once mode is confirmed, open the door for the dump. The exact opener varies by mode (see `references/mode-conversation-examples.md`). For Mode 1:

> "Go ahead, I'm listening." / "Brain dump whenever you're ready, I'll capture as you go."

Then SHUT UP. Do not interrupt mid-dump. Let the creator land their full thought before responding. Read-once, respond-once.

For modes 2-7, the dump shape varies but the rule holds: open the door, let them dump, do not interrupt.

### Phase 3: Reflect back what landed

After the dump, mirror back what was captured. Use the creator's own language. Surface the points, stories, claims, proofs, metaphors, open questions you heard. Format:

> "Got [point 1], [point 2], [point 3], plus the [thing] story. Miss anything?"

Creator confirms or corrects. This step takes 30 seconds. It builds trust (the creator hears their thinking organized) and surfaces gaps (the AI flags what it could not catch).

### Phase 4: Iceberg and Top 3 alignment check

Two-layer alignment, fast. The detail is in `knowledge/iceberg-and-top-3-alignment.md`. Surface format:

> "That's Problem [N], the [specific Top 3 thread] one, inside your iceberg. Right?"

Possible creator responses:

- YES → confirmed, lock alignment in frontmatter, move to Phase 5.
- NO, wrong Top 3 → ask which one fits better, confirm.
- NO, doesn't fit any Top 3 but does fit iceberg → flag as `outlier_within_iceberg`, ask for a one-line rationale, allow override.
- NO, doesn't fit iceberg → harder flag. Ask "wrong channel for this one, or has your iceberg shifted?" If shifted, point at /foundation refresh. Otherwise capture rationale and let creator decide whether to save anyway.

Never block the save. The creator's call. The flag in frontmatter signals to downstream skills that alignment was deliberate.

### Phase 5: Drill ONLY where needed

Scan the dumped material. If the dump is rich and clear, skip drilling, go to Phase 6. If the dump has thin spots, ask 1-3 surgical questions max. The detail on push vs pause lives in `references/push-vs-pause-rules.md`. Quick rules.

**Push when:**
- A claim is made with no proof attached ("Where's that number from?")
- A story is referenced but not told ("Tell me the moment, not the lesson.")
- The viewer outcome is mushy ("What does the viewer go and DO after watching?")
- Iceberg or Top 3 alignment was unclear in Phase 4

**Don't push when:**
- The dump is rich and clear. Confirm + move on
- The creator already said "I'll come back to that". Respect, mark TODO
- 2 rounds of drilling on one point have not unlocked. Bail, mark TODO
- Creator says "stop, just save". Save with TODOs, end

When drilling on a thin story, use the dynamic 6 prompts from `knowledge/story-capture-guide.md`. Do not run all 6. Pick the prompt that fits the topic and the avatar's pain. If the first prompt does not unlock in 1-2 rounds, pivot to the next-best prompt. If 3 prompts in a row do not land, save the dump with a TODO that says "story missing for [point X], capture next session."

### Phase 6: Propose slug, create folder, save

Once the dump is captured and aligned:

1. Propose a kebab-case slug. Source from the topic the creator named, not from the iceberg (the iceberg is generic, the slug is specific to this video).
2. Confirm slug with creator in one short message: `slug: "frequency-vs-depth-on-youtube"`, sound right?
3. Create `content/pieces/{slug}/` directory.
4. Write `content/pieces/{slug}/brain-dump.md` per the schema below.
5. Ask which content pillar this video lands under. Offer the pillars from `creator-foundation.md`; the creator picks one or leaves it open (null is fine, it is not a blocker). Then create `content/pieces/{slug}/piece.md` with the intake frontmatter (the per-piece identity ledger every downstream skill appends to). See the piece.md schema below.
6. Confirm save in one line: "Saved. `vid-framing` next to lock the angle."

Do not create the folder before slug is confirmed. No orphan empty folders.

## Output schema (brain-dump.md)

```yaml
---
type: brain-dump
slug: {kebab-case-slug}
mode: idea | notes | own-transcript | inspired-by | news-jacking | client-win | story-first
captured: YYYY-MM-DD
problem_addressed: 1 | 2 | 3 | outlier_within_iceberg | outlier
iceberg_aligned: true | false
aligned_with: "{The problem this maps to. Use the bare mapping (e.g. 'Problem 1'), optionally followed by the creator's VERBATIM phrase for that problem from their dump. Never paraphrase, summarize, or add a justification or channel-fit clause. If you cannot quote it from what they actually said, just write the bare mapping.}"
source_internal_only: "{Optional. For inspired-by mode: brief internal note about source piece. NEVER referenced in productized video.}"
---

## Raw dump (verbatim)

{The creator's complete dump for this video, exactly as they said it. Nothing cut, nothing reordered, nothing cleaned beyond obvious transcription fixes. This is the lossless source of truth; every organized section below is an index built from this and must never drop, reorder, or contradict it. For paste input (own-transcript, inspired-by) this is the pasted text in full.}

## Topic + angle

{The topic and angle in the creator's OWN words and sentence shapes, not a summary of them. Use what they actually said. Do not open with "The angle is that..." or any narrative framing.}

## Audience and Top 3 problem

{Capture only. State which Top 3 problem this lands on (e.g. "Problem 1"). Then add only what the creator actually said about who this is for and why it matters to them, in their words. Do NOT invent a "why this avatar feels this pain right now" rationale they did not say. If they did not describe the audience, the problem mapping alone is enough.}

## Outcome

{Capture only. If the creator stated what they want the viewer to walk away with, write it in their words. If they did not state it, write "Not stated. vid-framing sets the core payoff and goal." Never synthesize or invent an outcome, and never reduce a listicle to a single action. Outcome framing is vid-framing's job, not intake's.}

## Material

### Lessons / points
- {Lesson 1 in creator's exact phrasing}
- {Lesson 2}
- {etc}

### Stories
- {A story or anecdote, including cautionary ones (someone got burned). [[story-bank/slug]] if pulled from existing bank, or new story captured here in P-A-O shape.}

### Proof
- {Evidence that something WORKS: a result, what you did, a testimonial of what worked for a client or for you. [[proof-bank/slug]] if pulled, or new proof captured here. A cautionary anecdote is a Story, not Proof.}

### Metaphors
- {[[metaphor-bank/slug]] if pulled, or new metaphor captured}

### Claims (no proof attached yet)
- {Claim 1}. TODO: source proof from [bank or new capture]

## Strongest raw lines

- "{The creator's most vivid, quotable lines, verbatim. Exact words, stutters cleaned only, never reworded. This is the voice reservoir the downstream writing skills pull from. Capture the lines the way the creator actually said them, not a tidy paraphrase of them.}"

## Open questions / TODOs

- {Anything thin or missing the creator wants to chase later}
- {Anything vid-framing or vid-segment will need to surface}

## Source notes (internal only, never appears in productized video)

{For inspired-by mode: the source piece's points captured for the creator's reference. For own-transcript mode: the original transcript, lightly cleaned. For other modes: empty.}
```

## Output schema (piece.md)

The per-piece identity ledger. vid-intake creates it with the intake fields; every downstream skill appends its own fields and never overwrites another skill's.

```yaml
---
type: content-piece
slug: {kebab-case-slug}
pillar: {pillar-slug or null}
status: ideating
created: YYYY-MM-DD              # today. Stamped once here, never changed.
last_updated: YYYY-MM-DD          # today. Every downstream skill that writes piece.md bumps this.
---
```

Set both `created` and `last_updated` to today's date at creation. `created` is permanent; `last_updated` moves forward every time a later skill touches this file.

vid-framing appends `selected_angle`, `core_payoff`, `format`, `goal`, `viewer_stage`, `voice_context`; vid-title appends `title`; vid-thumbnail produces `thumbnail-brief.md`; vid-structure appends `segment_purposes` + `tension_plan` and advances `status: drafting`; the writing skills append `stories_used` / `proofs_used` / `metaphors_used`; vid-segment appends `segments_completed`; vid-pressure-test appends the audit block and advances `status: filming-ready`. Full schema in `knowledge/vault-integration.md`.

## Conversational discipline

- **Conversation, not document.** Short messages. Never paste reference content into chat. References are for YOUR thinking.
- **Listen during dumps.** When the creator is mid-dump, do not interrupt. Read-once, respond-once.
- **Use the creator's exact phrasing.** When mirroring back, when saving, when asking follow-ups. The brain dump IS the voice. Polishing kills it.
- **Bank the raw lines verbatim.** As the creator talks, pull their most vivid, quotable lines into `## Strongest raw lines` exactly as said (stutters cleaned only, never reworded). Paraphrasing into tidy bullets is the most common way the voice gets lost. The Material bullets organize the thinking. The raw lines preserve the voice.
- **No narrative framing in the body.** Do NOT rewrite the creator's material into summary prose. Never write "The angle is that...", "This lesson is about...", "The viewer sees that...". Write Topic, Outcome, and Material in the creator's own words and sentence shapes, the way they said it. If they said "everyone thinks the answer is to grind harder, that is the trap," save that, not "The angle is that grinding harder is a trap." Reflect-back in chat can paraphrase for confirmation. The saved dump never does. The dump is raw capture, not a summary of raw capture.
- **No AI-meta narration anywhere, including frontmatter.** Fields like `aligned_with` and the Audience and Top 3 problem section read plainly or in the creator's words. Never write "the thesis of this is...", "Reinforces X", or similar AI-meta phrasing. If you would not say it out loud to the creator, do not write it.
- **Proof is not Story.** Proof is evidence that something WORKS: a result, what you did, a testimonial of what worked for a client or for you. An anecdote, including a cautionary one (someone got burned by slop), is a Story. Never file a story under Proof.
- **Bank wikilink format.** Bank pulls use the `bank-dir/slug` form, like `[[proof-bank/onboarding-5h-to-1h]]` or `[[story-bank/agency-owner-fired-himself]]`. Never put the banks folder in the path.
- **Capture the full dump first, organize second.** Put the creator's complete dump verbatim in `## Raw dump (verbatim)` before sorting anything into Material. The organized sections are an index built from the raw dump; they never drop, reorder, or contradict it. Raw is the source of truth, structure is the convenience layer.
- **Capture everything, cut nothing.** Intake captures every point the creator makes, raw, even rhetorical lines or points that overlap each other. You are not the editor here. Deciding what is a standalone lesson versus a line, and merging overlaps, is `vid-structure`'s job. Do not drop, dedup, or trim material at intake.
- **Push back when the material is thin.** Not interrogation. One surgical question that unlocks the next layer. If it does not unlock in 2 rounds, mark TODO and move on.
- **Specificity wins.** Vague answers get pushed back on. Generic verbs become specific verbs. Round numbers become real numbers. But not at the cost of the conversation feeling like a form.
- **Read-aloud as the final filter.** Before saving, ask the creator to read the brain dump back. If they would reword anything, capture the better wording.

## Hard friction (auto-flag)

1. **Fabricated content.** Anything not in the creator's dump or already in their banks. The brain dump is the creator's words plus what they explicitly pull from banks. Never invent stories, numbers, clients, results, or proof.
2. **Foundation missing.** Don't run vid-intake without `creator-foundation.md`. Tell the creator to run `/foundation` first.
3. **No alignment captured.** Never save brain-dump.md without iceberg fit and Top 3 alignment fields populated, even if `outlier`. Frontmatter has to be honest.
4. **Em-dashes.** Brand-level no. Use commas, periods, parens. Every save passes a Vale check.
5. **"Avatar" replaced with vague terms.** Avatar is specific. Do not soften to "audience" in foundation references. It's the constructed profile of the viewer/buyer per `creator-foundation.md`.

## Soft friction (surface and explain, creator decides)

1. **Outlier video.** If `iceberg_aligned: false` or `problem_addressed: outlier`, flag at save time. Explain consequence (channel coherence drops over time if outliers stack). Creator decides.
2. **Stretching to fit.** If the alignment feels forced ("kind of fits Problem 2 if we squint"), say so. Better to capture as outlier than fake the fit.
3. **Thin material with no banks to pull from.** If 3 drill rounds have not surfaced specifics and the banks are empty for this angle, save with TODOs and suggest running `vid-capture` to fill banks before `vid-framing`.

## Reference index

| Reference file | When to read it |
|---|---|
| `references/mode-conversation-examples.md` | Every run. Mock dialogues per mode (good + bad examples) so you calibrate the conversational shape before running it. |
| `knowledge/iceberg-and-top-3-alignment.md` | Phase 4. The 2-layer alignment gate decision flow with worked examples and near-misses. |
| `references/push-vs-pause-rules.md` | Phase 5. When to drill, when to save with TODOs, how to bail without burning the conversation. |
| `knowledge/story-capture-guide.md` | Mode 7 (story-first) and any mode where a thin story needs drilling. The 6 dynamic prompts plus reframes plus pivots. |
| `knowledge/vault-integration.md` | Phase 6. Frontmatter schema for `brain-dump.md`. Wikilink rules for bank pulls. |
| `foundation/creator-foundation.md` | Every run. Iceberg statement + Top 3 problems + audience. Drives the alignment check. |
| `foundation/voice-profile.md` | Every run. Words avoided, opener pattern, energy. Drives the AI's mirroring style. |

## Principles (the why behind the rules)

- **The brain dump IS the voice.** Every word the creator says is voice fuel for downstream writing skills. Polish it and you erase the voice. Mirror back, save verbatim where you can.
- **Fast and pleasurable beats thorough and exhausting.** A 5-minute conversation that captures 80% of what the creator has is better than a 20-minute conversation that captures 95% but burns them out. Downstream skills can chase gaps.
- **Alignment is a sanity check, not a tax.** Iceberg + Top 3 alignment takes 10 seconds to confirm if the dump fits. The check exists to catch wrong-channel videos early, not to interrogate every dump.
- **Outliers are creator decisions, not AI blocks.** Flag, explain consequence, let the creator override. The frontmatter records what was deliberate.

## Related skills

- `/foundation` produces the iceberg + Top 3 + audience this skill reads
- `vid-ideas` (optional front-door) hands this skill a picked-idea seed when the creator started blank on what to make
- `vid-voice-capture` produces the voice profile this skill reads
- `vid-capture` fills the story / proof / metaphor / testimonial banks this skill pulls from
- `vid-framing` reads the brain-dump.md this skill produces and locks the angle, format, goal
- `vid-pipeline` (future) invokes this skill at the start of the SCRIPT phase
