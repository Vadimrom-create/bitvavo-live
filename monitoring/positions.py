"""Deterministic management rules, independent of the frozen V4 ranking.

Plans are verified private inputs, not reconstructed from incomplete trade
history. These rules are uncalibrated risk-management rules, not a V5 edge claim.
"""
from __future__ import annotations

import copy
import hashlib
import json
from decimal import Decimal, ROUND_DOWN

from research.common import finite, freshness

SELL = 'VENDS'
PARTIAL = 'PRENDS PARTIELLEMENT TES PROFITS'
TRAIL = 'RELÈVE LE STOP'
BUY = 'ACHÈTE'
PRIORITY = {SELL: 0, PARTIAL: 1, TRAIL: 2, BUY: 3}


def rounded(value, step):
    return float((Decimal(str(value)) / Decimal(str(step))).to_integral_value(rounding=ROUND_DOWN) * Decimal(str(step)))


def management_event(balance, plan, quote, features, meta, orders, now):
    market = balance['symbol'] + '-EUR'
    total = finite(balance.get('amount'), 0)
    if total <= 0:
        return None, 'NO_POSITION'
    if not freshness(now=now, retrieved=quote.get('retrieved_at_utc'), max_retrieval_age=90)['ok']:
        return None, 'STALE_BOOK'
    bid, ask = finite(quote.get('bid')), finite(quote.get('ask'))
    tick = finite(meta.get('tickSize'))
    minimum = finite(meta.get('minOrderInQuoteAsset'))
    if bid is None or ask is None or not 0 < bid <= ask or tick is None or tick <= 0 or minimum is None:
        return None, 'INVALID_BOOK_OR_MARKET'
    if total * bid < minimum:
        return None, 'BELOW_ORDER_MINIMUM'
    if not isinstance(plan, dict) or not plan.get('position_id') or plan.get('verified') is not True:
        return None, 'VERIFIED_PLAN_MISSING'
    initial, cost = finite(plan.get('initial_amount')), finite(plan.get('cost_basis_eur'))
    stop = finite(plan.get('stop_eur'))
    precision = 10 ** -int(meta.get('quantityDecimals', 8))
    if initial is None or initial <= 0 or total > initial + precision or stop is None or stop <= 0:
        return None, 'POSITION_PLAN_MISMATCH'
    active = [o for o in orders if o.get('market') == market and o.get('side') == 'sell'
              and o.get('status') in {'new', 'partiallyFilled', 'awaitingTrigger'}]
    full_stops = [o for o in active if o.get('orderType') in {'stopLoss', 'stopLossLimit'}
                  and finite(o.get('amountRemaining'), 0) >= total - precision
                  and finite(o.get('triggerAmount', o.get('triggerPrice')), 0) > 0]
    # A confirmed exchange stop can tighten a plan, but never silently loosen it.
    stop = max([stop] + [finite(o.get('triggerAmount', o.get('triggerPrice'))) for o in full_stops])
    event = {'market': market, 'position_id': str(plan['position_id']), 'price_eur': bid,
             'stop_eur': stop, 'amount': total, 'requires_human_approval': True, 'dry_run': True,
             'observed_at_utc': quote['retrieved_at_utc'], 'action': None}
    if bid <= stop:
        already_pending = any(o.get('orderType') in {'market', 'stopLoss'} and
                              finite(o.get('amountRemaining'), 0) >= total - precision and
                              (o.get('orderType') == 'market' or
                               finite(o.get('triggerAmount', o.get('triggerPrice')), 0) >= bid) for o in active)
        if already_pending:
            return None, 'EQUIVALENT_EXIT_ORDER_ALREADY_OPEN'
        return {**event, 'action': SELL, 'reason': 'Le prix acheteur a franchi le stop de gestion vérifié.',
                'review_open_orders_first': bool(active), 'trigger_key': 'stop_breach'}, 'ACTION'
    if cost is None or cost <= 0:
        return None, 'VERIFIED_COST_BASIS_MISSING'
    fee = finite(plan.get('fee_rate', .0025))
    slip = finite(plan.get('slippage_rate', .001))
    fraction = finite(plan.get('tp1_fraction', .5))
    if fee is None or slip is None or not 0 <= fee <= .05 or not 0 <= slip <= .05 or fraction is None or not 0 < fraction < 1:
        return None, 'INVALID_MANAGEMENT_CONFIG'
    friction = fee + slip
    tp1 = finite(plan.get('tp1_eur'))
    realized = plan.get('tp1_done') is True or total <= initial * (1 - fraction) + precision
    if tp1 and bid >= tp1 and not realized and bid * (1 - friction) > cost * (1 + friction):
        quantity = rounded(min(total, initial * fraction), precision)
        pending_tp = any(o.get('orderType') == 'limit' and finite(o.get('price'), float('inf')) <= bid
                         and finite(o.get('amountRemaining'), 0) >= quantity - precision for o in active)
        if pending_tp:
            return None, 'EQUIVALENT_PROFIT_ORDER_ALREADY_OPEN'
        if quantity * bid >= minimum and quantity >= finite(meta.get('minOrderInBaseAsset'), 0) and (ask / bid - 1) <= .01:
            return {**event, 'action': PARTIAL, 'amount': quantity, 'target_eur': tp1,
                    'reason': 'TP1 vérifié atteint, gain estimé positif après frais et glissement.',
                    'review_open_orders_first': bool(active), 'trigger_key': 'tp1'}, 'ACTION'
    if not features.get('valid') or not freshness(now=now, retrieved=quote['retrieved_at_utc'],
            candle_start_ms=features.get('last_closed_start_ms'), interval='15m')['ok']:
        return None, 'TRAILING_STRUCTURE_UNAVAILABLE'
    atr, support = finite(features.get('atr14_eur')), finite(features.get('support_eur'))
    if atr and atr > 0 and support and features.get('last_closed_start_ms') is not None:
        candidate = rounded(min(support - .5 * atr, bid - 1.5 * atr), tick)
        if candidate - stop >= max(.5 * atr, 2 * tick) and candidate > cost * (1 + friction) / (1 - friction):
            return {**event, 'action': TRAIL, 'new_stop_eur': candidate,
                    'reason': 'Support confirmé sur bougies closes ; nouveau stop au-dessus du seuil net de rentabilité.',
                    'review_open_orders_first': bool(active), 'trigger_key': 'trail'}, 'ACTION'
    return None, 'NO_JUSTIFIED_ACTION'


def select_actions(events, state, now):
    """One action per position; exits preempt profit taking and stop changes.

    An unchanged exit/TP episode is delivered once. A stronger stop needs both
    a new level and a 1h cooldown. BUY keeps its separate V4 episode gate.
    """
    state = copy.deepcopy(state)
    deliveries = state.setdefault('deliveries', {})
    selected, seen = [], set()
    for event in sorted(events, key=lambda e: PRIORITY[e['action']]):
        key = event.get('position_id', event['market'])
        if key in seen:
            continue
        seen.add(key)
        identity = json.dumps([key, event['action'], event.get('trigger_key')], separators=(',', ':'))
        event_id = hashlib.sha256(identity.encode()).hexdigest()
        previous = deliveries.get(event_id)
        if previous:
            if event['action'] != TRAIL:
                continue
            if now - previous['sent_at'] < 3600 or event['new_stop_eur'] <= previous.get('new_stop_eur', 0):
                continue
        if event['action'] != SELL and now - state.get('last_nonurgent_sent_at', 0) < 1800:
            continue
        selected.append({**event, 'event_id': event_id})
    return selected, state


def mark_delivered(state, events, now):
    for e in events:
        state.setdefault('deliveries', {})[e['event_id']] = {'sent_at': now, 'new_stop_eur': e.get('new_stop_eur')}
    if any(e['action'] != SELL for e in events):
        state['last_nonurgent_sent_at'] = now


def message(events):
    lines = ['BITVAVO — ACTIONS À VALIDER', '']
    for e in events:
        lines += [f"{e['action']} — {e['market']}", e['reason'],
                  f"Quantité : {e['amount']:.10g} | prix observé : {e['price_eur']:.10g} €",
                  f"Stop : {e.get('new_stop_eur', e.get('stop_eur')):.10g} €"]
        if e.get('target_eur'):
            lines.append(f"Objectif : {e['target_eur']:.10g} €")
        if e.get('review_open_orders_first'):
            lines.append('Vérifie les ordres de vente existants avant de modifier la position ou le stop.')
        lines += [f"Observation UTC : {e['observed_at_utc']}", '']
    lines.append('Validation humaine requise. Aucun ordre transmis. Vérifie le carnet avant toute action.')
    return ' | '.join(dict.fromkeys(e['action'] for e in events)) + ' — Bitvavo', '\n'.join(lines)
