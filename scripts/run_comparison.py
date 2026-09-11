#!/usr/bin/env python3
"""Capture an explicit cycle before publication; outcomes are evaluated elsewhere."""
import argparse
import time
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from research.common import atomic_json, read_json
from research.comparison import build_cycle, attach_plans


def run(journal,scan_id):
    scan=read_json(journal)
    if scan['scan_id']!=scan_id: raise ValueError('SCAN_ID_MISMATCH')
    path=Path('comparison_history')/scan['data_policy']/scan['scan_at_utc'][:10]/(scan_id+'.json.gz')
    if path.exists():
        previous=read_json(path)
        from research.input_contract import digest
        if previous['source_snapshot_sha256']!=digest(scan): raise ValueError('COMPARISON_COLLISION')
        return previous
    results={}
    for name,file in [('DL1','decision_layer.json'),('DL2','decision_layer_v2.json')]:
        p=read_json(file,{})
        if p.get('scan_id')==scan_id and p.get('data_policy')==scan['data_policy']: results[name]=p
    cycle=attach_plans(build_cycle(scan,results),scan,time.time())
    atomic_json(path,cycle)
    atomic_json('runtime/current_comparison.json',{'scan_id':scan_id,'journal':str(path)})
    return cycle


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--journal',required=True);p.add_argument('--scan-id',required=True)
    a=p.parse_args();run(a.journal,a.scan_id)
