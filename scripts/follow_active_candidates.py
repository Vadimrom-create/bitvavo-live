#!/usr/bin/env python3
"""Read-only post-BUY follower: public signals only, no account or order access."""
from __future__ import annotations

import json
import os
import smtplib
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from execution_probe import near_depth, trade_flow, walk_book
from research.common import atomic_json, read_json, utc
from research.http import PublicClient

SOURCE = 'production_alert_state.json'
STATE = 'production_candidate_follow_state.json'
STATUS = 'production_candidate_follow_status.json'
JOURNAL = 'production_candidate_follow_journal.json'
MAX_TARGETS = 12
TRACK_SECONDS = 72 * 3600
MAX_AGE_SECONDS = 45
NOTIFY_COOLDOWN_SECONDS = 1800


def num(value, default=None):
    try:
        value = float(value)
        return value if value == value and abs(value) != float('inf') else default
    except (ValueError, TypeError):
        return default


def register(state, source, now):
    """Track recently emailed Solaire BUY signals, never inferred holdings."""
    markets = state.setdefault('markets', {})
    incoming = []
    for market, row in (source.get('markets') or {}).items():
        sent = num(row.get('last_sent_ts'))
        entry = num(row.get('last_sent_entry_eur'))
        stop = num(row.get('last_sent_stop_eur'))
        if (not isinstance(market, str) or not market.endswith('-EUR')
                or sent is None or not 0 <= now - sent <= TRACK_SECONDS
                or entry is None or stop is None or not 0 < stop < entry):
            continue
        incoming.append((sent, market, row, entry, stop))
    incoming.sort(reverse=True)
    keep = set()
    for sent, market, row, entry, stop in incoming[:MAX_TARGETS]:
        alert_id = str(row.get('alert_id') or ('%s:%.3f' % (market, sent)))
        previous = markets.get(market)
        if previous is None or previous.get('alert_id') != alert_id:
            markets[market] = {
                'market': market, 'alert_id': alert_id, 'sent_at_ts': sent,
                'entry_eur': entry, 'stop_eur': stop,
                'profit_review_eur': num(row.get('last_sent_profit_alert_eur')),
                'status': 'ACTIVE', 'pending': None, 'pending_count': 0,
                'last_notice': None, 'last_notice_ts': 0,
                'min_seen_price': None, 'first_seen_ts': now,
            }
        keep.add(market)
    for market in list(markets):
        if market not in keep:
            del markets[market]
    return markets


def validated_levels(book):
    if not isinstance(book, dict):
        raise ValueError('BOOK_MISSING')
    bids = [(num(a[0]), num(a[1])) for a in book.get('bids', [])[:100]]
    asks = [(num(a[0]), num(a[1])) for a in book.get('asks', [])[:100]]
    if (not bids or not asks or
        any(p is None or q is None or p <= 0 or q <= 0 for p, q in bids + asks)):
        raise ValueError('BOOK_INVALID')
    if (bids[0][0] >= asks[0][0] or
        any(bids[i][0] > bids[i-1][0] for i in range(1, len(bids))) or
        any(asks[i][0] < asks[i-1][0] for i in range(1, len(asks))):
        raise ValueError('BOOK_CROSSED_OR_UNSORTED')
    return bids, asks


def observe(client, market, now):
    """Three direct, uncached public Bitvavo requests per candidate."""
    book = client.get('/' + market + '/book', {'depth': 100}, cache=False)
    book_time = time.time()
    bids, asks = validated_levels(book)
    trades = client.get('/' + market + '/trades', {'limit': 100}, cache=False)
    trades_time = time.time()
    candles = client.get('/' + market + '/candles', {'interval': '5m', 'limit': 20}, cache=False)
    if not isinstance(trades, list) or not isinstance(candles, list):
        raise ValueError('TRADES_OR_CANDLES_MISSING')
    closed = sorted(
        [c for c in candles if isinstance(c, list) and len(c) >= 6
         and num(c[0]) is not None and num(c[0]) + 300000 <= now * 1000],
        key=lambda c: c[0])
    if len(closed) < 8:
        raise ValueError('INSUFFICIENT_CLOSED_CANDLES')
    timed = [t for t in trades if isinstance(t, dict) and num(t.get('timestamp')) is not None]
    recent = max(timed, key=lambda t: num(t['timestamp'])) if timed else None
    age = (now * 1000 - num(recent['timestamp'])) / 1000 if recent else None
    if (book_time - now > MAX_AGE_SECONDS or age is None
            or age > 900 or age < -30):
        raise ValueError('STALE_OR_EMPTY_PUBLIC_TRADES')
    bid, ask = bids[0][0], asks[0][0]
    mid = (bid + ask) / 2
    flow = trade_flow(trades)
    depth = near_depth(bids, asks, mid).get('within_1pct') or {}
    hist_vol = [num(c[5], 0) for c in closed[-13:-1]]
    median_vol = sorted(hist_vol)[len(hist_vol)//2] if hist_vol else 0
    buy, sell = walk_book(asks, 150, 'buy'), walk_book(bids, 150, 'sell')
    return {
        'market': market, 'source': 'BITVAVO_PUBLIC_REST',
        'observed_at_utc': utc(book_time),
        'trades_observed_at_utc': utc(trades_time),
        'bid': bid, 'ask': ask,
        'spread_pct': round((ask-bid)/mid*100, 4),
        'buy_taker_share': flow.get('buy_taker_share'),
        'trades_sampled': len(trades),
        'latest_trade_age_seconds': round(age, 1),
        'bid_depth_1pct_eur': depth.get('bid_notional_eur'),
        'ask_depth_1pct_eur': depth.get('ask_notional_eur'),
        'buy_150_eur_vwap': buy.get('avg_price'),
        'sell_150_eur_vwap': sell.get('avg_price'),
        'buy_150_complete': buy.get('complete_in_depth'),
        'sell_150_complete': sell.get('complete_in_depth'),
        'volume_ratio_5m': round(num(closed[-1][5], 0)/median_vol, 3) if median_vol > 0 else None,
        'two_green_5m': all(num(c[4], 0) > num(c[1], 0) for c in closed[-2:]),
        'two_red_5m': all(num(c[4], 0) < num(c[1], 0) for c in closed[-2:]),
        'last_closed_5m_utc': utc(num(closed[-1][0])/1000),
        'research_only': True, 'orders_submitted': False,
    }


def classify(item, obs):
    entry, stop, price = item['entry_eur'], item['stop_eur'], obs['bid']
    share = num(obs['buy_taker_share'])
    if price <= stop:
        return 'INVALIDATED'
    if item.get('profit_review_eur') and price >= item['profit_review_eur']:
        return 'PROFIT_REVIEW'
    liquid = (obs['spread_pct'] <= 0.45
              and num(obs['bid_depth_1pct_eur'], 0) >= 1500
              and obs['buy_150_complete'] and obs['sell_150_complete'])
    minimum = item.get('min_seen_price')
    if (minimum and price >= minimum*1.007
            and price <= entry*1.02 and liquid
            and share is not None and share >= 0.56
            and obs['two_green_5m']
            and num(obs['volume_ratio_5m'], 0) >= 1.3):
        return 'RECONFIRMED'
    if (price < entry*0.988 and obs['two_red_5m']
            and share is not None and share < 0.45):
        return 'BREAKDOWN'
    if price < entry*0.995:
        return 'WAIT_REBOUND'
    return 'ACTIVE'


def advance(item, obs, now):
    """Two independent probes confirm every advisory except structural stop."""
    minimum = num(item.get('min_seen_price'))
    item['min_seen_price'] = min(minimum, obs['bid']) if minimum else obs['bid']
    proposed = classify(item, obs)
    if proposed == item.get('pending'):
        item['pending_count'] = int(item.get('pending_count') or 0) + 1
    else:
        item['pending'], item['pending_count'] = proposed, 1
    if proposed == 'INVALIDATED' or item['pending_count'] >= 2:
        item['status'] = proposed
    item['last_price_eur'] = obs['bid']
    item['last_observed_at_utc'] = obs['observed_at_utc']
    item['last_probe'] = obs
    action = item['status']
    if action not in ('BREAKDOWN', 'RECONFIRMED', 'INVALIDATED', 'PROFIT_REVIEW'):
        return None
    if item.get('last_notice') == action:
        return None
    if now - num(item.get('last_notice_ts'), 0) < NOTIFY_COOLDOWN_SECONDS and action != 'INVALIDATED':
        return None
    return action


def notify(item, action, obs):
    if os.getenv('FOLLOW_NOTIFY_ENABLED', 'false').lower() != 'true':
        return 'SHADOW_ONLY'
    user = os.getenv('ALERT_GMAIL_USER', '').strip()
    recipient = os.getenv('ALERT_EMAIL_TO', '').strip()
    password = os.getenv('GMAIL_APP_PASSWORD', '').strip()
    if not user or not recipient or not password:
        return 'SMTP_UNAVAILABLE'
    import email_alert
    subjects = {'BREAKDOWN': 'SURVEILLANCE - dynamique rompue',
                'RECONFIRMED': 'SURVEILLANCE - reprise a reevaluer',
                'INVALIDATED': 'SURVEILLANCE - invalidation structurelle',
                'PROFIT_REVIEW': 'SURVEILLANCE - seuil de benefices'}
    message = (
        'Surveillance dun signal PUBLIC Solaire. Ne presume pas dune position detenue.\n'
        f"Marche : {item['market']}\nEtat : {action}\n"
        f"Observation Bitvavo : {obs['observed_at_utc']}\n"
        f"Bid/ask : {obs['bid']:.8g} / {obs['ask']:.8g} EUR\n"
        f"Spread : {obs['spread_pct']:.3f}%\n"
        f"Taker acheteur : {obs['buy_taker_share']}\n"
        f"RVOL 5m : {obs['volume_ratio_5m']}\n"
        f"Entree initiale : {item['entry_eur']:.8g} EUR\n"
        f"Stop structurel initial : {item['stop_eur']:.8g} EUR\n"
        'Ce message nest pas un ordre ni une validation de prix future.\n'
        'Aucun ordre automatique.')
    try:
        email_alert.send_email(user, password, recipient,
                               f"{subjects[action]} - {item['market']}", message)
        return 'DELIVERED'
    except (smtplib.SMTPException, OSError, TimeoutError):
        return 'DELIVERY_FAILED'


def cycle(client=None, now=None, root=ROOT):
    now = time.time() if now is None else now
    state = read_json(str(root / STATE), {'markets': {}})
    markets = register(state, read_json(str(root / SOURCE), {}), now)
    status = {'schema': 'candidate_follow_v1', 'checked_at_utc': utc(now),
              'market_count': len(markets), 'status': 'OK', 'markets': [],
              'public_only': True, 'wallet_positions_unknown': True,
              'orders_submitted': False, 'affects_buy_gate': False}
    client = client or PublicClient(timeout=6, retries=1, requests_per_second=8)
    journal = read_json(str(root / JOURNAL), [])
    if not isinstance(journal, list):
        journal = []
    for market, item in markets.items():
        try:
            obs = observe(client, market, time.time())
            action = advance(item, obs, time.time())
            notice = None
            if action:
                notice = notify(item, action, obs)
                if notice in ('DELIVERED', 'SHADOW_ONLY'):
                    item['last_notice'], item['last_notice_ts'] = action, time.time()
                journal.append({'at_utc': utc(), 'market': market,
                                'alert_id': item['alert_id'], 'transition': action,
                                'notification': notice, 'bid': obs['bid'],
                                'spread_pct': obs['spread_pct']})
            status['markets'].append({'market': market, 'state': item['status'],
                                      'entry_eur': item['entry_eur'],
                                      'stop_eur': item['stop_eur'], 'probe': obs,
                                      'notification': notice})
        except (RuntimeError, ValueError, KeyError, TypeError, IndexError) as exc:
            item['pending'], item['pending_count'] = None, 0
            status['markets'].append({'market': market, 'state': 'UNAVAILABLE',
                                      'reason': type(exc).__name__ + ':' + str(exc)[:100],
                                      'probe': None})
    status['status'] = 'DEGRADED' if any(m['state'] == 'UNAVAILABLE' for m in status['markets']) else 'OK'
    atomic_json(str(root / STATE), state)
    atomic_json(str(root / STATUS), status)
    atomic_json(str(root / JOURNAL), journal[-500:])
    return status


if __name__ == '__main__':
    output = cycle()
    print('PUBLIC_CANDIDATE_FOLLOW ' + json.dumps({
        'checked_at_utc': output['checked_at_utc'],
        'market_count': output['market_count'],
        'status': output['status'],
        'states': {m['market']: m['state'] for m in output['markets']}}))
