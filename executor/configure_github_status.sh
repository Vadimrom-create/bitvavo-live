#!/usr/bin/env bash
set -euo pipefail

ENV_FILE="/etc/bitvavo-executor.env"
REPO_DEFAULT="Vadimrom-create/bitvavo-live"

if [ "$(id -u)" -ne 0 ]; then
  echo "Run as root: sudo bash configure_github_status.sh" >&2
  exit 1
fi

if [ ! -f "$ENV_FILE" ]; then
  echo "$ENV_FILE does not exist. Run install.sh first." >&2
  exit 1
fi

printf 'Paste GitHub fine-grained token, then press Enter (input hidden): '
IFS= read -rs GITHUB_TOKEN
printf '\n'

if [ -z "$GITHUB_TOKEN" ]; then
  echo "GitHub token cannot be empty." >&2
  unset GITHUB_TOKEN
  exit 1
fi

case "$GITHUB_TOKEN" in
  *$'\n'*|*$'\r'*)
    echo "Invalid newline in token." >&2
    unset GITHUB_TOKEN
    exit 1
    ;;
esac

TMP="$(mktemp)"
trap 'rm -f "$TMP"; unset GITHUB_TOKEN' EXIT

awk -v token="$GITHUB_TOKEN" -v repo="$REPO_DEFAULT" '
BEGIN { saw_token=0; saw_repo=0 }
/^GITHUB_STATUS_TOKEN=/ { print "GITHUB_STATUS_TOKEN=" token; saw_token=1; next }
/^GITHUB_STATUS_REPO=/ { print "GITHUB_STATUS_REPO=" repo; saw_repo=1; next }
{ print }
END {
  if (!saw_token) print "GITHUB_STATUS_TOKEN=" token
  if (!saw_repo) print "GITHUB_STATUS_REPO=" repo
}
' "$ENV_FILE" > "$TMP"

install -o root -g root -m 0600 "$TMP" "$ENV_FILE"
unset GITHUB_TOKEN

echo "GitHub status token stored in $ENV_FILE with mode 0600."
echo "The executor can now publish sanitized status files after restart."
