---
layout: default
title: "The Research Guild"
parent: "Day 4 — The GPU Fortress"
nav_order: 9
permalink: /day4/research-guild/
---

# The Research Guild

*The fortress doors swing open and the noise of battle fades. You step out into the courtyard where other researchers sit around low fires, arguing about cluster quotas and model latency and the best way to parallelize a dataset nobody has touched before. This is the Guild — not a classroom, not a tutorial, but the place where the real work happens: peer to peer, question by question, year after year. Your dungeon run is over. Your research career is just warming up.*

---

## Staying Connected

The DARC team runs the Yens and supports GSB researchers year-round. You are not expected to remember everything from this week — you are expected to know where to ask.

### Slack — `#gsb-yen-users`

Join the **#gsb-yen-users** channel on Stanford Slack. It's where Yen users and the DARC team:
- Answer questions about the cluster, SLURM, storage, and software
- Share tips and scripts that didn't make it into any tutorial
- Announce workshops, maintenance windows, and new hardware
- Collect feedback about what to improve

**Join here:** [#gsb-yen-users](https://circlerss.slack.com/archives/C01JXJ6U4E5)

If the link does not open automatically, open the Slack app, search for **#gsb-yen-users** in Channels, and join from there.

### Email

For questions that need a direct answer from the team, or anything you'd rather not post in a channel:

📧 **[gsb_darcresearch@stanford.edu](mailto:gsb_darcresearch@stanford.edu)**

Response time is typically one business day.

---

## What to Do When You're Stuck

| Situation | Where to go |
|-----------|-------------|
| "My SLURM job keeps failing" | `#gsb-yen-users` — someone has seen it |
| "Is this dataset ok to send to an LLM?" | Email DARC or ask your IRB coordinator |
| "I want to run something much bigger" | Email DARC — we can advise on allocations |
| "Is there a workshop on X?" | Watch `#gsb-yen-users` for announcements |
| "My code works on my laptop but not the Yens" | `#gsb-yen-users` — include your error output |

---

## Keep Exploring

Everything you ran this week is in your fork. Future projects can start from the same patterns:

- **More data, same pipeline:** swap the input list in your SLURM array script
- **Different model:** change `base_url` and `model` — the rest is identical
- **New dataset type:** adapt your Pydantic schema, rerun the pipeline
- **Need a GPU:** copy your `h200-chamber` job script and swap the `--gres` flag

The leaderboard stays up. Side quests you didn't finish are still there. The dungeon will be waiting.

