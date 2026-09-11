"""Optional V4 buy path. Imported only after critical position management."""
import os
import time
from email_alert_v4 import select_events
from research.common import finite, freshness, read_json
from research.risk import DEFAULTS, correlation, plan as make_plan
from monitoring.positions import BUY


def candidates(state, account, held, metadata, inputs, issues, exposure, portfolio_risk, client, market_inputs):
    events = []
    eligible_buys = []
    buy_state = state.get('buy_state', {'markets': {}})
    if os.getenv('ALLOW_BUY_ALERTS') == 'true':
        try:
            payload = read_json('alert_candidates.json', {})
            prior_buys = state.get('buy_state')
            if prior_buys is None:
                prior_buys = read_json('alert_state_v4.json', {'markets': {}})
            eligible_buys, buy_state = select_events(payload, prior_buys, time.time())
            state['buy_state'] = buy_state
        except Exception:
            # Corrupt prospecting files must not suppress a justified exit.
            issues.append('BUY_INPUT_UNAVAILABLE')
    can_buy = not issues and not any(o.get('side') == 'buy' for o in account['orders'])
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
    return events, buy_state
