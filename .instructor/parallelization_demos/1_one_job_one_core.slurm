#!/bin/bash
# Demo 1/4 — "Cores, Jobs, or Both": ONE JOB, ONE CORE.
# The serial baseline from Day 3: one SLURM job, one core, a for loop.
# The loop can't start filing 2 until filing 1 is done.
#
# Run from the repo root (needs .env for the API key):  sbatch .instructor/parallelization_demos/1_one_job_one_core.slurm
#SBATCH --job-name=demo-one-job-one-core
#SBATCH --output=logs/demo1_%j.out
#SBATCH --error=logs/demo1_%j.err
#SBATCH --time=00:10:00
#SBATCH --mem=2G
#SBATCH --cpus-per-task=1

cd $HOME/gsb-research-computing-ai-skills
source .venv/bin/activate

OUT=/scratch/shared/$USER/demo_results
mkdir -p "$OUT"

# one core walks the filings in sequence
for filing in data/sec_filings/*.txt; do
    python scripts/extract_form_3_cli.py "$filing" "$OUT/$(basename "$filing" .txt).json"
done
