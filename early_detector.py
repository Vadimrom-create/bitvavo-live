#!/usr/bin/env python3
"""V2 overlay: détecte les transitions précoces entre deux snapshots Bitvavo."""
from __future__ import annotations

import json
import math
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://api.bitvavo.com/v2"
LIVE = Path("bitvavo_live.json")
SCAN = Path("scan_feed.txt")
HISTORY = Path("scan_history.json")
EARLY_TXT = Path("early_watch.txt")
EARLY_JSON = Path("early_watch.json")

MAX_HISTORY_SEC = 3 * 3600
MAX_SAMPLES = 40
EARLY_TRIGGER = 6.5
EARLY_RESET = 4.5
SESSION_RESET_SEC = 3600
WATCH_COUNT = 25
ENRICH_COUNT = 18
HEADERS = {"Accept": "application/json", "User-Agent": "bitvavo-early-v2/1.0"}


def f(x, default=0.0):
    try:
        return float(x)
    except Exception:
        return default


def pct(a, b):
    return (a / b - 1) * 100 if b else None


def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def ema(values, period):
    if not values:
        return None
    a = 2 / (period + 1)
    e = values[0]
    for x in values[1:]:
        e = a * x + (1 - a) * e
    return e


def get_json(path, params=None, retries=3):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            err = e
            time.sleep(0.8 + attempt)
    raise RuntimeError(f"API {url}: {err}")


def candles(market, interval, limit=40):
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
            wick = max(wick, max(0, c["h"] - max(c["o"], c["c"])) / rng)
    prev20 = vols[-21:-1] if len(vols) >= 21 else vols[:-1]
    return {
        "last": closes[-1],
        "ch1": pct(closes[-1], closes[-2]),
        "ch4": pct(closes[-1], closes[-5]) if len(closes) >= 5 else None,
        "ch16": pct(closes[-1], closes[-17]) if len(closes) >= 17 else None,
        "vr1": vols[-1] / mean(prev20) if mean(prev20) else None,
        "vr4": sum(vols[-4:]) / sum(vols[-8:-4]) if sum(vols[-8:-4]) else None,
        "ema20": ema(closes, 20),
        "dist8high": pct(closes[-1], hi),
        "range8": (hi - lo) / closes[-1] * 100 if closes[-1] else None,
        "wick": wick,
    }


def book(market):
    b = get_json(f"/{market}/book", {"depth": 50})
    bids, asks = b.get("bids", []), b.get("asks", [])
    bv = sum(f(p) * f(q) for p, q in bids)
    av = sum(f(p) * f(q) for p, q in asks)
    return {"bid_share": bv / (bv + av) if bv + av else None, "bid_eur": bv, "ask_eur": av}


def load_history():
    try:
        d = json.loads(HISTORY.read_text(encoding="utf-8")) if HISTORY.exists() else {}
    except Exception:
        d = {}
    d.setdefault("version", 2)
    d.setdefault("markets", {})
    return d


def nearest(samples, now_ts, minutes):
    target = minutes * 60
    tol = max(6 * 60, target * 0.55)
    c = []
    for s in samples:
        age = now_ts - f(s.get("ts"))
        if age >= 90:
            c.append((abs(age - target), s))
    if not c:
        return None
    c.sort(key=lambda x: x[0])
    return c[0][1] if c[0][0] <= tol else None


def trajectory(row, rank, hm, now_ts):
    out = {}
    samples = hm.get("samples", [])
    for m in (5, 15, 30, 60):
        old = nearest(samples, now_ts, m)
        if old:
            out[f"dscore_{m}m"] = round(f(row.get("collector_priority")) - f(old.get("priority")), 4)
            out[f"drank_{m}m"] = round(f(old.get("rank")) - rank, 1) if old.get("rank") else None
            out[f"dprice_{m}m_pct"] = round(pct(f(row.get("last")), f(old.get("last"))), 4) if old.get("last") else None
        else:
            out[f"dscore_{m}m"] = out[f"drank_{m}m"] = out[f"dprice_{m}m_pct"] = None
    return out


def early_score(row, t):
    s = row.get("m15") or {}
    vr1 = max(0, f(s.get("volume_last_vs_prev20")))
    vr4 = max(0, f(s.get("volume_4_vs_prev4")))
    ch1h = f(s.get("change_4_candles_pct"))
    ch4h = f(s.get("change_16_candles_pct"))
    ch24 = f(row.get("change_24h_pct"))
    vol = f(row.get("quote_volume_24h_eur"))
    spread = f(row.get("spread_pct"), 99)
    wick = f(s.get("max_upper_wick_ratio_8bar"))

    x = 1.0
    x += min(max(vr1 - 1, 0), 8) * 0.22
    x += min(max(vr4 - 1, 0), 6) * 0.48
    x += 0.65 if 0.15 <= ch1h <= 3.5 else (0.25 if 3.5 < ch1h <= 6 else (-0.45 if ch1h < -1.5 else 0))
    x += 0.55 if 0 <= ch4h <= 6 else (0.10 if 6 < ch4h <= 10 else 0)

    d15, d30 = t.get("dscore_15m"), t.get("dscore_30m")
    r15, r30 = t.get("drank_15m"), t.get("drank_30m")
    if d15 is not None:
        x += min(max(d15, 0), 5) * 0.42
        x -= 0.35 if d15 < -1.5 else 0
    if d30 is not None:
        x += min(max(d30, 0), 6) * 0.20
    if r15 is not None:
        x += min(max(r15, 0), 100) / 100 * 1.25
    if r30 is not None:
        x += min(max(r30, 0), 150) / 150 * 0.65

    x += 0.60 if vol >= 250000 else (0.40 if vol >= 75000 else (0.15 if vol >= 25000 else (-0.85 if vol < 10000 else 0)))
    x += 0.45 if spread <= 0.08 else (0.25 if spread <= 0.18 else (-0.85 if spread > 0.40 else (-0.35 if spread > 0.25 else 0)))
    x -= min((ch24 - 6) * 0.18, 2.2) if ch24 > 6 else 0
    x -= 1.1 if ch24 > 15 else 0
    x -= min((ch4h - 9) * 0.16, 1.6) if ch4h > 9 else 0
    x -= 1.15 if wick >= 0.90 else (0.75 if wick >= 0.75 else (0.35 if wick >= 0.60 else 0))
    return round(max(0, min(10, x)), 3)


def stage(row, score):
    s = row.get("m15") or {}
    if f(row.get("change_24h_pct")) >= 15 or f(s.get("change_16_candles_pct")) >= 12:
        return "TOO_LATE"
    if score >= 8:
        return "IGNITION"
    if score >= EARLY_TRIGGER:
        return "EARLY"
    if score >= 5:
        return "WATCH"
    return "NONE"


def enrich_market(market):
    try:
        return market, {
            "5m": summarize(candles(market, "5m")),
            "15m": summarize(candles(market, "15m")),
            "1h": summarize(candles(market, "1h")),
            "4h": summarize(candles(market, "4h")),
            "book": book(market),
        }
    except Exception as e:
        return market, {"error": str(e)}


def fmt(x, n=2):
    if x is None:
        return "n/a"
    try:
        return f"{float(x):.{n}f}"
    except Exception:
        return str(x)


def main():
    live = json.loads(LIVE.read_text(encoding="utf-8"))
    rows = live.get("markets", [])
    generated = live.get("generated_at_utc") or datetime.now(timezone.utc).isoformat()
    try:
        now_ts = datetime.fromisoformat(generated.replace("Z", "+00:00")).timestamp()
    except Exception:
        now_ts = time.time()

    hist = load_history()
    hm_all = hist["markets"]

    for rank, row in enumerate(rows, 1):
        market = row["market"]
        hm = hm_all.setdefault(market, {})
        t = trajectory(row, rank, hm, now_ts)
        es = early_score(row, t)
        st = stage(row, es)

        first_seen = hm.get("first_early_seen")
        first_price = hm.get("first_early_price")
        last_early_ts = f(hm.get("last_early_seen_ts"))
        if es >= EARLY_TRIGGER and st != "TOO_LATE":
            if not first_seen or (last_early_ts and now_ts - last_early_ts > SESSION_RESET_SEC):
                first_seen, first_price = generated, f(row.get("last"))
                hm["first_early_score"] = es
            hm.update({"first_early_seen": first_seen, "first_early_price": first_price, "last_early_seen_ts": now_ts})
        elif es < EARLY_RESET and last_early_ts and now_ts - last_early_ts > SESSION_RESET_SEC:
            for k in ("first_early_seen", "first_early_price", "first_early_score", "last_early_seen_ts"):
                hm.pop(k, None)
            first_seen = first_price = None

        t["first_early_seen"] = first_seen
        t["first_early_price"] = first_price
        t["price_since_first_early_pct"] = round(pct(f(row.get("last")), f(first_price)), 4) if first_price else None
        row["current_rank"] = rank
        row["trajectory"] = t
        row["early_score"] = es
        row["early_stage"] = st

    early = sorted(rows, key=lambda r: (r.get("early_score", -1), r.get("collector_priority", -1)), reverse=True)
    enrich_names = [r["market"] for r in early[:ENRICH_COUNT]]
    enriched = {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = [ex.submit(enrich_market, m) for m in enrich_names]
        for fut in as_completed(futs):
            m, data = fut.result()
            enriched[m] = data

    cutoff = now_ts - MAX_HISTORY_SEC
    active = set()
    for row in rows:
        market = row["market"]
        active.add(market)
        hm = hm_all.setdefault(market, {})
        samples = [s for s in hm.get("samples", []) if f(s.get("ts")) >= cutoff]
        m15 = row.get("m15") or {}
        samples.append({
            "ts": now_ts, "rank": row.get("current_rank"), "priority": row.get("collector_priority"),
            "early": row.get("early_score"), "last": row.get("last"), "ch24": row.get("change_24h_pct"),
            "vr1": m15.get("volume_last_vs_prev20"), "vr4": m15.get("volume_4_vs_prev4"),
        })
        hm["samples"] = samples[-MAX_SAMPLES:]
    for market in list(hm_all):
        hm = hm_all[market]
        hm["samples"] = [s for s in hm.get("samples", []) if f(s.get("ts")) >= cutoff][-MAX_SAMPLES:]
        if market not in active and not hm["samples"]:
            hm_all.pop(market, None)

    hist["generated_at_utc"] = generated
    HISTORY.write_text(json.dumps(hist, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    def tf(s):
        return f"ch1={fmt(s.get('ch1'))},ch4={fmt(s.get('ch4'))},ch16={fmt(s.get('ch16'))},vr1={fmt(s.get('vr1'))},vr4={fmt(s.get('vr4'))},wick={fmt(s.get('wick'))}"

    lines = [
        "BITVAVO EARLY WATCH V2",
        f"generated_at_utc: {generated}",
        "NOTE: early_score mesure la vitesse de transition; validation finale NIL/HEI/HUMA obligatoire.",
        "rank | market | early | stage | current_rank | priority | dscore15 | drank15 | dscore30 | drank30 | price15% | since_first% | ch24% | vol24EUR | spread% | 5m | 1h | 4h | bid_share | first_seen",
    ]
    for i, row in enumerate(early[:WATCH_COUNT], 1):
        t = row["trajectory"]
        e = enriched.get(row["market"], {})
        b = e.get("book", {}) if isinstance(e, dict) else {}
        lines.append(
            f"{i} | {row['market']} | {fmt(row['early_score'],3)} | {row['early_stage']} | {row['current_rank']} | {fmt(row.get('collector_priority'),3)} | "
            f"{fmt(t.get('dscore_15m'))} | {fmt(t.get('drank_15m'),0)} | {fmt(t.get('dscore_30m'))} | {fmt(t.get('drank_30m'),0)} | "
            f"{fmt(t.get('dprice_15m_pct'))} | {fmt(t.get('price_since_first_early_pct'))} | {fmt(row.get('change_24h_pct'))} | "
            f"{fmt(row.get('quote_volume_24h_eur'),0)} | {fmt(row.get('spread_pct'),4)} | "
            f"5m[{tf(e.get('5m', {}))}] | 1h[{tf(e.get('1h', {}))}] | 4h[{tf(e.get('4h', {}))}] | "
            f"{fmt(b.get('bid_share'),3)} | {t.get('first_early_seen') or 'n/a'}"
        )
    EARLY_TXT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    out = {
        "generated_at_utc": generated,
        "method_note": "EARLY V2 = deltas score/rang/prix + volume + pénalité mouvement déjà avancé; ce n'est pas un signal d'achat.",
        "history_window_hours": MAX_HISTORY_SEC / 3600,
        "watch": early[:WATCH_COUNT],
        "enriched": enriched,
    }
    EARLY_JSON.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    # Le chemin historique scan_feed.txt reste compatible : on y préfixe la couche EARLY V2.
    base_scan = SCAN.read_text(encoding="utf-8") if SCAN.exists() else ""
    prefix = "\n".join(lines[:min(len(lines), 18)]) + "\n\n--- CURRENT_STRENGTH SNAPSHOT ---\n"
    SCAN.write_text(prefix + base_scan, encoding="utf-8")
    print(f"EARLY V2: {len(rows)} marchés, {len(enriched)} enrichis, historique {MAX_HISTORY_SEC//3600}h")


if __name__ == "__main__":
    main()
