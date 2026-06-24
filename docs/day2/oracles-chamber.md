---
layout: default
title: "The Oracle's Chamber"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 8
permalink: /day2/oracles-chamber/
---

# The Oracle's Chamber

<div data-room-id="d2-oracles-chamber"></div>

*Deep in the Alchemist's Lab, behind a door carved with question marks, sits the Oracle — a mind made of weights and probabilities, ancient knowledge compressed into a single blazing point. It does not volunteer answers. It responds to invocations. You have one question burning in your hand: who signed this filing, and in what capacity? Frame it perfectly, and the Oracle will reach into a dense forest of regulatory text and hand you the name. Frame it poorly, and you get noise. The difference between the two is a few well-chosen words — and you are about to learn exactly which ones.*

---

## 🗡️ Main Quest

The Oracle awaits your first invocation. Open the filing, shape your prompt like a key, and watch the model pull signal from the fog.

{: .important }
> **Quest:** Write a Python script that loads one SEC Form 3 filing and uses the Stanford AI Playground to extract the insider's name and role.

**Download a sample filing:**

```bash
# A sample SEC Form 3 is available in the course repo
ls ~/rf-bootcamp-2026/data/sec_filings/
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

💡 Notice the `[:4000]` slice — models have context limits. For now we stay within budget; Day 3 will handle hundreds of filings.

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="main"> Main Quest complete</label>
