# Scene Production — 4 Iterations

## Evolution

### v1-manim.py + v1-manim-canvas.html
First attempt using Python Manim. Created 3 scenes (BrainDumpIntro, WorkflowDiagram, BeforeAfterScene). Rendered at 480p15.
**Abandoned** — too limited for the visual style, slow iteration cycle.

### v2-lottie.html
HTML5 Canvas with LottieFiles character animations. Rendered via Puppeteer (headless Chromium → frame screenshots → FFmpeg encode).
More fun but still generic. Also made a vertical version for Xiaohongshu.

### v3-screenshots.html
Breakthrough: composited Jason's real iPhone screenshots into Canvas scenes. Each scene shows the actual Shortcuts editor UI. Much more authentic as a tutorial.
**Problem:** Scene durations were hardcoded, not matched to voice timing.

### v4-synced-final.html — FINAL
Duration-matched version. Used ffprobe to measure each voice section's exact duration, then set each scene's display time to match.

## Rendering Pipeline

```
HTML5 Canvas → Puppeteer (frame screenshots at 30fps) → FFmpeg (encode frames to H.264)
```

```bash
# Puppeteer renders frames
node render.js  # screenshots to frames-v4/frame_00000.png through frame_NNNNN.png

# FFmpeg encodes
ffmpeg -framerate 30 -i frames-v4/frame_%05d.png -c:v libx264 -preset fast -crf 23 -pix_fmt yuv420p output.mp4
```

## Scene Map (v4-synced — 9 scenes)

| Scene | Timestamp | Duration | Visual |
|-------|-----------|----------|--------|
| 1-hook | 0:00-0:07 | 7.4s | "Brain Dump" title card, gradient BG, brain emoji |
| 2-intro | 0:07-0:23 | 15.8s | iPhone Spotlight → Shortcuts library screenshots |
| 3-dictate | 0:23-0:54 | 31.4s | Shortcuts editor showing Dictate Text action |
| 4-timestamp | 0:54-1:36 | 42.5s | Current Date + Format Date actions, yyyy-MM-dd-HHmm overlay |
| 5-save | 1:36-2:14 | 37.9s | Save File action, iCloud/journal_inbox config |
| 6-rename | 2:14-2:59 | 44.7s | 7-step checklist with animated checkmarks |
| 7-demo | 2:59-3:36 | 37.3s | 4-part demo: library → recording → notification → Files result |
| 8-tips | 3:36-4:17 | 41.0s | 3 tip cards: Home Screen, Siri, AI Agent pipeline |
| 9-cta | 4:17-4:34 | 16.4s | PatchMyDay outro, subscribe prompt |
