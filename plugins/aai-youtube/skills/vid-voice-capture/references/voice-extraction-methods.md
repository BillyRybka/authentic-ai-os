---
type: reference
scope: shared
loaded_by: [vid-voice-capture]
status: active
tags: [reference, voice, extraction]
---

# Voice Extraction Methods

How to turn the creator's existing content into the two artifacts in [[voice-profile-schema]]: curated reference pieces (the voice engine) and a thin guardrail (`foundation/voice-profile.md`). Read the schema first.

The load-bearing move is passage selection, not rule extraction. The old instinct (read everything, distill it into rules and numbers) loses the voice. The job is to find the creator's best real passages and keep them intact.

## The cross-validation principle

A pattern from one source is a coincidence. A pattern from one medium (all transcripts, no writing) is medium noise. Something that holds across multiple sources and multiple media is voice.

This decides where things go:

- Holds across sources and across `voice_context`: it belongs in the guardrail (`signature_phrases`, `refusals`, fingerprint).
- Strong in one `voice_context`, absent elsewhere: it stays in that context's reference pieces. Do not promote it.
- One source only: drop it, or flag low-confidence for creator review. Never bake a guess.

## Source types and what they give you

A mix matters more than volume from one type.

- **YouTube / video transcripts:** spoken rhythm, recurring phrases, opener and energy patterns. People repeat themselves more on camera than in writing.
- **Podcast / interview transcripts:** conversational rhythm, how they answer, off-script tics.
- **Newsletters / long-form prose:** written cadence, paragraph shape, transitions, closing style.
- **LinkedIn / Twitter:** short-form rhythm, hook and opener habits, line-break feel.
- **Email / DM / Slack:** the raw floor, the voice they do not perform.
- **Past scripts they drafted:** the strongest signal for what they want to sound like.
- **Live 10-minute monologue (recorded fresh):** the spoken floor when the archive is thin.

## Step 1: group sources by `voice_context`

Sort every source into a `voice_context` (the medium/mode it was produced in): `youtube-script`, `tutorial`, `shorts`, `newsletter`, `linkedin`, `twitter`, `podcast`, `casual`, `talk`. A context needs roughly 3 pieces or 5,000 words before it earns its own curated reference set. Thinner contexts feed the guardrail only and are flagged.

## Step 2: diagnose the frame, then select passages

Do not fill a fixed template. A generic peak / baseline / signature slot set fails on real creators: a creator who always teaches through examples has no flat baseline, and a creator who narrates a live screen demo has a mode no slot set names.

Instead, read all the grouped sources for a context and form a rough picture of the creator's actual range: the modes they shift into for different moments (a cold-open hook, plain teaching, a live on-screen demonstration narrating an action, a rant, a told story, whatever the tape shows), where they sit calm and where they spike, and the recurring rhetorical move that is unmistakably them. This is a private coverage lens, not a sorting job. A real passage usually spans several of these at once, and that is fine. Do not categorize each passage, do not argue categories with the creator, do not defend a passage as one type. The lens exists to catch exactly one failure: a whole mode the creator clearly uses going unrepresented in the final set.

State that picture back to the creator in plain language, get it confirmed, then select the passages. This replaces guess, pick, get corrected, re-pick with confirm-then-fill.

Select for `foundation/reference-pieces/{voice_context}.md` so the set spans the creator's calm and charged poles, every distinct mode they actually use (the live-demonstration mode is the easiest to miss and under-weight, since it reads looser than scripted teaching and hides in screen-share sources), and their signature move. Usually 3 to 8 passages depending on the creator's range, aiming for 2 to 3 per major beat type to dilute structural shadowing in downstream writing. The number serves coverage, never the reverse. If a creator has no flat baseline because they always teach through examples, that absence is the finding, not a slot to fill.

**Registers are a coverage dimension inside one `voice_context`, not a reason to split contexts.** A creator whose hook, teaching, and outro are the same voice but who shifts into a looser register while demonstrating on screen is ONE context with a demonstration register in its reference set. Split `voice_context` only when the delivery medium is a genuinely separate persona (a written newsletter against a spoken video), never when the same person shifts register inside one medium.

**Provenance check (hard).** Before describing any passage, read its surrounding source text and confirm what it actually is. A passage where the creator is narrating an on-screen action is the demonstration register even when it sounds calm; do not describe it as plain teaching. Describe by what the source shows, never by how it sounds in isolation.

Pick for stylistic representativeness, not topic: a passage chosen because it matches a subject narrows the voice to that subject. Keep each passage **intact**, the way the creator actually said or wrote it, a few sentences to a short paragraph. Do not flatten or strip structural elements; flattened samples lose the rhythm that IS voice (the stylometric evidence is one-directional on this). Long enough that the rhythm is audible, short enough that there is no filler. Do not clean or rephrase the creator's words.

**Aim for 2 to 3 passages per major beat type the creator uses** (a cold-open kind of moment, plain teaching, a live demonstration, a signature analogy, an ending). Single-sample beats are prone to structural shadowing in downstream writing: with one whole-ending sample, the writing skill will tend to mirror that ending's arc. Multiple samples per beat dilute that. The voice-only-not-structure clause in each writing skill's prompt is the second defense (see [[voice-profile-schema]] load contract); together they keep the samples doing their job (voice grain) without dragging architecture along.

**Output: one file per `voice_context`.** Write all the selected passages into `foundation/reference-pieces/{voice_context}.md` as `## ` sections, each opening with a `> Demonstrates:` line in plain language describing what the passage shows (mode, energy, signature move), then the verbatim passage. One file, multiple sections, not one file per passage. The file is loaded whole by writing skills working in that `voice_context`.

**Exclusion rule:** never curate an improvised, creator-designated moment (a creator may name, for example, an unscripted personal closing they always deliver live) as a passage. Storing it as a seed lets a writing skill regenerate it, which the creator forbade. It goes in the guardrail as a hard refusal instead.

## Step 3: build the thin guardrail

From the cross-validation pass, write only:

- **`voice_fingerprint`:** 2 to 4 sentences. The gestalt. Who this sounds like, fast.
- **`signature_phrases`:** verbatim recurring quotes that hold across contexts. Real quotes, never paraphrased ("systems beat hustle every time", not "uses a systems-over-hustle phrase"). Cross-validation finds recurrence; it does not separate signature from filler. A discourse marker ("right?", "you know", "so", "like") can hold across every source and still be filler an AI would over-reproduce. When a candidate matches a known-filler shape, surface it to the creator and ask: "load-bearing for your voice, or filler you'd cut?" Load-bearing stays in `signature_phrases`. Filler routes to `refusals` words-avoided with the reason `filler, drop unless the sentence needs it`. Filler hints (`right?`, `you know`, `like`, `so`, `okay`, `alright`, `I mean`, `basically`) are a prompt for that question, not a blacklist; the list is creator-specific and grows over time. The creator's answer is the gate.
- **`refusals`:** anti-patterns (full phrasings they would never write, plus the global em-dash and clean-register rules); words avoided as `word to swap (one-line reason)`, reason required so the model generalizes to unseen offenders; named creator hard rules. Full spec in [[voice-profile-schema]] `refusals` section.
- **`pov_and_energy`:** two paragraphs maximum, two sentences each. POV first, then energy floor. Spec in [[voice-profile-schema]].
- **vid-intro orientation fields:** only if clearly observed. Omit otherwise.
- **`context_flex`:** one line per populated context, pointing at its `foundation/reference-pieces/{voice_context}.md` file.

Nothing else. No rhythm numbers, no punctuation counts, no per-context field grids. Rhythm lives in the reference pieces and is judged by ear at validation time (see [[voice-pressure-test]]).

## The quantitative read is a selection aid, not an output

You may count sentence lengths, paragraph shapes, or openers while reading, to help you notice which passages are most representative. That noticing informs which passages you pick. The numbers themselves never go into any file. They are scaffolding you discard.

## Method: live monologue (last resort only)

A fresh 10-minute monologue is a fallback when the archive is genuinely empty. **Never use it when archival sources exist**, even thin ones. Even with explicit "don't perform" coaching, a creator who knows the tape is for voice analysis performs. The result is a captured performance voice, not their natural one, and it corrupts every downstream output that writes from it.

If archive truly is empty:

1. Ask them to talk about something they care about. Tell them not to perform. Accept that they probably will.
2. Record, auto-transcribe.
3. Select passages and build the guardrail from it.
4. Flag everything `confidence: single-context, fresh-monologue` until validated against future archival sources. The monologue is a spoken-floor baseline only; it cannot capture written voice, and it cannot be trusted at performance peaks because the moment was itself a performance.

Prefer waiting for archive over recording fresh.

## Source minimums (the floor, not a target)

The floor depends on the context's format-length. A word-count rule fits long-form and breaks on short-form: 5,000 words of `shorts` is 30-plus reels, which is absurd.

- **Long-form contexts** (`youtube-script`, `tutorial`, `newsletter`, `podcast`, `talk`): roughly 5,000 words OR 3 to 5 pieces, whichever comes first. For spoken long-form, 30 to 60 minutes of recorded speech.
- **Short-form contexts** (`shorts`, `linkedin`, `twitter`): 3 to 5 pieces. Word count is irrelevant here; the pieces are short by nature.
- Either rule earns the context its own reference set.
- Below the floor: guardrail only, that context deferred (no file), low-confidence flagged.
- Much thinner than that: tell the creator the result will not be reliable until they bring more. Do not build a context from a single piece.

## Common extraction mistakes

- **Distilling instead of selecting.** Rewriting the creator's voice into a description of it. The passage is the asset; keep it whole.
- **Choosing passages by topic.** Narrows the voice. Choose by stylistic representativeness.
- **Cleaning the passages.** Auto-transcript mess and verbal tics that are intentional discourse markers ("so", "look", "right?") stay. Only separate true noise ("um").
- **Promoting a single-source pattern to the guardrail.** One source is noise.
- **Curating the improvised moment.** A creator-designated improvised beat they always deliver live is a refusal, never a reference piece.
- **Inventing to fill a section.** Empty beats a guess. A guessed guardrail corrupts every downstream piece.
- **Ignoring the read-aloud test.** If the creator does not recognize the result as theirs when said out loud, it is wrong no matter how clean the method was.
