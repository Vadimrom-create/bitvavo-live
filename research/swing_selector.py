"""Deterministic Human/Swing selector primitives.

This module is SHADOW research infrastructure. It does not place, modify,
block, or cancel orders and does not alter Solaire/Decision Layer decisions.

Objective: rank markets for a 24h-7d human holding horizon. Short-horizon
5m/15m acceleration is intentionally not part of the thesis score.
"""
from __future__ import annotations

import math
from typing import Any

VERSION = "SWING_SELECTOR_V1_FROZEN_2026-10-08_R2"

def _f(v: Any, default: float | None = None) -> float | None:
    try:
        x=float(v)
    except (TypeError, ValueError):
        return default
    return x if math.isfinite(x) else default

def _clip(x: float, lo: float, hi: float) -> float:
    return max(lo,min(hi,x))

def _ramp(x: float | None, low: float, high: float) -> float:
    if x is None:
        return 0.0
    if high == low:
        return 1.0 if x >= high else 0.0
    return _clip((x-low)/(high-low),0.0,1.0)

def _triangle(x: float | None, left: float, peak_left: float, peak_right: float, right: float) -> float:
    if x is None:
        return 0.0
    if peak_left <= x <= peak_right:
        return 1.0
    if x < peak_left:
        return _ramp(x,left,peak_left)
    if right == peak_right:
        return 0.0
    return _clip((right-x)/(right-peak_right),0.0,1.0)

def _log_liquidity(eur: float | None) -> float:
    if eur is None or eur <= 0:
        return 0.0
    # Soft scale: 10k=0, 100k~0.5, 1m=1.0.
    return _clip((math.log10(eur)-4.0)/2.0,0.0,1.0)

def score_market(
    market: str,
    trend: dict[str, Any],
    live: dict[str, Any] | None = None,
    news: dict[str, Any] | None = None,
) -> dict[str, Any]:
    live=live or {}
    news=news or {}

    ret3=_f(trend.get("ret3d"))
    ret7=_f(trend.get("ret7d"))
    ret14=_f(trend.get("ret14d"))
    ret30=_f(trend.get("ret30d"))
    slope=_f(trend.get("ema20_slope_5d_pct"))
    d20=_f(trend.get("dist_ema20_pct"))
    d50=_f(trend.get("dist_ema50_pct"))
    dd30=_f(trend.get("drawdown_30d_high_pct"))
    breakout=_f(trend.get("breakout20_pct"))
    vol3=_f(trend.get("vol3_vs_prev20"))
    atr=_f(trend.get("atr14_pct"))
    rs3=_f(trend.get("rs_btc_3d"))
    rs7=_f(trend.get("rs_btc_7d"))
    rs14=_f(trend.get("rs_btc_14d"))

    hh=bool(trend.get("higher_high_7d"))
    hl=bool(trend.get("higher_low_7d"))

    quote_vol=_f(live.get("quote_volume_24h_eur"))
    spread=_f(live.get("spread_pct"))
    ch24=_f(live.get("change_24h_pct"))

    # 0..30: persistent multi-day structure, deliberately not micro momentum.
    persistence=0.0
    persistence += 5.0*_triangle(ret3,-8,1,12,30)
    persistence += 6.0*_triangle(ret7,-10,4,25,60)
    persistence += 4.0*_triangle(ret14,-15,5,40,90)
    persistence += 5.0*_triangle(slope,-5,1,8,18)
    persistence += 3.0 if hh else 0.0
    persistence += 3.0 if hl else 0.0
    persistence += 2.0*_triangle(d20,-10,-1,8,20)
    persistence += 2.0*_triangle(d50,-15,0,18,40)

    # 0..20: relative strength over human horizons.
    relative=0.0
    relative += 6.0*_ramp(rs3,-5,8)
    relative += 8.0*_ramp(rs7,-5,15)
    relative += 6.0*_ramp(rs14,-8,20)

    # 0..20: preserve room for continuation; penalize vertical/chased states.
    early=0.0
    early += 7.0*_triangle(d50,-10,2,16,32)
    early += 5.0*_triangle(ret7,-10,2,22,55)
    early += 4.0*_triangle(dd30,-45,-22,-5,3)
    early += 4.0*_triangle(breakout,-35,-16,-2,5)

    # 0..15: participation/liquidity. Missing live liquidity is neutral-ish,
    # not fatal, so historical scoring remains possible.
    participation=0.0
    participation += 6.0*_triangle(vol3,0.0,0.8,2.5,7.0)
    participation += 6.0*(_log_liquidity(quote_vol) if quote_vol is not None else 0.5)
    if spread is None:
        participation += 1.5
    else:
        participation += 3.0*_clip((1.0-spread)/1.0,0.0,1.0)

    # 0..10: avoid unmanageably volatile/chased entries. This is not a stop.
    risk=0.0
    risk += 6.0*_triangle(atr,1.0,3.0,10.0,22.0)
    risk += 4.0*_triangle(ch24,-15,-2,8,25) if ch24 is not None else 2.0

    technical=_clip(persistence+relative+early+participation+risk,0.0,95.0)

    # News/catalyst modifier is capped at +/-5 and explicitly marked
    # unbacktested because historical news snapshots are not archived.
    news_mod=0.0
    news_reason=None
    direction=str(news.get("direction") or "").upper()
    news_score=_f(news.get("score"),0.0) or 0.0
    catalyst=news.get("catalyst") if isinstance(news.get("catalyst"),dict) else {}
    cdir=str(catalyst.get("direction") or "").upper()
    cscore=_f(catalyst.get("score"),0.0) or 0.0
    clevel=int(_f(catalyst.get("level"),0.0) or 0)

    if direction=="POSITIVE" and news_score>=6.5:
        news_mod += min(2.5,(news_score-5.5)*0.8)
        news_reason="positive_news"
    elif direction=="NEGATIVE" and news_score>=7.0:
        news_mod -= min(3.0,(news_score-6.0)*0.9)
        news_reason="negative_news"

    if cdir=="POSITIVE" and cscore>=6.5:
        news_mod += min(3.0,1.0+0.7*clevel)
        news_reason=(news_reason+"+positive_catalyst") if news_reason else "positive_catalyst"
    elif cdir=="NEGATIVE" and cscore>=7.0:
        news_mod -= min(3.0,1.0+0.7*clevel)
        news_reason=(news_reason+"+negative_catalyst") if news_reason else "negative_catalyst"

    news_mod=_clip(news_mod,-5.0,5.0)
    total=_clip(technical+news_mod,0.0,100.0)

    # Descriptive flags only; they do not change production behavior.
    flags=[]
    if ret7 is not None and ret7>45: flags.append("EXTENDED_7D")
    if d50 is not None and d50>30: flags.append("FAR_ABOVE_EMA50")
    if atr is not None and atr>18: flags.append("HIGH_ATR")
    if spread is not None and spread>0.8: flags.append("WIDE_SPREAD")
    if ch24 is not None and ch24>15: flags.append("CHASE_RISK_24H")
    if direction=="NEGATIVE" and news_score>=7.0: flags.append("NEGATIVE_NEWS")

    return {
        "market":market,
        "version":VERSION,
        "score":round(total,4),
        "technical_score":round(technical,4),
        "news_modifier":round(news_mod,4),
        "components":{
            "persistence":round(persistence,4),
            "relative_strength":round(relative,4),
            "early_stage":round(early,4),
            "participation":round(participation,4),
            "risk_manageability":round(risk,4),
        },
        "inputs":{
            "ret3d":ret3,"ret7d":ret7,"ret14d":ret14,"ret30d":ret30,
            "ema20_slope_5d_pct":slope,"dist_ema20_pct":d20,"dist_ema50_pct":d50,
            "drawdown_30d_high_pct":dd30,"breakout20_pct":breakout,
            "vol3_vs_prev20":vol3,"atr14_pct":atr,
            "rs_btc_3d":rs3,"rs_btc_7d":rs7,"rs_btc_14d":rs14,
            "higher_high_7d":hh,"higher_low_7d":hl,
            "quote_volume_24h_eur":quote_vol,"spread_pct":spread,"change_24h_pct":ch24,
        },
        "news_reason":news_reason,
        "flags":flags,
    }
