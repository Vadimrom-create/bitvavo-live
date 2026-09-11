"""Paired evaluation invariants, before any reading of performance."""
import copy
import unittest


class ComparisonTests(unittest.TestCase):
    def cycles(self):
        from research.comparison import build_cycle
        from test_quality import observation, NOW
        from research.common import utc
        o=observation()
        scan={'scan_id':'s1','scan_ts':NOW,'scan_at_utc':utc(NOW),'input_cutoff_at_utc':utc(NOW),
              'data_policy':'CORRECTED_INPUTS_V1','stage':'SIMULATED_FIXTURE','observations':[o],
              'baseline_output':{'watch':[dict(o['baseline'], action_status='WATCH')]}}
        result={'ranked':[{'market':'AAA-EUR','bucket':'LATENT'}]}
        times={p:{'policy_ready_at':NOW+1,'published_at':NOW+2,'publication_status':'PUBLISHED'} for p in ('V4','DL1','DL2')}
        return build_cycle(scan,{'DL1':result,'DL2':result},times)

    def test_identical_policies_zero_difference_and_no_duplicate_units(self):
        from research.comparison import evaluate_pairs
        c=self.cycles()
        labels={('s1','AAA-EUR'):{'status':'COMPLETE','positive':True,'first_target_at':c['cutoff']+3600}}
        a=evaluate_pairs([c],labels);b=evaluate_pairs([c,c],labels)
        self.assertEqual(a,b)
        self.assertEqual(a['paired_differences']['DL2_minus_DL1'],0)
        self.assertEqual(a['episode_count'],1)

    def test_publication_failure_is_not_a_decision_false_negative(self):
        from research.comparison import evaluate_pairs
        c=self.cycles();c['policies']['DL2']['native']['publication_status']='FAILED'
        c['policies']['DL2']['native']['published_at']=None
        labels={('s1','AAA-EUR'):{'status':'COMPLETE','positive':True,'first_target_at':c['cutoff']+3600}}
        r=evaluate_pairs([c],labels)['policies']['DL2']
        self.assertEqual(r['native']['fn_end_to_end'],1)
        self.assertEqual(r['native']['fn_decision_given_data'],0)
        self.assertEqual(r['native']['fn_components'],{'data':0,'decision':0,'integration':1})

    def test_missing_future_increases_censoring_not_fp_or_tn(self):
        from research.comparison import evaluate_pairs
        r=evaluate_pairs([self.cycles()],{})
        self.assertEqual(r['censored_episodes'],1)
        for p in r['policies'].values():
            self.assertEqual(p['native']['fp'],0)
            self.assertEqual(p['native']['tn'],0)

    def test_data_failure_attributed_once_and_does_not_change_mask_from_veto(self):
        from research.comparison import evaluate_pairs
        c=self.cycles();c['observations']['AAA-EUR']['usable_data']=False
        for p in c['policies'].values(): p['selected']=[]
        labels={('s1','AAA-EUR'):{'status':'COMPLETE','positive':True,'first_target_at':c['cutoff']+3600}}
        r=evaluate_pairs([c],labels)['policies']['DL2']['native']
        self.assertEqual(r['fn_components'],{'data':1,'decision':0,'integration':0})
        self.assertEqual(r['positive_data_denominator'],0)

    def test_native_latency_loses_window_without_delaying_other_policy(self):
        from research.comparison import evaluate_pairs
        c=self.cycles();c['policies']['DL2']['native']['published_at']=c['cutoff']+3700
        labels={('s1','AAA-EUR'):{'status':'COMPLETE','positive':True,'first_target_at':c['cutoff']+3600}}
        r=evaluate_pairs([c],labels)['policies']
        self.assertEqual(r['DL1']['native']['tp'],1)
        self.assertEqual(r['DL2']['native']['fn_end_to_end'],1)
        self.assertEqual(r['DL1']['common']['tp'],r['DL2']['common']['tp'])

    def test_missing_policy_retained_as_abstention_and_policy_states_separate(self):
        from research.comparison import build_cycle
        c=self.cycles()
        self.assertEqual(set(c['policies']),{'V4','DL1','DL2'})
        self.assertNotEqual(c['policies']['V4']['state_identity'],c['policies']['DL2']['state_identity'])

    def test_execution_never_precedes_readiness_and_wick_touch_not_certain_fill(self):
        from research.comparison import simulate_plan
        plan={'recorded_at':100,'entry_eur':100,'stop_eur':95,'tp1_eur':110,'amount':'1',
              'cost_assumptions':{'fee_rate_each_side':.0025,'slippage_rate_each_side':.001},'valid':True}
        bars=[{'t':t*1000,'o':102,'h':112,'l':99,'c':101,'v':1} for t in (300,600,900)]
        r=simulate_plan(plan,bars,available_at=601,expires_at=1200)
        self.assertGreaterEqual(r.get('first_admissible_bar',900),900)
        self.assertEqual(r['status'],'AMBIGUOUS')
        self.assertNotIn('pnl_eur',r)

    def test_portfolio_reservations_are_isolated_by_scenario(self):
        from research.comparison import reserve_plan
        states={}
        p={'valid':True,'stake_eur':250,'theoretical_loss_eur':12,'market':'AAA-EUR'}
        self.assertTrue(reserve_plan(states,'V4',p,'cycle1'))
        self.assertTrue(reserve_plan(states,'DL2',p,'cycle1'))
        self.assertFalse(reserve_plan(states,'V4',p,'cycle1'))
        self.assertEqual(states['DL2']['reserved_eur'],250)

    def test_future_inputs_rejected_and_labels_cannot_change_decisions(self):
        from research.comparison import build_cycle
        from research.common import utc
        from test_quality import observation, NOW
        o=observation();o['input_sources']['15m']['retrieved_at_utc']=utc(NOW+1)
        scan={'scan_id':'future','data_policy':'CORRECTED_INPUTS_V1','input_cutoff_at_utc':utc(NOW),'observations':[o]}
        with self.assertRaisesRegex(ValueError,'INPUT_AFTER_CUTOFF'): build_cycle(scan,{})

    def test_episode_not_restarted_by_missing_data_or_reordered_ingestion(self):
        from research.comparison import evaluate_pairs
        a=self.cycles();b=copy.deepcopy(a);b['scan_id']='s2';b['cutoff']+=300
        b['observations']['AAA-EUR']['usable_data']=False
        labels={('s1','AAA-EUR'):{'status':'COMPLETE','positive':True,'first_target_at':a['cutoff']+3600}}
        self.assertEqual(evaluate_pairs([a,b],labels),evaluate_pairs([b,a,a],labels))
        self.assertEqual(evaluate_pairs([a,b],labels)['episode_count'],1)

    def test_missing_period_remains_visible_and_data_cells_not_invented(self):
        from research.comparison import evaluate_pairs, data_contrast
        c=self.cycles();r=evaluate_pairs([c],{},missing_windows=[{'start':0,'end':300,'status':'NO_SCAN'}])
        self.assertEqual(r['coverage']['missing_reference_windows'],1)
        self.assertEqual(data_contrast([c],[],'V4')['status'],'UNAVAILABLE')
        d=copy.deepcopy(c);d['data_policy']='LEGACY_OBSERVED_V1'
        with self.assertRaisesRegex(ValueError,'SEPARATELY'): evaluate_pairs([c,d],{})

    def test_unknown_publication_is_bounded_not_reported_as_success_or_failure(self):
        from research.comparison import evaluate_pairs
        c=self.cycles();c['policies']['DL2']['native']['publication_status']='UNKNOWN'
        labels={('s1','AAA-EUR'):{'status':'COMPLETE','positive':True,'first_target_at':c['cutoff']+3600}}
        p=evaluate_pairs([c],labels)['policies']['DL2']['native']
        self.assertIsNone(p['recall']);self.assertEqual(p['recall_bounds'],[0,1])
        self.assertEqual(p['fn_end_to_end'],0)

    def test_stop_first_gap_and_costs_on_marketably_available_limit(self):
        from research.comparison import simulate_plan
        p={'valid':True,'recorded_at':0,'entry_eur':100,'stop_eur':95,'tp1_eur':110,'amount':'1',
           'cost_assumptions':{'fee_rate_each_side':.0025,'slippage_rate_each_side':.001}}
        bars=[{'t':0,'o':99,'h':101,'l':98,'c':99},{'t':300000,'o':90,'h':111,'l':89,'c':99}]
        r=simulate_plan(p,bars,available_at=0,expires_at=600)
        self.assertEqual(r['exit_reason'],'STOP');self.assertLess(r['pnl_eur'],-9)
        self.assertTrue(r['ambiguous_stop_and_target_bar'])
