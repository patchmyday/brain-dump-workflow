# Brain Dump Workflow — PatchMyDay Video #1

> "Your best ideas happen in the shower and die before you sit down."

First video for PatchMyDay channel. iPhone Shortcut that captures voice to timestamped Markdown in iCloud. Built entirely with AI assistance (Hermes Agent + ElevenLabs + FFmpeg + Puppeteer).

## What's In This Repo

This documents the ACTUAL production process — every iteration, every dead end, every tool used. Not a template. A real build log.

| Path | What It Is |
|------|-----------|
| `production-log/` | Blow-by-blow of how this video was made, including failed approaches |
| `scripts/` | EN script (v1 + v2), CN script, section JSON configs |
| `subtitles/` | Proofread SRT files (EN + CN) |
| `scenes/` | HTML5 Canvas scene source code (v1 through v4) |
| `audio/` | ElevenLabs voice config, section splits, concat files |
| `xiaohongshu/` | Chinese cross-post content (script + 小红书 graphic text post) |
| `PRODUCTION-PLAYBOOK.md` | Reusable playbook extracted from this production |

## Video Iterations

| Version | What Changed | Result |
|---------|-------------|--------|
| v1 | Manim animation (Python) | Too slow, limited visual options |
| v2-lottie | HTML5 Canvas + LottieFiles characters | Fun but generic, no real screenshots |
| v3-screenshots | Real iPhone screenshots composited into scenes | Good but not synced to voice |
| v4-synced | Each scene duration-matched to voice section | Correct sync, final structure |
| v5-proofread | SRT corrections (15 fixes) burned onto clean v4 base | FINAL |

## Final Output

- **Duration:** 4:34 (274s)
- **Master:** 1920x1080, H.264, CRF 23, ~21MB
- **Compressed:** 1280x720, CRF 26, ~6.3MB (Telegram-friendly)
- **Voice:** ElevenLabs Adam voice, Multilingual v2
- **Subtitles:** Burned-in, Arial 22pt white + black outline
- **Music:** Background lo-fi mixed at -18dB (volume 0.12)

## Tools Used

- **Hermes Agent** — AI assistant that wrote scripts, generated scenes, ran FFmpeg, proofread
- **ElevenLabs** — TTS voice generation (Creator tier, Adam voice)
- **Puppeteer** — Rendered HTML5 Canvas scenes to frame sequences
- **FFmpeg** — Everything: concat, mux, subtitle burn, compression, audio mixing
- **Whisper** — Generated initial SRT from voiceover audio
- **Manim** — First attempt at animation (abandoned for HTML5 Canvas)
- **Node.js + Chromium** — Puppeteer runtime for headless rendering

## Brand

**PatchMyDay** — Cybersecurity + AI Automation. Bilingual EN/CN. Fireship-style (no face cam, fast cuts, screen recordings + motion graphics).
