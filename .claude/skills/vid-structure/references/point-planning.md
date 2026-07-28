---
type: skill-reference
skill: vid-structure
step: 2
last_updated: 2026-07-28
---

# Point Planning

How to order the locked spine, and how to lock each point so the writers never re-plan. Read this at step 2, after the creator locks the spine and before you build anything out.

Two parts: [ordering](#ordering-the-spine) decides which point lands where, [the four locks](#the-four-locks) decides what each point carries.

## Ordering the spine

The title is the biggest setup the video makes, so its full answer lands late, past the midpoint. That is a default with a mechanism, not a commandment: the viewer clicked holding one question, and once the full answer lands, their reason to stay is gone.

**Withhold what the avatar does not already believe.** The point that answers the title, or inverts advice the avatar follows right now, is the payoff. Earlier points deliver pieces: context, mistakes, the mechanism. Each closes a small curiosity while the central one stays open.

**Front-load what the avatar already knows.** A point the avatar gets in one line is recognition, not revelation. Land it fast and move on; stringing out what the viewer already got is what earns "get to the point."

**Let the format set how late "late" is.** News pays off at "why it matters," minutes in. A Short Process pays off at the final step by construction. A Listicle holds the biggest item for last. The locked format's planner carries that arc, and it outranks the default.

**The test after any payoff lands:** does the avatar still want to know something? If yes, keep going. If no, the next point must open a new loop.

### Worked: a listicle reorder

Title: "The 'best practices' quietly killing your channel."

> **Weak order:** 1. "just post consistently" 2. copying thumbnails 3. the 5-second hook 4. overpromising titles.
>
> The named answer lands 90 seconds in. Everything after is bonus footage, and the viewer leaves.
>
> **Locked order:** 1. copying the big channels' thumbnails 2. the "5-second hook" myth 3. titles that overpromise 4. "just post consistently" (title payoff).
>
> Item 4 is the advice the avatar follows right now, so it is the one worth withholding. Items 1 to 3 each close their own small question while "which best practice is killing mine?" stays open to the end.

### Marking the plan

Once the order holds, write down three things. They go to piece.md as `tension_plan`, and the writers read them rather than re-deriving them.

1. **The central question** the viewer is holding from the title.
2. **Which point pays off the title.**
3. **1 or 2 threads:** a setup one point opens and a later one closes. Three or more running at once floods the viewer.

Cross-segment mechanics (handoffs, thread anti-patterns, per-format tension arcs) live in `knowledge/script-tension-architecture.md`. Read it when a piece has an unusual arc; the three items above cover the normal case.

## The four locks

A point is planned when the writer could start typing with zero decisions left.

1. **The parable type**, picked from `knowledge/parable-decision-matrix.md`. The pick, not a shortlist.
2. **The specific material.** The exact bank block (a wikilink) or the exact brain-dump moment it runs on. "A story from the bank" is not a material.
3. **The principle, stated as the lesson itself.** Not "something about ownership": the sentence the viewer could repeat back.
4. **The proof, linked or flagged.** `Proof: [[proof-slug]]` rides the principle line.

### Worked: thin against complete

> **Thin:**
>
> ```
> ## Mistake 3: No owner
> **Parable:** story, a client story about ownership
> **Principle:** assign an owner
> ```
>
> **Complete:**
>
> ```
> ## Mistake 3: No owner assigned to the process
> **Parable:** story. [[story-bank/agency-owner-fired-himself]]: Marcus had a process but no owner, so it defaulted back to him.
> **Principle:** a process with no owner defaults back to you. Assign the owner.
> ```

The thin one leaves the writer three decisions: which story, what it shows, what the lesson says. Every leftover decision becomes a re-interview with the creator, one segment at a time. The complete one leaves only words to write.

### Worked: a gap named, not filled

> ```
> ## Mistake 4: You document it once and never update it
> **Parable:** to build. Needs a quick real example of a stale document causing a miss.
> **Principle:** the document is a living thing; reality changes, the doc follows.
> ```

The banks had no match and the dump had no moment, so the plan names the hole. Filling it with an invented example is fabrication. Flagging it is the job, and the gap also lands as a row in script.md's `## To build`.

### How the locks flex by format

The four locks are the ceiling, not a quota. The locked planner owns the call.

- **Persuasive formats (Listicle, Roast, Interview)** run parable plus principle at every point.
- **Instructional formats (Short Process, Case Study, Deep Dive, News)** run one parable arc up front, then steps. The parable line tracks the arc ("story (continued)") and locks `none` where an earlier section already carried the emotion.

Never force a fresh parable onto a step. A step that already inherited its emotion does not need a new one, and stacking parables on lean steps is what turns a tight process video into a slog.

### Why this bar exists

A writer that has to re-pick a block, re-derive a lesson, or hunt for proof is a boundary bug: the planning leaked downstream. The fix is always here, never in the writer.
