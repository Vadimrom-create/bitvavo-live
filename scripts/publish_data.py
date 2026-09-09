#!/usr/bin/env python3
"""Publish only generated files, rebasing on concurrent unrelated changes.

Do not force push or blindly overwrite another scanner's newer state. A failed
compare/rebase aborts publication and prevents downstream notifications.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

GENERATED = ['bitvavo_live.json', 'scan_feed.txt', 'early_watch.txt', 'early_watch.json', 'scan_history.json',
             'signal_log.json', 'v4_watch.txt', 'v4_watch.json', 'v4_history.json', 'v4_signal_log.json',
             'v4_trend_cache.json', 'v4_watch_raw.txt', 'v4_watch_raw.json', 'v4_stability_state.json',
             'market_control.txt', 'market_control.json', 'execution_snapshot.json', 'v5_report.json', 'v5_report.md',
             'pipeline_health.json', 'evaluation.json', 'proposed_orders.json', 'alert_candidates.json', 'history',
             'decision_layer.json', 'decision_layer.md', 'decision_history']
ALERT_STATE = ['alert_state_v4.json', 'security_alert_state.json', 'position_alert_state.enc.json', 'position_monitor_status.json']


def git(*args, check=True):
    return subprocess.run(['git', *args], check=check, capture_output=True, text=True)


def main():
    files = ALERT_STATE if '--alerts' in sys.argv else GENERATED
    paths = [p for p in files if Path(p).exists()]
    if not paths:
        return
    git('add', '--', *paths)
    if git('diff', '--cached', '--quiet', check=False).returncode == 0:
        return
    git('commit', '-m', 'Persist alert delivery state' if '--alerts' in sys.argv else 'Record fresh scan and complete V4 measurement journal')
    for attempt in range(4):
        result = git('push', 'origin', 'HEAD:main', check=False)
        if result.returncode == 0:
            print('PUBLICATION_OK')
            return
        git('fetch', 'origin', 'main')
        # Rebase preserves unrelated executor status writes and code edits.
        # Generated-file conflicts are never auto-resolved with ours/theirs.
        rebased = git('rebase', 'origin/main', check=False)
        if rebased.returncode:
            git('rebase', '--abort')
            raise RuntimeError('Concurrent generated-state conflict: scan not published; no email will be sent.')
    raise RuntimeError('Publication failed after bounded retries')


if __name__ == '__main__':
    main()
