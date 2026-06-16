---
type: lessons
project: authentic-ai-os
date: 2026-06-05
status: living
last_updated: 2026-06-05
tags: [skill-wiring, schema-design, verification]
---

# Skill-wiring lessons

A living document. Add patterns as they earn their place by surviving real edits.

This system is warfarin. A small change to wiring or schema, a big downstream consequence. Slow down. Verify.

## The 8 patterns from the vid-research 4-to-3 bank cleanup (2026-06-05)

### 1. Routing is a real bug class

`vid-title` was supposed to load `power-words-bank` but never did. The bank existed. The skill's description said it would. The actual Load section in the SKILL.md did not include the file. Data was being collected for a consumer that never queried it. Invisible failure.

**Verification:** grep the SKILL.md Load section for every bank you expect it to read. If it is not there, the wiring is broken regardless of what the description claims.

### 2. Every field needs a named consumer

For every field on a row, ask: what downstream skill queries this, and how? If there is no concrete answer, the field is bloat. If there is one, the field stays.

The adversarial agent caught me cutting two fields (`view_count`, `hero_element`) that DID have consumers I had missed. The opposite is also true. Keeping unused fields because they "might be useful later" piles bloat.

**Verification:** trace every field to a specific Load + use site, or drop it.

### 3. File count vs row count are different bloat problems

Three banks slicing the same outliers is artificial complexity. But one giant bank is not always better. Separate files earn their keep when consumers load them at different times.

**Heuristic:** separate files when access patterns differ. Merge files when the same skill reads both for the same job.

### 4. Source-fidelity is not absolute. Medium matters.

Ed teaches one holistic bank because he uses a spreadsheet. Markdown is not a spreadsheet. The medium changes what structure is correct.

**Verification:** when adapting an external method, ask what FORMAT the source operates in. Translate the principle, not the literal layout.

### 5. Adversarial check before locking design

Three parallel agents (schema map, consumer-flow map, adversarial-break) caught two real cuts before they happened. The "would this actually work?" check is cheap.

**Pattern:** for any non-trivial scope change, run an adversarial pass that tries to BREAK the simplification. If it finds nothing, ship. If it finds something, adjust.

### 6. Solve the AI-bias problem at the field level, not the cut level

Showing absolute `view_count` biases the AI toward MrBeast-tier examples. The wrong fix is "remove view_count." The right fix is "add `outlier_multiplier`, tell the AI to rank by multiplier, keep view_count for citation only."

**Pattern:** when a field would bias the AI, add a co-field that captures the real signal, then specify which to rank on.

### 7. Wikilinks beat duplication

When the same outlier appeared as a worked example in three banks, we had three copies of the same data. Pattern-bank now holds it once. Title-bank and power-words-bank wikilink back.

**Pattern:** one source of truth per fact. Cross-reference, do not copy.

### 8. The grep is the verification

I caught my own mistakes today by grepping for stale references after every edit. If the build-plan still says "4 banks" after I cut to 3, the system is documentation-inconsistent and the next session re-discovers everything.

**Verification:** after every scope change, grep the WHOLE repo for the old names. Update or delete every hit.

## The thread through all eight

Prove the wiring works with actual file reads and grep, not with description text or intent. Skill descriptions lie sometimes. Code (the Load section, the grep results, the file contents) does not.

## Verification checklist for any non-trivial skill or bank change

Run this before considering the change done.

- [ ] Every produced field maps to a specific Load site in a specific SKILL.md
- [ ] Every Load site that should read a file actually has that file listed in its Load section (grep, not memory)
- [ ] Adversarial pass attempted to break the new design and failed
- [ ] Cross-bank references use wikilinks, not duplicated rows
- [ ] No field pre-stores data that is better collected on-demand at gen-time
- [ ] No field would bias AI toward a wrong dimension without a co-field to rank on
- [ ] Repo-wide grep for old names returns zero unresolved hits (historical work-log mentions allowed)
- [ ] Em-dash sweep on all touched files returns zero
- [ ] Mental dry-run: trace the data flow from research output through every per-video write step it should hit

## Where this gets applied first

The immediate next test is the **vid-pipeline orchestrator** (slash command, not a skill). Every load decision, every state hand-off, every input/output contract between writing skills should pass through these patterns before going in.

If the orchestrator is a single command, it has one Load section but many sub-invocations. Each sub-invocation is itself a wiring decision. Apply the eight patterns to each.

## Future entries

Add new lessons here as scope changes earn them. Date-stamp each batch with a short context line.
