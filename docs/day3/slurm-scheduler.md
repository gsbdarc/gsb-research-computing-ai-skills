---
layout: default
title: "The SLURM Scheduler"
parent: "Day 3 — Cluster Computing"
nav_order: 5
permalink: /day3/slurm-scheduler/
---

# The SLURM Scheduler

<div data-room-id="d3-head-chef"></div>

---

## Interactive Yens

The interactive Yens are unusual compared to most HPC clusters: they serve double duty as both login nodes and compute nodes. You can SSH in and run work right there. Most clusters don't allow this — on typical HPC systems, the login node is strictly for job submission.

The Yens has **5 interactive nodes** (`yen1`–`yen5`). When you SSH in, you land on one of these — and so does everyone else. CPU cores and RAM are **shared** between all users on the same node, and per-user limits are enforced — but many researchers running at once still slows everyone down.

| | Interactive Yens |
|---|---|
| Nodes | 5 (`yen1`–`yen5`) |
| How to access | SSH directly |
| Wait for resources? | No |
| CPU / RAM shared among users? | Yes |
| Notebooks? | Yes |
| GPUs? | No |

Use the interactive Yens for: exploring data, testing code, runs where you're watching the terminal (or using [`screen`](https://rcpedia.stanford.edu/_user_guide/screen/) to keep a session alive).

---

## When the Interactive Yens Aren't Enough

In the live demo earlier you saw what happens when many users share the same node — CPU cores get taken, RAM fills up, and everyone slows down. The interactive Yens hit the same limits:

- **All the CPU cores are busy** — someone else is using all available cores on the node; your script crawls
- **The node is out of RAM** — another user's job already claimed most of the memory; yours may crash or get killed
- **You hit the user limit** — per-user CPU and RAM caps are enforced; your script gets throttled even if the node has headroom
- **You need to walk away** — if your connection drops, your script dies; babysitting a terminal for hours is not research

The solution: a scheduler. **SLURM** reads every job request, knows what resources each job needs, and assigns work to **dedicated nodes** where nothing else is running.

| | Interactive Yens | SLURM Scheduled Nodes |
|---|---|---|
| Nodes | 5 (`yen1`–`yen5`) | 12 |
| How to access | SSH directly | Submit a job script |
| Wait for resources? | No | Yes — may queue |
| CPU / RAM shared among users? | Yes | No — yours alone |
| Notebooks? | Yes | No |
| GPUs? | No | Yes |

Instead of running your script directly on a shared node, you submit it to the scheduler: you specify what resources you need, SLURM runs it on a dedicated node, and you collect the results when it's done.

| SLURM concept | What it is |
|---|---|
| SLURM scheduler | Decides which jobs run where and when |
| Compute node | A dedicated machine that runs your job |
| CPU core | A unit of parallel compute you request |
| RAM | Memory you request for the job |
| Shared file system (VAST) | Where your data and code live, visible from every node |
| Job script (`sbatch`) | The script you submit to request resources and run your work |
| Job queue (`squeue`) | The list of pending and running jobs |
| Your Python / R / shell script | The actual program the job runs |

{: .note }
> **Why does this matter?** When you submit a job to the cluster, you have to tell the scheduler exactly how much CPU, RAM, and time your job needs. If you ask for too little, your job fails. If you ask for too much, you wait longer in the queue and waste shared resources. The only way to know what to ask for is to **measure first**.

---

## Exercise — Peek at the Queue

{: .important }
> **Task:** Look at the live SLURM queue to see what jobs are waiting or running right now.

```bash
squeue
```

Look at the columns:
- **JOBID** — unique ID for each job
- **PARTITION** — which partition (queue) the job was submitted to — each partition has different node types, time limits, and resource caps; see the [current partitions and their limits](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits)
- **ST** — status: `R` = running, `PD` = pending (waiting in queue for resources)
- **TIME** — how long the job has been running
- **NODELIST** — which compute node it landed on

There is also a shorthand to filter to just your jobs:

```bash
squeue --me
```

You can also filter by partition — for example, to see only GPU jobs:

```bash
squeue -p gpu
```

Every `PD` job is waiting for a node with the resources it requested. When SLURM finds a matching node — it runs.

Now run `sinfo` to see the state of all nodes and the partitions they belong to:

```bash
sinfo
```

- How many compute nodes are currently idle (`STATE=idle`)?
- What partitions exist? Which one would you use for a normal job?
- What is the maximum time limit for each partition? (See the [current partitions and their limits](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits).)

When you can read the queue, tell `R` from `PD`, and describe the Yens partitions and node states — put a **🟢 green sticky** on your laptop.

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="main"> I can read the queue with squeue, filter by partition, and describe the partitions and node states with sinfo</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/gsb-research-computing-ai-skills` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-head-chef.main` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/gsb-research-computing-ai-skills`), not the class repo `gsbdarc/gsb-research-computing-ai-skills` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

---

## Optional Exercises

{: .note }
> Finished early? Try this.

**Optional practice — Add a `longsqueue` alias**

The default `squeue` output is sparse. Pass a custom format to see what each job actually requested — CPU cores, memory, and time limit:

```bash
squeue -o "%.18i %.9P %.8j %.8u %.8T %.10M %.10l %.4C %.7m %.15R"
```

The columns are: job ID, partition, job name, user, state, time elapsed, time limit, CPU cores requested, memory requested, and reason/node.

Add it as an alias so you can use it any time:

```bash
echo "alias longsqueue='squeue -o \"%.18i %.9P %.8j %.8u %.8T %.10M %.10l %.4C %.7m %.15R\"'" >> ~/.bash_profile
source ~/.bash_profile
```

Now run `longsqueue` — you should see the full resource picture of every job in the queue.

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="side3"> I added the longsqueue alias to my ~/.bash_profile and can read CPU and memory requests in the queue</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/gsb-research-computing-ai-skills` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-head-chef.side3` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/gsb-research-computing-ai-skills`), not the class repo `gsbdarc/gsb-research-computing-ai-skills` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

**Optional practice — Inspect any job with scontrol**

Pick any job from `squeue` and look up its full details:

```bash
scontrol show job JOBID
```

Find these fields in the output:
- **NumCPUs** — how many CPU cores were requested
- **mem=** — how much RAM was requested
- **TimeLimit** — the time limit set for the job

This works on any job — yours or someone else's — as long as it is still in the queue or running.

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="side4"> I used scontrol to find the CPU, RAM, and time limit of a job in the queue</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/gsb-research-computing-ai-skills` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-head-chef.side4` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/gsb-research-computing-ai-skills`), not the class repo `gsbdarc/gsb-research-computing-ai-skills` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

**Optional practice — Compare partitions**

Run `sinfo -p gpu` and `sinfo -p normal` (or whichever partitions exist on the Yens) and compare what each offers — node count, time limits, resource caps. Can you explain when you'd request one over the other for a job?

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="side5"> I compared a GPU partition to a CPU partition with sinfo and can explain when I'd request each</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/gsb-research-computing-ai-skills` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-head-chef.side5` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/gsb-research-computing-ai-skills`), not the class repo `gsbdarc/gsb-research-computing-ai-skills` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>
