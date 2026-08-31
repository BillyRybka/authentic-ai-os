---
type: reference
skill: vid-pressure-test
reviewer: source-traceability
tags: [reviewer-rubric, traceability]
---

# Source-Traceability Reviewer Rubric

This reviewer runs in Phase 2 as a fresh-context Task spawn. Its single job: every claim, number, name, story, metaphor, framework, statistic, and quoted phrase in the script must trace to brain-dump.md, foundation docs, or banks. Untraceable = flag.

## What to scan

Walk script.md line by line and extract every:

1. **Number**: dollar figures, percentages, timeframes, counts, dates, ratios
2. **Named person**: clients, students, public figures, family, "Steve" / "Sarah" / etc.
3. **Story moment**: a specific scene, event, or anecdote
4. **Metaphor**: analogy, comparison
5. **Framework or named system**: "The 90-Minute Rule", "BENS", "Three-Circle Research"
6. **Statistic or external claim**: "47% of CEOs", "research shows", "studies say"
7. **Quoted phrase**: anything in quotation marks attributed to someone

For each, look for a source.

## Source-checking order

1. brain-dump.md (creator's own raw material for this piece)
2. foundation/avatar.md (avatar, Top 3) and foundation/credibility.md (the three proof points)
3. foundation/voice-profile.md (recurring phrases section)
4. banks/story-bank/*.md
5. banks/proof-bank/*.md
6. banks/metaphor-bank/*.md
7. banks/testimonial-bank/*.md
8. banks/framework-bank/*.md

If none of those cover it, flag.

## Severity tiers

**Hard issue (factual break):**

- Fabricated number ("47% of CEOs") with no source anywhere
- Named person who appears nowhere in foundation or banks
- Claimed result ("we got 200 clients") with no proof entry
- Statistic attributed to a study with no source

**Soft issue (worth flagging):**

- Round number that might be approximate (creator may have approximated a real figure)
- Story moment that paraphrases a real story but adds detail not in the source
- Metaphor that recurs but isn't formally in metaphor-bank yet

## Returning the top 3

Rank by severity. Pure fabrications first. Then named-claim mismatches. Then quoted phrases without provenance.

Each issue surfaces with:

```
Reviewer: source-traceability
Location: {section} line {N}
Quote: "{exact text from script.md}"
Issue: {one-sentence diagnosis}
Suggested fix: {specific replacement OR "drop the claim" OR "verify before filming"}
```

## Worked examples

### Example 1: pure fabrication (HARD)

Script line: "47% of CEOs say they struggle with this exact problem."

brain-dump.md has no source for "47%". foundation has no stat. No banks reference 47%. Verdict: fabricated.

```
Location: Segment 2 line 3
Quote: "47% of CEOs say they struggle with this exact problem."
Issue: The number 47% is not in brain-dump, foundation, or any bank. Likely fabricated.
Suggested fix: Drop the number. Rewrite as "most of my coaching clients struggle with this" (which traces to foundation/credibility.md: "200+ clients coached").
```

### Example 2: real claim, vague source (SOFT)

Script line: "Studies show curiosity drives retention."

brain-dump.md mentions creator read this somewhere but didn't cite. Not in banks.

```
Location: Segment 4 line 7
Quote: "Studies show curiosity drives retention."
Issue: "Studies show" is unsupported. Either cite the study (if real) or convert to creator's own observation.
Suggested fix: Rewrite as "from watching my own retention curves, curiosity is what holds the viewer" (frames as creator experience, no false attribution).
```

### Example 3: named client without proof entry (HARD)

Script line: "Steve went from $0 to $80k/month in 9 weeks."

brain-dump.md has Steve mentioned. story-bank has no Steve entry. proof-bank has no $80k Steve screenshot.

```
Location: Intro line 4
Quote: "Steve went from $0 to $80k/month in 9 weeks."
Issue: Steve is named in brain-dump but his result has no proof entry. The number is unverifiable.
Suggested fix: Verify the number with the source (your records on Steve), capture a proof entry via vid-bank, then re-include. OR rewrite as "one of my coaching clients went from zero to a strong monthly recurring number" until proof lands.
```

### Example 4: paraphrased story (SOFT)

Script line: "My wife was pregnant, I had just lost my job, and my business was making zero."

story-bank has a "founding moment" entry that matches but says "my business was making minimal revenue." Script tightened to "zero" for impact.

```
Location: Intro line 8
Quote: "...my business was making zero."
Issue: story-bank entry says "minimal revenue." Script tightens to "zero" for impact, which may be inaccurate.
Suggested fix: Either restore "minimal" to match the bank, or update the bank to reflect "zero" if that is the truthful version. Pick one.
```

## What this reviewer does NOT catch

- Voice or stylistic problems (voice-authenticity reviewer)
- Banned phrases (AI-slop reviewer)
- Retention or structure issues (retention-logic reviewer)

Stay focused on traceability only.

