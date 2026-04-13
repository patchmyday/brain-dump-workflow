# Production Playbook — PatchMyDay Videos

Extracted from actual Video #1 production. These are real lessons, not theory.

## The Pipeline

```
SCREENSHOTS → SCRIPT → VOICE (per section) → SCENES (duration-matched) → MUX → SUBS → MIX → RENDER
```

## Step 1: Collect Screenshots First

Before writing a single word, have ALL the screenshots/recordings you'll reference. The script writes itself when you're describing real screens.

For Video #1: Jason uploaded 7 iPhone screenshots of the shortcut being built + demo results.

## Step 2: Write Script in Sections

Use `sections.json` format — each key is a section name, value is the voiceover text:

```json
{
  "01-hook": "Your best ideas happen in the shower...",
  "02-intro": "This is Brain Dump, a single iPhone shortcut...",
  ...
}
```

This format is machine-readable for the TTS generation step.

### Structure (proven to work for 4-5 min tutorial):
1. **Hook** (5-7s) — pain point + promise
2. **Intro** (15s) — what we're building + anti-features
3. **Build steps** (2-3 min) — one section per logical step
4. **Demo** (30-40s) — run it end to end, show proof
5. **Power tips** (40s) — rapid fire advanced moves
6. **CTA** (15s) — tease next video, subscribe

## Step 3: Generate Voice Per Section

```bash
# Generate each section separately via ElevenLabs API
# Name: {NN}-{section}-{lang}.mp3
01-hook-en.mp3
02-intro-en.mp3
03-build-dictate-en.mp3
...
```

**Why per section?** Bad take on section 5? Regenerate just that one. Changed script for section 3? Only re-gen that section. Total voice track doesn't need re-doing.

Concatenate when all sections are good:
```bash
for f in 0{1..9}-*-en.mp3; do echo "file '$f'"; done > concat.txt
ffmpeg -f concat -safe 0 -i concat.txt -c copy voiceover.mp3
```

## Step 4: Build Scenes (Duration-Matched)

**Critical:** Measure each voice section's duration with ffprobe BEFORE creating scenes.

```bash
for f in 0{1..9}-*-en.mp3; do
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  echo "$f → ${dur}s"
done
```

Then set each scene's display time to exactly match. This is what v4-synced got right that v1-v3 got wrong.

### Rendering: HTML5 Canvas via Puppeteer

Create one big HTML file with all scenes. Each scene is a function that draws to canvas. Puppeteer takes a screenshot per frame at 30fps.

```bash
# ~275 seconds for a 4:34 video at 1920x1080
node render.js
ffmpeg -framerate 30 -i frames/frame_%05d.png -c:v libx264 -pix_fmt yuv420p scenes.mp4
```

## Step 5: Generate + Proofread Subtitles

```bash
whisper voiceover.mp3 --model medium --output_format srt
```

Then MANUALLY proofread. Whisper gets ~95% right but consistently misses:
- Brand names (PatchMyDay, DoorDash, Obsidian)
- Tech terms (regex, .txt, .md, Python)
- Homophones (mic/Mike, sync/sink)

See `subtitles/PROOFREAD-LOG.md` for the 15 corrections from Video #1.

## Step 6: Final Assembly

```bash
# 1. Mux clean video + voice + background music
ffmpeg -y -i scenes.mp4 -i voiceover.mp3 -i music.mp3 \
  -filter_complex "[1:a]volume=1[v];[2:a]volume=0.12[m];[v][m]amix=inputs=2:duration=first[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 128k -shortest \
  final-no-subs.mp4

# 2. Burn subtitles (onto CLEAN video — never onto video that already has subs!)
ffmpeg -y -i final-no-subs.mp4 \
  -vf "subtitles=subtitles-en.srt:force_style='FontName=Arial,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=2,Shadow=1,MarginV=30'" \
  -c:v libx264 -preset fast -crf 23 -c:a copy \
  final-master.mp4

# 3. Compress for social
ffmpeg -y -i final-master.mp4 -vf scale=1280:720 \
  -c:v libx264 -preset fast -crf 26 -c:a aac -b:a 96k \
  final-720p.mp4
```

## Hard-Won Lessons

1. **Don't burn subs onto video that already has subs** — you get double subs. Always use the clean video base. (We made this mistake on v5.)

2. **Section-based voice gen is non-negotiable** — re-generating a full 4-min voiceover because one sentence sounds off is a waste of ElevenLabs credits.

3. **Duration-match scenes to voice** — this took us 4 iterations to learn. Hardcoded scene durations = guaranteed desync.

4. **-preset fast, not ultrafast** — ultrafast doubles file size for maybe 30% time savings. Not worth it for final renders.

5. **Background music at volume 0.12 (-18dB)** — any louder and it fights the voice. Any quieter and it's inaudible.

6. **720p CRF 26 for Telegram** — keeps files under 10MB for the 50MB limit with room to spare.

7. **Whisper for initial SRT, then proofread** — never ship Whisper output directly. Budget 15 min for manual review.

8. **HTML5 Canvas > Manim for this style** — Manim is great for math animations but too rigid for tutorial-style content with screenshots and overlays.
