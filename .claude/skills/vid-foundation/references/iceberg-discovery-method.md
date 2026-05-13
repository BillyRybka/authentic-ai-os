# Iceberg Discovery Method

The conversation backbone for Stage 1 of vid-foundation. Walks the creator from "what do you sell?" to a locked iceberg.

This file is for Claude to drive the conversation with. Do **not** paste it into chat. Use it to know which question comes next, when to push back, which probe to pull, and what good output looks like.

The skill EXECUTES. It doesn't teach. The creator already knows the iceberg model from outside context. Don't explain the metaphor. Don't refresh definitions. Just run the production flow.

## Output (locked at end of Stage 1)

The conversation produces these fields, saved to `creator-foundation.md`:

- **Iceberg Statement.** One sentence, the channel's promise: *"I help [Person] [achieve result] by [solving the core problem]."*
- **Bottom of the iceberg.** 8-12 subtopics the creator can teach that deliver on the Iceberg Statement.
- **Person.** Clean public label + structured qualifiers. Never a paragraph-only Person.
- **Positioning Inputs.** Surface problem, deeper blocker, method, raw material, named enemy, stakes, and creator phrases. Internal signals that sharpen the statement and guide downstream skills.
- **Top 3 perceived problems.** Main + 2 supporting, in the avatar's exact language.

## Voice rules (hard, every phase)

These override default writing patterns. If a draft breaks one, the draft is wrong.

- **No em-dashes. Ever.** Use periods, commas, or line breaks. Em-dashes are an AI tell.
- **Declarative. No hedging.** Cut "kind of," "sort of," "I think," "maybe," "tends to." Past tense for results, present tense for principles.
- **No contrast/comparison templates.** Sentences like "Content became a second job. I'm already running the first one." force a shape that isn't the creator's voice. Don't invent that shape.
- **Use the creator's exact words.** When the creator gives you words, sharpen by cutting filler ONLY. Don't reinterpret. Don't switch perspective (third to first person, "they" to "I"). Don't rearrange to fit a template. Their words ARE the brand.
- **Plain beats clever.** Do not invent labels like "doom loop," "trust killer," "wedge," "business gets loud," or "audience can smell it" unless the creator used those words first. Use the creator's phrasing or boring domain words.
- **Pre-output scan.** Before every message to the creator, silently scan for em-dashes, clever labels, generic AI phrases, invented metaphors, and over-polished marketing language. Rewrite before sending.
- **If `foundation/voice-profile.md` exists, load it.** Its anti-patterns and recurring phrases beat defaults. If absent, hold these voice rules as the floor.

## Examples-first protocol (every drafting moment)

Before writing ANY sub-artifact (Iceberg Statement, Top 3 problems, Person, etc.), READ the matching examples in the supporting reference. Find the closest niche or shape. Write IN THAT SHAPE using the creator's actual words.

- **Drafting Top 3 perceived problems:** read `avatar-guide.md` "Bank: viewer-voice problem language by niche." Find the niche closest to the creator's avatar. Match the shape (short declarative sentences, viewer's actual phrasing, three distinct domains).
- **Drafting the Iceberg Statement:** read `positioning-framework.md` locked examples + good/bad pairs. Pull at least three different structural shapes into your head. If you show multiple candidates, they must be structurally different, not three rewordings of one template.
- **Drafting the Person:** read `avatar-guide.md` good/bad avatar pairs. Match the level of specificity (public label + stage + signal of constraint). Rich detail goes in Internal context, not the public label.

Not "consult if stuck." This is "consult before writing." The locked examples in those files have been tested. Default AI writing has not.

## Conversation rules (every phase)

- **One question at a time.** Never list multiple questions in one message. Wait for the answer. React.
- **Short messages.** 3-5 lines is usually right. The reference is for thinking, not for pasting.
- **Tell problems from solutions.** Creators reflexively list solutions ("they need confidence," "they need systems"). Run the disappearance probe: *"If they already HAD that, what would disappear?"* The answer is the actual problem.
- **Push back on vague.** Generic Person, generic Problem, generic Result get one specific probe each. If still generic, pull ONE good/bad pair from `positioning-framework.md` or `avatar-guide.md` to show shape.
- **Notice when the creator's stuck.** Offer two options ("we can do X or Y. Which fits?"). Don't grind on the same question.
- **Check searchability.** Could a viewer Google this? Would 100+ people nod and say "that's exactly me"? If no, the iceberg is too narrow or too vague.
- **Sharp angle before more questions.** If the creator has already given enough signal, name the sharp angle plainly instead of asking another broad question.
- **Internal checklist, not a form.** Run the Sharp Angle Checklist silently. Infer what is already present. Ask only for missing pieces that block the next decision.
- **Reject generic drafts silently.** Throw away weak drafts internally. Show the creator the strongest plain-language version, plus 1-2 structurally different alternatives only when useful.
- **Lock and move.** After 2 sharpening rounds on a sub-artifact, lock the best version and move on. Don't grind. The Iceberg Statement is the goal of Stage 1, not perfectly polished sub-bullets.
- **Read aloud.** Final test on every artifact: *"Read it back. Does it sound like something you'd naturally say when explaining what you do?"* If it feels forced, simplify.

## The 6-phase discovery flow

Run in order. Don't skip phases. Don't batch.

### Phase 1: Opening + offer anchor

**Opener (short, no metaphor explanation):**

> "Let's build your iceberg. We'll lock the top first, then the bottom. First question: what product or service do you currently sell, or plan to sell?"

The product/service answer anchors everything. It IS the result the avatar wants. Everything triangulates against this.

If they share existing positioning, acknowledge briefly then probe the weakest element first. Usually the Person.

### Phase 2: Audience narrowing

**Goal:** specific type of person + their situation. Not "entrepreneurs," not "creators." A real specific human.

**Opening question:**

> "Who specifically is your [offer] designed for?"

**Common issues + how to handle:**

| Issue | Handle |
|---|---|
| Too broad ("entrepreneurs," "small businesses") | "What type of [broad answer] exactly? What stage are they at?" |
| Multiple audiences ("coaches and consultants") | "Two options. (1) Find what naturally unites them. What do they both call themselves, what struggle do they share? (2) Focus on one for clearer messaging. You can still serve both, the channel just speaks to one. What feels more authentic?" |
| Vague situation ("people who want to grow") | "Grow how? Stage of business? Bottleneck they're hitting?" |
| Generic role ("business owners") | "What kind? Service, product, agency, ecom, coach, freelance? What revenue band?" |

**Key probes:**

- "What type of [broad answer] exactly?"
- "What stage are they at?"
- "How do they describe themselves?"

**When sharpening, pull a good/bad pair from `avatar-guide.md`.** Pick the pair closest to their niche. One pair, not four.

**Output of this phase:** Person locked as structured fields:

- **Public label:** clean noun phrase the Iceberg Statement can use.
- **Fit qualifier:** stage, revenue, life moment, industry constraint, or other gate.
- **Expertise / identity role:** why the person recognizes themselves.
- **Business / life context:** the situation that makes the problem urgent.
- **Content / channel role:** why they watch this creator.
- **Demographics:** age, sex, location only when they change examples, buying psychology, voice, or platform behavior. Otherwise mark them "not primary."
- **Internal context:** useful detail that should not bloat the public label.

Do not lock Person as a paragraph. If the creator gives a paragraph, extract the fields. The Iceberg Statement uses the public label, not the whole paragraph.

### Phase 3: Problem discovery

**Goal:** ONE main problem, in the avatar's words, that they actively know they have and want solved. Plus 2 supporting problems.

**Opening question:**

> "What specific problem keeps [avatar] from getting what they want?"

**Problem vs solution:**

Creators list solutions reflexively. "They need confidence." "They need systems." Those are solutions, not problems. The viewer doesn't search YouTube for "I need confidence." They search for the problem confidence would solve.

When they list a solution, run the **disappearance probe:**

> "If they already HAD [solution they listed], what would disappear from their day? That's the actual problem."

**Common issues + how to handle:**

| Issue | Handle |
|---|---|
| Listed a solution ("they need confidence") | Disappearance probe (above) |
| Multiple problems | "Force-rank them. Which one is most urgent. The one keeping them up?" |
| Not desperate enough | "On a 1-10 scale, how urgent is this for them? If it's under 8, we're not at the right problem yet. Keep digging." |
| Expert language ("lack of systems thinking") | "What would THEY say out loud over a beer? More like 'I'm drowning' or 'I keep forgetting things.'" |
| Problem isn't searchable | "Would they actually type that into YouTube? If not, we need a more concrete shape." |

**Once main problem is locked, ask for 2 supporting problems** in different domains:

> "Two more problems they vent about, ideally in different areas. If the first was time-related, the next two might be team-related, money-related, or identity-related."

**Sanity-check:** are the three actually distinct, or three flavors of one? If three flavors of one, keep the strongest, dig for two more in different domains.

**Output of this phase:** ONE main problem + 2 supporting problems, all in viewer language, three distinct domains.

### Phase 4: Sharp Angle Pass + Iceberg Statement (the top)

**Goal:** one sentence. *"I help [Person] [achieve result] by [solving the core problem]."*

Do not open with another broad transformation question if the creator has already given the signal. First, run the Sharp Angle Checklist silently.

**Internal Sharp Angle Checklist:**

- Person
- Fit qualifier
- Desired result
- Business / life consequence
- Surface problem
- Deeper blocker
- Method
- Creator-owned raw material
- Named enemy
- Stakes
- Exact creator phrases worth preserving

Infer as much as possible from prior turns. Do not show this checklist to the creator. It is for Claude to think with, not a form.

If a required piece is visible, propose it back instead of asking:

> "Reading you, the enemy is [creator phrase]. Confirm, or would you name it differently?"

If 1-3 required pieces are missing, ask one focused question at a time. Do not ask the creator to fill the checklist.

**Surface vs deeper wound check:**

If the creator says a broad surface problem like "consistency," "confidence," "growth," "content," or "visibility," ask what keeps it broken or infer it from prior turns.

Good sharp-angle thinking:

- Surface problem: "I can't stay consistent."
- Deeper wound: "Content is supposed to create business growth, but it takes too much time, the creator gets lost, and the usual shortcut makes generic work."

Do not lock the surface problem as the angle until the deeper blocker is clear.

**Creator-facing Sharp Angle Pass:**

Keep this short. Show the distilled signal, not the checklist.

> "Here's the sharp angle I hear:
>
> [Plain-language sharp statement.]
>
> That's sharper than [surface problem] because [one sentence explaining the real blocker or stakes].
>
> Is that the line, or is there a sharper result or enemy?"

Use the creator's actual words where they carry the bite. If the creator said a named enemy like "AI slop," use it. If they did not, use plain language.

**Draft the statement using distinct shapes:**

If one statement is clearly strongest, show that one first. If multiple candidates help, use structurally different shapes from `positioning-framework.md`:

- **Result-first:** "I help [Person] get [result] without [enemy]."
- **Method-first:** "I help [Person] use [method] to get [result] without [enemy]."
- **Raw-material-first:** "I help [Person] turn [what they already have] into [result] without [enemy]."

Do not show three tiny rewordings of the same template.

Optional longer version:

> "I help [avatar] [transformation] so they can [deeper reason]."

**Sharpening probes (use only if the draft is generic):**

| Probe | When to use |
|---|---|
| **Differentiator probe:** "In your niche, what does most everyone compete on. Speed, price, ease, credentials, aesthetics? Which one do you refuse to play on, and what do you own instead?" | When the statement sounds like every other channel in the niche. Use the answer to TIGHTEN the Iceberg Statement so the differentiator gets baked into the sentence. Don't save the answer as a separate field. Pull the Volvo/Red Bull pair from `positioning-framework.md` if they need the shape. |
| **Stretch by exclusion:** "If someone showed up wanting [adjacent thing], who would you tell them to go to instead? Sharpen by who this is NOT for." | When the Person is fuzzy. Exclusion sharpens inclusion. |

**Validation checks (run all five):**

- Can you say it in one breath? (If long-winded, compress.)
- Would 100+ people nod and say "yes, that's exactly what I want"? (If no audience that size, too narrow.)
- Would they search YouTube for this problem? (If no, wrong shape.)
- Does it contain enough tension? Person + result + method/raw material + enemy/stakes. If not, it will sound generic.
- Read it aloud. Does it sound like something you'd naturally say? (If forced, simplify.)

**Output of this phase:** Iceberg Statement (locked, with the differentiator baked into the sentence) plus Positioning Inputs saved as internal context.

### Phase 5: Bottom of the iceberg (subtopics)

**Goal:** 8-12 subtopics the creator can teach that solve the top problem. The menu. Not videos. Subtopics.

**Opening question:**

> "Now the bottom. List the subtopics you can teach that solve [main problem] for [avatar]. Not video titles. Subtopics. The categories of teaching."

**Prompt for breadth. The bottom should be wide:**

- "What techniques or methods do you teach?"
- "What mindset shifts?"
- "Stories from your own journey or your clients'?"
- "Common mistakes you fix?"
- "Adjacent topics that still solve the main problem?"

If they give 3 and stop, prompt with one example from their niche to show how broad the bottom can be.

**Validate:** "If someone implemented everything on this list, would they achieve [transformation]?"

If no, the bottom has gaps. Ask what else.
If yes, locked.

**MVP note:** this list grows with experience. 8-12 subtopics is the starting set. Refine as published videos surface what actually resonates.

**Output of this phase:** 8-12 subtopics.

### Phase 6: Final validation + fit check

Show the full iceberg back to the creator, top and bottom. Confirm:

- Iceberg Statement focuses on ONE problem the avatar knows they have
- Statement targets a specific, recognizable Person
- Language is clear and authentic, not jargony, not salesy
- Bottom items all clearly tie to solving the top
- Bottom is wide enough that the creator has 6 months of video angles before the menu thins

**Read-aloud test (final):**

> "Read your Iceberg Statement out loud. Does it sound like something you'd naturally say when someone asks what you do? If it feels forced, we simplify."

If they reword anything when reading it aloud, the version they reword TO is closer to the truth. Use that version.

**Demographics light pull (only if useful and not already surfaced):**

> "Quick fit check before we save: do age, sex, or location change how you'd speak to this person, or are they not primary here?"

If demographics matter, capture them specifically. If they do not matter, mark them "not primary" and prioritize role, stage, constraint, and buying context. Don't grind. MVP. Refine with real audience data later.

**Save** to `creator-foundation.md` using `assets/creator-foundation-template.md`.

## Edge cases

**Creator never had the avatar's problem** (doctor, physio, consultant): swap "you" for "a real client" through problem discovery. Real client, real problem, real outcome. Attribute clearly. Never fabricate.

**Brand-new creator with no clients yet:** educated guesses are fine for MVP. Flag it: *"We're guessing for now. The iceberg refines once you publish 3-4 videos and see what real comments come in."*

**Creator wants to serve multiple audiences:** see Phase 2 multi-audience handling. Pick one for the channel. Run vid-foundation again later for a second audience.

**Creator gives a list of 12 problems and refuses to pick one:** force-rank by 1-10 urgency for the avatar. Highest urgency wins. Tell them: *"We can always come back. The bottom of the iceberg lets you teach all 12. But the top has to be one."*

## What good output looks like

A locked iceberg artifact has:

- **Iceberg Statement** under 20 words, one breath, viewer would search the problem on YouTube, the differentiator baked into the sentence (not generic)
- **Person** specific: clean public label, role/stage signal, useful qualifiers, demographics only when they matter
- **Positioning Inputs** captured: surface problem, deeper blocker, method, raw material, named enemy, stakes, creator phrases
- **Top 3 problems**: main + 2 supporting, in viewer's exact language, three distinct domains
- **Bottom**: 8-12 subtopics, all clearly tied to the top, varied (techniques, mindset, stories, adjacent)
- **Read-aloud test passed**: creator didn't reword the Iceberg Statement when reading it back

If any of these miss, keep working. Don't lock too soon.

## Anti-patterns

- Letting the creator stay vague to be polite. Specificity is the whole point. Push back.
- Drafting the Iceberg Statement FOR the creator. They drive. Claude probes and tightens.
- Locking the top before checking against the avatar. Person and Problem have to align.
- Locking Person as a paragraph. The public label has to be usable in the Iceberg Statement.
- Showing the Sharp Angle Checklist to the creator as a form. It is internal. Ask only for missing pieces.
- Asking for a named enemy when the creator already gave one. Propose and confirm instead.
- Narrating every weak draft. Reject generic drafts silently and show the sharper version.
- Writing the bottom as video titles instead of subtopics. Subtopics, not videos.
- Pulling more than one good/bad pair at a time. One pair to illustrate. Never a list.
- Skipping the read-aloud test. It's the final filter on whether the iceberg is the creator's voice or Claude's.
- Explaining the iceberg metaphor in chat. The skill executes. The metaphor gets taught elsewhere.
