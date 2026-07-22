#!/bin/bash
#SBATCH --job-name=fix-me
#SBATCH --output=logs/fix_me_%j.out
#SBATCH --error=logs/fix_me_%j.err
#SBATCH --time=00:05:00
#SBATCH --mem=2G
#SBATCH --cpus-per-task=1

cd $HOME/gsb-research-computing-ai-skills
python scripts/extract_form_3_one_file.py
