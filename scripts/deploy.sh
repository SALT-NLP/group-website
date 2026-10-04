#!/bin/bash
#
# Builds the site locally and uploads it to the Stanford Domains server over
# scp. Use this from any machine with SSH access to the server; the GitHub
# Actions deploy can't reach the server because it blocks GitHub's IPs.
#
# Usage:
#   scripts/deploy.sh
#
# Overridable environment variables:
#   DEPLOY_USER   SSH user on the server            (default: saltsudo)
#   DEPLOY_HOST   server address                    (default: 146.190.148.141)
#   DEPLOY_PORT   SSH port                          (default: 22)
#   DEPLOY_PATH   docroot, relative to remote $HOME (default: saltlab.stanford.edu)
#   SSH_KEY       private key to use                (default: ssh's own default)

set -euo pipefail

DEPLOY_USER="${DEPLOY_USER:-saltsudo}"
DEPLOY_HOST="${DEPLOY_HOST:-146.190.148.141}"
DEPLOY_PORT="${DEPLOY_PORT:-22}"
DEPLOY_PATH="${DEPLOY_PATH:-saltlab.stanford.edu}"
UPLOAD_DIR="deploy-upload"
HUGO_VERSION="0.121.2"  # Keep in sync with .github/workflows/deploy.yml

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Reuse one SSH connection so you only authenticate once.
CONTROL_PATH="$(mktemp -u "${TMPDIR:-/tmp}/salt-deploy.XXXXXX")"
SSH_OPTS=(-p "$DEPLOY_PORT" -o ControlMaster=auto -o ControlPath="$CONTROL_PATH" -o ControlPersist=120)
SCP_OPTS=(-P "$DEPLOY_PORT" -o ControlMaster=auto -o ControlPath="$CONTROL_PATH" -o ControlPersist=120)
if [ -n "${SSH_KEY:-}" ]; then
    SSH_OPTS+=(-i "$SSH_KEY")
    SCP_OPTS+=(-i "$SSH_KEY")
fi
REMOTE="$DEPLOY_USER@$DEPLOY_HOST"
cleanup() { ssh "${SSH_OPTS[@]}" -O exit "$REMOTE" 2>/dev/null || true; }
trap cleanup EXIT

command -v hugo >/dev/null || { echo "Error: hugo is not installed." >&2; exit 1; }
if ! hugo version | grep -q "v$HUGO_VERSION"; then
    echo "Warning: expected Hugo v$HUGO_VERSION, found: $(hugo version)" >&2
fi

if [ -n "$(git status --porcelain)" ]; then
    echo "Warning: you have uncommitted changes; they will be deployed too." >&2
fi
if [ "$(git rev-parse --abbrev-ref HEAD)" != "main" ]; then
    echo "Warning: you are not on the main branch." >&2
fi

echo "==> Building site"
hugo --cleanDestinationDir
find public -name .DS_Store -delete

echo "==> Uploading to $REMOTE:~/$UPLOAD_DIR"
ssh "${SSH_OPTS[@]}" "$REMOTE" "rm -rf ~/$UPLOAD_DIR"
scp -q -r "${SCP_OPTS[@]}" public "$REMOTE:$UPLOAD_DIR"

# Sync the upload into the docroot, removing stale files but keeping
# server-managed ones (cPanel SSL validation, .htaccess, cgi-bin).
echo "==> Syncing into ~/$DEPLOY_PATH"
ssh "${SSH_OPTS[@]}" "$REMOTE" "rsync -a --delete \
    --exclude='.well-known' --exclude='.htaccess' --exclude='cgi-bin' \
    ~/$UPLOAD_DIR/ ~/$DEPLOY_PATH/ && rm -rf ~/$UPLOAD_DIR"

echo "==> Done. Check https://saltlab.stanford.edu/"
