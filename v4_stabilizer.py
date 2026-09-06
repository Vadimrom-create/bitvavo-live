#!/usr/bin/env python3
"""Stabilize V4 decisions so 5-minute noise cannot flip actionable recommendations.

The raw scanner remains fully observable in v4_watch_raw.{json,txt}. This layer only
stabilizes the decision state. Hard invalidations still revoke immediately.
"""
from __future__ import annotations

import json
import shutil
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

from v3_common import f, maybe, pct
from v4_common import suggested_trade_plan, trend_score

WATCH_JSON = Path('v4_watch.json')
WATCH_TXT = Path('v4_watch.txt')
RAW_JSON = Path('v4_watch_raw.json')
RAW_TXT = Path('v4_watch_raw.txt')
HISTORY = Path('v4_history.json')
LIVE = Path('bitvavo_live.json')
TREND = Path('v4_trend_cache.json')
STATE = Path('v4_stability_state.json')

BUY_HOLD_SEC = 15 * 60
DOWNGRADE_SCANS_REQUIRED = 2
BUY_OPP_FLOOR = 8.20
BUY_ENTRY_FLOOR = 7.00
EMERGENCY_ENTRY_FLOOR = 5.50
RECENT_BUY_TRACK_SEC = 2 * 3600
MAX_OUTPUT = 50

HARD_ACTIONS = {'TOO_LATE', 'WATCH_RISK'}
HARD_FLAGS = {'HEI_REJECTION', 'TOO_LATE_24H', 'ILLIQUID', 'WIDE_SPREAD'}


def load(path: Path, default):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return default


def save(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')


def parse_ts(value) -> float:
    try:
        return datetime.fromisoformat(str(value).replace('Z', '+00:00')).timestamp()
    except Exception:
        return 0.0


def live_by_market(payload: dict) -> dict:
    return {r.get('market'): r for r in payload.get('markets', []) if isinstance(r, dict) and r.get('market')}


def synthetic_row(market: str, hist: dict, live_row: dict, profile: dict) -> dict:
    row = deepcopy(live_row) if isinstance(live_row, dict) else {'market': market}
    row['market'] = market
    opp = f(hist.get('last_opportunity_score'))
    ent = f(hist.get('last_entry_score'))
    row['trend_profile'] = profile or {}
    row['trend_score'] = trend_score(profile or {})
    row['opportunity_score'] = opp
    row['entry_score'] = ent
    row['confirm_count'] = int(f(hist.get('opportunity_confirm_count')))
    first = maybe(hist.get('first_signal_price'))
    last = f(row.get('last'))
    row['since_first_signal_pct'] = round(pct(last, first) or 0, 4) if first and last else None
    row['entry_mode'] = 'STABILITY_HOLD'
    row['risk_flags'] = []
    row['action_status'] = hist.get('last_action_status') or 'NONE'
    row['buy_ready'] = False
    try:
        row['trade_plan'] = suggested_trade_plan(row, profile or {}, opp, ent)
    except Exception:
        row['trade_plan'] = None
    return row


def rank_value(action: str) -> int:
    return {'BUY_READY': 6, 'REENTRY_READY': 6, 'ENTRY_WINDOW': 5, 'WATCH': 4,
            'WATCH_RISK': 2, 'TOO_LATE': 1, 'NONE': 0}.get(action, 0)


def main() -> int:
    raw = load(WATCH_JSON, {})
    if not raw or not isinstance(raw.get('watch'), list):
        print('V4_STABILITY_SKIPPED invalid_watch')
        return 0

    shutil.copyfile(WATCH_JSON, RAW_JSON)
    if WATCH_TXT.exists():
        shutil.copyfile(WATCH_TXT, RAW_TXT)

    generated = raw.get('generated_at_utc') or datetime.now(timezone.utc).isoformat()
    now_ts = parse_ts(generated)
    history = load(HISTORY, {}).get('markets', {})
    live = live_by_market(load(LIVE, {}))
    profiles = load(TREND, {}).get('markets', {})
    state = load(STATE, {'version': 1, 'markets': {}})
    state.setdefault('markets', {})

    raw_rows = {r.get('market'): deepcopy(r) for r in raw.get('watch', []) if isinstance(r, dict) and r.get('market')}

    # Any recently confirmed BUY_READY stays visible for two hours even if raw V4 drops it.
    for market, hist in history.items():
        recent_buy = f(hist.get('last_buy_ready_ts'))
        if not hist.get('ever_buy_ready') or not recent_buy or now_ts - recent_buy > RECENT_BUY_TRACK_SEC:
            continue
        if market not in raw_rows:
            raw_rows[market] = synthetic_row(market, hist, live.get(market, {}), profiles.get(market, {}))

    stabilized = []
    for market, row in raw_rows.items():
        hist = history.get(market, {})
        st = state['markets'].setdefault(market, {})
        raw_action = str(row.get('action_status') or hist.get('last_action_status') or 'NONE')
        raw_buy = bool(row.get('buy_ready')) and raw_action in {'BUY_READY', 'REENTRY_READY'}
        opp = f(row.get('opportunity_score'), f(hist.get('last_opportunity_score')))
        ent = f(row.get('entry_score'), f(hist.get('last_entry_score')))
        flags = list(row.get('risk_flags') or [])
        hard = raw_action in HARD_ACTIONS or any(x in HARD_FLAGS for x in flags)
        chase = 'CHASE_RISK' in flags
        not_enriched = 'NOT_ENTRY_ENRICHED' in flags

        stable_action = str(st.get('stable_action') or raw_action)
        bad_count = int(f(st.get('downgrade_count')))
        hold_until = f(st.get('buy_hold_until_ts'))
        recent_hist_buy = f(hist.get('last_buy_ready_ts'))

        if raw_buy:
            stable_action = raw_action
            hold_until = max(hold_until, now_ts + BUY_HOLD_SEC)
            bad_count = 0
            st['last_raw_buy_ts'] = now_ts
            st['last_good_row'] = deepcopy(row)
        else:
            bootstrap_buy = (
                bool(hist.get('ever_buy_ready')) and recent_hist_buy > 0
                and now_ts - recent_hist_buy <= BUY_HOLD_SEC
                and ent >= BUY_ENTRY_FLOOR and opp >= 7.0 and not hard and not chase
            )
            if bootstrap_buy and stable_action not in {'BUY_READY', 'REENTRY_READY'}:
                stable_action = 'BUY_READY'
                hold_until = recent_hist_buy + BUY_HOLD_SEC
                bad_count = 0

            if stable_action in {'BUY_READY', 'REENTRY_READY'}:
                if hard or chase or (ent < EMERGENCY_ENTRY_FLOOR and not not_enriched):
                    stable_action = 'WATCH_RISK' if hard else 'ENTRY_WINDOW'
                    bad_count = 0
                    hold_until = 0.0
                elif now_ts < hold_until:
                    bad_count = 0
                else:
                    degraded = opp < BUY_OPP_FLOOR or ent < BUY_ENTRY_FLOOR
                    bad_count = bad_count + 1 if degraded else 0
                    if bad_count >= DOWNGRADE_SCANS_REQUIRED:
                        if opp >= 7.8 and ent >= 6.2:
                            stable_action = 'ENTRY_WINDOW'
                        elif opp >= 7.0:
                            stable_action = 'WATCH'
                        else:
                            stable_action = 'NONE'
                        hold_until = 0.0
                        bad_count = 0
            elif stable_action == 'ENTRY_WINDOW':
                if hard:
                    stable_action = 'WATCH_RISK'
                    bad_count = 0
                elif raw_action in {'BUY_READY', 'REENTRY_READY'}:
                    stable_action = raw_action
                    hold_until = now_ts + BUY_HOLD_SEC
                    bad_count = 0
                elif raw_action not in {'ENTRY_WINDOW', 'BUY_READY', 'REENTRY_READY'}:
                    bad_count += 1
                    if bad_count >= DOWNGRADE_SCANS_REQUIRED:
                        stable_action = 'WATCH' if opp >= 7.0 else 'NONE'
                        bad_count = 0
                else:
                    bad_count = 0
            else:
                stable_action = raw_action
                bad_count = 0

                # A previously actionable setup does not disappear immediately after its buy window.
                if (
                    stable_action == 'NONE' and bool(hist.get('ever_buy_ready')) and recent_hist_buy > 0
                    and now_ts - recent_hist_buy <= RECENT_BUY_TRACK_SEC and not hard
                ):
                    if opp >= 7.8 and ent >= 6.2:
                        stable_action = 'ENTRY_WINDOW'
                    elif opp >= 6.8:
                        stable_action = 'WATCH'

        row['raw_action_status'] = raw_action
        row['raw_buy_ready'] = raw_buy
        row['action_status'] = stable_action
        row['buy_ready'] = stable_action in {'BUY_READY', 'REENTRY_READY'}
        row['stability'] = {
            'held': stable_action != raw_action,
            'buy_hold_until_utc': datetime.fromtimestamp(hold_until, timezone.utc).isoformat() if hold_until else None,
            'downgrade_count': bad_count,
            'downgrade_scans_required': DOWNGRADE_SCANS_REQUIRED,
            'reason': 'HYSTERESIS_HOLD' if stable_action != raw_action else 'RAW_CONFIRMED',
        }
        if stable_action != raw_action:
            row['risk_flags'] = list(dict.fromkeys(flags + ['STABILITY_HOLD']))

        if row.get('trade_plan') is None and stable_action in {'BUY_READY', 'REENTRY_READY', 'ENTRY_WINDOW'}:
            try:
                row['trade_plan'] = suggested_trade_plan(row, row.get('trend_profile') or {}, opp, ent)
            except Exception:
                pass

        st['stable_action'] = stable_action
        st['downgrade_count'] = bad_count
        st['buy_hold_until_ts'] = hold_until
        st['last_seen_ts'] = now_ts
        st['last_raw_action'] = raw_action
        st['last_opportunity_score'] = opp
        st['last_entry_score'] = ent
        stabilized.append(row)

    stabilized.sort(key=lambda r: (rank_value(str(r.get('action_status'))), f(r.get('opportunity_score')), f(r.get('entry_score'))), reverse=True)
    stabilized = stabilized[:MAX_OUTPUT]

    raw['watch'] = stabilized
    raw['method_note'] = (
        'V4 + decision hysteresis: a confirmed BUY_READY is held for at least 15 minutes; downgrade requires '
        'two consecutive degraded scans unless hard structural invalidation occurs. Former BUY_READY setups '
        'remain visible as ENTRY_WINDOW/WATCH for up to two hours instead of disappearing on 5-minute noise.'
    )
    raw['stability_version'] = 2
    save(WATCH_JSON, raw)

    lines = [
        'BITVAVO SCAN V4 — STABILIZED DECISIONS',
        f'generated_at_utc: {generated}',
        'RULE: BUY_READY minimum lifetime 15m; 2 weak scans to downgrade; former buys tracked 2h unless hard invalidation.',
        'market | stable_action | raw_action | opportunity | entry | trend | last | ch24 | confirms | flags | stability',
    ]
    for r in stabilized:
        lines.append(
            f"{r.get('market')} | {r.get('action_status')} | {r.get('raw_action_status')} | "
            f"{f(r.get('opportunity_score')):.3f} | {f(r.get('entry_score')):.3f} | {f(r.get('trend_score')):.3f} | "
            f"{r.get('last')} | {f(r.get('change_24h_pct')):.2f}% | {r.get('confirm_count')} | "
            f"{','.join(r.get('risk_flags') or []) or '-'} | {(r.get('stability') or {}).get('reason')}"
        )
    WATCH_TXT.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    state['version'] = 2
    state['generated_at_utc'] = generated
    save(STATE, state)
    ready = [r.get('market') for r in stabilized if r.get('buy_ready')]
    print(f"V4_STABILITY: buy_ready={ready or 'none'}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
