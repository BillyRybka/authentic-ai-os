# Plan · Audit and Re-map the Skill-Knowledge Map and System Map

## Brief
Both `documents/skill-knowledge-map.md` and `documents/SYSTEM-MAP.md` have drifted from the repo: ~14 untracked knowledge files, a whole `aud-*` skill family and other WIP skills in neither map, a mislabeled tier on `vid-research`, and renamed reference files now living in `knowledge/`. Rebuild both docs from a fresh full-disk audit so they reflect all 28 skills, three packaging tiers, and every knowledge dependency accurately.

## Stack
- Grep / ripgrep for reference extraction across all skill roots
- Directory listings of the three skill roots and `knowledge/`
- Markdown output, Obsidian-flavored (mermaid pipeline diagram, callouts) matching the existing docs
- No paid APIs, no build step

## Scope
- Grep every `SKILL.md`, `references/*.md`, and `assets/*.md` across all three skill roots: `plugins/authentic-ai-os/skills/`, `.claude/skills/`, `.claude/skills-wip/`
- Cross-check every referenced `knowledge/` path (and the `common-english.txt` word list) against what exists on disk
- Rebuild `skill-knowledge-map.md`: forward map, reverse map, orphan list, broken-reference list, per-skill packaging checklist, maintenance note. Cover all 28 skills under three tiers
- Rebuild `SYSTEM-MAP.md`: a card per skill (READS / WRITES / NEXT / STATUS verified against each SKILL.md), the mermaid pipeline, the reused-files table, and the audit-findings section, all using three-tier vocabulary
- Classify every currently-untracked knowledge file: the feedback trio (`feedback-submit`, `feedback-capture-map`, `feedback-offer`), `update-check.md`, the `*-bank-schema.md` set, `hook-bank-template.md`, `transition-bank-template.md`, `iceberg-and-top-3-alignment.md`, `theory-of-one-curation.md`, `ai-hedging.md`, `synthetic-audience-method.md`, `common-english.txt`. Mark each as a read-time dependency, a write-target template, or an orphan, and name the consuming skill
- Account for the renamed reference files now resolved into `knowledge/` (iceberg-and-top-3-alignment, theory-of-one-curation)
- Record every defect found (broken reference, orphan, stale NEXT chain) inside the two map docs. Do not edit any skill or knowledge file

## Out of Scope
- Editing, fixing, or refactoring any `SKILL.md`, `references/`, `assets/`, or `knowledge/` file. This run is document-only
- Building the missing `vid-pipeline` orchestrator or authoring any new skill
- Authoring the planned `hook-bank` / `transition-bank` content, or rewriting any knowledge file body
- Voice, quality, or prose review of skill content
- Touching `banks/`, `content/`, `foundation/`, or any creator data file

## Constraints
- Exactly two files change on disk: `documents/skill-knowledge-map.md` and `documents/SYSTEM-MAP.md`
- Every reference, tier tag, and READS/WRITES/NEXT claim is grep-verified against disk. Zero fabricated entries
- Three-tier vocabulary used consistently in both docs: Released (`plugins/authentic-ai-os/skills/`), Staged (`.claude/skills/`), WIP (`.claude/skills-wip/`)
- Both docs carry a fresh provenance line dated 2026-06-16 and a regeneration recipe that names all three skill roots
- Markdown style matches each existing doc (mermaid, tables, callouts preserved)
- No em-dashes anywhere in either doc

## Definition of Done
A fresh grep of all skill references plus a directory listing of `knowledge/` and the three skill roots reconciles exactly with both rebuilt docs: every skill on disk appears with its correct tier, every knowledge dependency is listed against its consumer, and neither doc references a skill folder or knowledge file that does not exist on disk.

## Acceptance Criteria
- All 28 skills (8 Released, 3 Staged, 17 WIP) appear in both docs tagged with the correct tier; `vid-research` reads as Staged, not Shipped
- Forward map lists, per skill, exactly the `knowledge/` files that skill references (grep-verified, including transitive `via references/` and `via assets/` cases)
- Reverse map: every `knowledge/` file and `common-english.txt` on disk appears with its consumer list, or in the orphan section if it has none
- Every knowledge file referenced by a skill exists on disk; any that does not is listed in the broken-reference section with its referencing skill
- Each previously-untracked knowledge file is classified (read dependency / write-target template / orphan) with the consuming skill named
- SYSTEM-MAP card READS / WRITES / NEXT / STATUS match each skill's actual SKILL.md for all 28 skills
- The "no vid-pipeline orchestrator" finding and every other narrative claim is re-verified against disk and updated to current truth
- Both docs state build date 2026-06-16 and a regeneration recipe covering all three skill roots plus the `update-check.md` pre-flight
- Zero references in either doc to a skill folder or knowledge file absent from disk (the documented `knowledge/X.md` placeholder excepted)
- Zero `—` characters in either doc

## Verification
- Extract on-disk reference set: grep `knowledge/[A-Za-z0-9/_-]+\.(md|txt)` across the three skill roots, sort unique. Strip the `knowledge/X.md` documentation placeholder
- Build the disk sets: list the three skill roots for the skill set; list `knowledge/` plus `knowledge/format-planners/` for the knowledge-file set
- Reconcile: diff the disk reference set and skill set against the entries parsed from each rebuilt doc. The check passes only when the symmetric difference is empty on both sides (no phantom entries in the docs, no on-disk items missing from the docs)
- Em-dash gate: grep both docs for `—`, must return zero
- Spot-check: pick 3 skills across different tiers and confirm their SYSTEM-MAP card READS list matches their SKILL.md header

## Turn Budget
Stop after 40 turns, or sooner once the reconciliation check passes clean and the em-dash gate returns zero.

## References
- `documents/skill-knowledge-map.md` (staleness note flagged at lines 273-274)
- `documents/SYSTEM-MAP.md` (audit-findings section, lines 219-234)
- `CLAUDE.md` packaging rules and folder structure
- `knowledge/vault-integration.md` (frontmatter and wikilink contract)

## Risks / Open Questions
- Classification of schema and template files: `*-bank-schema.md`, `hook-bank-template.md`, `transition-bank-template.md` are read by skills to know an output shape, so they still must ship even though they are not "content" dependencies. The map's purpose is packaging (what must travel with the skill), so they belong in the forward map, flagged as template dependencies
- `common-english.txt` is a `.txt` word list, not markdown. Confirm its consumer (likely `vid-research` power-words work) and list it; do not let the `.md`-only grep silently drop it
- The `aud-*` family is experimental and may reference knowledge files that do not exist yet. Those go in the broken-reference section, not fixed
- Released-vs-Staged packaging: confirm `feedback-offer` and the feedback trio actually ship from `plugins/`, since `foundation` (Released) references `feedback-offer`
