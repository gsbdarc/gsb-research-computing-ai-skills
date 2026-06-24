# Instructor Setup — RF Coding Bootcamp 2026

Run these steps before class. Everything here is one-time per cohort unless noted.

---

## Before Day 1

### 1 — Generate and host the Grimoire

Students download the grimoire zip to their laptops at the start of Day 1 (Grimoire Vault room).

```bash
# On the Yens
cd /scratch/shared
git clone https://github.com/gsbdarc/rf-bootcamp-2026.git
cd rf-bootcamp-2026

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

The boss gate challenge lives at `/scratch/shared/rf-bootcamp-2026/boss1/`.

**Create 50 standard spell files (10 per element):**

```bash
mkdir -p /scratch/shared/rf-bootcamp-2026/boss1/

# Grimoire is a flat directory — no subdirectories yet (students sort theirs on laptops)
# Use wildcards on the element name in the filename to grab 10 per element
for elem in fire ice lightning earth wind; do
  ls /scratch/shared/rf-bootcamp-2026/grimoire/*_${elem}_*.spell | head -10 | xargs -I{} cp {} /scratch/shared/rf-bootcamp-2026/boss1/
done
```

**Create the signature spell:**

```bash
cat > /scratch/shared/rf-bootcamp-2026/boss1/void_arcane_6_legendary_archmage.spell << 'EOF'
SIGNATURE: ARCHMAGE-SEAL-7734
EOF
```

Verify:

```bash
ls /scratch/shared/rf-bootcamp-2026/boss1/ | wc -l   # should be 51
ls /scratch/shared/rf-bootcamp-2026/boss1/ | grep arcane  # should show the signature spell
```

**Set permissions so all students can read but not modify:**

```bash
chmod 755 /scratch/shared/rf-bootcamp-2026/boss1/
chmod 644 /scratch/shared/rf-bootcamp-2026/boss1/*.spell
```

---

## Day-of checklist

- [ ] Grimoire zip is accessible at the Google Drive link (test the download in a browser)
- [ ] `/scratch/shared/rf-bootcamp-2026/boss1/` has 51 files, readable by all
- [ ] Signature spell exists: `void_arcane_6_legendary_archmage.spell`
- [ ] Signature string inside it: `SIGNATURE: ARCHMAGE-SEAL-7734`

---

## Solution keys

See `.instructor/boss-gate-1.key.md` for the full step-by-step solution to Boss Gate 1.

---

## Grader notes

The auto-grader (`scripts/check_boss_gates.py`) runs on each student's GitHub Actions after every push. For Boss Gate 1 it checks:
- `signature_spell.txt` exists in the repo
- At least one line in the file ends with `.spell`

It does **not** check the signature string value — any correctly named spell file satisfies the grader.
