"""One serial collector, bounded retries, explicit holes. Never backfill prices."""
import copy
from research.common import timestamp, utc

PERIOD = 1800
OFFSET = 13 * 60
GRACE = 300
RETRY_DELAY = 600
MAX_ATTEMPTS_PER_SLOT = 2
RESERVATION_LEASE = 1200  # Same bound as the workflow timeout, never a permanent lock.


def slot_at(now):
    return int((now - OFFSET) // PERIOD) * PERIOD + OFFSET


def missed_slots(state, now):
    """Closed uncovered windows, including silence since the last writer."""
    first = state.get('last_completed_slot')
    if first is None:
        first = slot_at(timestamp(state['monitor_started_at_utc'])) if state.get('monitor_started_at_utc') else slot_at(now)
        first -= PERIOD
    return sorted(set(state.get('missed_slots', [])) |
                  set(range(first + PERIOD, slot_at(now), PERIOD)))


def health(state, now):
    expected = slot_at(now)
    completed = state.get('last_completed_slot')
    observation = state.get('last_valid_observation_ts')
    lag = max(0, now - expected)
    status = ('OK' if completed == expected else
              'DELAYED' if lag <= GRACE else 'MISSED')
    holes = missed_slots(state, now)
    return {
        'schema': 'solaire_prospective_cadence_v2', 'checked_at_utc': utc(now),
        'status': status, 'expected_slot_at_utc': utc(expected),
        'status_scope': 'CURRENT_SLOT_AT_CHECKED_AT_ONLY',
        'valid_until_utc': utc(min(now + GRACE, expected + PERIOD,
                                   expected + GRACE if status == 'DELAYED' else expected + PERIOD)),
        'requires_evaluation_on_read': True,
        'health_max_age_seconds': GRACE,
        'last_completed_slot_at_utc': utc(completed) if completed is not None else None,
        'slot_lifecycle': slot_lifecycle(state, now),
        'last_actual_start_at_utc': state.get('last_actual_start_at_utc'),
        'last_reserved_at_utc': state.get('last_reserved_at_utc'),
        'last_completed_at_utc': state.get('last_completed_at_utc'),
        'last_valid_observation_at_utc': utc(observation) if observation else None,
        'last_valid_observation_age_seconds': now - observation if observation else None,
        'current_slot_delay_seconds': lag if completed != expected else 0,
        'missed_slots_count': len(holes),
        'missed_slots_at_utc': [utc(s) for s in holes],
        'historical_coverage_status': 'GAPS_RECORDED' if holes else 'NO_KNOWN_GAPS',
        'expected_interval_seconds': PERIOD, 'delay_grace_seconds': GRACE,
        'historical_holes_backfilled': False, 'github_schedule_precision_guaranteed': False,
        'research_only': True, 'affects_buy_gate': False,
        'affects_email': False, 'orders_submitted': False,
    }


def slot_lifecycle(state, now):
    slot = slot_at(now)
    attempts = state.get('attempts', {}).get(str(slot), [])
    if state.get('last_completed_slot') == slot:
        return {'phase': 'COMPLETED', 'retry_status': 'NOT_NEEDED'}
    if not attempts:
        return {'phase': 'NOT_RESERVED', 'retry_status': 'ELIGIBLE'}
    last = attempts[-1]
    phase = last.get('phase', 'UNKNOWN_LEGACY_ATTEMPT')
    if phase in {'RESERVED', 'IN_PROGRESS'}:
        if now < last['started_ts'] + RESERVATION_LEASE:
            return {'phase': phase, 'retry_status': 'ACTIVE_LEASE',
                    'lease_expires_at_utc': utc(last['started_ts'] + RESERVATION_LEASE)}
        phase = 'INTERRUPTED_OR_UNFINISHED'
    retry = ('ABANDONED_RETRY_LIMIT' if len(attempts) >= MAX_ATTEMPTS_PER_SLOT else
             'RETRY_COOLDOWN' if now - last['started_ts'] < RETRY_DELAY else 'RETRYABLE')
    return {'phase': phase, 'retry_status': retry}


def read_health(snapshot, state, now):
    """Reevaluate at read time; the stored snapshot itself never changes with time."""
    result = health(state, now)
    try:
        age = now - timestamp(snapshot.get('checked_at_utc'))
    except (TypeError, ValueError):
        age = None
    try:
        valid_until = timestamp(snapshot.get('valid_until_utc'))
        fresh = age is not None and 0 <= age <= GRACE and now < valid_until
    except (TypeError, ValueError):
        fresh = False
    result['published_health_status'] = 'CURRENT_HEALTH' if fresh else 'STALE_HEALTH'
    result['published_health_age_seconds'] = age
    return result


def health_snapshot(status):
    """A static file must never claim to be a live OK badge."""
    return {**status, 'status': 'SNAPSHOT_REQUIRES_REEVALUATION',
            'current_slot_status_at_check': status['status'],
            'read_command': 'python scripts/prospective_cycle.py health'}


def begin(state, now, run_id, prior_observation=None):
    state = copy.deepcopy(state or {})
    slot = slot_at(now)
    if not state:
        state = {'monitor_started_at_utc': utc(now), 'attempts': {}, 'missed_slots': []}
        if prior_observation is not None and 0 <= prior_observation <= now:
            state['last_completed_slot'] = slot_at(prior_observation)
            state['last_valid_observation_ts'] = prior_observation
            state['bootstrap_source'] = 'PRE_MONITOR_PUBLISHED_FUNNEL_OK_NOT_A_NEW_CYCLE'
    state['missed_slots'] = missed_slots(state, now)
    attempts = state.setdefault('attempts', {}).setdefault(str(slot), [])
    reason = ('ALREADY_COMPLETE' if state.get('last_completed_slot') == slot else
              'SAME_ATTEMPT' if any(a['run_id'] == run_id for a in attempts) else
              'RESERVATION_ACTIVE' if slot_lifecycle(state, now)['retry_status'] == 'ACTIVE_LEASE' else
              'RETRY_LIMIT' if len(attempts) >= MAX_ATTEMPTS_PER_SLOT else
              'RETRY_COOLDOWN' if attempts and now - attempts[-1]['started_ts'] < RETRY_DELAY else
              'DUE')
    run = reason == 'DUE'
    if run:
        attempts.append({'run_id': run_id, 'started_ts': now, 'phase': 'RESERVED',
                         'reserved_at_utc': utc(now)})
        state['last_reserved_at_utc'] = utc(now)
    state['attempts'] = {k: v for k, v in state['attempts'].items() if int(k) >= slot - 7*86400}
    attempt = {'run_id': run_id, 'slot': slot, 'started_ts': now, 'run': run,
               'reason': reason, 'start_delay_seconds': now-slot,
               'missed_slots_before': list(state['missed_slots'])}
    return state, attempt, {**health(state, now), 'trigger_decision': reason}


def start(state, attempt, now):
    state = copy.deepcopy(state)
    records = state['attempts'][str(attempt['slot'])]
    record = next(r for r in records if r['run_id'] == attempt['run_id'])
    if record.get('phase') != 'RESERVED' or now >= record['started_ts'] + RESERVATION_LEASE:
        raise ValueError('NO_VALID_RESERVATION')
    record.update(phase='IN_PROGRESS', collection_started_at_utc=utc(now))
    state['last_actual_start_at_utc'] = utc(now)
    return state, health(state, now)


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
    for record in state.get('attempts', {}).get(str(attempt['slot']), []):
        if record['run_id'] == attempt['run_id']:
            record.update(phase='COMPLETED' if complete else 'FAILED',
                          finished_at_utc=utc(now), problems=problems)
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
