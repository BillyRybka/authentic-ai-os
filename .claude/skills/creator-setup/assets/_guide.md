---
type: guide
doc: container-guide
project: authentic-ai-os
status: active
tags: [guide, container]
---

# Authentic AI OS

This folder is your content vault. Everything the system builds about you and your channel lives here. The skills live in the plugin; your work lives here.

Work inside this folder. When you run Claude, point it at this folder so the skills read and write in the right place.

## Start here

Run `vid-foundation`. It walks you through your foundation in focused sessions, one at a time:

1. `vid-avatar`: who your viewer is
2. `vid-positioning`: your one-sentence channel promise (Iceberg Statement)
3. `vid-pillars`: what you teach (bottom of the iceberg)
4. `vid-credibility`: your three intro brags
5. `vid-backstory`: your origin story

Each saves to `foundation/creator-foundation.md`. The orchestrator auto-advances. Say "stop" any time to pause.

## What is in here

```
foundation/                 your identity docs (built by the foundation skills)
banks/proof-bank/assets/    proof entries and their screenshots
people/                     one file per person you mention (clients, guests)
CLAUDE.md                   instructions for Claude when working in this folder
.env.example                copy to .env and add API keys as future skills need them
```

More folders appear as more skills ship. Re-run `creator-setup` after a plugin update; it adds anything new and never touches what you have written.

## What's coming

This release ships the foundation skills. More are in development: voice capture, content production, pattern research, packaging. They will arrive in future plugin updates.

## One rule

Your `.env` holds API keys. It is never committed and never shared. Keep it in this folder, keep it private.
