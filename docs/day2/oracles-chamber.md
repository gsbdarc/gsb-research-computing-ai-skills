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
    model="gemini-2.5-flash-lite",
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
ls ~/gsb-research-computing-ai-skills/data/sec_filings/
```

You should see one or more `.txt` files. Load it in `oracle.ipynb` and take a look:

```python
with open("../data/sec_filings/Cheniere_Energy_Inc.txt", "r") as f:
    filing_text = f.read()

print(filing_text[:2000])   # preview the first 2000 characters
```

SEC Form 3 filings report an insider's financial interest in a company — their name, role, and any shares held. The format is dense and not consistently structured. This is where the Oracle earns its keep.

---

### Step 4 — Extract Information with the API

Now ask the model to pull out the key fields:

```python
response = client.chat.completions.create(
    model="gemini-2.5-flash-lite",
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

A notebook is great for exploration. Once the logic works, move it to a standalone script, the form you'll actually schedule and run on the cluster.

One thing should change when code leaves the notebook: how it reports progress. In a notebook you watch cell output live. A script often runs unattended (in the background, or as a cluster job whose output you read afterward), so instead of scattering `print()` calls for status, use Python's built-in **`logging`** library. It stamps each message with a timestamp and a severity level, and you can turn it up or down, or send it to a file, without rewriting the rest of your code.

In `oracle.ipynb`, consolidate the working code into one cell, now with logging:

```python
import logging
import os
import openai
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
)
logger = logging.getLogger(__name__)

load_dotenv()

client = openai.OpenAI(
    api_key=os.environ["STANFORD_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)

logger.info("Reading filing")
with open("../data/sec_filings/Cheniere_Energy_Inc.txt", "r") as f:
    filing_text = f.read()

logger.info("Sending %d characters to the model", len(filing_text[:4000]))
response = client.chat.completions.create(
    model="gemini-2.5-flash-lite",
    messages=[
        {"role": "system", "content": "You are a financial data extraction assistant. Extract information precisely and concisely."},
        {"role": "user", "content": f"Extract the insider's name and role. Reply with: NAME | ROLE\n\n{filing_text[:4000]}"}
    ]
)
logger.info("Model responded")

print(response.choices[0].message.content)
```

{: .note }
> 💡 Notice the split: **`logging` is for diagnostics** (what the program is doing, and when), while **`print` is for the actual result** you want to keep. Log messages carry a timestamp and level (`INFO`, `WARNING`, `ERROR`) and go to the error stream; your extracted answer stays clean on standard output. On Day 3, when these scripts run as cluster jobs, those logs are exactly what you'll read to see what happened.

Copy this into a new file called `form3_test.py` in your `day2/` folder (in the Jupyter terminal: `cd ~/gsb-research-computing-ai-skills/day2 && touch form3_test.py`).

Run it from the terminal:

```bash
cd ~/gsb-research-computing-ai-skills/day2
python form3_test.py
```

Verify you get the same output as the notebook. You now have a reproducible script you can schedule, share, or scale.

---

### Step 6 — Validate with Pydantic

The API returns a string. Pydantic turns it into a typed, validated Python object — and rejects responses that don't match your schema.

Define a model:

```python
from pydantic import BaseModel, ValidationError
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
logger.info("Requesting structured JSON extraction")
response = client.chat.completions.create(
    model="gemini-2.5-flash-lite",
    messages=[
        {"role": "system", "content": "Extract the requested fields from this SEC Form 3 filing. Return only valid JSON matching the schema provided."},
        {"role": "user", "content": f"Extract from this filing:\n\n{filing_text[:4000]}"}
    ],
    response_format={"type": "json_object"},
)

raw = response.choices[0].message.content

try:
    data = Form3Extraction.model_validate_json(raw)
except ValidationError as e:
    logger.error("Model output failed validation: %s", e)
    raise

logger.info("Validated extraction for issuer: %s", data.issuer_name)

with open("form3_extraction.json", "w") as f:
    f.write(data.model_dump_json(indent=2))
logger.info("Wrote form3_extraction.json")

print(data.model_dump_json(indent=2))
```

If the model returns a field that doesn't match the schema (wrong type, missing required field), `model_validate_json` raises a `ValidationError` — catching that error is how you know something went wrong before you scale to 10,000 filings.

Fold this into your `form3_test.py` so the script validates every response and writes `form3_extraction.json`, logging a clear error if validation ever fails.

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="main"> Main Quest complete</label>

---

## 📦 Side Quests

Your `client` talks to more than one endpoint. Each of these is a different door on the same Stanford gateway (your `base_url` never changes), so with the client already configured, they just work.

**Side Quest: List the Available Models**

Hit the models endpoint (`GET /v1/models`) to see exactly which model ids the gateway accepts. This is the menu for every other call.

```python
for m in client.models.list().data:
    print(m.id)
```

Look for `text-embedding-ada-002` and `imagen-4.0-generate-001` in the list; those are the ids the next two quests use.

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="side1"> I listed the available models</label>

**Side Quest: Turn Text into an Embedding**

An embedding turns text into a vector of numbers that captures its meaning, the foundation of semantic search and clustering. Call the embeddings endpoint (`POST /v1/embeddings`):

```python
resp = client.embeddings.create(
    model="text-embedding-ada-002",
    input="Insider files a Form 3 disclosure",
)
vector = resp.data[0].embedding
print(len(vector), "dimensions")
print(vector[:8])
```

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="side2"> I generated an embedding vector</label>

**Side Quest: Generate an Image**

The same gateway can create images. Call the image endpoint (`POST /v1/images/generations`):

```python
import base64
from IPython.display import Image, display

resp = client.images.generate(
    model="imagen-4.0-generate-001",
    prompt="A medieval alchemist's lab full of glowing potions, digital art",
)

img = resp.data[0]
if img.url:                       # some models return a link
    print(img.url)
else:                             # others (e.g. imagen) return base64
    display(Image(data=base64.b64decode(img.b64_json)))
```

{: .note }
> 💡 An images response carries the picture in one of two fields: `url` (a link to download) or `b64_json` (the image encoded inline as base64). A model fills in only one, so `resp.data[0].url` is `None` when the model returned base64. The code above checks for both.

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="side3"> I generated an image</label>

**Side Quest: Count Tokens and Calculate the Cost**

Every response reports how many tokens it used. Look at the `usage` field on one of your earlier chat responses:

```python
print(response.usage)
# CompletionUsage(prompt_tokens=..., completion_tokens=..., total_tokens=...)
```

Now look up your model's price on the <a href="https://uit.stanford.edu/service/ai-api-gateway/rates" target="_blank" rel="noopener noreferrer">AI API Gateway rates page</a> and work out what that single call cost:

```python
usage = response.usage

# From the rates page, in dollars per 1M tokens (fill in for your model):
input_price = 0.00
output_price = 0.00

cost = (usage.prompt_tokens * input_price + usage.completion_tokens * output_price) / 1_000_000
print(f"This call cost ${cost:.6f}")
```

Then multiply by 10,000 filings. That per-call number is small, but it is exactly what you budget against when you scale.

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="side4"> I found the token usage and estimated the cost</label>

---

## 🧠 Skills Learned

- The OpenAI-compatible API takes a list of messages with `role` (system/user/assistant) and `content` (the text)
- The system prompt frames what the model is and what it should do; the user prompt is the actual data
- Context limits mean you need to trim large documents before sending — `[:4000]` is a quick safeguard
- Pydantic models turn unstructured LLM output into typed, validated Python objects — if the model returns garbage, you catch it before it silently corrupts your dataset
- A notebook is for exploration; a `.py` script is for reproducibility
