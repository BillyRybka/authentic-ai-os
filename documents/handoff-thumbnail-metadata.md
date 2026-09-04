---
type: handoff
doc: handoff-thumbnail-metadata
project: authentic-ai-os
status: active
date: 2026-09-04
tags: [handoff, vid-research, outliers, metadata]
---

# Handoff: build the thumbnail metadata layers

Written for the next session after compaction. Read this and [[thumbnail-metadata-spec]] first. Nothing below is built yet; Billy approved the spec and said build it after compacting.

## Where things stand (all committed)

Plugin repo `authentic-ai-content-engine`, branch `dev`, released as aai-youtube v0.5.0. Clean tree.

Billy's vault `business-os` (`Content/banks/`), clean apart from daily notes:

- `outliers/` holds 143 notes, one per outlier, all with full workups (strategy, thumbnail_text, hero prose, packaging read). Thumbnails in `outliers/thumbs/thumbnail-{video_id}.jpg`, all real JPEGs.
- `outliers.base` with seven views. Billy has been editing it in Obsidian (column sizes, sort tweaks). Read the vault copy before touching it; do not overwrite his edits.
- `title-bank.md`: 24 shapes with linked proof examples, no preamble, no dropped section.
- `power-words-bank.md`: 34 entries, word plus one linked example, includes bolt-on phrases.
- `research-log.md`: replaces pattern-bank. Channel set with URLs, medians, floors, themes, plus findings. Nothing writing a video reads it.
- `pattern-bank.md`, `packaging-bank/` are gone. `pattern-bank1.md` archived to `Content/archive/`.

Plugin side, `shared-skills/vid-research/`: SKILL.md, the four templates in `assets/` (outlier-note, outliers.base, title-bank, power-words-bank, research-log), `references/pattern-extraction-prompts.md` (fill test, bolt-on rule), `references/thumbnail-vision-classification.md`, and the scripts (`youtube_fetch.py` keyless, `video_details.py`, `thumbnail_download.py` verifying JPEG bytes). `plugins/` regenerates from `shared-skills/` via `node scripts/generate-plugins.mjs`, then `node scripts/qa-plugins.mjs`.

## Billy's rulings that govern this build (do not relitigate)

- Tags are visual facts, never interpretations. Two-people test. Details in the spec.
- Emotional promise is a package property (title plus thumbnail), stored on the outlier note, using BENS letters plus fear, status, contrarian.
- No ranking language anywhere ("strongest", "outranks"). Numbers are facts. See memory `no-ranking-bias-in-banks`.
- No preambles in bank files. Build rules live below a `---` divider in templates, marked not-for-output.
- No "considered and dropped" sections. Remove means remove; no tombstones.
- Never nest two terms in one entry. Never combine tags.
- vid-framing never reads banks. Do not edit vid-title or vid-thumbnail without saying so first.
- Short replies. Verdict first.
- No em-dashes anywhere, including generated frontmatter and agent output.

## Build order

1. **Templates and references (plugin).**
   - `assets/outlier-note-template.md`: add the Layer 1 and Layer 3 fields per the spec schema. Retire `enhancers`.
   - `references/thumbnail-vision-classification.md`: add a Layer 1 tagging section with the full vocabulary and per-tag tests. The vision prompt must output tags, not prose, for hero, face, expression, gesture, layout, text_amount, text_style, background, bg_tone, devices. Keep the strategy classification as is.
   - `references/pattern-extraction-prompts.md`: add a Prompt 6, promise tagging, input title plus thumbnail_text plus strategy, output the BENS-plus-three list against the tests in the spec.
   - `assets/outliers.base`: add views once data exists (By hero, No face, Dark and big text, By promise). Use `'field == "value"'` and `field.contains("value")` syntax; verified against Obsidian docs this session. Relative dates: `published > now() - "90d"`.
   - SKILL.md: Phase 1 step 7 (the workup) now produces the tags; one sentence in "What this produces" naming the three layers.
   - Regenerate plugins, run QA.

2. **Migrate the 143 existing notes (vault).**
   - Layer 3 (promise) can be done from title plus thumbnail_text plus strategy without vision. One pass, or batched agents.
   - Layer 1 needs vision. Reuse the batch approach from this session: 7 agents, ~20 images each, each reads the reference then the images, writes JSON to the scratchpad, main session merges into frontmatter with a script. Zero failures last time. Include the vocabulary tables in the agent prompt verbatim so all seven tag identically.
   - Merge script pattern: match on `video_id` frontmatter, insert new fields after `thumbnail:`, drop `enhancers:`. Validate every note with pyyaml afterward. Keep `newline="\n"` (the repo enforces LF for `.base` and the vault is Obsidian).
   - Then tell Billy to reload Obsidian before opening the Base (Ctrl+P, Reload app without saving). New properties on 143 files at once will not all index without it.

3. **Views (vault and template).** Read the vault `outliers.base` first, add the new views to Billy's current file rather than overwriting, then mirror to the plugin template with the folder path swapped back to `banks/outliers`.

## Gotchas learned this session

- YouTube's CDN serves WEBP from a `.jpg` URL unless you send `Accept: image/jpeg` and check the magic bytes. Obsidian renders a WEBP-named-jpg as a blank tile. `thumbnail_download.py` now handles this; do not bypass it.
- Obsidian drops file-watcher events under a burst of writes. Always end a bulk write with the reload instruction.
- The vault keeps banks under `Content/banks/`, so any `file.inFolder(...)` in a Base must say `Content/banks/outliers` there and `banks/outliers` in the plugin template.
- Note filenames are sanitized titles; some contain `$`, `!`, parentheses. Quote paths. Match notes by `video_id`, never by name.
- Billy's working tree sometimes carries another session's staged changes (this happened with a Peak Systems design folder). Check `git status` for unrelated staged work before suggesting a commit, and commit `Content/banks` by path.

## Parked, not forgotten

- Scheduled competitor refresh as a Cowork task: scoped in [[v2-plans]] under vid-research. Recompute and report, never silently delete.
- `foundation/packaging-system.md` does not exist in the vault yet (Phase 7 never ran). The research log's thumbnail findings are meant to inform it when it does.
- `title-formats.md` in the vault is an older generic library that overlaps title-bank. Left alone; Billy's call.
