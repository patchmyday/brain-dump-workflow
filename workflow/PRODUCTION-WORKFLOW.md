# Production Workflow — PatchMyDay Video Pipeline

This is the end-to-end workflow for producing a PatchMyDay video from idea to upload. Refined from Brain Dump Workflow (Video #1).

## Pipeline Overview

```
IDEA → SCRIPT → VOICE → SCENES → SYNC → SUBTITLES → MIX → RENDER → COMPRESS → UPLOAD
```

## Phase 1: Pre-Production (1-2 hours)

1. **Brain dump** — Voice capture the raw idea (use the shortcut!)
2. **Outline** — Structure into sections: Hook → Intro → Build → Demo → Tips → CTA
3. **Script** — Write conversational script (~1000-1200 words for 4-5 min video)
4. **Shot list** — Map each script section to visual scenes
5. **Asset collection** — Screenshots, screen recordings, icons, animations

See: [01-PRE-PRODUCTION.md](01-PRE-PRODUCTION.md)

## Phase 2: Voice Production (30 min)

1. **Split script** into sections (hook, intro, build-step-1, build-step-2, etc.)
2. **Generate TTS** per section via ElevenLabs API
3. **Review** each clip — regenerate any that sound off
4. **Concatenate** all clips into single voiceover track
5. **Measure** total duration and per-section timestamps

See: [02-VOICE-PRODUCTION.md](02-VOICE-PRODUCTION.md)

## Phase 3: Visual Production (2-4 hours)

1. **Create scenes** matching each script section
2. **Render** each scene to match voice section duration
3. **Sync** scenes to voiceover timestamps
4. **Concatenate** all scene videos into single visual track

Methods (pick per scene):
- **Screenshots** with Ken Burns zoom/pan (simplest)
- **HTML5 Canvas** animations rendered via Puppeteer
- **Manim** for technical/math animations
- **Screen recordings** for demos
- **Lottie** animations for character/fun elements

See: [03-VISUAL-PRODUCTION.md](03-VISUAL-PRODUCTION.md)

## Phase 4: Assembly & Polish (1 hour)

1. **Mux** video + voiceover audio
2. **Add background music** at -18dB under voice
3. **Burn subtitles** from proofread SRT
4. **Proofread** SRT one final time
5. **Render** master (1080p) and compressed (720p) versions

See: [04-ASSEMBLY.md](04-ASSEMBLY.md)

## Phase 5: Delivery (30 min)

1. **Watch** the full video end-to-end
2. **Export** thumbnail (pick best frame or design custom)
3. **Write** title, description, tags
4. **Upload** to YouTube
5. **Cross-post** to Xiaohongshu (CN version if available)

See: [05-DELIVERY.md](05-DELIVERY.md)

## Timing Estimate

| Phase | Time |
|-------|------|
| Pre-production | 1-2 hours |
| Voice | 30 min |
| Visuals | 2-4 hours |
| Assembly | 1 hour |
| Delivery | 30 min |
| **Total** | **5-8 hours** |

## Lessons Learned (Video #1)

1. **Script first, always** — Don't start visuals until the script is locked
2. **Section-based rendering** — Render each voice section as a separate scene, then concatenate. Prevents re-rendering everything when one section changes
3. **Proofread SRT early** — TTS transcription has errors (proper nouns, homophones). Fix before burning subs
4. **-preset fast not ultrafast** — ultrafast doubles file size for marginal time savings
5. **720p for Telegram** — Telegram has 50MB limit, 720p CRF 26 keeps files under 10MB
6. **Voice + music mix** — Always -18dB for background music. Voice must dominate
7. **Don't burn subs onto video that already has subs** — Use the raw/clean video base!
