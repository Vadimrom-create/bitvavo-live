"""One serial collector, bounded retries, explicit holes. Never backfill prices."""
import copy
from research.common import timestamp, utc

PERIOD = 1800
OFFSET = 13 * 60
GRACE = 300
RETRY_DELAY = 600
MAX_ATTEMPTS_PER_SLOT = 2


def slot_at(now):
    return int((now - OFFSET) // PERIOD) * PERIOD + OFFSET


def health(state, now):
    expected = slot_at(now)
    completed = state.get('last_completed_slot')
    observation = state.get('last_valid_observation_ts')
    lag = max(0, now - expected)
    status = ('OK' if completed == expected else
              'DELAYED' if lag <= GRACE else 'MISSED')
    return {
        'schema': 'solaire_prospective_cadence_v1', 'checked_at_utc': utc(now),
        'status': status, 'expected_slot_at_utc': utc(expected),
        'last_actual_start_at_utc': state.get('last_actual_start_at_utc'),
        'last_completed_at_utc': state.get('last_completed_at_utc'),
        'last_valid_observation_at_utc': utc(observation) if observation else None,
        'last_valid_observation_age_seconds': now - observation if observation else None,
        'current_slot_delay_seconds': lag if completed != expected else 0,
        'missed_slots_count': len(state.get('missed_slots', [])),
        'missed_slots_at_utc': [utc(s) for s in state.get('missed_slots', [])],
        'expected_interval_seconds': PERIOD, 'delay_grace_seconds': GRACE,
        'historical_holes_backfilled': False, 'github_schedule_precision_guaranteed': False,
        'research_only': True, 'affects_buy_gate': False,
        'affects_email': False, 'orders_submitted': False,
    }


def begin(state, now, run_id, prior_observation=None):
    state = copy.deepcopy(state or {})
    slot = slot_at(now)
    if not state:
        state = {'monitor_started_at_utc': utc(now), 'attempts': {}, 'missed_slots': []}
        if prior_observation is not None and 0 <= prior_observation <= now:
            state['last_completed_slot'] = slot_at(prior_observation)
            state['last_valid_observation_ts'] = prior_observation
            state['bootstrap_source'] = 'PRE_MONITOR_PUBLISHED_FUNNEL_OK_NOT_A_NEW_CYCLE'
    previous = state.get('last_completed_slot', slot)
    state['missed_slots'] = sorted(set(state.get('missed_slots', [])) |
                                    set(range(previous + PERIOD, slot, PERIOD)))
    attempts = state.setdefault('attempts', {}).setdefault(str(slot), [])
    reason = ('ALREADY_COMPLETE' if state.get('last_completed_slot') == slot else
              'SAME_ATTEMPT' if any(a['run_id'] == run_id for a in attempts) else
              'RETRY_LIMIT' if len(attempts) >= MAX_ATTEMPTS_PER_SLOT else
              'RETRY_COOLDOWN' if attempts and now - attempts[-1]['started_ts'] < RETRY_DELAY else
              'DUE')
    run = reason == 'DUE'
    if run:
        attempts.append({'run_id': run_id, 'started_ts': now})
        state['last_actual_start_at_utc'] = utc(now)
    state['attempts'] = {k: v for k, v in state['attempts'].items() if int(k) >= slot - 7*86400}
    attempt = {'run_id': run_id, 'slot': slot, 'started_ts': now, 'run': run,
               'reason': reason, 'start_delay_seconds': now-slot,
               'missed_slots_before': list(state['missed_slots'])}
    return state, attempt, {**health(state, now), 'trigger_decision': reason}


def finish(state, attempt, now, outputs):
    state = copy.deepcopy(state)
    problems = []
    for name, doc in outputs.items():
        try:
            stamp = timestamp(doc.get('checked_at_utc'))
        except (TypeError, ValueError):
            stamp = None
        if stamp is None or not attempt['started_ts'] <= stamp <= now:
            problems.append(name + ':MISSING_OR_OLD_OUTPUT')
        elif doc.get('critical_error') or doc.get('status', 'OK') not in {'OK', 'OK_WITH_SOURCE_GAPS'}:
            problems.append(name + ':DEGRADED_OUTPUT')
    if not outputs:
        problems.append('NO_OUTPUTS')
    complete = not problems
    if complete:
        state['last_completed_slot'] = attempt['slot']
        state['last_completed_at_utc'] = utc(now)
        state['last_valid_observation_ts'] = timestamp(outputs['v3']['checked_at_utc'])
    receipt = {
        **attempt, 'finished_at_utc': utc(now), 'collection_complete': complete,
        'problems': problems,
        'recovery': 'LATE_CURRENT_CAPTURE_NO_BACKFILL' if complete and
                    (attempt['start_delay_seconds'] > GRACE or attempt['missed_slots_before']) else 'NONE',
        'paired_c0_comparison_complete': all(
            bool(outputs.get(k, {}).get('c0_pairing', {}).get('eligible')) for k in ('v3', 'v31', 'policy')),
        'research_only': True, 'affects_email': False, 'orders_submitted': False,
    }
    return state, receipt, health(state, now)
