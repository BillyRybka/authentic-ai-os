---
name: vid-capture
description: Capture or create a story, metaphor, proof, testimonial, or framework and save it to the creator's evergreen banks. Runnable standalone anytime raw material lands (a client win, a DM, a metaphor mid-conversation, a screenshot, a framework that just crystallized), OR invoked by another vid- skill mid-script when the banks don't have what the script needs. Handles both logging material the creator already has and walking them through building something from scratch. Triggers on "capture a story", "new story for the bank", "add to story bank", "save this metaphor", "metaphor capture", "help me come up with a metaphor", "brainstorm a metaphor", "I need a metaphor for", "proof bank", "save a client win", "log a testimonial", "new testimonial", "just got a screenshot", "capture a framework", "log my framework", "save my system", "add to my evergreen banks", or when any other vid- skill asks "do you have a story/metaphor/proof/framework for X".
---

# Video Capture

Capture one item at a time (stories, metaphors, proof, testimonials, or frameworks) into the creator's banks. This skill is how raw experience becomes usable material at script-writing time. Without these banks, every future script starts empty and fabrication pressure goes up.

This skill loads `knowledge/vault-integration.md` at session start. Every entry it creates matches that contract, including frontmatter schema, body template, tags, file naming, wikilinks, and the People stub rule.

## Invocation modes

The skill works two ways:

**Standalone.** Creator invokes directly (typed trigger phrase, or running vid-capture as a slash command). After each save, loop back to the routing menu. Capture multiple items in one session. End with a session-close visibility summary.

**Sub-skill (invoked by another vid- skill).** Another skill like `vid-pipeline` or `vid-segment` calls vid-capture mid-script when the banks don't have what the writing step needs. Capture ONE item, return the new entry's wikilink to the caller, skip the routing loop, skip the session-close summary. The caller handles the wrapping.

The five stage flows (S, M, P, T, F) are identical in both modes. The difference is only in the router and the session-close behavior.

If invoked with context from the caller (e.g., "I need a metaphor about client onboarding for Problem 2"), skip the questions the caller has already answered and go straight to the stage.

## What this produces

Bank entries in the creator's workspace, each following the vault-integration schema.

- `banks/story-bank/{slug}.md`: stories in Problem / Action / Outcome format
- `banks/metaphor-bank/{slug}.md`: metaphors tied to the concept they clarify
- `banks/proof-bank/{slug}.md`: screenshots, numbers, results (optionally with asset files in `banks/proof-bank/assets/`)
- `banks/testimonial-bank/{slug}.md`: verbatim client quotes with source tagging
- `banks/framework-bank/{slug}.md`: named systems with components, shape, problem solved
- `People/{Full Name}.md`: auto-created stubs for any client mentioned

The skill is looped. Capture one item, save it, loop back to the menu, capture another. End when the creator is done.

## When to run this

- Right after a client wins (capture the story plus the proof)
- A screenshot landed in DMs and it proves something useful
- A metaphor came up mid-conversation and actually worked
- A named system / framework crystallized during writing or coaching and the creator wants to lock it for reuse
- The creator had a breakthrough and wants to lock the story
- A downstream writing skill (vid-segment, vid-intro) asked for material that doesn't exist yet
- Monthly bank top-up session

Not for: soliciting testimonials from clients (out of scope, this skill captures what already exists), refining already-captured entries (use direct edit), or generating stories from thin air (this skill never fabricates).

## Prerequisites

Hard requirement: `foundation/creator-foundation.md` must exist with a readable "Top 3 problems" section. Every bank entry gets a `problem_illustrated` value mapping to one of those three (or "general"). If the file is missing, the skill exits and asks the creator to run `vid-foundation` first.

Optional but helpful:
- The raw material the creator wants to capture (a memory, a Slack screenshot, a DM, a number from analytics)
- The client's full name if a client is involved (so the People stub lands correctly)

## Folder structure this uses or creates

```
foundation/creator-foundation.md     (required, read not written)
banks/story-bank/                    (created if missing)
banks/metaphor-bank/                 (created if missing)
banks/proof-bank/                    (created if missing)
banks/proof-bank/assets/             (created if missing, for screenshots/videos)
banks/testimonial-bank/              (created if missing)
banks/framework-bank/                (created if missing)
People/                              (expected to exist, stubs created inside)
```

## Routing

At session start:

1. Load `vault-integration.md` to lock the schemas.
2. Load `foundation/creator-foundation.md` to pull the Top 3 problems.
3. Ask the creator what they're capturing: story, metaphor, proof, testimonial, or framework.
4. Route to the matching stage.
5. After save, loop back to step 3. End when the creator says they're done.

If the creator has multiple items in mind, process them one at a time. Do not batch multi-item captures.

## Stage S: Story capture

Load `knowledge/story-capture-guide.md`.

1. **Pick the story type.** Client (someone else's transformation), Own (creator's experience), or Viewer (fallback when no personal or client example exists). If the creator is unsure, walk them through the distinction from the reference.
2. **Extract the raw material.** If the creator knows the story, let them tell it. If they're not sure they have one, walk them through the 6 story prompts in the reference. Each is designed to unlock a memory.
3. **Dig deeper.** Do NOT accept the first pass as final. Probe for specifics:
   - Problem: "What did that feel like at the worst moment? What's the specific detail that made it sting?"
   - Action: "What's the one thing you did? Not everything, the key move."
   - Outcome: "What's the exact number, timeline, or result? What changed?"
   - Plan on 2-3 rounds. Loop until specificity emerges, then save. Flag in Notes if still thin.
4. **Client mention check.** If the creator names a client, check `People/{Full Name}.md`. If missing, create the stub per the vault-integration template. Write `client: "[[Full Name]]"` in frontmatter and `[[Full Name]]` at first body mention.
5. **Set `problem_illustrated`.** Ask which of the top 3 problems this story illustrates. Value is `1`, `2`, `3`, or `general`.
6. **Propose a slug.** Lowercase, hyphenated, 3-6 words, descriptive. Creator approves or overrides.
7. **Dedup check.** Scan `banks/story-bank/*.md` for matches on `problem_illustrated` plus theme tags plus slug proximity plus first-sentence overlap of the Problem section. If candidates found, show them and ask: update existing, save as new angle, or merge manually.
8. **Assemble the entry** using `assets/story-entry-template.md`. Fill frontmatter (including `used_in: []` empty). Body follows Problem, Action, Outcome, `> [!tip] Why this story lands`, Notes.
9. **Read-aloud test.** Read the entry back to the creator: "Would you reword any of this if you were saying it out loud?" Edit to match their phrasing. Save only after they confirm.
10. **Save** to `banks/story-bank/{slug}.md`.
11. Loop back to the router (standalone mode) OR return the new entry's wikilink to the caller (sub-skill mode).

## Stage M: Metaphor capture

Load `knowledge/metaphor-builder.md`.

**Branch:** Open by asking the creator which path they're on. Both paths use the same builder below; the difference is pace.

- **Log path.** Creator already has a metaphor (invented it, heard it from someone else, remembered an old one). Validate it through steps 1-3, then capture.
- **Create path.** Creator has a concept but no metaphor. Walk them through steps 1-3 to generate one. Push back when attempts feel abstract or forced.

The builder:

1. **Name the concept.** What abstract or confusing idea is the metaphor clarifying? One short phrase.
2. **Problem and solution.** State the problem in the concept (what viewers get wrong) and the solution (what they should do instead). Both in the creator's voice.
3. **Find the comparison.** Pull from everyday categories: food, cars, clothes, sports, travel. The reference shows 2 real metaphors. If the first attempt feels abstract or forced, push back: "Make it something anyone would recognize. What's the everyday version?"
4. **Classify visual vs non-visual.** Ask: "Does this metaphor depend on a prop or graphic to land, or does pure speech carry it?" Set `visual: true` or `visual: false`. Visual metaphors capture TWO body sections (Spoken plus Shown); non-visual capture one (The metaphor).
5. **Set `problem_illustrated`.** Which top-3 problem does this metaphor support?
6. **Propose a slug.** Creator approves.
7. **Dedup check.** Scan `banks/metaphor-bank/*.md` for matches on `concept:` field value (same concept) OR same `category:` with similar metaphor text. If candidates found, show them and ask: update existing, save as new angle, or merge manually.
8. **Assemble the entry** using `assets/metaphor-entry-template.md`. Body depends on `visual`: if true, include Spoken plus Shown subsections; if false, single "The metaphor" block.
9. **Read-aloud test.** The metaphor has to land fast. For non-visual, read it aloud with no visual aid. Does the viewer still get it? For visual, imagine Spoken plus Shown together. Does the spoken layer drag without the visual, or does the visual land without the speech?
10. **Save** to `banks/metaphor-bank/{slug}.md`.
11. Loop back to the router (standalone mode) OR return the new entry's wikilink to the caller (sub-skill mode).

## Stage P: Proof capture

Load `knowledge/proof-capture-guide.md`.

1. **Pick the proof type.** Two options: `personal-result` (creator's own numbers and wins) or `client-win` (someone else's result, with permission or anonymized). Presentation format (static screenshot, before-after pairing, live video clip, inline stat) is captured separately in the body, not as a top-level type.
2. **Collect the asset.** If there's a screenshot or video file, ask the creator for the path or where to save it. Put the asset in `banks/proof-bank/assets/`. Record the path in `asset_path:`. If the proof is inline (a stat or quote), capture it in the body.
2b. **Note presentation format.** In the body's "Presentation format" section, record how this proof is shown: static screenshot, before-after pairing, live video clip, or inline stat. A single proof can be available in multiple formats.
3. **Client mention check.** Same flow as Stage S. Auto-create `People/{Full Name}.md` stub if missing. Write `client:` wikilink in frontmatter.
4. **Capture what it proves.** One sentence. The claim this proof backs up.
5. **Context.** When, where, who, enough that the creator will remember why this matters in six months.
6. **Usage rules.** If there are NDA or permission constraints, add a `> [!warning] Usage rules` callout. If the client consented to stats but not their name, note it. Anonymization rules live in the body.
7. **Set `problem_illustrated`.** Which top-3 problem does this proof support?
8. **Propose a slug.** Creator approves.
9. **Dedup check.** Scan `banks/proof-bank/*.md` for matches on `proof_type:` plus `client:` plus first-sentence overlap of "What it proves". If candidates found, show them and ask: update existing, save as new angle, or merge manually.
10. **Assemble the entry** using `assets/proof-entry-template.md`. Fill frontmatter (`used_in: []` empty).
11. **Save** to `banks/proof-bank/{slug}.md`.
12. Loop back to the router (standalone mode) OR return the new entry's wikilink to the caller (sub-skill mode).

## Stage T: Testimonial capture

Load `knowledge/testimonial-capture.md`.

Testimonials are captured client voice, preserved verbatim. Different from stories (which the creator narrates) and different from general proof (which may be a number or graph). The source is always the client's own words.

1. **Source check.** Is this from a comment, DM, email, or video? Set `source:` accordingly.
2. **Capture the quote verbatim.** Do NOT paraphrase. Do NOT clean up grammar. The exact wording is the testimonial.
3. **Client identification.** If the client is named and OK to be named, use their name. If anonymization applies, use "Anonymous" in `client:` and set `anonymized: true`. Note permission status in the body's Anonymization section.
4. **People stub check.** If named, auto-create `People/{Full Name}.md` if missing.
5. **Context.** What were they responding to? Which video or offer triggered this testimonial? Link to it with a wikilink if the piece exists.
6. **Set `problem_illustrated`.** Which top-3 problem does this testimonial support? (Testimonials often map to `general` if the client isn't responding to a specific problem.)
7. **Propose a slug.** Creator approves.
8. **Dedup check.** Scan `banks/testimonial-bank/*.md` for matches on `client:` plus `source:` plus first-line of verbatim quote. If candidates found, show them and ask: update existing, save as new angle, or merge manually.
9. **Assemble the entry** using `assets/testimonial-entry-template.md`. Body follows the `> [!quote]` callout with verbatim text, Context, Anonymization, Notes.
10. **Save** to `banks/testimonial-bank/{slug}.md`.
11. Loop back to the router (standalone mode) OR return the new entry's wikilink to the caller (sub-skill mode).

## Stage F: Framework capture

Load `knowledge/framework-builder.md`.

Stage F handles the LOG path: the creator already has a named system and wants to save it for reuse across videos. The CRAFT path (building a framework from scratch via the 5-step process) lives inline in vid-segment, which loads `framework-builder.md` directly and walks the creator through the 5 steps mid-write. Stage F is invoked AFTER inline crafting completes (vid-segment routes here to save), OR standalone when a framework crystallizes outside writing.

**What counts as bank-worthy:** the creator's OWN named systems (not other people's frameworks, not AI-invented acronyms, not single tactics). A framework needs (a) a name the creator actually uses, (b) named components, (c) a clear problem it solves. See `framework-builder.md` "What NOT to bank" for the full exclusion list.

1. **Confirm the framework exists in the creator's voice.** Ask: "What do you call this system?" The name comes from the creator, not the AI. If they don't have a name yet but want one, route them into the inline craft flow via vid-segment OR walk Step 5 of the 5-step build (`framework-builder.md` "Step 5: Name it") right here.
2. **Capture the problem it solves.** One sentence in the creator's voice. "Why does this framework exist? What's the failure mode it prevents?"
3. **Capture the components.** Usually 3 (sometimes 4-5). Each component gets a name and a one-line "what it is, why it matters." Push back if the creator lists 6+; the framework probably hasn't crystallized yet.
4. **Pick the shape.** Use the selection matrix in `framework-builder.md`. If components are sequential → arrows. Equal-and-stacking → pyramid. Looping → cycle. Overlapping → Venn. Broad-to-narrow → funnel. Share-a-letter → acronym. If the creator doesn't care about the shape, infer silently from the component relationships and confirm.
5. **Set `problem_illustrated`.** Which of the Top 3 problems does this framework address? Value is `1`, `2`, `3`, or `general`.
6. **Propose a slug.** Lowercase, hyphenated, 3-6 words, descriptive (e.g., `3-part-onboarding-system`, `hire-or-automate-matrix`). Creator approves.
7. **Dedup check.** Scan `banks/framework-bank/*.md` for matches on `name:` proximity, `components:` overlap, or `problem_it_solves:` overlap. If candidates found, show them and ask: update existing, save as new angle, or merge manually.
8. **Assemble the entry** using the schema in `framework-builder.md` "Entry schema + worked body example." Body follows: What problem does this solve? / The components / The shape / When to use it / Related assets / Origin. Fill frontmatter with `used_in: []` empty.
9. **Read-aloud test on the NAME.** "Read the framework name out loud. Would you say this on camera without rewording it?" If they'd reword it, rename before saving. (The components and shape don't need a full read-aloud test; the name does.)
10. **Save** to `banks/framework-bank/{slug}.md`.
11. Loop back to the router (standalone mode) OR return the new entry's wikilink to the caller (sub-skill mode).

**Sub-skill invocation pattern.** When vid-segment routes here after inline crafting, the caller passes a context packet like: `{name: "The 3-Part Onboarding System", components: [...], shape: "arrows", problem_solved: "...", problem_illustrated: 2}`. Skip steps 1-4 (the caller already has the answers), go directly to step 5 (problem_illustrated, if not already passed), step 6 (slug), step 7 (dedup), step 8 (assemble), step 9 (read-aloud on name), step 10 (save), step 11 (return wikilink).

## Contract behaviors (enforced every stage)

These come from `knowledge/vault-integration.md`. Non-negotiable.

- **Frontmatter matches the schema exactly.** Field names, enum values, tag slugs are specified in the contract. Don't invent fields or alternate names.
- **`used_in: []` starts empty.** Writing skills (vid-segment, vid-intro) update it later when they actually use the entry. Never touch it from here after initial creation.
- **Client mention, People stub.** No exceptions. Orphan wikilinks break the graph.
- **Tags per type:** Story gets `story`, `problem-{n}`, optional theme slug. Metaphor gets `metaphor`, `category-{slug}`, `problem-{n}`. Proof gets `proof`, `{proof-type-slug}`. Testimonial gets `testimonial`, `source-{slug}`. Framework gets `framework`, `{shape-slug}`, `problem-{n}`.
- **File naming:** lowercase, hyphenated, 3-6 words, no dates in filename (dates live in frontmatter), no type prefix (folder carries that context).
- **Read-aloud test.** Every entry that captures creator voice (stories, metaphor text, testimonials) must pass: creator reads it and doesn't reword a word.

## Failure-mode behaviors

From `vault-integration.md` Failure modes section. Never silent inconsistency.

- **Missing `foundation/creator-foundation.md`:** hard stop. Tell the creator to run `vid-foundation` first. Do not proceed.
- **Missing bank subfolders:** create them silently and proceed.
- **People stub creation fails** (permission error, folder missing): do NOT save the bank entry with an unresolved `[[Client Name]]` wikilink. Report visibly, ask the creator to resolve, then retry save.
- **`creator-foundation.md` frontmatter malformed** (Top 3 problems section unreadable): show the creator what was found vs what was expected. Ask: "Want to skip `problem_illustrated` this session (default to 'general'), or pause and fix creator-foundation first?"
- **Re-save over a malformed existing entry:** show the diff. Don't overwrite silently.

## Session close

Before exiting, report:

- Entries captured this session (as wikilinks to each new bank file)
- People stubs created (names plus bucket)
- Any fields skipped or defaulted (e.g., `problem_illustrated: general`)
- Any unresolved warnings

End with: "When you're ready to write a script, run `vid-pipeline` (or any specific writing sub-skill). These banks will be there."

## Principles

- **Preserve creator's exact phrasing.** Mine the creator's actual words. Do NOT polish into generic prose. Voice lives in word choice, rhythm, and specificity. The read-aloud test is the quality bar.
- **Claude structures, Claude does not generate.** If a prompt gets no response, note "no story here yet" and move on. Never invent a client, number, result, or testimonial.
- **Dig deeper before saving.** Push for specifics. Thin entries are worse than empty ones because they take up space without pulling weight.
- **Honor the contract.** Every entry matches the vault-integration schema. Every client mention creates a People stub. Every entry gets a `problem_illustrated` value.
- **Banks are written once, read many times.** Optimize entries for downstream retrieval, not the capture moment.
- **One item at a time.** Batch captures encourage sloppy ones.
- **Dedup before save.** Always check existing bank entries for overlap. Duplicates pollute future retrieval and make it harder for writing skills to find the right entry.

## Reference index

References live in `knowledge/` (loaded by multiple skills, since vid-segment and vid-intro will load them too):

- Stage S loads `story-capture-guide.md` (6 prompts, 3 story types, P/A/O with real examples, dig-deeper probes)
- Stage M loads `metaphor-builder.md` (3-step builder, 5 everyday categories, 2 real metaphors, visual vs non-visual distinction, pivot phrases)
- Stage P loads `proof-capture-guide.md` (4 proof types, screenshot-immediately rule, placement, anonymization)
- Stage T loads `testimonial-capture.md` (verbatim capture, 4 sources, anonymization, scope)
- Stage F loads `framework-builder.md` (5 visual shapes, selection matrix, 5-step build process, naming rules, entry schema, what NOT to bank). Also loaded inline by vid-segment for the craft path mid-write.

Templates in `assets/`:

- `story-entry-template.md`
- `metaphor-entry-template.md`
- `proof-entry-template.md`
- `testimonial-entry-template.md`
- `people-stub-template.md`

(Framework entries use the schema embedded in `knowledge/framework-builder.md`. No separate template file. Single source of truth for framework structure.)
