---
layout: default
title: "The Oracle's Chamber"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 7
permalink: /day2/oracles-chamber/
---

# The Oracle's Chamber

<div data-room-id="d2-oracles-chamber"></div>

*The Oracle speaks in tokens. You ask, it answers — but only as precisely as your question allows. Today you ask it one thing: who signed this filing, and in what capacity? The answer is in the document. The Oracle's job is to find it. Your job is to frame the question correctly.*

---

## Main Quest

{: .important }
> **Quest:** Write a Python script that loads one SEC Form 3 filing and uses the Stanford AI Playground to extract the insider's name and role.

**Download a sample filing:**

```bash
# A sample SEC Form 3 is available in the course repo
ls ~/rf_bootcamp_2026/data/sec_filings/
# You should see one or more .txt files
```

**Write the extraction script:**

```python
from dotenv import load_dotenv
import os
import openai

load_dotenv()

client = openai.OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)

# Load the filing
with open("data/sec_filings/form3_sample.txt", "r") as f:
    filing_text = f.read()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a financial data extraction assistant. Extract information precisely and concisely."
        },
        {
            "role": "user",
            "content": f"""From this SEC Form 3 filing, extract:
1. The insider's full name
2. Their role/relationship to the issuer (e.g. Director, Officer, 10% Owner)

Reply with only: NAME | ROLE

Filing:
{filing_text[:4000]}"""
        }
    ]
)

print(response.choices[0].message.content)
```

Notice the `[:4000]` slice — models have context limits. For now we stay within budget; Day 3 will handle hundreds of filings.

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="main"> Main Quest complete</label>

---

## Chests

{: .chest }
> **Chest 1 — Model Mirror:** Run the same extraction prompt with two different models available in the Playground (e.g. `gpt-4o-mini` and `gpt-4o`). Compare the outputs for accuracy and response time. When is the cheaper model good enough?

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="chest1"> Model Mirror unlocked</label>

{: .chest }
> **Chest 2 — Stream Stone:** Modify your script to use streaming responses (`stream=True`). Print each chunk as it arrives. When would streaming improve the user experience in a real research tool?

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="chest2"> Stream Stone unlocked</label>

{: .chest }
> **Chest 3 — Async Arrow:** Rewrite the extraction to use `asyncio` and `AsyncOpenAI` to process 5 filings concurrently. How much faster is it than sequential calls?

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="chest3"> Async Arrow unlocked</label>

---

## Weapons Earned

{: .weapon }
> **Model Mirror** — compare model outputs for accuracy and cost; choose a model intentionally based on the task, not the default.
>
> **Stream Stone** — streaming API responses for interactive tools and long completions where you don't want to wait for the full response.
>
> **Async Arrow** — `asyncio` + `AsyncOpenAI` for concurrent API calls; turn sequential N-second waits into N/10-second batches.

---

## Skills Learned

- Call the Stanford AI Playground (OpenAI-compatible) from Python
- Write an effective extraction prompt with a system message and structured output format
- Understand the context window constraint and how to work within it
- Compare models by output quality and latency for a specific task
