#!/usr/bin/env bash
set -euo pipefail

# One-time bootstrap for the restricted GitHub -> Oracle deployment channel.
# Usage:
#   sudo bash bootstrap_oracle_deploy.sh 'ssh-ed25519 AAAA... github-actions-bitvavo-oracle'

DEPLOY_USER="bitvavo-deploy"
SERVICE="bitvavo-public-probe.service"
APP_DIR="/opt/bitvavo-public-probe"
CONTROL="/usr/local/sbin/bitvavo-oracle-control"
GATEWAY="/usr/local/sbin/bitvavo-deploy-gateway"
SUDOERS="/etc/sudoers.d/bitvavo-oracle-deploy"
REPO="https://github.com/Vadimrom-create/bitvavo-live.git"

if [[ "${EUID}" -ne 0 ]]; then
  echo "Run as root (sudo)." >&2
  exit 1
fi

PUBKEY="${1:-}"
if [[ ! "${PUBKEY}" =~ ^ssh-ed25519[[:space:]]+[A-Za-z0-9+/=]+([[:space:]].*)?$ ]]; then
  echo "Expected one ed25519 public key as the first argument." >&2
  exit 2
fi

command -v git >/dev/null || { echo "git is required" >&2; exit 3; }
command -v curl >/dev/null || { echo "curl is required" >&2; exit 3; }
command -v python3 >/dev/null || { echo "python3 is required" >&2; exit 3; }
command -v systemctl >/dev/null || { echo "systemd is required" >&2; exit 3; }
command -v sudo >/dev/null || { echo "sudo is required" >&2; exit 3; }

if ! id "${DEPLOY_USER}" >/dev/null 2>&1; then
  useradd --create-home --shell /bin/bash "${DEPLOY_USER}"
fi
passwd -l "${DEPLOY_USER}" >/dev/null 2>&1 || true

install -d -o "${DEPLOY_USER}" -g "${DEPLOY_USER}" -m 0700 "/home/${DEPLOY_USER}/.ssh"
AUTH="/home/${DEPLOY_USER}/.ssh/authorized_keys"
FORCED="restrict,command=\"${GATEWAY}\" ${PUBKEY}"
printf '%s\n' "${FORCED}" > "${AUTH}"
chown "${DEPLOY_USER}:${DEPLOY_USER}" "${AUTH}"
chmod 0600 "${AUTH}"

cat > "${GATEWAY}" <<'GATEWAY'
#!/usr/bin/env bash
set -euo pipefail
cmd="${SSH_ORIGINAL_COMMAND:-}"
case "${cmd}" in
  health|status|restart|logs)
    exec sudo /usr/local/sbin/bitvavo-oracle-control "${cmd}"
    ;;
  deploy [0-9a-f]*)
    sha="${cmd#deploy }"
    [[ "${sha}" =~ ^[0-9a-f]{40}$ ]] || { echo "invalid sha" >&2; exit 64; }
    exec sudo /usr/local/sbin/bitvavo-oracle-control deploy "${sha}"
    ;;
  *)
    echo "command not allowed" >&2
    exit 126
    ;;
esac
GATEWAY
chmod 0755 "${GATEWAY}"
chown root:root "${GATEWAY}"

cat > "${CONTROL}" <<'CONTROL'
#!/usr/bin/env bash
set -Eeuo pipefail

SERVICE="bitvavo-public-probe.service"
APP_DIR="/opt/bitvavo-public-probe"
REPO="https://github.com/Vadimrom-create/bitvavo-live.git"
HEALTH="http://127.0.0.1:8787/health"

health() {
  systemctl is-active --quiet "${SERVICE}"
  curl --fail --silent --show-error --max-time 5 "${HEALTH}"
  printf '\n'
}

case "${1:-}" in
  health)
    health
    ;;
  status)
    systemctl --no-pager --full status "${SERVICE}" | tail -n 35
    health
    ;;
  restart)
    systemctl restart "${SERVICE}"
    for _ in {1..10}; do
      sleep 1
      if health; then
        exit 0
      fi
    done
    echo "healthcheck failed after restart" >&2
    exit 1
    ;;
  logs)
    journalctl -u "${SERVICE}" -n 120 --no-pager --output=short-iso
    ;;
  deploy)
    sha="${2:-}"
    [[ "${sha}" =~ ^[0-9a-f]{40}$ ]] || { echo "invalid sha" >&2; exit 64; }

    tmp="$(mktemp -d /tmp/bitvavo-deploy.XXXXXX)"
    backup="${APP_DIR}/server.py.previous"
    trap 'rm -rf "${tmp}"' EXIT

    git -C "${tmp}" init -q
    git -C "${tmp}" remote add origin "${REPO}"
    git -C "${tmp}" fetch -q --depth=150 origin main
    if ! git -C "${tmp}" cat-file -e "${sha}^{commit}" 2>/dev/null; then
      echo "requested sha is not present in fetched main history" >&2
      exit 65
    fi
    if ! git -C "${tmp}" merge-base --is-ancestor "${sha}" FETCH_HEAD; then
      echo "requested sha is not an ancestor of origin/main" >&2
      exit 65
    fi

    git -C "${tmp}" show "${sha}:oracle/bitvavo_public_probe.py" > "${tmp}/server.py"
    python3 -m py_compile "${tmp}/server.py"

    install -d -o root -g root -m 0755 "${APP_DIR}"
    if [[ -f "${APP_DIR}/server.py" ]]; then
      cp -a "${APP_DIR}/server.py" "${backup}"
    fi
    install -o root -g root -m 0755 "${tmp}/server.py" "${APP_DIR}/server.py"
    printf '%s\n' "${sha}" > "${APP_DIR}/DEPLOYED_SHA"

    systemctl restart "${SERVICE}"
    ok=0
    for _ in {1..12}; do
      sleep 1
      if health >/dev/null 2>&1; then
        ok=1
        break
      fi
    done
    if [[ "${ok}" -ne 1 ]]; then
      echo "new version failed healthcheck; rolling back" >&2
      if [[ -f "${backup}" ]]; then
        cp -a "${backup}" "${APP_DIR}/server.py"
        systemctl restart "${SERVICE}"
        sleep 2
        health || true
      fi
      exit 70
    fi

    echo "DEPLOYED_SHA=${sha}"
    health
    ;;
  *)
    echo "usage: bitvavo-oracle-control {health|status|restart|logs|deploy SHA}" >&2
    exit 64
    ;;
esac
CONTROL
chmod 0755 "${CONTROL}"
chown root:root "${CONTROL}"

cat > "${SUDOERS}" <<EOF
Defaults:${DEPLOY_USER} !requiretty
${DEPLOY_USER} ALL=(root) NOPASSWD: ${CONTROL} *
EOF
chmod 0440 "${SUDOERS}"
visudo -cf "${SUDOERS}" >/dev/null

# Make remote recovery persistent in the active firewalld zone. Do this only
# after both rules are present, so a reload cannot silently remove SSH access.
if systemctl is-active --quiet firewalld; then
  ZONE="$(firewall-cmd --get-active-zones | awk 'NR==1{print $1}')"
  ZONE="${ZONE:-$(firewall-cmd --get-default-zone)}"
  firewall-cmd --zone="$ZONE" --permanent --add-service=ssh >/dev/null
  firewall-cmd --zone="$ZONE" --permanent --add-port=8787/tcp >/dev/null
  firewall-cmd --zone="$ZONE" --add-service=ssh >/dev/null || true
  firewall-cmd --zone="$ZONE" --add-port=8787/tcp >/dev/null || true
  firewall-cmd --reload >/dev/null
fi

echo "Restricted Oracle deployment channel installed."
echo "Service: ${SERVICE}"
echo "User: ${DEPLOY_USER}"
echo "Allowed SSH commands: health, status, restart, logs, deploy <40-char-sha>"
echo
echo "Server SSH host key fingerprint (verify this before creating GitHub known_hosts):"
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub || true
