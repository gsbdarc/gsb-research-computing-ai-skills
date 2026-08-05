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
- LLM-as-a-judge: scale a research **judgment call** by having a *second, different* model check the first one's label, blind to its reasoning, and report agreement + certainty; then flag the contested cases for human review — the escalation *policy lives in your code, not the prompt* (auditable). Agreement is consistency, not accuracy.
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
| Day 2 Challenge *(optional capstone)* | The Genre Tribunal: classify a movie's genre with model A → have model B check it blind (agreement + certainty) → flag `needs_human_review` in your code → report agreement rate → commit `results/genre_verdicts.json` |

### Side quests
- Prompt engineering: system vs. user messages, temperature, reasoning
- Batch processing preview: loop over a directory before Day 3
- Add here

---

## Day 3 — Cluster Computing

**Theme:** Slurm and batch computing on the cluster

### Core Concepts
- Compute resources: CPU cores, RAM, shared storage, and why a shared cluster needs a scheduler (Slurm)
- Resource estimation: measure wall time and memory before writing `#SBATCH` directives
- System data: analyze a real Yens `top`/yenstop snapshot (and live `top`) to understand CPU/RAM/process/user patterns, and per-user vs. whole-node limits
- Job lifecycle: submit → queue → run → complete → logs
- Job monitoring: `squeue`, `sinfo`, `sacct`, `scancel`, reading `.out`/`.err` logs

### Timing (9 am–12 pm — 3 hours incl. two 10-min breaks; ~160 min teaching)

Live pace is **main-quest-focused** (side quests are the buffer for students who finish early). The four big blocks — Compute (demo), Profiling, Slurm Job, Capstone — get 30 min each; the four lighter sections are brisk at 10. Two breaks — after Profiling (10:00) and after the Slurm Job section (11:00) — split the morning into ~60 / 50 / 50-min blocks. See `.instructor/day3-teaching-plan.md` for the full run-of-show.

| Section | Quests | Time |
|---|---|---|
| Compute Environments (demo + discussion) | 3 | 30 min |
| Profiling Resource Usage (two-terminal live profiling; document resource needs) | 5 | 30 min |
| ☕ **Break** | — | 10 min |
| Exploring Cluster Usage Data (analyze a real Yens yenstop snapshot with Claude) | 3 | 10 min |
| The Slurm Scheduler (why Slurm exists; read the queue + partitions with `squeue`/`sinfo`) | 4 | 10 min |
| Writing & Submitting a Slurm Job (write + submit + monitor + cancel; debug broken `fix_me*.slurm` jobs) | 11 | 30 min |
| ☕ **Break** | — | 10 min |
| Writing a Slurm Job with Claude (distill a global Yen skill from the job just run; make a figure, then distill a project plotting skill from it and invoke it; plus `claude -p` non-interactive mode) | 2 | 10 min |
| Documenting Your Pipeline (write the README) | 2 | 10 min |
| Day 3 Capstone (estimate resources for 100 filings *before* running, batch-submit, compare actual vs. estimate, document) | 1 | 30 min |

*If students finish the Capstone early: sync to climb the leaderboard, revisit skipped quests, and bring any lingering Day 3 questions to the instructors.*

### Section-by-Section Outline

| Section | Main quest(s) | Side quests | Skills Learned | Hands-on |
|---|---|---|---|---|
| **Compute Environments** | Class demo + discussion: laptop vs. Yens vs. cloud (CPU, RAM, storage tradeoffs) | Compare your laptop's cores/RAM to a Yen node; estimate cloud $/hr for the Day 2 job; use the laptop-vs-Yen widget | Shared vocabulary for CPU, RAM, and storage across environments | Demo + discussion |
| **Profiling Resource Usage** | Profile a mystery script with `time`, `watch userload`, and `htop` (serial vs. parallel); document resource needs in README | Vectorized vs. non-vectorized profiling; compare `/usr/bin/time -v`'s peak RAM to `userload`'s; profile an I/O-bound script (`sys` vs. `user` time) | Profiling methodology; estimating resources instead of guessing | Two-terminal live profiling |
| **Exploring Cluster Usage Data** | Load the real yenstop CSV, explore it (e.g. the biggest process in GB given yen1's ~1 TB RAM), and write up one finding in README | Make a plot; compare per-user usage against both the per-user limit and the whole node; run `top` live | Real cluster-data literacy; per-user vs. system limits; plain-language write-up | Explore a monitoring CSV with pandas/Claude; watch live `top` |
| **The Slurm Scheduler** | Read the queue with `squeue`, filter by partition, explain `R` vs. `PD`, and describe partitions/node states with `sinfo` | `longsqueue` alias; `scontrol show job`; compare a GPU vs. CPU partition | Why Slurm exists; interactive vs. scheduled nodes; partitions | Read and filter the live Slurm queue |
| **Writing & Submitting a Slurm Job** | Write a Slurm script from scratch (shebang, `#SBATCH` directives, `.out`/`.err` logs, env setup, run command); submit, monitor, and cancel a job; watch a job run on its node with `htop` | Email notifications (`--mail-type=ALL`); interactive allocation (`srun --pty`); job dependency chaining; the `dev` partition; **debug broken `fix_me*.slurm` jobs** to `COMPLETED` | Writing a Slurm script line by line; managing a job's lifecycle; reading logs; telling a Slurm setup bug from a code bug when a job fails | Write, submit, cancel, watch, and debug real Slurm jobs |
| **Writing a Slurm Job with Claude** | The "do the work, then distill a skill" pattern, twice: (1) have Claude capture the reusable Yen conventions from the job you just ran into a **global** skill (`~/.claude/skills/yen-slurm` — partitions/RCpedia, email, `%j` logs, always specifying `--time`/`--mem`/`--cpus-per-task`), then invoke it on a fresh job; (2) work with Claude to plot the letter distribution across the 10 filings' extracted fields (submitted via `slurm/plot.slurm`), then distill that figure's house style into a **project** skill (`.claude/skills/form3-plots`) and invoke it on a different plot | — | Authoring reusable Claude skills from work you've done; project vs. global scope; conventions beyond Slurm (a figure house style); reviewing an agent's output | Claude writes two SKILL.md skills; you make a real plot, distill its style, and re-invoke; you review |
| **Documenting Your Pipeline** | Write a README covering what the script does, how to run it, and where output lands | Have Claude stress-test your README as a first-time reader; explain it to your PI in plain language | Technical documentation habits; AI-assisted review; research communication | Write a full README while the work is fresh |
| **Day 3 Capstone** | Estimate CPU/RAM/time for 100 filings and write the estimate (which resources scale + why) in the README *before* running; bump the existing `slurm/extract_form_3_batch.slurm` to 100 (re-tuning resources) with email notifications; submit and confirm; compare actual (email/`sacct`) vs. estimate and document over/under; commit and push via Claude Code | — | Estimating a larger run before submitting, then checking the estimate against reality; synthesizing profiling → Slurm → debugging → docs | Full 100-filing batch submission, backed by real measurements |

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

### Timing (9 am–12 pm — 3 hours incl. two 10-min breaks; ~160 min teaching)

Two hands-on blocks carry the day — the array exercise and the Challenge — at 35 min each. The two LLM concept pages are brisk; Failure Modes gets 30 because it opens with a discussion the room supplies. Breaks fall after the array exercise (9:55) and after Failure Modes (11:10), splitting the morning into ~55 / 65 / 40-min blocks.

| Section | Quests | Time |
|---|---|---|
| Parallelization Basics (concepts, plus three worked examples for discussion) | 2 | 20 min |
| Slurm Job Arrays (write and submit an array; watch it in `squeue`; make a task safe to rerun) | 4 | 35 min |
| ☕ **Break** | — | 10 min |
| Why Run LLMs on the Yens? (local vs. Gateway vs. third-party; open vs. proprietary weights) | 1 | 10 min |
| How to Run LLMs on the Yens (query the shared server; GPU vs. CPU timing demo; GPU tiers and `srun --pty`) | 3 | 25 min |
| Handling LLM Failure Modes (crowdsource failure modes, then run two models over the same filings and compare) | 2 | 30 min |
| ☕ **Break** | — | 10 min |
| Day 4 Challenge (all 992 filings through an array, against a 512-task cap) | 1 | 35 min |
| Staying In Touch (Slack, DARC email, where to go next) | — | 5 min |

*If students finish the Challenge early: sync to climb the leaderboard, and go back for the optional practice on job arrays and on agent guardrails.*

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
