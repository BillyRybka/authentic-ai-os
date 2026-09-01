# Version 2 Plans (deferred)

What we deliberately left out of v1 to keep the skills simple. Nothing here is abandoned. Each entry is a real feature we want, parked until the v1 core is solid. When you build one, delete it from here and fold it into the skill.

## vid-intake: the "start from someone else's content" route

**Status:** deferred. v1 intake captures the creator's own material only, whether they talk it through or paste their own notes or transcript.

**What it is**

A second way into intake. The creator starts from a piece of content they did not make (a competitor's video, an article, a podcast) and uses it as a springboard for their own video. This is normal and fine. The point is not to copy it. The point is to start from it and build the creator's own, stronger take. The finished video still has to stand as the creator's own teaching, not read as a reaction to the source.

**The flow Billy wants**

1. The creator pastes the source. Pasting is the natural way in. They will not brain dump someone else's content, they will hand you the transcript.
2. Intake captures the full transcript.
3. Intake reflects it back as structured bullets: each main point the source made, a line on what they said about it, and a short summary per point. An overview the creator can actually see and react to.
4. From there the creator riffs. They talk through each point, agree, push back, add their own angle. That riff is the real material intake captures.
5. The brain dump ends up as the creator's own take, anchored by the source's structure but not bound to it.

**Why it is deferred**

It adds a genuine branch the core loop does not need yet: ingesting an external source, the structured bullet reflect-back, and capturing the riff as a second pass. v1 proves the core capture loop on the creator's own material first. Build this once that is solid.

**Where it plugs into v1 when we build it**

Add a second entry to vid-intake alongside "your own material": "start from something you saw." It runs paste the source, capture the transcript, reflect it back as bulleted main points, then the riff. The one spine picks up from there (reflect, deeper pass, fit, save). Restore the removed `inspired-by` value to the `intake_mode` enum, and bring back a place in brain-dump.md to hold the source's points separate from the creator's take (the old `## Source notes` section).

## vid-research: the scheduled competitor refresh

**Status:** deferred. Mode 2 (quarterly refresh) already does the work; what is missing is an automatic trigger and a digest.

**What it is**

A recurring job, most likely a scheduled task in Claude Cowork, that keeps the outlier bank current instead of frozen at the last manual run. It runs Mode 2 unattended: pull the confirmed channel set, fetch only videos published since `last_refresh`, dedup against existing notes by `video_id`, write notes plus full workups for anything new that clears its floor, and recompute every channel's median, floor, and every multiplier.

**Why it matters**

The research window is 12 months but the bank is a snapshot. On the first real build, only 9 of 143 outliers were published in the last 90 days. Without a refresh the creator plans against what worked last year.

**The rule that makes it safe**

It recomputes and reports; it never silently deletes. A channel's median rises as it grows, so a video banked at 8x can read 5x next quarter and fall under its floor. That is real signal, not an error. The job surfaces it (new outliers added, multipliers that moved, notes now under the floor) and leaves the decision to the creator. A scheduled job that quietly rewrites the bank is worse than no job.

**What to build**

The trigger and the digest, not the research. Decide where "what changed" lands (a dated note, or an append to pattern-bank), and decide whether thumbnails for videos that dropped out get pruned or archived (see the Mode 2 archive rule already in the skill).
