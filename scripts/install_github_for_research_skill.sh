#!/usr/bin/env bash
#
# install_github_for_research_skill.sh — Install the "github-for-research"
# Claude Code skill from its canonical repo, so it is available in every
# project you work on.
#
# The skill teaches research-grade GitHub practice (attribution, issues,
# branches, the GitHub Flow work cycle, data-integrity checks, reproducible
# environments) and lives in its own repository:
#     https://github.com/gsbdarc/claude-skill-github-for-research
#
# Usage:
#     bash scripts/install_github_for_research_skill.sh
#
# Safe to re-run at any time: it pulls the latest version of the skill and
# updates your installation in place.
#
set -euo pipefail

REPO_URL="https://github.com/gsbdarc/claude-skill-github-for-research.git"
SKILL_SUBPATH=".claude/skills/github-for-research"

CACHE_DIR="${HOME}/.claude/skill-sources/claude-skill-github-for-research"
SKILLS_DIR="${HOME}/.claude/skills"
LINK="${SKILLS_DIR}/github-for-research"
TARGET="${CACHE_DIR}/${SKILL_SUBPATH}"

echo "==> Installing the 'github-for-research' Claude Code skill"

# 1. Clone the skill repo (first run) or pull the latest (subsequent runs).
if [ -d "${CACHE_DIR}/.git" ]; then
  echo "    Updating existing copy in ${CACHE_DIR}"
  git -C "${CACHE_DIR}" pull --ff-only --quiet
else
  echo "    Cloning ${REPO_URL}"
  mkdir -p "$(dirname "${CACHE_DIR}")"
  git clone --quiet "${REPO_URL}" "${CACHE_DIR}"
fi

if [ ! -f "${TARGET}/SKILL.md" ]; then
  echo "ERROR: expected skill not found at ${TARGET}" >&2
  exit 1
fi

# 2. Link it into your personal Claude skills folder so it loads everywhere.
mkdir -p "${SKILLS_DIR}"
if [ -L "${LINK}" ] && [ "$(readlink "${LINK}")" = "${TARGET}" ]; then
  echo "    Symlink already correct — nothing to change"
elif [ -e "${LINK}" ] || [ -L "${LINK}" ]; then
  backup="${LINK}.backup.$(date +%Y%m%d%H%M%S)"
  echo "    Existing ${LINK} found — moving it aside to ${backup}"
  mv "${LINK}" "${backup}"
  ln -s "${TARGET}" "${LINK}"
else
  ln -s "${TARGET}" "${LINK}"
fi

echo "==> Done."
echo "    Skill installed at: ${LINK}"
echo "                     -> ${TARGET}"
echo "    Re-run this script anytime to pull the latest version."
