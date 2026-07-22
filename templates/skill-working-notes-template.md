---
type: dev-notes
status: in-progress
skill: {skill-name}
captured: YYYY-MM-DD
---

# Skill Working Notes

This file lives inside a writing skill's folder during development (e.g., `skills/{skill-name}/working-notes.md`). It records source citations for every claim, example, and anti-pattern in the productized skill files. The skill lead deletes this file before productization. The Phase 3 QA agent uses it to verify the source-backing trace from each productized claim back to its underlying source.

Fill in entries as you build. Every rule, pattern, example, and anti-pattern in `SKILL.md` or any `knowledge/*.md` or `banks/*.md` the skill ships needs an entry here.

---

## Source citations

Every rule or pattern in the productized skill files. One bullet block per claim.

- **Claim:** [the rule/pattern/example as it appears in the productized skill]
- **Source:** [absolute path to source file]
- **Lines:** [line range, e.g. 1849-1860]
- **Notes:** [brief context, why this source backs this claim, paraphrase vs. direct, any adaptation made]

- **Claim:**
- **Source:**
- **Lines:**
- **Notes:**

- **Claim:**
- **Source:**
- **Lines:**
- **Notes:**

---

## Examples sourced from

Every worked example in the productized skill. One bullet block per example. Adaptations into representative niches (e.g. fitness, copywriting, agency) are fine, just note the original and the niche substitution.

- **Example:** [the example string as productized]
- **Source:** [absolute path to source file]
- **Lines:** [line range]
- **Notes:** [direct quote vs. paraphrase, niche substitution if any]

- **Example:**
- **Source:**
- **Lines:**
- **Notes:**

- **Example:**
- **Source:**
- **Lines:**
- **Notes:**

---

## Anti-patterns sourced from

Every anti-pattern (banned phrase, failure mode, common mistake) in the productized skill. One bullet block per anti-pattern. Include the failure-mechanism explanation if it traces to a specific source line.

- **Anti-pattern:** [the anti-pattern as productized]
- **Source:** [absolute path to source file, or "live observation" if captured from project memory or feedback]
- **Lines:** [line range, or N/A for live observation]
- **Notes:** [why it fails, where the failure mechanism was confirmed]

- **Anti-pattern:**
- **Source:**
- **Lines:**
- **Notes:**

- **Anti-pattern:**
- **Source:**
- **Lines:**
- **Notes:**

---

## Cross-skill dependencies confirmed

Free-text list of coordination points with other team builders. One line per confirmed dependency. Date the confirmation. Use this when another skill's contract (a schema field, a pattern slug, a banned-phrase list) had to match this skill's contract.

- vid-intro confirmed canonical 5 hook types match vid-segment usage on YYYY-MM-DD
- vid-ending confirmed its 3-Part End Formula against the patterns in knowledge/transition-patterns.md on YYYY-MM-DD (the creator's transition bank holds proven rows, not the pattern library)
- voice-profile-schema field `preferred_hook_types` accepts the 5 hook types defined in .claude/skills/vid-intro/references/hook-patterns.md, confirmed YYYY-MM-DD (the creator's hook bank holds proven rows, no fixed type slugs live there)

---

Delete this file when the skill is finalized.
