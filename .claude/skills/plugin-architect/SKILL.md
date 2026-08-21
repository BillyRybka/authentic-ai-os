---
name: plugin-architect
description: Owns the plugin marketplace architecture for this repo. Use for anything that changes what ships: adding or removing a plugin, adding a skill to a plugin, graduating a WIP skill out of .claude/skills/, moving a skill between plugins, wiring an MCP connector, bumping a version, or running the pre-release QA gate. Triggers include "add a plugin", "new plugin", "graduate this skill", "ship this skill", "put this skill in X", "move this skill", "add a connector", "wire up apify", "is this ready to release", "run QA on the plugins", "check the marketplace", "why is the build stale", "release the plugin". Also use before ANY release, because the QA gate is the only thing standing between a broken install and every client. Not for writing skill content, that is skill-from-task.
---

# Plugin Architect

Single front door for the marketplace. Everything under `plugins/` is generated output. The source of truth is four things, and this skill is what keeps them honest.

| File or folder | Owns |
|---|---|
| `.claude-plugin/marketplace.json` | plugin metadata and version |
| `.claude-plugin/plugins-map.json` | what goes IN each plugin |
| `shared-skills/` | every shippable skill, exactly once |
| `knowledge/`, `connectors/`, `agents/`, `commands/` | shared assets, one copy each |

**Never hand-edit anything under `plugins/`.** It is deleted and rebuilt on every generate. Read `references/architecture-rules.md` before your first change in a session, it holds the invariants that have already broken things once.

## Route

| Ask | Do |
|---|---|
| Add a plugin, remove one, split one | `references/add-a-plugin.md` |
| Add a skill to a plugin, graduate a WIP skill, move one between plugins, park one | `references/add-a-skill.md` |
| Wire an MCP connector, add an agent or command | `references/add-a-plugin.md`, connectors section |
| "Is this ready to ship", pre-release check, release | `references/qa-and-release.md` |
| Build is stale, QA is failing, something broke | Run the gate below, then `references/qa-and-release.md` |

## The two commands

Everything mechanical is one of these. Run them, do not reimplement them.

```bash
node scripts/generate-plugins.mjs      # rebuild plugins/ from source
node scripts/qa-plugins.mjs            # the gate: 20 checks, BLOCKER vs WARNING
```

`generate-plugins.mjs --check` verifies `plugins/` matches source without writing. `qa-plugins.mjs` runs that check itself, so the gate alone is enough before a release.

## Every change follows the same shape

```
Task Progress:
- [ ] 1. Decide (does this need a new plugin, or does it belong in one that exists)
- [ ] 2. Edit source only (map + marketplace + shared-skills, never plugins/)
- [ ] 3. Regenerate
- [ ] 4. Run the gate
- [ ] 5. Report what changed and what the gate said
```

### 1. Decide
For a new plugin, apply the one-sentence test in `references/add-a-plugin.md`. If you cannot say who installs it and why in one sentence, it is not a plugin, it is a skill in a plugin that already exists. Say so and stop.

### 2. Edit source only
`plugins-map.json` and `marketplace.json` change together, always. The generator fails loudly if one has a plugin the other does not, so a half-added plugin cannot ship. That guard is deliberate, do not route around it.

### 3. Regenerate
`node scripts/generate-plugins.mjs`. It prints one line per plugin: skills, knowledge files, connectors. Check the counts match what you intended before moving on.

### 4. Run the gate
`node scripts/qa-plugins.mjs`. **BLOCKER means stop.** Every blocker is a broken client install, not a style note. Fix and re-run until clean. Warnings are judgment, surface them and let the creator decide.

### 5. Report
Say what moved, what the generated counts were, and the gate result. If the gate passed with warnings, list them.

## Human checkpoints

Stop and ask before any of these. Do not proceed on your own judgment.

- **Creating a new plugin.** Present 5 to 10 candidate names with the one-sentence "who installs this" for each, and let the creator pick. Naming is permanent once clients install.
- **Renaming the marketplace or any plugin.** This re-keys every existing client install. Never bundle it into another change.
- **Bumping a version or cutting a release.** Confirm the number.
- **Removing a skill from a plugin that already shipped.** Clients lose it on update.

## Self-improvement

This skill is never finished.

- When a QA check misses something that broke, add the check to `scripts/qa-plugins.mjs` with a `why` comment naming what it broke, then note the invariant in `references/architecture-rules.md`.
- When the creator corrects a decision here, write the correction into the relevant reference file so it sticks past this session.
- When a new invariant emerges (a packaging rule, a Cowork quirk, a validator limit), it goes in `references/architecture-rules.md` and, if it is mechanically checkable, in the gate.

## Routing

| Step | Reference |
|---|---|
| Invariants, read first | `references/architecture-rules.md` |
| Plugins, connectors, agents, commands | `references/add-a-plugin.md` |
| Skills in, out, and between plugins | `references/add-a-skill.md` |
| QA gate and release | `references/qa-and-release.md` |
