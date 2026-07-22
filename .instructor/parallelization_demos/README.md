# Parallelization demos (instructor)

Four SLURM scripts mapping 1:1 to the diagrams in the Day 4
["Cores, Jobs, or Both"](../../docs/day4/parallelization.md) section.
Each extracts the SEC filings in `data/sec_filings/` with
`scripts/extract_form_3_cli.py`, varying only *how* the work is spread.

| Script | Jobs | Cores/job | Parallelism |
|---|---|---|---|
| `1_one_job_one_core.slurm` | 1 | 1 | none — serial `for` loop |
| `2_one_job_many_cores.slurm` | 1 | 2 | within the job (`xargs -P` across reserved cores) |
| `3_many_jobs_one_core.slurm` | 2 (array) | 1 | across jobs (each task works its slice serially) |
| `4_many_jobs_many_cores.slurm` | 2 (array) | 2 | both dials at once |

## Running

From the repo root on the Yens (a `.env` with the API key must be present,
and `logs/` must exist — SLURM won't create it):

```bash
mkdir -p logs
sbatch .instructor/parallelization_demos/1_one_job_one_core.slurm
```

Results land in `/scratch/shared/$USER/demo_results/`; delete that directory
between runs to make timing comparisons clean.

## Comparing time and resources

The scripts don't print resource usage themselves — that's SLURM accounting's
job, queried after a job finishes. `MaxRSS` is the peak RAM actually used
(compare against the `ReqMem` you asked for); `TotalCPU` vs. `Elapsed` shows
how well the reserved cores were kept busy:

```bash
sacct -j <jobid> --format=JobID,JobName,Elapsed,TotalCPU,AllocCPUS,ReqMem,MaxRSS,State
```

Or the one-screen efficiency summary (CPU efficiency and memory utilization,
per job or per array task):

```bash
seff <jobid>        # seff 12345678, or seff 12345678_1 for one array task
```

*Co-authored by Claude (Opus 4.8).*
