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
from monitoring.account import ReadOnlyAccount
from monitoring.positions import BUY, management_event, mark_delivered, message, select_actions
from monitoring.state import load_state, save_state
from research.common import atomic_json, finite, freshness, read_json, utc, timestamp
from research.features import closed_candles, describe
from research.http import PublicClient

STATE = 'position_alert_state.enc.json'
STATUS = 'position_monitor_status.json'


def market_quote(client, market):
    response = client.capture('/' + market + '/book', {'depth': 25}, cache=False, consumer_id='monitor:'+market)
    book = response['data']
    return {'bid': finite(book['bids'][0][0]) if book.get('bids') else None,
            'ask': finite(book['asks'][0][0]) if book.get('asks') else None,
            'retrieved_at_utc': response['retrieved_at_utc'],
            'market_asof_at_utc':response.get('market_asof_at_utc'),
            'source_response_id':response.get('response_id'),
            'request_started_at_utc':response.get('request_started_at_utc'),
            'server_http_date':response.get('server_http_date')}


def market_features(client, market, now):
    try:
        from research.features import candles_from_response
        response = client.capture('/' + market + '/candles', {'interval': '15m', 'limit': 100},
                                  consumer_id='monitor:'+market)
        candles = candles_from_response(response, '15m')
        return describe(candles, '15m'), candles
    except Exception:
        return {'valid': False}, []


def market_inputs(client, market, now):
    quote = market_quote(client, market)
    features, candles = market_features(client, market, now)
    return quote, features, candles


def run(status):
    run_started=time.monotonic()
    key = os.getenv('BITVAVO_READ_API_KEY', '').strip()
    secret = os.getenv('BITVAVO_READ_API_SECRET', '').strip()
    state_key = os.getenv('POSITION_STATE_KEY', '').strip()
    if not key or not secret or not state_key:
        status.update(status='UNCONFIGURED', reason='READ_ACCOUNT_OR_ENCRYPTION_SECRET_MISSING',
                      buy_alerts='BLOCKED_ACCOUNT_UNKNOWN')
        return 0
    state = load_state(STATE, state_key)
    plans = json.loads(os.getenv('POSITION_PLANS_JSON', '{}'))
    if not isinstance(plans, dict):
        raise ValueError('INVALID_POSITION_PLANS')
    account = ReadOnlyAccount(key, secret).snapshot()
    status.setdefault('durations',{})['account_seconds']=time.monotonic()-run_started
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
            quote = market_quote(client, market)
            features, candles = {'valid': False}, []
            inputs[market] = (quote, features, candles)
            event, reason = management_event(balance, p, quote, features, metadata[market], account['orders'], time.time())
            observed[market]['assessment'] = reason
            if event:
                events.append(event)
            if reason not in {'ACTION', 'NO_JUSTIFIED_ACTION', 'BELOW_ORDER_MINIMUM',
                              'EQUIVALENT_EXIT_ORDER_ALREADY_OPEN', 'EQUIVALENT_PROFIT_ORDER_ALREADY_OPEN',
                              'TRAILING_STRUCTURE_UNAVAILABLE'}:
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
    # Only after all executable quotes have been assessed may enrichment start.
    if not events:
        for market, (quote, _, _) in list(inputs.items()):
            features, candles = market_features(client, market, time.time())
            inputs[market] = (quote, features, candles)
            event, reason = management_event(held[market], plans.get(market, {}), quote, features,
                                              metadata[market], account['orders'], time.time())
            observed[market]['assessment'] = reason
            if event:
                events.append(event)
            elif reason == 'TRAILING_STRUCTURE_UNAVAILABLE':
                issues.append(reason)
    from monitoring.telemetry import record_cycle
    measurement_issues=list(issues)
    if any(observed.get(m,{}).get('assessment')=='TRAILING_STRUCTURE_UNAVAILABLE' for m in held):
        measurement_issues.append('TRAILING_STRUCTURE_UNAVAILABLE')
    record_cycle(state, status, account, inputs, len(held), measurement_issues, time.time())
    status['durations']['position_assessment_seconds']=time.monotonic()-run_started
    if not events and os.getenv('ALLOW_BUY_ALERTS') == 'true':
        try:
            from monitoring.buy_candidates import candidates
            events, buy_state = candidates(state, account, held, metadata, inputs, issues,
                                           exposure, portfolio_risk, client, market_inputs)
            state['buy_state'] = buy_state
        except Exception:
            issues.append('BUY_INPUT_UNAVAILABLE')
    selected, state = select_actions(events, state, time.time())
    selected = [e for e in selected if freshness(now=time.time(), retrieved=e['observed_at_utc'], max_retrieval_age=90)['ok']]
    if not freshness(now=time.time(), retrieved=account['retrieved_at_utc'], max_retrieval_age=120)['ok']:
        selected = []
        issues.append('ACCOUNT_SNAPSHOT_STALE')
    status['final_freshness']={'account_age_seconds':time.time()-timestamp(account['retrieved_at_utc']),
                             'oldest_selected_quote_age_seconds':max((time.time()-timestamp(e['observed_at_utc']) for e in selected),default=None)}
    save_state(STATE, state_key, state)
    status.update(status='PARTIAL' if issues else 'OK', reason='SOME_CHECKS_UNAVAILABLE' if issues else 'CYCLE_COMPLETE',
                  buy_alerts='BLOCKED' if issues else 'REQUIRES_FRESH_VALID_SIGNAL_AND_ACCOUNT_LIMITS')
    if not selected:
        status['email'] = 'NONE'
        return 0
    user = os.getenv('ALERT_GMAIL_USER', '').strip()
    recipient = os.getenv('ALERT_EMAIL_TO', '').strip()
    password = os.getenv('GMAIL_APP_PASSWORD', '').strip().replace(' ', '')
    if recipient.lower() != 'bellonirom@gmail.com' or not user or not password:
        status.update(email='CONFIG_MISSING_OR_RECIPIENT_MISMATCH')
        return 0
    subject, body = message(selected)
    # State persistence and rendering take time too; recheck immediately before SMTP.
    if not freshness(now=time.time(),retrieved=account['retrieved_at_utc'],max_retrieval_age=120)['ok'] or any(
            not freshness(now=time.time(),retrieved=e['observed_at_utc'],max_retrieval_age=90)['ok'] for e in selected):
        status['email']='BLOCKED_FINAL_FRESHNESS'
        return 0
    email_alert.send_email(user, password, recipient, subject, body)
    sent_at = time.time()
    mark_delivered(state, selected, sent_at)
    for e in selected:
        if e['action'] == BUY:
            previous = state['buy_state']['markets'][e['market']]
            row = e['baseline_row']
            previous.update(last_sent_ts=sent_at, sent_episode=previous['episode'],
                            opportunity=row['opportunity_score'], entry=row['entry_score'])
            state['buy_state']['last_global_sent_ts'] = sent_at
    try:
        save_state(STATE, state_key, state)
    except Exception:
        status['email'] = 'SMTP_ACCEPTED_PERSISTENCE_UNCERTAIN'
        raise
    status['email'] = 'DELIVERY_COMPLETED'
    return 0


def main():
    status = {'checked_at_utc': utc(), 'status': 'STARTING', 'mode': 'READ_ONLY', 'dry_run': True}
    try:
        result = run(status)
    except Exception as exc:
        status.update(status='ERROR', reason=type(exc).__name__)
        status.setdefault('email', 'NO_DELIVERY_CONFIRMATION')
        result = 2
    status['completed_at_utc'] = utc()
    try:
        from monitoring.telemetry import record_availability
        availability=record_availability(read_json('monitor_availability.json',{}),status,time.time())
        atomic_json('monitor_availability.json',availability)
    except Exception:
        status['availability_record']='FAILED'  # Reporting failure cannot suppress an already justified exit.
    atomic_json(STATUS, status)
    print('POSITION_MONITOR ' + json.dumps(status))
    return result


if __name__ == '__main__':
    raise SystemExit(main())
