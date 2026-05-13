# Install Authentic AI OS

Welcome to the Inner Circle. This is how to install Billy's content system into your Claude Cowork or Claude Code.

## What you're getting

A set of AI skills that turn your raw material — stories, proof points, testimonials, metaphors — into YouTube videos in your authentic voice.

Skills installed:
- `vid-foundation` — set up your creator identity, voice profile, packaging system
- `vid-voice-capture` — extract your voice patterns from existing content
- `vid-capture` — log stories, proof points, testimonials, metaphors as you capture them
- `vid-title` — generate validated title variations
- `vid-thumbnail` — develop thumbnail concepts and briefs

Plus reference frameworks (BENS, Gift Framework, format planners) the skills use under the hood.

## Prerequisites

- Claude Cowork (desktop app) on Pro, Max, Team, or Enterprise — OR Claude Code CLI
- A GitHub account with access to the `peak-systems/authentic-ai-os` private repo (Billy adds you as a collaborator)
- For Claude Code CLI: `GITHUB_TOKEN` env var set so private repos can sync

## Install in Cowork (desktop)

1. Open Claude Cowork
2. Go to **Settings → Plugins → Marketplaces**
3. Click **Add Marketplace**
4. Paste: `peak-systems/authentic-ai-os`
5. Click **Install** on the `authentic-ai-os` plugin
6. Authorize permissions

Done. Skills are available in any Cowork project.

## Install in Claude Code CLI

```bash
claude
/plugin marketplace add peak-systems/authentic-ai-os
/plugin install authentic-ai-os@peak-systems
```

## First run

In a new Cowork project (or `cd` into a fresh folder for Claude Code):

```
Run /vid-foundation
```

Billy walks you through setting up your creator identity, voice profile, and packaging system. Takes ~30 minutes.

After that, you can capture material with `/vid-capture` whenever inspiration hits, and pull from your banks when you're ready to script a video.

## Updates

When Billy ships an update, you'll see it on next refresh. To pull manually:

```
/plugin update authentic-ai-os
```

Major releases will include a Loom walkthrough in the Inner Circle community.

## Troubleshooting

**"Plugin not found"** → confirm Billy added you as a collaborator on the private repo.

**"Authentication failed" (CLI only)** → set `GITHUB_TOKEN`:
```bash
export GITHUB_TOKEN=ghp_yourTokenHere
```
Generate a token at github.com → Settings → Developer settings → Personal access tokens → Fine-grained → access to `peak-systems/authentic-ai-os`.

**Skills not showing up** → run `/plugin` and confirm `authentic-ai-os` is enabled.

## Help

Inner Circle community → #ai-os channel.
