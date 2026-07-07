#!/bin/bash

#SBATCH --job-name=extract
#SBATCH --output=logs/extract_%j.out
#SBATCH --time=01:00:00
#SBATCH --mem=8G
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=your_email@stanford.edu

cd ~/rf-bootcamp-2026

source .venv/bin/activate

python scripts/extract_form_3_batch.py
