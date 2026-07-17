---
layout: default
title: "The Oracle's Chamber"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 6
permalink: /day2/oracles-chamber/
---

# The Oracle's Chamber

<div data-room-id="d2-oracles-chamber"></div>

*Deep in the Alchemist's Lab, behind a door carved with question marks, sits the Oracle — a mind made of weights and probabilities, ancient knowledge compressed into a single blazing point. It does not volunteer answers. It responds to invocations. You have one question burning in your hand: who signed this filing, and in what capacity? Frame it perfectly, and the Oracle will reach into a dense forest of regulatory text and hand you the name. Frame it poorly, and you get noise. The difference between the two is a few well-chosen words — and you are about to learn exactly which ones.*

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Make your first live API call, then use the Stanford AI Playground to extract structured information from a real SEC Form 3 filing — and save the logic to a standalone Python script.

---

### Step 1 — Open the Oracle's Notebook

Every invocation in this room happens in one notebook. In JupyterHub (on the Yens), open your `day2/` folder and create a **new notebook named `oracle.ipynb`**. From the kernel menu in the top-right, choose **Bootcamp 2026** — the kernel you forged in [The Venv Forge](../venv-forge/).

{: .important }
> Selecting the **Bootcamp 2026** kernel is what gives this notebook its reagents — `openai`, `python-dotenv`, and `pydantic` — the packages you installed into that venv. If the imports in the next step fail with `ModuleNotFoundError`, the wrong kernel is almost always the culprit: check the kernel name shown in the notebook's top-right corner.

Every code cell below runs in `oracle.ipynb` unless it says otherwise.

---

### Step 2 — Hello World (Exercise 4.2)

With your `.env` loaded and the OpenAI client initialized, confirm the API works:

```python
from dotenv import load_dotenv
import os
import openai

load_dotenv()

client = openai.OpenAI(
    api_key=os.environ["STANFORD_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)

completion = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello world!"}
    ]
)

print(completion.choices[0].message.content)
```

If you see a response, the API is working.

---

### Step 3 — Load and Inspect a SEC Filing (Exercise 4.3)

A sample SEC Form 3 filing is included in your course repo:

```bash
ls ~/rf-bootcamp-2026/data/sec_filings/
```

You should see one or more `.txt` files. Load it in `oracle.ipynb` and take a look:

```python
with open("data/sec_filings/Cheniere_Energy_Inc.txt", "r") as f:
    filing_text = f.read()

print(filing_text[:2000])   # preview the first 2000 characters
```

SEC Form 3 filings report an insider's financial interest in a company — their name, role, and any shares held. The format is dense and not consistently structured. This is where the Oracle earns its keep.

---

### Step 4 — Extract Information with the API

Now ask the model to pull out the key fields:

```python
response = client.chat.completions.create(
    model="gpt-4.1-nano",
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

{: .note }
> 💡 The `[:4000]` slice limits how much text you send — models have context limits. For now we stay within budget; Day 3 will scale this to hundreds of filings.

Experiment: try changing the system prompt. What happens if you ask for more fields? What if the prompt is vague?

---

### Step 5 — From Notebook to Script (Exercise 4.4)

A notebook is great for exploration. Once the logic works, move it to a standalone script.

In `oracle.ipynb`, consolidate the working code into one cell:

```python
from dotenv import load_dotenv
import os
import openai

load_dotenv()

client = openai.OpenAI(
    api_key=os.environ["STANFORD_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)

with open("data/sec_filings/Cheniere_Energy_Inc.txt", "r") as f:
    filing_text = f.read()

response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {"role": "system", "content": "You are a financial data extraction assistant. Extract information precisely and concisely."},
        {"role": "user", "content": f"Extract the insider's name and role. Reply with: NAME | ROLE\n\n{filing_text[:4000]}"}
    ]
)

print(response.choices[0].message.content)
```

Copy this into a new file called `form3_test.py` (create it in the Jupyter terminal: `touch form3_test.py`).

Run it from the terminal:

```bash
cd ~/rf-bootcamp-2026
python form3_test.py
```

Verify you get the same output as the notebook. You now have a reproducible script you can schedule, share, or scale.

---

### Step 6 — Validate with Pydantic

The API returns a string. Pydantic turns it into a typed, validated Python object — and rejects responses that don't match your schema.

Define a model:

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

Ask for structured JSON output:

```python
response = client.chat.completions.create(
    model="gpt-4.1-nano",
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

If the model returns a field that doesn't match the schema (wrong type, missing required field), `model_validate_json` raises a `ValidationError` — catching that error is how you know something went wrong before you scale to 10,000 filings.

Update your `form3_test.py` script to use the Pydantic model and save the output as JSON.

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="main"> Main Quest complete</label>

---

## 🧠 Skills Learned

- The OpenAI-compatible API takes a list of messages with `role` (system/user/assistant) and `content` (the text)
- The system prompt frames what the model is and what it should do; the user prompt is the actual data
- Context limits mean you need to trim large documents before sending — `[:4000]` is a quick safeguard
- Pydantic models turn unstructured LLM output into typed, validated Python objects — if the model returns garbage, you catch it before it silently corrupts your dataset
- A notebook is for exploration; a `.py` script is for reproducibility
