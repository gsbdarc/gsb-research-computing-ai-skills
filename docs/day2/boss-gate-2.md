---
layout: default
title: "Boss Gate 2"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 8
permalink: /day2/boss-gate-2/
---

# Boss Gate 2

*The Alchemist's seal is cold iron and older magic — it has heard every excuse, every "I would have," every "it almost worked." It does not open for intentions. It opens when the data flows, the schema holds, and five transcripts lie structured and committed on the other side. Prove you have mastered the Lab. The seal is watching.*

---

## 🔑 The Challenge

The boss doesn't care about your plan — only your output. Five transcripts, five verdicts, one clean JSON file. Show your work.

{: .boss }
> **Boss Battle — The Mood Ring Scroll**
>
> Five earnings call transcripts are waiting in the course repo at `data/earnings_calls/`. For each transcript:
>
> 1. Call the Stanford AI Playground to extract a **sentiment** (`positive`, `neutral`, or `negative`) and a one-sentence **summary** of management's tone
> 2. Store the result as a validated Pydantic model
> 3. Write all five results to `results/mood_ring.json` (a JSON array)
>
> Your final `mood_ring.json` should look like:
> ```json
> [
>   {"filename": "call_001.txt", "sentiment": "positive", "summary": "Management expressed..."},
>   ...
> ]
> ```
>
> **Submit:**
> ```bash
> git add results/mood_ring.json
> git commit -m "Boss Gate 2: Mood Ring Scroll complete"
> git push
> ```

💡 Use your Pydantic model from The Binding Room. If you haven't completed that side quest yet, now is a good time.
{: .tip }

---

<label class="quest-check"><input type="checkbox" data-room="d2-boss-gate" data-key="commit"> Committed and pushed `results/mood_ring.json`</label>

---

## 📊 End of Day 2 — Sync Your Progress

Let your instructor see where you landed today. Takes 2 minutes.

**Step 1 — Export your quest log**

Click **"📤 Sync to leaderboard"** in the bottom-left corner of this page. A file called `quest_log.json` downloads to your laptop.

**Step 2 — Upload it to your fork**

Go to your fork on GitHub (`github.com/YOUR_USERNAME/rf-bootcamp-2026`) → **Add file → Upload files** → drag `quest_log.json` in → **Commit changes** to `main`.

The leaderboard updates within 2 minutes. Your instructor can see your level, which boss gates you've cleared, and how many side quests you completed.

---

## ⚔️ Skills This Gate Tests

- You can now load secrets from a `.env` file and fire live API calls to the Stanford AI Playground from Python
- You can now craft extraction prompts that coerce an LLM's free-form reply into a validated, typed Pydantic model
- You can now loop over a directory of raw files and accumulate structured results without losing a single record
- You can now serialize a typed Python object to clean JSON and commit it as reproducible, auditable output
