# RF Coding Bootcamp 2026 — Agenda

**Stanford GSB DARC &nbsp;·&nbsp; 4 days &nbsp;·&nbsp; ~3 hours/day**

*Hands-on throughout. Each day ends with a Boss Gate — a capstone challenge you must push to GitHub to unlock the next floor.*

---

## 🔬 The Running Research Project

Every day adds a layer to **one research pipeline**. The dataset: SEC Form 3 filings — public disclosures of insider transactions. By Day 4, you'll have a fully documented, GPU-powered extraction pipeline running at scale on the Yens cluster.

Your `README.md` is a living document. It starts as a file inventory on Day 1 and ends as a production-grade pipeline description on Day 4. Each boss gate requires pushing an updated README.

| Day | What you add to the project |
|-----|-----------------------------|
| Day 1 | Organize the raw data dump. Write the first README. |
| Day 2 | Write the LLM extraction script. Process one filing. Update README. |
| Day 3 | Scale to hundreds of filings with a SLURM array job. Update README. |
| Day 4 | Swap to a local GPU model. Compare outputs. Final README. |

---

## Day 1 — Research Computing Foundations

**Theme:** Get oriented, get organized, get to the cluster.

### Why This Bootcamp?
- What is research computing, and why does it matter for pre-docs?
- What is a server? How is it different from your laptop?
- What is a terminal, and why do researchers use it?
- How to be effective: habits that compound across a research career

### Concepts
- The Unix file system: paths, permissions, directories
- Shared vs dedicated compute: why the Yens cluster exists
- Version control as a lab notebook: Git for reproducible research
- Project organization: the first thing to do when a PI sends a data dump

### Hands-on Exercises
1. CLI navigation: `ls`, `cd`, `mkdir`, `mv`, `cp`, `rm`, `find`
2. Bulk operations: rename 50 files with wildcards in one command (by hand vs in the terminal — same task, compare the experience)
3. SSH into the Yens cluster
4. Explore the cluster: file system layout, storage quotas, loading software modules
5. File transfer: `scp` data between laptop and cluster
6. Git: fork the bootcamp repo, clone it, make a commit, push

### 📁 Project Milestone — Day 1
> Receive a raw dump of SEC filing files with no structure. Organize them into a logical directory layout. Write `README.md` describing what you did and why. Commit and push.

### 🔑 Boss Gate 1
Organized project committed to GitHub.

---

## Day 2 — Python, AI Tools & the LLM Pipeline

**Theme:** From a Jupyter notebook to a working AI research pipeline.

### Concepts
- JupyterHub: notebooks vs. scripts, kernel setup, the Jupyter terminal
- Python environments: virtual environments, `pip`, reproducibility
- `$PATH`: how the shell finds programs; what `module load` and `venv activate` do to it
- Stanford AI Playground: web GUI and API gateway; what leaves the cluster and to where
- Tokens, costs, and context windows: the economics of every API call
- AI coding agents at Stanford: data privacy and security, best practices *(30-min discussion block)*
- Human vs. LLM: when AI helps, when humans win, how to validate at scale

### Hands-on Exercises
1. Connect to JupyterHub on the Yens; run first notebook cells; write a Python script and run it from the terminal
2. Load and unload software modules; observe how `$PATH` changes before and after `source venv/bin/activate`
3. Create a virtual environment; `pip install openai pydantic python-dotenv`; install a Jupyter kernel
4. Explore the Stanford AI Playground web GUI (aitools.stanford.edu)
5. Load the API key securely from `.env`; add `.env` to `.gitignore`; initialize an OpenAI-compatible client
6. First API call: send one SEC Form 3 filing to the LLM, extract `insider_name` and `role`
7. Add a Pydantic model; validate and serialize the LLM response to clean JSON
8. Refactor notebook code into a `.py` script; run it from the terminal
9. Discussion block *(30 min)*: AI coding agents at Stanford, data privacy and security, best practices; human vs. LLM decision framework

### 📁 Project Milestone — Day 2
> `scripts/extract_filing.py` added — processes one filing, returns validated JSON. `README.md` updated with pipeline description and how to run the script. Committed and pushed.

### 🔑 Boss Gate 2
Working LLM extraction script pushed to GitHub, returning structured output.

---

## Day 3 — The Cluster: SLURM & Batch Computing

**Theme:** Stop running big jobs on the shared kitchen — learn the scheduler.

### Concepts
- The kitchen analogy: CPU cores (burners), RAM (fridge), shared storage (warehouse), SLURM (head chef)
- Resource estimation: measure wall time and memory before writing `#SBATCH` directives
- Job lifecycle: submit → queue → run → complete → logs
- Job arrays: one script, one `--array` flag, hundreds of inputs running in parallel

### Hands-on Exercises
1. Kitchen demo *(30-min live class participation)*: run `userload` and `htop`, watch live resource contention across the cluster
2. Profile your Day 2 script: `time python extract_filing.py`, watch memory with `htop -u $USER`
3. Profile a mystery script: monitor CPU and RAM simultaneously from a second terminal
4. Write a SLURM batch script (`jobs/extract.sh`) with `#SBATCH` directives; submit with `sbatch`
5. Monitor with `squeue`; audit completed jobs with `sacct`; cancel a job with `scancel`
6. Convert to a job array: `#SBATCH --array=1-100`, one task per filing, collect all results

### 📁 Project Milestone — Day 3
> `jobs/extract.sh` (single job) and `jobs/array_extract.sh` (array job) added. Results from all filings in `results/`. `README.md` updated with SLURM instructions and how to rerun the array. Committed and pushed.

### 🔑 Boss Gate 3
Array job complete, results committed, README updated.

---

## Day 4 — Scaling Up: Arrays, GPUs & Local LLMs

**Theme:** One job is a proof of concept. A pipeline is research.

### Concepts
- GPU tiers on the Yens: A30 / A40 / H200 — VRAM, use cases, when the queue wait is worth it
- Local LLMs with Ollama: model weights run on cluster hardware, nothing leaves the Yens
- The OpenAI-compatible API: swapping `base_url` is the only code change between all endpoints
- LLM access pattern decision: local Ollama vs. Stanford AI Playground vs. third-party APIs
- Agent failure modes: hallucination at scale, runaway loops, prompt injection, irreversibility

### Hands-on Exercises
1. Submit a GPU job to `yen-gpu4` (H200); verify GPU access with `nvidia-smi` and a PyTorch CUDA check
2. Pull `llama3.2:3b` with Ollama; start `ollama serve` in a `screen` session; confirm the server is running
3. Swap `base_url` in your Day 2 script to point at the local Ollama server — same code, different endpoint
4. Run the same 5 filings through both Playground and Ollama; save side-by-side in `results/comparison.csv`
5. Class discussion: which model was more accurate? Which endpoint is appropriate for restricted data? When would you use each?

### 📁 Project Milestone — Day 4
> `results/comparison.csv` added (Playground vs. Ollama outputs side-by-side). `README.md` finalized — describes the full pipeline from raw data to GPU-powered extraction, both endpoints, and how to rerun everything. Committed and pushed.

### 🔑 Boss Gate 4
Full pipeline documented and pushed — raw data in, structured results out, README tells the story.

---

*Questions? Reach out to the DARC team — we're here all week.*
