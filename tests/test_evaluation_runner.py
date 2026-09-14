from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from research.common import atomic_json, read_json


class EvaluationRunnerTests(unittest.TestCase):
    def test_separate_runner_matches_reference_and_leaves_sources_unchanged(self):
        from scripts.run_evaluation import run
        from research.history import connect, rebuild
        from research.evaluation import evaluate
        from test_critical import sample_scan, NOW, candles
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);s=sample_scan();s['scan_at_utc']='2026-09-11T00:00:00+00:00'
            s['candles_5m']={'TEST-EUR':candles(48,300000,int(NOW*1000))}
            p=root/'history/2026-09-11/a.json.gz';atomic_json(p,s);before=p.read_bytes()
            expected=evaluate(rebuild(root/'history',connect()))
            result=run(root,now=NOW+20000)
            self.assertEqual(result['policies']['LEGACY_OBSERVED_V1']['metrics'],expected)
            self.assertEqual(p.read_bytes(),before)
            self.assertEqual(read_json(root/'evaluation.json')['metrics'],expected)
            second=run(root,now=NOW+20000)
            self.assertEqual(second['policies'],result['policies'])
            self.assertFalse((root/'alert_candidates.json').exists())

    def test_pipeline_does_not_import_exhaustive_evaluator(self):
        import ast
        path=Path(__file__).resolve().parents[1]/'pipeline.py'
        tree=ast.parse(path.read_text())
        imports=[n for n in tree.body if isinstance(n,ast.ImportFrom)]
        self.assertFalse(any(a.name in {'evaluate','rebuild','market_control'} for n in imports for a in n.names))
