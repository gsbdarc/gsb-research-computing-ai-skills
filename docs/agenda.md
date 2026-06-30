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

### Core Concepts
- What is research computing, a server, a terminal?
- The Unix file system and why researchers live in it
- Files, folders, local vs remote machine
- Staying organized: strategy when a PI sends a raw data dump
- Version control with Git; using Claude Code in the repo (add a skill)
- SSH and remote access; shared vs. dedicated compute
- IDE? VSCode - edit code, git, ssh, AI
- Claude Code: what it sends, Stanford approval, researcher role vs tool role
- Claude + Git hands-on (local)
- Claude on the Yens
- Security discussion

### Main Quests

**Setup block (~20-30 min) — do this before any CLI instruction:**

| # | Quest |
|---|-------|
| 0 | Setup: fork repo → enable Actions → enable GitHub Pages → trigger first build → open personal dungeon site |

*🟢/🔴 sticky check after Quest 0 — everyone should have their site open before proceeding.*

**CLI + cluster:**

| # | Quest |
|---|-------|
| 1 | CLI navigation — `ls`, `cd`, `mkdir`, `mv`, `cp`, `rm` |
| 2 | Bulk operations with wildcards — rename 300 files in one command |
| 3 | SSH into the Yens |
| 4 | Explore cluster: file system, quotas, `module load` |
| 5 | File transfer: `scp` data to and from the cluster |
| 6 | Git: commit and push to fork |
| 7 | Introduce Claude Code — run in repo, discuss researcher role vs AI tool, Stanford data rules |

### Side Quests *(optional)*
- Add here


## Day 2 — Python, AI Tools & the LLM Pipeline

**Theme:** Python + AI Tools — write and run a real extraction script

### Core Concepts
- JupyterHub: brief orientation; notebooks vs. scripts — scripts are the primary workflow
- Python environments: `$PATH`, `module load`, `venv`, `pip`, reproducibility
- Stanford AI Playground: web GUI and API gateway; what leaves the cluster; tokens, costs, context windows
- Secure key management: `.env`, `python-dotenv`, `.gitignore`
- Structured LLM output: Pydantic models and validation
- AI coding agents at Stanford: data privacy, security, best practices *(discussion)*

### Main Quests

| # | Quest |
|---|-------|
| 1 | Open JupyterHub briefly; write and run a Python script from the terminal |
| 2 | Understand `$PATH`; create venv; install packages; register Jupyter kernel |
| 3 | Explore Stanford AI Playground web GUI |
| 4 | Load API key from `.env`; initialize OpenAI-compatible client |
| 5 | First API call: extract fields from one SEC filing; validate with Pydantic; save to JSON |
| 6 | Discussion: AI coding agents at Stanford — data privacy, security, best practices |
| 7 | Update `README.md` with pipeline description; commit and push | 

### Side Quests *(optional)*
- Prompt engineering: system vs. user messages, temperature, reasoning
- Batch processing preview: loop over a directory before Day 3
- Add here

---

## Day 3 — The Cluster: SLURM & Batch Computing

**Theme:** Slurm; submit same python script

### Core Concepts
- The kitchen analogy: CPU (burners), RAM (fridge), shared storage (warehouse), SLURM (head chef)
- Resource estimation: measure wall time and memory before writing `#SBATCH` directives
- System data: analyze real cluster data (userload, sacct, ps) to understand CPU/RAM/process/user patterns
- Why parallelize? Independent tasks → same wall time × N cores
- Job lifecycle: submit → queue → run → complete → logs
- Job monitoring: `squeue`, `sacct`, `scancel`, reading output files

### Timing (3 hours)

| # | Quest | Time |
|---|-------|------|
| 1 | Kitchen demo | 25 min |
| NEW | The Data Mine: analyze real Yens system data with an AI agent | 35 min |
| 2+3 | Profile Day 2 script + profile mystery script | 30 min |
| 4 | Write + submit `jobs/extract.sh` | 25 min |
| 6 | Chronicle: write README while job runs | 20 min |
| 5 | Watch Tower: `sacct` after job completes | 15 min |
| BG | Boss Gate 3: commit + push | 15 min |
| — | Transitions | 10 min |

*After Quest 4 (`sbatch`), send students to Quest 6 (Chronicle) while the job queues. Return to Quest 5 (Watch Tower / `sacct`) once the job is COMPLETED.*

### Main Quests

| # | Quest |
|---|-------|
| 1 | Kitchen demo |
| NEW | The Data Mine: dig into `yens_sample.txt`; find CPU/RAM/process/user patterns using an AI agent or notebook |
| 2 | Profile Day 2 script: `time`, `htop -u $USER`, `userload` |
| 3 | Profile mystery script from a second terminal |
| 4 | Write `jobs/extract.sh` with `#SBATCH` directives; `sbatch` it |
| 5 | Monitor: `squeue`; retrieve output: `sacct`; cancel a job: `scancel` |
| 6 | Update `README.md` with SLURM instructions; commit and push | 

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

| # | Quest |
|---|-------|
| 1 | Convert day3 script to an array job; one task per filing; collect all results |
| 2 | Submit GPU job to `yen-gpu4` (H200); verify with `nvidia-smi` |
| 3 | Run 5 filings through both Playground and Ollama; save side-by-side comparison |
| 6 | Discussion: when to use local models vs third-party vs Playground? |
| 7 | Finalize `README.md` — full pipeline, both endpoints, how to rerun; commit and push | 

### Side Quests *(optional)*
- Add here
