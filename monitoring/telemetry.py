"""Private detailed timing, public aggregates only. A heartbeat is not success."""
from research.common import timestamp, freshness, finite


def percentile(values, q):
    if not values:
        return None
    values = sorted(values)
    return values[min(len(values)-1, int((len(values)-1)*q + .999999))]


def record_cycle(state, status, account, inputs, held_count, issues, now):
    metrics = state.setdefault('monitor_timing', {'successful_at': []})
    successes = metrics.setdefault('successful_at', [])
    successes[:] = [t for t in successes if t >= now-7*86400]
    assessed = sum(freshness(now=now,retrieved=q.get('retrieved_at_utc'),max_retrieval_age=90)['ok']
                   and finite(q.get('bid'),0)>0 and finite(q.get('ask'),0)>=finite(q.get('bid'),0)
                   for q,_,_ in inputs.values())
    complete = not issues and assessed == held_count and freshness(now=now,retrieved=account.get('retrieved_at_utc'),max_retrieval_age=120)['ok']
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


def record_availability(previous, status, now):
    """Public aggregate observations, never balances, symbols or order details."""
    old=previous.get('cycles',[])
    # Keep one boundary sample to measure the beginning of the seven-day window.
    older=[r for r in old if r['at']<now-7*86400]
    cycles=older[-1:]+[r for r in old if r['at']>=now-7*86400]
    successful=bool(status.get('timing',{}).get('successful_evaluation'))
    cycles.append({'at':now,'status':status.get('status','ERROR'),'successful':successful})
    times=[r['at'] for r in cycles if r['successful']]
    gaps=[b-a for a,b in zip(times,times[1:])]
    first=previous.get('first_observed_at',now)
    boundary=max(first,now-7*86400)
    interruptions=([times[0]-boundary,now-times[-1]] if times else [now-boundary])+gaps
    unconfigured=sum(max(0,b['at']-max(a['at'],boundary)) for a,b in zip(cycles,cycles[1:]) if a['status']=='UNCONFIGURED')
    complete_window=now-first>=7*86400
    slo='NOT_YET_DEMONSTRATED'
    if complete_window:
        slo='MET' if len(times)>1 and percentile(gaps,.95)<=300 and max(interruptions)<=600 else 'NOT_MET'
    return {'schema_version':1,'first_observed_at':first,'last_observed_at':now,'cycles':cycles,
            'successful_samples':len(times),'interval_p50_seconds':percentile(gaps,.5),
            'interval_p95_seconds':percentile(gaps,.95),'longest_observed_interruption_seconds':max(interruptions),
            'observed_unconfigured_seconds':unconfigured,'slo':slo,
            'private_validation':'PENDING PRIVATE CONFIGURATION' if not times else 'PROSPECTIVE_VALIDATION_PENDING',
            'duration_semantics':'state held between observations; not proof of service availability between samples'}
