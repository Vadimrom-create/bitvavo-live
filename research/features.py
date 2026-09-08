"""Diagnostics on CLOSED candles; never fed back into the frozen V4 score."""
from __future__ import annotations

import math
import statistics

from research.common import INTERVAL_MS, finite


def closed_candles(raw, interval, now):
    duration = INTERVAL_MS[interval]
    result = {}
    for r in raw:
        if not isinstance(r, list) or len(r) < 6:
            raise ValueError('invalid_ohlcv_shape')
        vals = [finite(v) for v in r[:6]]
        if any(v is None for v in vals):
            raise ValueError('non_finite_ohlcv')
        t, o, h, l, c, v = vals
        if t != int(t) or int(t) % duration or min(o, h, l, c) <= 0 or v < 0 or h < max(o, c, l) or l > min(o, c, h):
            raise ValueError('invalid_ohlcv_values')
        if t + duration <= now * 1000:
            row = {'t': int(t), 'o': o, 'h': h, 'l': l, 'c': c, 'v': v}
            if int(t) in result and result[int(t)] != row:
                raise ValueError('conflicting_candle')
            result[int(t)] = row
    return sorted(result.values(), key=lambda r: r['t'])


def pct(a, b):
    return (a / b - 1) * 100 if b else None


def describe(cs, interval):
    if len(cs) < 25:
        return {'valid': False, 'reasons': ['INSUFFICIENT_CLOSED_CANDLES'], 'bars': len(cs)}
    duration = INTERVAL_MS[interval]
    gaps = sum(b['t'] - a['t'] != duration for a, b in zip(cs[-25:-1], cs[-24:]))
    c = [r['c'] for r in cs]
    v = [r['v'] for r in cs]
    trs = [max(b['h'] - b['l'], abs(b['h'] - a['c']), abs(b['l'] - a['c'])) for a, b in zip(cs, cs[1:])]
    atr = statistics.mean(trs[-14:])
    prev_high = max(r['h'] for r in cs[-21:-1])
    support = min(r['l'] for r in cs[-8:])
    ma = statistics.mean(c[-20:])
    wick_ratios = [(r['h'] - max(r['o'], r['c'])) / (r['h'] - r['l']) if r['h'] > r['l'] else 0 for r in cs[-8:]]
    lower_wicks = [(min(r['o'], r['c']) - r['l']) / (r['h'] - r['l']) if r['h'] > r['l'] else 0 for r in cs[-8:]]
    relative_volume = v[-1] / statistics.mean(v[-21:-1]) if sum(v[-21:-1]) else None
    vr = sum(v[-4:]) / sum(v[-8:-4]) if sum(v[-8:-4]) else None
    prior_vr = sum(v[-8:-4]) / sum(v[-12:-8]) if sum(v[-12:-8]) else None
    returns = [math.log(b / a) for a, b in zip(c[-21:-1], c[-20:])]
    return {'valid': not gaps, 'reasons': ['CANDLE_GAPS'] if gaps else [], 'bars': len(cs),
            'last_closed_start_ms': cs[-1]['t'], 'last_closed_close_ms': cs[-1]['t'] + duration,
            'last_close_eur': c[-1], 'return_1bar_pct': pct(c[-1], c[-2]),
            'return_4bar_pct': pct(c[-1], c[-5]), 'return_16bar_pct': pct(c[-1], c[-17]),
            'momentum_acceleration_pp': pct(c[-1], c[-5]) - pct(c[-5], c[-9]),
            'relative_volume': relative_volume, 'volume_4_vs_prev4': vr,
            'volume_acceleration': vr - prior_vr if vr is not None and prior_vr is not None else None,
            'atr14_eur': atr, 'atr14_pct': atr / c[-1] * 100,
            'realized_volatility_pct': statistics.pstdev(returns) * 100,
            'upper_wick_max': max(wick_ratios), 'lower_wick_max': max(lower_wicks),
            'large_wick_count': sum(x >= .8 for x in wick_ratios),
            'support_eur': support, 'breakout_reference_eur': prev_high,
            'distance_to_breakout_pct': pct(c[-1], prev_high), 'extension_ma20_pct': pct(c[-1], ma),
            'consolidation_range_pct': (max(r['h'] for r in cs[-8:]) - support) / c[-1] * 100}


def chase_risk(features, change24):
    if not features.get('valid'):
        return {'score': None, 'components': {}, 'status': 'UNAVAILABLE'}
    cap = lambda x: round(max(0, min(10, x)), 3)
    components = {
        'rise_24h': cap((finite(change24, 0) - 5) / 2),
        'breakout_extension': cap(features['distance_to_breakout_pct'] * 2),
        'local_mean_extension': cap(features['extension_ma20_pct'] * 1.5),
        'vertical_momentum': cap(features['return_4bar_pct']),
        'climactic_volume': cap(((features['relative_volume'] or 0) - 5) if features['return_1bar_pct'] > 0 else 0),
    }
    return {'score': max(components.values()), 'components': components,
            'status': 'HEURISTIC_DIAGNOSTIC_ONLY', 'affects_baseline': False}


def wick_setup(features, row):
    if not features.get('valid'):
        return {'status': 'UNAVAILABLE', 'reasons': features.get('reasons', [])}
    reasons = []
    if finite(row.get('quote_volume_24h_eur'), 0) < 30_000:
        reasons.append('LOW_LIQUIDITY')
    spread = finite(row.get('spread_pct'))
    if spread is None or spread > .4:
        reasons.append('SPREAD_UNSUITABLE')
    if features['large_wick_count'] >= 3 and features['return_4bar_pct'] <= 0:
        reasons.append('REPEATED_DIRECTIONLESS_REJECTIONS')
    if reasons:
        return {'status': 'DANGEROUS_STRUCTURE', 'reasons': reasons, 'manipulation': 'NOT_INFERRED'}
    if max(features['upper_wick_max'], features['lower_wick_max']) >= .8:
        return {'status': 'POTENTIALLY_EXPLOITABLE' if features['return_4bar_pct'] > 0 else 'WAIT_FOR_DIRECTION',
                'reasons': ['STOP_AND_RISK_REWARD_REQUIRE_VALIDATION']}
    return {'status': 'NORMAL', 'reasons': []}


def nil_match(features):
    if not features.get('valid'):
        return {'score': None, 'status': 'UNAVAILABLE'}
    components = {
        'consolidation': max(0, 2.5 - features['consolidation_range_pct'] / 4),
        'volume_building': min(2.5, max(0, (features['volume_4_vs_prev4'] or 0) - 1)),
        'near_breakout': max(0, 2.5 - abs(features['distance_to_breakout_pct'])),
        'positive_acceleration': min(2.5, max(0, features['momentum_acceleration_pp'])),
    }
    return {'score': round(sum(components.values()), 3), 'components': components,
            'status': 'UNTRAINED_STRUCTURAL_PROXY_NOT_HISTORICAL_SIMILARITY', 'affects_baseline': False}


def category(row):
    flags = set(row.get('risk_flags') or [])
    if row.get('action_status') == 'TOO_LATE' or 'CHASE_RISK' in flags or 'TOO_LATE_24H' in flags:
        return 'TOO LATE'
    if row.get('buy_ready'):
        return 'IGNITION'
    if finite(row.get('change_24h_pct'), 0) > 10:
        return 'ALREADY MOVING'
    if row.get('action_status') in {'WATCH', 'ENTRY_WINDOW'}:
        return 'PRE-IGNITION'
    return 'NO SETUP'


def score_components(row, history_before, now):
    from v4_common import liquidity_score, persistence_score
    ign, trend = row.get('ignition_score', 0), row.get('trend_score', 5)
    pers, liq = persistence_score(history_before, now), liquidity_score(row)
    ignition = {'ignition': .62 * ign, 'trend': .23 * trend, 'persistence': .10 * pers, 'liquidity': .05 * liq}
    trend_path = {'trend': .68 * trend, 'ignition': .18 * ign, 'persistence': .09 * pers, 'liquidity': .05 * liq}
    return {'scale': 10, 'ignition_path': ignition, 'trend_path': trend_path,
            'selected_path': 'ignition' if sum(ignition.values()) >= sum(trend_path.values()) else 'trend',
            'score_100': round(row.get('opportunity_score', 0) * 10, 3),
            'entry_score_10': row.get('entry_score'), 'ignition_modules': row.get('ignition_scores'),
            'new_diagnostic_weight': 0}
