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
