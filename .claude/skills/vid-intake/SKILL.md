---
name: vid-intake
description: Capture raw video material into a structured brain-dump.md for one video, in the creator's exact words. One short capture conversation whether the creator talks the idea through or pastes notes or a transcript, then hands off to vid-framing. Runs standalone or via vid-pipeline. Use whenever a creator brings video material not yet captured into a piece folder, even if they don't say "intake": "I want to make a video about X", "here's a transcript I want to turn into a video", "I had this thing happen", "a video on my client win", "there's a new feature to cover", "let's start a new video", "let's plan this one out".
---

> 🔄 **Pre-flight (mandatory).** Before anything else, read `${CLAUDE_PLUGIN_ROOT}/knowledge/update-check.md` and follow it. If a newer version exists, halt and tell the creator. Otherwise continue.

# Video Intake

Capture the raw material for one video into `content/pieces/{slug}/brain-dump.md`, in the creator's exact words (minus obvious mistakes). Intake captures only. It does not frame, title, or write. `vid-framing` runs next.

## What loads, and when

- **Check at startup:** `foundation/creator-foundation.md` exists. If it does not, tell the creator to run `/foundation` first, and stop. (If `vid-pipeline` routed you here, it already verified this. Skip the re-check.)
- **Load on-demand, only at the phase that needs it:**

| File | Phase | For |
|---|---|---|
| `references/digging-deeper.md` | 3 (deeper pass) | which spots to push, when to save with a TODO |
| `references/verify-subagent.md` | 3, uncertain claim | the isolated verification sub-agent |
| `knowledge/story-capture-guide.md` | 3, thin story | the 6 drill prompts |
| `foundation/creator-foundation.md` | 4 (fit) | the iceberg statement and pillars |
| `knowledge/vault-integration.md` | 2 (checkpoint save) | frontmatter schema and bank wikilink rules |
| `references/mode-conversation-examples.md` | optional | worked example dialogues of the capture flow |

## The flow

Five phases, one spine, every time. What the creator hands you shifts how you open, never the spine. Each move is one short, human message in your own words, never a script.

1. **Open the door.** Clock what they brought and open to match, silently, never naming a category. If they are talking it through, tell them in your own words to dump everything raw and to flag if they want help digging in, then stop and let them land it without interrupting. If they pasted notes or a transcript, read it once and do not make them re-say what they wrote (for a transcript, confirm it is actually theirs first, so you treat it as their voice). If a caller handed you material to start from (for example `vid-ideas` passing a picked idea), run with it. Read once, respond once.

2. **Reflect back, then checkpoint the dump.** Mirror what landed in the creator's own language, the points, stories, claims, proof, metaphors, and any gaps, and ask if you missed anything. Then get their words on disk before you dig, so a dropped session never loses the dump. Derive a kebab-case slug from the topic they named (not the generic iceberg), and find where this vault's pieces live (default `content/pieces/{slug}/`; if a `pieces/` directory sits at the vault root, use that). List the directory and check against what exists, never blind-stack a path or let `mkdir -p` invent a parent. Write `brain-dump.md` and `piece.md` with `status: ideating` (schema in `knowledge/vault-integration.md`), leaving `iceberg_aligned` unset until the fit step so the checkpoint cannot trigger anything downstream. Save quietly, no confirmation round.

3. **Offer one deeper pass, updating as you go.** Open `references/digging-deeper.md` now; it calibrates which spots are worth pushing and when to pause. You are a co-writer, not a stenographer: name the 2-3 highest-leverage spots and offer once to push or save as-is. If they say go, ask in flow, one question at a time, no re-asking permission before each. Every answer that lands is new material: add it to `brain-dump.md` as it comes, in their words, and clear or add TODOs. Stop the moment they signal done (save it, I'll come back, that's it), never push one spot more than twice, and never invent to fill a gap, a gap is a TODO. If the creator brings something uncertain, verify it with `references/verify-subagent.md` rather than swapping in something safer; never research inline. For a thin story, use the prompts in `knowledge/story-capture-guide.md`.

4. **Fit and pillar, in one move.** Load `creator-foundation.md` now. In one line, confirm it fits the iceberg and name the most likely pillar, and let them correct either. Set `iceberg_aligned` and lock the pillar in `piece.md` from their answer. If it is a deliberate stretch, set `true` plus a one-line `alignment_note` in their words. If it does not fit, set `false`, ask whether it is the wrong channel or their iceberg has shifted, and let them decide whether to save anyway. Never block the save. The flag plus any note tells downstream skills the call was deliberate.
   
5. **Finalize and hand off.** The piece is already on disk from the checkpoint, so this is the close, not a first write. Make sure `brain-dump.md` holds everything the deeper pass surfaced and `piece.md` carries the fit and pillar, then confirm the save in one line and point to vid-framing as next. If the creator bailed earlier, their words are already safe from the checkpoint; leave it at `status: ideating` with the open TODOs, and the missing fit (`iceberg_aligned` still unset) is what tells the pipeline the piece still needs intake when they come back.

## What's in the dump (internal, never shown to the creator)

There is one intake: the creator's own material, talked through or pasted. The spine never changes. As you capture and reflect, watch for these shapes and handle them. They are not separate flows, just the things you would otherwise get wrong.

- **A story** ("this thing happened") → capture the moment in P-A-O (problem, action, outcome) first, locate the lesson second. Never ask for the lesson first.
- **A client win or result** → capture the proof fast, then force the pivot to the principle the viewer can DO. A case study teaches; it is not a client biography.
- **Fresh news or a release** → keep it fast. What is the news, what it means for the audience, their angle. Speed wins; do not force a full dump.
- **A claim with no proof** → get the source, or mark it a TODO. Never invent one.

Stamp `intake_mode` for what the material turned out to be (idea, notes, own-transcript, news-jacking, client-win, story-first). It is a record, not a routing decision, and the creator never hears it. Worked example dialogues live in `references/mode-conversation-examples.md`.

## Output: brain-dump.md

```yaml
---
type: brain-dump
slug: {kebab-case-slug}
intake_mode: idea | notes | own-transcript | news-jacking | client-win | story-first
captured: YYYY-MM-DD
iceberg_aligned: true | false
alignment_note: "{Only when the fit is a deliberate stretch or an off-iceberg save. One line in the creator's words. Omit the field entirely for a clean fit.}"
---

## Raw dump (verbatim)

{The creator's complete dump, exactly as said. Nothing cut, reordered, or cleaned beyond obvious transcription fixes. This is the lossless source of truth and the voice reservoir every downstream skill pulls from; the sections below are a light index built from it. For a pasted transcript or doc, this is the pasted text in full.}

## Topic

{What the video is about, in the creator's own words and sentence shapes, not a summary. Capture the topic only. The angle is vid-framing's job; do not name one here.}

## Audience

{Only if the creator described who this is for and why it matters to them, in their words. Omit the section entirely if they did not raise it. Never invent a pain rationale.}

## Outcome

{Only if the creator stated what they want the viewer to walk away with, in their words. Omit the section if unstated; vid-framing sets the core payoff. Never synthesize one, and never reduce a listicle to a single action.}

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

## Open questions / TODOs

- {Anything thin or missing the creator wants to chase later, or that vid-framing / vid-segment will need.}
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
