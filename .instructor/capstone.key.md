# Day 3 Capstone — Resource Estimation Key

**Instructor use only.** This file is not served by GitHub Pages. Use it to guide the discussion *after* students have written down their own estimate for 100 filings.

## Which resources scale, and why

The extraction loop is **API-bound and serial** — for each filing it makes one Stanford AI API call and waits for the response before moving to the next file.

| Resource | Scales with # of filings? | Why |
|----------|---------------------------|-----|
| **Wall-clock time** | **Yes — roughly linearly** | Filings are processed one after another; ~10× the files ≈ ~10× the time (plus network/API variance). |
| **RAM** | **No — stays about flat** | Only one filing's data is held in memory at a time; the loop doesn't accumulate. |
| **CPU cores** | **No — stays at 1** | The work is serial and spends most of its time *waiting on the API*, not computing, so extra cores sit idle. |

## Estimating for 100 from the 10-filing run

- **Time:** take the measured wall-clock for 10 filings and multiply by ~10, then add a safety margin (queue/API latency varies). If 10 took ~2 min, request `--time` well above ~20 min.
- **RAM:** keep the same `--mem` that comfortably fit the 10-filing run (e.g. `2G`); it won't grow.
- **CPU:** `--cpus-per-task=1` — more cores won't speed up serial, API-bound work.

## What to look for in the README

- An estimate written **before** submitting (which resources scale + why + the CPU/RAM/time numbers for 100).
- **After** the run: actual `Elapsed` / `MaxRSS` from the email and `sacct`, compared to the estimate.
- An honest **over- vs. under-estimate** note, with rough magnitude — the reflection matters more than being exactly right.
