"""Per-market acquisition clocks. No migration invents a fresh acquisition."""
import copy
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from research.common import atomic_json, read_json, timestamp
from research.features import candles_from_response

TTL_SECONDS = 90*60
MAX_AGE_SECONDS = 3*3600


class TrendCache:
    def __init__(self, path, fetch):
        self.path, self.fetch = Path(path), fetch
        self.state = read_json(self.path, {'schema_version': 1, 'profiles': {}, 'markets': {}})
        if self.state == {}:
            self.state = {'schema_version': 1, 'profiles': {}, 'markets': {}}
        if not isinstance(self.state, dict) or not isinstance(self.state.get('profiles'), dict):
            raise ValueError('INVALID_CORRECTED_TREND_CACHE')

    def refresh(self, markets, now, force=False):
        from v4_common import daily_profile_from_candles
        profiles = self.state['profiles']
        names = []
        for name in dict.fromkeys(markets):
            old = profiles.get(name, {})
            acquired = old.get('last_valid_acquisition_ts')
            if force or acquired is None or now-acquired >= TTL_SECONDS:
                names.append(name)
        def one(name):
            try:
                r = self.fetch(name)
                cs = candles_from_response(r, '1d')
                profile = daily_profile_from_candles(cs)
                if not profile:
                    return name, None, r, 'INSUFFICIENT_HISTORY'
                if any(b['t']-a['t'] != 86400000 for a,b in zip(cs, cs[1:])):
                    return name, None, r, 'GAP_UNKNOWN'
                return name, profile, r, 'VALID'
            except Exception:
                return name, None, None, 'FETCH_FAILED'
        with ThreadPoolExecutor(max_workers=6) as pool:
            results = list(pool.map(one, names))
        for name, profile, r, status in results:
            old = profiles.setdefault(name, {})
            old.update(last_attempt_ts=now, status=status)
            if profile:
                acquired = timestamp(r['retrieved_at_utc'])
                profile.update(updated_ts=acquired, response_id=r['response_id'])
                old.update(profile=profile, last_valid_acquisition_ts=acquired,
                           response_id=r['response_id'], last_closed_candle_ts=profile['last_candle_ts'])
        evaluated_at = max([now] + [timestamp(r['retrieved_at_utc']) for _,_,r,_ in results if r])
        valid = {}
        for name, p in profiles.items():
            acquired = p.get('last_valid_acquisition_ts')
            if acquired is not None and evaluated_at-acquired > MAX_AGE_SECONDS:
                p['status'] = 'STALE'
            if p.get('profile') and acquired is not None and -30 <= evaluated_at-acquired <= MAX_AGE_SECONDS:
                valid[name] = copy.deepcopy(p['profile'])
        for name, p in valid.items():
            refs = {ref: {'valid': ref in valid, 'response_id': profiles.get(ref, {}).get('response_id'),
                          'acquired_at': profiles.get(ref, {}).get('last_valid_acquisition_ts')}
                    for ref in ('BTC-EUR', 'ETH-EUR')}
            p.update(dependencies=refs, dependencies_fresh=all(r['valid'] for r in refs.values()))
        self.state['markets'] = valid
        atomic_json(self.path, self.state)
        return copy.deepcopy(self.state)
