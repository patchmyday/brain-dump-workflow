# Phase 3: Visual Production

## Scene Types

### 1. Screenshot Scenes (Simplest)
iPhone/app screenshots with Ken Burns zoom/pan effects.

```bash
# Ken Burns zoom on a screenshot (5 seconds, zoom from 100% to 120%)
ffmpeg -loop 1 -i screenshot.png -vf "
  zoompan=z='min(zoom+0.002,1.2)':d=150:s=1920x1080:fps=30,
  format=yuv420p" -t 5 -c:v libx264 -pix_fmt yuv420p scene.mp4
```

### 2. HTML5 Canvas Animations
For title cards, checklists, tip cards, overlays.

**Workflow:**
1. Create HTML file with Canvas/CSS animation
2. Render to video via Puppeteer screenshot sequence
3. FFmpeg encode frames to video

```javascript
// Example: Puppeteer render script
const browser = await puppeteer.launch({args: ['--no-sandbox']});
const page = await browser.newPage();
await page.setViewport({width: 1920, height: 1080});
await page.goto('file:///path/to/scene.html');
// Screenshot each frame at 30fps
for (let i = 0; i < totalFrames; i++) {
  await page.evaluate(`window.setFrame(${i})`);
  await page.screenshot({path: `frames/frame_${i.toString().padStart(5,'0')}.png`});
}
```

### 3. Manim Animations
For technical/mathematical visualizations.

```python
from manim import *
class MyScene(Scene):
    def construct(self):
        title = Text("Brain Dump Workflow", font_size=48)
        self.play(Write(title))
```

### 4. Screen Recordings
For live demos. Record on iPhone, transfer via AirDrop/iCloud.

### 5. Lottie Animations
Download from LottieFiles.com, render via lottie-web or Puppeteer.

## Scene Sync Strategy

Each scene must match its voiceover section duration exactly.

```
Voice section: 03-build-dictate-en.mp3 → 28.56 seconds
Scene video:   scene-03-dictate.mp4    → 28.56 seconds (pad/trim to match)
```

### Duration Matching

```bash
# Get audio duration
ffprobe -v error -show_entries format=duration -of csv=p=0 section.mp3

# Render scene to exact duration
ffmpeg -loop 1 -i image.png -t $DURATION -vf "scale=1920:1080" -c:v libx264 scene.mp4
```

## Concatenation

```bash
# Create scene list matching voice order
cat > scenes.txt << 'EOF'
file 'scene-01-hook.mp4'
file 'scene-02-intro.mp4'
file 'scene-03-dictate.mp4'
...
EOF

ffmpeg -f concat -safe 0 -i scenes.txt -c:v libx264 -preset fast scenes-full.mp4
```

## Color Palette (PatchMyDay Brand)

| Element | Color | Hex |
|---------|-------|-----|
| Background (dark) | Near black | #1a1a2e |
| Accent (primary) | Electric blue | #00d4ff |
| Accent (secondary) | Lime green | #00ff88 |
| Text | White | #ffffff |
| Subtitle outline | Black | #000000 |
