# Phase 2: Voice Production

## ElevenLabs Setup

- **Plan:** Creator tier (121 credits/mo)
- **Voice:** Adam (or custom clone)
- **Model:** Multilingual v2
- **Settings:** Stability 0.5, Similarity 0.75, Style 0.5

## Section-Based Generation

Split the script into logical sections. Generate each separately for:
- Better quality control (re-gen one section, not the whole thing)
- Easier timing/sync with visuals
- Flexibility to reorder

### Naming Convention

```
audio-v{N}/
  01-hook-en.mp3
  02-intro-en.mp3
  03-build-dictate-en.mp3
  04-build-timestamp-en.mp3
  05-build-save-en.mp3
  06-build-rename-en.mp3
  07-demo-en.mp3
  08-power-tips-en.mp3
  09-cta-en.mp3
  voiceover-en.mp3        # concatenated full track
  subtitles-en.srt        # whisper-generated, then proofread
```

For Chinese versions, use `-cn` suffix.

## Concatenation

```bash
# Create file list
for f in 0{1..9}-*-en.mp3; do echo "file '$f'"; done > concat.txt

# Concatenate
ffmpeg -f concat -safe 0 -i concat.txt -c copy voiceover-en.mp3
```

## Subtitle Generation

```bash
# Generate SRT from voiceover using Whisper
whisper voiceover-en.mp3 --model medium --output_format srt --language en
```

## Proofreading Checklist

Common TTS transcription errors to watch for:
- [ ] Proper nouns (DoorDash, PatchMyDay, Obsidian, iCloud)
- [ ] Technical terms (regex, Python, SRT, API)
- [ ] Homophones (mic/Mike, sync/sink)
- [ ] Contractions and grammar
- [ ] Number formatting (timestamps, dates)
- [ ] Missing/extra commas affecting pacing
