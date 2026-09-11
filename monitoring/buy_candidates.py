"""Optional V4 buy path. Imported only after critical position management."""
import os
import time
from email_alert_v4 import ranked_eligible_events
from research.common import finite, freshness, read_json
from research.risk import DEFAULTS, correlation, plan as make_plan
from monitoring.positions import BUY
from research.quality import spread_diagnostic


def candidates(state, account, held, metadata, inputs, issues, exposure, portfolio_risk, client, market_inputs):
    buy_state = state.get('buy_state', {'markets': {}})
    if os.getenv('ALLOW_BUY_ALERTS') != 'true':
        return [], buy_state
    if issues or not isinstance(account, dict) or not freshness(now=time.time(), retrieved=account.get('retrieved_at_utc'), max_retrieval_age=120)['ok']:
        issues.append('BUY_ACCOUNT_UNAVAILABLE')
        return [], buy_state
    if any(o.get('side') == 'buy' for o in account['orders']):
        return [], buy_state
    cash = next((finite(b.get('available')) for b in account['balances'] if b['symbol'] == 'EUR'), None)
    if cash is None or cash < 0:
        issues.append('BUY_BUDGET_UNKNOWN')
        return [], buy_state
    payload = read_json('alert_candidates.json', {})
    if payload.get('decision_policy', payload.get('policy', 'V4_FROZEN_20260908')) != 'V4_FROZEN_20260908':
        issues.append('NON_V4_BUY_ROUTE_REFUSED')
        return [], buy_state
    prior = state.get('buy_state')
    if prior is None:
        prior = read_json('alert_state_v4.json', {'markets': {}})
    ranked, buy_state = ranked_eligible_events(payload, prior, time.time())
    cfg = {**DEFAULTS, 'cash_eur':cash,'existing_exposure_eur':exposure,
           'existing_risk_eur':portfolio_risk,'existing_positions':len(held),
           'portfolio_state':'FRESH_READ_ONLY_ACCOUNT'}
    deadline = time.monotonic()+20  # Bounded optional acquisition, never delays an existing exit.
    rejected = []
    state['buy_diagnostics'] = rejected
    for row in ranked:
        if time.monotonic() >= deadline or not freshness(now=time.time(), retrieved=account['retrieved_at_utc'], max_retrieval_age=120)['ok']:
            issues.append('BUY_BUDGET_OR_ACCOUNT_EXPIRED')
            break
        market = row['market']
        if market in held or market not in metadata:
            rejected.append({'market':market,'reason':'HELD_OR_UNAVAILABLE'})
            continue
        try:
            quote, features, candles = market_inputs(client, market, time.time())
            if not features.get('valid') or not freshness(now=time.time(), retrieved=quote['retrieved_at_utc'],
                    candle_start_ms=features.get('last_closed_start_ms'), interval='15m', max_retrieval_age=90)['ok']:
                rejected.append({'market':market,'reason':'STALE_OR_INVALID_ENTRY_DATA'})
                continue
            if any((c := correlation(candles, values[2])) is None or c >= .8 for values in inputs.values()):
                rejected.append({'market':market,'reason':'CORRELATED_OR_UNKNOWN'})
                continue
            if not finite(row.get('last')) or not quote['ask'] or abs(quote['ask']/row['last']-1) > .005:
                rejected.append({'market':market,'reason':'PRICE_DRIFT'})
                continue
            bid, ask = finite(quote.get('bid')), finite(quote.get('ask'))
            current_spread = (ask-bid)/((ask+bid)/2)*100 if bid and ask and 0 < bid <= ask else None
            spread = spread_diagnostic(row.get('risk_flags') or [], current_spread)
            if not spread['execution_allowed']:
                rejected.append({'market':market,'reason':'SPREAD_NOT_EXECUTABLE'})
                continue
            p = make_plan({**row,'ask':ask},features,metadata[market],cfg)
            if not p['valid']:
                rejected.append({'market':market,'reason':p.get('reason','INVALID_PLAN')})
                continue
        except (ValueError, KeyError, TypeError, RuntimeError):
            rejected.append({'market':market,'reason':'CANDIDATE_DATA_UNAVAILABLE'})
            continue
        if time.monotonic() >= deadline:
            issues.append('BUY_ACQUISITION_DEADLINE')
            break
        episode = buy_state['markets'][market]['episode']
        return [{'action':BUY,'market':market,'position_id':'buy:'+market,'trigger_key':str(episode),
                 'price_eur':p['entry_eur'],'amount':float(p['amount']),'stop_eur':p['stop_eur'],
                 'target_eur':p['tp1_eur'],'trade_plan':p,
                 'reason':'Signal V4 valide, données fraîches et limites du portefeuille réel respectées.',
                 'observed_at_utc':quote['retrieved_at_utc'],'baseline_row':row}], buy_state
    return [], buy_state
