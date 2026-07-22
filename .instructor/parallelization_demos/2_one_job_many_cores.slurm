#!/bin/bash
# Demo 2/4 — "Cores, Jobs, or Both": ONE JOB, MANY CORES.
# One SLURM job that reserves 2 cores; xargs -P fans the filings out across
# them *inside* the job. Parallelism within a job: your code splits the work,
# not the scheduler.
#
# Run from the repo root (needs .env for the API key):  sbatch .instructor/parallelization_demos/2_one_job_many_cores.slurm
#SBATCH --job-name=demo-one-job-many-cores
#SBATCH --output=logs/demo2_%j.out
#SBATCH --error=logs/demo2_%j.err
#SBATCH --time=00:10:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=2

cd $HOME/gsb-research-computing-ai-skills
source .venv/bin/activate

export OUT=/scratch/shared/$USER/demo_results
mkdir -p "$OUT"

# -P runs up to $SLURM_CPUS_PER_TASK extractions at once — one per reserved core.
# Each worker grabs the next filing the moment it finishes one (dynamic waves).
ls data/sec_filings/*.txt | xargs -P "$SLURM_CPUS_PER_TASK" -n1 \
    bash -c 'python scripts/extract_form_3_cli.py "$1" "$OUT/$(basename "$1" .txt).json"' _
