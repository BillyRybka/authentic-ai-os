# Skill Template

The house shape for skills in this vault. Dev-facing, never shipped, never loaded at runtime.

This is a shape, not a checklist. It exists so a reader can open any skill and know where to look, and so an audit has something to check against. It governs the container. Whether the output is any good is a separate problem, and the craft lessons for that live in [skill-writing-lessons.md](skill-writing-lessons.md).

**The one rule that outranks the template:** a section that would be empty or filler gets cut, not filled. A skill with six real sections beats one with nine, three of which say nothing.

---

## The fixed spine

Every skill runs these in this order. The order is the point: what matters, what you load, what you do, what you produce, how you check.

### 1. Frontmatter

```yaml
---
name: skill-name
description: What it does in one or two sentences, then the trigger phrases. Nothing else.
---
```

The description is the trigger mechanism, not documentation. Behavior, principles, and mechanics go in the body. The long part should be example phrasings a creator would actually say, varied in formality, including ones that never name the skill.

### 2. Title and purpose

One paragraph. What goes in, what comes out, what runs next.

### 3. Scope line

Bold, one line, right under the purpose. What this skill does **not** do, and who does that instead. This is what stops a writing skill from re-planning and a planning skill from writing prose.

> **Scope: the plan, never the prose.** No intro, no segment prose, no ending, no title, no thumbnail. It does not re-pick the angle or the format; framing locked those.

### 4. Core principles

Each states the rule **and the mechanism behind it**, because a model given the mechanism reasons correctly in cases you never wrote down, and a model given a bare NEVER only handles the case you thought of.

> **Payoff late is judgment, not a rule.** The viewer clicked holding one question, and once the full answer lands, their reason to stay is gone.

Not:

> **NEVER pay off the title early.**

If a principle has no why, either find it or cut the principle.

The why does not have to ride in the same sentence, and usually reads better when it does not. See [How it reads](#how-it-reads).

### 5. What loads, and when

A table: File / Step / For. One row per file, stated once, never repeated at each step. Then the stops (what to do when a required file is missing, and which skill to route to) and any re-run mode.

Never front-load. Never bulk-load the banks.

**The one exception: voice reloads immediately before generation.** Strategy files (the avatar, the goal, the format, the plan) load once at the step that decides something and hold. Voice does not. Reference pieces and the refusals list loaded four steps earlier have decayed by the time the first word gets written, and the draft comes out sounding like a competent stranger. Any skill that produces prose in the creator's voice reloads the voice files as the last thing before drafting, and says so in that step. Repeating a load is a smell everywhere else and correct here.

### 6. The workflow

Numbered steps, scannable, not multi-paragraph walkthroughs. Each step is one move. Where a step needs depth, one line points at the reference that holds it.

**Mark the gates.** Where the creator has to decide before the skill continues, say so plainly on its own line:

> **Stop here. The creator locks the spine before anything gets built out.**

The gates are the whole reason a creative skill is worth running interactively. The default failure is the model sprinting to a finished artifact nobody shaped, and that failure is expensive because the output looks done. Soft phrasing ("show the spine") does not hold. This is the one place blunt beats explained.

A gate holds better when it names the wrong output, not just the stop: "bullet points describing what each section covers, a skeleton, not a draft" beats "do not write yet." The model can comply with the first one.

**Put a rule where it fires.** A rule about padding a list belongs in the step that builds the list, not in a rules section three screens away. Principles up top carry the ideas that shape every step; anything that guards one specific move goes next to that move, with the failure it prevents named. "Equal weight to five ideas turns a punchy post into a shallow blog post" works because the model is about to do exactly that.

Step numbers are internal. The creator never hears "step 2 complete."

Where a workflow runs long enough that the shape gets hard to hold, close it with a one-glance table: step, what happens, what the creator picks from. It shows the whole interaction and every gate in one place, for the reader and for the model.

### 7. Output and handoff

What lands on disk, in what shape, and who reads it next. Exact shapes live in `assets/`, not here. Field ownership lives in `knowledge/piece-contract.md`, not here.

A leaf skill names its prerequisite and its immediate handoff, nothing more. It does not narrate the pipeline; the orchestrator owns the chain.

### 8. Before you save (or: before you present)

The last thing the model reads before it writes or shows the work.

Long checklists do not get run. Twenty-seven items is a document; eight is a gate. Every line has to be something a reader could actually fail.

### 9. References for depth

One line per file, saying what is in it and when to open it.

---

## How it reads

Our habit is to fuse the rule and its reason into one sentence, so most lines land as three stacked clauses. Nothing is wrong in them. They are just tiring, and a tired reader skims, which costs more than the words saved.

Same content, breathing:

> **Dense:** Never pad to a count. Mining yields what it yields, and a gap between the points and the format's shape gets surfaced, thin dump back to `vid-intake` or wrong format back to `vid-framing`, never filled with tangents.
>
> **Breathing:** Never pad to a count. Mining yields what it yields.
>
> If the points come up short of the format's shape, that is information, not a hole. A thin dump goes back to `vid-intake`. A wrong format goes back to `vid-framing`.
>
> Nothing was cut. It became three sentences instead of one, and now it can be read at speed.

**Compress where a judgment gets made.** The mechanism has to sit next to the rule it explains, or the model applies the rule and misses the point. Those lines earn their density.

**Let everything else breathe.** Procedure, loads, output, checks. Nobody reads a step for nuance; they read it to know what to do next. One move per line.

The test on any sentence: if every clause is load-bearing, keep it. If two clauses restate each other or hedge, split them and lose nothing.

Line count is the wrong metric. A 200-line skill that can be scanned beats a 120-line skill that has to be studied. The question is whether a human hunting for one thing finds it in ten seconds.

### What a step looks like at the right density

```markdown
### 1. Rough the spine

1. **Mine the dump against the angle.** Every block gets one tag: main point,
   subpoint, combine, or tangent. Silent work; the method and a worked tagging
   pass are in `references/brain-dump-mining.md`.
2. **Check the fit.** If the surviving material does not fit the locked format,
   surface it now rather than shaping a spine around a mismatch.
3. **Shape the survivors to the format.** Lay the main points into the planner's
   body shape. Each gets a couple of subpoints saying what it actually claims.
4. **Show the spine.** Points, subpoints, and the cuts.

**Stop here.** The creator adds, cuts, merges, reorders. Nothing gets built out
until the spine is locked.
```

Each move is a bolded verb plus one or two sentences. Depth is a pointer, not a paragraph. The gate is on its own line where it cannot be skimmed past.

---

## Show the difference

A rule tells the model what to avoid. A pair shows it what the line looks like. Pairs are the most useful thing in our best skills, and every skill that produces something a human judges should carry a few.

Always both halves. A good example alone teaches surface-matching: the model copies the shape and reproduces the same mistake in new words. The weak half is what makes the distinction visible.

**Name why the weak one fails, in one line.** That line does the teaching, not the examples.

From vid-framing, on reading the viewer:

> Thin: "the viewer is an ADHD entrepreneur, the problem is planning, the payoff is a weekly plan."
>
> Strong: "she has bought the planners and tried the apps, she thinks she needs to plan harder, and every system she tries fights her brain, so she quits by week two and decides she is the broken one."
>
> Every word of the thin one is true and none of it is useful. There is nothing to push against.

From vid-title, on adjusting a proven structure to new material:

> Dead: outlier is "Gym MISTAKES That Kill Your Progress", the video is meal prep, you write "Meal Prep Mistakes That Kill Your Progress." Nouns swapped, pull lost. "Progress" was the gym audience's stake, not this one's.
>
> Alive: "Meal Prep Mistakes That Keep You Ordering Takeout." The engine survives and the stake is now this avatar's actual one.

### Three kinds, doing different jobs

- **The contrast pair.** Teaches a judgment call. Short, inline in SKILL.md, right at the step where the call gets made.
- **The worked artifact.** Thin version against complete version of the thing the skill produces. Teaches the output bar. Inline if short, a reference if it runs long (`references/point-planning.md`).
- **The worked session.** A dialogue showing pacing, gates, and how a creator pushes back. Always a reference, never SKILL.md (`references/structure-conversation-examples.md`).

### What makes an example useless

- **Placeholders.** `## Item 3: {second main point}` teaches nothing. Examples run on real material: a real title, a real client story, a real number.
- **One-sided.** The good half alone, with no failure to contrast against.
- **Too close to one case.** If the example is the only situation it fits, the model treats it as the template. Say what carries across ("the shape, not the words"), or pick an example from a different domain than the one the creator is working in.

The deletion test applies here too. An example earns its place when cutting it would change what the model produces.

---

## Where things live

| Layer | Holds | Test |
|---|---|---|
| `SKILL.md` | Everything load-bearing on every run | Does the skill still work correctly if the model never opens anything else? If no, it belongs here. |
| `references/` | Method depth: worked examples, decision logic, calibration | Depth and judgment, opened at a named step. Never the core loop. |
| `assets/` | The exact shape of what the skill writes | A template the skill fills, not prose it pastes into chat. |
| `knowledge/` (vault) | Anything two or more skills read | If a second skill needs it, it moves here and both point at it. |
| `foundation/`, `banks/`, `content/` (vault) | The creator's identity, material, and pieces | Never inside a skill. |

**References hold the method. The vault holds the creator.** This is the line that makes the system shippable. The moment a creator's voice, offer, avatar, or stories live inside `references/`, every install needs the plugin edited, and the next plugin update overwrites their work. Skills carry how to do the work. The vault carries whose work it is.

**Two rules that keep the layers honest:**

- **Source precedence.** Any skill that loads three or more sources that can disagree says which one wins, in one line, where the conflict happens. "If the parable type and the format planner conflict, the planner wins."
- **Empty-file fallback.** Any bank or reference that ships empty on a fresh install carries its own degrade instruction: what to do instead, and to say plainly once that it is empty. A required file that does not exist yet should not stall the skill or get invented around.

---

## What flexes by skill type

The spine holds. These slots change.

| Type | Examples | What it adds or drops |
|---|---|---|
| **Planner / decider** | vid-framing, vid-structure, vid-title, vid-thumbnail | Adds a shapes-at-a-glance table (the options it picks among). Two proposal gates and one confirm is the normal rhythm. Never writes prose. |
| **Writer** | vid-intro, vid-segment, vid-ending | Loads the voice profile and reference pieces. Replaces proposal gates with draft-then-iterate. "Before you present" carries the read-aloud test. Never re-plans; the plan is an input. |
| **Capture** | vid-intake, vid-capture, vid-voice-capture | The workflow is a conversation, not a build. "Before you save" checks fidelity to the creator's own words. Modes, where they exist, go in an inline routing table (behavior that must run every time cannot live in a reference). |
| **Generator** | vid-ideas | Adds the re-roll dial. Output is a set with receipts, not one artifact. Principles carry the anti-fabrication weight. |
| **Audit** | vid-pressure-test, vid-voice-audit | "Output and handoff" becomes "What it reports," plus severity rules. It never fixes what it finds unless asked. |
| **Orchestrator** | vid-pipeline | Drops core principles about craft entirely. A routing table replaces the workflow. Writes no content, ever. It is the only skill that knows the chain. |
| **Setup** | creator-setup, /foundation chain | Additive and re-runnable by design. Says what it will not touch before it touches anything. |

If a new skill fits none of these, that is fine. Keep the spine, name the slot it needs, and add the row here afterward.

---

## The copyable skeleton

```markdown
---
name: skill-name
description: One or two sentences on what it does, then trigger phrases.
---

# Skill Name

One paragraph: what goes in, what comes out, what runs next.

**Scope: {what it does}, never {what it does not}.** {Who owns the rest.}

## Core principles

- **{Rule.}** {The mechanism behind it.}

## What loads, and when

| File | Step | For |
|---|---|---|

Stops: {missing file} points to {skill}.

## The workflow

### 1. {Step name}
### 2. {Step name}
### 3. {Step name}

## Output and handoff

## Before you save

## References for depth
```

---

## House rules that apply everywhere

- No em-dashes. Anywhere, including comments and dev notes.
- Wikilinks for internal references in vault-facing output, never markdown links.
- Ask before scanning. Never load foundation docs, banks, or pieces pre-emptively.
- No fabrication. A gap is named and flagged, never filled with an invention.
- Machinery stays invisible. The creator never hears phase numbers or "loading your foundation."
- Every skill that writes piece.md appends only, and never touches another skill's fields.
- Dev notes go in `WORKING-NOTES.md` inside the skill, marked `ship: false`.
- **Corrections land in the vault, never in the skill.** When the creator corrects voice, a phrase, or a pattern, it belongs in `foundation/voice-profile.md` or a bank, and a winning piece belongs in their reference pieces. Skills ship read-only and the next plugin update overwrites anything written into them, so a correction saved to `references/` is a correction the creator loses. The loop is right; the destination is the vault.

## Reference implementations

`vid-framing` and `vid-structure` run this shape end to end. Read one of them before writing a new skill.
