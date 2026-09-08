"""Theoretical EUR plans only; no account access and no order submission."""
from __future__ import annotations

import hashlib
import json
import math
from decimal import Decimal, ROUND_DOWN

from research.common import finite

DEFAULTS = {'cash_eur': 1200, 'reserve_eur': 500, 'existing_exposure_eur': 0,
            'existing_risk_eur': 0, 'existing_positions': 0, 'max_position_eur': 250,
            'max_exposure_eur': 700, 'max_positions': 3, 'max_trade_risk_eur': 12,
            'max_portfolio_risk_eur': 24, 'fee_rate': .0025, 'slippage_rate': .001,
            'min_net_rr': 1.5, 'portfolio_state': 'THEORETICAL_NOT_ACCOUNT_BALANCE'}


def plan(row, features, meta, config=None, reserved=None):
    cfg = {**DEFAULTS, **(config or {})}
    used = reserved or {'exposure': 0, 'risk': 0, 'positions': 0}
    price = finite(row.get('ask'))
    if price is None or price <= 0 or not features.get('valid'):
        return {'valid': False, 'reason': 'MISSING_FRESH_PRICE_OR_STRUCTURE'}
    if any(finite(cfg[k]) is None or cfg[k] < 0 for k in DEFAULTS if isinstance(DEFAULTS[k], (int, float))):
        return {'valid': False, 'reason': 'INVALID_RISK_CONFIG'}
    atr = features['atr14_eur']
    # Below observed support, with a volatility buffer; widen the stop and reduce
    # size rather than clipping a structural stop to an arbitrary percentage.
    stop = min(features['support_eur'] - .5 * atr, price - 1.5 * atr)
    tick = finite(meta.get('tickSize'))
    if tick is None or tick <= 0:
        return {'valid': False, 'reason': 'MISSING_MARKET_TICK_SIZE'}
    down = lambda x: float((Decimal(str(x)) / Decimal(str(tick))).to_integral_value(rounding=ROUND_DOWN) * Decimal(str(tick)))
    entry, stop = down(price), down(stop)
    if not 0 < stop < entry or atr <= 0:
        return {'valid': False, 'reason': 'NO_STRUCTURAL_INVALIDATION'}
    unit_risk = entry - stop
    tp1, tp2 = down(entry + 2 * unit_risk), down(entry + 3 * unit_risk)
    cost = cfg['fee_rate'] + cfg['slippage_rate']
    risk_per_unit = entry * (1 + cost) - stop * (1 - cost)
    reward = tp1 * (1 - cost) - entry * (1 + cost)
    rr = reward / risk_per_unit
    if rr < cfg['min_net_rr']:
        return {'valid': False, 'reason': 'INSUFFICIENT_NET_RISK_REWARD', 'net_rr': rr}
    available_risk = min(cfg['max_trade_risk_eur'], cfg['max_portfolio_risk_eur'] - cfg['existing_risk_eur'] - used['risk'])
    notional = min(cfg['max_position_eur'], available_risk / risk_per_unit * entry,
                   (cfg['cash_eur'] - cfg['reserve_eur'] - used['exposure'] * (1 + cost)) / (1 + cost),
                   cfg['max_exposure_eur'] - cfg['existing_exposure_eur'] - used['exposure'])
    if cfg['existing_positions'] + used['positions'] >= cfg['max_positions'] or notional <= 0:
        return {'valid': False, 'reason': 'PORTFOLIO_LIMIT'}
    decimals = int(meta.get('quantityDecimals', 8))
    amount = (Decimal(str(notional)) / Decimal(str(entry))).quantize(Decimal(1).scaleb(-decimals), rounding=ROUND_DOWN)
    stake = float(amount) * entry
    minimum = finite(meta.get('minOrderInQuoteAsset'))
    min_base = finite(meta.get('minOrderInBaseAsset'), 0)
    if minimum is None or stake < minimum or float(amount) < min_base or amount <= 0:
        return {'valid': False, 'reason': 'BELOW_EXCHANGE_MINIMUM'}
    return {'valid': True, 'market': row['market'], 'side': 'buy', 'order_type': 'limit',
            'amount': format(amount, 'f'), 'entry_eur': entry, 'stop_eur': stop,
            'tp1_eur': tp1, 'tp2_eur': tp2, 'stake_eur': stake,
            'theoretical_loss_eur': float(amount) * risk_per_unit, 'net_rr_tp1': rr,
            'stop_distance_pct': unit_risk / entry * 100,
            'scenario': 'V4 setup; invalidation below recent support and ATR buffer',
            'target_note': '2R/3R scenarios, not forecasts; achievable reward not calibrated',
            'main_risk': 'Failed breakout, spread widening or gap through stop',
            'cost_assumptions': {'fee_rate_each_side': cfg['fee_rate'], 'slippage_rate_each_side': cfg['slippage_rate']},
            'portfolio_state': cfg['portfolio_state'], 'dry_run': True, 'requires_human_approval': True}


def correlation(a, b):
    a = {x['t']: x['c'] for x in a}
    b = {x['t']: x['c'] for x in b}
    times = sorted(a.keys() & b.keys())[-49:]
    pairs = [(x, y) for x, y in zip(times, times[1:]) if y - x == 900_000]
    if len(pairs) < 32:
        return None
    x = [math.log(a[y] / a[t]) for t, y in pairs]
    y = [math.log(b[y] / b[t]) for t, y in pairs]
    mx, my = sum(x) / len(x), sum(y) / len(y)
    denominator = math.sqrt(sum((v - mx) ** 2 for v in x) * sum((v - my) ** 2 for v in y))
    return sum((u - mx) * (v - my) for u, v in zip(x, y)) / denominator if denominator else None


def proposed_order(plan, scan_id):
    if not plan.get('valid'):
        raise ValueError('invalid_plan')
    order = {**plan, 'scan_id': scan_id, 'status': 'PROPOSED_REQUIRES_HUMAN_APPROVAL', 'dry_run': True}
    order['proposal_id'] = hashlib.sha256(json.dumps(order, sort_keys=True).encode()).hexdigest()[:24]
    return order


def execute(*_, dry_run=True, **__):
    if not dry_run:
        raise PermissionError('Live execution is not implemented in the public analysis pipeline. Human approval and a separately validated private executor are required.')
    return {'status': 'DRY_RUN', 'submitted': False}
