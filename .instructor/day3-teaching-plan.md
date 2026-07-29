# Day 3 — Teaching Run-of-Show (9 am–12 pm)

**Instructor use only.** Not served by GitHub Pages. An approximate live pace for Day 3.

3 hours total (9:00–12:00), **including two 10-min breaks** → ~160 min of teaching. You drive the **main quests** live on screen; **side quests are the buffer** — students who finish a main quest early work those while everyone else catches up.

## Schedule

| Clock | Section — what you do live (main quest) | ~min |
|-------|------------------------------------------|------|
| 9:00  | **Compute Environments** — demo + discussion: laptop vs Yens vs cloud (CPU / RAM / storage; the hardware diagram) | 30 |
| 9:30  | **Profiling Resource Usage** — live two-terminal profiling of the mystery script (`time`, `watch userload`, `htop`; serial vs parallel, CPU- vs I/O-bound), then document resource needs in the README | 30 |
| 10:00 | ☕ **Break 1** | 10 |
| 10:10 | **Exploring Cluster Usage Data** — load the real yenstop CSV, explore it with Claude, write up one finding | 10 |
| 10:20 | **The Slurm Scheduler** — read the live queue: `squeue`, filter by partition, `R` vs `PD`, partitions/node states with `sinfo` | 10 |
| 10:30 | **Writing & Submitting a Slurm Job** — write the batch `.slurm` by hand (deactivate → `mkdir -p logs` → shebang → `#SBATCH` → env setup → run line), then `sbatch` / `squeue` / `scancel` / email / watch on the node with `htop` | 30 |
| 11:00 | ☕ **Break 2** | 10 |
| 11:10 | **Writing a Slurm Job with Claude** — `ml claude-code` + launch; distill a **global** Yen skill from the job just run and invoke it; then make a letter-distribution plot with Claude, distill its house style into a **project** skill, and re-invoke | 10 |
| 11:20 | **Documenting Your Pipeline** — write the README (what it does / how to run / where output lands) | 10 |
| 11:30 | **Day 3 Capstone** — estimate resources for 100 filings (write it down *first*), write the batch for 100, submit, compare actual vs. estimate, commit/push | 30 |
| 12:00 | **End** | |

Blocks around the breaks are ≈ **60 / 50 / 50**.

## How to run it

- **Drive the main quests live.** Pause at each main-quest checkbox for stragglers and questions before moving on.
- **Side quests are the buffer.** Point fast finishers at that section's side quests so nobody idles and you don't have to slow the whole room:
  - **Profiling** → vectorized vs. non-vectorized; `/usr/bin/time -v` vs. `userload`; prompt-caching rerun.
  - **Cluster Usage Data** → make a plot; per-user vs. whole-node limits; live `top`.
  - **The Slurm Scheduler** → `longsqueue` alias; `scontrol show job`; gpu vs. normal partition.
  - **Slurm Job** → the four `fix_me*` debug quests; chain two jobs (`--dependency=afterok`); the `dev` partition; interactive `srun --pty`.
  - **Slurm with Claude** → `claude -p` one-shot mode.
  - **Documenting** → have Claude critique the README as a first-time reader.
- **The four 10-min sections are brisk on purpose** (Cluster, Scheduler, Slurm-with-Claude, Documenting): demo the main move, drop a 🟢 sticky, keep going — the depth lives in their side quests.
- **Protected 30-min blocks:** Compute (the demo), Profiling (two terminals + `htop`), Slurm Job (writing it + the fresh-shell / `logs/` troubleshooting), and the Capstone.
- **Not everyone finishes every main quest live** in 3 hours — that's expected; they sync and catch up afterward. The **Capstone** works as the close: walk the estimate step on screen, then let students work while you circulate.
