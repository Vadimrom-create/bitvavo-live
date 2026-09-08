"""Chronological, censored evaluation. Missing outcomes are never negatives."""
from __future__ import annotations

import json
import math
import statistics

HORIZONS = {'15m': 900, '30m': 1800, '1h': 3600, '2h': 7200, '4h': 14400}
THRESHOLDS = (5, 10, 15, 20, 30, 40)
EVALUATION_SPEC = {
    'primary_horizon': '4h', 'primary_threshold_pct': 5, 'max_adverse_before_target_pct': 5,
    'bar_resolution_minutes': 5, 'future_start': 'first complete 5m bar starting at or after scan',
    'minimum_useful_lead_minutes': 15, 'episode_separation_minutes': 240,
    'ambiguous_bar': 'low before high; stop before target',
    'missing_outcomes': 'censored, excluded from precision/recall denominators',
    'probabilities': 'unavailable until independent out-of-sample calibration',
}


def outcome(db, obs, horizon):
    start = math.ceil(obs['ts'] * 1000 / 300_000) * 300_000
    end = start + horizon * 1000
    rows = db.execute('SELECT * FROM candles WHERE market=? AND t>=? AND t<? ORDER BY t',
                      (obs['market'], start, end)).fetchall()
    expected = horizon // 300
    if len(rows) != expected or any(r['t'] != start + i * 300_000 for i, r in enumerate(rows)):
        return {'status': 'CENSORED', 'expected_bars': expected, 'observed_bars': len(rows)}
    price = obs['price']
    if not price or price <= 0:
        return {'status': 'CENSORED', 'reason': 'MISSING_REFERENCE_PRICE'}
    low, high = price, price
    targets = {}
    for row in rows:
        low, high = min(low, row['l']), max(high, row['h'])
        for threshold in THRESHOLDS:
            key = str(threshold)
            if key not in targets and row['h'] >= price * (1 + threshold / 100):
                targets[key] = {'reached': True, 'time_to_target_minutes': (row['t'] / 1000 - obs['ts']) / 60,
                                'mae_before_target_pct': (low / price - 1) * 100}
    for threshold in THRESHOLDS:
        targets.setdefault(str(threshold), {'reached': False})
    return {'status': 'COMPLETE', 'reference_price_eur': price, 'effective_start_ms': start,
            'unobserved_first_partial_bar_seconds': start / 1000 - obs['ts'],
            'forward_return_pct': (rows[-1]['c'] / price - 1) * 100,
            'mfe_pct': (high / price - 1) * 100, 'mae_pct': (low / price - 1) * 100,
            'targets': targets}


def simulate_trade(db, obs, horizon=14400):
    data = json.loads(obs['payload'])
    plan = data.get('trade_plan') or {}
    if not plan.get('valid'):
        return {'status': 'UNAVAILABLE', 'reason': 'NO_EX_ANTE_PLAN'}
    start = math.ceil(obs['ts'] * 1000 / 300_000) * 300_000
    rows = db.execute('SELECT * FROM candles WHERE market=? AND t>=? AND t<? ORDER BY t',
                      (obs['market'], start, start + horizon * 1000)).fetchall()
    if len(rows) != horizon // 300 or any(r['t'] != start + i * 300_000 for i, r in enumerate(rows)):
        return {'status': 'CENSORED'}
    costs = plan['cost_assumptions']
    fee, slip = costs['fee_rate_each_side'], costs['slippage_rate_each_side']
    # Submitted limit is held one bar; a price gap above it is not a filled trade.
    first = rows[0]
    limit, stop, target = plan['entry_eur'], plan['stop_eur'], plan['tp1_eur']
    if first['o'] >= limit and first['l'] > limit:
        return {'status': 'UNFILLED'}
    entry = min(first['o'] * (1 + slip), limit)
    if entry <= stop:
        return {'status': 'UNFILLED', 'reason': 'GAP_INVALIDATED_BEFORE_ENTRY'}
    ambiguous = False
    exit_price, reason = rows[-1]['c'], 'HORIZON_EXIT'
    for r in rows:
        if r['l'] <= stop:
            ambiguous = r['h'] >= target
            exit_price, reason = min(stop, r['o']) * (1 - slip), 'STOP'
            break
        if r['h'] >= target:
            exit_price, reason = target * (1 - slip), 'TP1'
            break
    if reason == 'HORIZON_EXIT':
        exit_price *= 1 - slip
    pnl = float(plan['amount']) * (exit_price * (1 - fee) - entry * (1 + fee))
    return {'status': 'COMPLETE', 'pnl_eur': pnl, 'return_pct': (exit_price * (1 - fee) / (entry * (1 + fee)) - 1) * 100,
            'exit_reason': reason, 'ambiguous_stop_and_target_bar': ambiguous,
            'assumptions': 'limit available one bar, stop first on ambiguity, all size exits TP1; no portfolio compounding'}


def before_move(db, market, onset_ts, price_now=None):
    result = {}
    for label, seconds in HORIZONS.items():
        target = onset_ts - seconds
        row = db.execute('SELECT * FROM observations WHERE market=? AND ts<=? ORDER BY ts DESC LIMIT 1',
                         (market, target)).fetchone()
        if row is None or target - row['ts'] > 20 * 60:
            result[label] = {'status': 'UNOBSERVED'}
        else:
            payload = json.loads(row['payload'])
            result[label] = {'status': 'OBSERVED', 'scan_ts': row['ts'],
                             'offset_error_seconds': target - row['ts'], 'observation': payload}
    first = db.execute('SELECT * FROM observations WHERE market=? AND ts>=? AND ts<? AND detected=1 ORDER BY ts LIMIT 1',
                       (market, onset_ts - 14400, onset_ts)).fetchone()
    return {'lookbacks': result, 'first_signal_ts': first['ts'] if first else None,
            'remaining_to_current_pct': (price_now / first['price'] - 1) * 100 if first and first['price'] and price_now else None}


def market_control(db, observations, now):
    leaders = sorted([o for o in observations if o.get('change_24h_pct') is not None],
                     key=lambda o: o['change_24h_pct'], reverse=True)[:20]
    out = []
    for obs in leaders:
        market = obs['market']
        # Find a recent short-term acceleration independently from 24h rank:
        # first 5% rise from a trailing one-hour low in the last four hours.
        bars = db.execute('SELECT * FROM candles WHERE market=? AND t>=? AND t<? ORDER BY t',
                          (market, int((now - 18000) * 1000), int(now * 1000))).fetchall()
        onset = None
        for i, bar in enumerate(bars):
            if i < 12:
                continue
            prior = bars[i - 12:i]
            if any(b['t'] - a['t'] != 300_000 for a, b in zip(prior, prior[1:])):
                continue
            low = min(prior, key=lambda b: b['l'])
            if bar['h'] >= low['l'] * 1.05:
                onset = low['t'] / 1000
                break
        history = before_move(db, market, onset, obs['price_eur']) if onset else {}
        first_ts = history.get('first_signal_ts')
        observed = [r for r in history.get('lookbacks', {}).values() if r['status'] == 'OBSERVED']
        if onset is None:
            state = 'NO_CONFIRMED_SHORT_TERM_EVENT'
        elif first_ts is not None:
            state = 'DETECTED_EARLY' if onset - first_ts >= 900 else 'DETECTED_LATE'
        elif len(observed) < len(HORIZONS):
            state = 'INSUFFICIENT_HISTORY'
        elif any((r['observation'].get('exclusions') or []) for r in observed):
            state = 'EXCLUDED_BEFORE_MOVE'
        else:
            state = 'FALSE_NEGATIVE'
        out.append({'market': market, 'price_eur': obs['price_eur'], 'change_24h_pct': obs['change_24h_pct'],
                    'current_baseline_action': (obs.get('baseline') or {}).get('action_status'),
                    'event_onset_ts': onset, 'audit_state': state, **history})
    return out


def evaluate(db):
    results = {}
    diagnostics = []
    for label, seconds in HORIZONS.items():
        metrics = {str(t): {'tp': 0, 'fp': 0, 'tn': 0, 'fn': 0, 'buy_tp': 0, 'buy_fp': 0} for t in THRESHOLDS}
        complete = censored = 0
        for obs in db.execute('SELECT * FROM observations ORDER BY ts,market'):
            future = outcome(db, obs, seconds)
            if future['status'] != 'COMPLETE':
                censored += 1
                continue
            complete += 1
            for t in THRESHOLDS:
                reached = future['targets'][str(t)]
                useful = reached['reached'] and reached.get('mae_before_target_pct', -100) >= -5
                predicted = bool(obs['detected'])
                bucket = metrics[str(t)]
                bucket['tp' if predicted and useful else 'fp' if predicted else 'fn' if useful else 'tn'] += 1
                if obs['buy']:
                    bucket['buy_tp' if useful else 'buy_fp'] += 1
                if label == '4h' and t == 5 and useful and not predicted and len(diagnostics) < 30:
                    diagnostics.append({'market': obs['market'], 'scan_ts': obs['ts'],
                                        'reason': 'BASELINE_NOT_DETECTED_BEFORE_OBSERVED_GAIN',
                                        'exclusions': json.loads(obs['payload']).get('exclusions', []), 'outcome': future})
        for bucket in metrics.values():
            bucket['recall'] = bucket['tp'] / (bucket['tp'] + bucket['fn']) if bucket['tp'] + bucket['fn'] else None
            bucket['precision_detection'] = bucket['tp'] / (bucket['tp'] + bucket['fp']) if bucket['tp'] + bucket['fp'] else None
            bucket['precision_buy'] = bucket['buy_tp'] / (bucket['buy_tp'] + bucket['buy_fp']) if bucket['buy_tp'] + bucket['buy_fp'] else None
        results[label] = {'complete': complete, 'censored': censored, 'thresholds': metrics}
    # Trade/episode statistics: do not count every repeated 5m BUY as an
    # independent trade. Overlapping market episodes are separated by four hours.
    episodes, last_market = [], {}
    for obs in db.execute('SELECT * FROM observations WHERE buy=1 ORDER BY ts,market'):
        if obs['ts'] - last_market.get(obs['market'], -1e20) < 14400:
            continue
        last_market[obs['market']] = obs['ts']
        future = outcome(db, obs, 14400)
        trade = simulate_trade(db, obs)
        episodes.append({'market': obs['market'], 'ts': obs['ts'], 'future': future, 'trade': trade})
    complete_episodes = [e for e in episodes if e['future']['status'] == 'COMPLETE']
    trades = [e['trade'] for e in episodes if e['trade']['status'] == 'COMPLETE']
    return {'evaluation_spec': EVALUATION_SPEC, 'by_horizon': results,
            'observation_count': db.execute('SELECT COUNT(*) FROM observations').fetchone()[0],
            'scan_count': db.execute('SELECT COUNT(*) FROM scans').fetchone()[0],
            'false_negative_examples': diagnostics, 'buy_episodes': len(episodes),
            'complete_buy_episodes': len(complete_episodes),
            'median_buy_mae_pct': statistics.median(e['future']['mae_pct'] for e in complete_episodes) if complete_episodes else None,
            'median_buy_mfe_pct': statistics.median(e['future']['mfe_pct'] for e in complete_episodes) if complete_episodes else None,
            'theoretical_trade_count': len(trades),
            'expected_value_eur_per_filled_trade': statistics.mean(t['pnl_eur'] for t in trades) if trades else None,
            'too_late_count': db.execute("SELECT COUNT(*) FROM observations WHERE decision='TOO LATE'").fetchone()[0],
            'v4_v5_comparison': {'v4': 'MEASURING_FROZEN_POLICY', 'v5': 'NO_OPTIMIZED_POLICY_YET',
                                 'improvement_demonstrated': False, 'holdout_test': 'NOT_YET_AVAILABLE'},
            'limitations': ['Overlapping observations are not independent; use episode counts.',
                           '5m OHLC cannot reveal tick-level stop/target order or executable depth.',
                           'No calibrated probabilities or statistical superiority claim.',
                           'Old V4 signal logs are not substituted for missing decision history.']}
