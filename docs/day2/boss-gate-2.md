---
layout: default
title: "Boss Gate 2"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 11
permalink: /day2/boss-gate-2/
---

# Boss Gate 2

*The Alchemist's seal. It will not open for a theory of how you would have extracted the data. It opens only when the data is real, structured, and committed.*

---

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

{: .tip }
> Use your Pydantic model from The Binding Room. If you haven't opened that chest yet, now is a good time.

---

<label class="quest-check"><input type="checkbox" data-room="d2-boss-gate" data-key="commit"> Committed and pushed `results/mood_ring.json`</label>

---

## Skills This Gate Tests

- Load a `.env` file and call the Stanford AI Playground from Python
- Write an effective extraction prompt and validate the response with Pydantic
- Loop over a directory of files and accumulate results
- Save structured output as JSON and commit to your fork
