"""Development-only prospective cohorts and explicit future validation gates.

No decision, account or notification route imports this module. Descriptive
pilot differences are never used to optimize a candidate or claim superiority.
"""
from __future__ import annotations

import base64
from collections import Counter
import hashlib
import math
from pathlib import Path
import statistics
import subprocess

from research.common import timestamp
from research.comparison import SPEC, POLICIES, episodes, evaluate_pairs
from research.input_contract import digest
from research.policies import CORRECTED_DATA, identities
from research.evaluation import HORIZONS

PILOT_POLICY = 'TECHNICAL_PILOT_INSTRUMENTATION_V1'
BLOCK_SCENARIOS = [14400, 86400, 259200]  # Descriptive sensitivity, not independence claims.
MAX_HORIZON = max(SPEC['horizon_seconds'], *HORIZONS.values())


def code_identity(root):
    root = Path(root)
    revision = subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
    files = subprocess.check_output(['git','-C',str(root),'ls-tree','-r','--name-only',revision],text=True).splitlines()
    def relevant(name):
        return (name.endswith('.py') or name.startswith(('config/','baseline/','.github/workflows/'))
                or name == 'v4_config.json' or 'requirements' in Path(name).name)
    files = [n for n in files if relevant(n)]
    blobs = {}
    for name in files:
        expected = subprocess.check_output(['git','-C',str(root),'rev-parse',revision+':'+name],text=True).strip()
        data = (root/name).read_bytes()
        actual = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if actual != expected:
            raise ValueError('UNCOMMITTED_CODE_OR_POLICY:'+name)
        blobs[name] = actual
    untracked = subprocess.check_output(['git','-C',str(root),'ls-files','--others','--exclude-standard'],text=True).splitlines()
    if any(relevant(n) for n in untracked):
        raise ValueError('UNCOMMITTED_CODE_OR_POLICY')
    return {'commit':revision,'blobs':blobs,'fingerprint':digest(blobs)}


def public_bootstrap(root):
    """Exact bytes of public rolling state only; never copy private monitoring state."""
    root=Path(root)
    paths=sorted((root/'policy_state'/CORRECTED_DATA).rglob('*.json'))
    result={}
    for p in paths:
        if p.is_symlink(): raise ValueError('BOOTSTRAP_SYMLINK_REFUSED')
        data=p.read_bytes()
        result[str(p.relative_to(root))]={'sha256':hashlib.sha256(data).hexdigest(),
                                        'base64':base64.b64encode(data).decode()}
    return result


def validate_enrollment(session, scan, code, now):
    if scan.get('source')!='live' or scan.get('stage')!='TECHNICAL_PILOT':
        raise ValueError('NOT_A_LIVE_TECHNICAL_PILOT_SCAN')
    if scan.get('data_policy')!=session['data_policy'] or code['fingerprint']!=session['code_fingerprint']:
        raise ValueError('PILOT_VERSION_CHANGED')
    if scan.get('code_commit')!=code['commit']:
        raise ValueError('SCAN_CODE_REVISION_MISMATCH')
    start=timestamp(scan['scan_ts']);end=timestamp(scan['input_cutoff_at_utc'])
    if not timestamp(session['started_at'])<=start<=end<=timestamp(now):
        raise ValueError('RETROSPECTIVE_OR_FUTURE_ENROLLMENT')


def _stats(values):
    return {'n':len(values),'mean':statistics.mean(values) if values else None,
            'sample_variance':statistics.variance(values) if len(values)>1 else None}


def _correlation(pairs):
    if len(pairs)<3: return None
    a,b=zip(*pairs)
    if statistics.pvariance(a)==0 or statistics.pvariance(b)==0: return None
    return statistics.correlation(a,b)


def sizing_metrics(cycles, labels, start, end, blocks=BLOCK_SCENARIOS):
    start,end=timestamp(start),timestamp(end)
    if end<start: raise ValueError('INVALID_PILOT_WINDOW')
    if not blocks or any(not isinstance(b,int) or b<MAX_HORIZON for b in blocks):
        raise ValueError('INVALID_BLOCK_SCENARIOS')
    # episodes() rejects conflicting duplicate scans; same scan is not new evidence.
    eps=episodes(cycles)
    unique={(c['data_policy'],c['scan_id']):c for c in cycles}
    cycles=list(unique.values())
    if any(not start<=c['cutoff']<=end for c in cycles): raise ValueError('CYCLE_OUTSIDE_PILOT')
    comparison=evaluate_pairs(cycles,labels)
    positive=[r for r in comparison['episode_rows'] if r['positive']]
    contrasts={}
    for base in ('V4','DL1'):
        for mode in ('common','native'):
            known=[];unknown=0
            for row in positive:
                a,b=row['policies']['DL2_'+mode],row['policies'][base+'_'+mode]
                if a is None or b is None: unknown+=1
                else: known.append({**row,'difference':a-b})
            differences=[r['difference'] for r in known]
            sensitivity={}
            for block in blocks:
                grouped={}
                for r in known:
                    bucket=int((r['at']-start)//block)
                    grouped.setdefault(bucket,[]).append(r)
                # One time block contains ALL markets; no independent-market sample count.
                summaries=[{'block':k,'start':start+k*block,'end':start+(k+1)*block,
                    'n':len(rows),'sum':sum(r['difference'] for r in rows),
                    'mean':statistics.mean(r['difference'] for r in rows),
                    'markets':sorted({r['market'] for r in rows})} for k,rows in sorted(grouped.items())]
                by_id={r['block']:r for r in summaries}
                adjacent=[(r['mean'],by_id[r['block']+1]['mean']) for r in summaries if r['block']+1 in by_id]
                market_blocks={}
                for k,rows in grouped.items():
                    for m in {r['market'] for r in rows}:
                        market_blocks.setdefault(m,{})[k]=statistics.mean(r['difference'] for r in rows if r['market']==m)
                correlations=[];unidentifiable=0
                markets=sorted(market_blocks)
                for i,m in enumerate(markets):
                    for n in markets[i+1:]:
                        common=market_blocks[m].keys() & market_blocks[n].keys()
                        pairs=[(market_blocks[m][k],market_blocks[n][k]) for k in sorted(common)]
                        corr=_correlation(pairs)
                        if corr is None: unidentifiable+=1
                        else: correlations.append({'markets':[m,n],'paired_blocks':len(pairs),'correlation':corr})
                sensitivity[str(block)]={'blocks':summaries,'block_mean_dispersion':_stats([r['mean'] for r in summaries]),
                    'adjacent_block_pairs':len(adjacent),'lag_one_correlation':_correlation(adjacent),
                    'cross_market_correlations':correlations,'unidentifiable_market_pairs':unidentifiable,
                    'empty_blocks':max(0,math.ceil((end-start)/block)-len(grouped)),
                    'independence_assumed':False}
            contrasts['DL2_minus_'+base+'_'+mode]={**_stats(differences),'paired_differences':differences,
                'discordant_pairs':sum(d!=0 for d in differences),'unknown_pairs':unknown,
                'discordance_fraction':sum(d!=0 for d in differences)/len(differences) if differences else None,
                'block_sensitivity':sensitivity,'denominator':'observable positive episodes with known paired delivery'}
    seconds=end-start
    return {'instrumentation_policy':PILOT_POLICY,'stage':'TECHNICAL_PILOT_DEVELOPMENT_ONLY',
        'scan_count':len(cycles),'episode_count':len(eps),'observable_labels':len(comparison['episode_rows']),
        'observable_label_fraction':len(comparison['episode_rows'])/len(eps) if eps else None,
        'positive_episodes':len(positive),'positive_episodes_per_calendar_day':len(positive)*86400/seconds if seconds else None,
        'episode_frequency_per_calendar_day':len(eps)*86400/seconds if seconds else None,
        'calendar_seconds':seconds,'contrasts':contrasts,'paired_comparison':comparison,
        'recommended_sample_size':None,'confidence_interval':None,'superiority_demonstrated':False,'held_out_performed':False,
        'limitations':['Calendar rates include observed gaps; missing labels remain unknown.',
                      'Pairwise complete block correlations are descriptive and may be unidentifiable.',
                      'Block sizes are sensitivity scenarios, not scientifically validated choices.',
                      'No sizing on the most favorable pilot gain; no probability calibration.']}


def validate_protocol(p, now, last_development_cutoff, pilot_report_sha256):
    required=('effect','error','precision','multiplicity','blocks','duration','sample_size','costs_and_delays')
    if p.get('schema_version')!=1: raise ValueError('PROTOCOL_SCHEMA')
    if p.get('primary_contrast') not in {f'DL2_minus_{b}_{m}' for b in ('V4','DL1') for m in ('common','native')}:
        raise ValueError('PRIMARY_CONTRAST_REQUIRED')
    if p.get('primary_metric')!='recall_at_3': raise ValueError('PRIMARY_METRIC_REQUIRED')
    for k in ('useful_effect','error_rate','precision_target'):
        value=p.get(k)
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not 0<value<1: raise ValueError('UNSET_STATISTICAL_CHOICE:'+k)
    if any(not isinstance(p.get('justification',{}).get(k),str) or not p['justification'][k].strip() for k in required):
        raise ValueError('JUSTIFICATION_REQUIRED')
    if p.get('multiplicity') not in ('primary_only','holm','bonferroni'): raise ValueError('MULTIPLICITY_REQUIRED')
    for k in ('planned_days','minimum_informative_pairs','block_seconds','embargo_seconds'):
        if type(p.get(k)) is not int or p[k]<=0: raise ValueError('POSITIVE_INTEGER_REQUIRED:'+k)
    if p['planned_days']<30 or p['embargo_seconds']<MAX_HORIZON: raise ValueError('DURATION_OR_EMBARGO_TOO_SHORT')
    if p['block_seconds']<MAX_HORIZON: raise ValueError('BLOCK_TOO_SHORT')
    sensitivity=p.get('sensitivity_block_seconds')
    if not isinstance(sensitivity,list) or p['block_seconds'] not in sensitivity or any(type(b) is not int or b<MAX_HORIZON for b in sensitivity):
        raise ValueError('BLOCK_SENSITIVITY_REQUIRED')
    if p.get('analysis_rule')!='fixed_calendar_then_information_gate': raise ValueError('STOP_RULE_REQUIRED')
    if p.get('pilot_report_sha256')!=pilot_report_sha256: raise ValueError('PILOT_EVIDENCE_MISMATCH')
    if timestamp(p['validation_start']) < max(timestamp(now),timestamp(last_development_cutoff)+MAX_HORIZON)+p['embargo_seconds']:
        raise ValueError('FUTURE_START_PURGE_AND_EMBARGO_REQUIRED')
    sensitivity=p.get('cost_delay_sensitivity',{})
    for k,lower in (('fee_multipliers',1),('delay_seconds',0)):
        values=sensitivity.get(k)
        if not isinstance(values,list) or not values or any(type(v) not in (int,float) or not math.isfinite(v) or v<lower for v in values):
            raise ValueError('COST_DELAY_SENSITIVITY_REQUIRED')


def holdout_eligibility(frozen, scan, code):
    """Eligibility only, never an analysis or a promotion authorization."""
    reasons=[]
    if scan.get('stage')!='HELD_OUT_FROZEN' or scan.get('freeze_id')!=digest(frozen):
        reasons.append('NO_EXPLICIT_FROZEN_COHORT')
    if code['fingerprint']!=frozen['code_fingerprint'] or scan.get('code_commit')!=code['commit']:
        reasons.append('FROZEN_CODE_CHANGED')
    if scan.get('data_policy')!=frozen['data_policy'] or scan.get('source')!='live': reasons.append('INELIGIBLE_SOURCE')
    if not frozen['validation_start']<=timestamp(scan['scan_ts'])<=timestamp(scan['input_cutoff_at_utc'])<frozen['analysis_at']:
        reasons.append('OUTSIDE_FROZEN_WINDOW')
    if frozen['last_development_cutoff']+MAX_HORIZON>frozen['validation_start']-frozen['embargo_seconds']:
        reasons.append('DEVELOPMENT_LABEL_OVERLAP')
    return {'eligible':not reasons,'reasons':reasons,'held_out_performed':False,'promotion_allowed':False}


def analysis_gate(frozen, now, informative_pairs):
    """Fixed calendar then information gate; no peeking or favorable-result stopping."""
    if timestamp(now)<frozen['analysis_at']:
        status='WAIT_FOR_FIXED_ANALYSIS_DATE'
    elif informative_pairs<frozen['protocol']['minimum_informative_pairs']:
        status='INCONCLUSIVE_INSUFFICIENT_INFORMATION'
    else:
        status='ELIGIBLE_FOR_PREREGISTERED_ANALYSIS_ONLY'
    return {'status':status,'automatic_extension':False,'promotion_allowed':False,'held_out_performed':False}
