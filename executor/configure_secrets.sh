#!/usr/bin/env bash
set -euo pipefail

ENV_FILE="/etc/bitvavo-executor.env"

if [ "$(id -u)" -ne 0 ]; then
  echo "Run as root: sudo bash configure_secrets.sh" >&2
  exit 1
fi

if [ ! -f "$ENV_FILE" ]; then
  echo "$ENV_FILE does not exist. Run install.sh first." >&2
  exit 1
fi

printf 'Paste Bitvavo API key, then press Enter: '
IFS= read -r API_KEY
printf 'Paste Bitvavo API secret, then press Enter (input hidden): '
IFS= read -rs API_SECRET
printf '\n'

if [ -z "$API_KEY" ] || [ -z "$API_SECRET" ]; then
  echo "API key/secret cannot be empty." >&2
  unset API_KEY API_SECRET
  exit 1
fi

# Reject multiline values so the environment file cannot be structurally altered.
case "$API_KEY$API_SECRET" in
  *$'\n'*|*$'\r'*)
    echo "Invalid newline in credentials." >&2
    unset API_KEY API_SECRET
    exit 1
    ;;
esac

TMP="$(mktemp)"
trap 'rm -f "$TMP"; unset API_KEY API_SECRET' EXIT

awk -v key="$API_KEY" -v secret="$API_SECRET" '
BEGIN { saw_key=0; saw_secret=0 }
/^BITVAVO_API_KEY=/ { print "BITVAVO_API_KEY=" key; saw_key=1; next }
/^BITVAVO_API_SECRET=/ { print "BITVAVO_API_SECRET=" secret; saw_secret=1; next }
{ print }
END {
  if (!saw_key) print "BITVAVO_API_KEY=" key
  if (!saw_secret) print "BITVAVO_API_SECRET=" secret
}
' "$ENV_FILE" > "$TMP"

install -o root -g root -m 0600 "$TMP" "$ENV_FILE"
unset API_KEY API_SECRET

echo "Credentials stored in $ENV_FILE with mode 0600."
echo "DRY_RUN remains enabled. No live order can be placed yet."
