"""Versioned acquisition adapter around unmodified V4 formulas and sources."""
from pathlib import Path
from research.common import INTERVAL_MS
from research.features import candles_from_response
from research.policies import CORRECTED_DATA
from research.trend_cache import TrendCache

STATE_DIRECTORY = Path('policy_state') / CORRECTED_DATA
STATE_NAMES = {'scan_history.json', 'signal_log.json', 'v4_history.json', 'v4_signal_log.json',
               'v4_trend_cache.json', 'v4_stability_state.json'}


def state_path(name, corrected):
    return STATE_DIRECTORY / name if corrected and name in STATE_NAMES else Path(name)


class CorrectedInputs:
    def __init__(self, client):
        self.client = client

    def __getattr__(self, name):
        return getattr(self.client, name)

    def get(self, path, params=None, **kwargs):
        r = self.client.capture(path, params, **kwargs)
        if path.endswith('/candles'):
            cs = candles_from_response(r, params['interval'])
            return [[c[k] for k in ('t','o','h','l','c','v')] for c in cs]
        return r['data']


def install(client):
    """Called only in a policy-isolated process (including each replay subprocess)."""
    import early_detector, v3_common, v4_common, v4_detector, v4_stabilizer
    STATE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    for module in (early_detector, v3_common, v4_common, v4_detector, v4_stabilizer):
        for name, value in list(vars(module).items()):
            if isinstance(value, Path) and str(value) in STATE_NAMES:
                setattr(module, name, state_path(str(value), True))
    def refresh(markets, now_ts, force=False):
        def fetch(market):
            return client.capture('/'+market+'/candles', {'interval':'1d','limit':95},
                                  consumer_id='v4-daily:'+market, cache=False)
        return TrendCache(state_path('v4_trend_cache.json', True), fetch).refresh(markets, now_ts, force)
    v4_detector.refresh_trend_cache = refresh
    v4_common.refresh_trend_cache = refresh
    return CorrectedInputs(client)
