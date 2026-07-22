# GSB Research Computing & AI Skills — Instructor Planning Agenda

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

### Main quests

**Setup block (~20-30 min) — do this before any CLI instruction:**

| # | Main quest |
|---|-------|
| 0 | Setup: fork repo → enable Actions → enable GitHub Pages → trigger first build → open personal dungeon site |

*🟢/🔴 sticky check after Quest 0 — everyone should have their site open before proceeding.*

**CLI + cluster:**

| # | Main quest |
|---|-------|
| 1 | CLI navigation — `ls`, `cd`, `mkdir`, `mv`, `cp`, `rm` |
| 2 | Bulk operations with wildcards — rename 300 files in one command |
| 3 | SSH into the Yens |
| 4 | Explore cluster: file system, quotas, `module load` |
| 5 | File transfer: `scp` data to and from the cluster |
| 6 | Git: commit and push to fork |
| 7 | Introduce Claude Code — run in repo, discuss researcher role vs AI tool, Stanford data rules |

### Side quests
- Add here


## Day 2 — Python, AI Tools & the LLM Pipeline

**Theme:** Python + AI Tools — write and run a real extraction script

### Core Concepts
- JupyterHub: brief orientation; notebooks vs. scripts — scripts are the primary workflow
- Python environments: `$PATH`, `module load`, `venv`, `pip`, reproducibility
- Reproducibility in practice: rebuild a complex project from `requirements.txt` in a fresh venv (the Potion Brawl example in The Venv Forge) — same recipe, same result, any machine
- Stanford AI Playground: web GUI and API gateway; what leaves the cluster; tokens, costs, context windows
- Secure key management: `.env`, `python-dotenv`, `.gitignore`
- Structured LLM output: Pydantic models and validation
- LLM-as-a-judge: have a model self-evaluate with an agreement + confidence score, then flag low-confidence outputs for human review — the escalation *policy lives in your code, not the prompt* (auditable)
- AI coding agents at Stanford: data privacy, security, best practices *(discussion)*

### Main quests

| # | Main quest |
|---|-------|
| 1 | Open JupyterHub briefly; write and run a Python script from the terminal |
| 2 | Understand `$PATH`; create venv; install packages; register Jupyter kernel; rebuild a complex script from `requirements.txt` to see reproducibility |
| 3 | Explore Stanford AI Playground web GUI |
| 4 | Load API key from `.env`; initialize OpenAI-compatible client |
| 5 | First API call: extract fields from one SEC filing; validate with Pydantic; save to JSON |
| 6 | Discussion: AI coding agents at Stanford — data privacy, security, best practices |
| 7 | Update `README.md` with pipeline description; commit and push |
| Boss Gate 2 *(optional capstone)* | The Genre Tribunal: predict a movie's genre → judge the prediction (agreement + certainty) → flag `needs_human_review` in your code → commit `results/genre_verdicts.json` |

### Side quests
- Prompt engineering: system vs. user messages, temperature, reasoning
- Batch processing preview: loop over a directory before Day 3
- Add here

---

## Day 3 — Cluster Computing

**Theme:** SLURM and batch computing on the cluster

### Core Concepts
- Compute resources: CPU cores, RAM, shared storage, and why a shared cluster needs a scheduler (SLURM)
- Resource estimation: measure wall time and memory before writing `#SBATCH` directives
- System data: analyze a real Yens `top`/yenstop snapshot (and live `top`) to understand CPU/RAM/process/user patterns, and per-user vs. whole-node limits
- Job lifecycle: submit → queue → run → complete → logs
- Job monitoring: `squeue`, `sinfo`, `sacct`, `scancel`, reading `.out`/`.err` logs

### Timing (3 hours ≈ 180 min)

Times are rough, scaled by how many quests each section holds and how hands-on it is (the SLURM job section is the heaviest — 13 quests including debugging). Keep a full **30 min** for the Capstone.

| Section | Quests | Time |
|---|---|---|
| Compute Environments (demo + discussion) | 3 | 20 min |
| Profiling Resource Usage (two-terminal live profiling; document resource needs) | 5 | 30 min |
| Exploring Cluster Usage Data (analyze a real Yens yenstop snapshot with Claude) | 3 | 25 min |
| The SLURM Scheduler (why SLURM exists; read the queue + partitions with `squeue`/`sinfo`) | 4 | 15 min |
| Writing & Submitting a SLURM Job (write + submit + monitor + cancel; debug broken `fix_me*.slurm` jobs) | 13 | 45 min |
| Documenting Your Pipeline (write the README) | 2 | 15 min |
| Day 3 Capstone (estimate resources for 100 filings *before* running, batch-submit, compare actual vs. estimate, document) | 1 | 30 min |

*If students finish the Capstone early: sync to climb the leaderboard, revisit skipped quests, and bring any lingering Day 3 questions to the instructors.*

### Section-by-Section Outline

| Section | Main quest(s) | Side quests | Skills Learned | Hands-on |
|---|---|---|---|---|
| **Compute Environments** | Class demo + discussion: laptop vs. Yens vs. cloud (CPU, RAM, storage tradeoffs) | Compare your laptop's cores/RAM to a Yen node; estimate cloud $/hr for the Day 2 job; use the laptop-vs-Yen widget | Shared vocabulary for CPU, RAM, and storage across environments | Demo + discussion |
| **Profiling Resource Usage** | Profile a mystery script with `time`, `watch userload`, and `htop` (serial vs. parallel); document resource needs in README | Vectorized vs. non-vectorized profiling; compare `/usr/bin/time -v`'s peak RAM to `userload`'s; profile an I/O-bound script (`sys` vs. `user` time) | Profiling methodology; estimating resources instead of guessing | Two-terminal live profiling |
| **Exploring Cluster Usage Data** | Load the real yenstop CSV, explore it (e.g. the biggest process in GB given yen1's ~1 TB RAM), and write up one finding in README | Make a plot; compare per-user usage against both the per-user limit and the whole node; run `top` live | Real cluster-data literacy; per-user vs. system limits; plain-language write-up | Explore a monitoring CSV with pandas/Claude; watch live `top` |
| **The SLURM Scheduler** | Read the queue with `squeue`, filter by partition, explain `R` vs. `PD`, and describe partitions/node states with `sinfo` | `longsqueue` alias; `scontrol show job`; compare a GPU vs. CPU partition | Why SLURM exists; interactive vs. scheduled nodes; partitions | Read and filter the live SLURM queue |
| **Writing & Submitting a SLURM Job** | Write a SLURM script from scratch (shebang, `#SBATCH` directives, `.out`/`.err` logs, env setup, run command); submit, monitor, and cancel a job; watch a job run on its node with `htop` | Email notifications (`--mail-type=ALL`); interactive allocation (`srun --pty`); job dependency chaining; the `dev` partition; **debug broken `fix_me*.slurm` jobs** to `COMPLETED`; audit requested-vs-used; follow a live job with `tail -f`; decode `ExitCode`; trigger an OOM; trigger a timeout | Writing a SLURM script line by line; managing a job's lifecycle; reading logs; telling code-bug vs. OOM vs. timeout failures apart | Write, submit, cancel, watch, and debug real SLURM jobs |
| **Documenting Your Pipeline** | Write a README covering what the script does, how to run it, and where output lands | Have Claude stress-test your README as a first-time reader; explain it to your PI in plain language | Technical documentation habits; AI-assisted review; research communication | Write a full README while the work is fresh |
| **Day 3 Capstone** | Estimate CPU/RAM/time for 100 filings and write the estimate (which resources scale + why) in the README *before* running; write `slurm/extract_form_3_batch.slurm` for 100 with email notifications; submit and confirm; compare actual (email/`sacct`) vs. estimate and document over/under; commit and push via Claude Code | — | Estimating a larger run before submitting, then checking the estimate against reality; synthesizing profiling → SLURM → debugging → docs | Full 100-filing batch submission, backed by real measurements |

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

### Main quests

| # | Main quest |
|---|-------|
| 1 | Convert day3 script to an array job; one task per filing; collect all results |
| 2 | Submit GPU job to `yen-gpu4` (H200); verify with `nvidia-smi` |
| 3 | Run 5 filings through both Playground and Ollama; save side-by-side comparison |
| 6 | Discussion: when to use local models vs third-party vs Playground? |
| 7 | Finalize `README.md` — full pipeline, both endpoints, how to rerun; commit and push | 

### Side quests
- Add here
