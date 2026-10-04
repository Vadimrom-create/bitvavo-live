"""Non-decision execution evidence. Estimates are never fills or authorization."""
import copy,hashlib,json,time
from pathlib import Path
from research.common import atomic_json,finite,timestamp,utc

SIZES=(50,100,150)
def identity(kind,*parts):
    return kind+'_'+hashlib.sha256(json.dumps(parts,sort_keys=True,separators=(',',':')).encode()).hexdigest()[:32]

def identifiers(row,cycle,source='PRODUCTION'):
    episode=(identity('episode',source,row['market'],float(row['episode_started_ts']),int(row['episode']))
             if row.get('episode_started_ts') is not None and row.get('episode') is not None else row.get('episode_id'))
    return {'episode_id':episode,'decision_id':identity('decision',source,cycle,row['market'],episode),
            'signal_id':identity('signal',source,cycle,row['market']),
            'episode_identity_status':'KNOWN' if episode else 'UNKNOWN_NOT_INFERRED_FROM_SYMBOL'}

def walk(levels,amount,quote_budget):
    remaining=amount;quantity=quote=0.;used=[]
    for p,q in levels:
        take=min(q,remaining/p if quote_budget else remaining)
        if take<=0:break
        quote+=p*take;quantity+=take;remaining-=p*take if quote_budget else take
        used.append({'price_eur':p,'quantity':take,'quote_eur':p*take})
        if remaining<=1e-9:break
    covered=remaining<=1e-9
    return {'covered':covered,'quantity':quantity,'quote_eur':quote,'vwap_eur':quote/quantity if quantity and covered else None,
            'uncovered':max(0,remaining),'levels_consumed':used,'status':'ESTIMATE' if covered else 'INSUFFICIENT_OBSERVED_DEPTH'}

def book_evidence(book,request_meta,available_ts,stop=None):
    result={'schema':'solaire_execution_cost_evidence_v1','raw_book':copy.deepcopy(book),
            'request_started_at_utc':request_meta.get('request_started_at_utc'),
            'response_received_at_utc':request_meta.get('retrieved_at_utc'),
            'available_at_ts':available_ts,'best_bid_eur':None,'best_ask_eur':None,
            'spread':None,'sizes':{},'book_valid':False,'missing_data':[],
            'full_exchange_depth_known':False,'depth_scope':'ALL_LEVELS_IN_THIS_RESPONSE',
            'fill_status':'NO_REAL_FILL_EVIDENCE','passive_fill_status':'PASSIVE_FILL_UNKNOWN',
            'c3_status':'UNKNOWN/NO_AUTHORIZATION','research_only':True,
            'affects_buy_gate':False,'affects_email':False,'orders_submitted':False}
    if not book:result['missing_data'].append('BOOK_NOT_REQUESTED_OR_UNAVAILABLE');return result
    try:
        sides={}
        for side in ['asks','bids']:
            parsed=[]
            for level in book.get(side,[]):
                p,q=finite(level[0]),finite(level[1])
                if p is None or q is None or p<=0 or q<=0:raise ValueError('INVALID_BOOK_LEVEL')
                parsed.append((p,q))
            prices=[p for p,q in parsed]
            if not parsed or prices!=sorted(set(prices),reverse=side=='bids'):raise ValueError('INCOMPLETE_OR_UNORDERED_BOOK')
            sides[side]=parsed
        bid,ask=sides['bids'][0][0],sides['asks'][0][0]
        if bid>ask:raise ValueError('CROSSED_BOOK')
        result.update(book_valid=True,best_bid_eur=bid,best_ask_eur=ask,spread=ask/bid-1,
                      bid_depth_eur=sum(p*q for p,q in sides['bids']),ask_depth_eur=sum(p*q for p,q in sides['asks']))
        received=request_meta.get('retrieved_at_utc')
        age=available_ts-timestamp(received) if received else None
        result['snapshot_age_seconds']=age
        requested=request_meta.get('request_started_at_utc')
        result['request_response_seconds']=timestamp(received)-timestamp(requested) if received and requested else None
        result['response_to_validation_seconds']=age
        result['freshness_status']='FRESH' if age is not None and 0<=age<=90 else 'UNKNOWN_OR_STALE'
        if age is None:result['missing_data'].append('RESPONSE_TIMESTAMP')
        if not request_meta.get('request_started_at_utc'):result['missing_data'].append('REQUEST_TIMESTAMP')
        for size in SIZES:
            entry=walk(sides['asks'],size,True)
            exit_est=walk(sides['bids'],entry['quantity'],False) if entry['covered'] else None
            gross=exit_est['quote_eur'] if exit_est and exit_est['covered'] else None
            fees=size*.0025+gross*.0025 if gross is not None else None
            result['sizes'][str(size)]={'entry':entry,'immediate_exit_estimate':exit_est,
                'entry_fee_eur_est':size*.0025,'roundtrip_fees_eur_est':fees,
                'entry_impact_from_ask_pct':(entry['vwap_eur']/ask-1)*100 if entry['vwap_eur'] else None,
                'roundtrip_cost_eur_est':size-gross+fees if gross is not None else None,
                'roundtrip_adverse_cost_eur_est':size-gross+fees+(size+gross)*.001 if gross is not None else None,
                'fee_each_side_assumption':.0025,'additional_adverse_slippage_each_side':.001,
                'planned_stop_loss_eur_est':entry['quantity']*(entry['vwap_eur']-stop)+(size+entry['quantity']*stop)*.0035
                    if entry['covered'] and stop and 0<stop<entry['vwap_eur'] else None,
                'exit_scope':'SAME_SNAPSHOT_IMMEDIATE_LIQUIDATION_NOT_FUTURE_EXIT',
                'status':'ESTIMATE' if gross is not None else 'UNKNOWN_EXIT_COST'}
    except (ValueError,TypeError,IndexError,KeyError) as exc:
        result['book_valid']=False;result['missing_data'].append(str(exc))
    return result

def capture_validation(row,cycle,client,record_start,validated,reason,checked_at,*,source='PRODUCTION',root='execution_observations',parent_decision_id=None):
    """Best effort telemetry: absolutely no observer failure may veto a BUY."""
    try:
        ids=identifiers(row,cycle,source);available=time.time()
        records=copy.deepcopy(getattr(client,'records',[])[record_start:])
        books=[r for r in records if r.get('path')=='/'+row['market']+'/book']
        observed=books[-1] if books else {};trade=(validated or {}).get('trade') or {}
        evidence=book_evidence(observed.get('data'),observed,available,trade.get('stop_eur'))
        oid=identity('observation',source,ids['decision_id'],checked_at,observed.get('request_started_at_utc'))
        result={**ids,'observation_id':oid,'market':row['market'],'source':source,'cycle_id':cycle,
                'control_check_started_at_ts':checked_at,'recorded_at_ts':available,'parent_decision_id':parent_decision_id,
                'execution_pass':validated is not None,'execution_reason':reason or 'PASS',
                'plan':copy.deepcopy(trade),'execution_costs':evidence,'requests':records,
                'research_only':True,'affects_buy_gate':False,'affects_email':False,'orders_submitted':False}
        path=Path(root)/(oid+'.json')
        if not path.exists():atomic_json(path,result)
        return {**ids,'execution_observation_id':oid,'execution_evidence_path':str(path),'evidence_status':'RECORDED'}
    except Exception as exc:
        return {'evidence_status':'UNAVAILABLE','evidence_error':type(exc).__name__}
