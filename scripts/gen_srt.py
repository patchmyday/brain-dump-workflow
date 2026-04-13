import sys, os
os.chdir("/root/content-engine/output/brain-dump-workflow")
print("Importing...", flush=True)
from faster_whisper import WhisperModel
print("Loading tiny model...", flush=True)
model = WhisperModel("tiny", device="cpu", compute_type="int8")
print("Model loaded!", flush=True)

def fmt(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = int((t % 1) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def segments_to_srt(segments, output_path):
    srt_entries = []
    idx = 1
    for seg in segments:
        text = seg.text.strip()
        if not text:
            continue
        srt_entries.append(f"{idx}\n{fmt(seg.start)} --> {fmt(seg.end)}\n{text}\n")
        idx += 1
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(srt_entries))
    print(f"Wrote {idx-1} subtitles to {output_path}", flush=True)

print("Transcribing EN...", flush=True)
segs, info = model.transcribe("audio-v3/full-voiceover-v3-en-final.mp3")
segs = list(segs)
print(f"EN done: {len(segs)} segments", flush=True)
segments_to_srt(segs, "audio-v3/subtitles-en.srt")

print("Transcribing CN...", flush=True)
segs2, info2 = model.transcribe("audio-v3/full-voiceover-v3-cn.mp3", language="zh")
segs2 = list(segs2)
print(f"CN done: {len(segs2)} segments", flush=True)
segments_to_srt(segs2, "audio-v3/subtitles-cn.srt")

print("ALL_DONE", flush=True)
