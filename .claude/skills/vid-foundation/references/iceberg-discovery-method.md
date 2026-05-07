# Iceberg Discovery Method

The conversation backbone for Stage 1 of vid-foundation. Walks the creator from "what do you sell?" to a locked iceberg — top (channel positioning) + bottom (subtopic angles that solve it).

This file is for Claude to drive the conversation with. Do **not** paste it into chat. Use it to know which question comes next, when to push back, which probe to pull, and what good output looks like.

## The iceberg

```
TOP        →  positioning statement
              "I help [Person] [achieve result] by [solving problem]."
              The single sentence the channel lives under.

BOTTOM     →  8–12 subtopic angles
              everything the creator can teach to solve the top problem.
              Different topics; all trace back to the top.
```

Top = thumbnail / title / cold-viewer hook. Bottom = the menu the creator pulls from when planning videos.

## Conversation rules (every phase)

- **One question at a time.** Never list multiple questions in a single message. Wait for the answer. React.
- **Short messages.** 3-5 lines is usually right. The reference is for thinking, not for pasting.
- **Distinguish problems from solutions.** Creators often list solutions ("they need confidence," "they need systems"). The probe: "If they already HAD that, what would disappear?" The answer is the actual problem.
- **Push back on vague.** Generic Person, generic Problem, generic Result get one specific probe each. If still generic after the probe, pull ONE good/bad pair from `positioning-framework.md` or `avatar-guide.md` — never four.
- **Recognize when the creator's stuck on a yes/no.** Offer two options ("we can either X or Y — which feels more authentic?"), don't grind on the same question.
- **Validate searchability.** Could a viewer Google this? Would 100+ people nod and say "that's exactly me"? If the answer's no, the iceberg is too narrow or too vague.
- **Read aloud.** Final test on every artifact: "Read it back. Does it sound like something you'd naturally say when explaining what you do?" If it feels forced, simplify.

## The 6-phase discovery flow

Run sequentially. Don't skip phases. Don't batch.

### Phase 1 — Opening

**Brief opener:**

> "Let's build the iceberg for your channel. Top = the one-sentence umbrella every video lives under. Bottom = the subtopic angles you can teach that solve the top problem. We'll work top-down. Doesn't have to be perfect — we'll sharpen as we go."

**Anchor question:**

> "What product or service do you currently sell, or plan to sell?"

Why this anchors first: it stops abstract positioning loops. The product or service IS the result the avatar wants. Everything else triangulates against this.

If they share existing positioning, acknowledge briefly then probe the weakest element first (usually the Person — most creators target too broadly).

### Phase 2 — Audience narrowing

**Goal:** Specific type of person + their situation + desired outcome. Not "entrepreneurs." Not "creators." A real specific human.

**Opening question:**

> "Who specifically is your [offer] designed for?"

**Common issues + how to handle:**

| Issue | Handle |
|---|---|
| Too broad ("entrepreneurs," "small businesses") | "What type of [broad answer] exactly? What stage are they at?" |
| Multiple audiences ("coaches and consultants") | "We've got two options. (1) Find what naturally unites them — what do they both call themselves, what struggle do they share? (2) Focus on one for clearer messaging — you can still serve both, the channel just speaks to one. What feels most authentic?" |
| Vague situation ("people who want to grow") | "Grow how? Stage of business? Bottleneck they're hitting?" |
| Generic role ("business owners") | "What kind? Service, product, agency, ecom, coach, freelance? What revenue band?" |

**Key probes:**

- "What type of [broad answer] exactly?"
- "What stage are they at?"
- "How do they describe themselves?"

**When sharpening, pull a good/bad pair from `avatar-guide.md`** — pick the pair closest to their niche. One pair, not four. Show what specific looks like.

**Output of this phase:** Person locked. Specific role + stage + (optionally) revenue/life stage marker.

### Phase 3 — Problem discovery

**Goal:** ONE main problem, in the avatar's words, that they actively know they have and want solved. Plus 2 supporting perceived problems for the avatar's Top 3 list.

**Opening question:**

> "What specific problem keeps [avatar] from getting what they want?"

**Critical distinction — problems vs. solutions:**

Creators list solutions reflexively. "They need confidence." "They need systems." "They need clarity." Those are solutions, not problems. The viewer doesn't search YouTube for "I need confidence." They search for the problem confidence would solve.

When they list a solution, run the **disappearance probe:**

> "If they already HAD [solution they listed], what would disappear from their day? That's the actual problem."

**Common issues + how to handle:**

| Issue | Handle |
|---|---|
| Listed a solution ("they need confidence") | Disappearance probe (above) |
| Multiple problems | "Force-rank them. Which one is most urgent — the one keeping them up?" |
| Not desperate enough | "On a 1–10 scale, how urgent is this for them? If it's under 8, we're not at the right problem yet — keep digging." |
| Expert language ("lack of systems thinking") | "What would THEY say out loud over a beer? More like 'I'm drowning' or 'I keep forgetting things.'" |
| Problem isn't searchable | "Would they actually type that into YouTube? If not, we need a more concrete shape." |

**Key probes:**

- "If they already HAD [solution], what would disappear?"
- "Would they actually search YouTube for this?"
- "Which problem is MOST urgent?"

**Once main problem is locked, ask for 2 supporting problems** (different domains — if main is time/workflow, supporting could be team/identity/money):

> "Two more problems they vent about, ideally in different areas. If the first was time-related, the next two might be team-related, money-related, or identity-related."

**Sanity-check:** Are the three actually distinct, or three flavors of one? If three flavors of one — keep the strongest, dig for two more in different domains.

**Output of this phase:** ONE main problem (most urgent, in viewer's exact words) + 2 supporting problems (different domains).

### Phase 4 — Iceberg Top (positioning statement)

**Goal:** One sentence — *"I help [Person] [achieve result] by [solving the core problem]."*

**Opening question:**

> "What transformation does [avatar] desperately want — what's the result they'd hand you a testimonial for?"

Then:

> "And what's the deeper reason underneath? What would this transformation let them do that they can't do now?"

**Draft the top:**

> "I help [avatar] [transformation] by [solving main problem]."

Optional longer version:

> "I help [avatar] [transformation] so they can [deeper reason]."

**Sharpening probes (use only if the draft is generic):**

| Probe | When to use |
|---|---|
| **Axis-of-differentiation:** "In your niche, what does most everyone compete on — speed, price, ease, credentials, aesthetics? Which one do you refuse to play on, and what do you own instead?" | When the statement sounds like every other channel in the niche. Pull Volvo/Red Bull example from `positioning-framework.md` if they need the shape. |
| **Known-for-one-thing:** "If your channel hit, what's the single word people would associate with you? (Volvo = safety. Red Bull = energy. The narcissist lady. The cheese guy.)" | When the statement covers too many problems. Forces compression to one concept. |
| **Stretch by exclusion:** "If someone showed up wanting [adjacent thing], who would you tell them to go to instead? Sharpen by who this is NOT for." | When the Person is fuzzy. Exclusion sharpens inclusion. |

**Validation checks (run all four):**

- Can you say it in one breath? (If long-winded, compress.)
- Would 100+ people nod and say "yes, that's exactly what I want"? (If no audience that size — too narrow.)
- Would they search YouTube for this problem? (If no — wrong shape.)
- Read it aloud. Does it sound like something you'd naturally say? (If forced — simplify.)

**Output of this phase:** Iceberg Top — locked positioning statement.

### Phase 5 — Iceberg Bottom (subtopic angles)

**Goal:** 8-12 subtopic angles the creator can teach that solve the top problem. The menu. Not videos — angles.

**Opening question:**

> "Now the bottom of the iceberg. List everything you can teach that helps [avatar] solve [main problem]. Not video ideas — angles. Topics. Categories of teaching."

**Prompt for breadth (the bottom should be wide):**

- "What techniques or methods do you teach?"
- "What mindset shifts?"
- "Stories from your own journey or your clients'?"
- "Common mistakes you fix?"
- "Adjacent topics that still solve the main problem?"

If they give 3 and stop: prompt with one example from their niche to show how broad the bottom can be. "For a YouTube-for-business channel, the bottom might include: titles, thumbnails, hooks, retention, monetization, the script structure, idea generation, outliers, packaging, niches, audience research, positioning. All of those solve 'how do I grow my channel for sales' even though they look like different topics."

**Validate:** "If someone implemented everything on this list, would they achieve [transformation]?"

If no — the bottom has gaps. Ask what else.
If yes — locked.

**Note:** This list will grow with experience. MVP = 8-12 angles; refine as published videos surface what actually resonates.

**Output of this phase:** Iceberg Bottom — list of 8-12 subtopic angles.

### Phase 6 — Final validation

Present the full iceberg back to the creator. Both top and bottom. Confirm:

- Top focuses on ONE problem the avatar knows they have
- Top targets a specific, recognizable Person
- Top language is clear and authentic — not jargony, not salesy
- Bottom items all clearly tie to solving the top
- Bottom is wide enough that the creator has 6 months of video angles before the menu thins

**Read-aloud test (final):**

> "Read your top sentence out loud. Does it sound like something you'd naturally say when someone asks what you do? If it feels forced, we simplify."

If they reword anything when reading it aloud — the version they reword TO is closer to the truth. Use that version. Save.

## Demographics — pulled from the conversation

By Phase 5, the conversation usually surfaces age range, sex skew, and location naturally. After the iceberg locks, do a quick light pull:

> "Quick demographics check before we save: age range (specific span — 28-42, not 18-60), sex skew, location, type-of-person label."

If something didn't surface naturally, ask. Don't grind. MVP — refine with real audience data later.

**Output:** Person details fully captured — age, sex, location, type.

## Edge cases

**Creator never had the avatar's problem** (doctor, physio, consultant): swap "you" for "a real client" throughout problem discovery. Real client, real problem, real outcome. Attribute clearly. Never fabricate.

**Creator is brand new and doesn't have a real client either:** use educated guessing for MVP. Flag it: "We're guessing for now; the iceberg refines once you publish 3-4 videos and see what real comments come in."

**Creator wants to serve multiple audiences:** see Phase 2 multi-audience handling. Pick one for the channel, run vid-foundation again later for a second audience.

**Creator gives a list of 12 problems and refuses to pick one:** the most common stuck state. Force-rank by 1-10 urgency for the avatar. Highest urgency wins. Tell them: "We can always come back. The bottom of the iceberg lets you teach all 12 — but the top has to be one."

## What good output looks like

A locked iceberg artifact has:

- **Top sentence** — under 20 words, one breath, viewer would search the problem on YouTube
- **Top is differentiated** — the axis-of-differentiation probe was answered (we own X, refuse to play on Y)
- **Person is specific** — age range, type-of-person label, role/stage signal
- **Top 3 problems** — main + 2 supporting, in viewer's exact language, three distinct domains
- **Bottom list** — 8-12 angles, all clearly tied to the top, varied (techniques, mindset, stories, adjacent topics)
- **Read-aloud test passed** — creator didn't reword the top when reading it back

If any of these miss → keep working. Don't lock prematurely.

## Anti-patterns

- Letting the creator stay vague to be polite. Specificity is the whole point — push back.
- Drafting the iceberg FOR the creator. They drive. Claude probes and tightens.
- Locking the top before checking against the avatar. Person and Problem must align.
- Writing the bottom as video titles instead of subtopic angles. Angles, not videos.
- Pulling more than one good/bad pair at a time. One pair to illustrate. Never a list.
- Skipping the read-aloud test. It's the final filter on whether the iceberg is the creator's voice or Claude's.
