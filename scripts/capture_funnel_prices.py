#!/usr/bin/env python3
"""Fresh public prices for measurement only; never runs the production scanner."""
import argparse,hashlib,json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from research.common import atomic_json,finite,utc
from research.http import PublicClient

def capture(client,clock=time.time):
    started=clock();raw=client.get('/ticker/price',cache=False);received=clock()
    meta=client.metadata('/ticker/price')
    rows=[{'market':r['market'],'price_eur':finite(r.get('price'))} for r in raw
          if str(r.get('market','')).endswith('-EUR') and finite(r.get('price'),0)>0]
    if not rows:raise ValueError('NO_PUBLIC_EUR_PRICES')
    return {'schema':'solaire_funnel_public_prices_v1','generated_at_utc':utc(received),
            'request_started_at_utc':meta.get('request_started_at_utc') or utc(started),
            'retrieved_at_utc':meta.get('retrieved_at_utc') or utc(received),
            'source':'BITVAVO_PUBLIC_TICKER_PRICE_MEASUREMENT_ONLY',
            'price_kind':'LAST_TRADE_PRICE_AT_QUERY','underlying_trade_timestamp':None,
            'rows':rows,'raw_sha256':hashlib.sha256(json.dumps(raw,sort_keys=True).encode()).hexdigest(),
            'research_only':True,'affects_buy_gate':False,'affects_email':False,'orders_submitted':False}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',default='runtime/prospective_inputs/funnel_prices.json')
    args=parser.parse_args();dest=(ROOT/args.output).resolve()
    if not dest.is_relative_to(ROOT/'runtime/prospective_inputs'):raise ValueError('MEASUREMENT_OUTPUT_PATH_REQUIRED')
    try:doc=capture(PublicClient(timeout=10,retries=2));code=0
    except (RuntimeError,ValueError,KeyError) as exc:
        doc={'schema':'solaire_funnel_public_prices_v1','generated_at_utc':utc(),'rows':[],
             'status':'DATA_UNAVAILABLE','reason':str(exc),'research_only':True,'affects_email':False,'orders_submitted':False};code=1
    atomic_json(dest,doc);print(json.dumps({'status':doc.get('status','OK'),'rows':len(doc['rows']),'at':doc['generated_at_utc']}))
    return code
if __name__=='__main__':raise SystemExit(main())
