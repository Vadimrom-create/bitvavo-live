#!/usr/bin/env bash
set -euo pipefail

REPO_RAW="https://raw.githubusercontent.com/Vadimrom-create/bitvavo-live/main/executor"
APP_DIR="/opt/bitvavo-executor"
STATE_DIR="/var/lib/bitvavo-executor"
ENV_FILE="/etc/bitvavo-executor.env"
SERVICE_FILE="/etc/systemd/system/bitvavo-executor.service"

if [ "$(id -u)" -ne 0 ]; then
  echo "Run as root: sudo bash install.sh" >&2
  exit 1
fi

# Oracle Linux 9 uses dnf. Keep Debian/Ubuntu support for portability.
if command -v dnf >/dev/null 2>&1; then
  dnf -y install python3 python3-pip curl ca-certificates
elif command -v yum >/dev/null 2>&1; then
  yum -y install python3 python3-pip curl ca-certificates
elif command -v apt-get >/dev/null 2>&1; then
  apt-get update -y
  apt-get install -y python3 python3-venv python3-pip curl ca-certificates
else
  echo "Unsupported Linux distribution: no dnf/yum/apt-get found" >&2
  exit 1
fi

NOLOGIN="$(command -v nologin || true)"
[ -n "$NOLOGIN" ] || NOLOGIN="/sbin/nologin"

if ! id bitvavoexec >/dev/null 2>&1; then
  useradd --system --home "$STATE_DIR" --shell "$NOLOGIN" bitvavoexec
fi

install -d -m 0755 "$APP_DIR"
install -d -o bitvavoexec -g bitvavoexec -m 0700 "$STATE_DIR"

curl -fsSL "$REPO_RAW/daemon.py" -o "$APP_DIR/daemon.py"
curl -fsSL "$REPO_RAW/bitvavo_client.py" -o "$APP_DIR/bitvavo_client.py"
curl -fsSL "$REPO_RAW/requirements.txt" -o "$APP_DIR/requirements.txt"
curl -fsSL "$REPO_RAW/.env.example" -o "$APP_DIR/.env.example"
curl -fsSL "$REPO_RAW/configure_secrets.sh" -o "$APP_DIR/configure_secrets.sh"
curl -fsSL "$REPO_RAW/bitvavo-executor.service" -o "$SERVICE_FILE"

# venv is bundled with Python on Oracle Linux 9; fail clearly if unavailable.
if ! python3 -m venv "$APP_DIR/.venv"; then
  echo "python3 venv creation failed" >&2
  exit 1
fi
"$APP_DIR/.venv/bin/pip" install --upgrade pip
"$APP_DIR/.venv/bin/pip" install -r "$APP_DIR/requirements.txt"

chown -R root:root "$APP_DIR"
chmod 0755 "$APP_DIR/daemon.py" "$APP_DIR/bitvavo_client.py" "$APP_DIR/configure_secrets.sh"
chmod 0644 "$APP_DIR/requirements.txt" "$SERVICE_FILE"

if [ ! -f "$ENV_FILE" ]; then
  cp "$APP_DIR/.env.example" "$ENV_FILE"
  chmod 0600 "$ENV_FILE"
  echo
  echo "Created $ENV_FILE. It contains NO secrets yet."
fi

systemctl daemon-reload
systemctl enable bitvavo-executor.service

echo
printf '%s\n' \
  "Installation complete." \
  "The service is NOT started automatically until the API credentials are added." \
  "Next: run sudo $APP_DIR/configure_secrets.sh" \
  "Then start in DRY_RUN mode with: sudo systemctl start bitvavo-executor" \
  "Logs: sudo journalctl -u bitvavo-executor -f"
