#!/usr/bin/env python3
"""Every-cycle private supervision; no test-email bypass or order submission.

Only the encrypted ledger and aggregate availability status may be published.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import email_alert
from email_alert_v4 import select_events
from monitoring.account import ReadOnlyAccount
from monitoring.positions import BUY, management_event, mark_delivered, message, select_actions
from monitoring.state import load_state, save_state
from research.common import atomic_json, finite, freshness, read_json, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.risk import DEFAULTS, correlation, plan as make_plan

STATE = 'position_alert_state.enc.json'
STATUS = 'position_monitor_status.json'
BUY_INPUT = 'alert_candidates.json'
BUY_STATE = 'alert_state_v4.json'
MAX_BUY_PRICE_DRIFT = .005
MAX_BUY_SPREAD = .005


def market_inputs(client, market, now):
    book = client.get('/' + market + '/book', {'depth': 25}, cache=False)
    quote = {'bid': finite(book['bids'][0][0]) if book.get('bids') else None,
             'ask': finite(book['asks'][0][0]) if book.get('asks') else None,
             'retrieved_at_utc': client.metadata('/' + market + '/book', {'depth': 25})['retrieved_at_utc']}
    try:
        raw = client.get('/' + market + '/candles', {'interval': '15m', 'limit': 100})
        candles = closed_candles(raw, '15m', now)
        features = describe(candles, '15m')
    except Exception:
        # A stop breach needs a fresh executable quote, not an ATR history.
        candles, features = [], {'valid': False}
    return quote, features, candles


def smtp_credentials():
    user = os.getenv('ALERT_GMAIL_USER', '').strip()
    recipient = os.getenv('ALERT_EMAIL_TO', '').strip()
    password = os.getenv('GMAIL_APP_PASSWORD', '').strip().replace(' ', '')
    if recipient.lower() != 'bellonirom@gmail.com' or not user or not password:
        return None
    return user, password, recipient


def public_buy_event(row, buy_state, client, metadata, now):
    """Revalidate a published V4 buy with fresh public execution data.

    This deliberately makes no claim about holdings or live cash. Those checks
    remain exclusive to the read-only private-account path below.
    """
    market = row.get('market')
    if not market or market not in metadata:
        return None, 'MARKET_UNAVAILABLE'
    quote, features, _ = market_inputs(client, market, now)
    bid, ask, signal_price = finite(quote.get('bid')), finite(quote.get('ask')), finite(row.get('last'))
    if bid is None or ask is None or signal_price is None or not 0 < bid <= ask:
        return None, 'INVALID_BOOK'
    if ask / bid - 1 > MAX_BUY_SPREAD:
        return None, 'SPREAD_TOO_WIDE'
    if abs(ask / signal_price - 1) > MAX_BUY_PRICE_DRIFT:
        return None, 'PRICE_MOVED'
    if not features.get('valid') or not freshness(
            now=now, retrieved=quote.get('retrieved_at_utc'),
            candle_start_ms=features.get('last_closed_start_ms'), interval='15m',
            max_retrieval_age=90)['ok']:
        return None, 'STALE_OR_INVALID_STRUCTURE'
    trade = make_plan({**row, 'ask': ask}, features, metadata[market])
    if not trade.get('valid'):
        return None, trade.get('reason', 'INVALID_PLAN')
    episode = buy_state['markets'][market].get('episode', 0)
    return {
        'action': BUY,
        'market': market,
        'position_id': 'public-buy:' + market,
        'trigger_key': str(episode),
        'price_eur': trade['entry_eur'],
        'amount': float(trade['amount']),
        'stop_eur': trade['stop_eur'],
        'target_eur': trade['tp1_eur'],
        'trade_plan': trade,
        'reason': ('Signal V4 validé ; carnet, prix et structure de marché encore compatibles '
                   'avec une entrée. Solde et positions Bitvavo non vérifiés.'),
        'observed_at_utc': quote['retrieved_at_utc'],
        'baseline_row': row,
    }, None


def run_public_buy_fallback(status):
    """Keep prospecting alerts available when private supervision is disabled."""
    status['position_actions'] = 'BLOCKED_ACCOUNT_UNKNOWN'
    if os.getenv('ALLOW_BUY_ALERTS') != 'true':
        status.update(buy_alerts='BLOCKED_PUBLICATION_OR_REPLAY', email='NONE')
        return 0
    now = time.time()
    payload = read_json(BUY_INPUT, {})
    buy_state = read_json(BUY_STATE, {'markets': {}})
    candidates, buy_state = select_events(payload, buy_state, now, limit=None)
    # Persist observation/episode transitions even when the scan is empty. SMTP
    # delivery markers are still written only after a successful send.
    atomic_json(BUY_STATE, buy_state)
    if not candidates:
        status.update(buy_alerts='PUBLIC_MARKET_VALIDATION_READY', email='NONE')
        return 0
    client = PublicClient(timeout=10, retries=2)
    client.get('/time')
    if abs(client.server_offset) > 30:
        status.update(buy_alerts='PUBLIC_VALIDATION_UNAVAILABLE', email='NONE')
        return 2
    metadata = {m['market']: m for m in client.get('/markets')
                if m.get('quote') == 'EUR' and m.get('status') == 'trading'}
    selected = None
    checked = 0
    validation_errors = 0
    for row in candidates:
        checked += 1
        try:
            selected, _ = public_buy_event(row, buy_state, client, metadata, time.time())
        except Exception:
            selected = None
            validation_errors += 1
        if selected:
            break
    status['public_buy_candidates_checked'] = checked
    if not selected:
        if validation_errors:
            status.update(buy_alerts='PUBLIC_VALIDATION_UNAVAILABLE', email='NONE')
            return 2
        status.update(buy_alerts='NO_MARKET_VALIDATED_CANDIDATE', email='NONE')
        return 0
    credentials = smtp_credentials()
    if credentials is None:
        status.update(buy_alerts='BLOCKED_SMTP_CONFIG', email='CONFIG_MISSING_OR_RECIPIENT_MISMATCH')
        return 2
    _, body = message([selected])
    subject = f"ACHÈTE — {selected['market']} — Bitvavo"
    email_alert.send_email(*credentials, subject, body)
    sent_at = time.time()
    market = selected['market']
    row = selected['baseline_row']
    previous = buy_state['markets'][market]
    previous.update(last_sent_ts=sent_at, sent_episode=previous.get('episode', 0),
                    opportunity=row.get('opportunity_score'), entry=row.get('entry_score'),
                    price=row.get('last'), status=row.get('action_status'))
    buy_state['last_global_sent_ts'] = sent_at
    buy_state['updated_at_utc'] = utc(sent_at)
    atomic_json(BUY_STATE, buy_state)
    status.update(buy_alerts='PUBLIC_MARKET_VALIDATED', email='DELIVERY_COMPLETED')
    return 0


def view_only_buy_guard(account):
    """Fail closed for private BUY alerts when reserved EUR may hide an open buy."""
    eur = next((b for b in account.get('balances', []) if b.get('symbol') == 'EUR'), None)
    if eur is None:
        return False, 'BLOCKED_EUR_BALANCE_UNAVAILABLE'
    available, locked = finite(eur.get('available')), finite(eur.get('in_order'))
    if available is None or locked is None or min(available, locked) < 0:
        return False, 'BLOCKED_EUR_BALANCE_INVALID'
    if locked > 0:
        return False, 'BLOCKED_EUR_IN_ORDER_UNKNOWN'
    return True, 'READY_VIEW_ONLY_BALANCE'


def run(status):
    key = os.getenv('BITVAVO_READ_API_KEY', '').strip()
    secret = os.getenv('BITVAVO_READ_API_SECRET', '').strip()
    state_key = os.getenv('POSITION_STATE_KEY', '').strip()
    if not key or not secret or not state_key:
        status.update(status='UNCONFIGURED', reason='READ_ACCOUNT_OR_ENCRYPTION_SECRET_MISSING',
                      account_aware_buy_alerts='BLOCKED_ACCOUNT_UNKNOWN')
        return run_public_buy_fallback(status)
    state = load_state(STATE, state_key)
    plans = json.loads(os.getenv('POSITION_PLANS_JSON', '{}'))
    if not isinstance(plans, dict):
        raise ValueError('INVALID_POSITION_PLANS')
    account = ReadOnlyAccount(key, secret).snapshot()
    if (account.get('access_mode') != 'VIEW_ONLY_BALANCE' or
            account.get('open_orders_visibility') != 'UNAVAILABLE_VIEW_ONLY'):
        raise ValueError('STRICT_VIEW_ONLY_ACCOUNT_CONTRACT_REQUIRED')
    status.update(account_access='VIEW_ONLY_BALANCE',
                  open_orders='UNAVAILABLE_VIEW_ONLY',
                  position_actions='VIEW_ONLY_BALANCE_MANUAL_ORDER_CHECK')
    if not freshness(now=time.time(), retrieved=account['retrieved_at_utc'], max_retrieval_age=120)['ok']:
        status.update(status='STALE', reason='ACCOUNT_SNAPSHOT_STALE', buy_alerts='BLOCKED')
        return 0
    client = PublicClient(timeout=10, retries=2)
    client.get('/time')
    if abs(client.server_offset) > 30:
        raise ValueError('CLOCK_SKEW')
    metadata = {m['market']: m for m in client.get('/markets') if m.get('quote') == 'EUR' and m.get('status') == 'trading'}
    held = {b['symbol'] + '-EUR': b for b in account['balances'] if b['symbol'] != 'EUR' and b['amount'] > 0}
    observed = state.setdefault('positions', {})
    for market, old in observed.items():
        if market not in held:
            old['closed_observed'] = True
    events, inputs, issues = [], {}, []
    exposure, portfolio_risk = 0., 0.
    for market, balance in held.items():
        p = plans.get(market, {})
        old = observed.get(market, {})
        if old.get('closed_observed') and old.get('position_id') == p.get('position_id'):
            issues.append('REOPENED_POSITION_REQUIRES_NEW_PLAN')
            continue
        observed[market] = {'position_id': p.get('position_id'), 'amount': balance['amount'],
                            'observed_at_utc': account['retrieved_at_utc'], 'closed_observed': False}
        if market not in metadata:
            issues.append('HELD_MARKET_UNAVAILABLE')
            continue
        try:
            quote, features, candles = market_inputs(client, market, time.time())
            inputs[market] = (quote, features, candles)
            # Open-order details are intentionally unavailable: reading them would
            # require a Bitvavo trading permission. Management stays conservative.
            event, reason = management_event(balance, p, quote, features, metadata[market], None, time.time())
            observed[market]['assessment'] = reason
            if event:
                events.append(event)
            if reason not in {'ACTION', 'NO_JUSTIFIED_ACTION', 'BELOW_ORDER_MINIMUM',
                              'EQUIVALENT_EXIT_ORDER_ALREADY_OPEN', 'EQUIVALENT_PROFIT_ORDER_ALREADY_OPEN'}:
                issues.append(reason)
            bid = finite(quote['bid'])
            if bid is None:
                issues.append('POSITION_VALUE_UNAVAILABLE')
                continue
            exposure += balance['amount'] * bid
            stop = finite(p.get('stop_eur'))
            if stop is None or stop <= 0:
                issues.append('POSITION_RISK_UNKNOWN')
            else:
                portfolio_risk += balance['amount'] * max(0, bid * 1.0035 - stop * .9965)
        except Exception:
            observed[market]['assessment'] = 'MARKET_READ_FAILED'
            issues.append('MARKET_READ_FAILED')
    if not freshness(now=time.time(), retrieved=account['retrieved_at_utc'], max_retrieval_age=120)['ok']:
        events = []
        issues.append('ACCOUNT_SNAPSHOT_STALE')
    eligible_buys = []
    buy_state = state.get('buy_state', {'markets': {}})
    if os.getenv('ALLOW_BUY_ALERTS') == 'true':
        try:
            payload = read_json('alert_candidates.json', {})
            prior_buys = state.get('buy_state')
            if prior_buys is None:
                prior_buys = read_json(BUY_STATE, {'markets': {}})
            eligible_buys, buy_state = select_events(payload, prior_buys, time.time(), limit=None)
            state['buy_state'] = buy_state
            # The public buy state contains no account data and remains the
            # canonical bridge if private supervision is later unavailable.
            atomic_json(BUY_STATE, buy_state)
        except Exception:
            # Corrupt prospecting files must not suppress a justified exit.
            issues.append('BUY_INPUT_UNAVAILABLE')
    buy_guard_ok, buy_guard_status = view_only_buy_guard(account)
    status['account_aware_buy_alerts'] = buy_guard_status
    can_buy = not issues and not events and buy_guard_ok
    if can_buy:
        cash = next((b['available'] for b in account['balances'] if b['symbol'] == 'EUR'), 0)
        cfg = {**DEFAULTS, 'cash_eur': cash, 'existing_exposure_eur': exposure,
               'existing_risk_eur': portfolio_risk, 'existing_positions': len(held),
               'portfolio_state': 'FRESH_READ_ONLY_ACCOUNT'}
        for row in eligible_buys:
            market = row['market']
            if market in held or market not in metadata:
                continue
            quote, features, candles = market_inputs(client, market, time.time())
            if not features.get('valid') or not freshness(now=time.time(), retrieved=quote['retrieved_at_utc'],
                    candle_start_ms=features.get('last_closed_start_ms'), interval='15m', max_retrieval_age=90)['ok']:
                continue
            if any((c := correlation(candles, values[2])) is None or c >= .8 for values in inputs.values()):
                continue
            if not finite(row.get('last')) or not quote['ask'] or abs(quote['ask'] / row['last'] - 1) > .005:
                continue
            p = make_plan({**row, 'ask': quote['ask']}, features, metadata[market], cfg)
            if not p['valid']:
                continue
            episode = buy_state['markets'][market]['episode']
            events.append({'action': BUY, 'market': market, 'position_id': 'buy:' + market,
                           'trigger_key': str(episode), 'price_eur': p['entry_eur'], 'amount': float(p['amount']),
                           'stop_eur': p['stop_eur'], 'target_eur': p['tp1_eur'], 'trade_plan': p,
                           'reason': 'Signal V4 valide, données fraîches et limites du portefeuille réel respectées.',
                           'observed_at_utc': quote['retrieved_at_utc'], 'baseline_row': row})
            # Keep the existing one-proposed-buy limit, but apply it after all
            # final eligibility checks so a rejected top row cannot mask the
            # next admissible candidate.
            break
    selected, state = select_actions(events, state, time.time())
    selected = [e for e in selected if freshness(now=time.time(), retrieved=e['observed_at_utc'], max_retrieval_age=90)['ok']]
    if not freshness(now=time.time(), retrieved=account['retrieved_at_utc'], max_retrieval_age=120)['ok']:
        selected = []
        issues.append('ACCOUNT_SNAPSHOT_STALE')
    save_state(STATE, state_key, state)
    buy_status = ('BLOCKED' if issues else
                  ('REQUIRES_FRESH_VALID_SIGNAL_AND_ACCOUNT_LIMITS' if buy_guard_ok else buy_guard_status))
    status.update(status='PARTIAL' if issues else 'OK', reason='SOME_CHECKS_UNAVAILABLE' if issues else 'CYCLE_COMPLETE',
                  buy_alerts=buy_status)
    if not selected:
        status['email'] = 'NONE'
        return 0
    credentials = smtp_credentials()
    if credentials is None:
        status.update(email='CONFIG_MISSING_OR_RECIPIENT_MISMATCH')
        return 0
    subject, body = message(selected)
    email_alert.send_email(*credentials, subject, body)
    sent_at = time.time()
    mark_delivered(state, selected, sent_at)
    for e in selected:
        if e['action'] == BUY:
            previous = state['buy_state']['markets'][e['market']]
            row = e['baseline_row']
            previous.update(last_sent_ts=sent_at, sent_episode=previous['episode'],
                            opportunity=row['opportunity_score'], entry=row['entry_score'])
            state['buy_state']['last_global_sent_ts'] = sent_at
    if 'buy_state' in state:
        state['buy_state']['updated_at_utc'] = utc(sent_at)
        atomic_json(BUY_STATE, state['buy_state'])
    save_state(STATE, state_key, state)
    status['email'] = 'DELIVERY_COMPLETED'
    return 0


def main():
    status = {'checked_at_utc': utc(), 'status': 'STARTING', 'mode': 'READ_ONLY', 'dry_run': True}
    try:
        result = run(status)
    except Exception as exc:
        status.update(status='ERROR', reason=type(exc).__name__, email='NO_DELIVERY_CONFIRMATION')
        result = 2
    status['completed_at_utc'] = utc()
    atomic_json(STATUS, status)
    print('POSITION_MONITOR ' + json.dumps(status))
    return result


if __name__ == '__main__':
    raise SystemExit(main())
