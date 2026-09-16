"""Whole-universe public watch, separate from fixed-period trading features.

Absent source candles are explicit slots WITHOUT OHLCV. No interpolation,
carry-forward price, synthetic volume or active decision is produced here.
"""
from collections import Counter
from research.common import finite, freshness, INTERVAL_MS
from research.input_contract import source_close_bound

SURVEILLANCE_POLICY = 'PUBLIC_SPARSE_WATCH_V1'
REPRESENTATION_POLICY = 'SOURCE_ABSENCE_GRID_V1'


def candle_window(tf, interval):
    """Only a successful, provenance-bound response can support source absence."""
    source = tf.get('source') or {}
    rows = tf.get('candles') or []
    if not source.get('response_id'):
        return {'status': 'COLLECTION_UNAVAILABLE', 'missing_slots': [], 'inference': 'UNKNOWN'}
    duration = INTERVAL_MS[interval]
    bound = source_close_bound(source)
    if 'end' in source.get('params', {}):
        bound = min(bound, (int(source['params']['end']) + 1) / 1000)
    last = int(bound * 1000 // duration) * duration - duration
    present = {c['t'] for c in rows}
    earliest = min(present) if present else None
    slots = []
    for t in range(last - 24 * duration, last + 1, duration):
        if t not in present:
            # A limited response proves nothing before its first returned bar.
            covered = earliest is not None and t >= earliest
            slots.append({'start_ms': t, 'status': 'ABSENT_FROM_SUCCESSFUL_SOURCE' if covered else 'OUTSIDE_RETURNED_HISTORY',
                          'no_trade_inferred': covered})
    return {'status': 'SPARSE_SOURCE' if slots else 'CONTIGUOUS_SOURCE',
            'response_id': source['response_id'], 'closed_at_source_bound': bound,
            'returned_closed_bars': len(rows), 'missing_slots': slots,
            'inference': 'NO_TRADE_PER_API_CONTRACT; NOT_AN_INDEPENDENT_TRADE_AUDIT',
            'synthetic_candles': False}


def public_rows(record):
    if not record or not isinstance(record.get('data'), list): return {}
    rows = {}
    for row in record['data']:
        market = row.get('market') if isinstance(row, dict) else None
        if market in rows: raise ValueError('DUPLICATE_PUBLIC_MARKET')
        if market: rows[market] = row
    return rows


def observe(markets, universe, ticker_record, book_record, now, errors=()):
    tickers, books = public_rows(ticker_record), public_rows(book_record)
    observations = []
    for meta in markets:
        market = meta['market']; ticker = tickers.get(market, {}); book = books.get(market, {})
        reasons = []
        for name, record, row in [('ticker', ticker_record, ticker), ('book', book_record, book)]:
            if not row or not record or not record.get('response_id'):
                reasons.append('MISSING_' + name.upper())
            elif not freshness(now=now, retrieved=record['retrieved_at_utc'])['ok']:
                reasons.append('STALE_' + name.upper())
        last, opening = finite(ticker.get('last')), finite(ticker.get('open'))
        bid, ask = finite(book.get('bid')), finite(book.get('ask'))
        if last is None or last <= 0: reasons.append('INVALID_LAST_TRADE_PRICE')
        if bid is None or ask is None or bid <= 0 or ask <= 0 or bid > ask:
            reasons.append('INVALID_OR_CROSSED_BOOK')
        data = universe.get(market, {})
        windows = {i: candle_window(data.get('timeframes', {}).get(i, {}), i) for i in ('5m', '15m')}
        # Quote observation is useful even when fixed-period indicators cannot be computed.
        observations.append({'market': market,
            'status': 'PUBLIC_MARKET_WATCH' if not reasons else 'PUBLIC_SNAPSHOT_UNAVAILABLE',
            'reasons': sorted(set(reasons)), 'last_trade_price_eur': last,
            'change_24h_pct': (last/opening-1)*100 if last and opening and opening>0 else None,
            'bid_eur': bid, 'ask_eur': ask,
            'spread_pct': (ask/bid-1)*100 if bid and ask and 0<bid<=ask else None,
            'volume_quote_24h_eur': finite(ticker.get('volumeQuote')),
            'price_semantics': 'LAST_REPORTED_TRADE; NOT_A_GUARANTEE_OF_A_RECENT_TRADE',
            'book_semantics': 'PUBLIC_TOP_OF_BOOK_AT_RETRIEVAL; NOT_A_FILL_GUARANTEE',
            'source_ids': {'ticker': (ticker_record or {}).get('response_id'), 'book': (book_record or {}).get('response_id')},
            'retrieved_at_utc': {'ticker': (ticker_record or {}).get('retrieved_at_utc'), 'book': (book_record or {}).get('retrieved_at_utc')},
            'candle_windows': windows, 'candle_collection_errors': data.get('errors', []),
            'active_alerts_enabled': False, 'fixed_period_trading_eligibility_changed': False})
    return {'schema_version': 1, 'surveillance_policy': SURVEILLANCE_POLICY,
            'representation_policy': REPRESENTATION_POLICY, 'active_alerts_enabled': False,
            'surveillance_only': True, 'synthetic_candles': False, 'observed_at': now,
            'universe': len(markets), 'status_counts': dict(Counter(o['status'] for o in observations)),
            'collection_errors': list(errors), 'markets': observations}


def collect_public_watch(client, markets, universe):
    """Bulk primary coverage has no optional per-market enrichment deadline."""
    import time
    records = {}; errors = []
    for name, path in [('ticker', '/ticker/24h'), ('book', '/ticker/book')]:
        try:
            records[name] = client.capture(path, cache=False, consumer_id='surveillance:' + name)
        except (ValueError, RuntimeError, KeyError) as e:
            errors.append({'source': name, 'reason': str(e)})
    return observe(markets, universe, records.get('ticker'), records.get('book'), time.time(), errors)
