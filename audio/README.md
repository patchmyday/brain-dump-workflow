# Voice Production

## ElevenLabs Config

- **Voice:** Adam
- **Model:** Multilingual v2
- **Plan:** Creator tier (121 credits/mo)

## 3 Iterations

### v1 (audio/)
Voice tests with 4 different voices (Brian, Chris, Eric, Liam) using v1 script.
Selected Adam. Generated 9 sections + .ogg variants.

### v2 (audio-v2/)
Regenerated with v2 (Fireship-rewrite) script. Both EN and CN.

### v3 (audio-v3/) — FINAL
Final generation. Tested yunyang voice for CN. Multiple mix versions:
- Raw voice → tempo-adjusted → mixed with background music → final

## Section Split Strategy

Each script section is generated as a separate MP3. This allows:
1. Re-generating one bad section without redoing everything
2. Measuring exact duration per section for scene sync
3. Easy reordering if structure changes

## Concat Command

```bash
# EN example
ffmpeg -f concat -safe 0 -i concat-en.txt -c copy full-voiceover.mp3
```

## Audio files not in repo (too large)

The actual .mp3 files are in `/root/content-engine/output/brain-dump-workflow/audio-v3/` on the production server. This repo only has the concat manifests and configs.
