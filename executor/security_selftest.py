#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

ENV_FILE = Path('/etc/bitvavo-executor.env')
APP_DIR = Path('/opt/bitvavo-executor')

if os.geteuid() != 0:
    raise SystemExit('Run as root')

if not ENV_FILE.exists():
    raise SystemExit(f'{ENV_FILE} not found')

for raw in ENV_FILE.read_text(encoding='utf-8').splitlines():
    line = raw.strip()
    if not line or line.startswith('#') or '=' not in line:
        continue
    k, v = line.split('=', 1)
    os.environ[k] = v

sys.path.insert(0, str(APP_DIR))
from daemon import Executor  # noqa: E402

ex = Executor()
if not ex.dry_run:
    raise SystemExit('Refusing security self-test because DRY_RUN is false')
if ex.auto_cancel_unknown:
    raise SystemExit('Refusing security self-test because AUTO_CANCEL_UNKNOWN_ORDERS is true')

fake = {
    'event': 'order',
    'market': 'FET-EUR',
    'orderId': 'SECURITY-SELFTEST-NO-REAL-ORDER',
    'clientOrderId': 'unauthorized-selftest',
    'operatorId': 99999999,
    'side': 'buy',
    'orderType': 'limit',
    'status': 'new',
}

ex.handle_account_event(fake)
if not ex.state.get('security_freeze'):
    raise SystemExit('SELFTEST FAILED: security_freeze was not activated')

print('SECURITY_SELFTEST_FREEZE_OK', flush=True)
time.sleep(2)

ex.state['security_freeze'] = False
ex._save_state()
ex.publish_status()
print('SECURITY_SELFTEST_CLEARED_OK', flush=True)
print(json.dumps({'ok': True, 'no_real_order_sent': True, 'auto_cancel_unknown_orders': ex.auto_cancel_unknown}), flush=True)
