#!/usr/bin/env python3
"""Sync your Quest Log progress to the leaderboard.

On your personal course site, tick the quests you finished, then copy the ready
"spell" from the sync command shown on the page. Run it here on the Yens, inside
your clone of your fork:

    python3 scripts/quest_sync.py <spell>

It decodes your progress, writes quest_log.json, and pushes it to your fork so
the leaderboard updates. (Instructor/debug: pass --raw with a base64 token.)
"""

import argparse
import base64
import json
import subprocess
import sys
from pathlib import Path

CLASS_REPO = "gsbdarc/gsb-research-computing-ai-skills"
REPO_ROOT = Path(__file__).resolve().parent.parent
QUEST_LOG = REPO_ROOT / "quest_log.json"
QUEST_KEYS = Path(__file__).resolve().parent / "quest_keys.json"
SPELL_WORDS = REPO_ROOT / "docs" / "_data" / "spell_words.json"


def fnv1a_hex(s):
    """FNV-1a (32-bit) hex digest — must match keyListHash() in quest-log.js."""
    h = 0x811C9DC5
    for ch in s.encode("utf-8"):
        h ^= ch
        h = (h * 0x01000193) & 0xFFFFFFFF
    return format(h, "x")


STALE_MSG = (
    "This spell is from a different version of the site than this clone.\n"
    "Run 'git pull' in your fork, reload the site, copy a fresh spell, and re-cast."
)


def _keys_from_bitfield(raw, keys):
    return [k for i, k in enumerate(keys)
            if (i >> 3) < len(raw) and raw[i >> 3] & (1 << (i & 7))]


def decode_spell(spell):
    """Decode a hyphen-joined word 'spell' into the list of completed keys.

    Layout: one word per bitfield byte, then two 'seal' words carrying the first
    two bytes of the key-list hash (so a spell cast from a stale site is rejected).
    """
    words = spell.strip().split("-")
    keys = json.loads(QUEST_KEYS.read_text())
    wordlist = json.loads(SPELL_WORDS.read_text())
    index = {w: i for i, w in enumerate(wordlist)}
    nbytes = (len(keys) + 7) // 8
    if len(words) != nbytes + 2:
        sys.exit("That doesn't look like a full sync spell — copy a fresh one from the page.")
    try:
        vals = [(index[w] - i * 17) % 256 for i, w in enumerate(words)]
    except KeyError as e:
        sys.exit("Unknown word in the spell (%s) — copy a fresh one from the page." % e.args[0])
    hh = fnv1a_hex(",".join(keys)).rjust(8, "0")
    if vals[nbytes] != int(hh[0:2], 16) or vals[nbytes + 1] != int(hh[2:4], 16):
        sys.exit(STALE_MSG)
    return _keys_from_bitfield(bytes(vals[:nbytes]), keys)


def decode_raw(token):
    """Decode the base64 'version.hash.bitfield' token (instructor/debug form)."""
    parts = token.strip().split(".")
    if len(parts) != 3 or parts[0] != "1":
        sys.exit("Unrecognized --raw token — expected '1.<hash>.<base64>'.")
    _, token_hash, b64 = parts
    keys = json.loads(QUEST_KEYS.read_text())
    if token_hash != fnv1a_hex(",".join(keys)):
        sys.exit(STALE_MSG)
    raw = base64.urlsafe_b64decode(b64 + "=" * (-len(b64) % 4))
    return _keys_from_bitfield(raw, keys)


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=str(REPO_ROOT), capture_output=True, text=True
    )


def require_fork():
    url = git("remote", "get-url", "origin").stdout.strip()
    if not url:
        sys.exit("No git 'origin' remote found — run this inside your cloned fork.")
    if CLASS_REPO in url:
        sys.exit(
            "Your 'origin' points at the class repo (%s), not your own fork.\n"
            "Pushing here would write to the shared repo. Point origin at your\n"
            "fork first, then re-run this." % CLASS_REPO
        )
    return url


def main():
    ap = argparse.ArgumentParser(description="Sync Quest Log progress to your fork.")
    ap.add_argument("spell", help="the sync spell copied from the command on your course site")
    ap.add_argument("--raw", action="store_true",
                    help="treat the argument as a raw base64 token instead of a word spell")
    args = ap.parse_args()

    decoder = decode_raw if (args.raw or args.spell.strip().startswith("1.")) else decode_spell
    try:
        keys = decoder(args.spell)
    except SystemExit:
        raise
    except Exception:
        sys.exit("That spell could not be decoded — copy it again from the page.")
    if not keys:
        sys.exit("No completed quests in that spell — nothing to sync.")

    require_fork()

    QUEST_LOG.write_text(json.dumps({k: True for k in keys}, indent=2) + "\n")
    print("The runes align — %d quest%s sealed into your grimoire (%s)."
          % (len(keys), "" if len(keys) == 1 else "s", QUEST_LOG.name))

    git("add", str(QUEST_LOG))
    commit = git("commit", "-m", "Sync quest log")
    if commit.returncode != 0 and "nothing to commit" in (commit.stdout + commit.stderr):
        print("Already up to date — nothing new to push.")
        return
    push = git("push", "origin", "HEAD:main")
    if push.returncode != 0:
        sys.exit(
            "Push failed:\n" + (push.stderr or push.stdout)
            + "\nIf that's an authentication error, sign in once with 'gh auth login' "
            "on the Yens (Day 1's Repository room), then re-run this."
        )
    print("Pushed to your fork. The leaderboard updates within ~2 minutes.")


if __name__ == "__main__":
    main()
