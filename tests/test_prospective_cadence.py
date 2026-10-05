import unittest
import json
import os
from pathlib import Path
import subprocess
import tempfile
from unittest.mock import Mock
from research.common import utc
from research.prospective_cadence import begin, start, finish, health, health_snapshot, read_health, slot_at
from scripts.prospective_wakeup import wakeup, ROOT_EVENTS


class CadenceTests(unittest.TestCase):
    def test_holes_detected_and_not_relabelled_as_backfilled(self):
        now=slot_at(20000)+400; prior=now-4*1800
        state,attempt,status=begin({},now,'a',prior)
        self.assertEqual(status['status'],'MISSED')
        self.assertEqual(len(state['missed_slots']),3)
        state,receipt,status=finish(state,attempt,now+60,{'v3':{'checked_at_utc':utc(now),'status':'OK'}})
        self.assertEqual(status['status'],'OK');self.assertEqual(status['missed_slots_count'],3)
        self.assertEqual(receipt['recovery'],'LATE_CURRENT_CAPTURE_NO_BACKFILL')
        self.assertFalse(status['historical_holes_backfilled'])
    def test_completed_window_not_collected_twice(self):
        now=slot_at(20000)+50;s,a,_=begin({},now,'a')
        s,_,_=finish(s,a,now+10,{'v3':{'checked_at_utc':utc(now),'status':'OK'}})
        _,b,_=begin(s,now+20,'b');self.assertFalse(b['run'])
        _,c,_=begin(s,now+1800,'c');self.assertTrue(c['run'])
    def test_failures_have_bounded_retries_and_old_outputs_never_complete(self):
        now=slot_at(20000)+10;s,a,_=begin({},now,'a')
        s,r,_=finish(s,a,now+20,{'v3':{'checked_at_utc':utc(now-100),'status':'OK'}})
        self.assertFalse(r['collection_complete'])
        _,b,_=begin(s,now+30,'b');self.assertEqual(b['reason'],'RETRY_COOLDOWN')
        s,b,_=begin(s,now+601,'b');self.assertTrue(b['run'])
        s,_,_=finish(s,b,now+602,{})
        _,c,_=begin(s,now+1202,'c');self.assertEqual(c['reason'],'RETRY_LIMIT')
    def test_delayed_is_distinct_from_missed_and_age_is_visible(self):
        t=slot_at(20000)
        self.assertEqual(health({},t+1)['status'],'DELAYED')
        self.assertEqual(health({},t+301)['status'],'MISSED')

    def test_silent_hours_expire_a_previously_ok_health_without_a_writer(self):
        t=slot_at(20000);state={'last_completed_slot':t,'last_valid_observation_ts':t+1}
        old=health_snapshot(health(state,t+60))
        self.assertEqual(old['status'],'SNAPSHOT_REQUIRES_REEVALUATION')
        self.assertEqual(old['current_slot_status_at_check'],'OK')
        current=health(state,t+4*1800+400)
        self.assertEqual(current['status'],'MISSED')
        self.assertEqual(current['missed_slots_count'],3)
        self.assertEqual(current['last_valid_observation_age_seconds'],7599)
        self.assertNotIn('missed_slots',state)  # read-only evaluation
        self.assertEqual(read_health(old,state,t+120)['published_health_status'],'CURRENT_HEALTH')
        expired=read_health(old,state,t+7600)
        self.assertEqual(expired['published_health_status'],'STALE_HEALTH')
        self.assertEqual(expired['published_health_age_seconds'],7540)

    def test_never_completed_monitor_still_records_closed_holes(self):
        t=slot_at(20000);state,_,_=begin({},t+1,'failed')
        status=health(state,t+2*1800+1)
        self.assertEqual(status['missed_slots_count'],2)

    def test_watchdog_workflow_run_is_terminal_even_when_collection_is_missing(self):
        dispatch=Mock();t=slot_at(20000)+400
        for event in ('workflow_run','repository_dispatch','unknown',None):
            result=wakeup({},t,event,'watchdog',dispatch)
            self.assertFalse(result['dispatch_requested'])
        dispatch.assert_not_called()
        for event in ROOT_EVENTS:
            dispatch.reset_mock();result=wakeup({},t,event,'root',dispatch)
            self.assertTrue(result['dispatch_requested']);dispatch.assert_called_once()
            self.assertIn('solaire_prospective_shadows.yml',dispatch.call_args.args[0])
        dispatch.reset_mock()
        self.assertFalse(wakeup({'last_completed_slot':slot_at(t)},t,'schedule','root',dispatch)['dispatch_requested'])
        dispatch.assert_not_called()

    def test_workflow_publishes_reservation_first_and_cannot_loop_through_watchdog(self):
        s=Path('.github/workflows/solaire_prospective_shadows.yml').read_text()
        w=Path('.github/workflows/production_scan_watchdog.yml').read_text()
        self.assertNotIn("      - 'Solaire production stale-scan watchdog'",s)
        job=w.split('  prospective-wakeup:',1)[1].split('  rescue-if-stale:',1)[0]
        self.assertIn("if: github.event_name == 'schedule' || github.event_name == 'workflow_dispatch' || github.event_name == 'push'",job)
        self.assertNotIn('send_production_buy_alert',job);self.assertNotIn('production_scan.py',job)
        self.assertLess(s.index('bash scripts/persist_prospective_reservation.sh'),s.index('run: python scripts/prepare_v3_universe.py'))
        self.assertIn("always() && steps.reservation.outcome == 'success'",s)

    def test_crash_reservation_survives_fresh_checkout_and_bounds_retries(self):
        script=str(Path('scripts/persist_prospective_reservation.sh').resolve())
        def git(cwd,*args):
            return subprocess.run(['git',*args],cwd=cwd,check=True,capture_output=True,text=True)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);remote=root/'remote.git';repo=root/'first'
            git(root,'init','--bare',str(remote));git(root,'clone',str(remote),str(repo))
            git(repo,'checkout','-b','main');git(repo,'config','user.name','test');git(repo,'config','user.email','test@example.invalid')
            (repo/'seed').write_text('seed');git(repo,'add','seed');git(repo,'commit','-m','seed');git(repo,'push','origin','main')
            t=slot_at(20000)+1;state,attempt,status=begin({},t,'crashed')
            (repo/'prospective_collection_state.json').write_text(json.dumps(state))
            (repo/'prospective_collection_health.json').write_text(json.dumps(health_snapshot(status)))
            (repo/'prospective_wakeup_receipts').mkdir()
            (repo/'prospective_wakeup_receipts/crashed.json').write_text(json.dumps(attempt))
            subprocess.run(['bash',script],cwd=repo,env={**os.environ,'GITHUB_RUN_ID':'crashed','GITHUB_RUN_ATTEMPT':'1'},check=True,capture_output=True)
            recovered=root/'retry';git(root,'clone','--branch','main',str(remote),str(recovered))
            saved=json.loads((recovered/'prospective_collection_state.json').read_text())
            self.assertEqual(begin(saved,t+30,'retry')[1]['reason'],'RESERVATION_ACTIVE')
            saved,b,_=begin(saved,t+1201,'retry')
            self.assertTrue(b['run'])
            saved,_,_=finish(saved,b,t+1202,{})
            self.assertEqual(begin(saved,t+1203,'third')[1]['reason'],'RETRY_LIMIT')

    def test_reservation_running_failure_and_retry_states_are_distinct(self):
        t=slot_at(20000)+1;s,a,h=begin({},t,'one')
        self.assertEqual(h['slot_lifecycle']['phase'],'RESERVED')
        self.assertEqual(begin(s,t+1,'two')[1]['reason'],'RESERVATION_ACTIVE')
        s,h=start(s,a,t+2);self.assertEqual(h['slot_lifecycle']['phase'],'IN_PROGRESS')
        s,_,h=finish(s,a,t+30,{})
        self.assertEqual(h['slot_lifecycle'],{'phase':'FAILED','retry_status':'RETRY_COOLDOWN'})
        self.assertEqual(health(s,t+601)['slot_lifecycle']['retry_status'],'RETRYABLE')
        s,b,_=begin(s,t+601,'two');s,_,h=finish(s,b,t+620,{})
        self.assertEqual(h['slot_lifecycle']['retry_status'],'ABANDONED_RETRY_LIMIT')
        self.assertTrue(begin(s,t+1800,'next-slot')[1]['run'])

    def test_skip_cli_records_causal_receipt_without_market_data(self):
        cli=str(Path('scripts/prospective_cycle.py').resolve())
        with tempfile.TemporaryDirectory() as tmp:
            import time
            root=Path(tmp);t=time.time()
            (root/'prospective_collection_state.json').write_text(json.dumps({'last_completed_slot':slot_at(t)}))
            subprocess.run([os.sys.executable,cli,'begin'],cwd=root,check=True,capture_output=True,
                env={**os.environ,'GITHUB_RUN_ID':'skip','GITHUB_RUN_ATTEMPT':'1','GITHUB_EVENT_NAME':'workflow_run','GITHUB_OUTPUT':str(root/'output')})
            r=json.loads((root/'prospective_wakeup_receipts/skip_1.json').read_text())
            self.assertEqual(r['reason'],'ALREADY_COMPLETE');self.assertFalse(r['run'])
            self.assertEqual(r['trigger'],'workflow_run');self.assertIn('checked_at_utc',r)
            self.assertFalse(r['market_collection_performed']);self.assertNotIn('prices',r)
