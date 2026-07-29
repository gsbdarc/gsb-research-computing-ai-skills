#!/usr/bin/env python3
"""Chain demo — step 2.

Read step 1's result from scratch and do more math with it. This job only runs
if step 1 succeeded (submitted with --dependency=afterok:<step1-jobid>).
"""
import math
import os
import time

SCRATCH = f"/scratch/users/{os.environ['USER']}/chain_demo"
IN = os.path.join(SCRATCH, "step1_result.txt")
OUT = os.path.join(SCRATCH, "step2_result.txt")

with open(IN) as f:
    step1 = float(f.read())

DURATION = 30  # seconds of real work, so you can catch step 2 running in the queue

result = step1 * 2 + 42  # more math, built directly from step 1's output

print(f"step 2: read step1_result = {step1:.4f}", flush=True)
print(f"step 2: crunching numbers for ~{DURATION}s ...", flush=True)
start = time.time()
n = 0
while time.time() - start < DURATION:
    math.sqrt((n % 1000) + 1)  # busy work so the job is visible running in the queue
    n += 1

with open(OUT, "w") as f:
    f.write(str(result))

print(f"step 2: did {n:,} operations, computed {result:.4f}, wrote {OUT}")
