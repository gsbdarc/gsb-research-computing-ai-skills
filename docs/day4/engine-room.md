---
layout: default
title: "The Engine Room"
parent: "Day 4 — The GPU Fortress"
nav_order: 5
permalink: /day4/engine-room/
---

# The Engine Room

<div data-room-id="d4-engine-room"></div>

*Deep in the fortress, past the GPU racks and the hum of cooling fans, lies the Engine Room — where models don't just run, they roar. Ollama is a torch: brilliant, portable, yours alone. But when a hundred researchers hammer the same model at once, a torch becomes a liability. Here live the true power systems: vLLM, TensorRT-LLM, NVIDIA NIM — industrial-grade inference engines built to serve armies. You won't operate them today. You'll learn to recognize them, respect them, and know exactly when to call for the engineers who run them.*

---

## 🗡️ Main Quest

The fate of your research pipeline hinges on a single question: are you a lone wolf, or are you building something the whole team will depend on? Choose your weapon wisely.

{: .important }
> **Quest:** Understand the production-grade local LLM stack and know the decision point between Ollama and vLLM.

This is a concept and demo block.

**Ollama vs. vLLM:**

| | Ollama | vLLM |
|---|---|---|
| **Use case** | Single researcher, prototyping | Multi-user, high-throughput serving |
| **Setup complexity** | `ollama pull` | Docker / conda, configuration required |
| **Throughput** | Good for 1 user | Scales to 100+ concurrent requests |
| **Features** | Simple API, easy model management | Continuous batching, quantization, LoRA |
| **When to use** | Your personal research pipeline | Shared research infrastructure, deployed tools |

**NVIDIA NIM:**

NVIDIA provides containerized inference endpoints for popular models (Llama, Mistral, Stable Diffusion) called NIM (NVIDIA Inference Microservices). They're pre-optimized for specific GPU architectures and expose the same OpenAI-compatible API.

💡 The beautiful secret: your Python code doesn't change. Swap one URL and you've gone from laptop prototype to production cluster.

```python
# Same Python code works for Ollama, vLLM, NIM, and the Stanford Playground
# Only base_url changes
client = openai.OpenAI(base_url="http://nim-server:8000/v1", api_key="nim")
```

**The decision tree:**

```
Solo research pipeline? → Ollama
Research team sharing a model? → vLLM on a dedicated node
Need a specific optimized model (Llama, etc.)? → Consider NVIDIA NIM
Data must stay on-prem? → Any of the above (all local)
Any of the above with cloud OK? → Stanford AI Playground
```

<label class="quest-check"><input type="checkbox" data-room="d4-engine-room" data-key="main"> Engine Room briefing complete — I understand the path from Ollama to production serving</label>

---

## 🧠 Skills Learned

- You can now distinguish between Ollama (your personal torch) and vLLM (the shared power grid) — and know which one your project needs
- You can identify when NVIDIA NIM is the right call: pre-optimized, containerized, GPU-architecture-aware serving for popular models
- You know that Ollama, vLLM, and NIM all speak the same OpenAI-compatible API — one Python client rules them all
- You can recognize the moment a solo pipeline needs to graduate to shared infrastructure, and you know who to call when it does
