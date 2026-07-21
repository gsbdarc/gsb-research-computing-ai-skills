#!/bin/bash
#SBATCH --job-name=last-year-bug
#SBATCH --output=logs/last_year_%j.out
#SBATCH --error=logs/last_year_%j.err
#SBATCH --time=00:02:00
#SBATCH --mem=1G
#SBATCH --cpus-per-task=1

cd $HOME/gsb-research-computing-ai-skills
source .venv/bin/activate
python scripts/last_year_bug.py
