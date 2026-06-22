# RF Coding Bootcamp 2026 — Class Agenda

**Format:** 💻 hands-on · 🖊️ whiteboard/concept · 💬 discussion · 🔑 capstone

Every concept has a hands-on exercise. The website documents everything so students can look it up later — class time is for building mental models and doing, not memorizing syntax.

---

## Day 1 — Getting on the Yens (~3 hrs)

*By end of day: you can log in, navigate the cluster, run a notebook, and have your work in git.*

| # | Block | Format | Time | What researchers master |
|---|---|---|---|---|
| 1.0 | Welcome — how the course works, green/red stickies, website as reference | 💬 | 10 min | — |
| 1.1 | The command line — what it is, why researchers use it instead of clicking | 🖊️ | 10 min | Mental model: shell as a research tool, not a developer tool |
| 1.2 | CLI basics — `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rm` | 💻 | 20 min | Navigate and manipulate files on any Unix system |
| 1.3 | File wrangling exercise — sort a directory of spell files by element using wildcards | 💻 | 25 min | Bulk file operations; wildcards; thinking in patterns not clicks |
| — | ☕ Break | — | 10 min | — |
| 1.4 | Remote computing — what a server is, why researchers use one, what the Yens are | 🖊️ | 10 min | Mental model: local laptop vs. shared cluster |
| 1.5 | SSH — connect to the Yens, identify your node, understand the login banner | 💻 | 15 min | Connect to a remote server; understand login vs. compute nodes |
| 1.6 | Yens file system — home vs. `/scratch`, `gsbquota`, `gsbbrowser`, `module avail` | 💻 | 15 min | Know where data lives, how much space you have, what software is available |
| 1.7 | File transfer — `scp` a file up; understand the shared file system | 💻 | 10 min | Move data between local and remote; shared FS means one copy everywhere |
| 1.8 | JupyterHub — open a notebook on the Yens, run a cell, understand the kernel | 💻 | 15 min | Run code on cluster hardware from a browser |
| 1.9 | Git for research — `clone`, `branch`, `add`, `commit`, `push`; why every project needs this | 💻 | 20 min | Version-control a project; understand the fork → commit → push workflow |
| 1.10 | AI primer — token, context window, prompt, agent (4 pictures, draw together) | 🖊️ | 15 min | Working mental model of how LLMs work before touching one |
| 1.11 | 🔑 Capstone: find the hidden file in `/scratch/…/vault/`, commit your answer to your fork | 🔑 | 15 min | Use everything from today together on an open-ended problem |

**Total: ~3h**

---

## Day 2 — Your First Research Pipeline (~3h 15min)

*By end of day: you can call an LLM on a real document, get structured output, and run a script that keeps going after you close your laptop.*

| # | Block | Format | Time | What researchers master |
|---|---|---|---|---|
| 2.0 | Day 1 recap — sticky check | 💬 | 10 min | — |
| 2.1 | Virtual environments — why they exist, what breaks without them | 🖊️ | 5 min | Mental model: project isolation |
| 2.2 | Create and use a venv, connect it to JupyterHub as a kernel | 💻 | 20 min | Isolate dependencies per project; never break another project's environment |
| 2.3 | `$PATH` and `module load` — why the same command gives different results | 💻 | 15 min | Understand how the shell finds commands; fix "command not found" confidently |
| 2.4 | Stanford AI Playground — what it is, why it exists, data governance, budget caps, available models | 🖊️💬 | 15 min | Know what the Playground guarantees vs. a personal OpenAI account; understand Stanford's data perimeter |
| 2.5 | Security and secrets — `.env`, `python-dotenv`, `.gitignore`; what cloud APIs log; never commit keys | 💻 | 15 min | Keep credentials secure; understand what leaves your machine on every API call |
| 2.6 | Claude Code — what it is, try it, use it to write a cluster script; one rule: don't paste keys or restricted data | 💻 | 15 min | Use AI-assisted coding as a research tool; verify AI output; know the security rule |
| — | ☕ Break | — | 10 min | — |
| 2.7 | First LLM call — call the Playground on one SEC Form 3, extract the insider's name and role | 💻 | 25 min | Call any OpenAI-compatible API from Python; write an effective research prompt |
| 2.8 | Structured outputs — `pydantic` model, validate the response, save as JSON | 💻 | 20 min | Extract structured data reliably; never parse free text when you can type it |
| 2.9 | When not to use an LLM — token cost intuition, `grep` vs. LLM decision | 💬 | 10 min | Apply "regex first, LLM second"; estimate cost before scaling |
| 2.10 | `screen` — detach a session, close your laptop, reattach tomorrow | 💻 | 15 min | Run jobs that outlast your SSH session |
| 2.11 | 🔑 Capstone: 5 earnings call transcripts → structured JSON → commit to fork | 🔑 | 20 min | End-to-end LLM research pipeline |

**Total: ~3h 15min**

---

## Day 3 — Scaling with SLURM (~3h)

*By end of day: you can submit batch jobs, scale to hundreds of inputs, document your pipeline, and commit everything.*

| # | Block | Format | Time | What researchers master |
|---|---|---|---|---|
| 3.0 | Day 2 recap | 💬 | 10 min | — |
| 3.1 | Why batch scheduling — live demo of shared resources; kitchen analogy | 🖊️💻 | 20 min | Mental model: SLURM as a head chef, your script as a recipe; see resource contention live |
| 3.2 | Estimate resources first — `time`, `htop`, `userload` | 💻 | 15 min | Measure before requesting; be a good cluster neighbor |
| 3.3 | Write and submit your first `sbatch` script | 💻 | 25 min | Write a SLURM script from scratch; understand every directive |
| 3.4 | Monitor and manage — `squeue`, `scancel`, `sacct` | 💻 | 15 min | Track, cancel, and audit jobs; use `sacct` for post-mortem |
| 3.5 | Spot-the-Bug — 3 broken scripts, class finds the bugs | 💬 | 12 min | Recognize the most common SLURM failures before they cost you queue time |
| — | ☕ Break | — | 10 min | — |
| 3.6 | Job arrays — scale to 100 inputs, combine outputs into one CSV | 💻 | 30 min | Run hundreds of jobs in parallel; aggregate results cleanly |
| 3.7 | README for your pipeline — write it while the pipeline is fresh | 💻 | 15 min | Document research work clearly; README as a research artifact |
| 3.8 | 🔑 Capstone: 100 filings via array → CSV + README → commit to fork | 🔑 | 20 min | Real research pipeline at scale, documented |
| 3.9 | Hall of Heroes — live `userload`, fastest array, best job name | 💬 | 5 min | — |

**Total: ~2h 57min**

> **Fault-tolerant pipelines** (log completed tasks, skip on rerun) are covered as optional chests in the Job Arrays room — students who finish early can explore this pattern.

---

## Day 4 — GPUs, Local LLMs, and Doing Research Right (~2h 40min)

*By end of day: you've run a job on the H200, talked to a local LLM, know how to protect your data, and have updated your documented pipeline.*

| # | Block | Format | Time | What researchers master |
|---|---|---|---|---|
| 4.0 | Day 3 recap | 💬 | 10 min | — |
| 4.1 | GPU landscape — A30 / A40 / H200 on yen-gpu4, what each is for | 🖊️ | 10 min | Know what GPUs are available, when you need one, how to request it |
| 4.2 | First GPU job — `--gres=gpu:1`, target yen-gpu4, run inference | 💻 | 25 min | Submit and run a GPU job; understand GPU memory and why model size matters |
| 4.3 | Local LLMs with Ollama — pull a model, chat from Jupyter | 💻 | 25 min | Host a local LLM on cluster hardware; understand the OpenAI-compatible interface |
| 4.4 | vLLM and NIM — production-grade serving, concept + demo only | 💬 | 10 min | Know the path from Ollama prototype → production serving |
| — | ☕ Break | — | 10 min | — |
| 4.5 | Privacy and data governance — 3-bucket rule + classify your own datasets (5 min exercise) | 💬🖊️💻 | 20 min | Apply the 3-bucket rule to your own datasets; know when cloud API is off-limits |
| 4.6 | Agent risks — hallucination at scale, runaway loops, prompt injection, irreversibility | 💬 | 15 min | Name failure modes before they happen in your research pipeline |
| 4.7 | 🔑 Capstone: swap Day 3 pipeline to Ollama endpoint, compare outputs, update README, commit | 🔑 | 25 min | Full stack: SLURM → GPU → local LLM → structured output → documented |
| 4.8 | Wrap — what's next (fine-tuning, Sherlock, Redivis), feedback survey | 💬 | 10 min | — |

**Total: ~2h 40min**

---

## Coverage checklist

| Topic | Day |
|---|---|
| CLI + file system | 1 |
| SSH + Yens orientation | 1 |
| File transfer (`scp`) | 1 |
| JupyterHub | 1 |
| Git for version control | 1 |
| AI primer (mental model) | 1 |
| Virtual environments | 2 |
| `$PATH` and modules | 2 |
| Stanford AI Playground + data governance | 2 |
| Security best practices + secrets | 2 |
| Claude Code | 2 |
| LLM API calls + structured output | 2 |
| Token cost intuition | 2 |
| `screen` for long jobs | 2 |
| SLURM — why, live demo, batch jobs | 3 |
| Resource estimation | 3 |
| Job monitoring and debugging | 3 |
| Job arrays + scaling | 3 |
| Fault-tolerant pipelines (optional chest) | 3 |
| README + project communication | 3 |
| GPU jobs + H200 | 4 |
| Ollama — local LLMs | 4 |
| vLLM / NIM concept | 4 |
| Privacy / data governance | 4 |
| Agent risks | 4 |
