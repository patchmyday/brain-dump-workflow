# Phase 4: Assembly & Polish

## Step 1: Mux Video + Audio

```bash
# Combine clean video with voiceover
ffmpeg -y -i scenes-synced.mp4 -i voiceover-en.mp3 \
  -c:v copy -c:a aac -b:a 128k -shortest \
  muxed.mp4
```

## Step 2: Add Background Music

```bash
# Mix voice (full volume) with music (-18dB)
ffmpeg -y -i voiceover-en.mp3 -i music.mp3 \
  -filter_complex "[1:a]volume=0.12[music];[0:a][music]amix=inputs=2:duration=first[out]" \
  -map "[out]" mixed-audio.aac

# Or add music during final assembly
ffmpeg -y -i scenes-synced.mp4 -i voiceover-en.mp3 -i music.mp3 \
  -filter_complex "[1:a]volume=1[voice];[2:a]volume=0.12[music];[voice][music]amix=inputs=2:duration=first[out]" \
  -map 0:v -map "[out]" -c:v copy -c:a aac -b:a 128k \
  final-no-subs.mp4
```

## Step 3: Burn Subtitles

```bash
# Burn proofread SRT into video
ffmpeg -y -i final-no-subs.mp4 \
  -vf "subtitles=subtitles-en.srt:force_style='FontName=Arial,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=2,Shadow=1,MarginV=30'" \
  -c:v libx264 -preset fast -crf 23 -c:a copy \
  final-master.mp4
```

**IMPORTANT:** Always burn subs onto the CLEAN video (no existing subs). Double-subs = amateur hour.

## Step 4: Compress for Distribution

```bash
# 720p for Telegram/social (< 10MB target)
ffmpeg -y -i final-master.mp4 \
  -vf scale=1280:720 \
  -c:v libx264 -preset fast -crf 26 \
  -c:a aac -b:a 96k \
  final-720p.mp4

# Check file size
ls -lh final-720p.mp4
```

## Encoding Presets Reference

| Preset | Speed | Size | Use When |
|--------|-------|------|----------|
| ultrafast | 1x | 2x | Testing/preview only |
| fast | 3x | 1.1x | Production renders |
| medium | 5x | 1x | Final master (if time allows) |
| slow | 10x | 0.95x | Archival quality |

## CRF Reference

| CRF | Quality | Use |
|-----|---------|-----|
| 18 | Visually lossless | Archival master |
| 23 | High quality | YouTube upload |
| 26 | Good quality | Social media / Telegram |
| 30 | Acceptable | Quick previews |

## Final Checklist

- [ ] Video plays start to finish without glitches
- [ ] Voice and visuals are in sync
- [ ] Subtitles are readable and correctly timed
- [ ] No double subtitles
- [ ] Background music audible but not overpowering
- [ ] File size under 50MB for Telegram
- [ ] Both 1080p and 720p versions rendered
