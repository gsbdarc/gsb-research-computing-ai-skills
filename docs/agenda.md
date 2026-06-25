# RF Coding Bootcamp 2026 — Instructor Planning Agenda

## The Running Research Project

Every day adds a layer to one research pipeline. The dataset: SEC Form 3 filings — public disclosures of insider transactions. The `README.md` is a living document updated each day.

| Day | Project milestone |
|-----|-------------------|
| Day 1 | Organize raw data dump. Write first README. |
| Day 2 | Write LLM extraction script. Process one filing. Update README. |
| Day 3 | Submit first SLURM batch job. Update README. |
| Day 4 | Scale with job arrays. Add GPU and local LLM. Final README. |

---

## Day 1 — Research Computing Foundations

**Theme:** Get oriented, get organized, get to the cluster.
**Duration:** ~3 hours

### Core Concepts
- What is research computing, a server, a terminal?
- The Unix file system and why researchers live in it
- Staying organized: strategy when a PI sends a raw data dump
- Version control as a lab notebook
- SSH and remote access; shared vs. dedicated compute

### Main Quests

| # | Quest | Presenter |
|---|-------|-----------|
| 1 | CLI navigation — `ls`, `cd`, `mkdir`, `mv`, `cp`, `rm` | | 
| 2 | Bulk operations with wildcards — rename 50 files in one command | | 
| 3 | SSH into the Yens | | 
| 4 | Explore cluster: file system, quotas, `module load` | 
| 5 | File transfer: `scp` data to and from the cluster | | 
| 6 | Git: fork bootcamp repo, commit, push | | 
| 7 | Organize raw SEC filing data dump; write `README.md`; commit | |

### Side Quests *(optional)*
- Add here


## Day 2 — Python, AI Tools & the LLM Pipeline

**Theme:** Interactive Jobs on the Yens (Jupyter)

### Core Concepts
- JupyterHub: notebooks vs. scripts; kernel setup; the Jupyter terminal
- Python environments: `venv`, `pip`, reproducibility; modules; what `$PATH` is and how it changes
- Stanford AI Playground: web GUI and API gateway; what leaves the cluster; tokens, costs, context windows
- Secure key management: `.env`, `python-dotenv`, `.gitignore`
- Structured LLM output: Pydantic models and validation
- AI coding agents at Stanford: data privacy, security, best practices *(30-min discussion)*

### Main Quests

| # | Quest | Presenter |
|---|-------|-----------|
| 1 | Connect to JupyterHub; run cells; run a script from the terminal | | 
| 2 | Load modules; observe `$PATH`; create venv; install packages; register kernel | | 
| 3 | Explore Stanford AI Playground web GUI | | 
| 4 | Load API key from `.env`; initialize OpenAI-compatible client | | 
| 5 | First API call: extract `insider_name` and `role` from one SEC filing | | 
| 6 | Add Pydantic model; validate and serialize response to JSON | | 
| 7 | Refactor notebook code into `scripts/extract_filing.py`; run from terminal | | 
| 8 | Update `README.md` with pipeline description; commit and push | | 

### Side Quests *(optional)*
- What's LLM? Context, models, tokens, costs, environment, agents, Claude Code 
- Prompt engineering: system vs. user messages, temperature, reasoning
- Batch processing preview: loop over a directory before Day 3 ?
- Add here

---

## Day 3 — The Cluster: SLURM & Batch Computing

**Theme:** Slurm; submit same python script

### Core Concepts
- The kitchen analogy: CPU (burners), RAM (fridge), shared storage (warehouse), SLURM (head chef)
- Resource estimation: measure wall time and memory before writing `#SBATCH` directives
- Job lifecycle: submit → queue → run → complete → logs
- Job monitoring: `squeue`, `sacct`, `scancel`, reading output files

### Main Quests

| # | Quest | Presenter |
|---|-------|-----------|
| 1 | Kitchen demo | |
| 2 | Profile Day 2 script: `time`, `htop -u $USER`, `userload` | | 
| 3 | Profile mystery script from a second terminal | | 
| 4 | Write `jobs/extract.sh` with `#SBATCH` directives; `sbatch` it | | 
| 5 | Monitor: `squeue`; retrieve output: `sacct`; cancel a job: `scancel` | | 
| 6 | Update `README.md` with SLURM instructions; commit and push | | 

### Side Quests *(optional)*
- Email notifications: `#SBATCH --mail-type=ALL`
- Interactive jobs: `srun --pty bash`
- Checkpointing: saving progress mid-job
- Reading `sacct` fields: elapsed time, memory used, exit codes

---

## Day 4 — Scaling to a Reproducible Research Pipeline

**Theme:** Scaling and making research pipeline reproducible

### Core Concepts
- Job arrays: one script, one `--array` flag, hundreds of inputs in parallel
- Fault tolerance: checkpoint log + skip completed files in array jobs
- GPU tiers on the Yens: A30 / A40 / H200 — VRAM and use cases
- Local LLMs: model weights on cluster hardware, nothing leaves the Yens
- The OpenAI-compatible API: swapping `base_url` is the only code change
- Human vs. LLM: when to trust results at scale, how to validate *(discussion)*
- Reproducibility: README as the deliverable that makes a pipeline rerunnable

### Main Quests

| # | Quest | Presenter | 
|---|-------|-----------|
| 1 | Convert day3 script to an array job; one task per filing; collect all results | | 
| 2 | Submit GPU job to `yen-gpu4` (H200); verify with `nvidia-smi` | | 
| 3 | Run 5 filings through both Playground and Ollama; save side-by-side comparison | | 
| 6 | Discussion: when to use local models vs third-party vs Playground? | | 
| 7 | Finalize `README.md` — full pipeline, both endpoints, how to rerun; commit and push | | 

### Side Quests *(optional)*
- Add here
