---
type: reference
scope: shared
loaded_by: [vid-voice-capture, vid-foundation]
status: active
tags: [reference, voice, extraction]
---

# Voice Extraction Methods

How to pull voice patterns out of existing creator content. The output of this work goes into `foundation/voice-profile.md` (schema in `voice-profile-schema.md`).

## The cross-validation principle

A pattern from one source is a coincidence. A pattern from one format (all transcripts, no writing) is format noise. A pattern from multiple sources across multiple formats is voice.

The extraction process always asks: "does this hold across the corpus?" Single-source patterns get demoted or dropped. Cross-source patterns get promoted to the profile.

## Source types and what they tell you

Different sources reveal different patterns. Pulling from a mix matters more than pulling a lot from one type.

- **YouTube transcripts**: sentence rhythm, fillers, opener patterns, energy variation, real recurring phrases (people repeat themselves more on camera than in writing)
- **Podcast appearances or interview transcripts**: conversational rhythm, how they answer questions, callbacks, off-script tics
- **Newsletters / blog posts / long-form prose**: paragraph structure, punctuation signature, written sentence rhythm, transitions, callback structure, CTA style
- **LinkedIn / Twitter posts**: short-form rhythm, hook patterns, opener clusters, line-break habits
- **Email replies, DMs, Slack messages**: raw conversational voice, energy floor, the voice they DON'T perform
- **Past scripts they drafted**: best signal for "here's what they want to sound like"
- **Live 10-minute monologue (recorded fresh)**: current voice baseline if archive is thin

## Method A: Quantitative pass (numbers)

Per source, count and record:

### Sentence length distribution

Split text into sentences. Count words per sentence. Record:
- Median sentence length
- Range (shortest to longest)
- % short (≤8 words), % medium (9-20 words), % long (21+ words)
- Pattern observation (does the creator alternate short-short-long? cluster long sentences then snap back?)

**Example output:** "Newsletter: median 11 words. 55% short, 30% medium, 15% long. Pattern: opens with 1-2 short sentences, expands to medium, occasional long for nuance, returns short."

### Paragraph structure ratio

Count paragraphs. For each, count sentences. Record:
- % single-sentence paragraphs
- % 2-3 sentence paragraphs
- % 4+ sentence paragraphs

**Example output:** "LinkedIn: 80% single-sentence paragraphs. Almost no 4+ sentence paragraphs in this corpus."

### Punctuation signature

Per 1000 words of source, count:
- Em-dashes (`,` or `--` if formatted that way)
- Ellipses (`...` or `…`)
- Parenthetical asides `(like this)`
- Semicolons
- Exclamation marks
- Question marks

**Example output:** "Newsletter: 8 em-dashes per 1000 words, 0 semicolons, 2 parentheticals, 1 exclamation, 4 questions."

Watch for cross-format consistency. If em-dashes only show up in newsletters because the platform renders them well, that's format noise, not voice.

### Opener pattern clustering

For each piece in the source, classify the opening sentence into a bucket:
- Question
- Declaration / bold claim
- Anecdote / story open
- Data-first / number open
- Contrarian / "everyone says X but..."
- Quote (someone else's words)
- Hook / cliffhanger

Record % distribution across the corpus per context.

**Example output:** "YouTube scripts: 70% question, 20% declaration, 10% anecdote. Newsletters: 50% anecdote, 30% question, 20% declaration."

### Closing pattern clustering

Same approach for the last paragraph or closing line. Buckets:
- No CTA (just ends)
- Direct ask (subscribe, reply, click)
- Callback to opener
- Community invite (let me know in the comments)
- Question back to reader/viewer
- Series teaser (next time we'll...)
- Quote / aphorism

## Method B: Qualitative pass (patterns the numbers miss)

Numbers tell you rhythm. Qualitative pulls out the voice itself.

### Recurring phrases

Read 3-5 pieces in a row. Note phrases that appear more than once. Pull them as real quotes, not paraphrases. After 5 pieces, the cross-piece repeats are the recurring phrases. Aim for 5-10 across the full corpus.

**Anti-pattern:** writing "uses the phrase 'systems beat hustle.'" Better: capture the actual quote. "systems beat hustle every time", because the variation matters.

### Words avoided

Read pieces looking for what's NOT there. Does the creator ever say "leverage" as a verb? "Synergy"? "Game-changer"? Note absences. Then pair each with what they use instead.

**Example output:** "Avoided: 'leverage' (uses 'use'), 'game-changer' (uses 'changes everything' or names the specific change), 'dive in' (uses 'let's go,' 'let me show you,' or just starts)."

### Anti-patterns

Stronger than words avoided. These are full phrasings the creator has corrected before, called AI-tells, or rejected in edits. Pull from:
- voice-rule-capture history if it exists
- Edit diffs in past drafts
- Direct creator quotes ("I would never write...")

### Rhetorical tics

Watch for habits across the corpus:
- Rule of three? ("X, Y, and Z. Three things.")
- Rhetorical questions? Frequency?
- Understatement habit?
- Callbacks (mentions an idea early, returns to it at the close)?
- Hyperbole? Frequency?

### Transitions

How does the creator move between ideas? Note actual phrases. Examples to watch for:
- "Here's the thing." / "Here's what nobody tells you."
- "But." (single-word transition)
- "So." (sentence opener pattern)
- Numbered list transitions ("First. Second. Third.")
- Pure line breaks (no transition word, structure carries it)

### POV default

When does the creator use "I"? When "you"? When "we"? Note the situations, not just the pronoun. Example: "I" for personal experience, "you" for instruction, "we" for shared journey or shared belief. Never "we" as the corporate plural.

### Energy descriptor

After reading the corpus, write one phrase that captures the energy. "Quiet confidence." "Dry wit with directness." "Performer with vulnerable beats." "High conviction, low volume." This goes in `energy_baseline`.

## Method C: Live monologue (when archive is thin)

If the creator has limited content, record a 10-minute monologue:

1. Ask them to talk about a topic they care about. Tell them not to perform, just talk.
2. Record. Auto-transcribe.
3. Run Method A and B passes against the transcript.
4. Flag every pattern as `confidence: single-context` until validated against future writing samples.

The monologue captures the spoken-voice floor. It cannot capture written-voice patterns. It is a starting baseline only.

## Cross-validation: which patterns make the cut

After Methods A and B per source, ask of every pattern:

- Does it appear in 2+ sources?
- Does it appear in 2+ formats (transcript AND writing)?
- Or is it isolated to one source/format?

Sort:

- **Cross-source AND cross-format → core profile (Layer 1)** with `confidence: high`
- **Cross-source within ONE format → context map for that format (Layer 2)** with `confidence: format-specific`
- **Single source → drop or flag `confidence: low`** for creator review

## Source minimums

Defaults that produce a useful profile (not absolute, just the floor):

- 3-5 transcripts OR 30-60 minutes of recorded speech (for spoken patterns)
- 15,000-20,000 words written across at least 2 formats (for written patterns)
- Per context map: at least 3 pieces or 5,000 words in that format

If thinner: build core profile only, defer context maps, flag low confidence.

If much thinner: tell the creator the profile won't be reliable until they bring more sources. Do not build a profile from 500 words.

## Worked example (illustrative, adapt to actual creator data)

**Source: 4 YouTube transcripts (40 mins total) plus 6 newsletters (~12k words) plus 8 LinkedIn posts (~3k words)**

Quantitative pass per context:

- YouTube median sentence: 7 words. 75% short. Em-dashes per 1000: 0. Ellipses: 5. Pattern: short-short-callback. 75% question-opener.
- Newsletter median sentence: 12 words. 50% short. Em-dashes: 9. Ellipses: 1. Single-sentence paragraphs: 65%. 40% anecdote-opener.
- LinkedIn: too thin for full quantitative. Qualitative only.

Qualitative pass:

- Cross-context recurring phrases (3 found): "every single time," "the truth is," "let me show you". All appear in YouTube AND newsletter AND LinkedIn → **core profile**.
- Newsletter-only phrases: "I'll be honest with you" (7x in newsletters, 0 in YouTube) → **newsletter context map**.
- POV: "I" for personal, "you" for direct instruction, never "we" as plural → **core profile**.
- Energy: high conviction with dry wit, modulates up in YouTube, down in newsletter → **core baseline plus per-context modulation note**.

Cross-validation result:

- 3 cross-context phrases → core (high confidence)
- 1 newsletter-only phrase → context map (format-specific confidence)
- LinkedIn context map deferred (too thin)
- Core baseline plus modulation captured per context

Output: rich profile with two strong context maps (YouTube, newsletter) and a deferred LinkedIn map awaiting more source material.

## Common extraction mistakes

- **Counting one piece as if it were the whole creator.** Single-piece patterns are noise.
- **Trusting auto-transcripts without cleaning.** Verbal fillers ("um," "you know") need separating from intentional discourse markers ("so," "look").
- **Inventing patterns to fill the schema.** If a field has no data, leave it empty or `confidence: low`. Filling with guesses corrupts every downstream output.
- **Conflating brand voice with personal voice.** Brand stuff (mission, tagline) belongs in `Context/brand.md`, not the voice profile.
- **Ignoring the read-aloud test.** Numbers and patterns mean nothing if the creator doesn't recognize the result as their voice when said out loud.
