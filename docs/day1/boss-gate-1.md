---
layout: default
title: "Day 1 Challenge"
parent: "Day 1 — Foundations"
nav_order: 10
permalink: /day1/boss-gate-1/
---

# Day 1 Challenge

<div data-room-id="d1-boss-gate-1"></div>

This challenge ties the whole day together into a single piece of proof. You'll
capture a fingerprint of **your laptop**, carry it across to **the Yens** with
`scp`, and then hand the analysis and the git work to **Claude Code** — the tool
you just set up. The result is one file, `day1_challenge.json`, that travels from
your laptop to the cluster and lands in your fork as a pull request.

Everything you'll use today shows up here: SSH, `scp`, Claude Code, and the
fork → branch → commit → push → PR workflow from the github-for-research skill.

---

## The Challenge

{: .important }
> **Task:** Capture your laptop's public IP, `scp` it to the Yens, then have
> Claude Code compute a letter distribution over the grimoire spell names, write
> both into `day1_challenge.json`, and open a pull request on your fork.

The finished file has this **structure** (the numbers below are placeholders to
show the shape — Claude computes the real counts):

```json
{
  "public_ip": "203.0.113.42",
  "letter_distribution": { "a": 0, "b": 0, "c": 0 }
}
```

- `public_ip` — the public IP address of **your laptop** (proof the file started
  on your machine and crossed to the cluster).
- `letter_distribution` — how often each letter `a`–`z` appears across the
  **spell name** field of the grimoire (Claude computes this for you).

---

### Step 1 — Grab your laptop's public IP

Do this on your **laptop** (a local Terminal / Git Bash tab), *not* on the Yens —
run it on the Yens and you'd capture the *cluster's* address instead of yours.

```bash
curl -s https://api.ipify.org > ~/Desktop/provenance.txt   # your laptop's public IP
cat ~/Desktop/provenance.txt                               # confirm you got an address
```

You should see something like `203.0.113.42`.

{: .note }
> Everyone in the room shares the same network, so this address points at the
> classroom, not at you personally.

---

### Step 2 — Send it to the Yens with `scp`

Still on your **laptop**, copy the file straight into your course repo on the
Yens (`scp` runs over the SSH connection you set up earlier):

```bash
scp ~/Desktop/provenance.txt SUNetID@yen.stanford.edu:~/gsb-research-computing-ai-skills/provenance.txt
```

This is the same upload direction you practiced in
[Transferring Files (scp)](../scroll-transfer/) — source is local, destination is
remote.

---

### Step 3 — Let Claude Code do the analysis and the git work

Now hop onto the Yens, move into your repo, and launch Claude Code:

```bash
ssh SUNetID@yen.stanford.edu     # if you're not already connected
cd ~/gsb-research-computing-ai-skills
claude
```

Press `Shift+Tab` until you reach **plan mode** — so Claude investigates and
proposes an approach *without changing anything* until you approve. This is the
`look → plan → approve → act` loop from [Working with Claude Code](../familiars-den/).

Now describe the task **in your own words** — don't copy a script. Tell Claude
what you want to end up with, and let it work out the how. Your instruction should
cover all of these objectives:

- **Analyze the grimoire.** The dataset is already in the repo you cloned, at
  `docs/assets/data/grimoire.zip` — Claude just needs to unzip it (no download).
  Count how often each letter `a`–`z` appears across the **spell name** field
  only — the
  first underscore-separated field of each filename (e.g. `ashstrike` in
  `ashstrike_fire_3_defensive_meteor.spell`), never the element, tier, type, or
  mastery. Be explicit about **how** you count: use every one of the files' names
  (names repeat across the dataset, and each file counts), lowercase `a`–`z`
  only, as integer counts.
- **Read your provenance.** Pull your laptop's public IP from `provenance.txt`,
  the file you just `scp`'d into this repo.
- **Write the result.** Produce a file named `day1_challenge.json` in the repo,
  containing exactly two top-level keys and nothing else:
  - `public_ip` — the IP string from `provenance.txt`.
  - `letter_distribution` — an object mapping each lowercase letter to its integer
    count.

  The file's **structure** must match this (the numbers are placeholders — Claude
  fills in the real counts):

  ```json
  {
    "public_ip": "203.0.113.42",
    "letter_distribution": { "a": 0, "b": 0, "c": 0 }
  }
  ```
- **Do the git work the research way.** Log an issue for the task, work on a new
  branch, commit crediting Claude, and open a pull request.

**Then read the plan Claude gives you.** Before you approve, check it yourself:

- Does it hit **every** objective above — the analysis, the IP, the JSON file,
  *and* the full issue → branch → commit → PR cycle?
- Is it following the **github-for-research** skill you installed in
  [Working with Claude Code](../familiars-den/)? If the plan doesn't mention the
  skill or the branch/issue/PR habits, ask Claude: `> are you using the
  github-for-research skill for this?` — and have it revise the plan if not.

Refine the plan until it clearly achieves the objectives, then approve it and let
Claude carry it out. Notice what you *didn't* do: no `curl` for the dataset, no
`unzip`, no counting by hand, no `git` commands typed out — you described the
outcome and reviewed the approach, and Claude did the rest.

---

### Step 4 — Verify your submission

Open your fork on GitHub in a browser. You should see a new **pull request** with
`day1_challenge.json` in its **Files changed** tab. Open the file and check it has
both keys — a valid IP in `public_ip` and a set of letter counts in
`letter_distribution`. That pull request is your submission.

Merging it is optional — the open PR is enough to count as done.

{: .note }
> If Claude reports that `git push` failed for authentication, you haven't
> signed in to GitHub on the Yens yet — run `module load gh && gh auth login`
> (see Step 3 of [Version Control with Git](../repository/)), then ask Claude to
> push again. Still stuck? Ask an instructor.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

<label class="quest-check"><input type="checkbox" data-room="d1-boss-gate-1" data-key="main"> Day 1 Challenge complete</label>

---

## What You Learned

| Skill | Where you learned it |
|-------|---------------------|
| `curl` to fetch data over the network | Bulk File Operations |
| `ssh` to a remote server | Connecting to a Cluster |
| `scp` to move a file laptop → cluster | Transferring Files (scp) |
| The spell filename fields (`name_element_tier_type_mastery`) | Bulk File Operations |
| Driving a task in plain English with Claude Code | Working with Claude Code |
| Branch → commit → PR, done for you by the skill | Version Control with Git + Working with Claude Code |

You just ran a full research loop end to end: fingerprint your machine, move data
across the network, analyze it with an AI assistant, and version-control the
result — the same shape of workflow you'll use for real projects on the Yens.
