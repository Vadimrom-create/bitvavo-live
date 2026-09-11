"""Deterministic fabricated public transport for integration, never real observations."""
import json
import math
import sys
import time
import urllib.parse
from unittest.mock import patch

ROOT, policy = sys.argv[1:]
sys.path.insert(0, ROOT)
import pipeline
from research.http import PublicClient
from research.common import INTERVAL_MS

NOW = time.time()
MARKETS = ('AAA-EUR','BTC-EUR','ETH-EUR')


class Response:
    headers = {}
    def __init__(self, value): self.value=value
    def __enter__(self): return self
    def __exit__(self, *args): pass
    def read(self): return json.dumps(self.value).encode()


def fixture(req, **kwargs):
    u=urllib.parse.urlparse(req.full_url);path=u.path.removeprefix('/v2');q=urllib.parse.parse_qs(u.query)
    if path=='/time': data={'time':int(NOW*1000)}
    elif path=='/markets':
        data=[{'market':m,'base':m[:-4],'quote':'EUR','status':'trading','tickSize':'.01','quantityDecimals':4,
               'minOrderInQuoteAsset':'5','minOrderInBaseAsset':'.01'} for m in MARKETS]
    elif path.startswith('/ticker/'):
        data=[{'market':m,'last':'101','open':'100','high':'105','low':'95','bid':'100.99','ask':'101.01',
               'volume':'10000','volumeQuote':'1000000','timestamp':int(NOW*1000)} for m in MARKETS]
    elif path.endswith('/candles'):
        interval=q['interval'][0];n=int(q.get('limit',['100'])[0]);span=INTERVAL_MS[interval]
        end=int(NOW*1000//span)*span
        data=[[end-i*span,100,102,99,101,100+i%5] for i in range(n)]
    elif path.endswith('/book'):
        data={'market':path.split('/')[1],'bids':[['100.99','200']],'asks':[['101.01','100']]}
    elif path.endswith('/trades'): data=[]
    else: raise AssertionError('UNDECLARED_FIXTURE_ENDPOINT:'+path)
    return Response(data)

with patch('urllib.request.urlopen', side_effect=fixture), patch.object(PublicClient, 'pace', return_value=None), patch('time.time', return_value=NOW):
    pipeline.run(policy)
