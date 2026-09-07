#!/usr/bin/env bash
set -euo pipefail

ENV_FILE="/etc/bitvavo-executor.env"

if [ "$(id -u)" -ne 0 ]; then
  echo "Run as root: sudo bash enable_live_test_mode.sh" >&2
  exit 1
fi

if [ ! -f "$ENV_FILE" ]; then
  echo "$ENV_FILE does not exist." >&2
  exit 1
fi

set_kv() {
  local key="$1" value="$2"
  if grep -q "^${key}=" "$ENV_FILE"; then
    sed -i "s|^${key}=.*|${key}=${value}|" "$ENV_FILE"
  else
    printf '%s=%s\n' "$key" "$value" >> "$ENV_FILE"
  fi
}

# Live execution is enabled only for the deliberately tiny end-to-end test.
set_kv DRY_RUN false
set_kv MAX_ORDER_EUR 10
set_kv MAX_TOTAL_NEW_EXPOSURE_EUR 10
set_kv AUTO_CANCEL_UNKNOWN_ORDERS false
set_kv SECURITY_FREEZE_ON_UNKNOWN true

chmod 600 "$ENV_FILE"
systemctl restart bitvavo-executor
sleep 2

echo "LIVE_TEST_MODE_ENABLED"
echo "DRY_RUN=false"
echo "MAX_ORDER_EUR=10"
echo "MAX_TOTAL_NEW_EXPOSURE_EUR=10"
echo "AUTO_CANCEL_UNKNOWN_ORDERS=false"
systemctl is-active bitvavo-executor
