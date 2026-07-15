---
layout: default
title: "The H200 Chamber"
parent: "Day 4 — The GPU Fortress"
nav_order: 4
permalink: /day4/h200-chamber/
---

# The H200 Chamber

<div data-room-id="d4-h200-chamber"></div>

---

## Main Quest

{: .important }
> **Quest:** Submit a GPU job targeting `yen-gpu4` (the H200 node), verify it runs on the GPU, and inspect the GPU utilization.

**Write `jobs/first_gpu_job.sh`:**

```bash
#!/bin/bash
#SBATCH --job-name=first_gpu_job
#SBATCH --output=logs/gpu_job_%j.out
#SBATCH --error=logs/gpu_job_%j.err
#SBATCH --time=00:15:00
#SBATCH --mem=16G
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:1                     # request 1 GPU
#SBATCH --nodelist=yen-gpu4             # target the H200
#SBATCH --partition=gpu                 # GPU partition (confirm with instructor)

echo "Running on: $(hostname)"
echo "GPU info:"
nvidia-smi

source ~/rf-bootcamp-2026/.venv/bin/activate
pip install torch --quiet   # if not already installed

python3 - <<'EOF'
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"GPU: {torch.cuda.get_device_name(0)}")
print(f"VRAM total: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")

# Simple GPU computation to confirm it's working
x = torch.randn(10000, 10000, device="cuda")
y = x @ x.T
print(f"Matrix multiply complete. Result shape: {y.shape}")
EOF
```

**Submit:**
```bash
sbatch jobs/first_gpu_job.sh
```

**Check the log when it runs:**
```bash
tail -f logs/gpu_job_JOBID.out
```

<label class="quest-check"><input type="checkbox" data-room="d4-h200-chamber" data-key="main"> Main Quest complete</label>
