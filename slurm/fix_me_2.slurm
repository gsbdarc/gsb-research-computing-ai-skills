#!/bin/bash
#SBATCH --job-name=fix-me-2
#SBATCH --output=logs/fix_me_2_%j.out
#SBATCH --error=logs/fix_me_2_%j.err
#SBATCH --time=00:05:00
#SBATCH --mem=2G
#SBATCH --cpus-per-task=1

cd $HOME/gsb-research-computing-ai-skills
source .venv/bin/activate
python extract_form_3_one_file.py
