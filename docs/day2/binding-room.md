---
layout: default
title: "The Binding Room"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 9
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
