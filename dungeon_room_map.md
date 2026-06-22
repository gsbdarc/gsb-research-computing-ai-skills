# DARC Dungeon — Room Map & Learning Objectives

**Grimoire file format:** `fireball_fire_3_offensive_meteor.spell`
`name_element_tier_type_mastery.spell`
Elements: fire / ice / lightning / earth / wind
Types: offensive / defensive / utility / healing

Each hands-on block is a **dungeon room**. Every room has:
- 🗡️ **Main quest** — required, everyone does this
- 📦 **Chests** — finish early? go deeper on the same skill, unlock a named weapon
- 🧠 **Skills learned** — what the researcher takes away (the learning objective)
- 🔑 **Boss Gates** — floor exits, require all main quests on that floor

Weapons are cumulative: a skill unlocked in Day 1 pays off in Day 3 and beyond.

---

## Day 1 — The Gatehouse *(Levels 1–3)*

| Room | 🗡️ Main quest | 📦 Chests → weapons unlocked | 🧠 Skills learned |
|---|---|---|---|
| **The Command Spire** | `pwd ls cd mkdir cp mv` on your laptop | 🗡️ Grep Blade: `grep`, pipes, `sort`, `uniq` / ⚔️ Shell Rune: `sed`, for loops / 🏆 Arcane Blade: write a reusable `.sh` script | Navigate any Unix file system; understand absolute vs. relative paths |
| **The Grimoire Vault** | Sort spell files by element using wildcards | 🗡️ Wildcard Wand: find rarest element+type combo / ⚔️ Find Familiar: `find -exec` / 🏆 Awk Sigil: generate a full spell inventory | Manipulate hundreds of files in bulk using patterns and wildcards |
| **The SSH Gate** | `ssh` onto the Yens, identify your node | 🗡️ SSH Sigil: `~/.ssh/config` alias — type `ssh yen`, nothing else | Connect to a remote server; understand what a login node is |
| **The Cartographer's Room** | `/scratch`, `gsbquota`, `gsbbrowser`, `module avail` | 🗡️ Module Lens: `module spider`, find a hidden module | Understand cluster file system layout; know where data lives, how much space you have, and why |
| **The Scroll Transfer** | `scp` your grimoire up to the Yens | 🗡️ Rsync Rune: `rsync` instead of `scp`, understand the difference | Move data between local and remote; understand the shared file system |
| **The Repository** | `git clone` the course repo, create a branch, `add` + `commit` + `push` a file — required for every Boss Gate | 🗡️ History Lens: `git log --oneline`, `git diff`, `git status` / ⚔️ Stash Spell: `git stash` for mid-task interruptions / 🏆 Blame Blade: `git blame` to understand who changed what and why | Version-control every project from day one; understand the fork → branch → commit → push → PR workflow; know why git is non-negotiable for reproducible research |
| **The Arcane Notebook** | Open JupyterHub, run a cell | 🗡️ Magic Scroll: keyboard shortcuts, `%time` / ⚔️ Shell Tome: `%%bash` cell, run shell from inside Jupyter / 🏆 Vim Sigil: Vim keybindings mode in Jupyter | Run code on cluster hardware from a browser; understand what a kernel is |
| **The Primer Chamber** | AI primer — token, prompt, LLM, agent (4 pictures) | 💬 Discussion — no chest | Have a working mental model of how LLMs work before touching one |
| 🔑 **Boss Gate 1** | Find the Archmage's signature spell hidden in `/scratch/…/vault/`. Commit `signature_spell.txt` | — | Use CLI + SSH + shared file system together to solve an open-ended search problem |

---

## Day 2 — The Alchemist's Lab *(Levels 4–6)*

| Room | 🗡️ Main quest | 📦 Chests → weapons unlocked | 🧠 Skills learned |
|---|---|---|---|
| **The Venv Forge** | Create venv, activate, install packages, connect kernel | 🗡️ Freeze Flask: `requirements.txt`, `pip freeze` / ⚔️ Editable Elixir: `pip install -e .` / 🏆 Pyenv Potion: `pyenv` for multiple Python versions | Isolate Python dependencies per project; never break another project's environment |
| **The Path Labyrinth** | `$PATH`, `which`, `module load` | 🗡️ Profile Rune: `~/.bash_profile` that sets your environment automatically | Know why the same command behaves differently in different contexts |
| **The Key Vault** | Stanford AI Playground — what it is, why it exists, data governance; load key from `.env` with `python-dotenv` | 🗡️ Shield of `.gitignore`: never commit a secret / ⚔️ Keyring Knife: `keyring` for OS-level secret storage | Understand the Stanford AI Playground: walled garden, Stanford data perimeter, budget caps, approved models, audit logs — and why this matters vs. a personal API key |
| **The Watchtower of Secrets** | Security best practices: what cloud APIs log (prompts, metadata), key rotation + revocation, what the Playground guarantees that a personal key does not, PII and the three-bucket rule preview | 💬 Discussion + checklist exercise — no chest | Know what leaves your machine every time you make an API call; apply a pre-flight security check to any new dataset before sending it to a cloud API |
| **The AI Scribe** | Claude Code — what it is, install + configure, use it to write a Python script for the Yens, understand when to trust and when to verify suggestions | 🗡️ Prompt Blade: write an effective coding prompt / ⚔️ Context Tome: feed Claude Code a SLURM script, ask it to explain + improve | Use AI-assisted coding as a research tool; verify AI output rather than blindly trust it; understand the security implications of pasting cluster code into an AI tool |
| **The Oracle's Chamber** | LLM call on one SEC Form 3 — extract name + role | 🗡️ Model Mirror: try two models, compare outputs / ⚔️ Stream Stone: streaming response / 🏆 Async Arrow: `asyncio` batch calls | Call any OpenAI-compatible API from Python; choose a model intentionally |
| **The Binding Room** | Pydantic structured output from the same filing | 🗡️ Nested Tome: nested models, optional fields / ⚔️ Retry Rune: validation errors + retry logic / 🏆 Schema Shield: export JSON schema | Extract structured data from unstructured text reliably; validate and type LLM output |
| **The Ledger** | When NOT to use an LLM — cost intuition | 💬 Discussion — no chest | Apply "regex first, LLM second"; estimate API cost before running at scale |
| **The Persistence Chamber** | `screen` for long-running sessions — detach, reattach | 🗡️ Screen Scroll: split windows, `~/.screenrc` config | Run a script that outlasts your SSH session; come back tomorrow and it's still running |
| 🔑 **Boss Gate 2** | Mood Ring Scroll — 5 earnings calls → structured JSON, committed to fork | — | Build a complete LLM research pipeline end-to-end: load data → prompt → structured output → save results |

---

## Day 3 — The SLURM Mines *(Levels 7–8)*

| Room | 🗡️ Main quest | 📦 Chests → weapons unlocked | 🧠 Skills learned |
|---|---|---|---|
| **The Kitchen** | Why batch scheduling — live demo: show `userload` and `htop` on the Yens right now, then kitchen analogy | 🖊️💻 20 min minimum | Understand why batch scheduling exists; see resource contention live before writing a single SLURM script |
| **The Scales** | Estimate resources: `time`, `htop`, `userload` | 🗡️ Sacct Scythe: `sacct` post-mortem on any job / ⚔️ Seff Sigil: `seff` efficiency report | Measure before you request; know what your script actually costs in cores, memory, and time |
| **The Foreman's Desk** | Write + submit first `sbatch`, read the log | 🗡️ Mail Medallion: `--mail-type` notifications / ⚔️ Template Tome: job script with `$1` argument so one script handles any input | Write a SLURM script from scratch; understand every directive |
| **The Watch Tower** | `squeue`, `scancel`, `sacct` | 🗡️ Watch Wand: `watch -n 5 squeue -u $USER` live loop | Monitor, cancel, and audit batch jobs without staring at a terminal |
| **The Trap Room** | Spot-the-Bug speed round | 💬 Class shouts — no chest | Recognize the three most common SLURM failure modes before they cost you queue time |
| **The Array Cavern** | Job array over 100 inputs, combine outputs into one CSV | 🗡️ Dependency Dagger: `--dependency=afterok` chained jobs / 🗡️ Dynamic Draught: generate array from a file list at runtime / ⚔️ Checkpoint Charm: log completed IDs, skip already-done on rerun / 🏆 Siege Scale: go from 100 → 10,000 inputs, organize outputs into dated subdirectories | Scale one script to thousands of inputs; aggregate parallel results cleanly; (optional) write pipelines that survive partial failures |
| **The Chronicle** | Write a README for your pipeline: what it does, how to run it, what it produces, known limitations | 🗡️ Structure Sigil: standard research project layout (`data/`, `scripts/`, `results/`) / ⚔️ Changelog Charm: CHANGELOG.md for tracking what changed between runs | Communicate your work clearly enough that a collaborator — or future you — can reproduce it; README as research artifact, not afterthought |
| 🔑 **Boss Gate 3** | Great Scroll Sweep — 100 filings via array → CSV + README, committed to fork | — | Run a real research pipeline at scale: parallel jobs, combined output, resource audit, documented |
| **Hall of Heroes** | Live `userload` + `squeue` on the projector — celebrate fastest array, best quest job name, first full Quest Log | 💬 Celebration — no chest | — |

---

## Day 4 — The GPU Fortress *(Levels 9–10)*

| Room | 🗡️ Main quest | 📦 Chests → weapons unlocked | 🧠 Skills learned |
|---|---|---|---|
| **The Armory** | GPU partition tour — A30 / A40 / H200 (whiteboard) | 💬 Discussion — no chest | Know what GPUs are on the Yens, what each is good for, and how to request one |
| **The H200 Chamber** | First GPU job (`--gres=gpu:1 --nodelist=yen-gpu4`) | 🗡️ Smi Sight: `nvidia-smi` inside the job / ⚔️ Benchmark Blade: same script on A30 vs H200, compare wall time | Submit and run a GPU-accelerated job; understand GPU memory and why model size matters |
| **The Summoning Circle** | Ollama — pull a model, chat from Jupyter | 🗡️ Model Menagerie: compare 3 models on speed + quality / ⚔️ Modelfile Magic: custom system prompt via Modelfile / 🏆 Throughput Tome: benchmark requests/sec from H200 | Host a local LLM on cluster hardware; understand when local beats cloud |
| **The Engine Room** | vLLM and NIM on H200 — concept + demo, no hands-on; "Ollama for prototyping, vLLM/NIM for production traffic" | 💬 Discussion — no chest | Understand the production-grade local LLM stack; know when to graduate from Ollama |
| **The Grand Hall** | Privacy buckets — 3-bucket rule + classify your own datasets (5 min exercise) | 💬 Discussion + exercise — no chest | Apply the 3-bucket rule (public / restricted / PII) to your own research datasets; know when cloud API is off-limits |
| **The Trap Garden** | Agent risks — hallucination at scale, runaway loops, prompt injection, irreversibility | 💬 Discussion — no chest | Name 4 LLM agent failure modes and a concrete defense for each |
| 🔑 **Boss Gate 4** | Champion's Ascent — swap Day 3 pipeline to Ollama endpoint, compare outputs, update README with Ollama changes, commit | 🎓 Graduation | Demonstrate the full stack: cluster → SLURM → GPU → local LLM → structured output → documented |

---

## The weapons rack — cumulative skills across all 4 days

What a student who opens every chest walks away with, organized by domain:

| Domain | Weapons earned |
|---|---|
| **Shell** | Grep Blade · Wildcard Wand · Shell Rune · Rsync Rune · Arcane Blade |
| **Remote access** | SSH Sigil · Module Lens · Screen Scroll |
| **Version control** | History Lens · Stash Spell · Blame Blade |
| **Python env** | Freeze Flask · Editable Elixir · Pyenv Potion · Profile Rune |
| **Security** | Shield of `.gitignore` · Keyring Knife |
| **AI Playground + APIs** | Model Mirror · Stream Stone · Async Arrow |
| **AI-assisted coding** | Prompt Blade · Context Tome |
| **Data extraction** | Nested Tome · Retry Rune · Schema Shield |
| **SLURM + scaling** | Sacct Scythe · Mail Medallion · Template Tome · Watch Wand · Dependency Dagger · Checkpoint Charm · Siege Scale |
| **Documentation** | Structure Sigil · Changelog Charm |
| **GPU + local LLMs** | Smi Sight · Benchmark Blade · Model Menagerie · Modelfile Magic · Throughput Tome |

Basic quest only → Level 10 graduate.
Every chest opened → fully equipped researcher.

---

## Open decisions

1. **Grimoire file attributes** — confirm: `name_element_tier_type_mastery.spell` with elements fire/ice/lightning/earth/wind?
2. **Quest Log card** — printed card (mark off rooms + chests as you go) or digital tracker on the course site?
3. **Chest instructions** — written walkthrough on the site, or just a one-line prompt and students figure it out (Python Challenge style)?
4. **Day 4 pacing** — privacy + agents + MCP is discussion-heavy; is that okay after 3 hands-on days, or should one of the three be trimmed?
