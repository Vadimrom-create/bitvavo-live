#!/usr/bin/env python3
"""Separate disposable indexing and historical reports, with immutable inputs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from research.common import atomic_json, read_json, timestamp, utc
from research.evaluation import evaluate, market_control, HISTORY_POLICY
from research.history import open_index
from research.input_contract import digest, code_revision
from research.policies import LEGACY_DATA, LEGACY_DIAGNOSTICS, CORRECTED_DATA, identities
from research.publication import file_hash, immutable_json, apply_receipt

HISTORY_ROOTS={LEGACY_DATA:'history',LEGACY_DIAGNOSTICS:'history_legacy_diagnostics',CORRECTED_DATA:'history_corrected'}


def run(root='.',now=None):
    root=Path(root).resolve();now=time.time() if now is None else now
    started=time.monotonic();policies={};source_manifests={};latest_control=None
    attempts=[read_json(p) for p in sorted((root/'scan_attempts').glob('*.json'))]
    for policy,directory in HISTORY_ROOTS.items():
        journals=sorted((root/directory).glob('*/*.json.gz'))
        if not journals: continue
        db=open_index(root/'runtime/evaluation_index'/f'{policy}.sqlite3',root/directory)
        try:
            manifest=[dict(r) for r in db.execute('SELECT id,sha256,bytes_sha256 FROM journal_integrity ORDER BY id')]
            source_manifests[policy]=manifest
            scan_times=[r[0] for r in db.execute('SELECT ts FROM scans ORDER BY ts,id')]
            intervals=[b-a for a,b in zip(scan_times,scan_times[1:])]
            gaps=[{'start':a,'end':b,'seconds':b-a,'status':'NO_RECORDED_SCAN_BETWEEN_ENDPOINTS',
                   'missed_event_outcomes':'UNKNOWN'} for a,b in zip(scan_times,scan_times[1:]) if b-a>300]
            metrics=evaluate(db)  # Exact existing evaluator; no changed thresholds or outcome rules.
            last=max((read_json(p) for p in journals[-3:]),key=lambda s:(s['scan_ts'],s['scan_id']))
            control={'scan_id':last['scan_id'],'data_policy':policy,'evaluation_policy':HISTORY_POLICY,
                     'scope':'COMPLETE_OBSERVATION_JOURNAL','markets':market_control(db,last['observations'],
                         timestamp(last.get('input_cutoff_at_utc',last['scan_ts'])))}
            cycles=[]
            for path in sorted((root/'comparison_history'/policy).glob('*/*.json.gz')):
                cycle=read_json(path)
                match=db.execute('SELECT sha256 FROM journal_integrity WHERE id=?',(cycle['scan_id'],)).fetchone()
                if not match or match[0]!=cycle['source_snapshot_sha256']: raise ValueError('COMPARISON_SOURCE_MISMATCH')
                receipt_path=root/'publication_history'/path.parent.name/(cycle['scan_id']+'.json')
                if receipt_path.exists(): cycle=apply_receipt(cycle,read_json(receipt_path))
                cycles.append(cycle)
            comparison={'status':'NO_RECORDED_COMPARISON_CYCLES'}
            if cycles:
                from research.comparison import labels_from_db, evaluate_pairs, evaluate_portfolios
                comparison=evaluate_pairs(cycles,labels_from_db(cycles,db,now),missing_windows=gaps)
                comparison['portfolios']=evaluate_portfolios(cycles,db,now)
            policies[policy]={**identities(data_policy=policy),'historical_evaluation_policy':HISTORY_POLICY,
                'source_manifest_sha256':digest(manifest),'source_scan_count':len(manifest),'latest_scan_id':last['scan_id'],
                'metrics':metrics,'comparison':comparison,'market_control_history':control,'stage':'DEVELOPMENT_ONLY'}
            policies[policy]['scan_cadence']={'intervals_seconds':intervals,'nominal_seconds':300,
                'longest_interval_seconds':max(intervals,default=None),'gaps':gaps,
                'scope':'recorded scans; not successful private position monitoring'}
            atomic_json(root/'evaluation_policies'/f'{policy}.json',policies[policy])
            latest_control=control
        finally:
            db.close()
    report={'schema_version':1,'producer':'evaluation','code_commit':code_revision(),'generated_at':utc(now),
            'policies':policies,'source_manifests':source_manifests,'stage':'DEVELOPMENT_ONLY',
            'recorded_attempts':attempts,'attempts_without_scan':sum(not a.get('scan_id') for a in attempts),
            'superiority_demonstrated':False,'held_out_performed':False}
    evaluation_id=digest(report)
    immutable_json(root/'evaluation_history'/(evaluation_id+'.json.gz'),report)
    selected=next((policies[p] for p in (CORRECTED_DATA,LEGACY_DIAGNOSTICS,LEGACY_DATA) if p in policies),None)
    atomic_json(root/'evaluation.json',{**(selected['metrics'] if selected else {}),**(selected or {'status':'NO_SCANS'}),
                                     'evaluation_id':evaluation_id,'generated_at':utc(now),'code_commit':report['code_commit']})
    atomic_json(root/'comparison_report.json',{'evaluation_id':evaluation_id,'generated_at':utc(now),
                'policies':{p:r['comparison'] for p,r in policies.items()},'stage':'DEVELOPMENT_ONLY'})
    if latest_control is not None: atomic_json(root/'market_control_history.json',latest_control)
    outputs=['evaluation.json','comparison_report.json']+(['market_control_history.json'] if latest_control is not None else [])
    atomic_json(root/'evaluation_manifest.json',{'producer':'evaluation','evaluation_id':evaluation_id,
        'code_commit':report['code_commit'],'generated_at':utc(now),'source_manifests':source_manifests,
        'attempt_manifest_sha256':digest(attempts),
        'outputs':{n:file_hash(root/n) for n in outputs},'index_bytes':sum(p.stat().st_size for p in (root/'runtime/evaluation_index').glob('*.sqlite3')),
        'duration_seconds':time.monotonic()-started,'cache_role':'DISPOSABLE_REBUILDABLE_NO_SOURCE_REWRITE'})
    print(json.dumps({'evaluation_id':evaluation_id,'policies':list(policies),'held_out_performed':False}))
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--root',default='.')
    args=parser.parse_args();run(args.root)
