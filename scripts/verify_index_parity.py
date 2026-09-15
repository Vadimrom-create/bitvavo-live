#!/usr/bin/env python3
"""Acceptance gate against the pre-lot-11 evaluator/index on real journals."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import types
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from research.common import atomic_json, read_json
from research.history import connect, ingest
from research.evaluation import evaluate
from research.input_contract import digest

REFERENCE='a7c5d6f9281535bc870359f98e0f66f3c1bcf9b1'


def table_hash(db,table):
    sha=hashlib.sha256();count=0
    order={'scans':'id','observations':'scan_id,market','candles':'market,t'}[table]
    for row in db.execute('SELECT * FROM '+table+' ORDER BY '+order):
        sha.update(json.dumps(tuple(row),separators=(',',':'),allow_nan=False).encode()+b'\n');count+=1
    return {'rows':count,'sha256':sha.hexdigest()}


def run(history,output):
    started=time.monotonic();files=sorted(Path(history).glob('*/*.json.gz'))
    source=subprocess.check_output(['git','-C',str(ROOT),'show',REFERENCE+':research/history.py'],text=True)
    old=types.ModuleType('pre_lot11_history');exec(compile(source,'pre_lot11_history.py','exec'),old.__dict__)
    hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    reference=old.rebuild(history,old.connect())
    print('REFERENCE_INDEX_BUILT',len(files),flush=True)
    with tempfile.TemporaryDirectory(prefix='lot11-parity-') as directory:
        dbpath=Path(directory)/'incremental.sqlite3';incremental=connect(dbpath);full=connect()
        for i,p in enumerate(files):
            if i==len(files)//2:
                incremental.close();incremental=connect(dbpath)
            ingest(incremental,read_json(p),hashes[str(p)])
        print('INCREMENTAL_RESTART_INDEX_BUILT',flush=True)
        for p in reversed(files): ingest(full,read_json(p),hashes[str(p)])
        tables={}
        for table in ('scans','observations','candles'):
            values=[table_hash(db,table) for db in (reference,incremental,full)]
            if values[0]!=values[1] or values[0]!=values[2]: raise AssertionError('INDEX_PARITY_FAILED:'+table)
            tables[table]=values[0]
        print('ALL_REAL_TABLES_EQUAL',json.dumps(tables),flush=True)
        reference_metrics=evaluate(reference)
        print('REFERENCE_METRICS_EVALUATED',flush=True)
        actual=evaluate(incremental)
        if reference_metrics!=actual: raise AssertionError('EVALUATION_PARITY_FAILED')
        # Full/reversed tables are identical; also run the evaluator to detect order-sensitive queries.
        if evaluate(full)!=actual: raise AssertionError('REVERSED_EVALUATION_PARITY_FAILED')
        for p in files:
            if hashlib.sha256(p.read_bytes()).hexdigest()!=hashes[str(p)]: raise AssertionError('SOURCE_CHANGED')
        report={'reference_commit':REFERENCE,'journals':len(files),'source_manifest_sha256':digest(hashes),
                'tables':tables,'incremental_restart_equals_full_reverse_equals_reference':True,
                'evaluation_outputs_equal':True,'evaluation_sha256':digest(actual),'historical_sources_unchanged':True,
                'duration_seconds':time.monotonic()-started,'scope':'REPRODUCIBILITY_NOT_PERFORMANCE_VALIDATION'}
        atomic_json(output,report);print(json.dumps(report),flush=True)
        incremental.close();full.close();reference.close()
        return report


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--history',default='history');p.add_argument('--output',required=True)
    args=p.parse_args();run(args.history,args.output)
