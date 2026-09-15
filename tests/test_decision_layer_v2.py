import copy
import json
from pathlib import Path
import unittest
from test_quality import observation, NOW
from research.decision_layer import BUCKET_IMMEDIATE, BUCKET_LIMIT, BUCKET_LATENT, BUCKET_REENTRY


def candidate(m='AAA-EUR', entry=None):
    o=observation();o['market']=m;o['baseline']['market']=m
    if entry is not None:
        o['baseline'].update(entry_score=entry,risk_flags=[])
        o['exclusions']=[]
    return o


class DecisionLayerV2Tests(unittest.TestCase):
    def test_unknown_entry_latent_only_with_verified_structure(self):
        from research.decision_layer_v2 import decide
        o=candidate();r=decide([o],NOW,'scan')['ranked'][0]
        self.assertEqual(r['bucket'],BUCKET_LATENT)
        self.assertIsNone(r['entry_score_measured'])
        o['features']['15m']['valid']=False
        r=decide([o],NOW,'scan')['ranked'][0]
        self.assertIsNone(r['bucket']);self.assertEqual(r['readiness'],'AWAIT_REVALIDATION')

    def test_entry_boundaries_do_not_erase_surveillance(self):
        from research.decision_layer_v2 import decide
        for value in (5.79,5.8,6.79,6.8,7.5):
            r=decide([candidate(entry=value)],NOW,'scan')['ranked'][0]
            self.assertIsNotNone(r['bucket'])
            if value>=5.8: self.assertEqual(r['bucket'],BUCKET_LIMIT)
            self.assertFalse(r['production_buy_allowed'])
            self.assertIsNone(r['trade_plan'])

    def test_negative_24h_and_weak_structure_do_not_prove_pullback(self):
        from research.decision_layer_v2 import decide
        o=candidate(entry=6.5);o['change_24h_pct']=-10
        self.assertNotEqual(decide([o],NOW,'s')['ranked'][0]['bucket'],BUCKET_REENTRY)
        o['baseline'].update(entry_mode='PULLBACK',opportunity_score=7.39)
        self.assertIsNone(decide([o],NOW,'s')['ranked'][0]['bucket'])

    def test_opportunity_only_stable_ties_and_no_future_input(self):
        from research.decision_layer_v2 import decide
        a,b=candidate('AAA-EUR'),candidate('BBB-EUR')
        b['baseline']['trend_score']=9.9
        before=copy.deepcopy([a,b])
        r=decide([b,a],NOW,'s')
        self.assertEqual([x['market'] for x in r['ranked']],['AAA-EUR','BBB-EUR'])
        self.assertEqual(r,decide([a,b],NOW,'s'))
        a['future_outcome']={'profit':999}
        self.assertEqual(r,decide([a,b],NOW,'s'))
        self.assertEqual(before[1],b)

    def test_spread_chase_and_wick_never_create_active_routes(self):
        from research.decision_layer_v2 import decide
        o=candidate(entry=8);o['baseline']['buy_ready']=True
        self.assertEqual(decide([o],NOW,'s')['ranked'][0]['bucket'],BUCKET_IMMEDIATE)
        for flag in ('WIDE_SPREAD_RISK','WIDE_SPREAD','TOO_LATE_24H'):
            o['baseline']['risk_flags']=[flag]
            r=decide([o],NOW,'s')['ranked'][0]
            self.assertNotEqual(r['bucket'],BUCKET_IMMEDIATE)
            self.assertFalse(r['production_buy_allowed'])
        o['baseline']['risk_flags']=[]
        for status in ('NORMAL','POTENTIALLY_EXPLOITABLE','WAIT_FOR_DIRECTION','DANGEROUS_STRUCTURE','UNAVAILABLE'):
            o['wick_setup']={'status':status,'reasons':[]}
            r=decide([o],NOW,'s')
            self.assertFalse(r['principles']['production_orders_enabled'])
            self.assertFalse(r['hypotheses']['support_limit']['enabled'])
            self.assertFalse(r['hypotheses']['pullback_resumption']['enabled'])

    def test_repeat_snapshot_deterministic_four_buckets_always_present(self):
        from research.decision_layer_v2 import decide
        o=candidate()
        self.assertEqual(decide([o],NOW,'s'),decide([o],NOW,'s'))
        r=decide([],NOW,'s')
        self.assertEqual(set(r['bucket_winners']),{BUCKET_IMMEDIATE,BUCKET_LIMIT,BUCKET_LATENT,BUCKET_REENTRY})

    def test_observed_pullback_requires_existing_mode_and_closed_sequence(self):
        from research.decision_layer_v2 import decide
        o=candidate(entry=6.5);o['baseline']['entry_mode']='PULLBACK'
        o['setup_evidence']={'closed_15m_tail':[{'t':int(NOW-1800)*1000,'o':101,'h':105,'l':99,'c':102,'v':1},
                                              {'t':int(NOW-900)*1000,'o':102,'h':103,'l':98,'c':100,'v':1}]}
        r=decide([o],NOW,'s')['ranked'][0]
        self.assertEqual(r['bucket'],BUCKET_REENTRY)
        self.assertIsNone(r['setup_evidence']['confirmation_event'])
        o['setup_evidence']['closed_15m_tail'][-1]['t']+=900000
        self.assertNotEqual(decide([o],NOW,'s')['ranked'][0]['bucket'],BUCKET_REENTRY)

    def test_explicit_runner_never_writes_active_outputs_or_retimes_replay(self):
        import os
        import subprocess
        import sys
        import tempfile
        from research.common import atomic_json, read_json, utc
        root=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as d:
            work=Path(d)
            active=work/'alert_candidates.json';active.write_text('ACTIVE-SENTINEL')
            scan={'scan_id':'test-scan','scan_ts':NOW,'scan_at_utc':utc(NOW),'data_policy':'CORRECTED_INPUTS_V1',
                  'stage':'SIMULATED_FIXTURE','observations':[candidate()]}
            atomic_json(work/'scan.json',scan)
            cmd=[sys.executable,str(root/'scripts/run_shadow.py'),'--journal','scan.json','--scan-id','test-scan','--version','v2']
            for _ in range(2):
                p=subprocess.run(cmd,cwd=work,capture_output=True,text=True)
                self.assertEqual(p.returncode,0,p.stderr)
                payload=read_json(work/'decision_layer_v2.json')
                if _==0: first=payload
                else: self.assertEqual(first,payload)
            self.assertEqual(active.read_text(),'ACTIVE-SENTINEL')
            self.assertEqual(len(list((work/'decision_history_v2').rglob('*.json.gz'))),1)
            cmd[cmd.index('test-scan')]='wrong-scan'
            self.assertNotEqual(subprocess.run(cmd,cwd=work,capture_output=True).returncode,0)
