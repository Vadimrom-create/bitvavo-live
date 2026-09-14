import copy
import unittest
from unittest.mock import Mock, patch
from research.common import utc
from monitoring import buy_candidates as module
from monitoring.positions import BUY, SELL, select_actions
from email_alert_v4 import select_events

NOW=1800000000.


def row(m,score):
    return {'market':m,'opportunity_score':score,'entry_score':8.,'buy_ready':True,'action_status':'BUY_READY',
            'last':100.,'spread_pct':.1,'quote_volume_24h_eur':100000,'data_quality':{'ok':True}}


class BuyFallbackTests(unittest.TestCase):
    def exercise(self, *, held=None, stale=False, drift=False, correlated=False, reject_all=False, throw_first=False):
        rows=[row('AA-EUR',9),row('BB-EUR',8.8)]
        account={'retrieved_at_utc':utc(NOW-121 if stale else NOW),'orders':[],
                 'balances':[{'symbol':'EUR','available':1200}]}
        inputs={'HELD-EUR':({}, {}, [{'t':1,'c':1}])} if correlated else {}
        quote={'bid':99.99,'ask':100,'retrieved_at_utc':utc(NOW)}
        features={'valid':True,'last_closed_start_ms':int(NOW//900-1)*900000,'atr14_eur':2,'support_eur':97}
        def market_inputs(c,m,n):
            if throw_first and m=='AA-EUR': raise RuntimeError('market unavailable')
            return {**quote,'ask':101 if drift and m=='AA-EUR' else 100}, features, [{'t':1,'c':1}]
        meta={'tickSize':'.01','quantityDecimals':4,'minOrderInQuoteAsset':'5'}
        with patch.dict('os.environ',{'ALLOW_BUY_ALERTS':'true'}), patch.object(module.time,'time',return_value=NOW), \
             patch.object(module,'validate_buy_bundle',return_value={'ok':True}), \
             patch.object(module,'read_json',return_value={'generated_at_utc':utc(NOW),'watch':rows}) as read, \
             patch.object(module,'correlation',side_effect=[.9,.1] if correlated else None), \
             patch.object(module,'make_plan',return_value={'valid':False} if reject_all else {'valid':True,'entry_eur':100,'amount':'1','stop_eur':95,'tp1_eur':110}):
            events,state=module.candidates({},account,held or {},{'AA-EUR':meta,'BB-EUR':meta},inputs,[],0,0,None,market_inputs)
            if stale: read.assert_not_called()
        return [e['market'] for e in events],state

    def test_first_locally_rejected_falls_back_once(self):
        for kw in ({'drift':True},{'held':{'AA-EUR':{}}},{'correlated':True},{'throw_first':True}):
            with self.subTest(kw=kw): self.assertEqual(self.exercise(**kw)[0],['BB-EUR'])

    def test_first_valid_only_all_invalid_and_global_failure(self):
        self.assertEqual(self.exercise()[0],['AA-EUR'])
        self.assertEqual(self.exercise(reject_all=True)[0],[])
        self.assertEqual(self.exercise(stale=True)[0],[])

    def test_legacy_selector_still_returns_one(self):
        payload={'generated_at_utc':utc(NOW),'watch':[row('AA-EUR',9),row('BB-EUR',8.8)]}
        self.assertEqual([r['market'] for r in select_events(payload,{},NOW)[0]],['AA-EUR'])

    def test_final_action_boundary_caps_buys_and_prioritizes_management(self):
        events=[{'market':m,'position_id':m,'trigger_key':'buy','action':BUY} for m in ('AA-EUR','BB-EUR')]
        self.assertEqual(len(select_actions(events,{},NOW)[0]),1)
        sell={'market':'CC-EUR','position_id':'CC-EUR','trigger_key':'stop','action':SELL}
        self.assertEqual([e['action'] for e in select_actions(events+[sell],{},NOW)[0]],[SELL])

    def test_fallback_delivery_marks_only_bb_after_smtp_ack(self):
        import json
        import tempfile
        from pathlib import Path
        from cryptography.fernet import Fernet
        from monitoring.state import load_state
        from test_positions import runner
        rows=[row('AA-EUR',9),row('BB-EUR',8.8)]
        meta={'tickSize':'.01','quantityDecimals':4,'minOrderInQuoteAsset':'5'}
        class Public:
            server_offset=0
            def __init__(self, **kw): pass
            def get(self,path):
                if path=='/markets': return [dict(meta,market=m,quote='EUR',status='trading') for m in ('AA-EUR','BB-EUR')]
                return {'time':int(NOW*1000)}
        quote={'bid':99.99,'ask':100,'retrieved_at_utc':utc(NOW)}
        features={'valid':True,'last_closed_start_ms':int(NOW//900-1)*900000,'atr14_eur':2.,'support_eur':97.}
        key=Fernet.generate_key().decode()
        env=dict(ALLOW_BUY_ALERTS='true',BITVAVO_READ_API_KEY='fake',BITVAVO_READ_API_SECRET='fake',POSITION_STATE_KEY=key,
                 POSITION_PLANS_JSON='{}',ALERT_GMAIL_USER='fake',ALERT_EMAIL_TO='bellonirom@gmail.com',GMAIL_APP_PASSWORD='fake')
        def payload(path,default):
            return {'generated_at_utc':utc(NOW),'watch':rows} if path=='alert_candidates.json' else default
        with tempfile.TemporaryDirectory() as d, patch.dict('os.environ',env,clear=True), \
             patch.object(module,'validate_buy_bundle',return_value={'ok':True}), \
             patch.object(runner,'STATE',str(Path(d)/'state.json')), patch.object(runner,'PublicClient',Public), \
             patch.object(runner,'ReadOnlyAccount') as private, patch.object(runner.time,'time',return_value=NOW), \
             patch.object(module,'read_json',side_effect=payload), patch.object(runner.email_alert,'send_email') as smtp, \
             patch.object(runner,'market_inputs',side_effect=lambda c,m,n:({**quote,'ask':101 if m=='AA-EUR' else 100},features,[])):
            private.return_value.snapshot.return_value={'retrieved_at_utc':utc(NOW),'orders':[], 'balances':[{'symbol':'EUR','amount':1200,'available':1200}]}
            smtp.side_effect=RuntimeError('SMTP failed')
            with self.assertRaises(RuntimeError): runner.run({})
            self.assertFalse(load_state(runner.STATE,key)['deliveries'])
            smtp.side_effect=None;runner.run({})
            body=smtp.call_args.args[-1]
            self.assertIn('BB-EUR',body);self.assertNotIn('AA-EUR',body)
            state=load_state(runner.STATE,key)
            self.assertNotIn('last_sent_ts',state['buy_state']['markets']['AA-EUR'])
            self.assertEqual(state['buy_state']['markets']['BB-EUR']['last_sent_ts'],NOW)
