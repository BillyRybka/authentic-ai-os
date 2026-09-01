# Authentic AI YouTube

Billy Rybka's YouTube content system, packaged as a Claude Code plugin. An Obsidian-native workspace for taking ideas to published YouTube videos and cross-platform derivatives in the creator's voice.

## Installation

```
/plugin marketplace add BillyRybka/authentic-ai
/plugin install aai-youtube@authentic-ai
```

## Getting updates

New versions land in the marketplace repo. They do not install themselves unless you turn that on.

- **Automatic:** open `/plugin`, go to the Marketplaces tab, and enable auto-update for `authentic-ai`. Third-party marketplaces ship with this off. Once enabled it runs shortly after a session starts, so the update lands on your next launch rather than mid-session.
- **Manual, any time:** `/plugin marketplace update authentic-ai`.
- **Claude Cowork** keeps its own plugin state, synced through your claude.ai account rather than from the CLI. Updating in the terminal does not update Cowork. Refresh it from Cowork's own plugin panel.

## What's in this release

**Foundation.** Six steps, run by the `/foundation` orchestrator. It checks what is already locked and picks up where you stopped.

| Skill | Produces |
|---|---|
| `vid-avatar` | Offer summary (`offer.md`), avatar plus Top 3 perceived problems in viewer language (`avatar.md`) |
| `vid-positioning` | Iceberg Statement (`iceberg.md`) |
| `vid-pillars` | 8 to 12 content pillars (`iceberg.md`) |
| `vid-credibility` | Three viewer-relevant credibility brags (`credibility.md`) |
| `vid-backstory` | Problem-Action-Outcome backstory (`backstory.md`) |
| `vid-voice-capture` | Reference pieces (`reference-pieces/`) plus the voice guardrail (`voice-profile.md`) |

The first five are interviews and run into each other. Voice capture needs real material from you, so it waits for your go.

**Research.** `vid-research` builds your evidence base from real YouTube data: one note per outlier with its thumbnail and receipts, a browsable gallery, title shapes, and power words.

**Per video.** `vid-pipeline` routes one video from raw idea to filming-ready script, delegating to `vid-braindump`, `vid-framing`, `vid-title`, `vid-thumbnail`, `vid-structure`, `vid-intro`, `vid-segment`, `vid-ending`, and `vid-pressure-test`.

**Voice, ongoing.** `vid-voice-audit` checks a finished script against your real sentences. `vid-voice-update` turns a correction you make mid-draft into a permanent rule when it should be one.

**Also:** `creator-setup` scaffolds the workspace, `vid-bank` captures stories and metaphors, `aai-feedback` sends a bug or a win straight to Billy.

## First-time setup

Run `creator-setup` once inside the folder you want to use as your content vault. It scaffolds the workspace structure, writes a workspace `CLAUDE.md`, and records any path overrides you choose. Re-run it after any update and it adds what is new without touching what you have written.

Then run `/foundation`. Each session is a dedicated sitting. Stop and resume whenever.

## What this is NOT

- A generic AI assistant. This is a content production system.
- A vault scanner. It reads on demand, never pre-emptively.
- A finished product. Foundation, research, and the script pipeline have shipped. Idea generation and performance measurement are still in development.

## Support

For support, contact billy@peaksystems.io.

## License

Proprietary. See [LICENSE](./LICENSE).
