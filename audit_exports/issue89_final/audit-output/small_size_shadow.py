"""Pure proposed volume-proxy challenger; NOT wired to production.

Returns UNKNOWN for missing evidence. The only potentially overridden veto is
24h quote-volume < 75k. Every other production protection remains required.
"""
import math

def assess(x,notional,now):
 required=('available_ts','book_ts','structure_ts','bids','asks','market_trading','confirmed','score','evidence_count','data_ok','range_pct','stop','fee_rate','min_order_eur')
 if any(k not in x or x[k] is None for k in required):return {'status':'UNKNOWN','reason':'MISSING_CAUSAL_INPUT'}
 if not 0<notional<=150:return {'status':'REJECT','reason':'SIZE_OUTSIDE_SHADOW_SCOPE'}
 if any(x[k]>now for k in ('available_ts','book_ts','structure_ts')):return {'status':'REJECT','reason':'FUTURE_INPUT'}
 if any(now-x[k]>90 for k in ('book_ts','structure_ts')):return {'status':'REJECT','reason':'STALE_INPUT'}
 if not x['bids'] or not x['asks']:return {'status':'UNKNOWN','reason':'MISSING_BID_OR_ASK_DEPTH'}
 if not x['market_trading'] or not x['data_ok'] or not x['confirmed'] or x['score']<6.5 or x['evidence_count']<3:return {'status':'REJECT','reason':'UPSTREAM_OR_DATA_NOT_ELIGIBLE'}
 asks=sorted((float(p),float(q)) for p,q in x['asks']);bids=sorted(((float(p),float(q)) for p,q in x['bids']),reverse=True)
 if any(not math.isfinite(v) or v<=0 for side in (asks,bids) for level in side for v in level):return {'status':'UNKNOWN','reason':'INVALID_BOOK'}
 ask=asks[0][0];bid=bids[0][0];spread=ask/bid-1
 if spread<0:return {'status':'UNKNOWN','reason':'CROSSED_BOOK'}
 if spread>.005:return {'status':'REJECT','reason':'SPREAD_TOO_WIDE'}
 fee=x['fee_rate'];budget=notional/(1+fee)
 if budget<x['min_order_eur']:return {'status':'REJECT','reason':'MIN_ORDER'}
 rem=budget;qty=0
 for p,q in asks:
  take=min(rem,p*q);qty+=take/p;rem-=take
 if rem>1e-8:return {'status':'REJECT','reason':'INSUFFICIENT_ASK_DEPTH'}
 entry=budget/qty;remq=qty;proceeds=0
 for p,q in bids:
  take=min(remq,q);proceeds+=take*p;remq-=take
 if remq>1e-8:return {'status':'REJECT','reason':'INSUFFICIENT_BID_DEPTH'}
 buyimpact=entry/ask-1;sellimpact=1-proceeds/qty/bid
 if max(buyimpact,sellimpact)>.001:return {'status':'REJECT','reason':'SIZE_IMPACT_TOO_HIGH'}
 stop=x['stop'];dist=1-stop/entry
 if x['range_pct']<6:return {'status':'REJECT','reason':'STRUCTURAL_RANGE_TOO_NARROW'}
 if not 0<dist<=.10:return {'status':'REJECT','reason':'STRUCTURAL_STOP_TOO_WIDE'}
 risk=notional-qty*stop*.999*(1-fee)
 if risk>12:return {'status':'REJECT','reason':'EUR_RISK_CAP'}
 tp=entry+2*(entry-stop);reward=qty*tp*.999*(1-fee)-notional
 if reward/risk<1.5:return {'status':'REJECT','reason':'INSUFFICIENT_NET_RR'}
 return {'status':'SMALL_SIZE_EXECUTABLE','entry_vwap':entry,'risk_eur':risk,'buy_impact':buyimpact,'sell_impact':sellimpact,'spread_pct':spread*100,'roundtrip_cost_eur':notional-proceeds*(1-fee),'override_scope':'24H_VOLUME_PROXY_ONLY','exit_depth_note':'Current bid depth does not guarantee future stop execution'}

def presentation(full_ranked,delivered_pending):
 return {'immediate': [r for r in full_ranked if r.get('action')=='ACHETE_MAINTENANT'],
         'pending_alerts':[dict(e,action='REVALIDATE') for e in delivered_pending]}

if __name__=='__main__':
 x=dict(available_ts=100,book_ts=100,structure_ts=100,bids=[[.999,1000]],asks=[[1,110],[1.02,1000]],market_trading=True,confirmed=True,score=7,evidence_count=4,data_ok=True,range_pct=7,stop=.94,fee_rate=.0025,min_order_eur=5)
 assert assess(x,100,100)['status']=='SMALL_SIZE_EXECUTABLE'
 assert assess(x,150,100)['reason']=='SIZE_IMPACT_TOO_HIGH'
 assert assess(dict(x,bids=[]),100,100)['status']=='UNKNOWN'
 assert assess(dict(x,available_ts=101),100,100)['reason']=='FUTURE_INPUT'
 assert assess(x,100,200)['reason']=='STALE_INPUT'
 print('5 causal/size assertions passed')
