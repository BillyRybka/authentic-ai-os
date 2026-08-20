---
name: vid-intake
description: Capture raw video material into a structured brain-dump.md for one video, in the creator's exact words. One short capture conversation whether the creator talks the idea through or pastes notes or a transcript, then hands off to vid-framing. Runs standalone or via vid-pipeline. Use whenever a creator brings video material not yet captured into a piece folder, even if they don't say "intake", like "I want to make a video about X", "here's a transcript I want to turn into a video", "I had this thing happen", "a video on my client win", "there's a new feature to cover", "let's start a new video", "let's plan this one out". Not for deciding the angle (vid-framing) or writing anything (vid-structure onward).
---

# Video Intake

Get everything the creator has about one video onto disk in their own words, then pull out what they know but did not say.

Two files: `content/pieces/{slug}/brain-dump.md` and `piece.md`. Intake captures. It never frames, structures, or writes.

If `foundation/iceberg.md` does not exist, tell them to run `/foundation` first and stop.

## The conversation

**1. Take the dump.** They talk it through, or they paste notes or a transcript. Either way, read once and respond once. Never make them re-say what they already wrote. For a pasted transcript, confirm it is theirs before you treat it as their voice.

The moment you know the topic, put the piece on disk. Slug is kebab-case from the topic they named. List the pieces directory first (`content/pieces/`, or `pieces/` if that sits at the vault root) so the slug is unique and no path gets invented. Write `piece.md` from `templates/output-piece-md.md`. Save quietly.

**2. Mirror it back.** Their points, stories, claims, proof, metaphors, in their language. Ask what you missed. Then write `brain-dump.md` from `templates/output-brain-dump-md.md` before you dig, so a dropped session cannot lose their words. Leave `iceberg_aligned` unset. Save quietly.

**3. Dig until it's sharp.** Read `references/digging-deeper.md`.

**4. Check the fit.** Read `foundation/iceberg.md`. One line: confirm it fits and name the likely pillar. Let them correct either. Set `iceberg_aligned` and the pillar in `piece.md` from their answer. A deliberate stretch is `true` plus a one-line `alignment_note` in their words. A miss is `false`, and you say plainly that a channel of outliers stops meaning anything, then save whatever they decide. Never block the save.

**5. Close.** Both files are already written. Confirm in one line and point at `vid-framing`.

If they bail at any point, their words are safe from step 2. Leave `status: ideating` with the open TODOs and `iceberg_aligned` unset.

## What you are capturing

Save what they said, the way they said it. Polishing erases the voice every later skill writes from. The `## Raw dump` section is complete and verbatim before anything gets sorted into Material, and the sorted sections never drop or contradict it.

Everything in the file came out of the creator's mouth or a file that exists on disk. A gap is a TODO, never an invention. That covers stories, numbers, clients, results, proof, and bank wikilinks alike.

Some things you would otherwise get wrong:

- **A story** ("this thing happened") gets captured as the moment first, problem then action then outcome, and the lesson second. Ask for the lesson first and you get a summary instead of a scene. Thin story: `knowledge/story-capture-guide.md`.
- **A client win** gets the proof captured fast, then pivots to the principle a viewer can go do. A case study teaches. It is not a biography.
- **Something uncertain** gets verified, never swapped for something safer. Run `references/verify-subagent.md`. Never research inline.
- **Proof is evidence something works.** A result, a testimonial. An anecdote is a Story even when it is cautionary.
- **People stay plain text.** Capture the name as they said it. No wikilink, no `people/` stub. Downstream creates the profile if the material ever becomes a bank entry.
- **Bank wikilinks are `bank-dir/slug`**, like `[[proof-bank/onboarding-5h-to-1h]]`. No banks folder in the path. Only link what they actually pulled and what exists, because a link to nothing looks connected and isn't.

Stamp `intake_mode` for what the material turned out to be. It is a record, not a decision, and the creator never hears it.

## How you talk

Earn every turn. Most of this skill is you being quiet while they dump and writing files without narrating it.

When you do speak: no announcing what you are about to do, no "Great" or "Perfect" openers, no play-by-play. Report a save afterward, past tense, one line. Short turns stay short.

No em-dashes anywhere, frontmatter included. Every save passes Vale.

Read the saved dump aloud in your head before you write it. If the creator would reword it, you captured it wrong.
