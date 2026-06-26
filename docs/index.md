---
layout: default
title: "The DARC Dungeon"
nav_order: 0
permalink: /
---

# The DARC Dungeon

*You stand at the entrance of an ancient tower. Four floors rise above you, each sealed with an Archmage's crest. Somewhere inside, the secrets of computational research await — CLI runes carved into stone walls, SLURM forges humming in the depths, GPU engines blazing on the highest floor.*

{: .important }
> **Day 1 — Do this first**
>
> 1. **Fork this repo** — click **Fork** in the top-right corner of the [GitHub page](https://github.com/gsbdarc/rf-bootcamp-2026) to create your own copy
> 2. **Enable Actions** on your fork — click the **Actions** tab → **"I understand my workflows, go ahead and enable them"**
> 3. **Enable GitHub Pages** on your fork: Settings → Pages → Build and deployment → Source → select **GitHub Actions** (saves automatically)
> 4. **Trigger the first build** — Actions → "Deploy Jekyll site to Pages" → Run workflow → Run workflow
> 5. **Open your personal dungeon site** (~2 min after step 4): `https://YOUR-USERNAME.github.io/rf-bootcamp-2026/`
>
> Once your site is live, put a **🟢 green sticky** on your laptop lid. If you're stuck on any step, put a **🔴 red sticky** up so an instructor can come help.
>
> Your site is your quest log for the entire course. Keep it open — every room, exercise, and leaderboard submission happens here.

**How the dungeon works**

Each floor corresponds to one day of the bootcamp. Every floor has **rooms** — enter each room, complete the **Main Quest**, and move to the next.

Finished early? Look for **Side Quests** — optional deeper challenges that unlock a named **Weapon** (a skill you carry for the rest of the course). Weapons compound: what you earn in Day 1 pays off in Day 3.

Each floor ends with a **Boss Gate**: a capstone challenge you submit by committing your work to your fork on GitHub. Push your commit → the grader runs → the next floor unlocks on your personal site.

Every completed quest adds to your **Quest Log** (shown in the widget, bottom-left). Completing all main quests on each floor is enough to pass the Boss Gate and advance. Side quests push your level higher — that is what separates the top of the leaderboard. The more side quests you finish, the higher your rank.

---

## The Four Floors

{% assign unlocked = site.data.progress.unlocked_floors %}

<div class="dungeon-layout">
  <div class="floor-card{% unless unlocked contains 1 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day1/' | relative_url }}">Floor 1 — The Gatehouse</a>{% unless unlocked contains 1 %} 🔒{% endunless %}</h3>
    <p>Levels 1–3 &nbsp;·&nbsp; 6 rooms + Boss Gate</p>
  </div>
  <div class="floor-skills">CLI &middot; SSH &middot; Yens file system &middot; Git</div>

  <div class="floor-card{% unless unlocked contains 2 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day2/' | relative_url }}">Floor 2 — The Alchemist's Lab</a>{% unless unlocked contains 2 %} 🔒{% endunless %}</h3>
    <p>Levels 4–6 &nbsp;·&nbsp; 8 rooms + Boss Gate</p>
  </div>
  <div class="floor-skills">JupyterHub &middot; Python envs &middot; AI Playground &middot; Secure key management &middot; Pydantic &middot; AI agents &amp; data privacy</div>

  <div class="floor-card{% unless unlocked contains 3 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day3/' | relative_url }}">Floor 3 — The SLURM Mines</a>{% unless unlocked contains 3 %} 🔒{% endunless %}</h3>
    <p>Levels 7–8 &nbsp;·&nbsp; 6 rooms + Boss Gate</p>
  </div>
  <div class="floor-skills">SLURM &middot; Resource estimation &middot; Job lifecycle &middot; Job monitoring</div>

  <div class="floor-card{% unless unlocked contains 4 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day4/' | relative_url }}">Floor 4 — The GPU Fortress</a>{% unless unlocked contains 4 %} 🔒{% endunless %}</h3>
    <p>Levels 9–10 &nbsp;·&nbsp; 7 rooms + Boss Gate</p>
  </div>
  <div class="floor-skills">Job arrays &middot; GPU tiers &middot; Local LLMs &middot; OpenAI-compatible API &middot; Human vs LLM</div>
</div>

---

*The gate is open. The torch is lit. Whatever waits inside — the shell that answers in milliseconds, the cluster that never sleeps, the model you'll summon from bare silicon — it is yours to claim.*

*Good luck, adventurer. The dungeon awaits.*
