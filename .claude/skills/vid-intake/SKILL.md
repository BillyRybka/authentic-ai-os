---
name: vid-intake
description: Capture raw video material into a structured brain-dump.md for one video, in the creator's exact words. Auto-detects which of 7 intake modes the creator is in (idea, notes or outline, own transcript, inspired-by a competitor, news-jacking, client win, story-first) and runs the matching short conversation. Runs standalone or via vid-pipeline. Use whenever a creator brings video material not yet captured into a piece folder, even if they don't say "intake": "I want to make a video about X", "here's a transcript I want to turn into a video", "I saw this competitor video and want my own take", "I had this thing happen", "a video on my client win", "there's a new feature to cover", "let's start a new video", "let's plan this one out".
---

> 🔄 **Pre-flight (mandatory).** Before anything else, read `${CLAUDE_PLUGIN_ROOT}/knowledge/update-check.md` and follow it. If a newer version exists, halt and tell the creator. Otherwise continue.

# Video Intake

Capture the raw material for one video into `content/pieces/{slug}/brain-dump.md`, in the creator's exact words, in 5-10 minutes. The brain dump is the voice fuel every downstream writing skill reads, so the words stay verbatim, never polished. Intake captures only. It does not frame, title, or write. `vid-framing` runs next.

## What loads, and when

Cold open. You do not need the creator's identity or a schema to start listening, so load nothing up front.

- **Check at startup:** `foundation/creator-foundation.md` exists. If it does not, tell the creator to run `/foundation` first, and stop. (If `vid-pipeline` routed you here, it already verified this. Skip the re-check.)
- **Load on-demand, only at the phase that needs it:**

| File | Phase | For |
|---|---|---|
| `foundation/creator-foundation.md` | 4 (fit) | the iceberg statement and pillars |
| `knowledge/story-capture-guide.md` | 5, thin story | the 6 drill prompts |
| `references/push-vs-pause-rules.md` | 5 | when to drill, when to save with a TODO |
| `references/verify-subagent.md` | 5, uncertain claim | the isolated verification sub-agent |
| `knowledge/vault-integration.md` | 6 (save) | frontmatter schema and bank wikilink rules |
| `references/mode-conversation-examples.md` | optional | full worked dialogues for any mode |

## How it runs

**Standalone:** the creator invokes directly. Run the flow, create the piece folder, save, point them to `vid-framing`.

**As a sub-skill:** `vid-pipeline` invokes it, often with context (`intake for piece={slug}, mode=inspired-by, source=[...]`). Skip mode detection and go straight to the flow, then return the brain-dump packet to the caller.

The save (piece folder, `brain-dump.md`, `piece.md`) happens here either way.

## The flow

Six phases, same spine for every mode. The body of each phase varies by mode (see the modes table). Quoted lines show register and length, not a script: short, human, one move per message. Never paste one verbatim.

1. **Detect the mode, silently.** Read the creator's first message and route using the modes table. Do not announce the mode or make the creator confirm it. Just open the door. Surface the menu only when you genuinely cannot tell.

2. **Open the door, then listen.** "Brain dump whenever you're ready, I'll capture as you go." Then stop. Do not interrupt mid-dump. Read-once, respond-once.

3. **Reflect back.** Mirror what landed, in the creator's own language: the points, stories, claims, proof, metaphors, and any gaps. "Got [point 1], [point 2], plus the [thing] story. Miss anything?" Thirty seconds. It builds trust and surfaces what you missed.

4. **Fit and pillar, in one move.** Load `creator-foundation.md` now. Run one check that does both jobs at once, does this fit the iceberg and which pillar: "That fits your channel, looks like your [pillar] pillar. Right?" Set `iceberg_aligned` and lock the pillar from their answer. If it is a deliberate stretch, set `true` plus a one-line `alignment_note` in their words. If it does not fit, set `false`, ask "wrong channel, or has your iceberg shifted?", and let them decide whether to save anyway. Never block the save. The flag plus any note tells downstream skills the call was deliberate.

5. **Offer one deeper pass, then flow.** You are a co-writer, not a stenographer, so do not just bank the dump and move on. Scan it, pick the 2-3 spots where a little more would sharpen the video most, and offer once: "This is solid. I can push on [spot A] and [spot B], or save as-is?" Theirs to decline. If they say go, just ask the questions, one at a time, in the flow of the conversation. Do not re-ask permission before each one. Asking "can I ask another?" right after they already said yes is what breaks the flow. Keep pulling while they stay engaged and the answers keep coming back richer; a strong dump here pays off in every downstream skill. Worth pushing on:
   - A claim with no mechanism. "Why is that actually true, what's underneath it?"
   - A story referenced but not landed. "What was the exact moment it turned?"
   - The viewer's objection left unanswered. "What's the pushback, and your answer?"
   - The contrarian edge under-sharpened. "What's the version people argue with?"

   These pull more out of the creator. They never invent. **Verify, do not replace:** when the creator brings something real but uncertain (a stat, a claim, a metaphor), do not water it down or swap in something safer. That safe-generic reach is what makes slop. Spawn the isolated verification sub-agent (`references/verify-subagent.md`) and act on its verdict: holds, keep it verbatim with a note and sources; does not hold, tell them what's true in one line and let them adjust; can't confirm, mark a TODO and keep it. Never research inline. **Stop the moment they signal done** (save it, I'll come back, that's it): respect it, mark a TODO for anything left open, and save. Do not reopen a spot they closed, and never push one spot more than twice. For a thin story, use the prompts in `knowledge/story-capture-guide.md`; if 3 in a row don't land, save with a TODO.
   
6. **Slug, folder, save.** Propose a kebab-case slug from the topic they named (not the generic iceberg) and fold the confirm into the save rather than a separate round. Find where this vault's pieces already live and create the new `{slug}/` folder alongside them: the default is `content/pieces/{slug}/`, but if a `pieces/` directory already sits at the vault root, put it there. List the directory and confirm against what exists. Do not blind-stack a path or let `mkdir -p` invent a wrong parent. Write `brain-dump.md` and `piece.md` (load `knowledge/vault-integration.md` for the schema). Do not create the folder before the slug is settled (no orphan folders). Close in one line: "Saved as `cardio-vs-strength-for-founders`. vid-framing next."

## The 7 modes (internal routing, never shown to the creator)

Route on the creator's opening message. Every mode runs the same spine. Only the opener and the one or two distinctive moves change.

| Mode | Opening signal | What differs from the default |
|---|---|---|
| **Idea + dump** | Talks a topic through conversationally | The default. Open the door, let them dump freely. |
| **Notes / paste** | Pastes bullets or a doc | Scan it. Only drill the placeholders, or the bullet they flag as the anchor. Leave the full thoughts alone. |
| **Own transcript** | Pastes a wall of text | Ask "yours, or someone else's?" first (this splits it from inspired-by). Read silently, once. Reflect what's there and what's missing. |
| **Inspired-by** | Points at a competitor video, article, or podcast | Set the contract up front: the source is invisible, never named in the video. Capture source points into `source_internal_only`. Get the creator's take per point, then force "what's the lesson you teach?" |
| **News-jacking** | A fresh release, feature, or event | Skip the dump. Three fast questions: what's the news, what it means for the audience, their angle. Speed wins. |
| **Client win** | Opens with a result or a client name | Capture the proof fast, then force the pivot: "what's the principle the viewer can DO?" A case study teaches; it is not a client biography. |
| **Story-first** | "This thing happened..." | Capture the moment in P-A-O (problem, action, outcome) before anything else. Then locate the lesson. Never ask for the lesson first. |

When you cannot tell, ask once: "Quick check, which is this: an idea to think through, notes you have, a transcript you recorded, something you saw and want your own take on, fresh news, a client win, or a story?" Then run the matching row. Full worked dialogues for any mode live in `references/mode-conversation-examples.md`.

## Output: brain-dump.md

```yaml
---
type: brain-dump
slug: {kebab-case-slug}
intake_mode: idea | notes | own-transcript | inspired-by | news-jacking | client-win | story-first
captured: YYYY-MM-DD
iceberg_aligned: true | false
alignment_note: "{Only when the fit is a deliberate stretch or an off-iceberg save. One line in the creator's words. Omit the field entirely for a clean fit.}"
source_internal_only: "{Inspired-by mode only: a brief internal note on the source. Never referenced in the video.}"
---

## Raw dump (verbatim)

{The creator's complete dump, exactly as said. Nothing cut, reordered, or cleaned beyond obvious transcription fixes. This is the lossless source of truth; every section below is an index built from it. For paste modes (own-transcript, inspired-by) this is the pasted text in full.}

## Topic + angle

{The topic and angle in the creator's own words and sentence shapes, not a summary. No "The angle is that..." framing.}

## Audience

{Capture only. What the creator said about who this is for and why it matters to them, in their words. If they did not describe it, write "Not described in the dump." Do not invent a pain rationale.}

## Outcome

{Capture only. What they want the viewer to walk away with, in their words. If unstated, write "Not stated. vid-framing sets the core payoff." Never synthesize one, and never reduce a listicle to a single action.}

## Material

### Lessons / points
- {Each lesson in the creator's exact phrasing}

### Stories
- {A story or anecdote, including cautionary ones. [[story-bank/slug]] if pulled, or captured here in P-A-O shape.}

### Proof
- {Evidence something WORKS: a result, what you did, a testimonial. [[proof-bank/slug]] if pulled, or captured here.}

### Metaphors
- {[[metaphor-bank/slug]] if pulled, or captured here.}

### Claims (no proof attached yet)
- {Claim}. TODO: source proof from [bank or new capture]

## Strongest raw lines

- "{The creator's most vivid, quotable lines, verbatim. Stutters cleaned only, never reworded. This is the voice reservoir downstream skills pull from.}"

## Open questions / TODOs

- {Anything thin or missing the creator wants to chase later, or that vid-framing / vid-segment will need.}

## Source notes (internal only, never appears in the video)

{Inspired-by: the source's points, for the creator's reference. Own-transcript: the original transcript, lightly cleaned. Otherwise empty.}
```

## Output: piece.md

The per-piece identity ledger. vid-intake creates it; every downstream skill appends its own fields and never overwrites another's.

```yaml
---
type: content-piece
slug: {kebab-case-slug}
pillar: {pillar-slug or null}
status: ideating
created: YYYY-MM-DD       # today, stamped once, never changed
last_updated: YYYY-MM-DD  # today; every skill that writes piece.md bumps this
---
```

Set both dates to today. `created` is permanent; `last_updated` moves forward on every later write. The pillar comes from the Phase 4 fit check; if it stayed open, leave it null (not a blocker). Full downstream schema in `knowledge/vault-integration.md`.

## Rules (and why)

1. **The brain dump IS the voice.** Save the creator's words verbatim. Polishing erases the voice every downstream skill writes from.
2. **Raw first, organize second.** Put the complete dump in `## Raw dump (verbatim)` before sorting anything into Material. The organized sections are an index built from it; they never drop, reorder, or contradict it.
3. **No narrative framing in the saved body.** Write Topic, Outcome, and Material in the creator's own sentence shapes. Never "The angle is that...", "This lesson is about...". Reflect-back in chat can paraphrase; the saved dump never does.
4. **No AI-meta anywhere, frontmatter included.** If you would not say it out loud to the creator, do not write it.
5. **Capture everything, cut nothing.** Even overlapping or rhetorical lines. Deciding what is a standalone lesson, and merging overlaps, is `vid-structure`'s job, not intake's.
6. **Never fabricate.** The dump is the creator's words plus what they explicitly pull from banks. A gap becomes a TODO, never an invention: no made-up stories, numbers, clients, results, or proof.
7. **Proof is not Story.** Proof is evidence something works (a result, a testimonial). An anecdote, even a cautionary one, is a Story. Never file a story under Proof.
8. **Bank wikilinks use the `bank-dir/slug` form**, like `[[proof-bank/onboarding-5h-to-1h]]`. Never put the banks folder in the path.
9. **The save is always honest.** `iceberg_aligned` must be populated, true or false. Never block the save on it; record the call instead.
10. **No em-dashes.** Commas, periods, parentheses. Every save passes a Vale check.
11. **Push only when thin, and only as an offer.** One surgical question that unlocks the next layer, never a question battery. Two rounds with no unlock, mark a TODO and move on.
12. **Read-aloud is the final filter.** Before saving, if the creator would reword anything, capture the better wording.

## Creator decides (flag, explain, let them choose)

1. **Outlier video.** If `iceberg_aligned: false`, flag it at save and explain the cost (channel coherence erodes if outliers stack). Their call.
2. **Stretching to fit.** If the fit feels forced, say so. Better an honest off-iceberg save than a faked fit.
3. **Thin material, empty banks.** If drilling has not surfaced specifics and the banks are empty for this angle, save with TODOs and suggest `vid-capture` to fill the banks before `vid-framing`.
