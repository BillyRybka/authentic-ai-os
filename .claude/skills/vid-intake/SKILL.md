---
name: vid-intake
description: Capture raw video material into a structured brain-dump.md for one video. Auto-detects which of 7 intake modes the creator is in (idea + dump, outline paste, own transcript, inspired-by, news-jacking, client win, story-first), runs the matching short conversation, confirms the idea fits the channel (iceberg), saves to content/pieces/{slug}/brain-dump.md. The creator's exact phrasing is preserved verbatim because the brain dump IS the voice for every downstream writing skill. Anti-fabrication. Adaptive drilling. Target 5-10 minutes, never an interrogation. Runnable standalone OR invoked by vid-pipeline. Use whenever a creator brings video material not yet captured into a piece folder, even if they don't say "intake": "I want to make a video about X", "here's a transcript I want to turn into a video", "I saw this competitor video and want my own take", "I had this thing happen", "a video on my client win", "there's a new feature to cover", "let's start a new video", "let's plan this one out".
---

> 🔄 **Pre-flight (mandatory).** Before doing anything else, read `${CLAUDE_PLUGIN_ROOT}/knowledge/update-check.md` and follow it. If a newer version exists, halt and tell the creator. If you're up to date, continue with the skill below.

# Video Intake

Captures whatever raw material the creator brings and produces a structured `content/pieces/{slug}/brain-dump.md` that downstream skills (`vid-framing`, `vid-structure`, `vid-segment`, `vid-intro`, `vid-ending`) read at runtime. Seven intake modes covering the realistic ways a creator starts a video. Auto-detects mode, runs the matching short conversation, locks iceberg fit, saves.

**Scope boundary:** vid-intake captures raw material only. It does NOT pick the format (`vid-framing` does that), does NOT generate angle framings (`vid-framing`), does NOT write any script content (`vid-intro`, `vid-segment`, `vid-ending`). Light fit check (iceberg) happens here so downstream skills don't waste time on a video that does not fit the channel. Full angle framing and Core Payoff selection happen in `vid-framing` next.

## What this produces

`content/pieces/{slug}/brain-dump.md` with creator's exact phrasing preserved, plus the iceberg fit locked. Voice fuel for every downstream writing skill.

When invoked as a sub-skill (e.g. by vid-pipeline to start a new piece), it also returns the brain-dump packet to the caller. The save (the piece folder, brain-dump.md, and piece.md) still happens here, in both modes.

## When to run this

- Creator has a video to start and the piece folder does not exist yet
- Creator wants to dump material for a video they have been thinking about
- Orchestrator (`vid-pipeline`) invokes it to start a new piece
- Creator just had an experience or got a client win and wants to capture it before it fades
- `vid-ideas` hands over a picked-idea seed packet (the front-door, when the creator started blank). Run the matching mode (usually idea + dump) seeded from `{idea_title, pillar, iceberg_fit, anchor}`, then drill for the material.

## Prerequisites

Hard requirement:

- `foundation/creator-foundation.md` exists (iceberg + audience). vid-intake checks that it exists at the top, so a creator with no foundation bails before investing a full dump. It loads the iceberg content later, at the fit check (Phase 4), not up front.

If foundation is missing, tell the creator to run `/foundation` first.

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

Mode detection happens from the creator's opening message. If ambiguous, surface a short menu and ask. The one-line cues above are enough to route on a normal run. Open `references/mode-conversation-examples.md` (full mock dialogues per mode, worked examples and near-misses) only as a fallback, when a conversation stalls and you need calibration.

## The walkthrough

Same shape every mode runs. The body of each mode varies (see references), but the spine is universal.

Every quoted line below shows register and length, not a script. Respond to what the creator actually said. Never paste one verbatim. The point is the feel: short, human, one move per message.

### Phase 1: Detect mode (cold open)

Load nothing at open. The brain dump is the creator's raw words, you do not need their identity or a schema to start listening. Every reference this skill uses loads later, only at the phase that needs it (see the Reference index). When vid-pipeline routed you here, foundation existence was already verified, so do not re-check it here.

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

### Phase 4: Iceberg fit + pillar

Load `foundation/creator-foundation.md` now (the iceberg statement and the pillars) and run one fast check that does two jobs at once: does this fit the channel, and which pillar does it sit in. This is the first heavy load in the skill, and it lands after the dump, where it is actually used. (When vid-pipeline routed you here, foundation was already verified to exist; that guard skips the existence re-check, never this content load.) Surface format, proposing the most likely pillar in the same breath as the fit:

> "That fits your channel, looks like your [pillar] pillar. Right?"

Possible creator responses:

- YES → confirmed. Set `iceberg_aligned: true` and lock the pillar they confirmed. Move to Phase 5. Do NOT ask the pillar again at save.
- YES on fit, different pillar → set `iceberg_aligned: true`, lock the pillar they name instead.
- NO, fits the iceberg but feels like a stretch → set `iceberg_aligned: true`, add a one-line `alignment_note` in the creator's words, settle the pillar, move on.
- NO, does not fit the iceberg → set `iceberg_aligned: false`. Ask "wrong channel for this one, or has your iceberg shifted?" If shifted, point at /foundation refresh. Otherwise capture a one-line `alignment_note` and let the creator decide whether to save anyway.

Never block the save. The creator's call. If no pillar maps cleanly, leave it open (null is fine, not a blocker). The `iceberg_aligned` flag plus any `alignment_note` signal to downstream skills that the call was deliberate.

### Phase 5: Offer one deeper pass

You are a co-writer, not a stenographer. Never silently accept the dump and move on. After the reflect-back, scan the material, pick the 2-3 spots where a little more would most sharpen the video, and offer:

> "This is solid. I can push on a couple things to sharpen it: [spot A], [spot B]. Want to, or save as-is?"

If the creator says save, go to Phase 6. If they want to go, ask the pointed questions one at a time, fast. This is an offer, not an interrogation, and it is theirs to decline.

**What makes a spot worth pushing on (pick the 2-3 highest-leverage, never all of them):**
- A claim stated without its mechanism. "Why is that actually true, what's the reason underneath it?"
- A story referenced but not landed. "What was the exact moment it turned? Tell me that, not the lesson."
- The viewer's objection left unanswered. "What's the pushback on this, and your answer to it?"
- A nuance the creator gestured at but did not open. "You said [X] like there's more there. What's the rest?"
- The contrarian edge under-sharpened. "What's the disagreeable version, the part people argue with?"
- The stakes or the "why now" missing. "Why does this matter to them right now?"

These pull more out of the creator. They never invent content; the creator supplies every answer.

**Verify, don't replace.** When the creator brings something real but uncertain (a metaphor, a stat, a claim), do NOT dismiss it, water it down, or swap it for something safer. That safe-generic reach is the exact instinct that makes slop. Verify the real thing first. Spawn an isolated verification sub-agent (its own context window, so the research never clutters this conversation) using the template in `references/verify-subagent.md`, and act on what it returns: holds → keep the material verbatim plus a one-line verified note and sources; does not hold → tell the creator in one line what is actually true, let them adjust or drop it; can't confirm → mark a TODO, keep the material. Never research inline.

**When to stop:** the creator says "stop, just save", or "I'll come back to that" (respect it, mark a TODO), or 2 rounds on one spot have not unlocked (bail, mark a TODO). The detail on pacing lives in `references/push-vs-pause-rules.md`.

When drilling on a thin story, use the dynamic 6 prompts from `knowledge/story-capture-guide.md`. Do not run all 6. Pick the prompt that fits the topic and the avatar's pain. If the first prompt does not unlock in 1-2 rounds, pivot to the next-best prompt. If 3 prompts in a row do not land, save the dump with a TODO that says "story missing for [point X], capture next session."

### Phase 6: Propose slug, create folder, save

Once the dump is captured and aligned:

1. Propose a kebab-case slug. Source from the topic the creator named, not from the iceberg (the iceberg is generic, the slug is specific to this video).
2. Confirm slug with creator in one short message: `slug: "frequency-vs-depth-on-youtube"`, sound right?
3. Find where this vault's pieces already live, and create the new `{slug}/` folder alongside them. The default layout is `content/pieces/{slug}/`, but the existing pieces are the source of truth: if a `pieces/` directory already sits at the vault root (the root is itself the content folder), put the new piece there, do NOT stack a second `content/` on top of it. List the directory and confirm against what exists rather than blind-stacking the literal path or letting `mkdir -p` invent a wrong parent.
4. Write `brain-dump.md` into that folder per the schema below. Load `knowledge/vault-integration.md` now (at save) for the frontmatter schema and the wikilink rules for bank pulls.
5. Write `piece.md` into the same folder with the intake frontmatter (the per-piece identity ledger every downstream skill appends to), including the `pillar` settled in the fit check (Phase 4). Do NOT ask the pillar again; if the fit check left it open, it stays null (not a blocker). See the piece.md schema below.
6. Confirm save in one line: "Saved. `vid-framing` next to lock the angle."

Do not create the folder before slug is confirmed. No orphan empty folders.

## Output schema (brain-dump.md)

```yaml
---
type: brain-dump
slug: {kebab-case-slug}
intake_mode: idea | notes | own-transcript | inspired-by | news-jacking | client-win | story-first
captured: YYYY-MM-DD
iceberg_aligned: true | false
alignment_note: "{Optional. Only when the fit is a deliberate stretch or an off-iceberg save. One line in the creator's own words on why it was kept. Omit the field entirely for a clean fit. Never paraphrase or add an AI-meta justification.}"
source_internal_only: "{Optional. For inspired-by mode: brief internal note about source piece. NEVER referenced in productized video.}"
---

## Raw dump (verbatim)

{The creator's complete dump for this video, exactly as they said it. Nothing cut, nothing reordered, nothing cleaned beyond obvious transcription fixes. This is the lossless source of truth; every organized section below is an index built from this and must never drop, reorder, or contradict it. For paste input (own-transcript, inspired-by) this is the pasted text in full.}

## Topic + angle

{The topic and angle in the creator's OWN words and sentence shapes, not a summary of them. Use what they actually said. Do not open with "The angle is that..." or any narrative framing.}

## Audience

{Capture only. Add only what the creator actually said about who this is for and why it matters to them, in their words. Do NOT invent a "why this avatar feels this pain right now" rationale they did not say. If they did not describe the audience, write "Not described in the dump."}

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
- **No AI-meta narration anywhere, including frontmatter.** Fields like `alignment_note` and the Audience section read plainly or in the creator's words. Never write "the thesis of this is...", "Reinforces X", or similar AI-meta phrasing. If you would not say it out loud to the creator, do not write it.
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
3. **No fit captured.** Never save brain-dump.md without the `iceberg_aligned` field populated. Frontmatter has to be honest.
4. **Em-dashes.** Brand-level no. Use commas, periods, parens. Every save passes a Vale check.
5. **"Avatar" replaced with vague terms.** Avatar is specific. Do not soften to "audience" in foundation references. It's the constructed profile of the viewer/buyer per `creator-foundation.md`.

## Soft friction (surface and explain, creator decides)

1. **Outlier video.** If `iceberg_aligned: false`, flag at save time. Explain consequence (channel coherence drops over time if outliers stack). Creator decides.
2. **Stretching to fit.** If the fit feels forced ("kind of fits your lane if we squint"), say so. Better to capture as an off-iceberg save than fake the fit.
3. **Thin material with no banks to pull from.** If 3 drill rounds have not surfaced specifics and the banks are empty for this angle, save with TODOs and suggest running `vid-capture` to fill banks before `vid-framing`.

## Reference index

| Reference file | When to read it |
|---|---|
| `references/mode-conversation-examples.md` | Fallback only. Open if a conversation stalls and you need calibration. The one-line mode cues in the skill are enough on a normal run. |
| `references/push-vs-pause-rules.md` | Phase 5. When to drill, when to save with TODOs, how to bail without burning the conversation. |
| `references/verify-subagent.md` | Phase 5, when the creator brings uncertain but checkable material. The isolated verification sub-agent prompt and how to act on its verdict. |
| `knowledge/story-capture-guide.md` | Mode 7 (story-first) and any mode where a thin story needs drilling. The 6 dynamic prompts plus reframes plus pivots. |
| `knowledge/vault-integration.md` | Phase 6 (save). Frontmatter schema for `brain-dump.md`. Wikilink rules for bank pulls. |
| `foundation/creator-foundation.md` | Phase 4. The iceberg statement, for the fit check. Loaded after the dump, never at open. |

## Principles (the why behind the rules)

- **The brain dump IS the voice.** Every word the creator says is voice fuel for downstream writing skills. Polish it and you erase the voice. Mirror back, save verbatim where you can.
- **Fast and pleasurable beats thorough and exhausting.** A 5-minute conversation that captures 80% of what the creator has is better than a 20-minute conversation that captures 95% but burns them out. Downstream skills can chase gaps.
- **The fit check is a sanity check, not a tax.** The iceberg fit check takes 10 seconds to confirm if the dump belongs on the channel. It exists to catch wrong-channel videos early, not to interrogate every dump.
- **Outliers are creator decisions, not AI blocks.** Flag, explain consequence, let the creator override. The frontmatter records what was deliberate.

## Related skills

- `/foundation` produces the iceberg + audience this skill reads
- `vid-ideas` (optional front-door) hands this skill a picked-idea seed when the creator started blank on what to make
- `vid-capture` fills the story / proof / metaphor / testimonial banks this skill pulls from
- `vid-framing` reads the brain-dump.md this skill produces and locks the angle, format, goal
- `vid-pipeline` invokes this skill to start a new piece
