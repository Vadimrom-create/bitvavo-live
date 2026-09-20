#!/usr/bin/env bash
set -euo pipefail

SRC='https://raw.githubusercontent.com/Vadimrom-create/bitvavo-live/main/oracle/bitvavo_public_probe.py'
APP='/opt/bitvavo-public-probe'
UNIT='/etc/systemd/system/bitvavo-public-probe.service'

useradd --system --no-create-home --shell /sbin/nologin bitvavoprobe 2>/dev/null || true
install -d -o root -g root -m 0755 "$APP"
curl -fsSL "$SRC" -o "$APP/server.py"
chmod 0755 "$APP/server.py"

cat > "$UNIT" <<'EOF'
[Unit]
Description=Bitvavo public read-only market probe
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=bitvavoprobe
Group=bitvavoprobe
ExecStart=/usr/bin/python3 /opt/bitvavo-public-probe/server.py
Restart=always
RestartSec=3
TimeoutStopSec=10
MemoryHigh=192M
MemoryMax=256M
TasksMax=64
LimitNOFILE=1024
OOMScoreAdjust=500
NoNewPrivileges=true
PrivateTmp=true
ProtectHome=true
ProtectSystem=strict
ProtectKernelTunables=true
ProtectKernelModules=true
ProtectControlGroups=true
RestrictSUIDSGID=true
LockPersonality=true

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable --now bitvavo-public-probe.service
if systemctl is-active --quiet firewalld; then
  ZONE="$(firewall-cmd --get-active-zones | awk 'NR==1{print $1}')"
  ZONE="${ZONE:-$(firewall-cmd --get-default-zone)}"
  # Preserve remote administration before any reload. The previous installer
  # only persisted 8787, which was not defensive enough.
  firewall-cmd --zone="$ZONE" --permanent --add-service=ssh >/dev/null
  firewall-cmd --zone="$ZONE" --permanent --add-port=8787/tcp >/dev/null
  firewall-cmd --zone="$ZONE" --add-service=ssh >/dev/null || true
  firewall-cmd --zone="$ZONE" --add-port=8787/tcp >/dev/null || true
  firewall-cmd --reload >/dev/null
fi

echo '=== SERVICE ==='
systemctl is-active bitvavo-public-probe.service
echo '=== PORT ==='
ss -lntp | grep ':8787' || true
echo '=== HEALTH ==='
curl -fsS http://127.0.0.1:8787/health; echo
echo '=== BTC PROBE ==='
curl -fsS 'http://127.0.0.1:8787/quote?market=BTC-EUR&stake_eur=75'; echo
