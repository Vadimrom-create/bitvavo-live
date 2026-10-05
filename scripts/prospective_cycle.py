#!/usr/bin/env python3
"""CLI lifecycle for the serial prospective workflow; never dispatches workflows."""
import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from research.common import atomic_json, read_json, timestamp, utc
from research.prospective_cadence import begin, start, finish, read_health, health_snapshot

STATE = 'prospective_collection_state.json'
HEALTH = 'prospective_collection_health.json'
ATTEMPT = 'runtime/prospective_inputs/cycle_attempt.json'
OUTPUTS = {
    'v3': 'solaire_v3_status.json', 'v3_evaluation': 'solaire_v3_evaluation_status.json',
    'v31': 'solaire_v31_status.json', 'v31_evaluation': 'solaire_v31_evaluation_status.json',
    'phase_c': 'phase_c_observation_status.json', 'funnel': 'solaire_funnel_audit_status.json',
    'policy': 'solaire_policy_challengers_status.json',
    'policy_evaluation': 'solaire_policy_challengers_evaluation_status.json',
}


def main():
    p = argparse.ArgumentParser(); p.add_argument('action', choices=['begin', 'start', 'finish', 'health'])
    args = p.parse_args(); now = time.time()
    state = read_json(STATE, {}) or {}
    if args.action == 'health':
        print(json.dumps(read_health(read_json(HEALTH, {}) or {}, state, now)))
        return 0
    if args.action == 'begin':
        prior = read_json('solaire_funnel_audit_status.json', {}) or {}
        try:
            observed = timestamp(prior.get('checked_at_utc')) if prior.get('status') == 'OK' else None
        except (TypeError, ValueError):
            observed = None
        run_id = os.environ['GITHUB_RUN_ID'] + '_' + os.environ.get('GITHUB_RUN_ATTEMPT', '1')
        state, attempt, status = begin(state, now, run_id, observed)
        attempt['scheduling_input_revision'] = os.environ.get('SOLAIRE_INPUT_SHA')
        attempt['trigger'] = os.environ.get('GITHUB_EVENT_NAME')
        attempt['checked_at_utc'] = utc(now)
        event_path = os.environ.get('GITHUB_EVENT_PATH')
        event = (read_json(event_path, {}) or {}) if event_path else {}
        upstream = event.get('workflow_run') or {}
        attempt['upstream'] = {k: upstream.get(k) for k in ('id', 'name', 'event', 'conclusion')}
        attempt['dispatch_inputs'] = event.get('inputs') or {}
        atomic_json(ATTEMPT, attempt)
        atomic_json('prospective_wakeup_receipts/' + run_id + '.json',
                    {**attempt, 'health_at_wakeup': status, 'research_only': True,
                     'market_collection_performed': False})
        with open(os.environ['GITHUB_OUTPUT'], 'a') as out:
            out.write('collect=' + str(attempt['run']).lower() + '\n')
    elif args.action == 'start':
        state, status = start(state, read_json(ATTEMPT, {}), now)
    else:
        attempt = read_json(ATTEMPT, {})
        if not attempt.get('run'):
            return 0
        attempt['input_revision'] = os.environ.get('SOLAIRE_INPUT_SHA')
        outputs = {k: read_json(path, {}) or {} for k, path in OUTPUTS.items()}
        state, receipt, status = finish(state, attempt, now, outputs)
        receipt['outputs'] = {k: {'path': path, 'checked_at_utc': outputs[k].get('checked_at_utc'),
                                'sha256': hashlib.sha256(Path(path).read_bytes()).hexdigest() if Path(path).exists() else None}
                              for k, path in OUTPUTS.items()}
        receipt['c0_pairing'] = outputs['v3'].get('c0_pairing')
        atomic_json('prospective_cycle_receipts/' + attempt['run_id'] + '.json', receipt)
        status['last_cycle'] = receipt
    atomic_json(STATE, state); atomic_json(HEALTH, health_snapshot(status))
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as out:
            out.write('### Prospective cadence — dated observation\n\n```json\n' +
                      json.dumps(status, indent=2) + '\n```\n')
    print(json.dumps(status))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
