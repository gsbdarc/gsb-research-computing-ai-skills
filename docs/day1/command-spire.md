---
layout: default
title: "Command Line Basics"
parent: "Day 1 — Foundations"
nav_order: 2
permalink: /day1/command-spire/
---

# Command Line Basics

<div data-room-id="d1-command-spire"></div>

This room introduces the terminal: what it is, why researchers use it, and the core commands for navigating and organizing files. Master these basics and any Unix system — a cluster, a remote server, an HPC node — will feel familiar.

---

## The Terminal

A terminal is a text interface to your computer. Instead of clicking icons, you type commands. It is how researchers talk to servers, automate repetitive work, and do in seconds what a mouse would take days to do.

**Open yours now:**

- **Mac:** Press `Cmd+Space`, type `Terminal`, press Enter.
- **Windows:** Download and install [Git Bash](https://git-scm.com/downloads), then open "Git Bash" from the Start menu.

You should see a blinking cursor. That is where you type commands.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

---

## Why This Matters

With a terminal open, here is what you can now do:

| | GUI (Finder / Explorer) | CLI (Terminal) |
|---|---|---|
| **Speed** | Click → drag → drop, one file at a time | 300 files moved in one second |
| **Navigate** | Browse folders by clicking | `cd`, `ls`, `pwd` — anywhere, instantly |
| **Organize** | Rename files one by one | Wildcards sort an entire dataset at once |
| **Power** | Limited to what the app exposes | Run scripts, schedule jobs, automate anything |

And later this morning, when you SSH into the Yens, every command you learn right now runs identically on a machine 500× more powerful than your laptop:

| | Your laptop | Stanford Yens |
|---|---|---|
| **Cores** | ~8–16 | 32–512 per node |
| **RAM** | ~8–32 GB | 250 GB – 3 TB per node |
| **Commands** | `$ ls` `$ cd` `$ pwd` | `$ ls` `$ cd` `$ pwd` |
| **Access** | direct | `ssh SUNetID@yen.stanford.edu` |

Same commands. More power.

**Class discussion — file organization**

You have been working on your research projects for about a month. Before we go further:

- What kinds of files do you actually have? *(raise your hand — we will whiteboard this)*
- Where do they live right now?
- What happens when you need to find something from three weeks ago?

<details markdown="1">
<summary>One example structure (expand after discussion)</summary>

Organizing files is not a rule for its own sake — it is what makes your work reproducible, shareable, and recoverable when something goes wrong. Here is one common structure for a research project:

<svg viewBox="0 0 600 336" role="img" aria-labelledby="cs-tree-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:600px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="cs-tree-title">A research project folder named my_project holds four separate items: a data folder for raw data that is never modified, a scripts folder for your code, a results folder for the outputs your scripts generate, and a README file describing what the project is and how to run it.</title>
  <!-- root project folder -->
  <rect x="20" y="18" width="250" height="42" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="36" y="45" font-size="19">📁</text>
  <text x="66" y="45" font-size="15" font-weight="700" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#2c3e50">my_project/</text>
  <!-- tree connector lines -->
  <line x1="40" y1="60" x2="40" y2="286" stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="40" y1="100" x2="64" y2="100" stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="40" y1="162" x2="64" y2="162" stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="40" y1="224" x2="64" y2="224" stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="40" y1="286" x2="64" y2="286" stroke="#cbd3e0" stroke-width="1.5"/>
  <!-- data/ -->
  <rect x="64" y="74" width="512" height="52" rx="10" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="80" y="107" font-size="20">📁</text>
  <text x="112" y="97" font-size="15" font-weight="700" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#2c3e50">data/</text>
  <text x="112" y="115" font-size="12.5" fill="#6a7280">raw data — <tspan font-weight="700" fill="#c0392b">never modify it</tspan></text>
  <!-- scripts/ -->
  <rect x="64" y="136" width="512" height="52" rx="10" fill="#f3f4f7" stroke="#d5d8e2" stroke-width="1.5"/>
  <text x="80" y="169" font-size="20">📁</text>
  <text x="112" y="159" font-size="15" font-weight="700" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#2c3e50">scripts/</text>
  <text x="112" y="177" font-size="12.5" fill="#6a7280">your code — the analysis you write</text>
  <!-- results/ -->
  <rect x="64" y="198" width="512" height="52" rx="10" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="80" y="231" font-size="20">📁</text>
  <text x="112" y="221" font-size="15" font-weight="700" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#2c3e50">results/</text>
  <text x="112" y="239" font-size="12.5" fill="#6a7280">outputs your scripts generate — safe to delete &amp; rebuild</text>
  <!-- README.md -->
  <rect x="64" y="260" width="512" height="52" rx="10" fill="#f5f3fb" stroke="#ddd6ef" stroke-width="1.5"/>
  <text x="80" y="293" font-size="20">📄</text>
  <text x="112" y="283" font-size="15" font-weight="700" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#2c3e50">README.md</text>
  <text x="112" y="301" font-size="12.5" fill="#6a7280">what this project is &amp; how to run it</text>
</svg>

*One project folder, four separate jobs: keep **raw data** untouched, your **code** in one place, the **results** your code regenerates in another, and a **README** that explains it all — so nothing important ever gets mixed up or overwritten.*

There are many ways to organize files — this is one example. What matters is that the structure is consistent and that raw data is never mixed with outputs.

</details>

---

## Exercise

Your terminal is open. In this exercise you will use the command line to find where you are, move around the file system, and create and delete files and folders.

{: .important }
> **Goal:** Use the command line to navigate your file system and reorganize a directory of files — without touching a mouse.

**Investigation**

Find your current working directory and list the files in it.

```bash
pwd          # print working directory — where you are right now
ls           # list files and directories here
```

Now look for hidden files — files whose names start with a dot are invisible to a plain `ls`:

```bash
ls -lah      # -l long format · -a all files (including hidden) · -h human-readable sizes
```

A **flag** modifies the behavior of a command. `-lah` is three flags combined into one: it tells `ls` to show everything, in detail, with file sizes you can actually read. You can look up any command's flags by searching online — for example, "ls command flags".

{: .tip }
> **Tab completion:** Start typing a filename or path and press `Tab` — the shell completes it. Press `Tab` twice to see all matches. Use it constantly; it prevents typos and saves time.

---

**Movement**

Use `cd` to change directories. `~` is your home directory; `..` means one level up.

```bash
cd ~/Desktop    # navigate to your Desktop — once you type D, press Tab to autocomplete
                # press Tab twice to see all options if nothing completes
pwd             # confirm where you landed
cd ..           # go up one level
pwd             # confirm you moved up
```

---

**Creation**

Create a new folder on your Desktop, create a file inside it, and duplicate it.

```bash
mkdir ~/Desktop/spell_chamber        # create a new folder on your Desktop
cd ~/Desktop/spell_chamber           # enter it
touch scroll.txt                     # create a new file
cp scroll.txt scroll_copy.txt        # create a copy of that file
ls                                   # confirm both files are here
```

---

**Deletion**

Clean up — remove everything you just created.

{: .warning }
> ⚠️ `rm` is permanent. There is no undo, no trash can. Double-check what you are removing before you run it.

```bash
rm scroll.txt                        # remove the file
rm scroll_copy.txt                   # remove the copy
rm -r ~/Desktop/spell_chamber        # remove the folder and all its contents
```

<label class="quest-check"><input type="checkbox" data-room="d1-command-spire" data-key="main"> Exercise complete</label>

{: .note }
> **📤 Casting your progress to the leaderboard**
>
> Whenever you check off a quest, a **🔮 Cast to the leaderboard** button appears beneath it. Click it to reveal your personal **incantation** — a short spell like `cast frost-ember-sigil` — then run it on the Yens, inside your clone, to update the leaderboard.
>
> **First time only:** you'll ready your spell-caster (make `cast` executable) and sign in with `gh auth login` — both covered in **The Repository**.
