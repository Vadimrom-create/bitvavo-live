#!/usr/bin/env python3
"""Append a public workflow outcome even when a scan never became publishable."""
import os
from pathlib import Path
import re
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from research.common import utc, read_json
from research.input_contract import code_revision
from research.publication import immutable_json


def run():
    run_id=os.environ['GITHUB_RUN_ID'];attempt=os.getenv('GITHUB_RUN_ATTEMPT','1')
    if not re.fullmatch(r'\d+',run_id+attempt): raise ValueError('INVALID_RUN_ID')
    current=read_json('runtime/current_scan.json',{})
    payload={'workflow_run_id':run_id,'attempt':attempt,'code_commit':code_revision(),'observed_at':utc(),
             'scan_id':current.get('scan_id'),'data_policy':current.get('data_policy'),
             'steps':{k:os.getenv('OUTCOME_'+k,'unknown') for k in ('SCAN','V1','V2','COMPARISON','REPLAY','PUBLICATION','PILOT','PILOT_RECORD')},
             'source':'GITHUB_ACTIONS_OBSERVATION','private_data':False}
    immutable_json(Path('scan_attempts')/(run_id+'-'+attempt+'.json'),payload)
    return payload


if __name__=='__main__': run()
