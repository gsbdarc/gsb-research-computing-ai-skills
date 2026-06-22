---
layout: default
title: "The Trap Room"
parent: "Day 3 — The SLURM Mines"
nav_order: 6
permalink: /day3/trap-room/
---

# The Trap Room

<div data-room-id="d3-trap-room"></div>

*Pressure plates in the floor. Step on one and your job waits in queue forever, or crashes immediately, or runs successfully while producing garbage output. Every researcher springs these traps at least once. The Trap Room shows them to you first.*

---

## Main Quest

{: .important }
> **Quest:** Identify the bugs in three broken SLURM scripts before they cost you queue time — no running allowed.

This is a class discussion. Call out the bug for each script.

---

**Script 1:**
```bash
#!/bin/bash
#SBATCH --time=100:00:00
#SBATCH --mem=500G
#SBATCH --cpus-per-task=64

python3 extract_all.py
```

*What's wrong?*

<details>
<summary>Reveal the bug</summary>
<p>Requested 500 GB of memory and 64 CPUs. No node on the Yens has that much RAM available in one slot. This job will wait in <code>PD</code> (pending) state forever — or until the scheduler gives up. Always measure before requesting (<a href="../scales/">The Scales</a>). Most single-threaded Python scripts need 1 CPU and 2–8 GB.</p>
</details>

---

**Script 2:**
```bash
#!/bin/bash
#SBATCH --job-name=extraction
#SBATCH --output=output.log
#SBATCH --time=01:00:00

cd /home/users/researcher/project
python extract.py data/filings/
```

*What's wrong?*

<details>
<summary>Reveal the bug</summary>
<p>The output log is a relative path (<code>output.log</code>). SLURM writes the log relative to the working directory at submission time — which may not be <code>/home/users/researcher/project</code>. Use an absolute path or <code>%j</code> for the job ID: <code>--output=/home/users/researcher/project/logs/extraction_%j.out</code>. Also: no <code>--mem</code> directive — the job gets the default memory allocation, which may not be enough.</p>
</details>

---

**Script 3:**
```bash
#!/bin/bash
#SBATCH --time=02:00:00
#SBATCH --mem=4G

source activate myenv
python3 pipeline.py
```

*What's wrong?*

<details>
<summary>Reveal the bug</summary>
<p><code>source activate myenv</code> is conda syntax, not venv syntax — and it only works if conda's <code>conda init</code> has modified the shell's startup files, which SLURM non-interactive shells don't source. The correct command for a venv is <code>source ~/project/.venv/bin/activate</code> with an absolute path. If you use conda, you need to initialize it differently or use the full path to the conda environment's Python binary.</p>
</details>

<label class="quest-check"><input type="checkbox" data-room="d3-trap-room" data-key="main"> Trap Room complete — I can spot the three failure modes</label>

---

## Skills Learned

- Recognize over-requesting as a cause of permanent `PD` (pending) status
- Always use absolute paths in SLURM scripts — relative paths depend on submission directory
- Know how to activate a Python venv correctly inside a non-interactive SLURM shell
