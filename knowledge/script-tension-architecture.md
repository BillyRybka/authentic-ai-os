---
name: Script Tension Architecture
type: shared-knowledge
loaded_by: vid-structure, vid-segment, vid-pressure-test (future)
last_updated: 2026-05-13
---

# Script Tension Architecture

How tension rises, falls, and connects across the WHOLE script, not just within one segment.

This file is the cross-segment complement to `references/parable-principle-shapes.md` inside vid-segment. That file owns the parable + principle of a single segment (the content). This file owns the tension arc across all segments: how segment 1 sets something up that segment 4 pays off, why early payoff kills retention, how each segment hands tension to the next without letting it sag, and how the title's promise stays unresolved until the moment it lands.

Every skill that makes a structural decision about the script as a whole loads this. vid-structure plans the cross-segment arc. vid-segment reads it to understand where the current segment sits in the larger tension graph. vid-pressure-test audits for retention risk.

## Two separate layers (the split)

A script runs two separate things at once. Keep them apart.

**Per-segment content (lives in vid-segment).** Inside one segment: a parable (the show, the emotion brick) then a principle (the tell, the logic brick), each segment teaching one thing. How often the two bricks repeat is the format's call, and the planner owns it: persuasive formats (List Video, Review, Interview) run parable + principle at every point; instructional formats (Step-by-Step, Success Story, Deep Dive, News) run one parable arc up front, then steps. Either way this is NOT a Setup/Tension/Payoff skeleton; it is the content layer. See `references/parable-principle-shapes.md`.

**Cross-segment tension (this file).** Across all segments: the title makes a promise, the intro raises the central question, segments deliver pieces of the answer in an order that withholds the BIG payoff until the moment of maximum tension, and the ending pivots to the next problem. Setups and payoffs live HERE, not inside a segment. The intro is one big setup; transitions are little setups; the points pay off curiosity one by one. The viewer stays through 5+ minutes because the central promise hasn't fully paid off yet.

A script with strong parable + principle per segment but flat cross-segment tension feels like a series of disconnected lessons. The viewer learns, but they don't binge. Strong cross-segment tension but weak parable + principle feels exciting but empty. The viewer binges, but they don't learn.

Both run at once, planned and checked at different moments. vid-structure plans the cross-segment shape (title-promise location, threads, handoffs). vid-segment delivers the parable + principle. vid-pressure-test audits the cross-segment tension after the script is assembled.

## The script-level tension graph

Every video runs on one central question, the question the title and thumbnail implicitly raise.

**Example:** title is "How I Added 50 Pounds To My Squat In 12 Weeks." The central question is "how did you do that?" Everything in the script either raises that question (raises tension) or partially answers it (raises curiosity AND releases some tension at the same time). The full answer (the complete method) only lands at the moment of maximum tension, late in the body after earlier segments deliver pieces.

The tension graph isn't flat. It rises through the intro, peaks somewhere in the middle, dips briefly as each segment delivers a partial payoff, rises again toward the big payoff, then falls into the ending pivot.

```
  ^
  |               *  <- big payoff (the full method)
  |          *   * 
  |       * *   *
  |      *     
  |    *  <- mid-script peak
  |   *
  |  *
  | *  <- intro question raises tension
  | *
  +-------------------------> time
   Intro  S1  S2  S3  S4  S5  End
```

**The job:** the script must stay above zero tension at every moment. As soon as the viewer's tension drops to zero (every question they had got answered), they leave. The viewer stays because something they want to know is still hanging.

## Three load-bearing tactics

These are the tactics vid-structure plans for and vid-segment executes against.

### 1. Title-promise lock

The promise the title makes does NOT get fully paid off until the moment of maximum tension. Early-payoff kills retention.

**The mechanic.** When a viewer clicks a thumbnail/title that promises X, they're holding tension until X lands. If the full answer to X arrives in segment 1, the remaining segments have nothing to hold the viewer. They leave. The classic failure signal is the viewer comment "get to the point." Tension already gone.

**The fix.** Identify what the title promises. Push the full payoff LATE in the body (past midpoint), not early. Earlier segments deliver pieces of the answer, context, or related insights, but never the complete picture. Where exactly "late" lands depends on format (see format-specific arcs below) and brain-dump volume.

**Worked example.** Title: "Why 80% Of YouTube Channels Stall At 1k Subs." Central promise: the reason channels stall. Early segments deliver context (the algorithm dynamics, common mistakes, why people give up), each adding a piece. The full reason, the named insight, drops in segment 4 of 5. Segment 5 is the "what to do about it" application.

**Near-miss.** Same title, but segment 1 opens with "Here's the reason: they're posting too consistently and the algorithm punishes them." Viewer learned the answer in 90 seconds. They leave. Tension graph just hit zero.

**Anti-pattern flag.** Watch for "Here's why X" or "The answer is Y" in early segments. That's the early-payoff signal. Refactor to push the named answer later. Use bread-crumb language ("part of the reason is...", "we'll come back to this", "but the real driver is something else") to keep tension up.

### 2. Setup-payoff threading across segments

A segment can open an "open loop" that another segment closes. This is what makes a script feel woven instead of stacked.

**The mechanic.** Segment 1 introduces a concept, name, character, or claim without fully explaining it. Segment 3 references it again, deepens it. Segment 5 resolves it. The viewer's brain marks the open loop and stays alert for the resolution.

**Examples of threads:**
- A character introduced in segment 1 ("Steve was making $0 a month, married, baby on the way...") whose outcome lands in segment 4 ("by month nine, Steve was hitting $80k...")
- A claim made in segment 1 ("most people get this wrong, but I'll show you why in a moment") that pays off in segment 3
- A counterintuitive insight teased in the intro ("there's one thing every successful channel does that none of the gurus teach") and named in segment 4
- A specific number raised in segment 2 ("this 23-minute window matters more than you'd think") and explained in segment 5

**How vid-structure plans threads.** When proposing the cross-segment skeleton, identify at least ONE open loop running across the body. Mark it explicitly in the segment purposes: "Segment 1 opens the Steve thread; Segment 4 pays it off." vid-segment then knows to leave the thread open in segment 1's prose and close it in segment 4.

**Anti-pattern: stacked lessons.** A script with five disconnected segments (each a complete lesson) reads as flat. The viewer learns each thing but feels no pull. A thread is the usual fix; a format that carries its own pull (news urgency, a list video's ranking) can decline one deliberately.

**Anti-pattern: too many open loops.** Loops are open promises. The more open at once, the easier it is for the viewer to lose track of any single one, and the harder for the creator to honor every payoff. Most scripts stay clearest with 1-2 prominent loops. More is doable but requires deliberate tracking and faster resolution. Test what your audience can follow.

### 3. Tension reset between segments (handoff)

Every segment ends. The moment a segment ends, tension drops slightly (the payoff just landed). The next segment must lift it back up before the viewer disengages.

**The mechanic.** Outbound transition + inbound setup do the lift together. The outbound transition (last sentence of segment N) forward-hooks into segment N+1 by raising a new question, naming what's coming, or opening a small gap. The inbound setup (first sentence of segment N+1) lands the hook and immediately raises new tension.

**Worked handoff.**
- Segment 2 ends: "...and that's the second mistake. But the third one is the one I see most often, and it's the one nobody warns you about."
- Segment 3 opens: "The third mistake is the one I made for two years before someone called me out on it. Here's what it looks like..."

The viewer never gets a moment where they could decide to leave. The transition forward-hooks into a new gap, the new setup raises a new question, and they're inside the next segment before they realized they had a chance to bounce.

**Anti-pattern: closed payoff at segment end.** "...so that's how you fix the second mistake. Moving on." Tension drops to near-zero. The next segment has to lift from cold start. Some viewers leave during the drop.

**Anti-pattern: open loop dropped silently.** Segment 2 ends with "...we'll come back to this." Segment 3 never references it. Viewer's brain flags the broken promise. Trust erodes.

vid-segment owns the outbound transition. vid-structure owns the verification that handoffs work across the full sequence.

## Format-specific tension arcs

The segment shapes themselves live in `knowledge/format-planners/{format}.md`, the single per-format authority. This section keeps only the tension layer on top: where the title promise lands and how many threads stay active per format.

| Format | Title-promise location | Active threads |
|---|---|---|
| Success Story | The outcome moment, after the obstacles. The lesson and steps are application, not the payoff. | 1: the protagonist's transformation, opened in the intro, closed at the outcome |
| List Video | The final item, or the item that delivers the title's core promise. The list builds toward it; never pay it off at the open. | 1 positional ("which one is the best?"), plus optional sub-threads across items |
| Step-by-Step | Between the last step and the close: "you now have the complete system." | 1: the viewer's growing capability |
| Deep Dive | The synthesis lesson, usually the last big idea, where everything connects. | Concept threads that deepen across lessons; each lesson opens a question, pays it off, and raises the next one higher |
| News | The "why it matters" moment. News compresses everything; the named answer cannot wait as long as elsewhere. | 1 max |
| Review | The promised lesson at the end of the review pattern, or the most egregious subject's reveal for entertainment titles. | 1: the pattern emerging across subjects |
| Interview | The question whose answer delivers the title's promise, usually 2/3 through the conversation. | 1: the through-line the host weaves |

Guests sometimes introduce their own thread (a story they keep returning to). Let it play.

## Anti-patterns (the failure modes)

**Early payoff.** The full title promise gets answered in segment 1 or 2. Tension graph hits zero. Viewer leaves. Refactor by pushing the named answer later and replacing early-segment payoffs with partial pieces.

**Broken thread.** A segment opens a loop ("I'll explain that in a moment") and no later segment closes it. Viewer's brain flags it. Audit by listing every "we'll come back to this" and verifying each one resolves.

**Stacked lessons (no threads).** Five segments, five disconnected lessons, no thread connecting them. Reads as flat. The viewer learns but doesn't binge. A thread spanning 3+ segments is the usual fix, unless the format deliberately declined one.

**Cold handoffs.** Segments end on closed payoffs ("...so that's the fix. Moving on."). Tension drops at each boundary. Some viewers leave at every drop. Forward-hook every outbound transition.

**Tension overload.** Three or more open loops running at once. Viewer can't track them. Working memory floods. Reduce to 1-2 active threads.

**Promise drift.** The title promises X but the body delivers Y. Even if Y is good, the viewer feels deceived. The tension never resolves because what they came for never landed. Audit the title's central question and confirm every segment serves it (or open a thread back to it).

**Cliffhanger-as-content.** Open loop after open loop with no resolution. Feels like a tease, not a payoff. The viewer leaves frustrated, doesn't subscribe. Loops must close.

## How vid-structure uses this

At outline time, before writing the skeleton, vid-structure plans the tension graph:

1. **Identify the title's central question.** What is the viewer holding tension on? Write it down.
2. **Locate the title-promise payoff.** Which segment delivers the named answer? Place it where the format table puts it, and record it as `title_promise_segment`.
3. **Plan threads (when the format wants one).** Pick 1-2 threads to run across the body, or none when the format carries tension without them. When a thread exists, mark the exact section labels that open and close it.
4. **Verify handoffs.** For each segment boundary, confirm the outbound transition can forward-hook into the next segment's setup.
5. **Surface to creator.** Show the tension graph as part of the skeleton proposal. "Title promise lands in segment 4. One thread: Steve's transformation, opens segment 1, closes segment 4. Handoffs forward-hook on retention-mistake question between 2 and 3." Creator confirms or adjusts.

The tension plan is recorded once, in piece.md (`tension_plan:` block). script.md does not carry a duplicate copy; downstream skills read the block.

## How vid-segment uses this

When writing one segment, vid-segment loads this file to understand context the segment can't see from inside itself:

- **Is this segment the title-promise payoff?** If yes, write the payoff to fully land. If no, write the segment to deliver its piece without resolving the central question.
- **Does this segment open or close a thread?** If opens, plant the seed prominently. If closes, deliver the resolution with weight.
- **Outbound transition.** Forward-hook into the next segment's setup, not into the ending.

The per-segment parable + principle shapes are in `references/parable-principle-shapes.md`. This file just tells vid-segment where the current segment sits in the larger arc.

## How vid-pressure-test uses this

Adversarial retention review. The pressure-test agent reads the full script against this file's anti-patterns:

- Early-payoff check: does the title's promise resolve before the segment `tension_plan` assigned it? When the plan is absent, fall back to the format table's payoff location.
- Broken-thread check: every "we'll come back to this" or open loop. Does it close?
- Cold-handoff check: every segment-end. Does it forward-hook?
- Overload check: are 3+ threads active at once?
- Promise-drift check: does every segment serve the title's central question?

Findings get surfaced as ranked issues in pressure-test.md.

## Principles

- **Tension and curiosity are the fuel.** Information without tension doesn't retain. Most "boring videos" have good information but no curiosity arc.
- **Two separate layers.** Parable + principle per segment at vid-segment (how often they repeat is the format's call). Cross-segment tension planned at vid-structure and audited at vid-pressure-test. Both matter.
- **Title-promise resolves where the format builds to it.** The named answer to the central question lands at the payoff point the format table assigns, never before the video has earned it. Early-payoff is the most common failure.
- **Threads make scripts feel woven.** One open loop running across the body is the difference between "five lessons stacked" and "one experience."
- **Every handoff forward-hooks.** Segment ends with a question, name, or gap that lifts into the next segment's setup. No closed-payoff endings except the very last.
- **Loops must close.** Every open loop the script raises must resolve. Broken promises destroy trust.
