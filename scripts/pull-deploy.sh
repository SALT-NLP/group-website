#!/bin/bash
#
# Pulls the built site from the "deploy" branch on GitHub and syncs it into
# the cPanel docroot. Runs on the Stanford Domains server via cron every
# 5 minutes; GitHub Actions no longer pushes over SSH, it just updates the
# deploy branch and this script picks the change up over outbound HTTPS.

set -euo pipefail

REPO_URL="https://github.com/SALT-NLP/group-website.git"
BRANCH="deploy"
CLONE_DIR="$HOME/deploy-repo"
DOCROOT="$HOME/saltlab.stanford.edu"
LOG_FILE="$HOME/pull-deploy.log"
LOCK_FILE="$HOME/pull-deploy.lock"
STALE_SECONDS=900

if [ -e "$LOCK_FILE" ]; then
    LOCK_AGE=$(( $(date +%s) - $(stat -c %Y "$LOCK_FILE" 2>/dev/null || stat -f %m "$LOCK_FILE") ))
    if [ "$LOCK_AGE" -lt "$STALE_SECONDS" ] && kill -0 "$(cat "$LOCK_FILE")" 2>/dev/null; then
        exit 0
    fi
fi
echo $$ > "$LOCK_FILE"
trap 'rm -f "$LOCK_FILE"' EXIT

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

if [ ! -d "$CLONE_DIR/.git" ]; then
    log "Cloning $REPO_URL ($BRANCH) into $CLONE_DIR"
    git clone --branch "$BRANCH" --single-branch "$REPO_URL" "$CLONE_DIR" >> "$LOG_FILE" 2>&1
fi

cd "$CLONE_DIR"

BEFORE=$(git rev-parse HEAD)
git fetch origin "$BRANCH" >> "$LOG_FILE" 2>&1
git reset --hard "origin/$BRANCH" >> "$LOG_FILE" 2>&1
AFTER=$(git rev-parse HEAD)

if [ "$BEFORE" = "$AFTER" ]; then
    exit 0
fi

log "Deploy branch updated: $BEFORE -> $AFTER, syncing to $DOCROOT"
rsync -a --delete --exclude='.git' "$CLONE_DIR"/ "$DOCROOT"/ >> "$LOG_FILE" 2>&1
log "Sync complete"
