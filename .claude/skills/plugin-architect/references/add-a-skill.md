# Skills In, Out, and Between Plugins

## Contents
1. Where a skill lives at each stage
2. Graduating a WIP skill
3. Adding an existing skill to another plugin
4. Moving between plugins
5. Parking a skill
6. What the gate checks

## 1. Where a skill lives at each stage

| Stage | Location | Ships | Auto-loads while working in this repo |
|---|---|---|---|
| WIP | `.claude/skills/<id>/` | no | yes |
| Shipping | `shared-skills/<id>/` + listed in the map | yes | no |
| Built output | `plugins/<plugin>/skills/<id>/` | yes | never edit |

`.claude/skills/` is the workshop. It never ships, because `main` is an allowlist rebuild and that path is not on it. That is structural, not a rule anyone has to remember.

## 2. Graduating a WIP skill
```bash
git mv .claude/skills/<id> shared-skills/<id>
```
Then add `"<id>"` to the target plugin's `skills` array in `.claude-plugin/plugins-map.json`.

Before regenerating, check these by hand. The gate catches all of them, but catching them now is faster than reading a blocker list:

- `SKILL.md` frontmatter `name:` equals `<id>`, exactly. A mismatch silently fails to resolve.
- `description` is under 1024 characters. Over that and the validator rejects the **entire plugin**, every skill in it.
- Every `references/`, `assets/`, `scripts/`, or `templates/` path the skill names actually exists inside the skill folder.
- Every `knowledge/<file>.md` it references exists at repo root **and is committed**. On disk is not enough, see invariant 5.
- No machine-local paths (`C:\Users\...`, `/Users/...`) anywhere in it.

The skill's own `references/` and `assets/` travel with it automatically. Shared `knowledge/` files do not need declaring: the generator finds them by scanning the skill's markdown for `knowledge/<file>.md` and copies each into that plugin's `knowledge/` folder, which is where `${CLAUDE_PLUGIN_ROOT}/knowledge/...` resolves at runtime.

Regenerate, run the gate, report.

## 3. Adding an existing skill to another plugin
Add the id to the second plugin's `skills` array. Nothing else. The skill stays in one place in `shared-skills/` and the generator copies it into both.

Do not copy the folder. Two physical copies drift, and the drift is invisible until a client reports that one plugin behaves differently from the other.

## 4. Moving between plugins
Remove the id from one `skills` array, add it to the other. No file moves.

If clients already installed the plugin it is leaving, they lose the skill on their next update. Flag that before doing it.

## 5. Parking a skill
```bash
git mv shared-skills/<id> .claude/skills/<id>
```
and remove the id from every `skills` array in the map. Removing the folder without removing the map entry is a blocker, which is the intended safety net.

## 6. What the gate checks
Run `node scripts/qa-plugins.mjs` after any of the above. Skill-related blockers:

| Check | Fires when |
|---|---|
| `missing-skill` | the map names a skill with no folder, or a folder with no SKILL.md |
| `frontmatter` | no frontmatter, no `name:`, no `description:`, or `name:` does not match the folder |
| `description-length` | over 1024 characters |
| `dangling-ref` | the skill points at a `references/` or `assets/` file it does not contain |
| `missing-knowledge` | a referenced `knowledge/` file does not exist |
| `uncommitted-knowledge` | it exists on disk but is not committed on the release ref |
| `orphan-skill` (warning) | a folder in `shared-skills/` that no plugin claims, so it will never ship |
