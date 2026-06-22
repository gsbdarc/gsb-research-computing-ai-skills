---
layout: default
title: "The Summoning Circle"
parent: "Day 4 — The GPU Fortress"
nav_order: 4
permalink: /day4/summoning-circle/
---

# The Summoning Circle

<div data-room-id="d4-summoning-circle"></div>

*Draw the circle, speak the name, and the model appears — running entirely inside the fortress, never sending a single token off campus. Ollama is the summoning ritual. The model is yours to keep, interrogate, and benchmark. No API key. No usage caps. No prompts logged to a server in another state.*

---

## Main Quest

{: .important }
> **Quest:** Pull a model with Ollama on the H200, chat with it from a Jupyter notebook, and confirm it runs locally.

**Inside a GPU job on yen-gpu4** (or from an interactive session if available):

```bash
# Check if Ollama is installed (ask instructor if not)
ollama --version

# Pull a model (this downloads the weights to local storage)
ollama pull llama3.2:3b        # 3B parameter model, ~2 GB download

# Serve the model (keep this running in a screen session)
screen -S ollama_server
ollama serve
# Ctrl-A D to detach
```

**From JupyterHub** (or a Python script), query the local model:

```python
import openai

# Ollama exposes an OpenAI-compatible API locally
client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",   # dummy value — Ollama doesn't use auth
)

response = client.chat.completions.create(
    model="llama3.2:3b",
    messages=[
        {"role": "user", "content": "What is SLURM and why do researchers use it? Reply in 3 sentences."}
    ]
)

print(response.choices[0].message.content)
```

Notice: the interface is **identical to the Stanford AI Playground** — same Python code, different `base_url`. This is the OpenAI-compatible API standard.

{: .note }
> Ollama must be running (via `ollama serve`) on the same node where you're querying it. The model runs entirely on the Yens; your prompts never leave Stanford's network.

<label class="quest-check"><input type="checkbox" data-room="d4-summoning-circle" data-key="main"> Main Quest complete</label>

---

## Chests

{: .chest }
> **Chest 1 — Model Menagerie:** Pull two additional models (e.g. `phi3:mini` and `gemma2:2b`). Ask each the same question about SLURM. Compare response quality, speed (tokens/second), and the trade-off between model size and latency.

<label class="quest-check"><input type="checkbox" data-room="d4-summoning-circle" data-key="chest1"> Model Menagerie unlocked</label>

{: .chest }
> **Chest 2 — Modelfile Magic:** Create a custom Ollama `Modelfile` that gives a base model a system prompt making it respond as a SLURM expert with terse, command-focused answers. Build the custom model with `ollama create` and test it.

<label class="quest-check"><input type="checkbox" data-room="d4-summoning-circle" data-key="chest2"> Modelfile Magic unlocked</label>

---

## Weapons Earned

{: .weapon }
> **Model Menagerie** — compare multiple local models on the same task; choose by latency, quality, and VRAM requirements rather than defaulting to the largest model.
>
> **Modelfile Magic** — customize any Ollama model with a system prompt via `Modelfile`; create purpose-built research assistants without cloud API costs.

---

## Skills Learned

- Pull and serve a local LLM with Ollama on cluster GPU hardware
- Use the OpenAI-compatible Ollama API from Python — same code as the Stanford AI Playground
- Understand that local models mean zero data leaves the Yens — useful for restricted datasets
- Know when local (Ollama) beats cloud (Playground): privacy requirements, high-volume batches, no API budget
