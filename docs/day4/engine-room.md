---
layout: default
title: "The Engine Room"
parent: "Day 4 — The GPU Fortress"
nav_order: 5
permalink: /day4/engine-room/
---

# The Engine Room

<div data-room-id="d4-engine-room"></div>

*The machines behind the machines. Ollama is a torch — quick to light, good for one researcher at a time. When a hundred researchers need the same model simultaneously, you need an engine room: vLLM, TensorRT-LLM, NVIDIA NIM. The Engine Room is concept-only today. You don't need to operate it — you need to know it exists and when to call for it.*

---

## Main Quest

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

## Skills Learned

- Understand the difference between Ollama (prototyping) and vLLM (production serving)
- Know that NVIDIA NIM provides pre-optimized containerized model serving
- Recognize that all three (Ollama, vLLM, NIM) expose OpenAI-compatible APIs — same Python client
- Know when to escalate from personal Ollama to shared infrastructure
