---
name: vid-voice-capture
description: Capture the creator's voice by curating real passages they wrote or said into reference pieces, plus a thin guardrail of refusals and signature phrases. The reference pieces are the voice engine every writing skill writes from; the guardrail is the short list of what the creator refuses to say. Triggers on "build my voice profile", "capture my voice", "deepen voice profile", "refresh voice profile", "extract my voice", "analyze my writing voice", "voice capture", "my voice profile is outdated", or when a writing skill flags voice drift.
---

# Voice Capture

Voice is reproduced from the creator's real sentences, not from a description of them. This skill does two things:

1. Curates **reference pieces**: real passages the creator produced, written into `foundation/reference-pieces/{voice_context}.md` (one file per populated context, passages inside as `## ` sections). This is the voice engine. Every writing skill writes from these.
2. Writes a **thin guardrail**: `foundation/voice-profile.md`. Fingerprint, signature phrases, refusals, POV and energy. The short list of what examples cannot teach.

No statistics are stored. Rhythm is judged by ear against the reference pieces at validation time. Read [[voice-profile-schema]] for the full contract. `/foundation` does not write these files.

> **Resolving `knowledge/` paths.** Any path written `knowledge/X.md` is a plugin reference file. Load it from `${CLAUDE_PLUGIN_ROOT}/knowledge/X.md` when running as an installed plugin. If `${CLAUDE_PLUGIN_ROOT}` is unset or that path does not exist (running from the source repo during development), load `knowledge/X.md` relative to the repo root instead.

Banned terminology: never say "voice locked" or "voice-locked drafting". The voice is preserved, never locked.

## What this produces

- `foundation/reference-pieces/{voice_context}.md`: one file per populated context. Inside: 3 to 8 stylistically representative passages as `## ` sections, intact, the creator's exact words, each opening with a `> Demonstrates:` line. Aim for 2 to 3 passages per major beat type the creator uses.
- `foundation/voice-profile.md`: the thin guardrail. Sections per [[voice-profile-schema]] (`voice_fingerprint`, `signature_phrases`, `refusals`, `pov_and_energy`, optional vid-intro orientation fields, `context_flex`, `sources_analyzed`, `update_log`). No rhythm or punctuation numbers.

A context with too little material gets no folder (no stub) and is noted in `context_flex`.

## Invocation modes

**Standalone.** The creator runs it directly: the first build after `/foundation`, or a refresh when the voice has drifted or new sources exist.

**Sub-skill.** A writing skill detects drift and invokes this to refresh from updated sources. Returns a wikilink to the refreshed guardrail.

## When to run

- After `/foundation`, once the creator has source material to bring.
- Quarterly, or after a medium/audience/tone shift.
- When a writing skill logs repeated drift, or the creator says "this doesn't sound like me anymore".

## Prerequisites

- `foundation/iceberg.md` and `foundation/avatar.md` exist (positioning and avatar shape how voice reads in context).
- Source material. Minimum viable depends on format-length: 3 to 5 pieces for short-form contexts (`shorts`, `linkedin`, `twitter`); 3 to 5 transcripts or ~5,000 words for long-form contexts (`youtube-script`, `tutorial`, `newsletter`, `podcast`, `talk`). Thinner runs still work but flag low confidence and defer contexts. Full floor in `references/voice-extraction-methods.md`.

## Load at session start

1. `knowledge/interview-posture.md`. Shared posture. Non-negotiable.
2. `knowledge/voice-profile-schema.md`. The two-artifact contract and load contract, including both artifacts' frontmatter.
3. `knowledge/vault-integration.md`. The foundation-doc schema `voice-profile.md` is written against, plus tag and naming conventions.
4. `foundation/iceberg.md` and `foundation/avatar.md`. Positioning and avatar.
5. `references/voice-extraction-methods.md` when curation starts. Source grouping, passage selection, guardrail build.
6. `knowledge/voice-pressure-test.md` at the read-aloud stage.

## Pre-check (silent)

Check for `foundation/voice-profile.md` and `foundation/reference-pieces/`.

- **Neither exists:** fresh run.
- **Both exist:** refresh. Surface the fingerprint and the populated contexts. Ask: refresh which contexts, keep, or replace.
- **Partial:** resume. Tell the creator what is captured and what is next.

## FIRST ACTION: create the task list

After the loads and the silent pre-check, create a TodoWrite list:

1. Source intake and grouping by `voice_context`
2. Passage selection per context
3. Guardrail build (cross-validated)
4. Assemble (write reference-piece folders + thin profile)
5. Read-aloud validation
6. Save and state the load contract

Mark `in_progress` on start, `completed` when the creator confirms and you move on.

## Stage 1: Source intake and grouping

Ask what content is available. Every source ends up as a file on disk in `raw/voice-sources/` before you analyze it. Working from disk keeps chat context clean and makes the files re-readable on a refresh run. Two ways the creator brings sources:

- **They point you at a folder or files.** Read them in place if already under `raw/voice-sources/`, otherwise copy them there.
- **They paste a transcript into chat.** Expected and fine. Do not refuse it. Write each pasted transcript to `raw/voice-sources/{slug}.txt` yourself (slug from what it is, e.g. `yt-4-blind-spots-ai.txt`), confirm the save, then work from the file. Never analyze a long paste inline.

As sources land, group each by `voice_context` (the medium/mode it was produced in): `youtube-script`, `tutorial`, `shorts`, `newsletter`, `linkedin`, `twitter`, `podcast`, `casual`, `talk`. Confirm which contexts clear the source floor (3 to 5 pieces for short-form; ~5,000 words or 3 to 5 transcripts for long-form, per `references/voice-extraction-methods.md`). Those earn a reference set. Thin contexts feed the guardrail only and are flagged. Record the source list and grouping in the worksheet (`assets/extraction-worksheet-template.md`).

## Stage 2: Diagnose the range, then select passages

Run `references/voice-extraction-methods.md` Step 2. It is the method; this Stage is the operational beats:

1. Read the context's sources and form the rough range picture Step 2 describes (a coverage lens, not a sorting job).
2. State that picture back to the creator in plain language and get it confirmed before selecting anything. Confirm-then-fill, not guess-pick-correct.
3. Select the passages per Step 2. Keep each passage intact (not trimmed of structure), verbatim. Give each one a `> Demonstrates:` line in plain language describing what it shows. The line describes; it is not a category to defend. Aim for 2 to 3 passages per major beat type the creator uses, intact.
4. Ask the creator directly: "Any moment you always deliver live and never want drafted (a personal beat, a closing ritual, a recurring ad-lib)?" Anything named here is a hard refusal for Stage 3, never a reference piece. This is the **exclusion rule (hard):** an improvised, creator-designated moment is never a seed.

## Stage 3: Guardrail build (cross-validated)

Walk every candidate pattern through the cross-validation test in [[voice-profile-schema]]: holds across sources and contexts goes to the guardrail; strong in one context stays in that context's reference pieces; single-source gets dropped or flagged.

Write only: `voice_fingerprint` (2 to 4 sentences), `signature_phrases` (verbatim cross-context quotes), `refusals` (anti-patterns including the global em-dash and clean-register rules; words-avoided as `word to swap (one-line reason)` with reason required; named creator hard rules), `pov_and_energy` (hard cap, two paragraphs, two sentences each), the vid-intro orientation fields only if clearly observed, and one `context_flex` line per populated context. Nothing else. Full spec in [[voice-profile-schema]].

**Filler check on signature phrases.** Recurrence is not enough. Before locking any `signature_phrases` candidate that matches a known-filler shape (`right?`, `you know`, `like`, `so`, `okay`, `alright`, `I mean`, `basically`, or anything that reads like a discourse marker), ask the creator: "this came up a lot, is it load-bearing for your voice or filler you'd cut?" Load-bearing stays. Filler moves to words-avoided with the reason `filler, drop unless the sentence needs it`. The hint list is a prompt for the question, not an auto-block. The creator's answer is the gate. This catches the regression at Stage 3 instead of waiting for the Stage 5 read-aloud.

Surface creator-specific judgment calls explicitly and get the creator's ruling before locking them as refusals. Two common shapes: a recurring but improvised personal beat the creator delivers live, captured as a hard refusal ("leave the slot, never draft its text"); and an emphasis or intensity device that fires at peaks by function, captured as a refusal against cadence-placement or carpet-bombing, not as a frequency rule.

## Stage 4: Assemble

Use `assets/voice-profile-template.md` for the guardrail.

- Write one file per populated `voice_context` to `foundation/reference-pieces/{voice_context}.md`. Inside the file: a short header explaining what the file is, then each selected passage as a `## ` section opening with a `> Demonstrates:` line in plain language, then the verbatim passage. One file, multiple sections.
- Write `foundation/voice-profile.md` from the template, guardrail sections only.
- Contexts without enough material: no file, no stub. Add a `context_flex` line in the guardrail noting it is deferred.

**Refresh runs.** Per [[voice-profile-schema]] merge logic: append new `## ` sections to an existing context file and log the addition; a context whose sources no longer validate is marked `deprecated` in `context_flex` (file kept, not deleted); a new context gets a new file and a log line. At every refresh, re-ask the exclusion-rule question ("any new moment you always deliver live and never want drafted, any existing one no longer relevant"). New guardrail patterns appear with `(added YYYY-MM-DD)`; conflicts are surfaced to the creator, not auto-resolved. One update log in the profile.

## Stage 5: Read-aloud validation

Load `knowledge/voice-pressure-test.md`.

Read selected passages and the guardrail back to the creator. Ask: "Does this sound like you in this context? Anything you would cut?" For each context: "If you were writing a {context} piece now, are these the right passages to write from?" If the creator rejects a passage, swap it for a better one from the same source. If the creator rejects three or more, the source mix is wrong: get different sources or ask what feels off. The profile and reference set only contain what the creator confirms out loud.

## Stage 6: Save and state the load contract

Save the folders and the guardrail. Update `sources_analyzed` and the single `update_log`. Confirm to the creator:

"Voice captured. Reference pieces curated for {list contexts} (the passages every writing skill will write from). Guardrail holds {N} signature phrases and your refusals. No rhythm gets stored; it is judged by ear against your real passages. Writing skills load the guardrail always, plus the reference pieces matching the piece's `voice_context`. Add sources and re-run to populate more contexts."

## Closing the skill

Voice capture is the last foundation step before research. Announce completion. Do not auto-invoke the next skill.

> "Voice captured. That completes your foundation. Next: run `vid-research` to build your pattern banks and author your packaging defaults from real channel evidence (it needs a YouTube API key and about 90 minutes). Run it when you are ready."

If the creator wants to keep moving, they invoke `vid-research`.

## Failure modes

- **No source material.** Hard stop. Transcripts, scripts, posts, or a 10-minute live monologue. Voice cannot be built from nothing.
- **Single context only.** Build the guardrail, defer all context folders, flag low confidence. Tell the creator to add other-medium sources and re-run.
- **Conflicting patterns across two contexts.** This is exactly when separate reference sets earn their keep. Do not average. Keep each context's passages separate; the contradiction is the signal.
- **Existing files locked or read-only.** Do not overwrite silently. Show the diff, ask permission.
- **A context's voice has evolved faster than the rest.** Refresh that context's reference set independently. Folders make this clean.

## Anti-patterns

- Distilling the voice into rules and numbers instead of keeping real passages. The passage is the asset.
- Selecting passages by topic. Narrows the voice. Select for stylistic range.
- Cleaning or rephrasing the creator's words in a reference piece.
- Curating an improvised, creator-designated moment as a reference piece. It is a refusal.
- Writing rhythm or punctuation numbers into any file.
- Storing a guessed pattern. Empty beats a guess.
- Locking anything the creator has not heard out loud.
- Saying "voice locked".

## References

- `knowledge/voice-profile-schema.md`: the two-artifact contract and the unified load contract.
- `references/voice-extraction-methods.md`: source grouping, passage selection, guardrail build.
- `knowledge/voice-pressure-test.md`: how writing skills validate against the reference pieces.
- `knowledge/voice-rhythm.md`: the lens for hearing rhythm (loaded by writing skills, not this one).

Templates live in `assets/` (skill-local):

- `voice-profile-template.md`: the thin guardrail shape.
- `reference-piece-template.md`: a single curated passage shape.
- `extraction-worksheet-template.md`: scratch workspace for the curation session.
