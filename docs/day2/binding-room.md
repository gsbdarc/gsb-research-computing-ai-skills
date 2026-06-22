---
layout: default
title: "The Binding Room"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 8
permalink: /day2/binding-room/
---

# The Binding Room

<div data-room-id="d2-binding-room"></div>

*The Oracle speaks in prose. The Binding Room turns prose into structure. A Pydantic model is a contract: "give me a string here, an integer there, and these fields are required." When the Oracle violates the contract, the Binding Room rejects the answer and asks again — automatically.*

---

## Main Quest

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

## Chests

{: .chest }
> **Chest 1 — Nested Tome:** Add a nested `Transaction` model to `Form3Extraction` to hold `date`, `shares`, and `price_per_share`. A filing can have multiple transactions — make the field a `List[Transaction]`. Test it on a filing with multiple transaction rows.

<label class="quest-check"><input type="checkbox" data-room="d2-binding-room" data-key="chest1"> Nested Tome unlocked</label>

{: .chest }
> **Chest 2 — Retry Rune:** The model sometimes returns malformed JSON. Add a retry loop: if `model_validate_json` raises a `ValidationError`, log the error and retry the API call up to 3 times. Print a warning after the final failure.

<label class="quest-check"><input type="checkbox" data-room="d2-binding-room" data-key="chest2"> Retry Rune unlocked</label>

{: .chest }
> **Chest 3 — Schema Shield:** Export your Pydantic model's JSON schema with `Form3Extraction.model_json_schema()` and include it in the system prompt instead of a free-text description. Does the model follow the schema more reliably?

<label class="quest-check"><input type="checkbox" data-room="d2-binding-room" data-key="chest3"> Schema Shield unlocked</label>

---

## Weapons Earned

{: .weapon }
> **Nested Tome** — nested Pydantic models and `List[Model]` fields for complex structured extraction; model real-world data that doesn't fit a flat schema.
>
> **Retry Rune** — validation error handling with automatic retry; make LLM pipelines robust to malformed outputs without manual intervention.
>
> **Schema Shield** — export Pydantic JSON schema into the system prompt; give the model an explicit contract instead of hoping it infers the structure.

---

## Skills Learned

- Define a Pydantic model to describe the structure you expect from an LLM
- Use `response_format: json_object` and `model_validate_json` for typed, validated extraction
- Understand that LLMs sometimes violate output formats — build retry logic into the pipeline
- Know why structured output is always better than parsing free text: types, validation, IDE support
