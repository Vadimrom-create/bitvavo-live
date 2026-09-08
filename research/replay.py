"""Replay the untouched reference and the instrumented V4 on identical inputs."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

from research.common import read_json, atomic_json

RUNNER = '''
import json,sys
from pathlib import Path
sys.path.insert(0,sys.argv[1])
sys.path.append(sys.argv[2])
from research.http import ReplayClient
from research.common import read_json
snapshot=read_json(sys.argv[3])
client=ReplayClient(snapshot['requests'])
import v3_common,early_detector,v4_detector,v4_stabilizer
v3_common.get_json=client.get
early_detector.main()
v4_detector.main()
v4_stabilizer.main()
'''


def replay(snapshot_path, reference=False):
    root = Path(__file__).resolve().parents[1]
    snapshot_path = Path(snapshot_path).resolve()
    snapshot = read_json(snapshot_path)
    source = root / 'baseline/v4_20260908' if reference else root
    with tempfile.TemporaryDirectory() as temp:
        for name, value in snapshot['state_before'].items():
            atomic_json(Path(temp) / name, value)
        atomic_json(Path(temp) / 'bitvavo_live.json', snapshot['live'])
        env = {**os.environ, 'PYTHONHASHSEED': '0'}
        result = subprocess.run([sys.executable, '-c', RUNNER, str(source), str(root), str(snapshot_path)],
                                cwd=temp, env=env, capture_output=True, text=True, timeout=120)
        if result.returncode:
            raise RuntimeError('baseline_replay_failed: ' + result.stderr[-1500:])
        return read_json(Path(temp) / 'v4_watch.json')


def compare(path):
    reference = replay(path, True)
    instrumented = replay(path, False)
    original = read_json(path)['expected_baseline']
    return {'reference_equals_instrumented': reference == instrumented,
            'reference_equals_recorded_live': reference == original,
            'reference_watch_count': len(reference.get('watch', []))}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('snapshot')
    args = parser.parse_args()
    comparison = compare(args.snapshot)
    print(json.dumps(comparison))
    if not all(comparison[k] for k in ('reference_equals_instrumented', 'reference_equals_recorded_live')):
        raise SystemExit(1)
