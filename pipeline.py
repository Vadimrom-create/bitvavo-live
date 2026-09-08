#!/usr/bin/env python3
"""One collect -> V3/V4 -> full-universe journal -> evaluate -> report cycle.

No trading credentials, no private executor and no email are invoked here.
Publication and notification are separate workflow steps after this succeeds.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from research.common import atomic_json, finite, freshness, read_json, timestamp, utc
from research.evaluation import evaluate, market_control
from research.features import category, chase_risk, closed_candles, describe, nil_match, score_components, wick_setup
from research.history import connect, ingest, rebuild, recurrent, save_scan
from research.http import PublicClient
from research.risk import correlation, plan, proposed_order

POLICY = 'V4_FROZEN_20260908'
STATE_FILES = ['scan_history.json', 'signal_log.json', 'v4_history.json', 'v4_signal_log.json',
               'v4_trend_cache.json', 'v4_stability_state.json', 'v4_config.json']


def load_collector():
    spec = importlib.util.spec_from_file_location('collector_v4', 'collector-2.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def collect_universe(client, markets, ticker, now):
    """Every trading EUR market, including below the old liquidity prefilter."""
    results = {}
    def one(meta):
        name = meta['market']
        data = {'meta': meta, 'ticker': ticker.get(name, {}), 'timeframes': {}, 'errors': []}
        for interval in ('5m', '15m'):
            params = {'interval': interval, 'limit': 100}
            try:
                raw = client.get('/' + name + '/candles', params)
                record = client.metadata('/' + name + '/candles', params)
                cs = closed_candles(raw, interval, now)
                data['timeframes'][interval] = {'candles': cs, 'features': describe(cs, interval),
                                                'retrieved_at_utc': record['retrieved_at_utc']}
            except (ValueError, RuntimeError, KeyError) as exc:
                data['errors'].append({'interval': interval, 'reason': str(exc)})
        return name, data
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(one, m) for m in markets]
        for future in as_completed(futures):
            name, data = future.result()
            results[name] = data
    return results


def report_text(report):
    h = report['health']
    lines = ['# Bitvavo — V4 mesurée / infrastructure V5', '',
             f"Scan UTC : {report['scan_at_utc']}",
             f"État : {h['status']} | marchés EUR : {h['universe']} | V4 : {h['baseline_analyzed']} | données valides : {h['valid_markets']}",
             f"Récupération : {h['collected_at_utc']} | âge ticker : {h['ticker_age_seconds']:.1f} s | durée : {h['duration_seconds']:.1f} s", '',
             '## ACHÈTE — signal V4 et plan théorique', '']
    buys = report['buy']
    if not buys:
        lines.append('RIEN À ACHETER' if h['status'] == 'OK' else 'SCAN INCOMPLET — aucune recommandation d’achat publiée')
    for obs in buys:
        p, b = obs['trade_plan'], obs['baseline']
        lines += [f"- {obs['market']} : {obs['price_eur']:.8g} € | {obs['category']} | score {b['opportunity_score'] * 10:.2f}/100 | entrée {b['entry_score']:.2f}/10",
                  f"  Entrée {p['entry_eur']:.8g} € ; stop {p['stop_eur']:.8g} € ; TP1 {p['tp1_eur']:.8g} € ; TP2 {p['tp2_eur']:.8g} € ; montant {p['stake_eur']:.2f} € ; risque théorique {p['theoretical_loss_eur']:.2f} € ; R/R net {p['net_rr_tp1']:.2f}.",
                  f"  Chase risk : {obs['chase_risk']['score']}/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles."]
    lines += ['', '## SURVEILLE', '']
    for obs in report['watch']:
        lines.append(f"- {obs['market']} : {obs['price_eur']:.8g} € ; score {(obs.get('baseline') or {}).get('opportunity_score', 0) * 10:.2f}/100 ; {obs['decision']} ; {', '.join(obs['exclusions']) or 'seuil achat non atteint'}")
    lines += ['', '## Contrôle des hausses', '', '| Marché | Prix € | 24 h | État historique |', '|---|---:|---:|---|']
    for r in report['market_control'][:10]:
        lines.append(f"| {r['market']} | {r['price_eur']:.8g} | {r['change_24h_pct']:+.2f} % | {r['audit_state']} |")
    ev = report['evaluation']
    lines += ['', f"Historique : {ev['scan_count']} scans ; {ev['observation_count']} observations ; {ev['complete_buy_episodes']} épisodes d’achat évaluables.",
              'V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.',
              'Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.', '']
    return '\n'.join(lines)


def run():
    start = time.time()
    scan_id = time.strftime('%Y%m%dT%H%M%SZ', time.gmtime(start)) + '-' + uuid.uuid4().hex[:8]
    Path('runtime').mkdir(exist_ok=True)
    before = {f: read_json(f, {}) for f in STATE_FILES}
    client = PublicClient()
    client.get('/time', cache=False)
    if abs(client.server_offset) > 30:
        raise RuntimeError('EXCHANGE_CLOCK_SKEW')
    print('PIPELINE collect legacy inputs', flush=True)
    collector = load_collector()
    collector.get_json = client.get
    collector.main()
    live = read_json('bitvavo_live.json')
    # Retain the actual input snapshots and baseline state for exact replay.
    replay_input = {'scan_id': scan_id, 'source_commit': os.getenv('GITHUB_SHA'), 'state_before': before,
                    'live': copy.deepcopy(live), 'baseline_manifest': read_json('baseline/v4_20260908/manifest.json')}
    import v3_common
    import early_detector
    import v4_detector
    import v4_stabilizer
    import market_control as legacy_control
    import execution_probe
    v3_common.get_json = client.get
    legacy_control.get_json = client.get
    execution_probe.get_json = client.get
    print('PIPELINE baseline V3/V4', flush=True)
    early_detector.main()
    captured = {}
    def observe(rows, enriched, generated):
        captured.update({'rows': copy.deepcopy(rows), 'enriched': copy.deepcopy(enriched),
                         'generated_at_utc': generated, 'scan_ts': time.time()})
    v4_detector.main(audit_sink=observe)
    v4_stabilizer.main()
    baseline_output = read_json('v4_watch.json')
    legacy_control.main()
    execution_probe.main()
    baseline_ts = captured['scan_ts']
    baseline_rows = {r['market']: r for r in captured['rows']}
    stabilized = {r['market']: r for r in baseline_output['watch']}
    for name, row in stabilized.items():
        baseline_rows[name] = row
    markets_raw = client.get('/markets')
    markets = sorted([m for m in markets_raw if m.get('quote') == 'EUR' and m.get('status') == 'trading'], key=lambda m: m['market'])
    tickers = {r['market']: r for r in client.get('/ticker/24h')}
    print(f'PIPELINE full EUR universe: {len(markets)} markets, closed 5m/15m candles', flush=True)
    # Observation features must not include information after the baseline signal.
    universe = collect_universe(client, markets, tickers, baseline_ts)
    finish = time.time()
    ticker_at = client.metadata('/ticker/24h')['retrieved_at_utc']
    db = rebuild('history', connect())
    observations, candles5 = [], {}
    for meta in markets:
        name = meta['market']
        data = universe[name]
        t = tickers.get(name, {})
        b = baseline_rows.get(name)
        baseline = copy.deepcopy(b) if b else None
        m15 = data['timeframes'].get('15m', {})
        m5 = data['timeframes'].get('5m', {})
        features = m15.get('features', {'valid': False, 'reasons': ['MISSING_15M']})
        quality = freshness(now=finish, retrieved=ticker_at)
        for interval, tf in (('5m', m5), ('15m', m15)):
            if not tf.get('features', {}).get('valid'):
                quality['reasons'].append('INVALID_' + interval.upper())
            # Candle freshness is assessed at the signal time, retrieval at the
            # report time. Later-closing candles cannot leak into this signal.
            if tf.get('candles'):
                q = freshness(now=baseline_ts, retrieved=ticker_at,
                              candle_start_ms=tf['candles'][-1]['t'], interval=interval)
                quality['reasons'].extend(q['reasons'])
            else:
                quality['reasons'].append('MISSING_' + interval.upper())
        if baseline:
            e = captured['enriched'].get(name, {})
            if e.get('error') or 'NOT_ENTRY_ENRICHED' in baseline.get('risk_flags', []):
                quality['reasons'].append('ENTRY_INPUTS_UNAVAILABLE')
            profile = baseline.get('trend_profile') or {}
            if baseline.get('buy_ready') and (baseline_ts - finite(profile.get('updated_ts'), 0) > 3 * 3600):
                quality['reasons'].append('STALE_DAILY_PROFILE')
        quality['reasons'] = sorted(set(quality['reasons']))
        quality['ok'] = not quality['reasons']
        last, open24 = finite(t.get('last')), finite(t.get('open'))
        change24 = (last / open24 - 1) * 100 if last and open24 else None
        row = baseline or {'market': name, 'last': last, 'ask': finite(t.get('ask')), 'spread_pct': None,
                           'quote_volume_24h_eur': finite(t.get('volumeQuote'), 0)}
        cls = category(row)
        exclusions = list(row.get('risk_flags') or [])
        if not baseline:
            exclusions.append('LEGACY_VOLUME_PREFILTER_OR_COLLECTION_FAILURE')
        exclusions += quality['reasons']
        trade = plan(row, features, meta) if row.get('buy_ready') and quality['ok'] else None
        obs = {'market': name, 'price_eur': last, 'change_24h_pct': change24, 'baseline': baseline,
               'category': cls, 'features': {'5m': m5.get('features'), '15m': features},
               'score_components': score_components(row, before['v4_history.json'].get('markets', {}).get(name, {}), timestamp(live['generated_at_utc'])) if baseline else None,
               'data_quality': quality, 'exclusions': exclusions, 'chase_risk': chase_risk(features, change24),
               'wick_setup': wick_setup(features, row), 'nil_match': nil_match(features),
               'recurrence': recurrent(db, name, baseline_ts, cls), 'trade_plan': trade,
               'probabilities': {'10': None, '20': None, '30': None, '40': None, 'status': 'NOT_CALIBRATED'},
               'decision': 'SURVEILLE' if cls in {'PRE-IGNITION', 'IGNITION'} else cls,
               'timestamps': {'ticker_retrieved_at_utc': ticker_at, 'scan_at_utc': utc(baseline_ts),
                              'exchange_time': client.metadata('/time')['data']['time'],
                              'candle15_start_ms': features.get('last_closed_start_ms'),
                              'candle15_close_ms': features.get('last_closed_close_ms')}}
        if not quality['ok']:
            obs['decision'] = 'DATA UNAVAILABLE'
        observations.append(obs)
        candles5[name] = m5.get('candles', [])
    # Portfolio limits apply cumulatively to the same theoretical order batch.
    buys, used = [], {'exposure': 0, 'risk': 0, 'positions': 0}
    for obs in sorted(observations, key=lambda o: (o.get('baseline') or {}).get('opportunity_score', 0), reverse=True):
        if not (obs.get('baseline') or {}).get('buy_ready') or not obs['data_quality']['ok']:
            continue
        name = obs['market']
        p = plan(obs['baseline'], obs['features']['15m'], universe[name]['meta'], reserved=used)
        obs['trade_plan'] = p
        if not p['valid']:
            obs['exclusions'].append(p['reason'])
            continue
        related = []
        for other in buys:
            corr = correlation(universe[name]['timeframes']['15m']['candles'], universe[other['market']]['timeframes']['15m']['candles'])
            if corr is None or corr >= .8:
                related.append({'market': other['market'], 'correlation': corr})
        if related:
            obs['correlation_warning'] = related
            obs['exclusions'].append('CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW')
            continue
        used['exposure'] += p['stake_eur']; used['risk'] += p['theoretical_loss_eur']; used['positions'] += 1
        obs['decision'] = 'ACHÈTE'
        buys.append(obs)
    health = {'status': 'OK', 'universe': len(markets), 'baseline_analyzed': len(captured['rows']),
              'valid_markets': sum(o['data_quality']['ok'] for o in observations),
              'collected_at_utc': live['generated_at_utc'], 'ticker_age_seconds': finish - timestamp(ticker_at),
              'duration_seconds': finish - start, 'api_error_count': len(client.errors),
              'api_errors': client.errors, 'exchange_clock_offset_seconds': client.server_offset,
              'ignored_markets': [{'market': m['market'], 'reason': m.get('status')} for m in markets_raw if m.get('quote') == 'EUR' and m.get('status') != 'trading']}
    if health['ticker_age_seconds'] > 300 or not markets or len(captured['rows']) < .5 * len(markets):
        health['status'] = 'DEGRADED'
        for obs in buys:
            obs['decision'] = 'DATA UNAVAILABLE'
            obs['exclusions'].append('PIPELINE_DEGRADED')
        buys = []
    scan = {'schema_version': 1, 'scan_id': scan_id, 'scan_ts': baseline_ts, 'scan_at_utc': utc(baseline_ts),
            'policy': POLICY, 'source': 'live', 'observations': observations, 'candles_5m': candles5,
            'health': health, 'baseline_input_policy': 'legacy includes forming candles; closed diagnostics never change V4 scoring'}
    journal = save_scan('history', scan)
    ingest(db, scan)
    evaluation = evaluate(db)
    control = market_control(db, observations, baseline_ts)
    watch = sorted([o for o in observations if o['decision'] == 'SURVEILLE'],
                   key=lambda o: (o.get('baseline') or {}).get('opportunity_score', 0), reverse=True)[:5]
    report = {'scan_id': scan_id, 'scan_at_utc': utc(baseline_ts), 'health': health, 'buy': buys, 'watch': watch,
              'market_control': control, 'evaluation': evaluation, 'journal_path': str(journal),
              'orders': [proposed_order(o['trade_plan'], scan_id) for o in buys]}
    atomic_json('v5_report.json', report)
    text = report_text(report)
    Path('v5_report.md').write_text(text, encoding='utf-8')
    atomic_json('pipeline_health.json', health)
    atomic_json('evaluation.json', evaluation)
    atomic_json('proposed_orders.json', {'dry_run': True, 'orders': report['orders']})
    # Preserve raw baseline public outputs for audit; provide a separate, fresh,
    # quality-checked payload to the existing alert transport.
    alert_payload = {**baseline_output, 'watch': [{**o['baseline'], 'data_quality': o['data_quality']} for o in buys]}
    atomic_json('alert_candidates.json', alert_payload)
    replay_input.update({'requests': client.records, 'expected_baseline': baseline_output,
                         'expected_all_rows': captured['rows']})
    atomic_json('runtime/replay-' + scan_id + '.json.gz', replay_input)
    if os.getenv('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as f:
            f.write(text)
    print(json.dumps({'scan_id': scan_id, 'health': health['status'], 'markets': len(markets),
                      'buys': [r['market'] for r in buys], 'journal': str(journal)}, ensure_ascii=False), flush=True)
    return 0 if health['status'] == 'OK' else 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--evaluate-only', action='store_true')
    args = parser.parse_args()
    if args.evaluate_only:
        atomic_json('evaluation.json', evaluate(rebuild('history', connect())))
        return 0
    try:
        return run()
    except Exception as exc:
        atomic_json('pipeline_health.json', {'status': 'FAILED', 'failed_at_utc': utc(),
                                           'error_type': type(exc).__name__, 'reason': str(exc)})
        raise


if __name__ == '__main__':
    raise SystemExit(main())
