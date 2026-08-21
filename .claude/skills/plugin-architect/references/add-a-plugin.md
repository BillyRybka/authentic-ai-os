# Adding, Removing, and Splitting Plugins

Also covers connectors, agents, and commands, since those attach to a plugin.

## Contents
1. The justification test
2. Naming
3. Adding a plugin
4. Connectors
5. Agents and commands
6. Passthrough files
7. Removing or splitting

## 1. The justification test
Before anything else, make the creator answer in one sentence: **who installs this and why.**

Reject the plugin if:
- The sentence needs "and" to be accurate. That is two plugins, or one plugin plus a skill that belongs elsewhere.
- The sentence also describes a plugin that already exists. Add the skill to that one instead.
- The answer is a category name ("marketing", "productivity") with no installer behind it. A category is a label, not an install decision. Labels go in the `category` and `keywords` fields, which are free. Plugins are not free: each one costs a version line, a git tag prefix, a public mirror repo, an update-check path, and a release cadence forever.

If it fails, say which test it failed and what to do instead. Do not create it.

## 2. Naming
Prefix with `aai-`. The plugin name is the skill namespace (`<plugin>:<skill>`), and it collides across marketplaces, not just within one. See invariant 3.

Before proposing names, list what is already installed so you do not collide:
```bash
ls ~/.claude/plugins/marketplaces/*/plugins/ 2>/dev/null
```

Present 5 to 10 candidates, each with its one-sentence installer, and let the creator pick. Never pick for them. The name is permanent once a client installs it.

## 3. Adding a plugin
Both manifests, same change, or the generator hard-fails.

**`.claude-plugin/marketplace.json`**, append to `plugins`:
```json
{
  "name": "aai-example",
  "displayName": "Example",
  "source": "./plugins/aai-example",
  "description": "One or two sentences a buyer reads. What it does, not how.",
  "version": "0.1.0",
  "author": { "name": "Billy Rybka", "email": "billy@peaksystems.io" },
  "license": "LicenseRef-Proprietary",
  "category": "content-creation",
  "keywords": ["..."]
}
```
`source` must be exactly `./plugins/<name>`. The gate blocks on any other value.

**`.claude-plugin/plugins-map.json`**, add under `plugins`:
```json
"aai-example": {
  "skills": ["some-skill"],
  "connectors": [],
  "agents": [],
  "commands": [],
  "files": []
}
```

Then regenerate and run the gate. A plugin shipping zero skills is a blocker.

### Deriving a bundle
To ship an "everything" plugin, derive it rather than retyping the list. BenAI hand-maintains theirs and roughly 450 lines of their map is one department restating every other skill's metadata, which drifts the moment a summary changes.
```json
"aai-everything": { "includePluginsSkills": ["authentic-ai-os", "aai-example"], "skills": [] }
```
The generator unions and de-duplicates them.

## 4. Connectors
One MCP server per file in `connectors/`, referenced by name. The generator writes each plugin's `.mcp.json` from its declared list, so a server is defined once no matter how many plugins use it.

`connectors/apify.json`:
```json
{ "type": "http", "url": "https://mcp.apify.com" }
```

`connectors/youtube.json`:
```json
{ "command": "npx", "args": ["-y", "@kirbah/mcp-youtube"], "env": { "YOUTUBE_API_KEY": "" } }
```

Declare it: `"connectors": ["apify", "youtube"]`. Leave secret values empty in the file and document the key in `.env.example`. The gate blocks on anything that looks like a live key in the shipped tree.

## 5. Agents and commands
One file each in `agents/<id>.md` and `commands/<id>.md`, declared by id in the map. Same rule as skills: stored once, copied into every plugin that claims it.

## 6. Passthrough files
LICENSE, README, and similar per-plugin files live in `plugin-files/<plugin-name>/` and are declared by path:
```json
"files": ["plugin-files/aai-example/LICENSE", "plugin-files/aai-example/README.md"]
```
They land at the plugin root by basename. They are normalized to LF like everything else.

## 7. Removing or splitting
Removing a plugin that has already shipped takes it away from clients on their next update. Confirm with the creator first, and confirm again if it holds skills nothing else ships.

Splitting: create the new plugin, move the skill ids in the map, regenerate, run the gate. Because skills live once in `shared-skills/`, a split moves list entries, never files. If a skill should be in both, list it in both. That is the whole point of the layout.
