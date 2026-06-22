---
layout: default
title: "The H200 Chamber"
parent: "Day 4 — The GPU Fortress"
nav_order: 3
permalink: /day4/h200-chamber/
---

# The H200 Chamber

<div data-room-id="d4-h200-chamber"></div>

*141 gigabytes of HBM3e memory. The largest, fastest GPU on the Yens. You will submit a job that runs on it — your first real GPU job. Watch the `nvidia-smi` output when it starts. The numbers are real: this silicon is doing work that would take your laptop days.*

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

source ~/rf_bootcamp_2026/.venv/bin/activate
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

---

## Chests

{: .chest }
> **Chest 1 — Smi Sight:** Run `nvidia-smi` inside your GPU job and add `nvidia-smi --query-gpu=name,memory.total,memory.used,utilization.gpu --format=csv` to log GPU state at the start and end of your script. Save the output to a file.

<label class="quest-check"><input type="checkbox" data-room="d4-h200-chamber" data-key="chest1"> Smi Sight unlocked</label>

{: .chest }
> **Chest 2 — Benchmark Blade:** Run the same matrix multiply on both the H200 (yen-gpu4) and CPU only. Compare wall-clock time using Python's `time` module. At what matrix size does the GPU start to win decisively?

<label class="quest-check"><input type="checkbox" data-room="d4-h200-chamber" data-key="chest2"> Benchmark Blade unlocked</label>

---

## Weapons Earned

{: .weapon }
> **Smi Sight** — `nvidia-smi` inside a SLURM GPU job; monitor GPU memory and utilization; know whether your model is actually using the GPU or running on CPU by mistake.
>
> **Benchmark Blade** — time the same computation on CPU vs. GPU; quantify the speedup; make GPU requests defensible with data.

---

## Skills Learned

- Write a SLURM script that requests a GPU with `--gres=gpu:1` and targets a specific node with `--nodelist`
- Verify the GPU is actually being used with `nvidia-smi` and `torch.cuda.is_available()`
- Understand GPU memory (VRAM) as separate from system RAM — they are different resources
- Know when GPU is worth the queue wait: large matrix operations, model inference, embedding generation
