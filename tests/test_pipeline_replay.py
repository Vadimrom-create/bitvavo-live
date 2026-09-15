import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from research.common import read_json
from research.replay import compare
from research.policies import CORRECTED_DATA, LEGACY_DATA

ROOT=Path(__file__).resolve().parents[1]


class PipelineReplayTests(unittest.TestCase):
    include_shadow_publication = False
    def test_both_data_paths_replay_actual_consumptions_without_network(self):
        for policy in (LEGACY_DATA, CORRECTED_DATA):
            with self.subTest(policy=policy), tempfile.TemporaryDirectory() as d:
                work=Path(d)
                for f in ROOT.glob('*.py'): (work/f.name).symlink_to(f)
                (work/'v4_config.json').write_bytes((ROOT/'v4_config.json').read_bytes())
                (work/'baseline').symlink_to(ROOT/'baseline', target_is_directory=True)
                run=subprocess.run([sys.executable,str(ROOT/'tests/fixtures/public_scenario.py'),str(ROOT),policy],cwd=work,
                                   capture_output=True,text=True,env={**os.environ,'PYTHONHASHSEED':'0'},timeout=60)
                self.assertEqual(run.returncode,0,run.stderr[-2500:])
                path=next((work/'runtime').glob('replay-*.json.gz'))
                result=compare(path)
                self.assertTrue(result['reference_equals_instrumented'],result)
                self.assertTrue(result['reference_equals_recorded_live'],result)
                snapshot=read_json(path)
                self.assertTrue(snapshot['consumptions'])
                if policy==CORRECTED_DATA:
                    self.assertTrue((work/'policy_state'/policy/'v4_trend_cache.json').exists())
                    self.assertFalse((work/'v4_trend_cache.json').exists())
                if not self.include_shadow_publication:
                    continue
                current=read_json(work/'runtime/current_scan.json')
                def command(*args):
                    p=subprocess.run([sys.executable,*args],cwd=work,capture_output=True,text=True,
                                     env={**os.environ,'PYTHONPATH':str(ROOT)},timeout=60)
                    self.assertEqual(p.returncode,0,p.stderr[-3000:])
                before=(work/'alert_candidates.json').read_bytes()
                for version in (('v1','v2') if policy==CORRECTED_DATA else ('v1',)):
                    command(str(ROOT/'scripts/run_shadow.py'),'--journal',current['journal'],'--scan-id',current['scan_id'],'--version',version)
                command(str(ROOT/'scripts/run_comparison.py'),'--journal',current['journal'],'--scan-id',current['scan_id'])
                if policy==LEGACY_DATA:
                    (work/'decision_layer.md').unlink()  # A partially written optional runner must not suppress V4.
                command(str(ROOT/'scripts/prepare_publication.py'))
                self.assertEqual((work/'alert_candidates.json').read_bytes(),before)
                manifest=read_json(work/'scan_manifest.json')
                self.assertEqual(manifest['shadow_status']['DL2']['status'],'OK' if policy==CORRECTED_DATA else 'FAILED_OR_MISSING')
                self.assertEqual(manifest['shadow_status']['DL1']['status'],'OK' if policy==CORRECTED_DATA else 'FAILED_OR_MISSING')
                self.assertTrue(manifest['replay']['reference_equals_recorded_live'])
                self.assertIn(current['journal'],manifest['outputs'])
                self.assertFalse((work/'evaluation.json').exists())

                # Publish the complete sealed bundle and its observed receipt to a local bare remote.
                from test_publication import run as git
                remote=work/'remote.git'
                git('init','--bare','--initial-branch=main',str(remote),cwd=work)
                git('init','--initial-branch=main',cwd=work)
                git('config','user.name','Test',cwd=work);git('config','user.email','test@example.invalid',cwd=work)
                (work/'seed.txt').write_text('publication fixture')
                git('add','seed.txt',cwd=work);git('commit','-m','seed',cwd=work)
                git('remote','add','origin',str(remote),cwd=work);git('push','origin','main',cwd=work)
                head=git('rev-parse','HEAD',cwd=work).stdout
                command(str(ROOT/'scripts/publish_data.py'))
                self.assertEqual(git('rev-parse','HEAD',cwd=work).stdout,head)
                receipt_path='publication_history/'+Path(current['journal']).parent.name+'/'+current['scan_id']+'.json'
                import json
                receipt=json.loads(git('show','main:'+receipt_path,cwd=remote).stdout)
                self.assertEqual(receipt['status'],'PUBLISHED')
                self.assertEqual(receipt['policy_publication']['DL1'],'PUBLISHED' if policy==CORRECTED_DATA else 'FAILED')
                self.assertLessEqual(receipt['publication_started_at'],receipt['publication_confirmed_at'])
                command(str(ROOT/'scripts/run_evaluation.py'),'--root',str(work))
                evaluated=read_json(work/'comparison_report.json')['policies'][current['data_policy']]
                self.assertGreater(evaluated['episode_count'],0)
                self.assertEqual(evaluated['censored_episodes'],evaluated['episode_count'])
