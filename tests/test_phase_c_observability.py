import copy,io,json,tempfile,unittest,urllib.error
from pathlib import Path
from unittest.mock import Mock,patch
from research.common import utc,atomic_json
from research.execution_observability import identifiers,book_evidence,capture_validation
from scripts.capture_phase_c_books import collect
from scripts.prepare_v3_universe import prepare
from scripts.solaire_v3_shadow import source_error,fetch_external_price_snapshot
from research.production_journal import record_cycle
from research.recovery_registry import register_episode

class PhaseCTests(unittest.TestCase):
    def test_two_episodes_and_stable_retry_identity(self):
        r={'market':'CT-EUR','episode':1,'episode_started_ts':100}
        a=identifiers(r,'cycle');self.assertEqual(a,identifiers(copy.deepcopy(r),'cycle'))
        self.assertNotEqual(a['episode_id'],identifiers({**r,'episode':2,'episode_started_ts':200},'cycle')['episode_id'])
        self.assertIsNone(identifiers({'market':'CT-EUR'},'cycle')['episode_id'])
    def test_entry_exit_depth_spread_cost_and_unknown_real_fill(self):
        r=book_evidence({'asks':[[10,5],[11,100]],'bids':[[9,5],[8,100]]},
                        {'request_started_at_utc':utc(99),'retrieved_at_utc':utc(100)},101)
        self.assertAlmostEqual(r['spread'],10/9-1)
        self.assertEqual(r['sizes']['50']['entry']['vwap_eur'],10)
        self.assertEqual(r['sizes']['50']['immediate_exit_estimate']['vwap_eur'],9)
        self.assertAlmostEqual(r['sizes']['50']['roundtrip_cost_eur_est'],5+.0025*(50+45))
        self.assertGreater(r['sizes']['150']['entry']['vwap_eur'],10)
        self.assertEqual(r['passive_fill_status'],'PASSIVE_FILL_UNKNOWN')
        self.assertEqual(r['c3_status'],'UNKNOWN/NO_AUTHORIZATION')
    def test_missing_bid_depth_does_not_invent_exit_cost(self):
        r=book_evidence({'asks':[[10,100]],'bids':[[9,1]]},{},100)
        self.assertIsNone(r['sizes']['50']['roundtrip_cost_eur_est'])
        self.assertEqual(r['sizes']['50']['status'],'UNKNOWN_EXIT_COST')
        self.assertIn('RESPONSE_TIMESTAMP',r['missing_data'])
    def test_pre_book_volume_rejection_stays_unknown_and_observer_failure_nonblocking(self):
        client=Mock(records=[]);row={'market':'CT-EUR','episode':1,'episode_started_ts':100}
        with tempfile.TemporaryDirectory() as d:
            e=capture_validation(row,'cycle',client,0,None,'INSUFFICIENT_EXECUTION_LIQUIDITY',110,root=d)
            raw=json.loads(Path(e['execution_evidence_path']).read_text())
            self.assertIn('BOOK_NOT_REQUESTED_OR_UNAVAILABLE',raw['execution_costs']['missing_data'])
        with patch('research.execution_observability.atomic_json',side_effect=OSError('disk full')):
            e=capture_validation(row,'cycle',client,0,None,'SPREAD_TOO_WIDE',110)
            self.assertEqual(e['evidence_status'],'UNAVAILABLE')
    def test_causal_links_propagate_without_matching_by_symbol_only(self):
        ids={'episode_id':'ep2','decision_id':'d2','signal_id':'s2','execution_observation_id':'o2'}
        payload={'generated_at_utc':utc(100),'watch':[{'market':'CT-EUR'}]}
        status={'checked_at_utc':utc(101),'rejections':[{'market':'CT-EUR','reason':'SPREAD_TOO_WIDE',**ids}]}
        j=record_cycle(payload,status,{})
        self.assertEqual(j['entries'][0]['decision_id'],'d2')
        r=register_episode({}, {'event_id':'r2','market':'CT-EUR','source_decision_id':'d2','source_episode_id':'ep2'},None,101)
        self.assertEqual(r['episodes']['r2']['source_decision_id'],'d2')
    def test_separate_shadow_book_collection_has_no_buy_or_production_mutation(self):
        registry={'episodes':{'r':{'event_id':'r','market':'CT-EUR','closed':False,'expires_at_ts':200,
                                 'first_veto_ts':90,'source_decision_id':'d'}}};before=copy.deepcopy(registry)
        class Client:
            def get(self,path,params=None,cache=True):
                assert not cache
                return {'asks':[[10,100]],'bids':[[9,100]]} if path.endswith('/book') else []
            def metadata(self,*_):return {'retrieved_at_utc':utc(100),'request_started_at_utc':utc(100)}
        with patch('email_alert.send_email') as email,patch('research.risk.execute') as order:
            rows,_=collect(registry,{},Client(),lambda:100)
            self.assertEqual(rows[0]['parent_decision_id'],'d');self.assertEqual(registry,before)
            self.assertEqual(rows[0]['c3_status'],'UNKNOWN/NO_AUTHORIZATION');email.assert_not_called();order.assert_not_called()
