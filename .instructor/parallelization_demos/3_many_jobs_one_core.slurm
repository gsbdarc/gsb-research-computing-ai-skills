#!/bin/bash
# Demo 3/4 — "Cores, Jobs, or Both": MANY JOBS, ONE CORE EACH.
# A job array: the scheduler launches one independent job per array task
# (possibly on different nodes), and each task works its own slice of the
# filings serially on a single core. Parallelism across jobs: SLURM splits
# the work by task ID.
#
# Run from the repo root (needs .env for the API key):  sbatch .instructor/parallelization_demos/3_many_jobs_one_core.slurm
#SBATCH --job-name=demo-many-jobs-one-core
#SBATCH --output=logs/demo3_%A_%a.out
#SBATCH --error=logs/demo3_%A_%a.err
#SBATCH --time=00:10:00
#SBATCH --mem=2G
#SBATCH --cpus-per-task=1
#SBATCH --array=1-2

cd $HOME/gsb-research-computing-ai-skills
source .venv/bin/activate

OUT=/scratch/shared/$USER/demo_results
LIST=/scratch/shared/$USER/demo_filings_list.txt
mkdir -p "$OUT"
ls data/sec_filings/*.txt > "$LIST"   # every task regenerates the same list; harmless

# split the list into as many contiguous chunks as there are array tasks;
# this task processes chunk number $SLURM_ARRAY_TASK_ID, one filing at a time
TOTAL=$(wc -l < "$LIST")
CHUNK=$(( (TOTAL + SLURM_ARRAY_TASK_COUNT - 1) / SLURM_ARRAY_TASK_COUNT ))
START=$(( (SLURM_ARRAY_TASK_ID - 1) * CHUNK + 1 ))
END=$(( START + CHUNK - 1 ))

sed -n "${START},${END}p" "$LIST" | while read -r filing; do
    python scripts/extract_form_3_cli.py "$filing" "$OUT/$(basename "$filing" .txt).json"
done
