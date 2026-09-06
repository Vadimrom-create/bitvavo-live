#!/usr/bin/env python3
"""Bitvavo scanner V4: opportunity selection separated from entry timing."""
from __future__ import annotations

import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

from v3_common import LIVE, f, maybe, pct, load_history as load_v3_history, trajectory, enrich_market, clamp
from v3_scoring import burst_score, slow_score, continuation_score
from v4_common import (
    CORE_MARKETS, V4_HISTORY, V4_HISTORY_RETENTION_SEC, V4_SIGNAL_LOG, V4_SIGNAL_RETENTION_SEC,
    V4_WATCH_JSON, V4_WATCH_SEC, V4_WATCH_TXT, add_relative_strength, liquidity_score,
    load_config, load_v4_history, persistence_score, refresh_trend_cache,
    save_json, suggested_trade_plan, trend_score,
)

OPPORTUNITY_WATCH = 7.20
OPPORTUNITY_STRONG = 8.00
ENTRY_WINDOW = 6.20
ENTRY_READY = 7.00
BUY_OPPORTUNITY = 8.20
CONFIRMATIONS_REQUIRED = 2
ENTRY_ENRICH_COUNT = 72
TREND_UNIVERSE_CAP = 120
OUTPUT_COUNT = 50


def num(x, default=None):
    try:
        return float(x)
    except Exception:
        return default


def entry_score(row: dict, e: dict, profile: dict, opportunity: float) -> tuple[float, list[str], list[str], str]:
    s = 4.7
    flags: list[str] = []
    hard: list[str] = []
    entry_mode = 'MOMENTUM'
    vol = f(row.get('quote_volume_24h_eur'))
    spread = f(row.get('spread_pct'), 99)
    ch24 = f(row.get('change_24h_pct'))

    if vol >= 1_000_000: s += 0.65
    elif vol >= 250_000: s += 0.45
    elif vol >= 75_000: s += 0.20
    elif vol < 12_000: hard.append('ILLIQUID')
    elif vol < 30_000: flags.append('LOW_LIQUIDITY'); s -= 0.55

    if spread <= 0.05: s += 0.65
    elif spread <= 0.12: s += 0.45
    elif spread <= 0.25: s += 0.15
    elif spread > 0.80: hard.append('WIDE_SPREAD')
    elif spread > 0.40: flags.append('WIDE_SPREAD_RISK'); s -= 0.80
    else: flags.append('SPREAD_RISK'); s -= 0.30

    b = e.get('book') or {}
    bid = maybe(b.get('bid_share'))
    if bid is not None:
        if bid >= 0.58: s += 0.45
        elif bid >= 0.45: s += 0.20
        elif bid < 0.20: flags.append('VERY_SELLER_HEAVY_BOOK'); s -= 0.75
        elif bid < 0.30: flags.append('SELLER_HEAVY_BOOK'); s -= 0.35
    else:
        flags.append('NO_BOOK')

    s5, s15, s1h, s4h = (e.get('5m') or {}, e.get('15m') or {}, e.get('1h') or {}, e.get('4h') or {})
    c5, c15 = f(s5.get('ch1')), f(s15.get('ch1'))
    c15_4, c1h_4, c4h_4 = f(s15.get('ch4')), f(s1h.get('ch4')), f(s4h.get('ch4'))
    w5, w15 = f(s5.get('wick')), f(s15.get('wick'))
    d5, d15 = f(s5.get('dist8high'), -99), f(s15.get('dist8high'), -99)
    vr5, vr15 = maybe(s5.get('vr4')), maybe(s15.get('vr4'))

    true_hei = max(w5, w15) >= 0.90 and ((d5 < -1.6 and c5 < -0.2) or (d15 < -1.8 and c15 < -0.25))
    if true_hei:
        hard.append('HEI_REJECTION')
    elif max(w5, w15) >= 0.84:
        flags.append('WICK_SETUP'); s -= 0.15

    if 0.05 <= c15_4 <= 3.5: s += 0.45
    if 0.10 <= c1h_4 <= 6.0: s += 0.45
    if -0.5 <= c4h_4 <= 10.0: s += 0.25
    if vr5 is not None and 1.1 <= vr5 <= 12: s += 0.25
    if vr15 is not None and 1.05 <= vr15 <= 10: s += 0.25

    tscore = trend_score(profile)
    if tscore >= 7.8 and -1.8 <= c15_4 <= 0.20 and c1h_4 > -1.0 and c4h_4 > 0:
        s += 0.65
        entry_mode = 'PULLBACK'
    breakout20 = maybe(profile.get('breakout20_pct')) if profile else None
    if breakout20 is not None and -1.5 <= breakout20 <= 3.5 and c15_4 > 0.10:
        s += 0.35
        entry_mode = 'BREAKOUT' if entry_mode == 'MOMENTUM' else entry_mode

    if ch24 > 25:
        hard.append('TOO_LATE_24H')
    elif ch24 > 15:
        flags.append('EXTENDED_24H'); s -= 0.55
    if f(s15.get('ch16')) > 12 or f(s1h.get('ch16')) > 20:
        flags.append('VERTICAL_SHORT_TERM'); s -= 0.45

    if opportunity >= 9.0 and not hard:
        s += 0.20
    return round(clamp(s), 3), flags, hard, entry_mode


def load_signal_log() -> dict:
    try:
        d = json.loads(V4_SIGNAL_LOG.read_text(encoding='utf-8')) if V4_SIGNAL_LOG.exists() else {}
    except Exception:
        d = {}
    if not isinstance(d, dict): d = {}
    d['version'] = 4
    d.setdefault('events', [])
    return d


def update_signal_log(log: dict, rows_by_market: dict, now_ts: float, generated: str) -> dict:
    events = [e for e in log.get('events', []) if now_ts - f(e.get('created_ts')) <= V4_SIGNAL_RETENTION_SEC]
    for event in events:
        row = rows_by_market.get(event.get('market'))
        if not row: continue
        first = f(event.get('first_price'))
        last = f(row.get('last'))
        event['last_seen_utc'] = generated
        event['last_price'] = last
        event['pct_now'] = round(pct(last, first) or 0, 4) if first else None
        event['max_price'] = max(f(event.get('max_price'), last), last)
        old_min = maybe(event.get('min_price'))
        event['min_price'] = min(old_min if old_min is not None else last, last)
        event['mfe_pct'] = round(pct(f(event['max_price']), first) or 0, 4) if first else None
        event['mae_pct'] = round(pct(f(event['min_price']), first) or 0, 4) if first else None
        elapsed = now_ts - f(event.get('created_ts'))
        cps = event.setdefault('checkpoints', {})
        for label, sec in (('30m',1800),('1h',3600),('3h',10800),('6h',21600),('12h',43200),('24h',86400),('3d',259200),('7d',604800),('14d',1209600)):
            if elapsed >= sec and label not in cps and first:
                cps[label] = {'ts_utc': generated, 'price': last, 'pct': round(pct(last, first) or 0, 4)}
        if elapsed >= 14 * 86400:
            event['status'] = 'CLOSED'

    active = {e['market']: e for e in events if e.get('status') == 'ACTIVE'}
    for market, row in rows_by_market.items():
        if f(row.get('opportunity_score')) < OPPORTUNITY_WATCH:
            continue
        if market in active and now_ts - f(active[market].get('created_ts')) < 7 * 86400:
            continue
        last = f(row.get('last'))
        events.append({
            'market': market, 'created_ts': now_ts, 'first_seen_utc': generated,
            'first_price': last, 'first_opportunity_score': row.get('opportunity_score'),
            'first_entry_score': row.get('entry_score'), 'first_status': row.get('action_status'),
            'trend_score': row.get('trend_score'), 'last_seen_utc': generated, 'last_price': last,
            'max_price': last, 'min_price': last, 'pct_now': 0.0, 'mfe_pct': 0.0, 'mae_pct': 0.0,
            'status': 'ACTIVE', 'checkpoints': {},
        })
    log['generated_at_utc'] = generated
    log['events'] = events
    return log


def fmt(x, digits=2):
    if x is None: return 'n/a'
    try: return f'{float(x):.{digits}f}'
    except Exception: return str(x)


def main():
    live = json.loads(Path(LIVE).read_text(encoding='utf-8'))
    rows = [r for r in live.get('markets', []) if isinstance(r, dict) and r.get('market')]
    generated = live.get('generated_at_utc') or datetime.now(timezone.utc).isoformat()
    try: now_ts = datetime.fromisoformat(generated.replace('Z','+00:00')).timestamp()
    except Exception: now_ts = time.time()

    v3_history = load_v3_history()
    v4_history = load_v4_history()
    hm4_all = v4_history['markets']

    for rank, row in enumerate(rows, 1):
        hm3 = v3_history.get('markets', {}).get(row['market'], {})
        t = trajectory(row, rank, hm3, now_ts)
        row['current_rank'] = rank
        row['trajectory'] = t
        row['ignition_scores'] = {
            'burst': burst_score(row, t),
            'slow': slow_score(row, t),
            'continuation': continuation_score(row, t, hm3),
        }
        row['ignition_score'] = max(row['ignition_scores'].values())

    names = {r['market'] for r in rows}
    active_names = {m for m,h in hm4_all.items() if f(h.get('watch_until_ts')) > now_ts}
    top_ign = [r['market'] for r in sorted(rows, key=lambda x: f(x.get('ignition_score')), reverse=True)[:55]]
    top_liq = [r['market'] for r in sorted(rows, key=lambda x: f(x.get('quote_volume_24h_eur')), reverse=True)[:35]]
    trend_universe = list(dict.fromkeys(
        ['BTC-EUR','ETH-EUR'] + top_ign + top_liq + list(active_names) + [m for m in CORE_MARKETS if m in names]
    ))[:TREND_UNIVERSE_CAP]
    cache = refresh_trend_cache(trend_universe, now_ts)
    add_relative_strength(cache)
    profiles = cache.get('markets', {})

    for row in rows:
        profile = profiles.get(row['market'], {})
        tr = trend_score(profile)
        ign = f(row.get('ignition_score'))
        hm4 = hm4_all.setdefault(row['market'], {})
        pers = persistence_score(hm4, now_ts)
        liq = liquidity_score(row)
        ignition_path = 0.60 * ign + 0.25 * tr + 0.10 * pers + 0.05 * liq
        trend_path = 0.66 * tr + 0.22 * ign + 0.08 * pers + 0.04 * liq
        opportunity = round(clamp(max(ignition_path, trend_path)), 3)
        row['trend_profile'] = profile
        row['trend_score'] = tr
        row['opportunity_score'] = opportunity

    ranked_opp = sorted(rows, key=lambda r: f(r.get('opportunity_score')), reverse=True)
    selected_names = []
    for group in (
        [r['market'] for r in ranked_opp[:55]],
        [m for m in active_names if m in names],
        [m for m in CORE_MARKETS if m in names],
    ):
        for m in group:
            if m not in selected_names:
                selected_names.append(m)
            if len(selected_names) >= ENTRY_ENRICH_COUNT: break
        if len(selected_names) >= ENTRY_ENRICH_COUNT: break
    selected = [next(r for r in rows if r['market'] == m) for m in selected_names]
    live_details = live.get('details') or {}
    enriched = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        futs = [pool.submit(enrich_market, r['market'], live_details) for r in selected]
        for fut in as_completed(futs):
            market, data = fut.result(); enriched[market] = data

    for row in rows:
        market = row['market']
        hm = hm4_all.setdefault(market, {})
        opp = f(row.get('opportunity_score'))
        profile = row.get('trend_profile') or {}
        e = enriched.get(market, {})
        if market in enriched:
            ent, flags, hard, entry_mode = entry_score(row, e, profile, opp)
        else:
            ent, flags, hard, entry_mode = 4.5, ['NOT_ENTRY_ENRICHED'], [], 'UNKNOWN'
        row['entry_score'] = ent
        row['risk_flags'] = flags + hard
        row['entry_mode'] = entry_mode

        if opp >= OPPORTUNITY_WATCH:
            if not hm.get('first_signal_ts') or now_ts - f(hm.get('first_signal_ts')) > V4_WATCH_SEC:
                hm['first_signal_ts'] = now_ts
                hm['first_signal_seen'] = generated
                hm['first_signal_price'] = row.get('last')
                hm['opportunity_confirm_count'] = 1
            else:
                last_confirm_ts = f(hm.get('last_confirm_ts'))
                if now_ts - last_confirm_ts >= 180:
                    hm['opportunity_confirm_count'] = int(f(hm.get('opportunity_confirm_count'))) + 1
            hm['last_confirm_ts'] = now_ts
            hm['watch_until_ts'] = now_ts + V4_WATCH_SEC
        elif opp < 6.4 and f(hm.get('watch_until_ts')) < now_ts:
            hm['opportunity_confirm_count'] = 0

        first_price = maybe(hm.get('first_signal_price'))
        last = f(row.get('last'))
        if first_price:
            hm['peak_since_signal'] = max(f(hm.get('peak_since_signal'), first_price), last)
            old_trough = maybe(hm.get('trough_since_signal'))
            hm['trough_since_signal'] = min(old_trough if old_trough is not None else first_price, last)
            row['since_first_signal_pct'] = round(pct(last, first_price) or 0, 4)
        else:
            row['since_first_signal_pct'] = None

        confirms = int(f(hm.get('opportunity_confirm_count')))
        buy_ready = False
        action = 'NONE'
        if opp >= OPPORTUNITY_WATCH:
            action = 'WATCH'
        if opp >= OPPORTUNITY_STRONG and ent >= ENTRY_WINDOW:
            action = 'ENTRY_WINDOW'
        if hard:
            action = 'TOO_LATE' if any(x.startswith('TOO_LATE') for x in hard) else 'WATCH_RISK'
        elif opp >= BUY_OPPORTUNITY and ent >= ENTRY_READY and confirms >= CONFIRMATIONS_REQUIRED:
            action = 'BUY_READY'; buy_ready = True

        peak = maybe(hm.get('peak_since_signal'))
        drawdown = pct(last, peak) if peak else None
        s15 = e.get('15m') or {}
        rebound = f(s15.get('ch4')) > 0.15 and f((e.get('1h') or {}).get('ch4')) > -1.0
        if hm.get('ever_buy_ready') and not hard and opp >= 8.0 and ent >= 6.8 and drawdown is not None and -7.5 <= drawdown <= -0.8 and rebound:
            action = 'REENTRY_READY'; buy_ready = True
            row['reentry_reason'] = f'clean reset {drawdown:.2f}% from post-signal peak + rebound'

        if buy_ready:
            hm['ever_buy_ready'] = True
            hm['last_buy_ready_ts'] = now_ts
        hm['last_opportunity_score'] = opp
        hm['last_entry_score'] = ent
        hm['last_action_status'] = action
        row['confirm_count'] = confirms
        row['action_status'] = action
        row['buy_ready'] = buy_ready
        row['trade_plan'] = suggested_trade_plan(row, profile, opp, ent) if action in {'BUY_READY','REENTRY_READY','ENTRY_WINDOW'} else None

    for market in list(hm4_all):
        hm = hm4_all[market]
        if f(hm.get('watch_until_ts')) < now_ts - V4_HISTORY_RETENTION_SEC:
            hm4_all.pop(market, None)
    v4_history['generated_at_utc'] = generated
    save_json(V4_HISTORY, v4_history)

    rows_by_market = {r['market']: r for r in rows}
    siglog = update_signal_log(load_signal_log(), rows_by_market, now_ts, generated)
    save_json(V4_SIGNAL_LOG, siglog)

    status_rank = {'BUY_READY':5,'REENTRY_READY':5,'ENTRY_WINDOW':4,'WATCH':3,'WATCH_RISK':2,'TOO_LATE':1,'NONE':0}
    out_rows = sorted(
        [r for r in rows if f(r.get('opportunity_score')) >= 6.5 or r.get('action_status') != 'NONE'],
        key=lambda r: (status_rank.get(r.get('action_status'),0), f(r.get('opportunity_score')), f(r.get('entry_score'))),
        reverse=True,
    )[:OUTPUT_COUNT]

    signal_first = {}
    for ev in siglog.get('events', []):
        m = ev.get('market')
        if m and (m not in signal_first or f(ev.get('created_ts')) < f(signal_first[m].get('created_ts'))):
            signal_first[m] = ev
    eligible = [r for r in rows if f(r.get('quote_volume_24h_eur')) >= 75_000 and r['market'] in profiles]
    audit7, audit30 = [], []
    for days, bucket in ((7,audit7),(30,audit30)):
        key = f'ret{days}d'
        for r in sorted(eligible, key=lambda x: f((profiles.get(x['market']) or {}).get(key), -999), reverse=True)[:15]:
            ev = signal_first.get(r['market'])
            bucket.append({
                'market': r['market'], 'return_pct': (profiles.get(r['market']) or {}).get(key),
                'rs_btc_pct': (profiles.get(r['market']) or {}).get(f'rs_btc_{days}d'),
                'opportunity_score': r.get('opportunity_score'), 'entry_score': r.get('entry_score'),
                'first_v4_signal': ev.get('first_seen_utc') if ev else None,
                'first_v4_price': ev.get('first_price') if ev else None,
                'gain_since_v4_signal_pct': round(pct(f(r.get('last')), f(ev.get('first_price'))) or 0,4) if ev else None,
            })

    cfg = load_config()
    payload = {
        'generated_at_utc': generated, 'version': 4,
        'method_note': 'V4 separates OPPORTUNITY (asset selection) from ENTRY (timing), adds 90d daily trend/relative-strength context, 7d persistent watch, re-entry logic and 7d/30d winner audit.',
        'goal_context': {
            'portfolio_target_eur': cfg.get('portfolio_target_eur'), 'estimated_cash_eur': cfg.get('estimated_cash_eur'),
            'target_gain_eur': cfg.get('target_gain_eur'),
            'note': 'Goal affects sizing guardrails only; it never inflates signal scores.'
        },
        'watch': out_rows,
        'enriched': {r['market']: enriched.get(r['market'], {}) for r in out_rows if r['market'] in enriched},
        'winner_audit_7d': audit7, 'winner_audit_30d': audit30,
    }
    save_json(V4_WATCH_JSON, payload)

    lines = [
        'BITVAVO SCAN V4 — OPPORTUNITY + ENTRY',
        f'generated_at_utc: {generated}',
        f"goal: target={cfg.get('portfolio_target_eur')} EUR | cash~{cfg.get('estimated_cash_eur')} EUR | gain_needed~{cfg.get('target_gain_eur')} EUR",
        'NOTE: Opportunity selects the horse. Entry decides whether to buy now. Book/wicks can delay entry without deleting the opportunity.',
        'rank | market | action | opportunity | entry | trend | ignition[b,s,c] | confirms | last | ch24 | ret7 | ret30 | rsBTC7 | rsBTC30 | since_signal | vol24 | spread | bid_share | entry_mode | flags | stake | stopGuide',
    ]
    for i,r in enumerate(out_rows,1):
        p = r.get('trend_profile') or {}; e = enriched.get(r['market'],{}); b=e.get('book') or {}; sc=r.get('ignition_scores') or {}; plan=r.get('trade_plan') or {}
        lines.append(
            f"{i} | {r['market']} | {r.get('action_status')} | {fmt(r.get('opportunity_score'),3)} | {fmt(r.get('entry_score'),3)} | {fmt(r.get('trend_score'),3)} | "
            f"[{fmt(sc.get('burst'))},{fmt(sc.get('slow'))},{fmt(sc.get('continuation'))}] | {r.get('confirm_count')} | {r.get('last')} | {fmt(r.get('change_24h_pct'))}% | "
            f"{fmt(p.get('ret7d'))}% | {fmt(p.get('ret30d'))}% | {fmt(p.get('rs_btc_7d'))}% | {fmt(p.get('rs_btc_30d'))}% | {fmt(r.get('since_first_signal_pct'))}% | "
            f"{fmt(r.get('quote_volume_24h_eur'),0)} | {fmt(r.get('spread_pct'),4)}% | {fmt(b.get('bid_share'),3)} | {r.get('entry_mode')} | {','.join(r.get('risk_flags') or []) or '-'} | "
            f"{fmt(plan.get('suggested_stake_eur'),0)} EUR | {fmt(plan.get('structural_stop_guide_pct'))}%"
        )
    lines += ['', 'WINNER_AUDIT_7D']
    for a in audit7:
        lines.append(f"{a['market']} | ret7={fmt(a['return_pct'])}% | rsBTC7={fmt(a['rs_btc_pct'])}% | opp={fmt(a['opportunity_score'])} | entry={fmt(a['entry_score'])} | firstV4={a['first_v4_signal'] or 'n/a'}")
    lines += ['', 'WINNER_AUDIT_30D']
    for a in audit30:
        lines.append(f"{a['market']} | ret30={fmt(a['return_pct'])}% | rsBTC30={fmt(a['rs_btc_pct'])}% | opp={fmt(a['opportunity_score'])} | entry={fmt(a['entry_score'])} | firstV4={a['first_v4_signal'] or 'n/a'}")
    V4_WATCH_TXT.write_text('\n'.join(lines)+'\n', encoding='utf-8')

    ready = [r['market'] for r in out_rows if r.get('buy_ready')]
    print(f"SCAN V4: {len(rows)} markets | trend_universe={len(trend_universe)} | entry_enriched={len(enriched)} | buy_ready={ready or 'none'}")


if __name__ == '__main__':
    main()
