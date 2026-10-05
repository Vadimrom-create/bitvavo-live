import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch
from research.common import atomic_json, utc
from research.prospective_control import receipt, digest, tag_event, paired_groups, asof
from scripts.prepare_v3_universe import prepare
from scripts.update_solaire_v3_evaluation import _summary, paired_summary


class ContemporaryControlTests(unittest.TestCase):
    def inputs(self, ts=100):
        return ({'generated_at_utc':utc(ts), 'rows':[{'market':'A-EUR','price_eur':2}]},
                {'generated_at_utc':utc(ts), 'tracking':[], 'watch':[]})

    def test_observed_production_is_copied_without_restamping_even_if_no_signal(self):
        u,c=self.inputs();before=copy.deepcopy((u,c));scan=Mock()
        neutral,control,manifest=prepare(u,scan,101,c,commit='a'*40)
        pair=receipt(neutral,control,manifest,102)
        self.assertEqual(pair['status'],'CURRENT');self.assertEqual(pair['age_seconds'],2)
        self.assertEqual(pair['kind'],'PRODUCTION_OBSERVED');scan.assert_not_called()
        self.assertEqual((u,c),before);self.assertEqual(control['generated_at_utc'],utc(100))

    def test_stale_or_mismatched_pair_recomputes_both_in_one_isolated_scan(self):
        u,c=self.inputs();before=Path.cwd();calls=[]
        def scan():
            calls.append(Path.cwd());self.assertNotEqual(Path.cwd(),before)
            fresh,control=self.inputs(1000)
            atomic_json('production_universe_snapshot.json',fresh)
            atomic_json('production_alert_candidates.json',control)
        with patch('email_alert.send_email') as email,patch('research.risk.execute') as order:
            n,p,m=prepare(u,scan,1001,c,commit='b'*40)
        self.assertEqual(len(calls),1);self.assertEqual(Path.cwd(),before)
        pair=receipt(n,p,m,1002);self.assertEqual(pair['status'],'CURRENT')
        self.assertEqual(pair['kind'],'RECOMPUTED_SHADOW');self.assertEqual(pair['age_seconds'],2)
        email.assert_not_called();order.assert_not_called()
        # Fresh but different generation cannot be labelled an observed pair.
        calls.clear();prepare(*[u,scan,101],{**c,'generated_at_utc':utc(99)},commit='b'*40)
        self.assertEqual(len(calls),1)

    def test_stale_missing_future_or_tampered_control_cannot_be_paired(self):
        u,c=self.inputs();n,p,m=prepare(u,Mock(),101,c,commit='c'*40)
        self.assertEqual(receipt(n,p,m,401)['status'],'UNKNOWN_STALE_CONTROL')
        self.assertEqual(receipt(n,p,m,99)['status'],'UNKNOWN_STALE_CONTROL')
        self.assertFalse(receipt(n,{},m,102)['eligible'])
        changed={**p,'watch':[{'market':'OTHER-EUR'}]}
        self.assertEqual(receipt(n,changed,m,102)['status'],'UNKNOWN_SNAPSHOT_MISMATCH')
        self.assertFalse(receipt(n,p,{**m,'logic_commit':'UNKNOWN'},102)['eligible'])

    def test_invalid_and_legacy_records_never_enter_paired_statistics(self):
        ev={'event_type':'X','evaluations':{'4':{'complete_horizon':True,'net_close_return_pct_est':1}}}
        valid={**copy.deepcopy(ev),'c0_pairing':{'eligible':True,'kind':'RECOMPUTED_SHADOW'}}
        invalid={**copy.deepcopy(ev),'c0_pairing':{'eligible':False,'kind':'UNKNOWN'}}
        groups=paired_groups([ev,valid,invalid])
        self.assertEqual(groups['RECOMPUTED_SHADOW'],[valid])
        self.assertEqual(_summary([invalid],'X',4)['n'],0)
        summary=paired_summary([ev,valid,invalid])
        self.assertEqual(summary['legacy_or_invalid_excluded'],2)
        self.assertEqual(summary['by_control_kind']['RECOMPUTED_SHADOW']['X']['4']['n'],1)

    def test_pairing_is_propagated_without_rewriting_old_events(self):
        old={'event_type':'OLD'};journal={'events':[old],'current_c0_pairing':{'eligible':False}}
        event={'event_type':'NEW'};tag_event(journal,event)
        self.assertNotIn('c0_pairing',old);self.assertFalse(event['c0_pairing']['eligible'])

    def test_late_consumer_and_late_event_lose_comparison_eligibility(self):
        u,c=self.inputs();n,p,m=prepare(u,Mock(),101,c,commit='c'*40)
        pair=receipt(n,p,m,102)
        self.assertTrue(asof(pair,200,n)['eligible'])
        self.assertFalse(asof(pair,401,n)['eligible'])
        e={'decision_ts':401};tag_event({'current_c0_pairing':pair},e)
        self.assertEqual(e['c0_pairing']['status'],'UNKNOWN_STALE_CONTROL')
        self.assertTrue(pair['eligible'])

    def test_workflow_has_one_lock_a_due_guard_and_no_self_trigger(self):
        s=Path('.github/workflows/solaire_prospective_shadows.yml').read_text()
        triggers=s.split('permissions:',1)[0]
        self.assertNotIn("      - 'Solaire prospective shadow measurements'",triggers)
        self.assertNotIn('workflow_dispatches',s)
        self.assertIn('group: solaire-prospective-shadow-measurements',s)
        self.assertIn('cancel-in-progress: false',s)
        self.assertEqual(s.count("if: steps.cadence.outputs.collect == 'true'"),11)
        self.assertNotIn('send_production_buy_alert.py',s)
        self.assertLess(s.index('run: python scripts/solaire_policy_challengers.py'),
                        s.index('run: python scripts/update_solaire_v3_evaluation.py'))
