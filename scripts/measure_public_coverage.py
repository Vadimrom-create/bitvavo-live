#!/usr/bin/env python3
"""Public acquisition experiment only: no policy execution, publication or pilot."""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from research.common import atomic_json, INTERVAL_MS, timestamp, utc
from research.features import closed_candles
from research.http import PublicClient
from research.input_contract import code_revision, source_close_bound

INTERVALS = {'5m': 300000, '15m': 900000, '30m': 1800000, '1h': 3600000}


def summarize(record, interval, reference):
    # Diagnostic-only registration; never changes a decision policy or raw bar.
    INTERVAL_MS.setdefault('30m', INTERVALS['30m'])
    rows = closed_candles(record['data'], interval, min(reference, source_close_bound(record)))
    duration = INTERVALS[interval]
    expected = int(reference * 1000 // duration) * duration - duration
    starts = {r['t'] for r in rows}
    missing = [expected - i * duration for i in range(24, -1, -1) if expected - i * duration not in starts]
    enough = len(rows) >= 25
    contiguous = enough and all(b['t'] - a['t'] == duration for a, b in zip(rows[-25:-1], rows[-24:]))
    latest = bool(rows) and rows[-1]['t'] == expected
    reasons = []
    if not enough: reasons.append('FEWER_THAN_25_CLOSED_BARS')
    if enough and not contiguous: reasons.append('SOURCE_CANDLE_GAPS')
    if not latest: reasons.append('LATEST_CLOSED_INTERVAL_ABSENT')
    return {'response_obtained': True, 'closed_bars': len(rows), 'at_least_25': enough,
            'last_25_contiguous': contiguous, 'latest_closed_present': latest,
            'usable': enough and contiguous and latest, 'reasons': reasons,
            'primary_reason': reasons[0] if reasons else 'USABLE',
            'missing_period_starts': missing, 'response_id': record['response_id']}


def run(output):
    client = PublicClient()
    client.capture('/time', cache=False)
    markets = sorted(m['market'] for m in client.get('/markets') if m['quote'] == 'EUR' and m['status'] == 'trading')
    tickers = client.capture('/ticker/24h', cache=False)
    books = client.capture('/ticker/book', cache=False)
    reference = source_close_bound(client.capture('/time', cache=False))
    start = time.monotonic()
    rows = []
    def one(market, interval):
        began = time.monotonic()
        try:
            record = client.capture('/' + market + '/candles',
                {'interval': interval, 'limit': 100, 'end': int(reference * 1000) - 1},
                consumer_id='coverage:' + market + ':' + interval, cache=False)
            result = summarize(record, interval, reference)
        except (ValueError, RuntimeError, KeyError) as e:
            result = {'response_obtained': False, 'usable': False, 'primary_reason': 'COLLECTION_FAILED', 'error': str(e)}
        return {'market': market, 'interval': interval, 'queued_delay_seconds': began - start,
                'completed_after_seconds': time.monotonic() - start, **result}
    # Interleave all native timeframes per market at a common fixed candle cutoff.
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(one, market, interval) for market in markets for interval in INTERVALS]
        for f in as_completed(futures): rows.append(f.result())
    summary = {}
    for interval in INTERVALS:
        group = [r for r in rows if r['interval'] == interval]
        summary[interval] = {'queried': len(group), 'responses': sum(r['response_obtained'] for r in group),
            'at_least_25': sum(r.get('at_least_25', False) for r in group),
            'last_25_contiguous': sum(r.get('last_25_contiguous', False) for r in group),
            'usable': sum(r['usable'] for r in group),
            'primary_causes': dict(Counter(r['primary_reason'] for r in group))}
    value = {'schema_version': 1, 'kind': 'PUBLIC_COVERAGE_EXPERIMENT_NOT_PILOT', 'code_commit': code_revision(),
        'reference_at_utc': utc(reference), 'universe': markets, 'workers': 8, 'requests_per_second': 12,
        'duration_seconds': time.monotonic() - start, 'summary': summary, 'rows': sorted(rows, key=lambda r:(r['market'],r['interval'])),
        'http_errors': client.errors, 'http_requests_started': client.request_sequence,
        'requests': client.records, 'consumptions': client.consumptions,
        'ticker_response_id': tickers['response_id'], 'book_response_id': books['response_id'],
        'held_out_performed': False, 'active_alerts_enabled': False}
    atomic_json(output, value)
    print(__import__('json').dumps({k: value[k] for k in ('code_commit','reference_at_utc','duration_seconds','summary','http_errors','http_requests_started')}))


if __name__ == '__main__':
    p = argparse.ArgumentParser();p.add_argument('--output', default='runtime/public-coverage.json.gz')
    run(p.parse_args().output)
