#!/bin/bash
#SBATCH --job-name=mystery-watch
#SBATCH --output=logs/mystery_%j.out
#SBATCH --error=logs/mystery_%j.err
#SBATCH --time=00:05:00
#SBATCH --mem=2G
#SBATCH --cpus-per-task=4

# A deliberately CPU-heavy demo job (~30s across 4 workers) so there's time to
# SSH to the node and watch it run with htop. See Writing & Submitting a SLURM Job.
cd $HOME/gsb-research-computing-ai-skills
source .venv/bin/activate
python scripts/mystery_script.py
