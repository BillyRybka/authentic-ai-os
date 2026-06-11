# Plan · Map Skill-to-Knowledge Dependencies

## Brief
The vault's `knowledge/` folder holds 35+ reference files that skills load at runtime, but there's no record of which skill needs which file. As skills ship to clients, each client should receive only the knowledge files their installed skills actually use, not the whole folder.

## Stack
- Grep / ripgrep for reference extraction across skill files
- Markdown output file living in the vault
- No APIs, no build step, no dependencies

## Scope
- Scan every skill: the 8 shipped skills in `.claude/skills/` AND the WIP skills described in `SYSTEM-MAP.md` (vid-voice-capture, vid-capture, vid-intake, vid-framing, vid-title, vid-thumbnail, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test)
- For shipped skills, extract `knowledge/` references by scanning `SKILL.md` plus `references/`, `assets/`, `scripts/` files
- For WIP skills, extract `knowledge/` references from `SYSTEM-MAP.md` READS lines AND a mandatory prose-scan of any existing skill files
- Treat `SYSTEM-MAP.md` READS lines as a header-level summary only, not the source of truth. SYSTEM-MAP itself notes many `knowledge/` files load conditionally deep in skill bodies, never in header read-lists. The recursive grep plus body-read is what resolves which skill loads which file
- Mark every WIP skill's knowledge deps as "unverified - WIP read-list incomplete" so they are never shipped off blind
- Build a forward map: skill -> list of `knowledge/` files it requires (shipped = verified, WIP = unverified)
- Build a reverse map: knowledge file -> list of skills that consume it
- Classify every unreferenced `knowledge/` file into one of two buckets: genuine orphan (no skill loads it, flag it) or reserved-for-future (a skill is planned but unbuilt, e.g. `thumbnail-composition-guide.md` for `vid-thumbnail-gen`, note it without flagging)
- Flag broken references (a skill points to a `knowledge/` file that does not exist)
- Distinguish vault `knowledge/` files from skill-bundled `references/`/`assets/` files (skill-bundled files ship with the skill automatically and are out of scope for the map)
- Output a single map file with a per-skill packaging checklist (the files to copy into a client's `knowledge/` when that skill ships)

## Out of Scope
- `vid-foundation-workspace/` (dev/eval workspace, not a shipped skill - exclude entirely)
- Editing or moving any knowledge file
- Editing any skill to fix or add references
- Building an automated sync tool or install script
- Mapping bank/template files or `Content/` artifacts
- Deleting orphan files (flag only, no action)

## Constraints
- Read-only on all skill files and knowledge files except the one new map file
- Map file written to `knowledge/skill-knowledge-map.md`
- No em-dashes anywhere in the output
- Every skill folder under `.claude/skills/` except `vid-foundation-workspace/` must appear in the map, even skills with zero knowledge dependencies
- A reference counts only if the path resolves to a real file in `knowledge/`

## Definition of Done
`knowledge/skill-knowledge-map.md` exists and contains a forward map (every shipped and WIP skill listed with its required `knowledge/` files, WIP entries marked unverified), a reverse map (every `knowledge/` file listed with its consuming skills), an orphan list, and a broken-reference list, with every count cross-checked against the actual filesystem.

## Acceptance Criteria
- File `knowledge/skill-knowledge-map.md` exists
- Every skill folder in `.claude/skills/` except `vid-foundation-workspace/` appears in the forward map
- Every WIP skill named in `SYSTEM-MAP.md` appears in the forward map, tagged WIP
- Each forward-map entry lists the exact `knowledge/` filenames that skill references, or states "none"
- Every WIP skill entry is tagged "unverified - WIP read-list incomplete"
- The reverse map lists every file currently in `knowledge/` at least once (consumed or marked orphan)
- Orphan section lists every `knowledge/` file referenced by zero skills, split into genuine orphans vs reserved-for-future
- If zero genuine orphans are found, the section states so explicitly (this confirms or corrects SYSTEM-MAP's "all files wired" claim)
- Broken-reference section lists every skill reference pointing to a non-existent `knowledge/` file (or states "none found")
- Each skill entry includes a copy-ready packaging checklist of files to bundle when that skill ships
- No `knowledge/` file appears in both the consumed reverse map and the orphan list
- No em-dashes in the file

## Verification
1. `ls knowledge/` and count files (and recurse `format-planners/`); this is the universe the reverse map must cover.
2. For each shipped skill folder, `grep -rn "knowledge/" .claude/skills/{skill}/` to extract every reference.
3. For WIP skills, extract `knowledge/` references from `SYSTEM-MAP.md` READS lines, then read each WIP skill's prose for loose references not caught by path-grep.
4. For each extracted path, confirm the target exists with `ls knowledge/{path}`; mismatches go to the broken-reference list.
5. Diff the set of all referenced files against the `ls knowledge/` universe; files in the universe but not referenced are orphans.
6. Confirm every shipped skill folder (minus `vid-foundation-workspace`) and every WIP skill name from `SYSTEM-MAP.md` appears as a heading in the map file.
7. `grep -cP '\x{2014}' knowledge/skill-knowledge-map.md` returns 0 (scans for the em-dash character U+2014).

## References
- `.claude/skills/` - 9 skill folders (8 shipped, 1 workspace)
- `knowledge/` - 35 files plus `format-planners/` subfolder
- `SYSTEM-MAP.md` at vault root - existing untracked system map, check for overlap before writing

## Risks / Open Questions
- SYSTEM-MAP.md READS lines are header-level only. Many `knowledge/` files load conditionally deep in skill bodies. Trust the recursive grep plus body-read, not the READS summary.
- WIP knowledge deps are best-effort and tagged unverified; do not ship a WIP skill off this map without re-checking when it goes live.
- WIP skills may not have full skill files yet; their only source may be the SYSTEM-MAP READS line. Where that is the sole source, note it explicitly.
- `format-planners/` is a subfolder; decide whether to map individual planner files or the folder as one unit.
