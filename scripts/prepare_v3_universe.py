#!/usr/bin/env python3
"""Capture an inseparable neutral universe / C0 detector payload for research."""
import copy
import hashlib
import json
import os
import sys
import tempfile
import time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from research.common import atomic_json, read_json, timestamp, utc
from research.prospective_control import digest, receipt
from scripts.production_scan import run as neutral_scan
DEST = ROOT / 'runtime/prospective_inputs'
LOGIC_FILES = ('scripts/production_scan.py', 'research/production_gate.py',
               'research/production_acceleration.py', 'research/production_context.py',
               'research/features.py', 'research/risk.py')


def prepare(source, scan, now, control_source=None, *, commit='UNKNOWN', logic_hashes=None):
    control_source = control_source or {}
    try:
        age = now - timestamp(source.get('generated_at_utc'))
    except (ValueError, TypeError):
        age = None
    matched = (source.get('generated_at_utc') == control_source.get('generated_at_utc') and
               isinstance(control_source.get('tracking'), list) and isinstance(control_source.get('watch'), list))
    if age is not None and 0 <= age <= 300 and source.get('rows') and matched:
        doc = copy.deepcopy(source); control = copy.deepcopy(control_source)
        kind = 'PRODUCTION_OBSERVED'; mode = 'FRESH_PUBLISHED_NEUTRAL_INPUT'
    else:
        # Both outputs come from the same unchanged scanner invocation. There
        # is no sender, no production-state read/write inside this directory.
        prior = Path.cwd()
        with tempfile.TemporaryDirectory(prefix='solaire-neutral-shadow-') as tmp:
            try:
                os.chdir(tmp)
                scan()
                doc = read_json('production_universe_snapshot.json', {})
                control = read_json('production_alert_candidates.json', {})
            finally:
                os.chdir(prior)
        if not doc.get('rows'):
            raise RuntimeError('FRESH_NEUTRAL_INPUT_UNAVAILABLE')
        kind = 'RECOMPUTED_SHADOW'; mode = 'FRESH_NEUTRAL_RECOMPUTED_FOR_RESEARCH_ONLY'
    doc['measurement_provenance'] = {
        'mode': mode, 'original_published_age_seconds': age,
        'production_state_written': False, 'sender_called': False, 'prepared_at_utc': utc(),
    }
    manifest = {
        'kind': kind, 'logic_commit': commit, 'logic_sha256': logic_hashes or {},
        'universe_sha256': digest(doc), 'control_sha256': digest(control),
        'generated_at_utc': control.get('generated_at_utc'), 'prepared_at_utc': utc(),
        'production_payload_generated_at_utc': control_source.get('generated_at_utc'),
        'scope': 'PRODUCTION_DETECTOR_CANDIDATES_NOT_DELIVERED_BUYS',
        'research_only': True, 'published_as_production_decision': False,
        'sender_called': False, 'orders_submitted': False,
    }
    manifest['control_id'] = 'c0_' + digest(manifest)
    return doc, control, manifest


def main():
    commit = os.environ.get('SOLAIRE_INPUT_SHA', 'UNKNOWN')
    try:
        doc, control, manifest = prepare(
            read_json(ROOT/'production_universe_snapshot.json', {}), neutral_scan, time.time(),
            read_json(ROOT/'production_alert_candidates.json', {}), commit=commit,
            logic_hashes={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in LOGIC_FILES})
        code = 0
    except (ValueError, RuntimeError, OSError) as exc:
        doc = {'generated_at_utc': utc(), 'rows': [], 'status': 'DATA_UNAVAILABLE', 'reason': str(exc)}
        control = {}; manifest = {'kind': 'UNKNOWN', 'reason': str(exc), 'logic_commit': commit}; code = 1
    atomic_json(DEST/'v3_universe.json', doc)
    atomic_json(DEST/'c0_control.json', control)
    atomic_json(DEST/'c0_manifest.json', manifest)
    paired = receipt(doc, control, manifest, time.time())
    print(json.dumps({'status': doc.get('status', 'OK'), 'rows': len(doc.get('rows', [])),
                      'provenance': doc.get('measurement_provenance'), 'c0_pairing': paired}))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
