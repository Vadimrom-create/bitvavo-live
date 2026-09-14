#!/usr/bin/env python3
"""Seal the explicit scan after an exact replay, tolerating optional shadow failure."""
from pathlib import Path
import shutil
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from research.common import atomic_json, read_json
from research.input_contract import digest
from research.publication import build_manifest, file_hash, immutable_json

PUBLIC_FILES=['bitvavo_live.json','scan_feed.txt','early_watch.txt','early_watch.json','v4_watch.txt','v4_watch.json',
              'v4_watch_raw.txt','v4_watch_raw.json','market_control.txt','market_control.json','market_control_current.json',
              'execution_snapshot.json','v5_report.json','v5_report.md','pipeline_health.json','proposed_orders.json','alert_candidates.json']


def run():
    from research.replay import compare
    current=read_json('runtime/current_scan.json')
    scan=read_json(current['journal'])
    if scan['scan_id']!=current['scan_id']: raise ValueError('SCAN_ID_MISMATCH')
    replay_source=Path('runtime')/('replay-'+scan['scan_id']+'.json.gz')
    replay=compare(replay_source)
    files=[*PUBLIC_FILES,current['journal']]
    status={}
    for name,filename in [('DL1','decision_layer'),('DL2','decision_layer_v2')]:
        journal_root='decision_history_versioned' if name=='DL1' else 'decision_history_v2'
        journal_path=Path(journal_root)/scan['data_policy']/scan['scan_at_utc'][:10]/(scan['scan_id']+'.json.gz')
        try:
            payload=read_json(filename+'.json',{})
            valid=(payload.get('scan_id')==scan['scan_id'] and payload.get('source_snapshot_sha256')==digest(scan)
                   and payload.get('data_policy')==scan['data_policy'])
            valid=valid and read_json(journal_path)==payload and ('Scan : '+scan['scan_id']) in Path(filename+'.md').read_text()
        except (ValueError,OSError,EOFError):
            valid=False
        status[name]={'status':'OK' if valid else 'FAILED_OR_MISSING','policy_ready_at':payload.get('policy_ready_at') if valid else None}
        if valid:
            files.extend([filename+'.json',filename+'.md',str(journal_path)])
    status['COMPARISON']={'status':'FAILED_OR_MISSING'}
    try:
        comparison=read_json('runtime/current_comparison.json',{})
        if comparison.get('scan_id')==scan['scan_id'] and read_json(comparison['journal'])['source_snapshot_sha256']==digest(scan):
            files.append(comparison['journal'])
            status['COMPARISON']={'status':'OK'}
    except (ValueError,OSError,EOFError,KeyError,TypeError):
        pass
    atomic_json('shadow_status.json',{'scan_id':scan['scan_id'],'policies':status})
    files.append('shadow_status.json')
    target=Path('replay_history')/scan['scan_at_utc'][:10]/(scan['scan_id']+'.json.gz')
    target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists() and file_hash(target)!=file_hash(replay_source): raise ValueError('REPLAY_JOURNAL_COLLISION')
    if not target.exists(): shutil.copy2(replay_source,target)
    files.append(str(target))
    # Bind only the state written by this data policy, never stale files from a code checkout.
    if scan['data_policy']=='LEGACY_V4_CORRECTED_DIAGNOSTICS_V1':
        files.extend(n for n in ('scan_history.json','signal_log.json','v4_history.json','v4_signal_log.json',
                                'v4_trend_cache.json','v4_stability_state.json') if Path(n).exists())
    state_root=Path('policy_state')/scan['data_policy']
    files.extend(str(p) for p in sorted(state_root.rglob('*.json')))
    manifest=build_manifest(scan,replay,files)
    manifest['shadow_status']=status
    manifest['archive_path']=str(Path('scan_manifests')/scan['scan_at_utc'][:10]/(scan['scan_id']+'.json'))
    immutable_json(manifest['archive_path'],manifest)
    atomic_json('scan_manifest.json',manifest)
    return manifest


if __name__=='__main__': run()
