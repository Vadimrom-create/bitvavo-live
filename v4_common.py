from __future__ import annotations

import json
import math
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from v3_common import candles, clamp, ema, f, maybe, mean, pct

V4_HISTORY = Path('v4_history.json')
V4_WATCH_JSON = Path('v4_watch.json')
V4_WATCH_TXT = Path('v4_watch.txt')
V4_SIGNAL_LOG = Path('v4_signal_log.json')
TREND_CACHE = Path('v4_trend_cache.json')
CONFIG_PATH = Path('v4_config.json')

TREND_CACHE_TTL_SEC = 90 * 60
V4_WATCH_SEC = 7 * 24 * 3600
V4_HISTORY_RETENTION_SEC = 14 * 24 * 3600
V4_SIGNAL_RETENTION_SEC = 21 * 24 * 3600

CORE_MARKETS = {
    'BTC-EUR','ETH-EUR','SOL-EUR','XRP-EUR','BNB-EUR','ADA-EUR','DOGE-EUR','LINK-EUR',
    'AVAX-EUR','SUI-EUR','NEAR-EUR','DOT-EUR','ATOM-EUR','LTC-EUR','AAVE-EUR','UNI-EUR',
    'INJ-EUR','RENDER-EUR','FET-EUR','SEI-EUR','JUP-EUR','ZK-EUR','SUSHI-EUR','ETHFI-EUR',
    'NIL-EUR','ONDO-EUR','TIA-EUR','ARB-EUR','OP-EUR','ENA-EUR','WLD-EUR','TAO-EUR',
    'PEPE-EUR','SHIB-EUR','WIF-EUR','FLOKI-EUR','GRT-EUR','RUNE-EUR','APT-EUR','FIL-EUR',
    'IMX-EUR','STX-EUR','AERO-EUR','PENDLE-EUR','VIRTUAL-EUR','FLOCK-EUR','HUMA-EUR','HEI-EUR'
}

DEFAULT_CONFIG = {
    'portfolio_target_eur': 2700,
    'estimated_cash_eur': 1200,
    'target_gain_eur': 400,
    'default_position_eur': 150,
    'strong_position_eur': 200,
    'exceptional_position_eur': 250,
    'max_position_eur': 250,
    'max_risk_per_trade_eur': 12,
    'max_simultaneous_exposure_eur': 700,
    'min_cash_reserve_eur': 500,
    'tp1_pct': 7,
    'runner_target_pct': 15,
    'runner_keep_pct': 40,
}


def load_config() -> dict:
    cfg = dict(DEFAULT_CONFIG)
    try:
        raw = json.loads(CONFIG_PATH.read_text(encoding='utf-8')) if CONFIG_PATH.exists() else {}
        if isinstance(raw, dict):
            cfg.update(raw)
    except Exception:
        pass
    return cfg


def load_v4_history() -> dict:
    try:
        data = json.loads(V4_HISTORY.read_text(encoding='utf-8')) if V4_HISTORY.exists() else {}
    except Exception:
        data = {}
    if not isinstance(data, dict):
        data = {}
    data['version'] = 4
    data.setdefault('markets', {})
    return data


def save_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')


def _ret(closes: list[float], days: int) -> float | None:
    if len(closes) <= days or not closes[-1-days]:
        return None
    return pct(closes[-1], closes[-1-days])


def _atr_pct(cs: list[dict], period: int = 14) -> float | None:
    if len(cs) < period + 1:
        return None
    trs = []
    for i in range(1, len(cs)):
        h, l, prev = cs[i]['h'], cs[i]['l'], cs[i-1]['c']
        trs.append(max(h-l, abs(h-prev), abs(l-prev)))
    atr = mean(trs[-period:])
    return atr / cs[-1]['c'] * 100.0 if atr and cs[-1]['c'] else None


def daily_profile_from_candles(cs: list[dict]) -> dict:
    if len(cs) < 35:
        return {}
    closes = [x['c'] for x in cs]
    highs = [x['h'] for x in cs]
    lows = [x['l'] for x in cs]
    vols = [x['v'] for x in cs]
    last = closes[-1]
    ema20_now = ema(closes, 20)
    ema50_now = ema(closes, 50) if len(closes) >= 50 else None
    ema20_prev5 = ema(closes[:-5], 20) if len(closes) > 25 else None
    high20_prev = max(highs[-21:-1]) if len(highs) >= 21 else None
    high30 = max(highs[-30:]) if len(highs) >= 30 else None
    low7 = min(lows[-7:]) if len(lows) >= 14 else None
    prev_low7 = min(lows[-14:-7]) if len(lows) >= 14 else None
    high7 = max(highs[-7:]) if len(highs) >= 14 else None
    prev_high7 = max(highs[-14:-7]) if len(highs) >= 14 else None
    prev20vol = mean(vols[-23:-3]) if len(vols) >= 23 else mean(vols[:-3])
    recent3vol = mean(vols[-3:])
    green7 = sum(1 for i in range(max(1, len(closes)-7), len(closes)) if closes[i] > closes[i-1])
    return {
        'last': last,
        'ret1d': _ret(closes, 1),
        'ret3d': _ret(closes, 3),
        'ret7d': _ret(closes, 7),
        'ret14d': _ret(closes, 14),
        'ret30d': _ret(closes, 30),
        'ema20': ema20_now,
        'ema50': ema50_now,
        'dist_ema20_pct': pct(last, ema20_now) if ema20_now else None,
        'dist_ema50_pct': pct(last, ema50_now) if ema50_now else None,
        'ema20_slope_5d_pct': pct(ema20_now, ema20_prev5) if ema20_now and ema20_prev5 else None,
        'breakout20_pct': pct(last, high20_prev) if high20_prev else None,
        'drawdown_30d_high_pct': pct(last, high30) if high30 else None,
        'vol3_vs_prev20': recent3vol / prev20vol if recent3vol and prev20vol else None,
        'green_days_7': green7,
        'higher_high_7d': bool(high7 and prev_high7 and high7 > prev_high7),
        'higher_low_7d': bool(low7 and prev_low7 and low7 > prev_low7),
        'atr14_pct': _atr_pct(cs, 14),
        'bars': len(cs),
        'last_candle_ts': cs[-1]['t'],
    }


def load_trend_cache() -> dict:
    try:
        data = json.loads(TREND_CACHE.read_text(encoding='utf-8')) if TREND_CACHE.exists() else {}
    except Exception:
        data = {}
    if not isinstance(data, dict):
        data = {}
    data.setdefault('version', 4)
    data.setdefault('markets', {})
    return data


def refresh_trend_cache(markets: list[str], now_ts: float, force: bool = False) -> dict:
    cache = load_trend_cache()
    cache_ts = f(cache.get('updated_ts'))
    stale = force or now_ts - cache_ts >= TREND_CACHE_TTL_SEC
    missing = [m for m in markets if m not in cache['markets']]
    names = list(dict.fromkeys(markets if stale else missing))
    if not names:
        return cache

    def one(market: str):
        try:
            cs = candles(market, '1d', 95)
            return market, daily_profile_from_candles(cs), None
        except Exception as exc:
            return market, {}, str(exc)

    with ThreadPoolExecutor(max_workers=6) as pool:
        futs = [pool.submit(one, m) for m in names]
        for fut in as_completed(futs):
            market, profile, err = fut.result()
            if profile:
                profile['updated_ts'] = now_ts
                cache['markets'][market] = profile
            elif err:
                old = cache['markets'].get(market, {})
                old['last_error'] = err
                cache['markets'][market] = old
    cache['updated_ts'] = now_ts
    cache['updated_at_utc'] = datetime.fromtimestamp(now_ts, timezone.utc).isoformat()
    save_json(TREND_CACHE, cache)
    return cache


def add_relative_strength(cache: dict) -> None:
    btc = cache.get('markets', {}).get('BTC-EUR') or {}
    eth = cache.get('markets', {}).get('ETH-EUR') or {}
    for market, p in cache.get('markets', {}).items():
        for days, key in ((3, 'ret3d'), (7, 'ret7d'), (14, 'ret14d'), (30, 'ret30d')):
            r = maybe(p.get(key))
            b = maybe(btc.get(key))
            e = maybe(eth.get(key))
            p[f'rs_btc_{days}d'] = round(r - b, 4) if r is not None and b is not None else None
            p[f'rs_eth_{days}d'] = round(r - e, 4) if r is not None and e is not None else None


def trend_score(profile: dict) -> float:
    if not profile:
        return 5.0
    # Broad 0-10 scale: only exceptional multi-horizon trends should approach 10.
    s = 2.6
    r3, r7, r14, r30 = [maybe(profile.get(k)) for k in ('ret3d','ret7d','ret14d','ret30d')]
    rs7, rs30 = maybe(profile.get('rs_btc_7d')), maybe(profile.get('rs_btc_30d'))
    rs7e = maybe(profile.get('rs_eth_7d'))
    slope = maybe(profile.get('ema20_slope_5d_pct'))
    d20, d50 = maybe(profile.get('dist_ema20_pct')), maybe(profile.get('dist_ema50_pct'))
    breakout = maybe(profile.get('breakout20_pct'))
    dd = maybe(profile.get('drawdown_30d_high_pct'))
    vol = maybe(profile.get('vol3_vs_prev20'))
    atr = maybe(profile.get('atr14_pct'))

    if r3 is not None:
        s += 0.25 if r3 > 1 else 0.0
        s += 0.25 if r3 > 3 else 0.0
    if r7 is not None:
        s += 0.35 if r7 > 3 else 0.0
        s += 0.35 if r7 > 7 else 0.0
        s += 0.20 if r7 > 12 else 0.0
    if r14 is not None and r14 > 6:
        s += 0.25
    if r30 is not None:
        s += 0.35 if r30 > 8 else 0.0
        s += 0.35 if r30 > 18 else 0.0
        s += 0.20 if r30 > 35 else 0.0

    # Relative strength is central: the historical winners beat BTC even during weak tape.
    if rs7 is not None:
        s += 0.45 if rs7 > 3 else 0.0
        s += 0.30 if rs7 > 7 else 0.0
    if rs7e is not None and rs7e > 3:
        s += 0.20
    if rs30 is not None:
        s += 0.45 if rs30 > 5 else 0.0
        s += 0.30 if rs30 > 12 else 0.0

    if d20 is not None and d20 > 0:
        s += 0.35
    if d50 is not None and d50 > 0:
        s += 0.25
    if slope is not None and slope > 0.4:
        s += 0.35
    if profile.get('higher_high_7d'):
        s += 0.20
    if profile.get('higher_low_7d'):
        s += 0.25
    if breakout is not None and -3 <= breakout <= 4:
        s += 0.30
    if dd is not None and -8 <= dd <= -1.5 and (slope or 0) > 0:
        s += 0.25
    if vol is not None and 1.1 <= vol <= 4.5:
        s += 0.25
    if (profile.get('green_days_7') or 0) >= 4:
        s += 0.15

    # Extension reduces timing quality, not the existence of the trend.
    if breakout is not None and breakout > 8:
        s -= 0.40
    if r7 is not None and r7 > 25:
        s -= 0.35
    if r7 is not None and r7 > 45:
        s -= 0.35
    if r30 is not None and r30 > 80:
        s -= 0.40
    if atr is not None and atr > 18:
        s -= 0.35
    if slope is not None and slope < -1:
        s -= 0.65
    return round(clamp(s), 3)


def liquidity_score(row: dict) -> float:
    vol = f(row.get('quote_volume_24h_eur'))
    spread = f(row.get('spread_pct'), 99)
    s = 5.0
    if vol >= 1_000_000: s += 1.0
    elif vol >= 250_000: s += 0.7
    elif vol >= 75_000: s += 0.35
    elif vol < 25_000: s -= 1.3
    if spread <= 0.05: s += 0.8
    elif spread <= 0.12: s += 0.55
    elif spread <= 0.25: s += 0.15
    elif spread > 0.8: s -= 2.0
    elif spread > 0.4: s -= 1.0
    return clamp(s)


def persistence_score(hm: dict, now_ts: float) -> float:
    s = 5.0
    if f(hm.get('watch_until_ts')) > now_ts:
        s += 1.0
    confirms = int(f(hm.get('opportunity_confirm_count')))
    s += min(confirms, 6) * 0.35
    last = maybe(hm.get('last_opportunity_score'))
    if last is not None and last >= 8.0:
        s += 0.6
    return clamp(s)


def suggested_trade_plan(row: dict, profile: dict, opportunity: float, entry: float) -> dict:
    cfg = load_config()
    atr = maybe(profile.get('atr14_pct')) if profile else None
    stop_pct = max(3.0, min(7.0, (atr or 3.6) * 1.15))
    if opportunity >= 9.25 and entry >= 8.25 and f(row.get('quote_volume_24h_eur')) >= 500_000:
        tier = f(cfg.get('exceptional_position_eur'), 250)
    elif opportunity >= 8.7 and entry >= 7.7:
        tier = f(cfg.get('strong_position_eur'), 200)
    else:
        tier = f(cfg.get('default_position_eur'), 150)
    risk_cap = f(cfg.get('max_risk_per_trade_eur'), 12)
    by_risk = risk_cap / (stop_pct / 100.0) if stop_pct > 0 else tier
    max_pos = f(cfg.get('max_position_eur'), 250)
    cash = f(cfg.get('estimated_cash_eur'), 1200)
    reserve = f(cfg.get('min_cash_reserve_eur'), 500)
    cash_cap = max(0.0, cash - reserve)
    stake = min(tier, by_risk, max_pos, cash_cap)
    stake = max(0.0, round(stake / 25.0) * 25.0)
    return {
        'suggested_stake_eur': stake,
        'structural_stop_guide_pct': round(stop_pct, 2),
        'risk_eur_at_guide': round(stake * stop_pct / 100.0, 2),
        'tp1_pct': f(cfg.get('tp1_pct'), 7),
        'runner_target_pct': f(cfg.get('runner_target_pct'), 15),
        'runner_keep_pct': f(cfg.get('runner_keep_pct'), 40),
        'note': 'Sizing guide only: stop must be placed on structural invalidation, not mechanically at this percentage.'
    }
