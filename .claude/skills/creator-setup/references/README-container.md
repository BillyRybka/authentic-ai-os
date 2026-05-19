---
type: guide
doc: container-guide
project: authentic-ai-os
status: active
tags: [guide, container]
---

# Authentic AI OS

This folder is your content vault. Everything the system builds about you and your channel lives here. The skills live in the plugin; your work lives here.

Work inside this folder. When you run Claude, point it at `Authentic-AI-OS/` so the skills read and write in the right place.

## Start here

Run `vid-foundation`. It walks you through your foundation in focused sessions, one at a time:

1. `vid-avatar`: who your viewer is
2. `vid-positioning`: your one-sentence channel promise
3. `vid-pillars`: what you teach
4. `vid-credibility`: your three intro brags
5. `vid-backstory`: your origin story

Each saves to `foundation/creator-foundation.md`. The orchestrator auto-advances. Say "stop" any time to pause.

## After the foundation

- `vid-voice-capture` builds your voice profile. Bring 2 to 3 transcripts or a 10-minute live riff. Manual start.
- `vid-research` builds your pattern banks and your packaging defaults from real evidence. It needs a YouTube Data API key. Copy `.env.example` to `.env` and paste your key there. Manual start, around 1.5 hours the first time.

## What is in here

```
foundation/                 your identity docs (built by the foundation skills)
banks/proof-bank/assets/    proof entries and their screenshots
People/                     one file per person you mention (clients, guests)
.env.example                copy to .env, add your YT_API_KEY for vid-research
```

More folders appear as you use more of the system. Re-run `creator-setup` after a plugin update; it adds anything new and never touches what you have written.

## One rule

Your `.env` holds your API key. It is never committed and never shared. Keep it in this folder, keep it private.
