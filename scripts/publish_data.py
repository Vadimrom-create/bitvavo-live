#!/usr/bin/env python3
"""Publish only generated files, rebasing on concurrent unrelated changes.

Do not force push or blindly overwrite another scanner's newer state. A failed
compare/rebase aborts publication and prevents downstream notifications.
"""
from __future__ import annotations

import os
import shutil
import tempfile
import subprocess
import sys
from pathlib import Path

GENERATED = ['bitvavo_live.json', 'scan_feed.txt', 'early_watch.txt', 'early_watch.json', 'scan_history.json',
             'signal_log.json', 'v4_watch.txt', 'v4_watch.json', 'v4_history.json', 'v4_signal_log.json',
             'v4_trend_cache.json', 'v4_watch_raw.txt', 'v4_watch_raw.json', 'v4_stability_state.json',
             'market_control.txt', 'market_control.json', 'market_control_current.json', 'market_control_history.json', 'execution_snapshot.json', 'v5_report.json', 'v5_report.md',
             'pipeline_health.json', 'evaluation.json', 'proposed_orders.json', 'alert_candidates.json', 'history',
             'decision_layer.json', 'decision_layer.md', 'decision_history', 'history_corrected', 'history_legacy_diagnostics', 'policy_state']
ALERT_STATE = ['alert_state_v4.json', 'security_alert_state.json', 'position_alert_state.enc.json', 'position_monitor_status.json']


def git(*args, check=True, cwd=None):
    return subprocess.run(['git', *args], cwd=cwd, check=check, capture_output=True, text=True)


def publish(files, message, source=None, base_sha=None, branch='main'):
    source = Path(source or Path.cwd()).resolve()
    paths = [p for p in files if (source / p).exists()]
    if not paths:
        return
    base_sha = base_sha or os.getenv('PUBLISH_BASE_SHA') or git('rev-parse', 'HEAD', cwd=source).stdout.strip()
    with tempfile.TemporaryDirectory(prefix='bitvavo-publication-') as directory:
        work = Path(directory) / 'checkout'
        git('worktree', 'add', '--detach', str(work), base_sha, cwd=source)
        try:
            for name in paths:
                src, dst = source / name, work / name
                if src.is_dir():
                    for f in src.rglob('*'):
                        if not f.is_file():
                            continue
                        target = dst / f.relative_to(src)
                        if name in {'history', 'history_corrected', 'history_legacy_diagnostics', 'decision_history'} and target.exists() and target.read_bytes() != f.read_bytes():
                            raise RuntimeError('IMMUTABLE_JOURNAL_CONFLICT')
                    shutil.copytree(src, dst, dirs_exist_ok=True)
                else:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
            git('add', '--', *paths, cwd=work)
            if git('diff', '--cached', '--quiet', check=False, cwd=work).returncode == 0:
                return
            git('commit', '-m', message, cwd=work)
            for attempt in range(4):
                result = git('push', 'origin', 'HEAD:' + branch, check=False, cwd=work)
                if result.returncode == 0:
                    print('PUBLICATION_OK')
                    return
                git('fetch', 'origin', branch, cwd=work)
                rebased = git('rebase', 'origin/' + branch, check=False, cwd=work)
                if rebased.returncode:
                    git('rebase', '--abort', cwd=work)
                    raise RuntimeError('CONCURRENT_GENERATED_STATE_CONFLICT')
            raise RuntimeError('PUBLICATION_RETRIES_EXHAUSTED')
        finally:
            git('worktree', 'remove', '--force', str(work), cwd=source)


def main():
    alerts = '--alerts' in sys.argv
    publish(ALERT_STATE if alerts else GENERATED,
            'Persist alert delivery state' if alerts else 'Record fresh scan and complete V4 measurement journal')


if __name__ == '__main__':
    main()
