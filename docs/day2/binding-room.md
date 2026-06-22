---
layout: default
title: "The Binding Room"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 8
permalink: /day2/binding-room/
---

# The Binding Room

<div data-room-id="d2-binding-room"></div>

*The Oracle speaks in riddles and prose — beautiful, unpredictable, and utterly untrustworthy as raw data. The Binding Room is where chaos gets a spine. Here, you inscribe a Pydantic model: a contract carved in stone that declares "a string lives here, an integer stands there, and these fields are non-negotiable." When the Oracle returns something that breaks the contract, the Binding Room slams the door and demands a better answer — automatically, without you lifting a finger.*

---

## 🗡️ Main Quest

Your target: a real SEC Form 3 filing, full of names and dates buried in unstructured text. You will forge a model that pulls exactly what you need — typed, validated, and ready to analyze.

{: .important }
> **Quest:** Define a Pydantic model for SEC Form 3 data and use structured output to extract it reliably from a filing.

**Install Pydantic (already in your venv):**
```bash
pip install pydantic   # already installed if you followed Venv Forge
```

**Define the model:**

```python
from pydantic import BaseModel
from typing import Optional

class Form3Extraction(BaseModel):
    insider_name: str
    role: str
    issuer_name: str
    transaction_date: Optional[str] = None
    shares_acquired: Optional[int] = None
```

**Extract with structured output:**

```python
from dotenv import load_dotenv
import os
import openai
import json

load_dotenv()

client = openai.OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)

with open("data/sec_filings/form3_sample.txt", "r") as f:
    filing_text = f.read()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Extract the requested fields from this SEC Form 3 filing. Return only valid JSON matching the schema provided."},
        {"role": "user", "content": f"Extract from this filing:\n\n{filing_text[:4000]}"}
    ],
    response_format={"type": "json_object"},
)

raw = response.choices[0].message.content
data = Form3Extraction.model_validate_json(raw)
print(data.model_dump_json(indent=2))
```

<label class="quest-check"><input type="checkbox" data-room="d2-binding-room" data-key="main"> Main Quest complete</label>

---

## 📦 Chests

Three sealed chests line the walls, each one holding a technique that separates brittle pipelines from bulletproof ones. Crack them open.

{: .chest }
> **Chest 1 — Nested Tome:** Add a nested `Transaction` model to `Form3Extraction` to hold `date`, `shares`, and `price_per_share`. A filing can have multiple transactions — make the field a `List[Transaction]`. Test it on a filing with multiple transaction rows.

<label class="quest-check"><input type="checkbox" data-room="d2-binding-room" data-key="chest1"> Nested Tome unlocked</label>

The Oracle isn't always cooperative — sometimes it hands back mangled JSON that crashes your pipeline at 2am. This chest teaches you to expect that and fight back.

{: .chest }
> **Chest 2 — Retry Rune:** The model sometimes returns malformed JSON. Add a retry loop: if `model_validate_json` raises a `ValidationError`, log the error and retry the API call up to 3 times. Print a warning after the final failure.

<label class="quest-check"><input type="checkbox" data-room="d2-binding-room" data-key="chest2"> Retry Rune unlocked</label>

Why describe a schema in plain English when you can hand the Oracle the exact specification? This chest unlocks a trick that makes model compliance measurably better.

{: .chest }
> **Chest 3 — Schema Shield:** Export your Pydantic model's JSON schema with `Form3Extraction.model_json_schema()` and include it in the system prompt instead of a free-text description. Does the model follow the schema more reliably?

<label class="quest-check"><input type="checkbox" data-room="d2-binding-room" data-key="chest3"> Schema Shield unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Nested Tome** — nested Pydantic models and `List[Model]` fields for complex structured extraction; model real-world data that doesn't fit a flat schema.
>
> **Retry Rune** — validation error handling with automatic retry; make LLM pipelines robust to malformed outputs without manual intervention.
>
> **Schema Shield** — export Pydantic JSON schema into the system prompt; give the model an explicit contract instead of hoping it infers the structure.

---

## 🧠 Skills Learned

- You can now define a Pydantic model that pins down exactly what an LLM must return — types, required fields, and all
- You can use `response_format: json_object` and `model_validate_json` to get structured, validated data instead of raw text you have to parse yourself
- You can build retry logic that catches `ValidationError` and automatically re-prompts the model, so one bad response doesn't sink your whole pipeline
- You understand why structured output beats free-text parsing every time: real Python types, automatic validation, and IDE autocomplete that actually works
