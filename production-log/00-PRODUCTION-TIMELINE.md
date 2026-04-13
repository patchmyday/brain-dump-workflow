# Production Timeline — Brain Dump Workflow Video

This is the actual sequence of events, not a template. Every iteration, dead end, and fix.

## Phase 0: Concept (User Input)

Jason uploaded iPhone screenshots of his Brain Dump shortcut:
- Shortcuts library showing the "Brain Dump" shortcut with brain emoji
- Shortcuts editor showing all 7 actions
- Dictate Text action config (Stop Listening: After Pause)
- Format Date action with yyyy-MM-dd-HHmm
- Save File action pointing to iCloud/journal_inbox
- Demo: notification "Brain Dump Saved"
- Demo: Files app showing the saved .md file

Also shared a LottieFiles screenshot — wanted fun monster characters in the video.

## Phase 1: Script Writing

### v1 Script (audio/sections.json)
- More formal, tutorial-style ("I'm Jason from PatchMyDay...")
- 9 sections, ~6 minutes estimated
- Voice: tested Brian, Chris, Eric, Liam voices
- **Problem:** Too long, too "YouTuber intro" energy

### v2 Script (youtube-script-v2.md + script-v2-sections.json)
- Fireship-style rewrite — punchy, fast, personality
- Same 9 sections but tighter (~4:30)
- Added humor: "because we're adults", "sounds like a regex incantation", "order DoorDash"
- **This became the final script**

### CN Script (script-cn-sections.json + script-cn-voiceover.json)
- Full Chinese translation adapted for 小红书 audience
- Not a literal translation — rewritten for Chinese internet culture
- 8 sections (combined some for pacing)

## Phase 2: Voice Generation (3 iterations)

### audio/ (v1)
- First attempt with ElevenLabs
- Tested 4 voices: Brian, Chris, Eric, Liam
- Selected voice, generated all 9 sections
- Created concat.txt, built full-voiceover.mp3
- Also generated .ogg versions

### audio-v2/
- Regenerated with v2 script (Fireship rewrite)
- Both EN and CN sections generated
- Created separate concat files for each language
- Built full-voiceover-v2-en.mp3 and full-voiceover-v2-cn.mp3

### audio-v3/ (FINAL)
- Third generation pass
- Tested yunyang voice for CN (test-yunyang-01.mp3)
- Generated final EN and CN sections
- Created multiple mix versions:
  - full-voiceover-v3-en.mp3 (raw voice)
  - full-voiceover-v3-en-fast.mp3 (tempo adjusted)
  - full-voiceover-v3-en-mixed.mp3 (voice + background music)
  - full-voiceover-v3-en-final.mp3 (final mix)
- Generated subtitles via Whisper:
  - subtitles-en.srt (later proofread — 15 corrections)
  - subtitles-cn.srt

## Phase 3: Visual Production (4 iterations)

### v1: Manim (animation.py → animation_full.mp4)
- Python Manim script with 3 scenes: BrainDumpIntro, WorkflowDiagram, BeforeAfterScene
- Generated SVG text elements in media/texts/
- Rendered at 480p15
- **Abandoned:** Too limited for the visual style wanted, slow to iterate

### v2-lottie: HTML5 Canvas + Lottie (animation-v2-lottie.html → brain-dump-v2-lottie.mp4)
- Switched to HTML5 Canvas rendered via Puppeteer
- Integrated LottieFiles character animations
- More visually fun but still generic
- Also created vertical version (animation-vertical.html → motion_canvas_vertical.mp4)

### v3-screenshots: Real Screenshots (animation-v3-screenshots.html → brain-dump-v3-screenshots.mp4)
- Composited Jason's actual iPhone screenshots into scenes
- Each scene showed the real Shortcuts editor UI
- Much more authentic and useful as a tutorial
- **Problem:** Scenes not synced to voice — visual sections didn't match audio timing

### v4-synced: Duration-Matched (animation-v4-synced.html → brain-dump-v4-synced.mp4)
- Measured each voice section's exact duration with ffprobe
- Set each scene's display time to match its voice section
- Rendered via Puppeteer frame-by-frame, then FFmpeg encoded
- 275 seconds render time, 1920x1080
- **This became the final video base**

## Phase 4: Assembly

### final-en.mp4 (v1)
- First assembly: v1 animation + v1 voice

### final-en-v2.mp4
- Updated with v2 script voice
- Also: final-en-v2-compressed.mp4, final-en-v2-sm.mp4 (size variants)

### final-cn.mp4 + final-cn-v2.mp4
- Chinese versions with CN voice
- final-cn-v2-sm.mp4 for Telegram delivery

### final-en-v4-synced.mp4 (21MB, 1080p)
- v4-synced video + v3 audio + background music + subtitles
- First properly synced version
- final-en-v4-synced-720p.mp4 (6MB) for Telegram

### final-en-v5-proofread.mp4 (FINAL)
- **Bug:** v4-synced already had subs burned in. Burning corrected subs created DOUBLE subtitles
- **Fix:** Used brain-dump-v4-synced.mp4 (clean, no subs) as base, burned only corrected SRT
- 15 subtitle corrections applied (see subtitles/PROOFREAD-LOG.md)
- final-en-v5-proofread-720p.mp4 (6.3MB) — delivered to Telegram

## Phase 5: Xiaohongshu Content

- xiaohongshu-post.md — Full 小红书 graphic text post with slide-by-slide layout
- xiaohongshu-script-v2.md — Adapted Chinese script for short-form
