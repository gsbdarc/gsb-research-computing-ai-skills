# Instructor Setup — RF Coding Bootcamp 2026

Run these steps before class. Everything here is one-time per cohort unless noted.

---

## Before Day 1

### 1 — Generate and host the Grimoire

Students download the grimoire zip to their laptops at the start of Day 1 (Grimoire Vault room).

```bash
# On the Yens
cd /scratch/shared
git clone https://github.com/gsbdarc/gsb-research-computing-ai-skills.git
cd gsb-research-computing-ai-skills

python3 scripts/generate_grimoire.py --seed 2026 --count 300
# creates grimoire/ with ~300 .spell files named name_element_tier_type_mastery.spell

zip -r grimoire.zip grimoire/
ml rclone
rclone copy grimoire.zip gdrive:<your-shared-drive-folder>/
```

Then in Google Drive:
- Open `grimoire.zip` → Share → **Stanford University → Viewer**
- Copy the link

Update the link in two places if it changes:
- `docs/day1/grimoire-vault.md` — the download button
- `docs/index.md` — the entrance page reference

Current link: `https://drive.google.com/file/d/1pGFegdCMjzHDDmfjJrSuZe10L8zrQsWo/view?usp=sharing`

---

### 2 — Stage Boss Gate 1 vault in scratch

The boss gate challenge lives at `/scratch/shared/gsb-research-computing-ai-skills/boss1/`.

**Create 50 standard spell files (10 per element):**

```bash
mkdir -p /scratch/shared/gsb-research-computing-ai-skills/boss1/

# Grimoire is a flat directory — no subdirectories yet (students sort theirs on laptops)
# Use wildcards on the element name in the filename to grab 10 per element
for elem in fire ice lightning earth wind; do
  ls /scratch/shared/gsb-research-computing-ai-skills/grimoire/*_${elem}_*.spell | head -10 | xargs -I{} cp {} /scratch/shared/gsb-research-computing-ai-skills/boss1/
done
```

**Create the signature spell:**

```bash
cat > /scratch/shared/gsb-research-computing-ai-skills/boss1/void_arcane_6_legendary_archmage.spell << 'EOF'
SIGNATURE: ARCHMAGE-SEAL-7734
EOF
```

Verify:

```bash
ls /scratch/shared/gsb-research-computing-ai-skills/boss1/ | wc -l   # should be 51
ls /scratch/shared/gsb-research-computing-ai-skills/boss1/ | grep arcane  # should show the signature spell
```

**Set permissions so all students can read but not modify:**

```bash
chmod 755 /scratch/shared/gsb-research-computing-ai-skills/boss1/
chmod 644 /scratch/shared/gsb-research-computing-ai-skills/boss1/*.spell
```

---

## Before Day 1 — Enroll students

Add each student's GitHub username to `docs/_data/students.yml` in the instructor repo before class starts. The leaderboard will show anyone listed here as soon as they push to their fork.

```yaml
- username: their-github-username
  name: "First L."
```

Commit and push to `main`. GitHub Pages rebuilds in ~2 minutes and the leaderboard is live.

---

## Displaying the Leaderboard on the Projector

Open this URL in a browser on the projector machine:

```
https://gsbdarc.github.io/gsb-research-computing-ai-skills/leaderboard/
```

**What it shows:**
- Each student's rank, level (Initiate → Archmage), boss gates cleared (⚔ = day cleared), and progress bar
- Students who did side quests rank higher — the progress bar shows who went beyond the main quests
- Students with no progress yet show as Level 1 / Initiate with an empty bar

**Refreshing:**
- Auto-refreshes every 2 minutes
- Click **↻ Refresh** for an instant update

**When to pull it up:**
- End of each day after students sync their quest logs (Claude Code commits `quest_log.json` to their fork)
- Boss gate clears show up once a student's `quest_log.json` marks that gate's key `true` and is pushed

**Reading the leaderboard:**
- ⚔ icons = boss gates cleared (one per day). A student with 2 swords has cleared Days 1 and 2.
- Progress bar = total quests completed including side quests. Long bar = went above and beyond.
- Level title = quick read on depth: Journeyman = solid, Master/Archmage = exceptional.
- Students with no bar at all = haven't synced yet, or are behind — worth checking in with.

---

## Day-of checklist

- [ ] Grimoire zip is accessible at the Google Drive link (test the download in a browser)
- [ ] `/scratch/shared/gsb-research-computing-ai-skills/boss1/` has 51 files, readable by all
- [ ] Signature spell exists: `void_arcane_6_legendary_archmage.spell`
- [ ] Signature string inside it: `SIGNATURE: ARCHMAGE-SEAL-7734`

---

## Solution keys

See `.instructor/boss-gate-1.key.md` for the full step-by-step solution to Boss Gate 1.

---

## Boss gates

There is **no auto-grader** — every floor is unlocked from the start and boss gates are optional capstone challenges. A student "clears" a gate by committing the gate's deliverables and marking its key `true` in `quest_log.json` (via Claude Code). The leaderboard reads those keys directly: `d1-boss-gate-1.main`, `d2-boss-gate.commit`, `d3-boss-gate.commit`, `d4-boss-gate.commit`.
