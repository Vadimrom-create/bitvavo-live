#!/usr/bin/env python3
"""One collect -> V3/V4 -> full-universe journal -> evaluate -> report cycle.

No trading credentials, no private executor and no email are invoked here.
Publication and notification are separate workflow steps after this succeeds.
"""
from __future__ import annotations

import argparse
import copy
from collections import Counter
import hashlib
import importlib.util
import json
import os
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from research.common import INTERVAL_MS, atomic_json, finite, freshness, read_json, timestamp, utc
from research.evaluation import evaluate, market_control
from research.feedback_loop import acceleration_signal
from research.features import category, chase_risk, closed_candles, describe, nil_match, score_components, wick_setup
from research.history import connect, ingest, new_candles, rebuild, recurrent, save_scan
from research.http import PublicClient
from research.risk import correlation, plan, proposed_order

POLICY = 'V4_FROZEN_20260908'
OPERATIONAL_POLICY = 'V4_FROZEN_20260908+ADAPTIVE_ENTRY_V1+TREND_GUARD_V1'
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
                                                'raw_count': len(raw), 'closed_count': len(cs),
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


def _interval_quality_snapshot(tf, interval):
    candles = list(tf.get('candles') or [])
    features = tf.get('features') or {}
    duration = INTERVAL_MS[interval]
    recent = candles[-25:]
    gaps = []
    for left, right in zip(recent, recent[1:]):
        delta = int(right['t']) - int(left['t'])
        steps = delta // duration if delta >= 0 and delta % duration == 0 else None
        if steps != 1:
            missing = max(0, steps - 1) if isinstance(steps, int) else None
            gaps.append({'from_start_ms': int(left['t']), 'to_start_ms': int(right['t']),
                         'missing_intervals': missing})
    span_slots = None
    coverage_pct = None
    if len(recent) >= 2:
        delta = int(recent[-1]['t']) - int(recent[0]['t'])
        if delta >= 0 and delta % duration == 0:
            span_slots = delta // duration + 1
            coverage_pct = round(len(recent) / span_slots * 100, 2) if span_slots else None
    return {
        'raw_count': tf.get('raw_count'),
        'closed_count': tf.get('closed_count', len(candles)),
        'feature_valid': bool(features.get('valid')),
        'feature_reasons': list(features.get('reasons') or []),
        'bars_reported': features.get('bars'),
        'gap_count_last_25_observed': len(gaps),
        'missing_intervals_last_25_observed': sum(g['missing_intervals'] or 0 for g in gaps),
        'largest_missing_run_last_25_observed': max([g['missing_intervals'] or 0 for g in gaps], default=0),
        'coverage_pct_over_span_last_25_observed': coverage_pct,
        'last_closed_start_ms': features.get('last_closed_start_ms'),
        'last_closed_close_ms': features.get('last_closed_close_ms'),
    }


def build_data_quality_audit(observations, universe, scan_id, scan_at_utc):
    quality_reasons = Counter()
    reasons_5m = Counter()
    reasons_15m = Counter()
    combinations = Counter()
    rows = []
    for obs in observations:
        name = obs['market']
        qreasons = tuple(sorted(obs.get('data_quality', {}).get('reasons') or []))
        quality_reasons.update(qreasons)
        combinations[' + '.join(qreasons) if qreasons else 'OK'] += 1
        tf5 = universe[name]['timeframes'].get('5m', {})
        tf15 = universe[name]['timeframes'].get('15m', {})
        d5 = _interval_quality_snapshot(tf5, '5m')
        d15 = _interval_quality_snapshot(tf15, '15m')
        reasons_5m.update(d5['feature_reasons'] or (['MISSING_FEATURES'] if not d5['feature_valid'] else []))
        reasons_15m.update(d15['feature_reasons'] or (['MISSING_FEATURES'] if not d15['feature_valid'] else []))
        baseline = obs.get('baseline') or {}
        ticker = universe[name].get('ticker') or {}
        quote_volume = finite(baseline.get('quote_volume_24h_eur'), finite(ticker.get('volumeQuote'), 0))
        rows.append({
            'market': name,
            'data_quality_ok': bool(obs.get('data_quality', {}).get('ok')),
            'quality_reasons': list(qreasons),
            'change_24h_pct': obs.get('change_24h_pct'),
            'quote_volume_24h_eur': quote_volume,
            'baseline_present': bool(obs.get('baseline')),
            '5m': d5,
            '15m': d15,
        })
    rejected = [r for r in rows if not r['data_quality_ok']]
    return {
        'schema': 'data_quality_audit_v1',
        'scan_id': scan_id,
        'scan_at_utc': scan_at_utc,
        'universe': len(rows),
        'strategy_grade': sum(r['data_quality_ok'] for r in rows),
        'rejected': len(rejected),
        'valid_5m': sum(r['5m']['feature_valid'] for r in rows),
        'valid_15m': sum(r['15m']['feature_valid'] for r in rows),
        'both_intervals_feature_valid': sum(r['5m']['feature_valid'] and r['15m']['feature_valid'] for r in rows),
        'quality_reason_counts': dict(quality_reasons.most_common()),
        'feature_failure_counts_5m': dict(reasons_5m.most_common()),
        'feature_failure_counts_15m': dict(reasons_15m.most_common()),
        'quality_reason_combinations': dict(combinations.most_common()),
        'top_volume_rejected': sorted(rejected, key=lambda r: finite(r['quote_volume_24h_eur'], 0), reverse=True)[:30],
        'top_positive_movers_rejected': sorted(rejected, key=lambda r: finite(r['change_24h_pct'], -1e9), reverse=True)[:30],
        'rows': rows,
        'interpretation_note': 'Observability only: this audit does not change V4 scores, validity rules, alerts or orders.'
    }


def data_quality_audit_text(audit):
    lines = ['# Audit qualité des données Bitvavo', '',
             f"Scan : {audit['scan_at_utc']} ({audit['scan_id']})",
             f"Univers : {audit['universe']} | strategy-grade : {audit['strategy_grade']} | rejetés : {audit['rejected']}",
             f"5m valides : {audit['valid_5m']} | 15m valides : {audit['valid_15m']} | deux intervalles valides : {audit['both_intervals_feature_valid']}", '',
             '## Causes de rejet globales', '', '| Cause | Marchés |', '|---|---:|']
    for reason, count in audit['quality_reason_counts'].items():
        lines.append(f'| {reason} | {count} |')
    lines += ['', '## Causes intrinsèques 5m', '', '| Cause | Marchés |', '|---|---:|']
    for reason, count in audit['feature_failure_counts_5m'].items():
        lines.append(f'| {reason} | {count} |')
    lines += ['', '## Causes intrinsèques 15m', '', '| Cause | Marchés |', '|---|---:|']
    for reason, count in audit['feature_failure_counts_15m'].items():
        lines.append(f'| {reason} | {count} |')
    lines += ['', '## Marchés rejetés les plus liquides', '',
              '| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |',
              '|---|---:|---:|---|---:|---:|']
    for row in audit['top_volume_rejected'][:20]:
        m5, m15 = row['5m'], row['15m']
        ch = row['change_24h_pct']
        chs = f'{ch:+.2f}%' if isinstance(ch, (int, float)) else 'n/a'
        lines.append(f"| {row['market']} | {finite(row['quote_volume_24h_eur'], 0):.0f} | {chs} | {', '.join(row['quality_reasons'])} | {m5['closed_count']}/{m5['missing_intervals_last_25_observed']} | {m15['closed_count']}/{m15['missing_intervals_last_25_observed']} |")
    lines += ['', 'Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.',
              'Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.', '']
    return '\n'.join(lines)


def report_text(report):
    h = report['health']
    lines = ['# Bitvavo — V4 mesurée / infrastructure V5', '',
             f"Scan UTC : {report['scan_at_utc']}",
             f"État : {h['status']} | marchés EUR : {h['universe']} | V4 : {h['baseline_analyzed']} | données valides : {h['valid_markets']}",
             f"Récupération : {h['collected_at_utc']} | âge ticker : {h['ticker_age_seconds']:.1f} s | durée : {h['duration_seconds']:.1f} s", '',
             '## ACHÈTE — signal V4 et plan théorique', '']
    buys = report['buy']
    if not buys:
        lines.append('AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.' if h['status'] == 'OK' else 'SCAN INCOMPLET — aucune recommandation d’achat publiée')
    lines += [f"Bougies utilisables : 5 min {h.get('valid_5m', 0)}/{h['universe']} ; 15 min {h.get('valid_15m', 0)}/{h['universe']}.",
              'Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.']
    if report.get('blocked_baseline_buys'):
        lines += ['', 'Achats bruts V4 bloqués avant alerte :']
        for row in report['blocked_baseline_buys']:
            lines.append(f"- {row['market']} : {', '.join(row['exclusions'])}")
    for obs in buys:
        p, b = obs['trade_plan'], obs['baseline']
        lines += [f"- {obs['market']} : {obs['price_eur']:.8g} € | {obs['category']} | score {b['opportunity_score'] * 10:.2f}/100 | entrée {b['entry_score']:.2f}/10",
                  f"  Entrée {p['entry_eur']:.8g} € ; stop {p['stop_eur']:.8g} € ; TP1 {p['tp1_eur']:.8g} € ; TP2 {p['tp2_eur']:.8g} € ; montant {p['stake_eur']:.2f} € ; risque théorique {p['theoretical_loss_eur']:.2f} € ; R/R net {p['net_rr_tp1']:.2f}.",
                  f"  Chase risk : {obs['chase_risk']['score']}/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles."]
    lines += ['', '## SURVEILLE', '']
    for obs in report['watch']:
        lines.append(f"- {obs['market']} : {obs['price_eur']:.8g} € ; score {(obs.get('baseline') or {}).get('opportunity_score', 0) * 10:.2f}/100 ; {obs['decision']} ; {', '.join(obs['exclusions']) or 'seuil achat non atteint'}")
    lines += ['', '## Contrôle des hausses', '',
              '| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |',
              '|---|---:|---:|---|---|---|']
    for r in report['market_control'][:10]:
        lines.append(f"| {r['market']} | {r['price_eur']:.8g} | {r['change_24h_pct']:+.2f} % | {r['detection_state']} | {r['failure_layer']} | {r['actionability_layer']} |")
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
    from research.trend_cache_guard import ensure_fresh_trend_cache
    trend_guard = ensure_fresh_trend_cache(
        client,
        [r.get('market') for r in live.get('markets', []) if isinstance(r, dict) and r.get('market')],
        timestamp(live['generated_at_utc']),
    )
    # Replay must start from the actually refreshed cache state used by V4.
    before['v4_trend_cache.json'] = read_json('v4_trend_cache.json', {})
    print('TREND_CACHE_GUARD ' + json.dumps(trend_guard, ensure_ascii=False), flush=True)
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
    # Preserve the exact frozen V4 raw output before the operational adaptive layer.
    frozen_raw_baseline = copy.deepcopy(read_json('v4_watch.json'))
    from research.adaptive_entry import promote_and_enrich, patch_watch_output
    adaptive_audit = promote_and_enrich(
        captured['rows'], captured['enriched'], captured['generated_at_utc'],
        captured['scan_ts'], live.get('details') or {}
    )
    patch_watch_output(captured['rows'], captured['enriched'], adaptive_audit)
    print('ADAPTIVE_ENTRY ' + json.dumps({
        'promoted': adaptive_audit.get('promoted_count'),
        'total_enriched': adaptive_audit.get('total_enriched_count'),
    }, ensure_ascii=False), flush=True)
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
            # Entry enrichment is a selection/capability state, not market-data quality.
            # Only a real enrichment error belongs in data_quality.
            if e.get('error'):
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
        entry_enrichment = (
            'ERROR' if baseline and (captured['enriched'].get(name) or {}).get('error')
            else 'AVAILABLE' if baseline and name in captured['enriched']
            else 'NOT_SELECTED' if baseline
            else 'NOT_APPLICABLE'
        )
        obs = {'market': name, 'price_eur': last, 'change_24h_pct': change24, 'baseline': baseline,
               'category': cls, 'features': {'5m': m5.get('features'), '15m': features},
               'entry_enrichment': entry_enrichment,
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
        # Independent shadow path: it may restore a market to the persistent
        # watchlist, but it never changes V4 scoring or the email payload.
        obs['acceleration'] = acceleration_signal(obs)
        observations.append(obs)
        candles5[name] = m5.get('candles', [])
    # Portfolio limits apply cumulatively to the same theoretical order batch.
    buys, used = [], {'exposure': 0, 'risk': 0, 'positions': 0}
    for obs in sorted(observations, key=lambda o: (o.get('baseline') or {}).get('opportunity_score', 0), reverse=True):
        if not (obs.get('baseline') or {}).get('buy_ready') or not obs['data_quality']['ok']:
            continue
        if obs['category'] == 'TOO LATE':
            # Preserve the raw V4 decision, but do not publish a contradictory
            # buy if its own chase/too-late flag survived the re-entry path.
            obs['decision'] = 'TOO LATE'
            obs['exclusions'].append('BASELINE_BUY_CHASE_CONTRADICTION')
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
              'valid_5m': sum(bool((o['features'].get('5m') or {}).get('valid')) for o in observations),
              'valid_15m': sum(bool((o['features'].get('15m') or {}).get('valid')) for o in observations),
              'quality_scope': 'OK describes collection execution; per-market admissibility is separate',
              'collected_at_utc': live['generated_at_utc'], 'ticker_age_seconds': finish - timestamp(ticker_at),
              'duration_seconds': finish - start, 'api_error_count': len(client.errors),
              'api_errors': client.errors, 'exchange_clock_offset_seconds': client.server_offset,
              'trend_cache_guard': trend_guard,
              'ignored_markets': [{'market': m['market'], 'reason': m.get('status')} for m in markets_raw if m.get('quote') == 'EUR' and m.get('status') != 'trading']}
    if health['ticker_age_seconds'] > 300 or not markets or len(captured['rows']) < .5 * len(markets):
        health['status'] = 'DEGRADED'
        for obs in buys:
            obs['decision'] = 'DATA UNAVAILABLE'
            obs['exclusions'].append('PIPELINE_DEGRADED')
        buys = []
    scan = {'schema_version': 2, 'scan_id': scan_id, 'scan_ts': baseline_ts, 'scan_at_utc': utc(baseline_ts),
            'policy': POLICY, 'operational_policy': OPERATIONAL_POLICY,
            'source_commit': os.getenv('GITHUB_SHA'), 'source': 'live',
            'observations': observations, 'candles_5m': new_candles(db, candles5),
            'candle_storage': 'FIRST_SEEN_DELTA_REBUILD_ALL_JOURNALS',
            'health': health, 'baseline_input_policy': 'legacy includes forming candles; closed diagnostics never change V4 scoring'}
    journal = save_scan('history', scan)
    ingest(db, scan)
    evaluation = evaluate(db)
    candles15 = {name: data['timeframes'].get('15m', {}).get('candles', [])
                 for name, data in universe.items()}
    control = market_control(db, observations, baseline_ts, candles15)
    watch = sorted([o for o in observations if o['decision'] == 'SURVEILLE'],
                   key=lambda o: (o.get('baseline') or {}).get('opportunity_score', 0), reverse=True)[:5]
    funnel = {
        'schema': 'decision_funnel_v1',
        'scan_id': scan_id,
        'operational_policy': OPERATIONAL_POLICY,
        'source_commit': os.getenv('GITHUB_SHA'),
        'active_eur_markets': len(markets),
        'legacy_collector_markets': len(live.get('markets', [])),
        'v4_scored_markets': len(captured['rows']),
        'v4_base_entry_enriched': adaptive_audit.get('base_enriched_count'),
        'adaptive_candidates': adaptive_audit.get('candidate_count'),
        'adaptive_promoted': adaptive_audit.get('promoted_count'),
        'total_entry_enriched': adaptive_audit.get('total_enriched_count'),
        'valid_5m': sum(bool((o['features'].get('5m') or {}).get('valid')) for o in observations),
        'valid_15m': sum(bool((o['features'].get('15m') or {}).get('valid')) for o in observations),
        'data_quality_ok': sum(o['data_quality']['ok'] for o in observations),
        'v4_watch_or_better': sum((o.get('baseline') or {}).get('action_status') in {'WATCH','ENTRY_WINDOW','BUY_READY','REENTRY_READY'} for o in observations),
        'v4_entry_window_or_better': sum((o.get('baseline') or {}).get('action_status') in {'ENTRY_WINDOW','BUY_READY','REENTRY_READY'} for o in observations),
        'v4_buy_ready': sum(bool((o.get('baseline') or {}).get('buy_ready')) for o in observations),
        'final_buy': len(buys),
        'drop_reason_counts': dict(Counter(reason for o in observations for reason in o.get('exclusions', []))),
    }
    atomic_json('decision_funnel.json', funnel)
    report = {'scan_id': scan_id, 'scan_at_utc': utc(baseline_ts),
              'operational_policy': OPERATIONAL_POLICY, 'source_commit': os.getenv('GITHUB_SHA'),
              'health': health, 'decision_funnel': funnel, 'buy': buys, 'watch': watch,
              'blocked_baseline_buys': [{'market': o['market'], 'exclusions': o['exclusions']} for o in observations
                                      if (o.get('baseline') or {}).get('buy_ready') and o not in buys],
              'market_control': control, 'evaluation': evaluation, 'journal_path': str(journal),
              'orders': [proposed_order(o['trade_plan'], scan_id) for o in buys]}
    atomic_json('v5_report.json', report)
    text = report_text(report)
    Path('v5_report.md').write_text(text, encoding='utf-8')
    atomic_json('pipeline_health.json', health)
    data_quality_audit = build_data_quality_audit(observations, universe, scan_id, utc(baseline_ts))
    atomic_json('data_quality_audit.json', data_quality_audit)
    Path('data_quality_audit.md').write_text(data_quality_audit_text(data_quality_audit), encoding='utf-8')
    atomic_json('evaluation.json', evaluation)
    atomic_json('proposed_orders.json', {'dry_run': True, 'orders': report['orders']})
    # Preserve raw baseline public outputs for audit; provide a separate, fresh,
    # quality-checked payload to the existing alert transport.
    alert_payload = {**baseline_output, 'generated_at_utc': utc(baseline_ts),
                     'watch': [{**o['baseline'], 'data_quality': o['data_quality'], 'trade_plan': o['trade_plan']} for o in buys]}
    atomic_json('alert_candidates.json', alert_payload)
    replay_input.update({'requests': client.records,
                         'expected_raw_baseline': frozen_raw_baseline,
                         'expected_baseline': baseline_output,
                         'expected_all_rows': captured['rows']})
    atomic_json('runtime/replay-' + scan_id + '.json.gz', replay_input)
    if os.getenv('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as f:
            f.write(text)
    print(json.dumps({'scan_id': scan_id, 'health': health['status'], 'markets': len(markets),
                      'buys': [r['market'] for r in buys], 'journal': str(journal)}, ensure_ascii=False), flush=True)
    print(text, flush=True)
    print('BASELINE_BUY_AUDIT ' + json.dumps([
        {'market': o['market'], 'decision': o['decision'], 'exclusions': o['exclusions'],
         'trade_plan': o['trade_plan']} for o in observations if (o.get('baseline') or {}).get('buy_ready')
    ], ensure_ascii=False), flush=True)
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
