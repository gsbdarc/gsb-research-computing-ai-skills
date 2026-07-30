---
layout: default
title: "The Slurm Scheduler"
parent: "Day 3 — Cluster Computing"
nav_order: 5
permalink: /day3/slurm-scheduler/
---

# The Slurm Scheduler

<div data-room-id="d3-slurm-scheduler"></div>

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

The solution: a scheduler. **Slurm** reads every job request, knows what resources each job needs, and assigns work to **dedicated nodes** where nothing else is running.

| | Interactive Yens | Slurm Scheduled Nodes |
|---|---|---|
| Nodes | 5 (`yen1`–`yen5`) | 12 |
| How to access | SSH directly | Submit a job script |
| Wait for resources? | No | Yes — may queue |
| CPU / RAM shared among users? | Yes | No — yours alone |
| Notebooks? | Yes | No |
| GPUs? | No | Yes |

Instead of running your script directly on a shared node, you submit it to the scheduler: you specify what resources you need, Slurm runs it on a dedicated node, and you collect the results when it's done.

<svg viewBox="0 0 730 108" role="img" aria-labelledby="whererun-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:730px;height:auto;margin:0.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="whererun-title">You submit a job from a shared interactive Yen; the Slurm scheduler runs it on a separate dedicated compute node, using that node's own cores and RAM.</title>
  <defs>
    <marker id="whererun-ah" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#e67e22"/></marker>
  </defs>
  <rect x="8" y="16" width="204" height="76" rx="12" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="26" y="50" font-size="17" font-weight="700" fill="#1f2937">💻 Interactive Yen</text>
  <text x="26" y="74" font-size="14" fill="#4b5563">yen1–yen5 · you work here</text>
  <line x1="214" y1="54" x2="272" y2="54" stroke="#e67e22" stroke-width="2.5" marker-end="url(#whererun-ah)"/>
  <text x="243" y="44" text-anchor="middle" font-size="13.5" font-weight="700" fill="#b3611a">submit</text>
  <rect x="274" y="32" width="140" height="44" rx="12" fill="#f3f4f7" stroke="#d5d8e2" stroke-width="1.5"/>
  <text x="344" y="54" text-anchor="middle" font-size="17" font-weight="700" fill="#1f2937">Slurm</text>
  <text x="344" y="70" text-anchor="middle" font-size="13" fill="#4b5563">the scheduler</text>
  <line x1="416" y1="54" x2="468" y2="54" stroke="#e67e22" stroke-width="2.5" marker-end="url(#whererun-ah)"/>
  <text x="442" y="44" text-anchor="middle" font-size="13.5" font-weight="700" fill="#b3611a">runs it</text>
  <rect x="470" y="8" width="242" height="92" rx="12" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="486" y="38" font-size="16" font-weight="700" fill="#1f2937">🖥️ Compute Node(s)</text>
  <text x="486" y="64" font-size="14" fill="#4b5563">your script gets dedicated</text>
  <text x="486" y="84" font-size="14" fill="#4b5563">cores + RAM</text>
</svg>

*You submit from a shared interactive Yen, but the job runs on separate **compute node(s)** — with dedicated cores and RAM, nothing else competing.*

| Slurm concept | What it is |
|---|---|
| Slurm scheduler | Decides which jobs run where and when |
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

## Main quest — Peek at the Queue

{: .important }
> **Task:** Look at the live Slurm queue to see what jobs are waiting or running right now.

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

Every `PD` job is waiting for a node with the resources it requested. When Slurm finds a matching node — it runs.

<svg viewBox="0 0 720 130" role="img" aria-labelledby="lifecycle-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:720px;height:auto;margin:1rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="lifecycle-title">A job's lifecycle: you submit it, it waits in the queue as PD, runs as R on a compute node, completes, and leaves .out and .err logs behind.</title>
  <defs>
    <marker id="lifecycle-ah" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#e67e22"/></marker>
  </defs>
  <line x1="124" y1="78" x2="150" y2="78" stroke="#e67e22" stroke-width="2.5" marker-end="url(#lifecycle-ah)"/>
  <line x1="262" y1="78" x2="288" y2="78" stroke="#e67e22" stroke-width="2.5" marker-end="url(#lifecycle-ah)"/>
  <line x1="400" y1="78" x2="426" y2="78" stroke="#e67e22" stroke-width="2.5" marker-end="url(#lifecycle-ah)"/>
  <line x1="538" y1="78" x2="564" y2="78" stroke="#e67e22" stroke-width="2.5" marker-end="url(#lifecycle-ah)"/>
  <rect x="12" y="40" width="112" height="76" rx="10" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="68" y="72" text-anchor="middle" font-size="17" font-weight="700" fill="#1f2937">submit</text>
  <text x="68" y="93" text-anchor="middle" font-size="12" fill="#6a7280">your job</text>
  <rect x="150" y="40" width="112" height="76" rx="10" fill="#f3f4f7" stroke="#d5d8e2" stroke-width="1.5"/>
  <text x="206" y="72" text-anchor="middle" font-size="17" font-weight="700" fill="#6a7280">PD</text>
  <text x="206" y="91" text-anchor="middle" font-size="12" fill="#6a7280">queued</text>
  <text x="206" y="107" text-anchor="middle" font-size="11" fill="#9aa4b0">waiting for a node</text>
  <rect x="288" y="40" width="112" height="76" rx="10" fill="#eef5ff" stroke="#e67e22" stroke-width="2"/>
  <text x="344" y="72" text-anchor="middle" font-size="17" font-weight="700" fill="#b3611a">R</text>
  <text x="344" y="91" text-anchor="middle" font-size="12" fill="#5b6472">running</text>
  <text x="344" y="107" text-anchor="middle" font-size="11" fill="#9aa4b0">on a compute node</text>
  <rect x="426" y="40" width="112" height="76" rx="10" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="482" y="72" text-anchor="middle" font-size="16" font-weight="700" fill="#1f2937">completed</text>
  <text x="482" y="93" text-anchor="middle" font-size="12" fill="#6a7280">job finishes</text>
  <rect x="564" y="40" width="112" height="76" rx="10" fill="#f3f4f7" stroke="#d5d8e2" stroke-width="1.5"/>
  <text x="620" y="72" text-anchor="middle" font-size="17" font-weight="700" fill="#1f2937">logs</text>
  <text x="620" y="91" text-anchor="middle" font-size="12" fill="#6a7280">.out / .err</text>
  <text x="620" y="107" text-anchor="middle" font-size="11" fill="#9aa4b0">in logs/</text>
  <g>
    <path d="M58,16 L78,16 L68,32 Z" fill="#0072B2"><animateTransform attributeName="transform" type="translate" values="0,0; 0,5; 0,0" dur="0.9s" repeatCount="indefinite"/></path>
    <animateTransform attributeName="transform" type="translate" values="0,0; 0,0; 138,0; 138,0; 276,0; 276,0; 414,0; 414,0; 552,0; 552,0; 0,0" keyTimes="0; 0.06; 0.22; 0.28; 0.44; 0.50; 0.66; 0.72; 0.88; 0.94; 1" dur="10s" repeatCount="indefinite" calcMode="linear"/>
  </g>
</svg>

*The lifecycle of every job — you'll see the `R` and `PD` states in `squeue`, and the logs are where you look when it's done (or when it fails). Later pages refer back to this flow.*

Now run `sinfo` to see the state of all nodes and the partitions they belong to:

```bash
sinfo
```

- How many compute nodes are currently idle (`STATE=idle`)?
- What partitions exist? Which one would you use for a normal job?
- What is the maximum time limit for each partition? (See the [current partitions and their limits](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits).)

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-scheduler" data-key="main"> I can read the queue with squeue, filter by partition, and describe the partitions and node states with sinfo</label>

---

## Side quests

{: .note }
> Finished early? Try any of these.

**Side quest — Add a `longsqueue` alias**

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

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-scheduler" data-key="side3"> I added the longsqueue alias to my ~/.bash_profile and can read CPU and memory requests in the queue</label>

**Side quest — Inspect any job with scontrol**

Pick any job from `squeue` and look up its full details:

```bash
scontrol show job JOBID
```

Find these fields in the output:
- **NumCPUs** — how many CPU cores were requested
- **mem=** — how much RAM was requested
- **TimeLimit** — the time limit set for the job

This works on any job — yours or someone else's — as long as it is still in the queue or running.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-scheduler" data-key="side4"> I used scontrol to find the CPU, RAM, and time limit of a job in the queue</label>

**Side quest — Compare partitions**

Run `sinfo -p gpu` and `sinfo -p normal` to compare node counts and time limits. `sinfo` doesn't show the per-user resource **caps** — those come from each partition's QoS, so check `sacctmgr show qos gpu` vs `sacctmgr show qos normal` (or the [current partitions and their limits](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits)). Can you explain when you'd request one over the other for a job?

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-scheduler" data-key="side5"> I compared a GPU partition to a CPU partition with sinfo and can explain when I'd request each</label>

