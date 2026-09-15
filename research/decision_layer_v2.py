"""Opportunity-only experimental baseline. All results are shadow observations."""
from research.common import finite, INTERVAL_MS
from research.decision_layer import (BUCKETS, BUCKET_IMMEDIATE, BUCKET_LIMIT, BUCKET_LATENT, BUCKET_REENTRY,
                                    LATENT_OPPORTUNITY_MIN, LATENT_TREND_MIN, IMMEDIATE_ENTRY_MIN,
                                    PASSIVE_LIMIT_ENTRY_MIN, REENTRY_TREND_MIN)
from research.input_contract import digest
from research.policies import CANDIDATE, FROZEN_V4, identities
from research.quality import assess


def pullback_evidence(obs, now):
    """Existing PULLBACK plus observable declining closes, not a resumption trigger."""
    baseline = obs.get('baseline') or {}
    if baseline.get('entry_mode') != 'PULLBACK':
        return None
    cs = (obs.get('setup_evidence') or {}).get('closed_15m_tail') or []
    if len(cs) < 2:
        return None
    a,b = cs[-2:]
    if b['t']-a['t'] != INTERVAL_MS['15m'] or b['t']+INTERVAL_MS['15m'] > now*1000 or b['c'] >= a['c']:
        return None
    reference = min(c['l'] for c in cs)
    return {'phase':'PULLBACK_OBSERVED','source_ids':[(obs.get('input_sources',{}).get('15m') or {}).get('response_id')],
            'observed_at':now,'reference_bar_start_ms':a['t'],'reference_high_eur':a['h'],
            'invalidation_reference_eur':reference,'confirmation_event':None,
            'reference_role':'DESCRIPTIVE_ONLY_NO_RESUMPTION_OR_ORDER_RULE'}


def classify(obs, now, snapshot_id):
    q = assess(obs, now)
    b = obs.get('baseline') or {}
    opp, trend = finite(b.get('opportunity_score')), finite(b.get('trend_score'))
    entry = q['entry_score_measured']
    flags = set(q['raw_flags'])
    late = obs.get('category') == 'TOO LATE' or b.get('action_status') == 'TOO_LATE' or bool(flags & {'TOO_LATE_24H','CHASE_RISK'})
    result = {'market':obs['market'],'opportunity_score':opp,'trend_score':trend,'entry_status':q['entry_status'],
              'entry_score_measured':entry,'rank_score':opp if q['structure_state']=='VALID' else None,
              'bucket':None,'readiness':'AWAIT_REVALIDATION','action':'SHADOW_WATCH',
              'production_buy_allowed':False,'trade_plan':None,'quality':q,'setup_phase':'UNDETERMINED',
              'entry_mode':'UNDETERMINED','reason_codes':[],
              'evidence_id':digest([snapshot_id,obs['market'],q['capabilities']['structure']['source_ids']])}
    if q['structure_state'] != 'VALID':
        result['reason_codes'] = q['capabilities']['structure']['reasons']
        return result
    if opp is None or trend is None:
        result['reason_codes']=['SCORE_UNAVAILABLE']
        return result
    strong = opp >= LATENT_OPPORTUNITY_MIN and trend >= LATENT_TREND_MIN
    pullback = pullback_evidence(obs, now)
    result.update(readiness='WATCH', setup_phase='STRUCTURE_OBSERVED', setup_evidence=pullback)
    if b.get('buy_ready') and entry is not None and entry >= IMMEDIATE_ENTRY_MIN and q['capabilities']['immediate']['available'] and not late:
        result.update(bucket=BUCKET_IMMEDIATE,readiness='THEORETICALLY_READY',entry_mode='IMMEDIATE_CANDIDATE',
                      reason_codes=['V4_BUY_READY_WITH_MEASURED_FRESH_ENTRY'])
    elif strong and trend >= REENTRY_TREND_MIN and pullback:
        result.update(bucket=BUCKET_REENTRY,readiness='AWAIT_CONFIRMATION',setup_phase='PULLBACK_OBSERVED',
                      reason_codes=['EXISTING_PULLBACK_WITH_CLOSED_SEQUENCE'])
    elif strong and entry is not None and entry >= PASSIVE_LIMIT_ENTRY_MIN and q['capabilities']['passive']['available'] and not late:
        result.update(bucket=BUCKET_LIMIT,readiness='INACTIVE_PLAN_REQUIRED',entry_mode='PASSIVE_CANDIDATE',
                      reason_codes=['STRONG_STRUCTURE_NO_EX_ANTE_PASSIVE_PLAN'])
    elif strong:
        result.update(bucket=BUCKET_LATENT,readiness='AWAIT_NEW_OBSERVATION' if late else 'AWAIT_ENTRY',
                      reason_codes=['CURRENT_TOO_LATE_CONSTRAINT' if late else 'ENTRY_NOT_YET_JUSTIFIED'])
    else:
        result['reason_codes']=['STRUCTURAL_THRESHOLDS_NOT_MET']
    return result


def decide(observations, now, snapshot_id, top_n=3):
    if not snapshot_id:
        raise ValueError('EXPLICIT_SNAPSHOT_REQUIRED')
    if len({o['market'] for o in observations}) != len(observations):
        raise ValueError('DUPLICATE_MARKET')
    ranked = [classify(o,now,snapshot_id) for o in observations]
    ranked.sort(key=lambda r:(r['rank_score'] is None, -(r['rank_score'] or 0),r['market']))
    winners = {b:next((r for r in ranked if r['bucket']==b),None) for b in BUCKETS}
    return {'schema_version':1,'policy':CANDIDATE,'frozen_scanner_policy':FROZEN_V4,
            'input_snapshot_id':snapshot_id,'information_cutoff':now,
            'principles':{'production_orders_enabled':False,'probabilities_calibrated':False,
                          'ranking':'OPPORTUNITY_ONLY_EXPERIMENTAL_NOT_OPTIMAL','mandatory_buckets':list(BUCKETS)},
            'thresholds':{'latent_opportunity_min':LATENT_OPPORTUNITY_MIN,'latent_trend_min':LATENT_TREND_MIN,
                          'immediate_entry_min':IMMEDIATE_ENTRY_MIN,'passive_limit_entry_min':PASSIVE_LIMIT_ENTRY_MIN,
                          'reentry_trend_min':REENTRY_TREND_MIN},
            'hypotheses':{'support_limit':{'enabled':False,'status':'DEFERRED_OPTIONAL_SHADOW_EXPERIMENT'},
                          'pullback_resumption':{'enabled':False,'status':'DEFERRED_OPTIONAL_SHADOW_EXPERIMENT'}},
            'bucket_winners':winners,'top_actionable':[r for r in ranked if r['bucket']][:top_n],'ranked':ranked}
