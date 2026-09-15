#!/usr/bin/env python3
"""Optional explicit-scan diagnostics with isolated, versioned candidate memory."""
import copy
from pathlib import Path
import re
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from research.common import atomic_json, read_json, timestamp, utc
from research.input_contract import digest
from research.publication import file_hash, immutable_json
from research.optional_publication import begin, seal
from research.feedback_diagnostics import POLICY, acceleration, layers
from research.feedback_loop import current_candidates, update_candidate_memory
from research.policies import FROZEN_DL1


def run(journal, scan_id):
    attempt = begin('feedback')
    current = read_json('runtime/current_scan.json', {})
    if current.get('scan_id') != scan_id or current.get('journal') != str(journal):
        raise ValueError('EXPLICIT_CURRENT_SCAN_REQUIRED')
    scan = read_json(journal)
    if scan['scan_id'] != scan_id or not re.fullmatch(r'[A-Za-z0-9_-]+', scan_id):
        raise ValueError('SCAN_ID_MISMATCH')
    data = scan['data_policy']
    if not re.fullmatch(r'[A-Z0-9_]+', data):
        raise ValueError('INVALID_DATA_POLICY')
    cutoff = timestamp(scan['input_cutoff_at_utc'])
    state_path = f'feedback_state/{POLICY}/{data}.json'
    archive = f'feedback_history/{POLICY}/{data}/{scan_id}.json'
    previous = read_json(state_path, {})
    if previous:
        prior_path = previous.get('archive_path', '')
        if not prior_path.startswith(f'feedback_history/{POLICY}/{data}/') or '..' in Path(prior_path).parts:
            raise ValueError('INVALID_MEMORY_PROVENANCE')
        prior = read_json(prior_path)
        if not prior or previous != prior['memory'] or prior['data_policy'] != data:
            raise ValueError('MEMORY_ARCHIVE_MISMATCH')
        if previous['scan_ts'] > scan['scan_ts']:
            raise ValueError('OUT_OF_ORDER_FEEDBACK_SCAN')
    sources = {str(journal): file_hash(journal)}
    if previous:
        sources[previous['archive_path']] = file_hash(previous['archive_path'])
    report = read_json(archive)
    if report:
        if report['source_snapshot_sha256'] != digest(scan):
            raise ValueError('FEEDBACK_JOURNAL_COLLISION')
        sources = report['source_files']
    else:
        observations = copy.deepcopy(scan['observations'])
        for obs in observations:
            obs['acceleration'] = acceleration(obs, cutoff)
        # Consume only a same-scan, source-verified DL1 record; never infer a
        # historically available decision by running today's classifier.
        dl = read_json('decision_layer.json', {})
        decision_path = Path('decision_history_versioned') / data / scan['scan_at_utc'][:10] / (scan_id + '.json.gz')
        recorded = read_json(decision_path)
        if (not recorded or recorded != dl or dl.get('scan_id') != scan_id or dl.get('data_policy') != data
                or dl.get('source_snapshot_sha256') != digest(scan) or not dl.get('policy_ready_at')
                or dl.get('decision_policy') != FROZEN_DL1):
            dl = {}
        else:
            sources[str(decision_path)] = file_hash(decision_path)
        decisions = {row['market']: row for row in dl.get('ranked', [])}
        candidates = current_candidates(list(decisions.values()), observations)
        for row in candidates:
            row.update(alert_eligible=False, buyable_now=False, buyability='WATCH_ONLY')
        memory = update_candidate_memory(previous, candidates, cutoff)
        memory.update(policy=POLICY, data_policy=data, scan_id=scan_id, scan_ts=scan['scan_ts'],
                      archive_path=archive, alert_policy='SHADOW_ONLY_NO_ACTIVE_ROUTE')
        ready = utc()  # Completion time, never backdated to the scan cutoff.
        report = {'schema_version': 1, 'diagnostic_policy': POLICY, 'data_policy': data,
                  'scan_id': scan_id, 'source_snapshot_sha256': digest(scan), 'source_journal': str(journal),
                  'source_files': sources,
                  'ready_at_utc': ready, 'stage': scan.get('stage', 'DEVELOPMENT_REPLAY'),
                  'active_alerts_enabled': False, 'memory': memory,
                  'accelerations': [{'market': o['market'], **o['acceleration']} for o in observations],
                  'layers': [layers(o, o['acceleration'], scan.get('policy_ready_at'), ready,
                                   decisions.get(o['market']), dl.get('policy_ready_at')) for o in observations]}
        immutable_json(archive, report)
    atomic_json(state_path, report['memory'])
    atomic_json('feedback_report.json', report)
    return seal('feedback', attempt, ['feedback_report.json', state_path, archive], sources,
                scan_id=scan_id, data_policy=data, diagnostic_policy=POLICY)


if __name__ == '__main__':
    current = read_json('runtime/current_scan.json', {})
    run(current['journal'], current['scan_id'])
