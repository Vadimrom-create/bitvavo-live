from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BASE = "https://api.bitvavo.com/v2"
LIVE = Path("bitvavo_live.json")
SCAN = Path("scan_feed.txt")
HISTORY = Path("scan_history.json")
EARLY_TXT = Path("early_watch.txt")
EARLY_JSON = Path("early_watch.json")
SIGNAL_LOG = Path("signal_log.json")

HISTORY_WINDOW_SEC = 24 * 3600
WATCH_PERSIST_SEC = 12 * 3600
SESSION_RESET_SEC = 12 * 3600
SIGNAL_LOG_RETENTION_SEC = 7 * 24 * 3600
WATCH_COUNT = 40
ENRICH_COUNT = 50
SIGNAL_THRESHOLD = 7.20
IGNITION_THRESHOLD = 8.00
BUY_READY_THRESHOLD = 8.55

HEADERS = {"Accept": "application/json", "User-Agent": "bitvavo-ignition-v3/1.0"}


def f(x: Any, default: float = 0.0) -> float:
    try:
        return float(x)
    except Exception:
        return default


def maybe(x: Any) -> float | None:
    try:
        return float(x)
    except Exception:
        return None


def clamp(x: float, lo: float = 0.0, hi: float = 10.0) -> float:
    return max(lo, min(hi, x))


def pct(a: float, b: float) -> float | None:
    return (a / b - 1.0) * 100.0 if b else None


def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def ema(values, period):
    if not values:
        return None
    alpha = 2.0 / (period + 1.0)
    e = values[0]
    for x in values[1:]:
        e = alpha * x + (1.0 - alpha) * e
    return e


def get_json(path: str, params: dict | None = None, retries: int = 3):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as exc:
            err = exc
            time.sleep(0.8 + attempt)
    raise RuntimeError(f"API {url}: {err}")


def candles(market: str, interval: str, limit: int = 50):
    rows = []
    for x in get_json(f"/{market}/candles", {"interval": interval, "limit": limit}):
        if len(x) >= 6:
            rows.append({"t": int(x[0]), "o": f(x[1]), "h": f(x[2]), "l": f(x[3]), "c": f(x[4]), "v": f(x[5])})
    return sorted(rows, key=lambda x: x["t"])


def summarize(cs):
    if len(cs) < 10:
        return {}
    closes = [x["c"] for x in cs]
    vols = [x["v"] for x in cs]
    recent = cs[-8:]
    hi = max(x["h"] for x in recent)
    lo = min(x["l"] for x in recent)
    wick = 0.0
    for c in recent:
        rng = c["h"] - c["l"]
        if rng > 0:
            wick = max(wick, max(0.0, c["h"] - max(c["o"], c["c"])) / rng)
    prev20 = vols[-21:-1] if len(vols) >= 21 else vols[:-1]
    prev4 = vols[-8:-4]
    return {
        "last": closes[-1],
        "ch1": pct(closes[-1], closes[-2]) if len(closes) >= 2 else None,
        "ch4": pct(closes[-1], closes[-5]) if len(closes) >= 5 else None,
        "ch16": pct(closes[-1], closes[-17]) if len(closes) >= 17 else None,
        "vr1": vols[-1] / mean(prev20) if mean(prev20) else None,
        "vr4": sum(vols[-4:]) / sum(prev4) if prev4 and sum(prev4) else None,
        "ema20": ema(closes, 20),
        "dist8high": pct(closes[-1], hi),
        "range8": (hi - lo) / closes[-1] * 100.0 if closes[-1] else None,
        "wick": wick,
    }


def normalize_summary(s: dict | None):
    s = s or {}
    return {
        "last": maybe(s.get("last")),
        "ch1": maybe(s.get("ch1", s.get("change_1_candle_pct"))),
        "ch4": maybe(s.get("ch4", s.get("change_4_candles_pct"))),
        "ch16": maybe(s.get("ch16", s.get("change_16_candles_pct"))),
        "vr1": maybe(s.get("vr1", s.get("volume_last_vs_prev20"))),
        "vr4": maybe(s.get("vr4", s.get("volume_4_vs_prev4"))),
        "ema20": maybe(s.get("ema20")),
        "dist8high": maybe(s.get("dist8high", s.get("distance_from_8bar_high_pct"))),
        "range8": maybe(s.get("range8", s.get("range_8bar_pct"))),
        "wick": maybe(s.get("wick", s.get("max_upper_wick_ratio_8bar"))),
    }


def book(market: str):
    b = get_json(f"/{market}/book", {"depth": 50})
    bids, asks = b.get("bids", []), b.get("asks", [])
    bv = sum(f(p) * f(q) for p, q in bids)
    av = sum(f(p) * f(q) for p, q in asks)
    return {"bid_share": bv / (bv + av) if bv + av else None, "bid_eur": round(bv, 2), "ask_eur": round(av, 2)}


def enrich_market(market: str, live_details: dict):
    existing = live_details.get(market) or {}
    try:
        s15 = normalize_summary(existing.get("m15_summary"))
        s1h = normalize_summary(existing.get("h1_summary"))
        s4h = normalize_summary(existing.get("h4_summary"))
        s5 = summarize(candles(market, "5m", 50))
        if not s15.get("last"):
            s15 = summarize(candles(market, "15m", 50))
        if not s1h.get("last"):
            s1h = summarize(candles(market, "1h", 50))
        if not s4h.get("last"):
            s4h = summarize(candles(market, "4h", 50))
        existing_book = existing.get("orderbook") or {}
        if existing_book:
            b = {
                "bid_share": maybe(existing_book.get("bid_share_50")),
                "bid_eur": maybe(existing_book.get("bid_notional_eur_50")),
                "ask_eur": maybe(existing_book.get("ask_notional_eur_50")),
            }
        else:
            b = book(market)
        return market, {"5m": s5, "15m": s15, "1h": s1h, "4h": s4h, "book": b}
    except Exception as exc:
        return market, {"error": str(exc)}


# échantillon compact : [ts, rank, priority, last, ch24, vr1, vr4, v3score]
S_TS, S_RANK, S_PRI, S_LAST, S_CH24, S_VR1, S_VR4, S_SCORE = range(8)


def compact_sample(s):
    if isinstance(s, list):
        vals = list(s[:8]) + [None] * max(0, 8 - len(s))
        return vals[:8]
    if isinstance(s, dict):
        return [f(s.get("ts")), s.get("rank"), s.get("priority"), s.get("last"), s.get("ch24"), s.get("vr1"), s.get("vr4"), s.get("v3", s.get("early"))]
    return None


def load_history():
    try:
        d = json.loads(HISTORY.read_text(encoding="utf-8")) if HISTORY.exists() else {}
    except Exception:
        d = {}
    if not isinstance(d, dict):
        d = {}
    d["version"] = 3
    d.setdefault("markets", {})
    for hm in d["markets"].values():
        hm["samples"] = [x for x in (compact_sample(s) for s in hm.get("samples", [])) if x]
        # migration douce V2 -> V3
        if hm.get("first_early_price") and not hm.get("first_signal_price"):
            hm["first_signal_price"] = hm.get("first_early_price")
            hm["first_signal_seen"] = hm.get("first_early_seen")
            try:
                hm["first_signal_ts"] = datetime.fromisoformat(str(hm.get("first_early_seen")).replace("Z", "+00:00")).timestamp()
            except Exception:
                pass
    return d


def thin_samples(samples, now_ts):
    valid = [s for s in samples if isinstance(s, list) and len(s) >= 8 and now_ts - f(s[S_TS]) <= HISTORY_WINDOW_SEC]
    valid.sort(key=lambda s: f(s[S_TS]))
    buckets = {}
    for s in valid:
        age = max(0.0, now_ts - f(s[S_TS]))
        width = 300 if age <= 2 * 3600 else 900 if age <= 8 * 3600 else 1800
        buckets[(width, int(f(s[S_TS]) // width))] = s
    return sorted(buckets.values(), key=lambda s: f(s[S_TS]))


def nearest(samples, now_ts, minutes):
    target = minutes * 60.0
    tolerance = max(7 * 60.0, target * 0.38)
    choices = []
    for s in samples:
        age = now_ts - f(s[S_TS])
        if age >= 90:
            choices.append((abs(age - target), s))
    if not choices:
        return None
    choices.sort(key=lambda x: x[0])
    return choices[0][1] if choices[0][0] <= tolerance else None


def trajectory(row, rank, hm, now_ts):
    out = {}
    samples = hm.get("samples", [])
    for m in (5, 15, 30, 60, 120, 240, 360, 720, 1440):
        old = nearest(samples, now_ts, m)
        if old:
            out[f"dscore_{m}m"] = round(f(row.get("collector_priority")) - f(old[S_PRI]), 4)
            old_rank = maybe(old[S_RANK])
            out[f"drank_{m}m"] = round(old_rank - rank, 1) if old_rank is not None else None
            old_price = maybe(old[S_LAST])
            out[f"dprice_{m}m_pct"] = round(pct(f(row.get("last")), old_price), 4) if old_price else None
            out[f"dvr4_{m}m"] = round(f((row.get("m15") or {}).get("volume_4_vs_prev4")) - f(old[S_VR4]), 4)
        else:
            out[f"dscore_{m}m"] = out[f"drank_{m}m"] = out[f"dprice_{m}m_pct"] = out[f"dvr4_{m}m"] = None
    return out


def btc_risk(live: dict) -> bool:
    btc = next((r for r in live.get("markets", []) if r.get("market") == "BTC-EUR"), None)
    if not btc:
        return True
    s = btc.get("m15") or {}
    return f(btc.get("change_24h_pct")) < -3.0 or f(s.get("change_4_candles_pct")) < -1.25 or f(s.get("change_16_candles_pct")) < -3.5
