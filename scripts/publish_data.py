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
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))

GENERATED = ['bitvavo_live.json', 'scan_feed.txt', 'early_watch.txt', 'early_watch.json', 'scan_history.json',
             'signal_log.json', 'v4_watch.txt', 'v4_watch.json', 'v4_history.json', 'v4_signal_log.json',
             'v4_trend_cache.json', 'v4_watch_raw.txt', 'v4_watch_raw.json', 'v4_stability_state.json',
             'market_control.txt', 'market_control.json', 'market_control_current.json', 'execution_snapshot.json', 'v5_report.json', 'v5_report.md',
             'pipeline_health.json', 'proposed_orders.json', 'alert_candidates.json', 'universe_surveillance.json',
             'decision_layer.json', 'decision_layer.md', 'history_corrected', 'history_legacy_diagnostics', 'policy_state', 'decision_layer_v2.json', 'decision_layer_v2.md',
             'decision_history_v2', 'decision_history_versioned', 'comparison_history', 'replay_history',
             'scan_manifest.json', 'scan_manifests', 'shadow_status.json']
ALERT_STATE = ['alert_state_v4.json', 'security_alert_state.json', 'position_alert_state.enc.json', 'position_monitor_status.json','monitor_availability.json']
EVALUATION_FILES = ['evaluation.json','evaluation_policies','evaluation_history','evaluation_manifest.json',
                    'market_control_history.json','comparison_report.json']
OWNERS = {'prospection':GENERATED,'monitoring':ALERT_STATE,'evaluation':EVALUATION_FILES,
          'publication_receipts':['publication_history'],'attempts':['scan_attempts'],
          'pilot':['prospective_sessions','prospective_observations'],
          'pilot_evaluation':['prospective_report.json','prospective_reports']}
OWNERS.update(quotes=['live_quotes.json','ethfi_live.json','quotes_manifest.json','producer_manifests/quotes'],
              feedback=['feedback_report.json','feedback_state','feedback_history','feedback_manifest.json','producer_manifests/feedback'])
OWNERS.update(oracle_request=['oracle_requested_probe.json'],
              oracle_shadow=['oracle_live_probe.json'])
IMMUTABLE = {'history_corrected','history_legacy_diagnostics','decision_history_v2','decision_history_versioned',
             'comparison_history','replay_history','scan_manifests','evaluation_history','publication_history','scan_attempts',
             'prospective_sessions','prospective_observations','prospective_reports'}
IMMUTABLE.update({'feedback_history','producer_manifests'})


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
                        if name in IMMUTABLE and target.exists() and target.read_bytes() != f.read_bytes():
                            raise RuntimeError('IMMUTABLE_JOURNAL_CONFLICT')
                    shutil.copytree(src, dst, dirs_exist_ok=True)
                else:
                    if Path(name).parts[0] in IMMUTABLE and dst.exists() and src.read_bytes()!=dst.read_bytes():
                        raise RuntimeError('IMMUTABLE_JOURNAL_CONFLICT')
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
            git('add', '--', *paths, cwd=work)
            if git('diff', '--cached', '--quiet', check=False, cwd=work).returncode == 0:
                return
            git('commit', '-m', message, cwd=work)
            changed = git('diff','--name-only','HEAD^','HEAD',cwd=work).stdout.splitlines()
            for attempt in range(4):
                push_started=time.time()
                result = git('push', 'origin', 'HEAD:' + branch, check=False, cwd=work)
                if result.returncode == 0:
                    confirmed=time.time()
                    print('PUBLICATION_OK')
                    return {'commit':git('rev-parse','HEAD',cwd=work).stdout.strip(),
                            'publication_started_at':push_started,'publication_confirmed_at':confirmed}
                git('fetch', 'origin', branch, cwd=work)
                concurrent=git('diff','--name-only','HEAD^','origin/'+branch,'--',*changed,cwd=work).stdout.splitlines()
                if concurrent:
                    raise RuntimeError('CONCURRENT_GENERATED_STATE_CONFLICT')
                rebased = git('rebase', 'origin/' + branch, check=False, cwd=work)
                if rebased.returncode:
                    git('rebase', '--abort', cwd=work)
                    raise RuntimeError('CONCURRENT_GENERATED_STATE_CONFLICT')
            raise RuntimeError('PUBLICATION_RETRIES_EXHAUSTED')
        finally:
            git('worktree', 'remove', '--force', str(work), cwd=source)


def main():
    if '--oracle-request' in sys.argv:
        return publish(OWNERS['oracle_request'],'Record requested Oracle public probe')
    if '--oracle-shadow' in sys.argv:
        return publish(OWNERS['oracle_shadow'],'Record Oracle enriched public probe shadow')
    from research.common import read_json
    from research.input_contract import digest
    from research.publication import file_hash, immutable_json
    for producer in ('quotes','feedback'):
        if '--'+producer in sys.argv:
            from research.optional_publication import validate
            m=validate(producer)
            return publish([*m['outputs'],producer+'_manifest.json',m['archive_path']],
                           'Record verified optional '+producer+' production')
    alerts = '--alerts' in sys.argv
    if alerts:
        return publish(ALERT_STATE,'Persist alert delivery state')
    if '--evaluation' in sys.argv:
        return publish(EVALUATION_FILES,'Record separately evaluated immutable observations')
    if '--attempt' in sys.argv:
        return publish(OWNERS['attempts'],'Record scan attempt availability')
    if '--pilot' in sys.argv:
        return publish(OWNERS['pilot'],'Record technical pilot enrollment without held-out claims')
    manifest=read_json('scan_manifest.json')
    current=read_json('runtime/current_scan.json')
    if not manifest or not current or current['scan_id']!=manifest['scan_id']:
        raise RuntimeError('PREPARED_SCAN_MANIFEST_REQUIRED')
    for name,entry in manifest['outputs'].items():
        if name not in GENERATED and Path(name).parts[0] not in GENERATED:
            raise RuntimeError('OUTPUT_NOT_OWNED_BY_PROSPECTION')
        if file_hash(name)!=entry['sha256']: raise RuntimeError('OUTPUT_CHANGED_AFTER_REPLAY:'+name)
    if read_json(manifest['archive_path'])!=manifest: raise RuntimeError('MANIFEST_ARCHIVE_MISMATCH')
    result=publish([*manifest['outputs'],'scan_manifest.json',manifest['archive_path']],
                   'Record coherent scan, exact replay and isolated shadows')
    if result is None: return
    comparison=read_json('runtime/current_comparison.json',{})
    cycle_path=comparison.get('journal') if (comparison.get('scan_id')==manifest['scan_id']
        and comparison.get('journal') in manifest['outputs']) else None
    cycle=read_json(cycle_path) if cycle_path else None
    receipt={**result,'scan_id':manifest['scan_id'],'data_policy':manifest['data_policy'],
             'manifest_sha256':digest(manifest),'comparison_sha256':digest(cycle) if cycle else None,
             'policy_publication':{'V4':'PUBLISHED',**{k:'PUBLISHED' if manifest['shadow_status'][k]['status']=='OK' else 'FAILED' for k in ('DL1','DL2')}},
             'status':'PUBLISHED','time_semantics':'remote push acknowledged; interval bounds, not an SMTP receipt'}
    receipt_path=Path('publication_history')/Path(current['journal']).parent.name/(current['scan_id']+'.json')
    immutable_json(receipt_path,receipt)
    publish([str(receipt_path)],'Record observed publication confirmation')


if __name__ == '__main__':
    main()
