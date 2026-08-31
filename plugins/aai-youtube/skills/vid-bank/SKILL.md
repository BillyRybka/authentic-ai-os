---
name: vid-bank
description: Capture or create a story, metaphor, proof, testimonial, or framework and save it to the creator's evergreen banks. Runnable standalone anytime raw material lands (a client win, a DM, a metaphor mid-conversation, a screenshot, a framework that just crystallized), OR invoked by another vid- skill mid-script when the banks don't have what the script needs. Handles both logging material the creator already has and walking them through building something from scratch. Triggers on "capture a story", "new story for the bank", "add to story bank", "save this metaphor", "metaphor capture", "help me come up with a metaphor", "brainstorm a metaphor", "I need a metaphor for", "proof bank", "save a client win", "log a testimonial", "new testimonial", "just got a screenshot", "capture a framework", "log my framework", "save my system", "add to my evergreen banks", or when any other vid- skill asks "do you have a story/metaphor/proof/framework for X".
---

# Vid Bank

Capture one item at a time (story, metaphor, proof, testimonial, framework) into the creator's banks, in the creator's exact words. The banks are the material every future script pulls from: written once, read many times.

## What loads, and when

| File | When | For |
|---|---|---|
| `knowledge/bank-contract.md` | session start | the schema every entry, wikilink, and person stub must match |
| `knowledge/prose-craft.md` | session start | the seven moves the `illustrates` line and every written summary are held to. Never applied to the creator's verbatim words |
| `knowledge/story-capture-guide.md` | Stage S | the 3 story types, the 6 story prompts, dig-deeper probes |
| `references/metaphor-builder.md` | Stage M | the 3-step builder, everyday categories, visual vs non-visual |
| `references/proof-capture-guide.md` | Stage P | the 2 proof types, the screenshot-immediately rule, anonymization |
| `references/testimonial-capture.md` | Stage T | verbatim handling, the 4 sources, permission rules |
| `knowledge/framework-builder.md` | Stage F | shapes, selection matrix, naming rules, entry schema, what NOT to bank |
| `assets/{type}-entry-template.md` | assemble time | the entry's frontmatter and body skeleton |

## The bar: capture what a writer can pull

A bank entry gets written once and read many times, by a writing skill mid-script, under time pressure, looking for something it can drop into a segment without rework. So the capture question is never "did the creator say this?" It is "could a writer pull this?" Capture what a writer can pull, not everything the creator said.

A pullable entry carries what a script cannot invent later: the worst-moment detail, the exact number, the client's verbatim words, the comparison anyone recognizes. An entry without those is worse than an empty slot. An empty slot tells the writer to ask. A thin entry gets pulled, and the segment goes out flat.

- **Weak:** "I was struggling with pricing, made some changes, and things got a lot better."
- **Strong:** "I priced my first course at $49 because I was scared to charge more. Three months in I had made $900, and realized I had built myself a minimum wage job."

The strong version is pullable because a writer can say it aloud as-is. The weak one needs the whole interview redone at write time, and redoing that interview at write time is the failure this skill exists to prevent.

## What this produces

- `banks/story-bank/{slug}.md`, `banks/metaphor-bank/{slug}.md`, `banks/proof-bank/{slug}.md` (screenshots and clips in `banks/proof-bank/assets/`), `banks/testimonial-bank/{slug}.md`, `banks/framework-bank/{slug}.md`
- `people/{Full Name}.md` stubs for any client named

No foundation dependency. Each entry is tagged from its own material (an `illustrates` or matching-key line plus open `themes:`), so capture works whether or not the foundation is built.

## Routing

Looped, one item at a time, never batched:

1. Load `knowledge/bank-contract.md` to lock the schemas.
2. Ask what the creator is capturing: story, metaphor, proof, testimonial, or framework.
3. Run the matching stage, then the shared finish below.
4. Loop back to step 2. End when the creator is done.

Called mid-script by another vid- skill: same stages, same finish. The caller passes what it already built or asked, so skip the questions it has answered, capture the item, and return the new entry's wikilink instead of looping.

Not for: soliciting new testimonials from clients, refining existing entries (edit them directly), or inventing material. A gap is a TODO, never a fabrication.

## Stage S: Story capture

Emotion is what stores a story in the viewer's memory; facts alone barely stick. The bar for a bankable story is twist or receipt: either the ending surprises (a result wildly different from what anyone expected), or the outcome carries a receipt the viewer could check (exact number, timeline, before vs after). A story with neither is a chronicle, and chronicles do not get pulled.

Load `knowledge/story-capture-guide.md`.

1. **Pick the type.** Client (highest trust, someone else's transformation), Own (credibility, an admitted failure makes it stronger), Viewer (fallback only).
2. **Get the raw story.** If the creator knows it, let them tell it. If they say they have none, walk the 6 story prompts one at a time, and bail after 3 prompts surface nothing.
3. **Dig for the moment, not the lesson.** Never accept the first pass. Push 2 to 3 rounds: the worst-moment detail in the Problem, the one key move in the Action, the exact receipt in the Outcome.
4. **Client mention.** A named client gets `client: "[[Full Name]]"` in frontmatter, `[[Full Name]]` at first body mention, and a `people/{Full Name}.md` stub from `assets/people-stub-template.md` if one does not exist.
5. **Write `illustrates` plus `themes`.** One short line, plain cause and effect, in the creator's voice. This line is what a writer searches the bank by, so it says what the story proves, not what it is about. Add a few open theme tags.

Then run the finish (slug, dedup, assemble, read-aloud, save).

## Stage M: Metaphor capture

Two tests decide whether a metaphor is bankable. The everyday-recognition test: anyone, no context, recognizes the comparison (food, cars, clothes, sports, travel). The read-aloud-without-visuals test: read it aloud with nothing on screen. If it still lands, it is non-visual; if it needs the prop, it is visual. That classification is what tells the writer whether to plan a visual or script the speech alone.

Load `references/metaphor-builder.md`.

Two paths in, one builder. The difference is pace, not process:

- **Log.** The creator already has the metaphor. Validate it through the builder, then capture. Heard-it-somewhere counts; note the origin in Notes if they want to remember it.
- **Create.** The creator has a concept but no comparison. Walk the builder and push back when attempts come out abstract or forced. If it still feels like a riddle after a couple of rounds, drop it. A forced metaphor is worse than none.

The builder:

1. **Name the concept.** The abstract idea being clarified, one short phrase. This is the entry's matching key.
2. **Problem and solution.** What viewers get wrong, and the one move instead, both in the creator's voice.
3. **Find the comparison.** Something anyone would recognize that works the same way.
4. **Classify with the read-aloud-without-visuals test.** Visual entries capture two body layers (Spoken plus Shown, precise enough that someone else could reproduce the shot). Non-visual entries capture one spoken block.

- **Weak:** "Your content system is like a well-oiled machine." Nothing to picture, fits everything, lands on nothing.
- **Strong:** "Early dating is like wine tasting. You sip, you swirl, you smell. You do not chug the bottle and assume it is perfect for life." Anyone has done one side of this; the mapping is instant.

Then run the finish.

## Stage P: Proof capture

Proof is the receipt that lets the avatar mentally simulate the result: a number, a screenshot, a before-after they can picture happening to them. "I have helped lots of people" fails the simulation test; one dashboard screenshot passes it. The screenshot-immediately rule (drop everything, capture the win the moment it lands, sort it later) is the upstream habit. This stage turns what landed into an entry.

Load `references/proof-capture-guide.md`.

1. **Pick the type.** `personal-result` (the creator's own numbers) or `client-win` (someone else's result, with permission or anonymized).
2. **Collect the asset.** A screenshot or clip goes into `banks/proof-bank/assets/` and its path into `asset_path:`. If there is no asset, the proof is an inline stat or quote and lives in the body. If there is no file and no exact words, there is no proof yet.
3. **Presentation format.** How it gets shown on screen (static screenshot, before-after pairing, live clip, inline stat). Captured in the body, not the type. One proof can grow formats over time.
4. **Client mention.** Same stub flow as Stage S.
5. **What it proves, in one sentence.** If it takes more than one sentence, the proof is too vague to bank.
6. **Context and usage rules.** When, where, who, enough that the creator remembers why it matters in six months. NDA or permission limits go in the `> [!warning] Usage rules` callout. When in doubt, anonymize.

- **Weak:** "My clients get amazing results." Nothing to simulate; a claim, not proof.
- **Strong:** "Analytics dashboard screenshot, 3.1M views over 12 months, file in `assets/`, one sentence naming what it backs." A writer can drop that on screen the moment a viewer asks "has this worked?"

Then run the finish.

## Stage T: Testimonial capture

A testimonial is the client's own words, and verbatim is the whole value: the receipt the avatar can mentally simulate saying. Paraphrasing or grammar cleanup turns proof back into a claim. The only edit allowed is trimming for length, noted in Context.

Load `references/testimonial-capture.md`.

1. **Source.** comment, dm, email, or video. The source drives permission: comments are public, everything else defaults to anonymized until the client has said yes.
2. **The quote, exactly.** Typos, lowercase, profanity, all of it, inside the `> [!quote]` callout. The authenticity is what lands.
3. **Client and stub.** Named with permission, or "Anonymous" plus `anonymized: true`. Named clients get the people stub.
4. **Context.** What the client was responding to; wikilink the piece if it exists.
5. **Write `illustrates` plus `themes`.** The point this quote backs, one short line in the creator's voice.

Then run the finish.

## Stage F: Framework capture

The bar for banking a framework: name it so the viewer can repeat it. If someone cannot say the name back after one watch, the framework has not crystallized yet, and banking it stores fog. The name comes from the creator's mouth, never invented here, and the read-aloud test on the name is the gate.

Load `knowledge/framework-builder.md`.

Stage F is the log path: the system already exists in the creator's practice. Building one from scratch is vid-segment's inline 5-step build; when that finishes, vid-segment hands what it built here for the save.

Bank-worthy means the creator's OWN named system: a name they actually use, named components, a clear problem it solves. Other people's frameworks, AI-invented acronyms, single tactics, and one-video novelties stay out. The full exclusion list is in the reference.

1. **The name, in the creator's words.** Ask what they call this system. No name yet means it is not ready to bank, or route them into the build flow.
2. **The problem it solves.** One sentence: the failure mode it prevents. This is the entry's matching key.
3. **The components.** Usually 3. Each gets a name plus one line of what it is and why it matters. Six or more means it has not crystallized.
4. **The shape.** From the selection matrix: sequential is arrows, equal-and-stacking is pyramid, looping is cycle, overlapping is Venn, broad-to-narrow is funnel, shared letters is acronym. Infer it from how the components relate and confirm.
5. **Read-aloud on the name.** The creator says it out loud. If they reword it, the rewording is the name.

- **Weak name:** "S.C.A.L.E. (Strongify Communication And Lead Engagement)." Strained letters, and nobody repeats it.
- **Strong name:** "The 3-Part Onboarding System." Descriptive, sayable, and clients will say it back.

When vid-segment routes here after building one inline, it passes what it built (name, components, shape, problem, themes). Skip whatever it already answered and go to the finish.

Then run the finish.

## Finishing any entry

Every stage ends the same way:

1. **Slug.** Propose lowercase, hyphenated, 3 to 6 words, no dates, no type prefix (the folder carries that). Creator approves or overrides.
2. **Dedup.** Scan the matching bank folder against the criteria below. On a candidate, show it and ask: update the existing entry, save as a new angle, or merge manually. An update keeps the existing slug.
3. **Assemble** from `assets/{type}-entry-template.md` (frameworks use the schema in `knowledge/framework-builder.md`). The template already carries the frontmatter and body skeleton; fill it, do not redesign it. `status: captured` and `used_in: []` start every entry's lifecycle. Writing skills move them later, never this skill.
4. **Read-aloud.** Read the entry back to the creator. Anything in their voice they would reword gets their rewording. Save only after they confirm.
5. **Save** to `banks/{type}-bank/{slug}.md`, creating the folder if missing. Standalone: loop back to the router. Called by another skill: return the entry's wikilink.

Dedup criteria per bank:

| Bank | A candidate match is |
|---|---|
| story | `illustrates` overlap, shared theme tags, slug proximity, first sentence of the Problem |
| metaphor | same `concept:`, or same `category:` with similar metaphor text |
| proof | `proof_type:` plus `client:` plus first sentence of "What it proves" |
| testimonial | `client:` plus `source:` plus first line of the quote |
| framework | `name:` proximity, `components:` overlap, or `problem_it_solves:` overlap |

## Session close

Report what changed: entries captured (as wikilinks), people stubs created, anything still thin (a TODO in an entry, a missing asset), and anything unresolved. No silent gaps.

## Principles

- **Written once, read many times.** Build every entry for the writer who pulls it mid-script, not for the capture moment.
- **Thin is worse than empty.** A thin entry gets pulled and flattens a segment. If the material is not there, say so and mark the TODO.
- **The creator's phrasing is the product.** Claude structures, Claude never polishes. The read-aloud test is the quality bar.
- **Never fabricate.** No invented clients, numbers, results, quotes, or metaphors. A gap is a TODO.
- **One item at a time.** Batching encourages sloppy captures.
- **The contract is one file.** Bank schemas, the wikilink and person-stub rules, and failure behavior live in `knowledge/bank-contract.md`. Every entry matches it.
- **Person stubs are created here, not upstream.** `vid-braindump` captures names as plain text and deliberately creates nothing, because a name in a raw dump is material, not yet an entity. This skill is where a named person becomes a `people/` profile: the moment their material becomes a bank entry.
