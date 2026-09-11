"""Versioned, censored paired observations. This module never makes live decisions.

An episode is anchored ex ante. Later scans can detect that SAME opportunity;
its reference price and outcome window never slide with a slow policy.
"""
from __future__ import annotations

import copy
import math
from research.common import finite, timestamp
from research.input_contract import digest
from research.policies import identities, FROZEN_V4, FROZEN_DL1, CANDIDATE
from research.quality import assess
from research.risk import DEFAULTS

POLICIES = {'V4': FROZEN_V4, 'DL1': FROZEN_DL1, 'DL2': CANDIDATE}
SPEC = {'evaluation_policy': 'PROSPECTIVE_PAIRED_V1', 'top_n': 3,
        'horizon_seconds': 14400, 'threshold_pct': 5, 'max_adverse_pct': 5,
        'common_availability_seconds': 120, 'minimum_useful_lead_seconds': 900,
        'episode_rule': 'market/setup/explicit structural levels; anchored maximum 4h; missing data does not reset',
        'native_stage': 'PUBLICATION_OBSERVED', 'probabilities': 'NOT_CALIBRATED',
        'execution': 'same ex ante risk plan; passive OHLC touch is ambiguous'}


def build_cycle(scan, results, timings=None):
    """Accept only decisions on this immutable bundle; no outcome argument."""
    cutoff = timestamp(scan['input_cutoff_at_utc'])
    sid, data = scan['scan_id'], scan['data_policy']
    observations = {}
    for o in scan['observations']:
        market = o['market']
        if market in observations:
            raise ValueError('DUPLICATE_MARKET')
        if any(s and timestamp(s['retrieved_at_utc']) > cutoff for s in o.get('input_sources', {}).values()):
            raise ValueError('INPUT_AFTER_CUTOFF')
        q = assess(o, cutoff)
        observations[market] = {'price': o.get('price_eur'), 'usable_data': q['capabilities']['structure']['available'],
            'data_reasons': q['capabilities']['structure'].get('reasons', []), 'category': o.get('category', 'UNANALYZED'),
            'setup_key': o.get('episode_setup_key', (o.get('baseline') or {}).get('entry_mode')),
            'structural_levels': o.get('episode_structural_levels', {'invalidation_eur': ((o.get('features') or {}).get('15m') or {}).get('support_eur')}),
            'liquidity_eur': (o.get('baseline') or {}).get('quote_volume_24h_eur'),
            'capabilities': q['capabilities'], 'baseline_analyzed': bool(o.get('baseline'))}
    policies = {}
    for name, identity in POLICIES.items():
        result = scan.get('baseline_output') if name == 'V4' else results.get(name)
        if result is not None:
            if result.get('scan_id', sid) != sid or result.get('data_policy', data) != data:
                raise ValueError('POLICY_SNAPSHOT_MISMATCH')
            if result.get('source_snapshot_sha256', digest(scan)) != digest(scan):
                raise ValueError('POLICY_INPUT_HASH_MISMATCH')
        rows = (result or {}).get('watch' if name == 'V4' else 'ranked', [])
        rows = [r for r in rows if (r.get('action_status') in {'WATCH','ENTRY_WINDOW','BUY_READY','REENTRY_READY'}
                                  if name == 'V4' else bool(r.get('bucket')))]
        selected = [r['market'] for r in rows]
        if len(selected) != len(set(selected)) or set(selected) - observations.keys():
            raise ValueError('INVALID_POLICY_POPULATION')
        native = copy.deepcopy((timings or {}).get(name, {}))
        native.setdefault('policy_ready_at', (result or {}).get('policy_ready_at', scan.get('policy_ready_at') if name == 'V4' else None))
        for k in ('policy_ready_at', 'published_at'):
            if native.get(k) is not None:
                native[k] = timestamp(native[k])
        native.setdefault('published_at', None)
        native.setdefault('publication_status', 'UNKNOWN')
        ids = identities(data_policy=data, decision_policy=identity)
        policies[name] = {**ids, 'state_identity': digest(ids), 'status': 'OK' if result is not None else 'POLICY_FAILED',
            'selected': selected[:SPEC['top_n']], 'native_complete_list': selected,
            'buckets': {r['market']: r.get('bucket', 'V4_NATIVE_'+r.get('action_status','UNKNOWN')) for r in rows},
            'native': native, 'plans': []}
    return {'schema_version': 1, 'scan_id': sid, 'data_policy': data, 'cutoff': cutoff,
            'source_snapshot_sha256': digest(scan), 'code_commit': scan.get('code_commit'),
            'stage': scan.get('stage', 'DEVELOPMENT_REPLAY'), 'spec': SPEC,
            'observations': observations, 'policies': policies}


def episodes(cycles):
    unique = {}
    for c in cycles:
        key = (c['data_policy'], c['scan_id'])
        if key in unique and digest(c) != digest(unique[key]):
            raise ValueError('COMPARISON_SCAN_COLLISION')
        unique[key] = c
    active, result = {}, []
    for c in sorted(unique.values(), key=lambda c:(c['cutoff'],c['data_policy'],c['scan_id'])):
        for market, o in sorted(c['observations'].items()):
            key = (c['data_policy'], market)
            e = active.get(key)
            setup = (o.get('setup_key'), o.get('structural_levels'))
            # Only explicit, usable structural evidence can start a new setup.
            old_level = ((e['setup'][1] or {}).get('invalidation_eur') if e else None)
            changed = e and o['usable_data'] and ((setup[0] is not None and e['setup'][0] is not None and setup[0] != e['setup'][0])
                or (old_level is not None and o['price'] is not None and o['price'] < old_level))
            if not e or c['cutoff'] >= e['at'] + SPEC['horizon_seconds'] or changed:
                e = {'id': digest([*key,c['scan_id'],setup])[:24], 'market': market, 'data_policy':c['data_policy'],
                     'scan_id':c['scan_id'], 'at':c['cutoff'], 'setup':setup, 'observation':o, 'visits':[]}
                active[key] = e
                result.append(e)
            e['visits'].append(c)
    return result


def labels_from_db(cycles, db, now):
    from research.evaluation import outcome
    labels = {}
    for e in episodes(cycles):
        start = math.ceil(e['at']/300)*300
        if start+SPEC['horizon_seconds'] > now:
            label = {'status':'IMMATURE'}
        else:
            label = outcome(db, {'market':e['market'],'ts':e['at'],'price':e['observation']['price']}, SPEC['horizon_seconds'])
            if label['status'] == 'COMPLETE':
                target = label['targets']['5']
                label = {**label, 'positive': bool(target['reached'] and target['mae_before_target_pct'] >= -5),
                         'first_target_at': e['at'] + target['time_to_target_minutes']*60 if target['reached'] else None}
        labels[(e['scan_id'],e['market'])] = label
    return labels


def _counts():
    return dict(tp=0,fp=0,tn=0,fn_end_to_end=0,fn_decision_given_data=0,positive_denominator=0,
                positive_data_denominator=0, unknown_delivery=0, unknown_positive_delivery=0, fn_components=dict(data=0,decision=0,integration=0),
                lead_before_target_seconds=[], useful_lead_tp=0)


def evaluate_pairs(cycles, labels, missing_windows=None):
    if len({c['data_policy'] for c in cycles}) > 1:
        raise ValueError('EVALUATE_DATA_POLICIES_SEPARATELY')
    eps = episodes(cycles)
    result = {'evaluation_policy':SPEC['evaluation_policy'], 'spec':SPEC, 'stage':'DEVELOPMENT_ONLY',
              'episode_count':len(eps), 'censored_episodes':0, 'censoring':[], 'episode_rows':[],
              'missing_windows':missing_windows or [], 'policies':{p:{mode:_counts() for mode in ('common','native')} for p in POLICIES}}
    for e in eps:
        label = labels.get((e['scan_id'],e['market']), {'status':'CENSORED'})
        if label.get('status') != 'COMPLETE':
            result['censored_episodes'] += 1
            result['censoring'].append({'episode_id':e['id'],'market':e['market'],'category':e['observation']['category'],
                'liquidity_eur':e['observation']['liquidity_eur'],'status':label['status']})
            continue
        positive = bool(label['positive'])
        deadline = label.get('first_target_at') if positive else e['at'] + SPEC['horizon_seconds']
        if deadline is None:
            raise ValueError('POSITIVE_LABEL_REQUIRES_EVENT_TIME')
        # Useful reference does not move with the decision/publication.
        visits = [c for c in e['visits'] if c['cutoff'] < deadline]
        usable = any(c['observations'][e['market']]['usable_data'] for c in visits)
        erow = {'episode_id':e['id'],'at':e['at'],'market':e['market'],'positive':positive,'usable_data':usable,
                'mfe_pct':label.get('mfe_pct'),'mae_pct':label.get('mae_pct'),'policies':{}}
        for name in POLICIES:
            selected, releases = [], []
            for c in visits:
                p = c['policies'][name]
                if e['market'] not in p['selected'] or p['status'] != 'OK':
                    continue
                ready = p['native'].get('policy_ready_at')
                # Common release is bounded; it never waits indefinitely for V2.
                common_at = c['cutoff'] + SPEC['common_availability_seconds']
                selected.append((ready,common_at,p['native']))
            policy_at = [r for r,_,_ in selected if r is not None and r < deadline]
            for mode in ('common','native'):
                count = result['policies'][name][mode]
                delivery_unknown = False
                if mode == 'common':
                    releases = [a for r,a,_ in selected if r is not None and r <= a and a < deadline]
                else:
                    releases = [n['published_at'] for r,_,n in selected if n.get('publication_status')=='PUBLISHED'
                                and n.get('published_at') is not None and r is not None and r <= n['published_at'] < deadline]
                    delivery_unknown = not releases and any(n.get('publication_status')=='UNKNOWN' for _,_,n in selected)
                detected = bool(releases)
                if positive:
                    count['positive_denominator'] += 1
                    count['positive_data_denominator'] += int(usable)
                    count['fn_decision_given_data'] += int(usable and not policy_at)
                    if delivery_unknown:
                        count['unknown_delivery'] += 1
                        count['unknown_positive_delivery'] += 1
                    elif detected:
                        count['tp'] += 1
                        lead = deadline-min(releases)
                        count['lead_before_target_seconds'].append(lead)
                        count['useful_lead_tp'] += int(lead >= SPEC['minimum_useful_lead_seconds'])
                    else:
                        count['fn_end_to_end'] += 1
                        cause = 'data' if not usable else 'decision' if not policy_at else 'integration'
                        count['fn_components'][cause] += 1
                elif delivery_unknown:
                    count['unknown_delivery'] += 1
                else:
                    count['fp' if detected else 'tn'] += 1
                erow['policies'][name+'_'+mode] = None if delivery_unknown else int(detected)
        result['episode_rows'].append(erow)
    for modes in result['policies'].values():
        for c in modes.values():
            positives = c['positive_denominator']
            censored = result['censored_episodes']
            unknown = censored + c['unknown_positive_delivery']
            c['recall'] = c['tp']/positives if positives and not c['unknown_positive_delivery'] else None
            c['precision'] = c['tp']/(c['tp']+c['fp']) if c['tp']+c['fp'] else None
            c['fn_decision_given_data_rate'] = c['fn_decision_given_data']/c['positive_data_denominator'] if c['positive_data_denominator'] else None
            c['recall_bounds'] = [c['tp']/(positives+censored), (c['tp']+unknown)/(positives+censored)] if positives+censored else [None,None]
    result['paired_differences'] = {}
    for base in ('V4','DL1'):
        a=result['policies']['DL2']['common']['recall'];b=result['policies'][base]['common']['recall']
        result['paired_differences']['DL2_minus_'+base] = a-b if a is not None and b is not None else None
    result['coverage'] = {'observable_episodes':len(eps)-result['censored_episodes'],'all_episodes':len(eps),
                          'missing_reference_windows':len(result['missing_windows']), 'missed_window_outcomes':'UNKNOWN_UNLESS_INDEPENDENTLY_OBSERVED'}
    result['stability'] = stability(cycles)
    result['confidence_interval'] = None  # Block design and held-out remain future work.
    return result


def reserve_plan(states, scenario, plan, cycle_id, config=None):
    cfg={**DEFAULTS,**(config or {})}
    state=states.setdefault(scenario, {'reserved_eur':0.,'reserved_risk_eur':0.,'plans':{},'cycles':[]})
    if not plan.get('valid') or cycle_id in state['cycles'] or plan['market'] in state['plans']:
        return False
    stake,risk=plan['stake_eur'],plan['theoretical_loss_eur']
    if not (0 < stake <= cfg['max_position_eur'] and 0 < risk <= cfg['max_trade_risk_eur']): return False
    if (state['reserved_eur']+stake > min(cfg['max_exposure_eur']-cfg['existing_exposure_eur'],
        (cfg['cash_eur']-cfg['reserve_eur'])/(1+cfg['fee_rate']+cfg['slippage_rate'])) or
        state['reserved_risk_eur']+risk+cfg['existing_risk_eur'] > cfg['max_portfolio_risk_eur'] or
        len(state['plans'])+cfg['existing_positions'] >= cfg['max_positions']): return False
    state['reserved_eur']+=stake;state['reserved_risk_eur']+=risk
    state['plans'][plan['market']]=copy.deepcopy(plan);state['cycles'].append(cycle_id)
    return True


def settle_plan(states, scenario, market, result):
    state=states[scenario]
    # Unknown fill remains exposed; it must not free capital optimistically.
    if result['status'] not in {'COMPLETE','UNFILLED','INVALIDATED'}: return False
    p=state['plans'].pop(market)
    state['reserved_eur']-=p['stake_eur'];state['reserved_risk_eur']-=p['theoretical_loss_eur']
    state['realized_pnl_eur']=state.get('realized_pnl_eur',0)+result.get('pnl_eur',0)
    return True


def simulate_plan(plan, bars, *, available_at, expires_at):
    if not plan.get('valid') or plan.get('recorded_at') is None or plan['recorded_at'] > available_at:
        return {'status':'UNAVAILABLE','reason':'NO_EX_ANTE_PLAN'}
    start=math.ceil(available_at/300)*300
    common={'first_admissible_bar':start,'available_at':available_at,'expires_at':expires_at,
            'assumptions':'OHLC theoretical model; not a verified exchange fill'}
    rows=sorted([b for b in bars if start <= b['t']/1000 < expires_at],key=lambda b:b['t'])
    expected=max(0,math.ceil((expires_at-start)/300))
    if not rows or len(rows)!=expected or any(b['t']/1000 != start+i*300 for i,b in enumerate(rows)):
        return {**common,'status':'CENSORED','reason':'EXECUTION_BARS_MISSING'}
    entry,stop,target=plan['entry_eur'],plan['stop_eur'],plan['tp1_eur']
    if not 0 < stop < entry < target: return {**common,'status':'UNAVAILABLE','reason':'INVALID_PLAN_LEVELS'}
    fee=plan['cost_assumptions']['fee_rate_each_side'];slip=plan['cost_assumptions']['slippage_rate_each_side']
    first=rows[0]
    if first['o'] <= stop:
        return {**common,'status':'INVALIDATED','reason':'GAP_BEFORE_ENTRY'}
    if first['o'] > entry:
        if any(b['l'] <= entry for b in rows):
            return {**common,'status':'AMBIGUOUS','reason':'PASSIVE_TOUCH_NOT_A_CERTAIN_FILL'}
        return {**common,'status':'UNFILLED'}
    fill=min(entry,first['o']*(1+slip))
    price,reason=rows[-1]['c']*(1-slip),'HORIZON_EXIT'
    ambiguous=False
    for b in rows:
        if b['l'] <= stop:
            price,reason=min(stop,b['o'])*(1-slip),'STOP'
            ambiguous=b['h'] >= target
            break
        if b['h'] >= target:
            price,reason=target*(1-slip),'TP1'
            break
    qty=float(plan['amount'])
    return {**common,'status':'COMPLETE','pnl_eur':qty*(price*(1-fee)-fill*(1+fee)),
            'exit_reason':reason,'ambiguous_stop_and_target_bar':ambiguous,
            'cost_assumptions':plan['cost_assumptions']}


def data_contrast(a, b, policy):
    """No fabricated D0 cell: pair exact snapshots/periods or report unavailable."""
    keys=lambda cs:{(c['scan_id'],c['cutoff']):c for c in cs}
    left,right=keys(a),keys(b)
    common=sorted(left.keys() & right.keys())
    if not common:
        return {'status':'UNAVAILABLE','reason':'NO_MATCHED_DATA_SNAPSHOTS','policy':policy}
    pairs=[]
    for k in common:
        x,y=left[k],right[k]
        if x['policies'][policy]['decision_policy']!=y['policies'][policy]['decision_policy']:
            raise ValueError('DATA_CONTRAST_CHANGED_DECISION_POLICY')
        pairs.append({'scan_id':k[0],'cutoff':k[1],'left':x['data_policy'],'right':y['data_policy'],
                      'selected_left':x['policies'][policy]['selected'],'selected_right':y['policies'][policy]['selected']})
    return {'status':'PAIRED','policy':policy,'pairs':pairs,'attribution':'data inputs only; no additive decomposition claim'}


def attach_plans(cycle, scan, recorded_at):
    """Identical existing planner, before future bars. No passive/resumption experiment."""
    from research.risk import plan
    from research.decision_layer import BUCKET_IMMEDIATE
    source={o['market']:o for o in scan['observations']}
    for name,p in cycle['policies'].items():
        for market in p['selected']:
            o=source[market];b=o.get('baseline') or {}
            eligible=b.get('buy_ready') if name=='V4' else p['buckets'].get(market)==BUCKET_IMMEDIATE
            if not eligible or not cycle['observations'][market]['capabilities']['immediate']['available']:
                continue
            try:
                proposal=plan(b,o['features']['15m'],o.get('market_meta') or {})
            except (KeyError,TypeError,ValueError):
                continue
            if proposal.get('valid'):
                p['plans']=[{**proposal,'recorded_at':recorded_at,'expires_at':recorded_at+SPEC['horizon_seconds'],
                             'scenario':p['state_identity'],'production_buy_allowed':False}]
                break
    return cycle


def evaluate_portfolios(cycles, db, now):
    """Frozen proposals, separate common/native budgets; unresolved exposure retained."""
    states,events={},[]
    for c in sorted({(c['data_policy'],c['scan_id']):c for c in cycles}.values(),key=lambda c:(c['cutoff'],c['scan_id'])):
        for name,p in c['policies'].items():
            for mode in ('common','native'):
                scenario=p['state_identity']+':'+mode
                for market, old in list(states.get(scenario,{}).get('plans',{}).items()):
                    if old['expires_at'] > c['cutoff']: continue
                    bars=[dict(r) for r in db.execute('SELECT * FROM candles WHERE market=? AND t>=? AND t<? ORDER BY t',
                        (market,old['available_at']*1000,old['expires_at']*1000))]
                    r=simulate_plan(old,bars,available_at=old['available_at'],expires_at=old['expires_at'])
                    if settle_plan(states,scenario,market,r): events.append({'scenario':scenario,'market':market,**r})
                available=c['cutoff']+SPEC['common_availability_seconds'] if mode=='common' else p['native'].get('published_at')
                ready=p['native'].get('policy_ready_at')
                if available is None or ready is None or ready>available or (mode=='native' and p['native'].get('publication_status')!='PUBLISHED'):
                    continue
                for proposed in p['plans']:
                    if proposed['recorded_at']>available or available>=proposed['expires_at']: continue
                    proposal={**proposed,'available_at':available}
                    # Unknown holdings correlation blocks further exposure; never presume decorrelation.
                    if states.get(scenario,{}).get('plans'):
                        events.append({'scenario':scenario,'market':proposal['market'],'status':'CORRELATION_REQUIRES_REVALIDATION'})
                        continue
                    accepted=reserve_plan(states,scenario,proposal,c['scan_id'])
                    events.append({'scenario':scenario,'market':proposal['market'],'status':'RESERVED' if accepted else 'PORTFOLIO_BLOCKED'})
    # Settle only mature plans; no future row can mature a still-open horizon.
    for scenario,state in states.items():
        for market,p in list(state['plans'].items()):
            if p['expires_at']>now: continue
            bars=[dict(r) for r in db.execute('SELECT * FROM candles WHERE market=? AND t>=? AND t<? ORDER BY t',
                (market,p['available_at']*1000,p['expires_at']*1000))]
            r=simulate_plan(p,bars,available_at=p['available_at'],expires_at=p['expires_at'])
            settle_plan(states,scenario,market,r)
            events.append({'scenario':scenario,'market':market,**r})
    return {'states':states,'events':events,'scope':'THEORETICAL_DEVELOPMENT_ONLY','costs':'ASSUMED_NOT_ACCOUNT_VERIFIED',
            'unresolved_fill':'capital remains reserved; no optimistic PnL','production_orders_enabled':False}


def stability(cycles):
    result={name:{'top_changes':0,'rank_changes':0,'bucket_transitions':[],'repeat_without_new_input':0} for name in POLICIES}
    previous={}
    for c in sorted({(c['data_policy'],c['scan_id']):c for c in cycles}.values(),key=lambda c:(c['cutoff'],c['scan_id'])):
        for name,p in c['policies'].items():
            old=previous.get((c['data_policy'],name))
            if old:
                result[name]['top_changes']+=int(set(old['selected'])!=set(p['selected']))
                result[name]['rank_changes']+=sum(old['selected'].index(m)!=p['selected'].index(m) for m in set(old['selected'])&set(p['selected']))
                result[name]['repeat_without_new_input']+=int(old['snapshot']==c['source_snapshot_sha256'])
                for m in set(old['buckets']) & set(p['buckets']):
                    if old['buckets'][m]!=p['buckets'][m]:
                        result[name]['bucket_transitions'].append({'market':m,'at':c['cutoff'],'from':old['buckets'][m],'to':p['buckets'][m]})
            previous[(c['data_policy'],name)]={**p,'snapshot':c['source_snapshot_sha256']}
    return result
