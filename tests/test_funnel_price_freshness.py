import copy,unittest
from unittest.mock import patch
from scripts.capture_funnel_prices import capture
from scripts import solaire_funnel_audit as funnel
from research.common import utc

class FunnelPriceFreshnessTests(unittest.TestCase):
    def test_public_capture_never_reads_old_signal_or_calls_sender(self):
        class Client:
            def get(self,path,cache=True):
                self.path=path;self.cache=cache
                return [{'market':'CT-EUR','price':'2'},{'market':'X-USD','price':'3'}]
            def metadata(self,path):return {'retrieved_at_utc':utc(100)}
        c=Client();doc=capture(c,lambda:100)
        self.assertEqual(c.path,'/ticker/price');self.assertFalse(c.cache)
        self.assertEqual(doc['rows'],[{'market':'CT-EUR','price_eur':2}])
        self.assertIsNone(doc['underlying_trade_timestamp']);self.assertFalse(doc['affects_email'])
    def run_funnel(self,fresh):
        now=20000;outputs={}
        docs={funnel.V3_CANDIDATES:{'generated_at_utc':utc(now),'candidates':[{'market':'CT-EUR','v2_state':'BUILDING_ACCELERATION'}]},
              funnel.V31_CANDIDATES:{'generated_at_utc':utc(now),'candidates':[{'market':'CT-EUR'}]},
              funnel.UNIVERSE:{'generated_at_utc':utc(now if fresh else 1),'source':'TEST',
                              'rows':[{'market':'CT-EUR','price_eur':999}]},
              funnel.STATE:{'architecture_version':funnel.AUDIT_VERSION,'episodes':{'e':{'episode_id':'e','market':'OLD-EUR',
                            'path':'V2_REAL','active':True,'opened_ts':1,'horizon_end_ts':100,'origin_price_eur':1,
                            'peak_eur':2,'low_eur':1}},'active_by_key':{'OLD-EUR|V2_REAL':'e'}}}
        with patch.object(funnel,'read_json',side_effect=lambda p,d=None:copy.deepcopy(docs.get(p,d))),patch.object(funnel,'atomic_json',side_effect=lambda p,d:outputs.update({p:copy.deepcopy(d)})),patch.object(funnel.time,'time',return_value=now):
            self.assertEqual(funnel.main(),0)
        return outputs
    def test_stale_source_does_not_fake_current_price_or_complete_horizon(self):
        o=self.run_funnel(False);e=o[funnel.STATE]['episodes']['e']
        self.assertIsNone(e['last_price_eur']);self.assertFalse(e['fixed_horizon_complete'])
        self.assertEqual(e['fixed_horizon_status'],'CENSORED_INPUT_GAP')
        self.assertEqual(o[funnel.STATUS]['status'],'DEGRADED_INPUT_GAP')
        self.assertTrue(any(e['event_type']=='FUNNEL_INPUT_GAP' for e in o[funnel.JOURNAL]['events']))
    def test_fresh_public_prices_allow_new_measurements(self):
        o=self.run_funnel(True)
        self.assertEqual(o[funnel.STATUS]['status'],'OK');self.assertGreater(o[funnel.STATUS]['active_episode_count'],0)
