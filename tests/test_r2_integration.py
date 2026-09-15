import copy
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from research.common import atomic_json, read_json, timestamp, utc
from research.feedback_diagnostics import acceleration, layers, POLICY
from research.optional_publication import begin, validate
from scripts.run_feedback import run
from scripts.live_quotes import build_snapshot, write_snapshot
from test_feedback_loop import acceleration_obs
from test_live_quotes import FakeClient, NOW as QUOTE_NOW
from test_quality import observation, NOW


def diagnostic_observation():
    o = observation()
    example = acceleration_obs()
    o['baseline'] = None
    o['data_quality'] = {'ok': False, 'reasons': ['BOOK_UNAVAILABLE']}
    for interval in ('5m', '15m'):
        o['features'][interval].update(example['features'][interval])
    return o


class R2Diagnostics(unittest.TestCase):
    def test_candle_capability_without_book_or_v4_profile(self):
        o = diagnostic_observation(); before = copy.deepcopy(o)
        self.assertTrue(acceleration(o, NOW)['detected'])
        self.assertEqual(o, before)

    def test_stale_open_missing_and_future_candle_sources_fail_closed(self):
        for problem in ('stale', 'open', 'missing', 'future', 'nonfinite'):
            o = diagnostic_observation()
            if problem == 'stale': o['input_sources']['5m']['retrieved_at_utc'] = utc(NOW-301)
            if problem == 'open': o['features']['5m']['last_closed_start_ms'] = int(NOW*1000)
            if problem == 'missing': o['input_sources'].pop('5m')
            if problem == 'future': o['input_sources']['5m']['retrieved_at_utc'] = utc(NOW+1)
            if problem == 'nonfinite': o['features']['5m']['return_4bar_pct'] = float('inf')
            with self.subTest(problem=problem):
                self.assertEqual(acceleration(o, NOW)['state'], 'DATA_UNAVAILABLE')

    def test_reconstructed_decision_has_no_historical_availability(self):
        o = diagnostic_observation(); a = acceleration(o, NOW)
        reconstructed = layers(o, a, utc(NOW), utc(NOW+10), {'bucket':'PULLBACK'})
        recorded = layers(o, a, utc(NOW), utc(NOW+10), {'bucket':'PULLBACK'}, utc(NOW+2))
        self.assertEqual(reconstructed['DL1']['provenance'], 'RECONSTRUCTED')
        self.assertIsNone(reconstructed['DL1']['available_at'])
        self.assertEqual(recorded['DL1']['provenance'], 'RECORDED_SHADOW')
        self.assertEqual(recorded['DL1']['available_at'], utc(NOW+2))
        self.assertEqual(reconstructed['ACCELERATION']['historical_availability'], 'UNKNOWN')


class R2Producers(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.previous = Path.cwd(); os.chdir(self.tmp.name)
        self.scan = dict(scan_id='scan1', scan_ts=NOW, scan_at_utc=utc(NOW),
                         input_cutoff_at_utc=utc(NOW), policy_ready_at=utc(NOW),
                         data_policy='CORRECTED_INPUTS_V1', observations=[diagnostic_observation()])
        self.journal = 'history_corrected/2027-01-15/scan1.json.gz'
        atomic_json(self.journal, self.scan)
        atomic_json('runtime/current_scan.json', dict(scan_id='scan1', journal=self.journal))

    def tearDown(self):
        os.chdir(self.previous); self.tmp.cleanup()

    def test_memory_scoped_immutable_scan_and_repeat_are_stable(self):
        before = Path(self.journal).read_bytes()
        atomic_json('candidate_memory.json', {'legacy':'must not be used'})
        run(self.journal, 'scan1')
        m = validate('feedback'); report = read_json('feedback_report.json')
        archive = Path(report['memory']['archive_path']).read_bytes()
        run(self.journal, 'scan1')
        self.assertEqual(report, read_json('feedback_report.json'))
        self.assertEqual(archive, Path(report['memory']['archive_path']).read_bytes())
        self.assertEqual(Path(self.journal).read_bytes(), before)
        self.assertEqual(read_json('candidate_memory.json'), {'legacy':'must not be used'})
        self.assertEqual(report['layers'][0]['DL1']['provenance'], 'UNKNOWN')
        self.assertTrue(any(p.startswith('feedback_state/'+POLICY+'/CORRECTED_INPUTS_V1') for p in m['outputs']))
        self.assertFalse(report['memory']['candidates'][0]['alert_eligible'])

    def test_failed_feedback_cannot_republish_previous_success(self):
        from scripts import publish_data
        run(self.journal, 'scan1')
        with patch('scripts.run_feedback.acceleration', side_effect=RuntimeError('broken')):
            # Different scan avoids intentional idempotent reuse.
            self.scan['scan_id']='scan2'; self.scan['scan_ts']+=1
            atomic_json(self.journal, self.scan)
            atomic_json('runtime/current_scan.json', dict(scan_id='scan2', journal=self.journal))
            with self.assertRaisesRegex(RuntimeError, 'broken'): run(self.journal, 'scan2')
        with patch.object(publish_data, 'publish') as publish, patch('sys.argv', ['publish_data.py','--feedback']):
            with self.assertRaisesRegex(ValueError, 'CURRENT_OPTIONAL_PRODUCTION_REQUIRED'): publish_data.main()
            publish.assert_not_called()

    def test_changed_source_and_output_refused(self):
        run(self.journal, 'scan1')
        Path(self.journal).write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError, 'OPTIONAL_SOURCE_MISMATCH'): validate('feedback')
        atomic_json(self.journal, self.scan)
        atomic_json('feedback_report.json', {})
        with self.assertRaisesRegex(ValueError, 'OPTIONAL_OUTPUT_MISMATCH'): validate('feedback')

    def test_only_verified_same_scan_dl_journal_counts_as_recorded(self):
        from research.input_contract import digest
        from research.policies import FROZEN_DL1
        dl={'scan_id':'scan1','data_policy':self.scan['data_policy'],
            'decision_policy':FROZEN_DL1, 'source_snapshot_sha256':digest(self.scan),
            'policy_ready_at':utc(NOW+2),'ranked':[{'market':'AAA-EUR','bucket':'PULLBACK','rank_score':7}]}
        atomic_json('decision_layer.json',dl)
        atomic_json('decision_history_versioned/'+self.scan['data_policy']+'/'+self.scan['scan_at_utc'][:10]+'/scan1.json.gz',dl)
        run(self.journal,'scan1')
        row=read_json('feedback_report.json')['layers'][0]['DL1']
        self.assertEqual(row['provenance'],'RECORDED_SHADOW')
        self.assertEqual(row['available_at'],utc(NOW+2))
        self.assertTrue(row['detected'])

    def test_legacy_launcher_requires_explicit_scan_and_never_uses_old_history(self):
        from scripts.run_decision_layer import main
        with patch('scripts.run_shadow.run') as shadow:
            main()
            shadow.assert_called_once_with(self.journal,'scan1','v1')
        Path('runtime/current_scan.json').unlink()
        with self.assertRaisesRegex(RuntimeError,'EXPLICIT_CURRENT_SCAN_REQUIRED'): main()

    def test_out_of_order_memory_refused(self):
        run(self.journal, 'scan1')
        self.scan['scan_id']='old'; self.scan['scan_ts']-=1
        atomic_json(self.journal, self.scan)
        atomic_json('runtime/current_scan.json', dict(scan_id='old',journal=self.journal))
        with self.assertRaisesRegex(ValueError, 'OUT_OF_ORDER'): run(self.journal, 'old')

    def test_failed_quotes_cannot_republish_previous_success(self):
        from scripts import live_quotes, publish_data
        good = build_snapshot(FakeClient(), now_fn=lambda: QUOTE_NOW)
        with patch.object(live_quotes, 'build_snapshot', return_value=good), patch('time.time',return_value=QUOTE_NOW):
            write_snapshot(); validate('quotes')
        with patch.object(live_quotes, 'build_snapshot', side_effect=RuntimeError('network')):
            with self.assertRaisesRegex(RuntimeError,'network'): write_snapshot()
        with patch.object(publish_data,'publish') as publish, patch('sys.argv',['publish_data.py','--quotes']):
            with self.assertRaisesRegex(ValueError,'CURRENT_OPTIONAL_PRODUCTION_REQUIRED'): publish_data.main()
            publish.assert_not_called()

    def test_optional_workflow_failure_does_not_gate_scan_or_monitor(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root/'.github/workflows/update.yml').read_text()
        steps = {block.split('id: ',1)[1].splitlines()[0]:block
                 for block in workflow.split('      - name: ') if 'id: ' in block}
        for name in ('feedback','quotes'):
            self.assertIn('continue-on-error: true',steps[name])
            self.assertIn('timeout-minutes:',steps[name])
        self.assertNotIn('feedback',steps['scan'])
        self.assertNotIn('git commit',steps['quotes'])
        self.assertNotIn('feedback', (root/'scripts/send_useful_alert.py').read_text())
        self.assertNotIn('research.feedback', (root/'pipeline.py').read_text())

    def test_site_removes_optional_files_when_current_producer_failed(self):
        from scripts.prepare_site import run as site
        atomic_json('scan_manifest.json', {'outputs':{}})
        Path('_site').mkdir()
        for name in ('feedback_report.json','feedback_manifest.json','live_quotes.json','quotes_manifest.json'):
            Path('_site',name).write_text('old')
        with patch.dict('os.environ', {'OUTCOME_FEEDBACK':'failure','OUTCOME_QUOTES':'failure'}):
            site()
        self.assertEqual(sorted(p.name for p in Path('_site').iterdir()),['index.html','scan_manifest.json'])

    def test_expired_quote_and_new_scan_invalidate_publication(self):
        from scripts import live_quotes
        good=build_snapshot(FakeClient(),now_fn=lambda:QUOTE_NOW)
        with patch.object(live_quotes,'build_snapshot',return_value=good): write_snapshot()
        with patch('time.time',return_value=QUOTE_NOW+31):
            with self.assertRaisesRegex(ValueError,'STALE_OPTIONAL_QUOTES'): validate('quotes')
        run(self.journal,'scan1')
        atomic_json('runtime/current_scan.json',dict(scan_id='other',journal=self.journal))
        with self.assertRaisesRegex(ValueError,'FEEDBACK_SCAN_MISMATCH'): validate('feedback')

    def test_publication_uses_isolated_checkout_and_preserves_source_head(self):
        from scripts import publish_data
        from test_publication import run as git
        remote=Path(self.tmp.name)/'remote.git'
        git('init','--bare','--initial-branch=main',str(remote),cwd='.')
        git('init','--initial-branch=main',cwd='.')
        git('config','user.name','Test',cwd='.');git('config','user.email','test@example.invalid',cwd='.')
        Path('seed').write_text('fixed code')
        git('add','seed',cwd='.');git('commit','-m','seed',cwd='.')
        git('remote','add','origin',str(remote),cwd='.');git('push','origin','main',cwd='.')
        before=git('rev-parse','HEAD',cwd='.').stdout
        run(self.journal,'scan1')
        with patch('sys.argv',['publish_data.py','--feedback']), patch.dict('os.environ',{'PUBLISH_BASE_SHA':before.strip()}):
            result=publish_data.main()
        self.assertIn('publication_confirmed_at',result)
        self.assertEqual(git('rev-parse','HEAD',cwd='.').stdout,before)
        self.assertEqual(git('show','main:feedback_report.json',cwd=remote).stdout,Path('feedback_report.json').read_text())


class R2QuoteQuality(unittest.TestCase):
    def test_nonfinite_price_and_crossed_book_reject_snapshot(self):
        for value in ('Infinity','NaN','-Infinity'):
            snap = build_snapshot(FakeClient(price=[{'market':'ETHFI-EUR','price':value}]), now_fn=lambda:QUOTE_NOW)
            self.assertFalse(snap['valid'])
        snap = build_snapshot(FakeClient(book=[{'market':'ETHFI-EUR','bid':'2','ask':'1'}]),now_fn=lambda:QUOTE_NOW)
        self.assertFalse(snap['valid'])

    def test_oldest_source_and_future_source_determine_freshness(self):
        class Staggered(FakeClient):
            def metadata(self,path,params=None):
                return {'retrieved_at_utc':utc(QUOTE_NOW-31 if path=='/ticker/price' else QUOTE_NOW)}
        self.assertFalse(build_snapshot(Staggered(),now_fn=lambda:QUOTE_NOW)['valid'])
        self.assertFalse(build_snapshot(FakeClient(retrieved=utc(QUOTE_NOW+3)),now_fn=lambda:QUOTE_NOW)['valid'])
