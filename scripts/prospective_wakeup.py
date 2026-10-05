#!/usr/bin/env python3
"""One optional dispatch from an independent watchdog root; no market operations."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from research.common import read_json
from research.prospective_cadence import begin, health, read_health

ROOT_EVENTS = {'schedule', 'workflow_dispatch', 'push'}
TARGET = 'solaire_prospective_shadows.yml'


def wakeup(state, now, event, run_id, dispatch):
    status = health(state, now)
    # Critical recursion barrier: prospective -> watchdog(workflow_run) is terminal.
    if event not in ROOT_EVENTS:
        reason = 'NON_ROOT_EVENT_NO_DISPATCH'
    else:
        _, attempt, _ = begin(state, now, 'probe_' + str(run_id))
        reason = attempt['reason']
        if attempt['run']:
            dispatch(['gh', 'workflow', 'run', TARGET, '--ref', 'main',
                      '-f', 'wakeup_source_run=' + str(run_id),
                      '-f', 'wakeup_source_event=' + event], check=True)
    return {'health_at_check': status, 'wakeup_reason': reason,
            'dispatch_requested': reason == 'DUE', 'source_run_id': str(run_id),
            'source_event': event, 'research_only': True,
            'affects_email': False, 'orders_submitted': False}


def main():
    now = time.time()
    state = read_json('prospective_collection_state.json', {}) or {}
    result = wakeup(state, now,
                    os.environ.get('GITHUB_EVENT_NAME'), os.environ['GITHUB_RUN_ID'], subprocess.run)
    result['health_at_check'] = read_health(read_json('prospective_collection_health.json', {}) or {}, state, now)
    print(json.dumps(result))
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as out:
            out.write('### Prospective health / bounded wakeup\n\n```json\n' +
                      json.dumps(result, indent=2) + '\n```\n')


if __name__ == '__main__':
    main()
