"""Vectorized vs. non-vectorized: the same sum of squares, computed two ways.

Run it and watch the timing difference:

    source .venv/bin/activate
    time python scripts/vectorize_demo.py

Both blocks compute the identical result. The only difference is HOW: a plain
Python `for` loop (one operation at a time, in the interpreter) vs. NumPy, which
pushes the whole computation into compiled C. This is the single most common
speedup in scientific Python.
"""

import time

import numpy as np

N = 50_000_000

# Non-vectorized: a plain Python loop — one multiply/add per iteration.
start = time.perf_counter()
total = 0.0
for i in range(N):
    total += i * i
loop_time = time.perf_counter() - start
print(f"Python loop:      {total:.3e}  in {loop_time:6.2f}s")

# Vectorized: the same math in NumPy, with no Python-level loop.
start = time.perf_counter()
arr = np.arange(N, dtype=np.float64)
total_vec = float(np.sum(arr * arr))
vec_time = time.perf_counter() - start
print(f"NumPy vectorized: {total_vec:.3e}  in {vec_time:6.2f}s")

print(f"\nVectorized was {loop_time / vec_time:.0f}x faster for the same answer.")
