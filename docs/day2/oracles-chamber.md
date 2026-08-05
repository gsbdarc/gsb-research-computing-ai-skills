---
layout: default
title: "The Oracle's Chamber"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 6
permalink: /day2/oracles-chamber/
---

# The Oracle's Chamber

<div data-room-id="d2-oracles-chamber"></div>

The Oracle answers, but only as well as you ask. In this room you make your first live call to the Stanford AI API Gateway, then put a model to real work: reading a dense SEC Form 3 filing and pulling out who filed it and in what role. You will shape the prompt until the answer comes back clean, validate it with Pydantic so bad output fails loudly instead of corrupting your results, and move the working logic out of the notebook into a logged, reproducible script.

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Make your first live API call, then use the Stanford AI API Gateway to extract structured information from a real SEC Form 3 filing, and save the logic to a standalone Python script.

---

### Step 1: Open the Oracle's Notebook

Every invocation in this room happens in one notebook. In JupyterHub (on the Yens), open your `day2/` folder and create a **new notebook named `oracle.ipynb`**. From the kernel menu in the top-right, choose **GSB AI 2026**, the kernel you forged in [The Venv Forge](../venv-forge/).

{: .important }
> Selecting the **GSB AI 2026** kernel is what gives this notebook its reagents (`openai`, `python-dotenv`, and `pydantic`), the packages you installed into that venv. If the imports in the next step fail with `ModuleNotFoundError`, the wrong kernel is almost always the culprit: check the kernel name shown in the notebook's top-right corner.

Every code cell below runs in `oracle.ipynb` unless it says otherwise.

---

### Step 2: Hello World

Load your `.env`, initialize the OpenAI client, and confirm the API answers:

```python
from dotenv import load_dotenv
import os
import openai

load_dotenv("../.env")   # this notebook is in day2/; .env is at the repo root

client = openai.OpenAI(
    api_key=os.environ["STANFORD_API_KEY"],
    base_url="https://aiapi-prod.stanford.edu/v1",
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

{: .note }
> 🟢 **Green sticky** = the model replied, so my key, my `base_url`, and my kernel are all working &nbsp;&nbsp; 🔴 **Red sticky** = I got an error instead of a reply
>
> Put a sticky note on your laptop lid so instructors can see where you are.

<details markdown="1">
<summary>💡 Got an error? Read which one — click to reveal</summary>

This is the first cell all week that talks to the outside world, so it's the first one that can fail for a reason other than your code. The error name tells you which piece to look at:

| What you see | What it means |
|---|---|
| `KeyError: 'STANFORD_API_KEY'` | `load_dotenv` didn't find the file. You're in `day2/`, so the path is `"../.env"` — check `pwd` in a terminal and that [The Key Vault](../key-vault/)'s `cp` actually landed. |
| `ModuleNotFoundError` | Wrong kernel. Check the top-right of the notebook says **GSB AI 2026**, not **Python 3**. |
| `401` / `AuthenticationError` | The key loaded but the gateway rejected it. Re-copy it from `/scratch/shared/gsb-research-computing-ai-skills/.env` rather than retyping. |
| `404` / `NotFoundError` | The `base_url` or the model id is off. The URL ends in `/v1`, and the model list is a side quest at the bottom of this room. |

</details>

---

### Step 3: Load and Inspect a SEC Filing

**First, what is a Form 3?** When someone becomes an insider at a public company — a director, an officer, or anyone holding more than 10% of it — the SEC requires them to declare what they own. That declaration is a **Form 3**, and it names the insider, their role at the company, and the shares they hold.

Those filings are a genuinely useful research dataset: who joined which board, when, and holding what. The catch is the format. A Form 3 is dense, semi-structured text written for regulators rather than for analysis, and the fields you want are buried in it rather than sitting in tidy columns. Hand-coding a thousand of them is a week of tedium; a regular expression breaks on the first filing that's laid out differently.

That is exactly where the Oracle earns its keep, and it's the pattern behind most AI-assisted research: **unstructured text in, structured fields out.**

A sample of these filings ships in your course repo:

```bash
ls ~/gsb-research-computing-ai-skills/data/sec_filings/
```

You should see five `.txt` files, one per company. Load one in `oracle.ipynb` and see what you're up against:

```python
with open("../data/sec_filings/Cheniere_Energy_Inc.txt", "r") as f:
    filing_text = f.read()

print(filing_text[:2000])   # preview the first 2000 characters
```

Read that preview before moving on. The insider's name and role *are* in there — and now you can see why pulling them out by hand, five thousand times, is nobody's idea of research.

---

### Step 4: Extract Information with the API

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
> 💡 The `[:4000]` slice limits how much text you send, since models have context limits. For now we stay within budget; Day 3 will scale this to hundreds of filings.

Experiment: try changing the system prompt. What happens if you ask for more fields? What if the prompt is vague?

---

### Step 5: From Notebook to Script

A notebook is great for exploration, and that's what you just did: you tried a prompt, looked at the answer, and adjusted. But a notebook is a poor place to *keep* working logic. It runs only while you're sitting there clicking, and a cluster job has nobody to click.

So the same logic moves into a **script**: a `.py` file that runs start to finish on its own. Your repo ships three of them, and they are the same program three times over, each one adding exactly one idea:

| Stage | Script | What it adds |
|-------|--------|--------------|
| **1** | `extract_form_3_step1_basic.py` | Nothing new — the notebook's logic in a file |
| **2** | `extract_form_3_step2_logged.py` | `logging`, and saving the result to a file |
| **3** | `extract_form_3_one_file.py` | A schema, so bad output fails loudly |

Nothing to type and nothing to paste. You'll **run** each one, read the few lines that changed, and finish holding the script Day 3 picks up.

{: .note }
> 📁 **These live in `scripts/`, and you run them from the repo root** — not from `day2/`. That's why the paths inside them read `data/sec_filings/...` with no `../` in front. Remember from [The Path](../the-path/): a relative path is relative to **wherever you're standing**, so where you run a script decides which files it can find.

Activate your venv and go to the repo root:

```bash
source ~/gsb-research-computing-ai-skills/.venv/bin/activate
cd ~/gsb-research-computing-ai-skills
```

---

#### Stage 1: the notebook's logic, in a file

Open it and read it — it's about a dozen lines of actual code, and you've seen all of them in your notebook:

```bash
cat scripts/extract_form_3_step1_basic.py
python3 scripts/extract_form_3_step1_basic.py
```

You get the same `NAME | ROLE` answer the notebook gave you. Same call, same prompt, new container.

Notice what it does **not** do: it prints the answer and forgets it. Close the terminal and the result is gone. That's the gap stage 2 fills.

---

#### Stage 2: say what you're doing, and keep the answer

Two things change when code stops being watched by a human.

**How it reports progress.** In a notebook you watch cell output live. A script often runs unattended — in the background, or as a cluster job whose output you read hours later — so instead of scattering `print()` calls, use Python's built-in **`logging`**. It stamps every message with a timestamp and a severity level, and you can turn it up or down without touching the rest of your code.

Point it at **two places at once**: your screen, so you can watch, and a **log file**, so you don't have to. The file handler *appends*, so runs accumulate rather than overwrite. After a morning of edits you have a timestamped history of every attempt — which is the record you go back to when a result looks wrong and you need to know what you actually ran.

**Where it puts the answer.** A script's terminal output scrolls away the moment you close the window, and a cluster job has no screen at all. So the script **writes its result to a file**. That file is the real product of the run: the thing you reopen tomorrow, hand to a collaborator, or feed into the next step.

Run it, then look at what it left behind:

```bash
python3 scripts/extract_form_3_step2_logged.py
cat results/form3_Cheniere_Energy_Inc.txt   # the answer, saved
cat form3_extract.log                       # what happened, timestamped
```

Now see precisely what changed since stage 1 — let the computer tell you instead of hunting for it by eye:

```bash
diff scripts/extract_form_3_step1_basic.py scripts/extract_form_3_step2_logged.py
```

Lines marked `>` are new. You should find only three ideas in there: the `logging` setup, a `FILING` constant hoisted to the top, and the block that writes the output file.

{: .note }
> 💡 **Two kinds of output, two different lifetimes.** `results/form3_*.txt` is **your data** — you keep it, you commit it, it outlives the run. `form3_extract.log` is a **diary of the process** — useful for a week, then disposable, which is why `*.log` is already in the repo's `.gitignore`. On Day 3, when these run as cluster jobs, the logs are what you read to see what happened and the result files are what you collect.

{: .note }
> 💡 **Why `FILING` sits at the top.** Anything you expect to change between runs belongs in a constant where you can find it without reading the whole file. Naming the output after it means two runs on two filings leave two results instead of one silently overwriting the other.

---

#### Exercise: point it at a different company

Cheniere Energy is one of five filings in that folder. See the rest:

```bash
ls data/sec_filings/
```

Open `scripts/extract_form_3_step2_logged.py`, change the single line near the top, and save:

```python
FILING = "FLOWSERVE_CORP"
```

Run it again and look at what's in `results/` now:

```bash
python3 scripts/extract_form_3_step2_logged.py
ls results/form3_*
cat results/form3_FLOWSERVE_CORP.txt
```

A different insider, a different role, and **both** result files are still there. Now read the log:

```bash
cat form3_extract.log
```

Both runs are in it, in order, timestamped. Notice the `Sending N characters` line differs between them, because the two filings aren't the same length. That's the log doing its job: not just "it worked," but a record of *what each run actually did*.

{: .note }
> 💡 Hold that thought. If swapping one filing is a single variable, then processing all five is a `for` loop around the same code. That's exactly the move you'll make on Day 3, at a scale where you'd never edit by hand.

---

### Step 6: Validate with Pydantic

Your result files are real artifacts, but each one is still just a blob of text — `NAME | ROLE`, with nothing checking that the model gave you that shape. Split on the wrong character, or get a chatty reply that opens with "Sure! Here's the extraction:", and your parsing quietly breaks.

Stage 3 closes that at both ends. Ask for **JSON** instead of freeform text, and validate it with **Pydantic**, which turns the reply into a typed Python object and rejects anything that doesn't match your schema.

The four new pieces:

1. **A schema** (`Form3Filing`) — your declaration of the fields you expect and their types.
2. **The schema described in the prompt**, so the model calls each field what your code calls it.
3. **`response_format`**, which constrains the reply to valid JSON as the model writes it.
4. **Validation**, which checks the finished reply and fails loudly if it doesn't match.

Here is the schema, the heart of it:

```python
class Form3Filing(BaseModel):
    insider_name: str
    insider_role: List[str]
    company_name: str
    company_cik: str
    filing_date: str
```

And the line that turns a hopeful string into a checked object:

```python
result = Form3Filing.model_validate_json(raw)
```

Read the whole thing, run it, then diff it against stage 2:

```bash
cat scripts/extract_form_3_one_file.py
python3 scripts/extract_form_3_one_file.py
diff scripts/extract_form_3_step2_logged.py scripts/extract_form_3_one_file.py
```

**Why it writes two files.** Every run leaves both the raw reply and the validated JSON, and keeping both is deliberate:

- **The raw file is your evidence.** It's written *before* validation, so it exists even on runs that crash. When a `ValidationError` fires you don't have to re-run — and re-pay for — the call to find out what the model said. You open the file and look. Most "the model returned garbage" mysteries turn out to be one stray character.
- **The JSON file is your data.** It's what survived the check, normalized to your types. This is what downstream code reads.
- **Together they're an audit trail.** Six months from now, "what did the model return, and what did we keep?" is answerable from disk rather than from memory.

```bash
cat results/form3_result.json
```

{: .note }
> 💡 **It also switched models.** Stages 1 and 2 used `gemini-2.5-flash-lite` — cheap and fast, which is what you want while you're still changing the prompt every two minutes. Stage 3 uses `gpt-5.2`, now that the prompt has settled and you want the best extraction. That swap is **one line**, because both live behind the same `base_url`. Iterate cheap, then spend where it counts.

{: .note }
> 🟢 **Green sticky** = all three stages ran and `results/form3_result.json` has all five fields &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

You now hold `scripts/extract_form_3_one_file.py` — one filing in, validated structured data out, with a log of what happened. **Day 3 starts by profiling this exact script**, then wraps it in a loop and hands it to the cluster.

<details markdown="1">
<summary>🔬 In the weeds: how the model is actually constrained (click to reveal)</summary>

**`response_format` and Pydantic are two different defenses, at two different moments.** It's tempting to think Pydantic is somehow steering the model. It isn't.

**`response_format={"type": "json_object"}` runs on the server, while the model is still writing.** A model generates one token at a time, choosing from a probability distribution over its whole vocabulary. JSON mode *masks* that distribution: any token that would break JSON syntax has its probability forced to zero, so the model literally cannot produce a stray "Sure, here you go!" or a trailing comma. That's why you no longer need to defend against chatty preambles. But notice what it does **not** do: it enforces valid JSON, not *your* JSON. `{"name": "...", "title": "..."}` is perfectly valid JSON and would sail straight through.

**Pydantic runs in your own Python process, after the response has fully arrived.** It never touches generation, and the model has no idea your `Form3Filing` class exists. `model_validate_json` takes the finished string and checks it against your field names and types, raising `ValidationError` if `insider_name` is missing or `insider_role` comes back as a bare string instead of a list.

That leaves a gap between the two, and **the prompt is what closes it.** The model only knows to call the field `insider_name` because you *told* it so, in that `system_prompt` listing the five fields by name. Nothing enforces that the prompt and the class agree — which is the quiet weakness of the stage 3 script. Rename a field in `Form3Filing` and forget to update the prompt, and validation starts failing on replies the model thought were correct.

The tighter version has Pydantic describe itself, so the class is the single source of truth at both ends:

```python
schema = json.dumps(Form3Filing.model_json_schema(), indent=2)
# ...then send `schema` as part of the system prompt instead of a hand-written field list
```

Now renaming a field updates the instruction and the check at once. Worth doing the moment a schema stops being something you can hold in your head.

**What's actually on the other end of that `base_url`.** The Stanford gateway is a **LiteLLM** proxy. LiteLLM is an open-source router that presents a single OpenAI-compatible API and translates each incoming request into the native format of whichever provider really serves that model, then translates the reply back. That is the machinery behind the Key Vault's one-client-many-services diagram, and behind the models list you pulled in the side quest: Gemini, Claude, and the rest are all reachable through one `base_url` because something in the middle is doing the format translation for you.

The catch is that a proxy can only pass along what the model underneath actually supports, so `response_format` is a request whose enforcement depends on the model behind the name. On this gateway, `{"type": "json_object"}` with `gemini-2.5-flash-lite` does hold: the replies come back as bare, parseable JSON.

A stronger option exists, `{"type": "json_schema"}`, which constrains decoding against your schema itself so the field names are masked into place rather than merely requested. It takes a **nested payload**, not just a type string:

```python
response_format={
    "type": "json_schema",
    "json_schema": {
        "name": "form3_filing",
        "schema": Form3Filing.model_json_schema(),
    },
}
```

Get that shape wrong and the failure is quiet rather than loud. Sending a bare `{"type": "json_schema"}` with no schema attached gives the gateway nothing to constrain against, the request degrades to ordinary unconstrained generation, and the model reverts to its default habit of wrapping the answer in a Markdown code fence (three backticks, then `json`). You still get a `200 OK`, and the breakage surfaces one line later as a confusing Pydantic error:

```text
Invalid JSON: expected value at line 1 column 1
  [type=json_invalid, input_value='```json\n{\n  "insider_n...']
```

Read that message closely: the JSON *inside* the fence is perfectly good and the field names are right. The three backticks in front of it are the entire problem. Whenever a validation error quotes an `input_value` that starts with backticks, the constraint layer isn't doing what you assumed it was.

**Which is exactly why you still validate.** The constraint layer is the part that changes when you swap `model="gemini-2.5-flash-lite"` for `gpt-5.2`, or when you point `base_url` at a model running locally on the Yens. Pydantic is the layer that behaves identically no matter who is on the other end. Prompt for the shape you want, ask for whatever constraint the model offers, and then check the result yourself regardless.

</details>

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="main"> Main Quest complete</label>

---

## 📦 Side Quests

{: .note }
> Finished early? Try any of these.

Your `client` talks to more than one endpoint. Each of these is a different door on the same Stanford gateway (your `base_url` never changes), so with the client already configured, they just work.

**Side quest: List the Available Models**

Hit the models endpoint (`GET /v1/models`) to see exactly which model ids the gateway accepts. This is the menu for every other call.

```python
for m in client.models.list().data:
    print(m.id)
```

Look for `text-embedding-ada-002` in the list; that's the id the next quest uses.

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="side1"> I listed the available models</label>

**Side quest: Turn Text into an Embedding**

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

**Side quest: Count Tokens and Calculate the Cost**

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

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="side3"> I found the token usage and estimated the cost</label>

**Side quest: Pay for Thinking You Never See**

Some models on the gateway **reason** before they answer: they work the problem through internally, then write a reply. That hidden reasoning is generated text, so it's billed as output tokens, and most of these models never show it to you.

Ask three models the same small trick question and compare what you're charged:

```python
QUESTION = "A farmer has 17 sheep. All but 9 run away. How many sheep are left?"

for model in ["gemini-2.5-flash-lite", "o3-mini", "deepseek-r1"]:
    try:
        r = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": QUESTION}],
        )
        answer = (r.choices[0].message.content or "").strip()
        print(f"\n=== {model} ===")
        print("answer :", answer[:300])
        print("usage  :", r.usage)
    except Exception as e:
        print(f"\n=== {model} ===\n  unavailable: {e}")
```

All three get it right, in about the same number of words. Here's what they charged:

| Model | Prompt tokens | **Completion tokens** | `reasoning_tokens` reported |
|---|---|---|---|
| `gemini-2.5-flash-lite` | 21 | **27** | not reported |
| `o3-mini` | 26 | **236** | **192** |
| `deepseek-r1` | 24 | **595** | not reported |

Read that middle column, because it's the one you pay. Same question, same answer, and `deepseek-r1` billed **22× more output** than `gemini-2.5-flash-lite` for two sentences.

The two reasoning models expose that differently, and both cases are worth seeing:

- **`o3-mini` tells you.** Its `completion_tokens_details` reports `reasoning_tokens=192`, so of the 236 output tokens you were billed for, **81% was thinking you never saw**. Only about 44 tokens were the answer.
- **`deepseek-r1` doesn't.** It returns `completion_tokens_details=None`, so the gateway gives you no breakdown at all.

**But "not reported" doesn't mean "didn't happen" — and you can do the subtraction yourself.** `deepseek-r1`'s visible reply is about forty words, call it **47 tokens**, against **595** billed. So roughly **548 tokens of reasoning** happened and simply weren't itemized. That arithmetic — *what I was charged, minus what I can actually read* — is your fallback whenever `completion_tokens_details` comes back `None`, and it works on any model.

That's why the instruction is to print the whole `usage` object instead of reaching for one field. Whether the split is *reported* is a property of the model and the gateway; whether the reasoning *was billed* is not up for debate. `completion_tokens` is always there, and it's always what you're charged.

{: .note }
> 💡 Not every id is guaranteed to be enabled, which is why the loop catches errors instead of crashing. Run the *List the Available Models* quest above to see what your key can actually reach, and swap in any reasoning model you find (`o1`, or a `gpt-5` variant).

Now price it. Put each model's rate from the rates page into the cost formula from the previous quest and work out the real cost of each of those three answers. The cheapest model is not always the cheapest *call*, and on a reasoning model the length of the reply tells you nothing about the bill.

<label class="quest-check"><input type="checkbox" data-room="d2-oracles-chamber" data-key="side4"> I compared token usage across a plain and a reasoning model</label>

---

## 🧠 Skills Learned

- The OpenAI-compatible API takes a list of messages with `role` (system/user/assistant) and `content` (the text)
- The system prompt frames what the model is and what it should do; the user prompt is the actual data
- Context limits mean you need to trim large documents before sending; `[:4000]` is a quick safeguard
- `response_format={"type": "json_object"}` constrains the model *as it generates*, masking any token that would break JSON syntax; where it's honored, you no longer have to strip chatty preambles by hand
- Pydantic validates *after* the reply arrives; it turns unstructured LLM output into typed, validated Python objects, so if the model returns garbage you catch it before it silently corrupts your dataset
- Those two are separate defenses, and neither one tells the model your field names — only the prompt does that, which is why the prompt and the schema have to stay in step
- A `logging.FileHandler` appends, so one log file accumulates a timestamped history across every run, which is what you read when a result looks wrong and you need to know what you actually ran
- A notebook is for exploration; a `.py` script is for reproducibility
- A relative path is relative to where you *run* from, which is why these scripts live in `scripts/` and run from the repo root
- Build a script in stages, one idea at a time, and `diff` consecutive versions to see exactly what each idea cost you in code
