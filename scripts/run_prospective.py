#!/usr/bin/env python3
"""Optional pilot enrollment/reporting and manual, future-only protocol freeze."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from research.common import atomic_json, read_json, timestamp
from research.input_contract import digest
from research.publication import immutable_json, apply_receipt, file_hash
from research.prospective import (code_identity, public_bootstrap, validate_enrollment, sizing_metrics,
                                 validate_protocol, PILOT_POLICY, MAX_HORIZON, BLOCK_SCENARIOS)
from research.comparison import SPEC, POLICIES, labels_from_db
from research.policies import CORRECTED_DATA, identities
from research.risk import DEFAULTS


def source_path(root, relative, allowed):
    p=Path(relative)
    if p.is_absolute() or '..' in p.parts or not p.parts or p.parts[0] not in allowed:
        raise ValueError('UNEXPECTED_PROSPECTIVE_SOURCE')
    resolved=(root/p).resolve()
    if not resolved.is_relative_to(root.resolve()): raise ValueError('SOURCE_OUTSIDE_ROOT')
    return root/p


def start(root='.', now=None):
    root=Path(root).resolve();now=time.time() if now is None else timestamp(now)
    code=code_identity(root)
    sid=digest([PILOT_POLICY,code['fingerprint'],CORRECTED_DATA])
    path=root/'prospective_sessions'/(sid+'.json.gz')
    session=read_json(path)
    if session is None:
        bootstrap=public_bootstrap(root)
        session={'schema_version':1,'session_id':sid,'started_at':now,'code_fingerprint':code['fingerprint'],
                 'code':code,**identities(),'decision_policies':POLICIES,'comparison_spec':SPEC,
                 'execution_assumptions':DEFAULTS,'bootstrap':bootstrap,'bootstrap_sha256':digest(bootstrap),
                 'instrumentation_policy':PILOT_POLICY,'stage':'TECHNICAL_PILOT_DEVELOPMENT_ONLY',
                 'held_out_performed':False,'private_validation':'PENDING PRIVATE CONFIGURATION'}
        immutable_json(path,session)
    if (session['code_fingerprint']!=code['fingerprint'] or session['session_id']!=sid or session['started_at']>now
        or digest(session['bootstrap'])!=session['bootstrap_sha256']):
        raise ValueError('INVALID_PILOT_SESSION')
    atomic_json(root/'runtime/current_pilot.json',{'session_id':sid,'session_sha256':digest(session)})
    return session


def record(root='.',now=None):
    root=Path(root).resolve();now=time.time() if now is None else timestamp(now)
    pointer=read_json(root/'runtime/current_pilot.json')
    session=read_json(root/'prospective_sessions'/(pointer['session_id']+'.json.gz'))
    if digest(session)!=pointer['session_sha256']: raise ValueError('PILOT_SESSION_CHANGED')
    current=read_json(root/'runtime/current_scan.json')
    path=source_path(root,current['journal'],{'history_corrected'})
    scan=read_json(path)
    if scan['scan_id']!=current['scan_id']: raise ValueError('SCAN_ID_MISMATCH')
    validate_enrollment(session,scan,code_identity(root),now)
    comparison=read_json(root/'runtime/current_comparison.json',{})
    comparison_source=None
    if comparison.get('scan_id')==scan['scan_id']:
        p=source_path(root,comparison['journal'],{'comparison_history'})
        value=read_json(p)
        if value['source_snapshot_sha256']!=digest(scan): raise ValueError('COMPARISON_SOURCE_MISMATCH')
        comparison_source={'path':str(p.relative_to(root)),'sha256':file_hash(p)}
    value={'schema_version':1,'session_id':session['session_id'],'session_sha256':digest(session),
           'scan_id':scan['scan_id'],'scan_ts':scan['scan_ts'],'cutoff':timestamp(scan['input_cutoff_at_utc']),
           'code_commit':scan['code_commit'],'data_policy':scan['data_policy'],'source_snapshot_sha256':digest(scan),
           'journal':str(path.relative_to(root)),'journal_sha256':file_hash(path),
           'comparison':comparison_source,'enrolled_at':now,'stage':'TECHNICAL_PILOT_DEVELOPMENT_ONLY'}
    dest=root/'prospective_observations'/session['session_id']/(scan['scan_id']+'.json')
    previous=read_json(dest)
    if previous is not None:
        if {k:v for k,v in previous.items() if k!='enrolled_at'}!={k:v for k,v in value.items() if k!='enrolled_at'}:
            raise ValueError('PILOT_ENROLLMENT_COLLISION')
        return previous
    immutable_json(dest,value)
    return value


def report(root='.',now=None):
    root=Path(root).resolve();now=time.time() if now is None else timestamp(now)
    from research.history import open_index
    groups={};sources={};evaluator=code_identity(root)
    sessions=sorted((root/'prospective_sessions').glob('*.json.gz'))
    for path in sessions:
        session=read_json(path);sid=session['session_id']
        if path.stem!=sid+'.json': raise ValueError('SESSION_FILENAME_MISMATCH')
        if session['started_at']>now: raise ValueError('SESSION_FROM_FUTURE')
        entries=[read_json(p) for p in sorted((root/'prospective_observations'/sid).glob('*.json'))]
        if session['code_fingerprint']!=evaluator['fingerprint'] or session['comparison_spec']!=SPEC:
            groups[sid]={'status':'REQUIRES_ORIGINAL_EVALUATOR','held_out_performed':False}
            continue
        cycles=[];scans=[];last=None;unavailable=[];source_hashes={str(path.relative_to(root)):file_hash(path)}
        for e in entries:
            if e['session_sha256']!=digest(session) or e['session_id']!=sid: raise ValueError('SESSION_CHANGED')
            if not session['started_at']<=e['scan_ts']<=e['cutoff']<=e['enrolled_at']<=now:
                raise ValueError('ENROLLMENT_FROM_FUTURE_OR_PAST')
            last=max(last or e['cutoff'],e['cutoff'])
            ep=root/'prospective_observations'/sid/(e['scan_id']+'.json')
            source_hashes[str(ep.relative_to(root))]=file_hash(ep)
            p=source_path(root,e['journal'],{'history_corrected'})
            if not p.exists():
                unavailable.append({'scan_id':e['scan_id'],'reason':'SOURCE_NOT_PUBLISHED','outcomes':'UNKNOWN'})
                continue
            if file_hash(p)!=e['journal_sha256']: raise ValueError('PILOT_JOURNAL_CHANGED')
            scan=read_json(p)
            if digest(scan)!=e['source_snapshot_sha256']: raise ValueError('SOURCE_SNAPSHOT_CHANGED')
            validate_enrollment(session,scan,{'fingerprint':session['code_fingerprint'],'commit':e['code_commit']},now)
            if scan['scan_id']!=e['scan_id']: raise ValueError('SCAN_ID_MISMATCH')
            if timestamp(scan['input_cutoff_at_utc'])!=e['cutoff'] or scan['scan_ts']!=e['scan_ts']:
                raise ValueError('ENROLLMENT_TIMESTAMP_CHANGED')
            scans.append(scan)
            source_hashes[e['journal']]=e['journal_sha256']
            if e['comparison'] is None: continue
            cp=source_path(root,e['comparison']['path'],{'comparison_history'})
            if not cp.exists():
                unavailable.append({'scan_id':e['scan_id'],'reason':'COMPARISON_NOT_PUBLISHED','outcomes':'UNKNOWN'})
                continue
            if file_hash(cp)!=e['comparison']['sha256']: raise ValueError('COMPARISON_CHANGED')
            c=read_json(cp)
            if (c['source_snapshot_sha256']!=digest(scan) or c['scan_id']!=scan['scan_id'] or
                c['spec']!=session['comparison_spec'] or c['data_policy']!=session['data_policy']):
                raise ValueError('COMPARISON_CONTRACT_CHANGED')
            source_hashes[str(cp.relative_to(root))]=file_hash(cp)
            receipt=root/'publication_history'/Path(e['journal']).parent.name/(e['scan_id']+'.json')
            if receipt.exists():
                r=read_json(receipt)
                if timestamp(r['publication_confirmed_at'])>now: raise ValueError('RECEIPT_FROM_FUTURE')
                c=apply_receipt(c,r);source_hashes[str(receipt.relative_to(root))]=file_hash(receipt)
            cycles.append(c)
        labels={};outcome_sources=[]
        if cycles:
            db=open_index(root/'runtime/prospective_index'/f'{sid}.sqlite3',root/'history_corrected')
            try:
                if db.execute('SELECT MAX(ts) FROM scans').fetchone()[0]>now: raise ValueError('OUTCOME_INDEX_FROM_FUTURE')
                labels=labels_from_db(cycles,db,now)
                outcome_sources=[dict(r) for r in db.execute('SELECT id,sha256,bytes_sha256 FROM journal_integrity ORDER BY id')]
            finally: db.close()
        metrics=sizing_metrics(cycles,labels,session['started_at'],now)
        times=sorted({timestamp(s['scan_ts']) for s in scans})
        intervals=[b-a for a,b in zip(times,times[1:])]
        missing=Counter()
        for s in scans:
            for o in s['observations']:
                for capability,details in (o.get('quality_v2',{}).get('capabilities',{})).items():
                    if not details.get('available'): missing[capability]+=1
        groups[sid]={'session_id':sid,'code_fingerprint':session['code_fingerprint'],
            'started_at':session['started_at'],'last_development_cutoff':last,'enrolled_scan_count':len(entries),
            'missing_comparison_scans':len(entries)-len(cycles),'unavailable_sources':unavailable,
            'comparison_coverage':len(cycles)/len(entries) if entries else None,
            'population_observations':sum(len(s['observations']) for s in scans),
            'unavailable_capability_observations':dict(missing),
            'scan_intervals_seconds':intervals,'seconds_since_last_scan':now-times[-1] if times else None,
            'no_scan_window_outcomes':'UNKNOWN','metrics_population':'ENROLLED_SCANS_WITH_RECORDED_COMPARISON; missing scans listed separately',
            'metrics':metrics,'source_hashes':source_hashes,'outcome_sources':outcome_sources,
            'status':'ACCUMULATING_DEVELOPMENT' if entries else 'NO_PROSPECTIVE_OBSERVATIONS'}
        groups[sid]['availability_samples']=[{'scan_id':c['scan_id'],
            'policies':{name:{'status':value['status'],
                'ready_delay_seconds':value['native']['policy_ready_at']-c['cutoff'] if value['native'].get('policy_ready_at') is not None else None,
                'publication_delay_seconds':value['native']['published_at']-c['cutoff'] if value['native'].get('published_at') is not None else None,
                'publication_status':value['native']['publication_status']} for name,value in c['policies'].items()}} for c in cycles]
        sources[sid]=digest([source_hashes,outcome_sources])
    result={'schema_version':1,'instrumentation_policy':PILOT_POLICY,'generated_at':now,
            'evaluator_code':evaluator,'sessions':groups,'source_manifests':sources,
            'held_out_performed':False,'superiority_demonstrated':False,'promotion_allowed':False,
            'status':'NO_PILOT_STARTED' if not sessions else 'TECHNICAL_PILOT_DEVELOPMENT_ONLY',
            'private_validation':'PENDING PRIVATE CONFIGURATION'}
    rid=digest(result)
    immutable_json(root/'prospective_reports'/(rid+'.json.gz'),result)
    atomic_json(root/'prospective_report.json',{'report_id':rid,**result})
    return result


def report_and_publish(root='.',now=None):
    """Publish only the report produced successfully by this invocation."""
    from scripts.publish_data import publish
    result=report(root,now)
    rid=digest(result)
    archive='prospective_reports/'+rid+'.json.gz'
    if (read_json(Path(root)/archive)!=result or
            read_json(Path(root)/'prospective_report.json')!={'report_id':rid,**result}):
        raise ValueError('CURRENT_PILOT_REPORT_MISMATCH')
    publish(['prospective_report.json',archive],
            'Record current technical pilot report without held-out claims',source=root)
    return result


def freeze(protocol_path,report_path,root='.',now=None):
    """Prepare a future manifest only. Never start held-out collection or promote."""
    root=Path(root).resolve();now=time.time() if now is None else timestamp(now)
    p=read_json(protocol_path);evidence=read_json(report_path)
    if not evidence or 'report_id' in evidence: raise ValueError('IMMUTABLE_PILOT_REPORT_REQUIRED')
    sid=p.get('session_id');group=evidence.get('sessions',{}).get(sid)
    if not group or not group.get('enrolled_scan_count') or group.get('last_development_cutoff') is None:
        raise ValueError('ACTUAL_PROSPECTIVE_PILOT_REQUIRED')
    metric=group['metrics']['contrasts'].get(p.get('primary_contrast'),{})
    if metric.get('sample_variance') is None: raise ValueError('PAIRED_VARIANCE_NOT_ESTIMABLE')
    if evidence['generated_at']>now: raise ValueError('PILOT_REPORT_FROM_FUTURE')
    code=code_identity(root)
    if code['fingerprint']!=group['code_fingerprint'] or code['fingerprint']!=evidence['evaluator_code']['fingerprint']:
        raise ValueError('PILOT_CODE_DIFFERS_FROM_CANDIDATE')
    if read_json(root/'prospective_reports'/(digest(evidence)+'.json.gz'))!=evidence:
        raise ValueError('PILOT_REPORT_NOT_ARCHIVED')
    for name,sha in group['source_hashes'].items():
        source=source_path(root,name,{'prospective_sessions','prospective_observations','history_corrected','comparison_history','publication_history'})
        if file_hash(source)!=sha: raise ValueError('PILOT_EVIDENCE_CHANGED')
    current_entries={str(path.relative_to(root)) for path in (root/'prospective_observations'/sid).glob('*.json')}
    recorded_entries={name for name in group['source_hashes'] if name.startswith('prospective_observations/')}
    if current_entries!=recorded_entries: raise ValueError('PILOT_REPORT_STALE')
    validate_protocol(p,now,group['last_development_cutoff'],digest(evidence))
    # Freeze all inputs, including exact public bootstrap; no private state is exported.
    bootstrap=public_bootstrap(root)
    value={'schema_version':1,'frozen_at':now,'code':code,'code_fingerprint':code['fingerprint'],
           **identities(),'decision_policies':POLICIES,'comparison_spec':SPEC,'execution_assumptions':DEFAULTS,
           'protocol':p,'pilot_report_sha256':digest(evidence),'bootstrap':bootstrap,'bootstrap_sha256':digest(bootstrap),
           'validation_start':timestamp(p['validation_start']),
           'analysis_at':timestamp(p['validation_start'])+p['planned_days']*86400,
           'embargo_seconds':p['embargo_seconds'],'last_development_cutoff':group['last_development_cutoff'],
           'stage':'FROZEN_PROTOCOL_NOT_ACTIVATED','held_out_performed':False,'promotion_allowed':False,
           'private_validation':'PENDING PRIVATE CONFIGURATION'}
    immutable_json(root/'prospective_freezes'/(digest(value)+'.json.gz'),value)
    return value


def main():
    p=argparse.ArgumentParser();p.add_argument('action',choices=['start','record','report','freeze'])
    p.add_argument('--root',default='.');p.add_argument('--protocol');p.add_argument('--pilot-report')
    p.add_argument('--publish',action='store_true',help='Publish only a successfully generated current report')
    a=p.parse_args()
    if a.publish and a.action!='report': p.error('--publish requires report')
    if a.action=='freeze':
        if not a.protocol or not a.pilot_report: p.error('freeze requires --protocol and --pilot-report')
        result=freeze(a.protocol,a.pilot_report,a.root)
    elif a.action=='report' and a.publish: result=report_and_publish(a.root)
    else: result=globals()[a.action](a.root)
    print(json.dumps({'action':a.action,'status':result.get('status',result.get('stage')),
                      'held_out_performed':False,'promotion_allowed':False}))


if __name__=='__main__':main()
