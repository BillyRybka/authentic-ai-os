# QA Gate and Release

## Contents
1. The gate
2. What each check catches
3. Reading the result
4. Pre-release sequence
5. After the release

## 1. The gate
```bash
node scripts/qa-plugins.mjs                 # full pass, current branch
node scripts/qa-plugins.mjs --ref dev       # check committed state of the release branch
node scripts/qa-plugins.mjs --json          # machine-readable
node scripts/qa-plugins.mjs --no-git        # skip git checks, NEVER before a release
```

Exit 0 means no blockers. Exit 1 means do not release. It runs `generate-plugins.mjs --check` internally, so the gate alone is sufficient before a release.

`--no-git` exists for working in a non-repo copy. Using it before a release disables the check that caught the only bug that has actually reached clients. Do not.

## 2. What each check catches

**Manifest integrity**
| Check | Catches |
|---|---|
| `manifest-parity` | a plugin in one manifest and not the other, or a wrong `source` path |
| `name-collision` | the same plugin name defined twice |
| `version` | missing or non-semver version, or a version whose git tag already exists |
| `empty-plugin` | a plugin that built with no plugin.json or zero skills |

**Skill integrity**
| Check | Catches |
|---|---|
| `missing-skill` | declared skill with no folder, or a folder with no SKILL.md |
| `frontmatter` | missing frontmatter, missing name or description, or a name that disagrees with its folder |
| `description-length` | over 1024 chars, which rejects the entire plugin at validation |
| `dangling-ref` | a skill pointing at a `references/` or `assets/` file it does not contain |
| `orphan-skill` | a skill in `shared-skills/` that no plugin claims (warning) |

**Reference integrity**
| Check | Catches |
|---|---|
| `missing-knowledge` | a referenced `knowledge/` file that does not exist |
| `uncommitted-knowledge` | one that exists on disk but is not committed, so it will not ship |

**Shipped-tree hygiene**
| Check | Catches |
|---|---|
| `stale-build` | `plugins/` does not match source, so the release would ship the old copy |
| `crlf` | CRLF in the shipped tree, which makes Cowork leak frontmatter into the body |
| `debug-trace` | builder-only `DEBUG-TRACE` instrumentation |
| `absolute-path` | a hardcoded `C:\Users\...` or `/Users/...`, useless on a client machine and it leaks the username |
| `secret` | something shaped like a live API key |
| `em-dash` | an em dash in shipped prose, code spans and fenced blocks exempt (warning) |

**Release state** (warnings, all require git)
`dirty-tree`, `branch` (releases come from `dev`), and a version whose tag already exists.

## 3. Reading the result
**BLOCKER is a hard stop.** Each one is a broken client install, not a style note. Fix the source, regenerate, re-run. Never release past a blocker and never edit `plugins/` to silence one, since the next generate deletes the edit.

**WARNING is judgment.** Surface every one to the creator with the file and line. Do not silently accept them and do not fix an em dash in a doc that is quoting the character on purpose.

If a check is wrong, fix the check in `scripts/qa-plugins.mjs` and say so. Do not work around it.

## 4. Pre-release sequence
Run in order. Stop at the first failure.

1. **Clean tree, right branch.** Releases come from `dev`. `release.ps1` refuses anything else. Commit or stash first.
2. **Regenerate.** `node scripts/generate-plugins.mjs`. Confirm the per-plugin counts match intent.
3. **Commit the regenerated tree** if it changed. `plugins/` is tracked because `main` ships from it.
4. **Run the gate against the release ref.** `node scripts/qa-plugins.mjs --ref dev`. Zero blockers required.
5. **Confirm the version with the creator.** Which plugin, which number. This is a checkpoint, not a guess.
6. **Release.** `pwsh scripts/release.ps1 -Plugin <name> -Version <x.y.z>`. Use `-DryRun` first on anything unusual: it builds `main` and the artifact locally, pushes nothing, and prints the rollback command.

Reminder from invariant 10: `main` must always carry every shipping plugin. Release selects which plugin versions and publishes, never which plugins exist. A single-plugin allowlist would delete the others from `main` and break those installs.

## 5. After the release
- Verify the public marketplace repo (`BillyRybka/authentic-ai`, remote `public`) received the push. That repo is the distribution channel: clients added it once and Claude auto-updates their plugins from it. Nothing else needs publishing.
- **Only history-free snapshots reach the public remote, never a branch.** main's own pre-allowlist history carries Billy's creator-foundation.md, banks/, audits/, and WIP skills; `git push public main` would leak all of it. release.ps1 builds a snapshot commit of main's tree on the separate `public-main` lineage and pushes that. If you ever publish manually, use the same commit-tree mechanism. A wrong push here is a data leak, not a broken build.
- Confirm `dev` was synced forward to the released version so future work does not iterate from behind.
