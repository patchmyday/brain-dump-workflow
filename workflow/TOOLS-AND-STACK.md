# Tools & Stack

## Core Production Stack

| Tool | Purpose | Cost |
|------|---------|------|
| **ElevenLabs** | Text-to-speech voice generation | Creator tier (~$22/mo, 121 credits) |
| **FFmpeg** | Video encoding, muxing, subtitle burning | Free (open source) |
| **Whisper** | Speech-to-text for subtitle generation | Free (open source) |
| **Puppeteer** | HTML5 Canvas → video frame rendering | Free (open source) |
| **Hermes Agent** | AI assistant for automation + scripting | Self-hosted |

## Optional Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **Manim** | Mathematical/technical animations | Complex visualizations |
| **Lottie/LottieFiles** | Pre-made character animations | Fun/personality elements |
| **Node.js + Canvas** | Programmatic graphics generation | Dynamic text overlays |
| **ImageMagick** | Image manipulation | Thumbnails, composites |

## AI Assistance

| Task | AI Tool |
|------|---------|
| Script writing | Claude (Opus for quality, Sonnet for speed) |
| Script proofreading | Claude (any model) |
| Scene planning | Claude + vision (analyze reference screenshots) |
| HTML animation code | Claude Sonnet |
| FFmpeg command generation | Claude (any model) |
| Subtitle correction | Claude + manual review |
| Thumbnail design | Stable Diffusion / Midjourney (future) |

## File Organization

```
content-engine/
├── output/
│   └── {video-slug}/
│       ├── audio-v{N}/          # Voice generation iterations
│       │   ├── 01-hook-en.mp3
│       │   ├── ...
│       │   ├── voiceover-en.mp3
│       │   └── subtitles-en.srt
│       ├── scenes/              # Individual scene renders
│       │   ├── scene-01-hook.mp4
│       │   ├── scene-02-intro.mp4
│       │   └── ...
│       ├── assets/              # Screenshots, images, Lotties
│       ├── html/                # HTML5 Canvas scene sources
│       ├── scripts/             # Automation scripts
│       ├── final-en.mp4         # Master render (1080p)
│       ├── final-en-720p.mp4   # Compressed (720p)
│       └── final-cn.mp4        # Chinese version
```

## Hardware Requirements

- Any Linux server with FFmpeg (rendering is CPU-bound)
- 4GB+ RAM for Puppeteer rendering
- Fast storage for frame sequences (temporary, ~2GB per video)
- No GPU required (all CPU encoding)
