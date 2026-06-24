---
layout: default
title: "The Summoning Circle"
parent: "Day 4 — The GPU Fortress"
nav_order: 4
permalink: /day4/summoning-circle/
---

# The Summoning Circle

<div data-room-id="d4-summoning-circle"></div>

*Chalk the circle on the stone floor. Speak the model's name. Watch the weights materialize on drives inside the fortress — billions of parameters, fully yours, answering only to you. Ollama is the ritual. The H200 is the altar. No API key demanded at the door, no usage meter ticking in the background, no whisper of your prompts drifting to a server farm in another state. What runs here stays here.*

---

## 🗡️ Main Quest

You've got raw GPU muscle beneath you — now it's time to bind a model to it. Speak the name and watch it answer.

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
> 💡 Ollama must be running (via `ollama serve`) on the same node where you're querying it. The model runs entirely on the Yens; your prompts never leave Stanford's network.

<label class="quest-check"><input type="checkbox" data-room="d4-summoning-circle" data-key="main"> Main Quest complete</label>
