"""Coherent public bundles and observed publication receipts; no order route."""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import re
from research.common import read_json, timestamp, freshness, atomic_json
from research.input_contract import digest
from research.policies import FROZEN_V4


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def immutable_json(path, value):
    path=Path(path)
    if path.exists():
        if read_json(path)!=value: raise ValueError('IMMUTABLE_ARTIFACT_COLLISION')
    else:
        atomic_json(path,value)


def build_manifest(scan, replay, files, root='.'):
    root=Path(root)
    if not all(replay.get(k) is True for k in ('reference_equals_instrumented','reference_equals_recorded_live')):
        raise ValueError('EXACT_REPLAY_REQUIRED')
    if read_json(root/'v4_watch.json')!=scan['baseline_output']:
        raise ValueError('BASELINE_OUTPUT_MISMATCH')
    if not re.fullmatch('[0-9a-f]{40}',scan['code_commit']): raise ValueError('CODE_REVISION_REQUIRED')
    outputs={}
    for name in files:
        if Path(name).is_absolute() or '..' in Path(name).parts: raise ValueError('INVALID_OUTPUT_PATH')
        p=root/name
        if not p.is_file(): raise ValueError('OUTPUT_MISSING:'+name)
        outputs[name]={'sha256':file_hash(p),'bytes':p.stat().st_size}
        if name.endswith(('.json','.json.gz')):
            payload=read_json(p)
            outputs[name]['payload_sha256']=digest(payload)
    return {'schema_version':1,'producer':'prospection','scan_id':scan['scan_id'],
            **{k:scan[k] for k in ('data_policy','decision_policy','execution_policy','evaluation_policy','code_commit')},
            'source_snapshot_sha256':digest(scan),'input_cutoff_at_utc':scan['input_cutoff_at_utc'],
            'policy_ready_at':scan['policy_ready_at'],'replay':replay,'outputs':outputs,
            'health':scan.get('health',{}).get('status','UNKNOWN'),
            'publication_status':'AWAITING_OBSERVED_RECEIPT','published_at':None,
            'stage':scan.get('stage','DEVELOPMENT_REPLAY')}


def validate_buy_bundle(payload, manifest, now, root='.'):
    try:
        if manifest.get('schema_version')!=1 or manifest.get('producer')!='prospection': raise ValueError('MANIFEST_REQUIRED')
        if manifest.get('health')!='OK': raise ValueError('PIPELINE_NOT_USABLE')
        if manifest['decision_policy']!=FROZEN_V4 or payload['decision_policy']!=FROZEN_V4: raise ValueError('NON_V4_POLICY')
        for k in ('scan_id','data_policy'):
            if not payload.get(k) or payload[k]!=manifest[k]: raise ValueError('SNAPSHOT_MISMATCH')
        for k in ('execution_policy','evaluation_policy','code_commit'):
            if not manifest.get(k): raise ValueError('INCOMPLETE_POLICY_IDENTITY')
        if not all(manifest['replay'].get(k) is True for k in ('reference_equals_instrumented','reference_equals_recorded_live')):
            raise ValueError('EXACT_REPLAY_REQUIRED')
        for t in (manifest['input_cutoff_at_utc'],payload['generated_at_utc']):
            if not freshness(now=now,retrieved=t,max_retrieval_age=900)['ok']: raise ValueError('STALE_MANIFEST')
        expected=manifest['outputs']['alert_candidates.json']
        if expected['sha256']!=file_hash(Path(root)/'alert_candidates.json') or expected['payload_sha256']!=digest(payload):
            raise ValueError('BUY_PAYLOAD_HASH_MISMATCH')
        return {'ok':True,'scan_id':manifest['scan_id'],'consumed_at':now,'manifest_sha256':digest(manifest)}
    except (KeyError,TypeError,ValueError,OSError) as exc:
        return {'ok':False,'reason':str(exc) if isinstance(exc,ValueError) else 'INCOMPLETE_BUY_BUNDLE'}


def apply_receipt(cycle, receipt):
    if (receipt.get('scan_id')!=cycle['scan_id'] or receipt.get('data_policy')!=cycle['data_policy']
        or receipt.get('comparison_sha256')!=digest(cycle) or receipt.get('status')!='PUBLISHED'):
        raise ValueError('PUBLICATION_RECEIPT_MISMATCH')
    start=timestamp(receipt['publication_started_at']);end=timestamp(receipt['publication_confirmed_at'])
    if end<start: raise ValueError('PUBLICATION_RECEIPT_CLOCK')
    result=copy.deepcopy(cycle)
    for name,p in result['policies'].items():
        status=receipt.get('policy_publication',{'V4':'PUBLISHED'}).get(name,'UNKNOWN')
        p['native'].update(publication_status=status,published_at=end if status=='PUBLISHED' else None,
                           publication_interval=[start,end],time_semantics='CONFIRMATION_UPPER_BOUND')
    return result
