---
layout: default
title: "Boss Gate 2"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 8
permalink: /day2/boss-gate-2/
---

# Boss Gate 2

*The Alchemist's seal is cold iron and older magic. It has heard every excuse, every "I would have," every "it almost worked." It does not open for intentions. This time it demands not one oracle but two minds in dialogue: an apprentice who dares to name a thing, and a master who judges the naming and says, plainly, how sure they are. Bring both. Log their verdicts. Commit the scroll. The seal is watching.*

---

## 🔑 The Challenge

The boss doesn't care about your plan, only your output. Ten films, two models, one honest verdict for each, and a clear mark on the ones a human should double-check.

{: .boss }
> **Boss Battle: The Genre Tribunal**
>
> The course repo ships a dataset at `data/top_rated_movies.csv`. It has `id`, `title`, `overview`, and more, but **no genre column**. That is the point: you are going to derive the genre, then judge your own derivation.
>
> For the **first 10 movies** in the file:
>
> 1. **Classify** (the apprentice): send the movie's `overview` to the model and have it pick the single best-fitting **genre** from the list below.
> 2. **Judge** (the master): send the `overview` *and* the predicted genre to the model again, and have it return whether it **agrees**, a **certainty** from 0 to 100, and a one-sentence **reason**.
> 3. **Flag** (your code, not the model): mark the movie `needs_human_review` when the judge disagrees **or** its certainty is below **70**.
> 4. Validate both model replies with **Pydantic**, and **log** your progress as you go (a `WARNING` when something gets flagged).
> 5. Write all ten results to `results/genre_verdicts.json`.
>
> **Submit:**
> ```bash
> cd ~/rf-bootcamp-2026 && source .venv/bin/activate
> python day2/genre_tribunal.py        # reads data/..., writes results/...
> git add results/genre_verdicts.json
> git commit -m "Boss Gate 2: Genre Tribunal complete"
> git push
> ```

Run it from the **repo root** (`~/rf-bootcamp-2026`) so that `data/top_rated_movies.csv` and `results/genre_verdicts.json` both resolve, and so the gate's grader finds your output.
{: .tip }

---

## 🧭 The Logical Flow

You are not writing anything you haven't already built in The Oracle's Chamber. You are *composing* two calls and one policy decision:

```text
overview ─▶ [ Classifier LLM ] ─▶ predicted_genre
                                        │
overview + predicted_genre ─▶ [ Judge LLM ] ─▶ agrees, certainty, reason
                                        │
              needs_human_review = (not agrees) or (certainty < 70)
                                        │
        append { id, title, predicted_genre, agrees, certainty, needs_human_review }
                                        ▼
                     results/genre_verdicts.json      (+ logged progress)
```

The judge only *reports* (does it agree, and how sure is it). **Your code decides the policy** (when to escalate to a human). Keeping that decision out of the prompt is what makes it auditable, the same lesson The Crucible drives home.

---

## 🎬 The Genre List

Constrain the classifier to this exact set (a Pydantic `Enum` is the clean way to reject anything off-list). `Other` is the escape hatch for a film that genuinely fits none:

```text
Action, Adventure, Animation, Comedy, Crime, Documentary, Drama, Family,
Fantasy, Horror, Mystery, Romance, Science Fiction, Thriller, War, Western, Other
```

---

## 📜 Required Output Schema

`results/genre_verdicts.json` is a JSON array, one object per movie:

```json
[
  {
    "id": 13448,
    "title": "Angels & Demons",
    "predicted_genre": "Thriller",
    "agrees": true,
    "certainty": 85,
    "needs_human_review": false,
    "reason": "The overview centers on investigation and conspiracy."
  }
]
```

Every entry must include `id`, `title`, `predicted_genre`, `certainty` (a number from 0 to 100), and `needs_human_review`. Include `agrees` and `reason` too; they make the scroll worth reading.

---

<label class="quest-check"><input type="checkbox" data-room="d2-boss-gate" data-key="commit"> Committed and pushed `results/genre_verdicts.json`</label>

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

- You can compose a **multi-stage LLM pipeline**, feeding one model's output into the next call
- You can **constrain generation** to a fixed set of labels with a Pydantic `Enum` and reject off-list replies
- You can implement an **LLM-as-a-judge** review step that reports agreement and confidence
- You can encode a **human-in-the-loop** escalation policy in *code*, not in the prompt, so it is explicit and auditable
- You can read a CSV with the standard-library `csv` module (no pandas required)
- You can separate **`logging` diagnostics** from **`print` results**, the habit that pays off when these run as cluster jobs on Day 3
- You can serialize validated verdicts to clean, committable JSON
