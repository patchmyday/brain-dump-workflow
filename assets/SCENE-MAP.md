# Scene Map — Brain Dump Workflow Video #1

Each row maps a script section to its visual scene, source files, and render method.

| # | Timestamp | Script Section | Visual Description | Render Method | Duration |
|---|-----------|---------------|-------------------|---------------|----------|
| 1 | 0:00-0:07 | Hook | "Brain Dump" title card with brain emoji, gradient BG, animated text | HTML5 Canvas | 7.4s |
| 2 | 0:07-0:23 | Intro | iPhone Spotlight search → Shortcuts app → library showing shortcuts list | Screenshots + Ken Burns | 15.8s |
| 3 | 0:23-0:54 | Build: Dictate | Two iPhone screenshots: Shortcuts editor showing "Dictate Text" action with annotations | Screenshots composite | 31.4s |
| 4 | 0:54-1:36 | Build: Timestamp | Shortcuts editor showing Current Date + Format Date actions, "yyyy-MM-dd-HHmm" overlay | Screenshots + text overlay | 42.5s |
| 5 | 1:36-2:14 | Build: Save | Shortcuts editor showing Save File action with iCloud/journal_inbox config, annotations | Screenshots + annotations | 37.9s |
| 6 | 2:14-2:59 | Build: Rename + Notify | iPhone showing completed 7-step shortcut + animated checkmark list | Screenshots + Canvas checklist | 44.7s |
| 7 | 2:59-3:36 | Demo | 4-part demo sequence: library tap → recording UI → notification → Files app result | Screenshots sequence | 37.3s |
| 8 | 3:36-4:17 | Power Tips | 3 tip cards: Home Screen icon, Siri voice, AI Agent pipeline diagram | HTML5 Canvas cards | 41.0s |
| 9 | 4:17-4:34 | CTA | PatchMyDay outro with subscribe prompt, brain emoji, gradient BG | HTML5 Canvas | 16.4s |

## Total Duration: 4:34 (274s)

## Scene Source Files

```
content-engine/output/brain-dump-workflow/
├── scenes/
│   ├── 01-hook/           # HTML5 Canvas title card
│   ├── 02-intro/          # iPhone screenshots
│   ├── 03-dictate/        # Shortcuts editor screenshots
│   ├── 04-timestamp/      # Format date screenshots + overlay
│   ├── 05-save/           # Save file screenshots
│   ├── 06-rename/         # Checklist animation
│   ├── 07-demo/           # Demo sequence screenshots
│   ├── 08-tips/           # Tip card animations
│   └── 09-cta/            # Outro animation
```
