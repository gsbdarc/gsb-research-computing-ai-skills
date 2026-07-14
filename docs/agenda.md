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
- Job lifecycle: submit → queue → run → complete → logs
- Job monitoring: `squeue`, `sacct`, `scancel`, reading output files

### Timing (3 hours)

| Room | Time |
|---|---|
| The Kitchen (demo) | 25 min |
| The Scales (profile Day 2 script + profile mystery script) | 30 min |
| The Storage Pantry (analyze real Yens system data with an AI agent) | 35 min |
| The Ticket Rail (write + submit `slurm/extract_form_3_one_file.slurm`) | 25 min |
| Failed Order (`sacct` after job completes) | 15 min |
| The Recipe Book (write README) | 20 min |
| Boss Gate 3 (commit + push) | 15 min |
| Transitions | 10 min |

### Room-by-Room Outline

| Room | Main Quest(s) | Side Quest(s) | Skills Learned | Hands-on Exercise |
|---|---|---|---|---|
| **The Kitchen** | Class demo + discussion: laptop vs. Yens vs. cloud (CPU, RAM, storage tradeoffs) | Compare your own laptop's cores/RAM to a Yen node; estimate cloud $/hr for the Day 2 job | Shared vocabulary for CPU, RAM, and storage across environments | Demo + discussion — no hands-on exercise on this page |
| **The Scales** | Profile a mystery script with `time`, `watch userload`, and `htop` (serial vs. parallel); document resource needs in README | Profile your own research script; compare `/usr/bin/time -v`'s peak RAM to `userload`'s; profile an I/O-bound script and compare `sys` vs. `user` time | Profiling methodology; estimating resources instead of guessing | Two-terminal live profiling technique |
| **The Storage Pantry** | Load the real yenstop CSV snapshot, explore it, and write up one finding in README | Make a plot/visualization; group processes by user and check against the per-user limits from The Scales | Real cluster data literacy; plain-language scientific write-up | Explore a real monitoring CSV with pandas/Claude |
| **The Back Kitchen** | Read `squeue`, filter by partition, explain `R` vs. `PD` | `sinfo` (partitions/node states); `longsqueue` alias; `scontrol show job`; compare a GPU vs. CPU partition request | Why SLURM exists; interactive vs. scheduled Yen nodes | Read and filter the live SLURM queue |
| **The Ticket Rail** | Write a SLURM script from scratch (shebang, `#SBATCH` directives, env setup, run command); submit, monitor, and cancel a job | Email notifications (`--mail-type=ALL`); interactive allocation (`srun --pty`); job dependency chaining (`--dependency=afterok`) | Writing a SLURM script line by line; managing a job's full lifecycle | Write, submit, and cancel a real SLURM job |
| **Failed Order** | Debug a failed job: read `sacct`/logs, fix the bug, resubmit to `COMPLETED` | Audit requested vs. actual resource usage; follow a live job with `tail -f`; decode `ExitCode`; deliberately trigger an OOM kill | Debugging methodology; recognizing failure signatures (code bug vs. OOM) | Real debug → fix → resubmit loop on a failing job |
| **The Recipe Book** | Write a README covering what the script does, how to run it, and where output lands | Have Claude critique the README as a first-time reader; write a plain-language summary for a non-technical audience | Technical documentation habits; AI-assisted review; research communication | Write a full README from a template while the work is fresh |
| **Boss Gate 3** | Commit and push the SLURM script + README (capstone) | Manually rerun against a few more filings; describe what breaks at scale (primes Day 4's job arrays) | Synthesize the day: profiling → SLURM → debugging → documentation → commit | Full pipeline submission, backed by real measurements |

---

## Day 4 — Scaling to a Reproducible Research Pipeline

**Theme:** Scaling and making research pipeline reproducible

### Core Concepts
- Why parallelize? Independent tasks → same wall time × N cores (job arrays)
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
