"""Private detailed timing, public aggregates only. A heartbeat is not success."""
from research.common import timestamp


def percentile(values, q):
    if not values:
        return None
    values = sorted(values)
    return values[min(len(values)-1, int((len(values)-1)*q + .999999))]


def record_cycle(state, status, account, inputs, held_count, issues, now):
    metrics = state.setdefault('monitor_timing', {'successful_at': []})
    successes = metrics.setdefault('successful_at', [])
    successes[:] = [t for t in successes if t >= now-7*86400]
    assessed = len(inputs)
    complete = not issues and assessed == held_count
    if complete and (not successes or now > successes[-1]):
        successes.append(now)
    gaps = [b-a for a,b in zip(successes, successes[1:])]
    ages = [now-timestamp(q['retrieved_at_utc']) for q,_,_ in inputs.values()]
    status['timing'] = {
        'successful_evaluation': complete,
        'account_age_at_decision_seconds': now-timestamp(account['retrieved_at_utc']),
        'oldest_book_age_at_decision_seconds': max(ages, default=None),
        'coverage_fraction': assessed/held_count if held_count else 1.,
        'interval_p50_seconds': percentile(gaps, .5),
        'interval_p95_seconds': percentile(gaps, .95),
        'interval_max_seconds': max(gaps, default=None),
        'seconds_since_success': now-successes[-1] if successes else None,
        'slo': 'NOT_YET_DEMONSTRATED',
    }
