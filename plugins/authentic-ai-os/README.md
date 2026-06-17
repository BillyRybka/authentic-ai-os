# Authentic AI OS

Billy Rybka's YouTube content system, packaged as a Claude Code plugin. An Obsidian-native workspace for taking ideas to published YouTube videos and cross-platform derivatives in the creator's voice.

## What's in this release

Five foundation interview skills plus an orchestrator command. Each skill runs a focused session and writes locked sections to `foundation/creator-foundation.md` in the creator's workspace.

| Skill | Produces |
|---|---|
| `vid-avatar` | Offer summary, avatar description, Top 3 perceived problems in viewer language |
| `vid-positioning` | Iceberg Statement (positioning) |
| `vid-pillars` | 8 to 12 content pillars |
| `vid-credibility` | Three viewer-relevant credibility brags |
| `vid-backstory` | Problem-Action-Outcome backstory |

Plus:

- `creator-setup`: one-time installer that scaffolds the workspace inside the creator's chosen content folder.
- `/foundation`: orchestrator. Checks state, points the creator at the next skill, auto-invokes it.

## Installation

Install via your Claude Code plugin marketplace, or load locally:

```bash
claude --plugin-dir /path/to/authentic-ai-os
```

## First-time setup

Run `creator-setup` once inside the folder you want to use as your content vault. It scaffolds the workspace structure, writes a workspace `CLAUDE.md`, and records any path overrides you choose.

After setup, run `/foundation` to walk through the five interviews. Each interview is a dedicated session. You can stop and resume at any point.

## What this is NOT

- A generic AI assistant. This is a content production system.
- A vault scanner. Read on demand, never pre-emptively.
- A finished product. More skills are in development: voice capture, content production, pattern research, and packaging.

## Support

For support, contact billy@peaksystems.io.

## License

Proprietary. See [LICENSE](./LICENSE).
