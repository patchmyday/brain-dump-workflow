# Brain Dump Workflow — Full Script (EN)

**Duration:** 4:34 | **Word count:** ~1,100 | **Voice:** ElevenLabs Adam

---

## 1. Hook (0:00 - 0:07)

Your best ideas happen in the shower and die before you sit down. Let's fix that in 10 seconds with something already on your phone.

## 2. Intro (0:07 - 0:23)

This is Brain Dump, a single iPhone shortcut — tap it, talk, and it saves a timestamped Markdown file straight to iCloud. No app, no subscription, no sign-up. Just the Shortcuts app you've been ignoring since 2018. Let's build it from zero, right now.

## 3. Build: Dictate Text (0:23 - 0:54)

New shortcut, tap the plus, search "Dictate Text," add it. This fires up your mic and transcribes everything you say in real time. Here's the thing — under "Stop Listening," set it to "After Pause." That means it records until you stop talking. 5 seconds, fine. 5 minutes, also fine. It just waits. Rename the shortcut "Brain Dump" at the top. Throw a brain emoji on there because we're adults.

## 4. Build: Timestamp (0:54 - 1:36)

Okay, so now we have raw text. But raw text with no timestamp is a junk drawer. Let's fix that. Next, add "Current Date." This grabs the exact moment you run the shortcut. But the default format is not great for file names. So right below it, add "Format Date." Switch from "Short" to "Custom" and type this exact string: yyyy-MM-dd-HHmm. That's the format string. Look, I know that sounds like a regex incantation. But it gives you year-month-day-hour-minute. Clean, sortable. Obsidian-friendly. If your preview says something like 2026-04-10-1131, you nailed it. This becomes your file name. Don't skip it.

## 5. Build: Save File (1:36 - 2:14)

Now we build the file body. Add a Text action, tap inside. Grab "Dictated Text" from the variables bar. That blue pill? That's everything you said. Transcribed in one block. Done. Now, Save File. Set the destination to iCloud Drive. I put mine in a folder called journal_inbox. Think of it as a landing zone. Raw brain dumps pile up here until you process them. Folder doesn't exist yet? Doesn't matter. Shortcuts creates it on first run. Here's the key move — toggle off "Ask Where to Save." You want zero friction. Tap, talk, done. No dialogs, no decisions.

## 6. Build: Rename + Notification (2:14 - 2:59)

Almost there. Add Rename, because text.txt tells you nothing six months from now. Set input to Saved File. For the name, grab your Formatted Date variable, then type -braindump.md. So you get something like 2026-04-10-1131-braindump.md. Beautiful. That .md extension means Obsidian, Notion, any text editor — they all love it. Last action: Show Notification. Title: "Brain Dump Saved." Body: drop that same Formatted Date variable. This is your dopamine hit. The little ping that says, "yeah, it worked." Seven actions total. That's the whole shortcut. If you can order DoorDash, you can build this.

## 7. Demo (2:59 - 3:36)

Let's run it. Tap Brain Dump. Mic goes hot, talk. "Idea for PatchMyDay — video on AI agents that process journal entries and extract action items." I stop talking and it stops listening. Bam — notification: Brain Dump Saved. Okay, let's verify. Files app. iCloud Drive → Shortcuts → journal_inbox. There it is. Tap it open — exact transcription. Already in iCloud. Already synced to my Mac. Already visible in Obsidian. Look at that timer. 10 seconds from thought to saved file. You never opened an app. Never typed a character, you just talked.

## 8. Power Tips (3:36 - 4:17)

Three power moves, rapid fire. One — long press the tile, Add to Home Screen. Now it's a one-tap icon on your dock. I keep mine next to the camera. It's that useful. Two — say "Hey Siri, Brain Dump." It fires hands-free. Perfect for driving. You literally never touch the phone. Three — and this is where it gets spicy. That journal_inbox folder? It's just a directory on iCloud. Which means you can point a Python script at it. An AI agent, a cron job that runs every night, reads your dumps, extracts action items, drops the summary into your task manager. That's not hypothetical. That's what I'm building next.

## 9. CTA (4:17 - 4:34)

Seven actions, $0, your ideas stop disappearing. Next video, I'm building the AI agent that actually reads these brain dumps and files action items into a task board automatically. It's half done, and it's kind of terrifying how well it works. Subscribe so you don't miss it. See you in that one.
