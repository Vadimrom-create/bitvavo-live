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

apt-get update -y
apt-get install -y python3 python3-venv python3-pip curl ca-certificates

if ! id bitvavoexec >/dev/null 2>&1; then
  useradd --system --home "$STATE_DIR" --shell /usr/sbin/nologin bitvavoexec
fi

install -d -m 0755 "$APP_DIR"
install -d -o bitvavoexec -g bitvavoexec -m 0700 "$STATE_DIR"

curl -fsSL "$REPO_RAW/daemon.py" -o "$APP_DIR/daemon.py"
curl -fsSL "$REPO_RAW/bitvavo_client.py" -o "$APP_DIR/bitvavo_client.py"
curl -fsSL "$REPO_RAW/requirements.txt" -o "$APP_DIR/requirements.txt"
curl -fsSL "$REPO_RAW/.env.example" -o "$APP_DIR/.env.example"
curl -fsSL "$REPO_RAW/bitvavo-executor.service" -o "$SERVICE_FILE"

python3 -m venv "$APP_DIR/.venv"
"$APP_DIR/.venv/bin/pip" install --upgrade pip
"$APP_DIR/.venv/bin/pip" install -r "$APP_DIR/requirements.txt"

chown -R root:root "$APP_DIR"
chmod 0755 "$APP_DIR/daemon.py" "$APP_DIR/bitvavo_client.py"
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
  "Next: edit $ENV_FILE, then run:" \
  "  sudo systemctl start bitvavo-executor" \
  "  sudo journalctl -u bitvavo-executor -f"
