#!/bin/bash
#SBATCH --job-name=extract-broken
#SBATCH --output=logs/extract_broken_%j.out
#SBATCH --error=logs/extract_broken_%j.err
#SBATCH --time=00:05:00
#SBATCH --mem=2G
#SBATCH --cpus-per-task=1

cd $HOMEgsb-research-computing-ai-skills
source .venv/bin/activate
python scripts/extract_form_3_one_file_broken.py
