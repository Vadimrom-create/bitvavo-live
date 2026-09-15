import copy
from pathlib import Path
import unittest
from research.common import read_json, utc

NOW=1800000000.


def observation():
    source={'response_id':'r15','request_started_at_utc':utc(NOW),'retrieved_at_utc':utc(NOW),
            'server_offset_seconds':0,'clock_uncertainty_seconds':0}
    return {'market':'AAA-EUR','price_eur':100,'data_policy':'CORRECTED_INPUTS_V1',
            'baseline':{'market':'AAA-EUR','opportunity_score':7.5,'trend_score':7.7,'entry_score':4.5,
                        'risk_flags':['NOT_ENTRY_ENRICHED'],'spread_pct':.1,'quote_volume_24h_eur':100000,
                        'trend_profile':{'updated_ts':NOW,'response_id':'daily', 'dependencies_fresh':True,
                                         'dependencies':{m:{'valid':True,'acquired_at':NOW,'response_id':m} for m in ('BTC-EUR','ETH-EUR')}}},
            'features':{'15m':{'valid':True,'last_closed_start_ms':int(NOW//900-1)*900000,'support_eur':95},
                        '5m':{'valid':True,'last_closed_start_ms':int(NOW//300-1)*300000}},
            'input_sources':{'15m':source,'5m':{**source,'response_id':'r5'}},
            'wick_setup':{'status':'NORMAL','reasons':[]},'exclusions':['ENTRY_INPUTS_UNAVAILABLE']}


class QualityTests(unittest.TestCase):
    def test_default_entry_unknown_does_not_destroy_independent_structure(self):
        from research.quality import assess
        o=observation();before=copy.deepcopy(o);q=assess(o,NOW)
        self.assertEqual(q['structure_state'],'VALID')
        self.assertEqual(q['entry_status'],'UNKNOWN')
        self.assertIsNone(q['entry_score_measured'])
        self.assertFalse(q['capabilities']['immediate']['available'])
        self.assertEqual(o,before)
        o['nil_match']=None;o['features']['5m']=None
        self.assertTrue(assess(o,NOW)['capabilities']['structure']['available'])

    def test_missing_required_proof_and_stale_reference_are_not_defaults(self):
        from research.quality import assess
        for change in ('daily','dependency','15m','identity'):
            o=observation()
            if change=='daily': o['baseline']['trend_profile']['updated_ts']=NOW-10801
            if change=='dependency': o['baseline']['trend_profile']['dependencies_fresh']=False
            if change=='15m': o['features']['15m']['valid']=False
            if change=='identity': o['baseline']['market']='BBB-EUR'
            with self.subTest(change=change):
                self.assertFalse(assess(o,NOW)['capabilities']['structure']['available'])

    def test_spread_severity_cannot_fall_when_spread_worsens(self):
        from research.quality import spread_diagnostic
        states=[spread_diagnostic(flags=f,value=v) for f,v in [([], .1),(['WIDE_SPREAD_RISK'], .5),(['WIDE_SPREAD'], .9),(['VERY_WIDE_SPREAD_RISK'],2)]]
        self.assertEqual([s['severity'] for s in states],sorted(s['severity'] for s in states))
        self.assertEqual([s['execution_allowed'] for s in states],[True,False,False,False])
        self.assertFalse(spread_diagnostic([],None)['execution_allowed'])

    def test_real_wick_payloads_separate_execution_from_price_rejection(self):
        from research.quality import wick_diagnostic
        for status in ('NORMAL','POTENTIALLY_EXPLOITABLE','WAIT_FOR_DIRECTION','UNAVAILABLE','DANGEROUS_STRUCTURE'):
            with self.subTest(status=status): self.assertEqual(wick_diagnostic({'status':status,'reasons':[]})['raw_status'],status)
        a=wick_diagnostic({'status':'DANGEROUS_STRUCTURE','reasons':['SPREAD_UNSUITABLE']})
        b=wick_diagnostic({'status':'DANGEROUS_STRUCTURE','reasons':['REPEATED_DIRECTIONLESS_REJECTIONS']})
        self.assertFalse(a['price_confirmation_required'])
        self.assertTrue(b['price_confirmation_required'])
        self.assertNotEqual(wick_diagnostic({'status':'UNAVAILABLE'}),wick_diagnostic({'status':'NORMAL'}))

    def test_real_historical_iost_does_not_receive_synthetic_evidence(self):
        from research.quality import assess
        root=Path(__file__).resolve().parents[1]
        found=False
        for p in sorted((root/'history/2026-09-09').glob('*.json.gz')):
            scan=read_json(p)
            for o in scan['observations']:
                if o['market']=='IOST-EUR' and 'NOT_ENTRY_ENRICHED' in (o.get('baseline') or {}).get('risk_flags',[]):
                    q=assess(o,scan['scan_ts'])
                    self.assertEqual(q['entry_status'],'UNKNOWN')
                    self.assertEqual(q['structure_state'],'UNVERIFIABLE')
                    found=True;break
            if found: break
        self.assertTrue(found)
