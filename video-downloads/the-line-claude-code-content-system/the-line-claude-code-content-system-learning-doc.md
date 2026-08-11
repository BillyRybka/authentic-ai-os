# "The Line". System Teardown for Replication

**Source:** YouTube, "I replaced my entire content team with Claude Code and it's insane!" (12:27)
**Builder:** Duncan (Claude Code Club / The Build Room). 67.6K subs, 4.1M views, 573 videos
**What it is:** A single-page web dashboard that runs seven Claude Code skills as a linear content pipeline, from competitor research to published cross-platform derivatives
**Total observed run cost for the ideation half:** ~$1.10 and ~7 minutes of wall clock

---

## The architecture in one paragraph

The Line is a **thin web UI over Claude Code skills**. Nothing clever happens in the browser. Each colored section on the page is one skill. You click Run, the skill executes, and the results render back into that section as a grid of scored cards. Each card is a decision. You click the card you want, and that selection becomes the input to the next section down. The page is the state; the skills are the work. There is a closed feedback loop at the bottom (Performance) that feeds back into the top (Angles).

---

## The seven modules

| # | Module | Color | Input | Data sources | Output | Cost / time |
|---|--------|-------|-------|--------------|--------|-------------|
| 1 | **ANGLES** | Red | Nothing (zero-input) | Recent uploads from ~30 competitors via YouTube Data API + own video archive | Ranked cards, each an uncovered angle with its demand signal | $0.24 / 152s |
| 2 | **IDEATION** | Black | The selected Angle card | Obsidian vault: `what-works-youtube.md`, `ICP-language-library.md`, the video archive | 3 positioned concepts, each with title options, gap, audience desire, shock score, "why now" rationale | $0.39 / ~3 min |
| 3 | **HOOKS** | Blue | Title + angle + audience desires | Hook swipe file, ICP language library, Kallaway desire framework | 3 hook sets, each with a Visual / Spoken / Text hook + score | not stated |
| 4 | **TITLES** | Red | The selected hook + concept | Own recent videos ranked by views, YouTube title research | 3 tiers of titles + character count + pattern + why + suggested thumbnail text | $0.24 |
| 5 | **THUMBNAIL** | Yellow | Title + thumbnail text from module 4 | Baked-in swipe of high-performing thumbnails (his + competitors'), reference photos of himself, company logos | 3 **rendered 4K 16:9 images** via Nano Banana, each in a different named style | not stated |
| 6 | **CASCADE** | Dark blue | YouTube URL (blank = auto-detect latest) | The published video | LinkedIn x2, Pinterest, Instagram carousel, Facebook, Reddit, X thread, Gumroad page + ManyChat and Leadshark automations | 10-15 min |
| 7 | **PERFORMANCE** | (below fold) | Nothing | Own channel analytics + **comments** | Videos scored /10 with why-it-worked analysis and what to make next | not stated |

Modules 1-5 run before filming. Module 6 runs after publishing. Module 7 closes the loop back to module 1.

---

## The core design pattern: self-documenting modules

**Key insight:** Every module on the page displays its own spec in labeled columns, visible before you run it. This is the single most copyable idea in the video.

Every section expands to show five fields:

| Field | What it holds | Example (ANGLES) |
|-------|---------------|------------------|
| **PURPOSE** | One sentence on the job | "Surface video angles Duncan hasn't covered" |
| **INPUT** | What it consumes | "Nothing" |
| **LOOK UP / API / DATA SOURCES** | Exactly where data comes from | "Recent uploads from 30 competitors via YouTube Data API" |
| **DECISION PROCESS** | The reasoning it applies | "Compare what competitors are publishing against Duncan's archive" |
| **OUTPUT** | The artifact shape | "A ranked set of cards" |

That five-field contract is effectively the skill's frontmatter surfaced in the UI. It means the operator never has to remember what a step does, and the skill and the UI can't drift apart.

**Action:** Whatever pipeline you build, force every stage to declare Purpose / Input / Sources / Decision / Output, and render that declaration in the interface itself.

---

## The core design pattern: scored cards as the handoff

**Key insight:** Every module outputs the same shape. A grid of cards, each scored, each with its reasoning exposed, plus a recommendation at the bottom telling the operator which one to pick.

A card is never just an idea. It carries:
- the artifact (an angle, a concept, a hook, a title, an image)
- a numeric score
- the **evidence** that produced it ("Nate and RoboNuggets both published on dynamic workflows this week")
- the **gap** it fills (competitor covers it / I don't)
- the **desire** it hits (money, time, status)
- a "why now" rationale citing a named competitor pattern ("Jack Roberts' I Replaced X format is his fastest growing format")

Then below the grid: **"the Claude read on it."** A short block that says which card to pick and why. He follows the recommendation live on camera in every single module.

**Why this matters for replication:** The handoff between skills is a *human click*, not an automated chain. That's a deliberate choice. It keeps the operator in the loop at every stage while removing all the blank-page work. It also means each skill can be run standalone.

**Action:** Standardize on one output contract across all skills. Scored card + evidence + recommendation. Uniform output is what makes seven separate skills feel like one product.

---

## The intelligence layer: the vault does the personalization

The skills are generic. The **files** are what make the output sound like him. Three named assets do the heavy lifting:

| File | What's in it | Which module uses it |
|------|--------------|---------------------|
| `ICP-language-library.md` | Verbatim audience phrases, sorted by where they were captured. "Exact Phrases (from coaching calls)" and "Exact Phrases (from LinkedIn/YouTube comments)". Real lines: "I'm not a content person", "I watch people with half my skills get all the clients", "I tried posting once and nothing happened" | Ideation, Hooks |
| `what-works-youtube.md` | Research on what performs on the platform | Ideation, Titles |
| Hook swipe file | Collected hooks that worked | Hooks |
| Video archive | His own published videos with view data | Angles, Ideation, Titles |
| Thumbnail swipe + reference photos + logos | High performers from him and competitors, plus images of his own face | Thumbnail |

He calls the ICP language library the thing he most recommends other people build. It is the reason the hooks come out in audience language rather than marketing language.

**Action:** Before building any of the skills, build the language library. Capture the exact words, from calls and comments, verbatim, with the source noted. Everything downstream is only as good as this file.

---

## The scoring systems

Different modules score on different scales, deliberately.

| Module | Scale | What the score means |
|--------|-------|---------------------|
| Angles | /3 | Coarse triage. Is this gap worth attacking |
| Ideation | /100 (85, 81, 79 observed) | Includes a **shock score** ("people on the internet like to be shocked") |
| Hooks | /100 (88, 92, 82 observed) | Retention likelihood against the Kallaway desire framework |
| Titles | Tiered, then scored | **Tier 1** high confidence, **Tier 2** calculated risk, **Tier 3** swing for the fences. Built for A/B testing |
| Performance | /10 (8.8 top) | How well the published video actually did |

The three-tier title structure is the sharpest bit here. It isn't "give me 10 titles." It's a risk ladder, so the operator can consciously choose how much they're gambling on this upload.

---

## The remix principle behind Ideation

**Key insight:** One angle should produce many videos, not one.

His stated reasoning: "the big creators do this. They take a concept and they remix it or they use it over and over again because it's working... You could create 10 different videos on dynamic workflows."

So Ideation exists purely to fan one validated angle into several distinct positions:
- The Content Pipeline Replacement Story (score 85)
- The Token Trap Fix (81). Sourced from the #1 complaint in comments on workflow videos: token burn
- The Contrarian Verdict (79)

Note that "The Token Trap Fix" came out of **comment mining**, not competitor titles. The system reads audience objections and turns them into positioning.

---

## The Cascade: the highest-leverage module

Runs after publishing. One input (a YouTube URL, or blank to auto-grab the latest). 10-15 minutes. It doesn't draft, it **publishes** and it **wires up automations**.

What it produces:

1. **LinkedIn personal post.** Full text, thumbnail pulled in, lead-magnet CTA ("Comment PRETZEL and I'll send it over")
2. **Leadshark automation, created automatically.** Rule: comment contains PRETZEL → send DM. One post processed **221 DMs = 221 leads**
3. **LinkedIn company page post** (The Build Room). A *variant*, not a duplicate
4. **Pinterest pins.** Admittedly low engagement, kept for SEO and long-tail discovery
5. **Instagram carousel.** Multi-slide, solid red background, bold type, one idea per slide ("YOUR BUSINESS LIVES IN 8 TABS", "AGENTS THAT CHECK EACH OTHER"). Caption + CTA word written too
6. **ManyChat sequence, created automatically.** Comment keyword → DM asking them to follow to get the link
7. **Facebook page post**
8. **Reddit post** to r/ClaudeAI, written in native Reddit voice ("I had Claude Opus 4.8 build me a custom 'operating system' for my business while I was at the vet")
9. **X thread.** Main post + reply carrying the link (link out of the first tweet, deliberately)
10. **Gumroad product page.** Thumbnail, full written description, a generated **HTML guide**, embedded YouTube player inside the product description, and a full setup walkthrough. Free, but tipped

**Key insight:** The repurposing isn't the leverage. The **automation wiring** is. Most people who build a cascade generate ten posts. He generates ten posts *and* creates the DM automations that convert the comments those posts get. That's the difference between distribution and lead capture.

**Second insight:** Every platform gets native treatment. The Reddit post reads like Reddit. The X post splits the link into a reply. The LinkedIn company post is reworded from the personal one. Nothing is copy-pasted across channels.

---

## The loop

```
PERFORMANCE  →  ANGLES  →  IDEATION  →  HOOKS  →  TITLES  →  THUMBNAIL
     ↑                                                            ↓
     └──────────────  CASCADE  ←──  film + publish  ←─────────────┘
```

Performance reads the channel **and the comments**, scores recent videos out of 10, explains why the winner won, and outputs what to make next. That output is the demand signal Angles consumes on the next cycle. From the video: breakout was "Claude Opus 4.8 Built an Agentic OS in 15 Minutes (Ultracode)" at 8.8, and the recommendation was to double down with "I built a full content business in 30 minutes with Claude workflows."

A **"run it back"** button clears all module state and resets to the top.

---

## What it looks like

Worth copying, because the look is doing real work.

- **Single page, vertical stack.** No routing, no tabs. Scroll = pipeline order
- **Retro aesthetic.** Beige background, bold saturated color blocks, heavy stylized type
- **One color per module** (red, black, blue, red, yellow, dark blue). Color is the wayfinding
- **Stats header.** Subs / views / watch hours / revenue / video count, always visible top right
- **Recent Long-Form and Recent Shorts grids** directly under the title, so context sits above the work
- **Collapsed by default.** Each module is a closed accordion. Expand to see the spec, run to see the cards
- **Run metadata surfaced.** Cost in dollars and execution time in seconds displayed above every result set. He calls this out explicitly because "a lot of people ask how much things cost"

Displaying per-run cost on the interface is a small touch with outsized trust value. It makes the economics of the system legible while you use it.

---

## Toolchain

| Layer | Tool |
|-------|------|
| Orchestration | Claude Code skills (7 of them) |
| Interface | Custom web app, built with Claude Code |
| Competitor data | YouTube Data API (~30 tracked competitors) |
| Knowledge base | Obsidian vault (dense wikilinked graph shown on screen) |
| Image generation | Nano Banana (referenced on-screen as Genmo), 4K, 16:9 |
| LinkedIn/IG DM automation | Leadshark, ManyChat |
| Product hosting | Gumroad |
| Distribution | Skool community, `the-line.zip` download |

---

## Common mistakes this system avoids

**Starting from a guess.** Angles takes zero input and starts from what competitors are *currently* getting views on. Every idea in the pipeline traces back to observed demand, never to a brainstorm.

**Generic best practices.** Titles are scored against his own channel's over-performing patterns, not against YouTube advice. Stated explicitly: "there's not going to be generic or best practices."

**Descriptions instead of assets.** The thumbnail module renders actual 4K images. A thumbnail *description* is not a deliverable. Same logic runs through Cascade, which publishes rather than drafts.

**One idea per angle.** Ideation exists because the failure mode is treating a validated topic as a single video instead of a vein to mine.

**Repurposing without capture.** Ten posts with no automation behind them is ten posts. The Leadshark and ManyChat wiring is what turned one LinkedIn post into 221 leads.

**Copy-paste cross-posting.** Every channel gets a native rewrite.

---

## If you're going to mimic this

Build order, cheapest to most valuable:

1. **The language library first.** `ICP-language-library.md` with verbatim audience phrases, tagged by source. Nothing downstream works without it
2. **The swipe files.** What-works notes, hook swipe, thumbnail swipe (yours + competitors'), reference photos
3. **The competitor list.** ~30 channels, pulled via YouTube Data API for titles, view counts, views/day
4. **Standardize the card contract** before writing a single skill. Artifact + score + evidence + gap + desire + rationale + recommendation
5. **Standardize the module spec** (Purpose / Input / Sources / Decision / Output) and render it in the UI
6. **Build modules 1-2 only** (Angles, Ideation) and run them for two weeks. That's where the compounding is
7. **Add Performance early**, not last. It's what makes the system get smarter instead of just faster
8. **Cascade last.** It's the biggest build and it's worthless until you're publishing consistently
