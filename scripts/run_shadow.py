#!/usr/bin/env python3
"""Explicit-scan shadow runner; no imports or writes into active buy delivery."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from research.common import atomic_json, read_json, timestamp, utc
from research.input_contract import digest, code_revision
from research.policies import CANDIDATE, FROZEN_DL1, LEGACY_DATA, identities


def run(journal, scan_id, version):
    if not re.fullmatch(r'[A-Za-z0-9_-]+',scan_id):
        raise ValueError('INVALID_SCAN_ID')
    scan=read_json(journal)
    if scan['scan_id'] != scan_id:
        raise ValueError('SCAN_ID_MISMATCH')
    data_policy=scan.get('data_policy',LEGACY_DATA)
    if not re.fullmatch(r'[A-Z0-9_]+',data_policy):
        raise ValueError('INVALID_DATA_POLICY')
    cutoff=timestamp(scan.get('input_cutoff_at_utc',scan['scan_ts']))
    if version=='v2':
        from research.decision_layer_v2 import decide
        result=decide(scan['observations'],cutoff,scan_id)
        name,root='decision_layer_v2','decision_history_v2'
    else:
        from research.decision_layer import decide
        result=decide(scan['observations'])
        name,root='decision_layer','decision_history_versioned'
    payload={**result,**identities(data_policy=data_policy,decision_policy=result['policy']),
             'scan_id':scan_id,'scan_at_utc':scan['scan_at_utc'],'source_journal':str(journal),
             'source_snapshot_sha256':digest(scan),'code_commit':code_revision(),
             'policy_ready_at':utc(),'stage':scan.get('stage','DEVELOPMENT_REPLAY'),'published_at':None}
    path=Path(root)/data_policy/scan['scan_at_utc'][:10]/(scan_id+'.json.gz')
    if path.exists():
        previous=read_json(path)
        stable=lambda p:{k:v for k,v in p.items() if k not in {'policy_ready_at','code_commit'}}
        if stable(previous)!=stable(payload):
            raise ValueError('SHADOW_JOURNAL_COLLISION')
        payload=previous  # Preserve original readiness; a replay is not a new event.
    else:
        atomic_json(path,payload)
    atomic_json(name+'.json',payload)
    lines=['# '+payload['policy'],'','Scan : '+scan_id,'Données : '+data_policy,'Stage : '+payload['stage'],
           'Toutes les catégories sont shadow. Aucun achat actif autorisé.','']
    for bucket,row in payload['bucket_winners'].items():
        lines.append('- '+bucket+' : '+(row['market'] if row else 'aucun candidat'))
    Path(name+'.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'scan_id':scan_id,'decision_policy':payload['policy'],'journal':str(path),'production_orders_enabled':False}))
    return payload


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--journal',required=True)
    parser.add_argument('--scan-id',required=True)
    parser.add_argument('--version',choices=['v1','v2'],required=True)
    a=parser.parse_args()
    run(a.journal,a.scan_id,a.version)
