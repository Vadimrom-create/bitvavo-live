#!/usr/bin/env python3
"""
Collecteur public Bitvavo -> bitvavo_live.json
Aucune clé API n'est nécessaire. Le script ne lit ni le wallet ni les ordres.
"""

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
OUTPUT = Path("bitvavo_live.json")
SCAN_FEED = Path("scan_feed.txt")

# On écarte seulement les marchés quasi inactifs. Le scan reste très large.
MIN_QUOTE_VOLUME_EUR_24H = 5_000.0

# Données détaillées multi-timeframe pour les meilleurs profils du pré-filtre.
DETAIL_COUNT = 60
ORDERBOOK_COUNT = 30

HEADERS = {
    "Accept": "application/json",
    "User-Agent": "bitvavo-live-bridge/1.0"
}

def get_json(path: str, params: dict | None = None, retries: int = 4):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    last_error = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            last_error = e
            time.sleep(1.0 + attempt * 1.5)
    raise RuntimeError(f"Échec API {url}: {last_error}")

def f(x, default=0.0):
    try:
        return float(x)
    except Exception:
        return default

def candles(market: str, interval: str, limit: int):
    data = get_json(f"/{market}/candles", {"interval": interval, "limit": limit})
    rows = []
    for row in data:
        if len(row) < 6:
            continue
        rows.append({
            "t": int(row[0]),
            "o": f(row[1]),
            "h": f(row[2]),
            "l": f(row[3]),
            "c": f(row[4]),
            "v": f(row[5]),
        })
    rows.sort(key=lambda x: x["t"])
    return rows

def safe_ratio(a, b):
    if not b:
        return None
    return a / b

def pct(a, b):
    if not b:
        return None
    return (a / b - 1.0) * 100.0

def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None

def ema(values, period):
    if not values:
        return None
    alpha = 2.0 / (period + 1.0)
    e = values[0]
    for x in values[1:]:
        e = alpha * x + (1 - alpha) * e
    return e

def candle_upper_wick_ratio(c):
    rng = c["h"] - c["l"]
    if rng <= 0:
        return 0.0
    return max(0.0, c["h"] - max(c["o"], c["c"])) / rng

def summarize(cs):
    if len(cs) < 10:
        return {}
    closes = [x["c"] for x in cs]
    vols = [x["v"] for x in cs]
    latest = cs[-1]
    last4 = vols[-4:]
    prev4 = vols[-8:-4]
    last16 = vols[-16:] if len(vols) >= 16 else vols
    prev16 = vols[-32:-16] if len(vols) >= 32 else []
    prev20 = vols[-21:-1] if len(vols) >= 21 else vols[:-1]
    recent = cs[-8:]
    recent_high = max(x["h"] for x in recent)
    recent_low = min(x["l"] for x in recent)
    upper_wick_max = max(candle_upper_wick_ratio(x) for x in recent)
    return {
        "last": latest["c"],
        "change_1_candle_pct": pct(closes[-1], closes[-2]) if len(closes) >= 2 else None,
        "change_4_candles_pct": pct(closes[-1], closes[-5]) if len(closes) >= 5 else None,
        "change_16_candles_pct": pct(closes[-1], closes[-17]) if len(closes) >= 17 else None,
        "volume_last_vs_prev20": safe_ratio(vols[-1], mean(prev20) or 0),
        "volume_4_vs_prev4": safe_ratio(sum(last4), sum(prev4)) if prev4 else None,
        "volume_16_vs_prev16": safe_ratio(sum(last16), sum(prev16)) if prev16 else None,
        "ema20": ema(closes[-60:], 20),
        "ema50": ema(closes[-100:], 50),
        "distance_from_8bar_high_pct": pct(latest["c"], recent_high),
        "range_8bar_pct": ((recent_high - recent_low) / latest["c"] * 100.0) if latest["c"] else None,
        "max_upper_wick_ratio_8bar": upper_wick_max,
    }

def priority_score(summary15, quote_vol, change24, spread_pct):
    # Ce score sert uniquement à choisir quels marchés enrichir en 1h/4h.
    # Ce n'est PAS le score final du scan.
    vr1 = summary15.get("volume_last_vs_prev20") or 0
    vr4 = summary15.get("volume_4_vs_prev4") or 0
    ch1h = summary15.get("change_4_candles_pct") or 0
    ch4h = summary15.get("change_16_candles_pct") or 0
    wick = summary15.get("max_upper_wick_ratio_8bar") or 0
    liq = max(0.0, min(2.0, (math.log10(max(quote_vol, 1)) - 4.0) / 2.0))
    score = (
        min(vr1, 4.0) * 1.2
        + min(vr4, 3.0) * 1.4
        + max(-2.0, min(ch1h, 5.0)) * 0.35
        + max(-3.0, min(ch4h, 8.0)) * 0.18
        + liq
    )
    # Pénalise les profils déjà verticaux / rejetés / illiquides.
    if ch1h > 8 or ch4h > 15 or change24 > 25:
        score -= 3.0
    score -= wick * 2.0
    if spread_pct is not None and spread_pct > 0.8:
        score -= 2.0
    return round(score, 4)

def book_metrics(market):
    b = get_json(f"/{market}/book", {"depth": 50})
    bids = b.get("bids", [])
    asks = b.get("asks", [])
    bid_eur = sum(f(p) * f(q) for p, q in bids)
    ask_eur = sum(f(p) * f(q) for p, q in asks)
    total = bid_eur + ask_eur
    return {
        "bid_notional_eur_50": round(bid_eur, 2),
        "ask_notional_eur_50": round(ask_eur, 2),
        "bid_share_50": round(bid_eur / total, 4) if total else None,
        "best_5_bids": bids[:5],
        "best_5_asks": asks[:5],
    }


def fmt(x, digits=4):
    if x is None:
        return "n/a"
    try:
        return f"{float(x):.{digits}f}"
    except Exception:
        return str(x)

def write_scan_feed(generated_at, good, details):
    """Petit fichier texte multi-lignes, pensé pour être lu facilement par ChatGPT."""
    lines = []
    lines.append("BITVAVO SCAN FEED")
    lines.append(f"generated_at_utc: {generated_at}")
    lines.append(f"markets_in_prefilter: {len(good)}")
    lines.append("NOTE: collector_priority est un préfiltre, jamais un signal d'achat.")
    lines.append("")

    # Toujours inclure le contexte BTC s'il existe.
    btc = next((x for x in good if x.get("market") == "BTC-EUR"), None)
    if btc:
        lines.append(
            "BTC_CONTEXT | "
            f"last={btc.get('last')} | change24={fmt(btc.get('change_24h_pct'),2)}% | "
            f"vol24_eur={fmt(btc.get('quote_volume_24h_eur'),0)} | spread={fmt(btc.get('spread_pct'),4)}%"
        )
        lines.append("")

    lines.append("TOP_CANDIDATES")
    lines.append(
        "rank | market | priority | last | ch24% | vol24EUR | spread% | "
        "15m[ch1,ch4,ch16,vol1/20,vol4/4,ema20,dist8high,wick] | "
        "1h[ch1,ch4,ch16,vol1/20,vol4/4,ema20,dist8high,wick] | "
        "4h[ch1,ch4,ch16,vol1/20,vol4/4,ema20,dist8high,wick] | book_bid_share"
    )

    # 35 lignes donnent au modèle un univers assez large sans fabriquer un monstre de 600 Ko.
    for rank, row in enumerate(good[:35], 1):
        market = row["market"]
        d = details.get(market, {})
        m15 = d.get("m15_summary") or row.get("m15") or {}
        h1 = d.get("h1_summary") or {}
        h4 = d.get("h4_summary") or {}
        book = d.get("orderbook") or {}

        def tf(s):
            return ",".join([
                fmt(s.get("change_1_candle_pct"),2),
                fmt(s.get("change_4_candles_pct"),2),
                fmt(s.get("change_16_candles_pct"),2),
                fmt(s.get("volume_last_vs_prev20"),2),
                fmt(s.get("volume_4_vs_prev4"),2),
                fmt(s.get("ema20"),8),
                fmt(s.get("distance_from_8bar_high_pct"),2),
                fmt(s.get("max_upper_wick_ratio_8bar"),2),
            ])

        lines.append(
            f"{rank} | {market} | {fmt(row.get('collector_priority'),3)} | "
            f"{row.get('last')} | {fmt(row.get('change_24h_pct'),2)} | "
            f"{fmt(row.get('quote_volume_24h_eur'),0)} | {fmt(row.get('spread_pct'),4)} | "
            f"15m[{tf(m15)}] | 1h[{tf(h1)}] | 4h[{tf(h4)}] | "
            f"{fmt(book.get('bid_share_50'),3)}"
        )

    # Inclure quelques actifs de référence / portefeuille s'ils n'étaient pas dans le top 35.
    refs = ["SEI-EUR", "ZK-EUR", "JUP-EUR", "ETHFI-EUR", "HUMA-EUR", "NIL-EUR", "HEI-EUR", "BTC-EUR"]
    existing = {r["market"] for r in good[:35]}
    extras = [r for r in good if r["market"] in refs and r["market"] not in existing]
    if extras:
        lines.append("")
        lines.append("REFERENCE_MARKETS")
        for row in extras:
            market = row["market"]
            d = details.get(market, {})
            m15 = d.get("m15_summary") or row.get("m15") or {}
            h1 = d.get("h1_summary") or {}
            h4 = d.get("h4_summary") or {}
            book = d.get("orderbook") or {}
            lines.append(
                f"{market} | priority={fmt(row.get('collector_priority'),3)} | last={row.get('last')} | "
                f"ch24={fmt(row.get('change_24h_pct'),2)}% | vol24EUR={fmt(row.get('quote_volume_24h_eur'),0)} | "
                f"spread={fmt(row.get('spread_pct'),4)}% | "
                f"15m_ch4={fmt(m15.get('change_4_candles_pct'),2)}% | 15m_vol4/4={fmt(m15.get('volume_4_vs_prev4'),2)} | "
                f"1h_ch4={fmt(h1.get('change_4_candles_pct'),2)}% | 1h_vol4/4={fmt(h1.get('volume_4_vs_prev4'),2)} | "
                f"4h_ch4={fmt(h4.get('change_4_candles_pct'),2)}% | bid_share={fmt(book.get('bid_share_50'),3)}"
            )

    SCAN_FEED.write_text("\n".join(lines) + "\n", encoding="utf-8")

def main():
    markets_raw = get_json("/markets")
    ticker_raw = get_json("/ticker/24h")
    ticker = {x.get("market"): x for x in ticker_raw if isinstance(x, dict)}

    active = []
    for m in markets_raw:
        if m.get("quote") == "EUR" and m.get("status") == "trading":
            name = m.get("market")
            t = ticker.get(name, {})
            qv = f(t.get("volumeQuote"))
            if qv >= MIN_QUOTE_VOLUME_EUR_24H:
                active.append(name)

    def collect15(market):
        try:
            cs = candles(market, "15m", 100)
            t = ticker.get(market, {})
            last = f(t.get("last"))
            open24 = f(t.get("open"))
            bid = f(t.get("bid"))
            ask = f(t.get("ask"))
            quote_vol = f(t.get("volumeQuote"))
            change24 = pct(last, open24) or 0.0
            spread_pct = ((ask - bid) / ((ask + bid) / 2) * 100.0) if bid and ask else None
            s15 = summarize(cs)
            return {
                "market": market,
                "last": last,
                "change_24h_pct": round(change24, 4),
                "quote_volume_24h_eur": round(quote_vol, 2),
                "bid": bid,
                "ask": ask,
                "spread_pct": round(spread_pct, 5) if spread_pct is not None else None,
                "m15": s15,
                "collector_priority": priority_score(s15, quote_vol, change24, spread_pct),
            }
        except Exception as e:
            return {"market": market, "error": str(e)}

    summaries = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = [ex.submit(collect15, m) for m in active]
        for fut in as_completed(futs):
            summaries.append(fut.result())

    good = [x for x in summaries if "error" not in x]
    good.sort(key=lambda x: x.get("collector_priority", -999), reverse=True)
    detailed_names = [x["market"] for x in good[:DETAIL_COUNT]]

    details = {}
    def collect_detail(market):
        try:
            c15 = candles(market, "15m", 40)
            c1h = candles(market, "1h", 40)
            c4h = candles(market, "4h", 40)
            return market, {
                "m15_summary": summarize(c15),
                "h1_summary": summarize(c1h),
                "h4_summary": summarize(c4h),
                "recent_candles": {
                    "15m": c15[-16:],
                    "1h": c1h[-16:],
                    "4h": c4h[-16:],
                }
            }
        except Exception as e:
            return market, {"error": str(e)}

    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = [ex.submit(collect_detail, m) for m in detailed_names]
        for fut in as_completed(futs):
            market, data = fut.result()
            details[market] = data

    # Carnet seulement pour les 30 plus prioritaires.
    for market in detailed_names[:ORDERBOOK_COUNT]:
        try:
            details.setdefault(market, {})["orderbook"] = book_metrics(market)
        except Exception as e:
            details.setdefault(market, {})["orderbook_error"] = str(e)

    generated_at = datetime.now(timezone.utc).isoformat()
    out = {
        "generated_at_utc": generated_at,
        "source": "Bitvavo public REST API",
        "no_api_key_used": True,
        "method_note": (
            "collector_priority sert uniquement de pré-filtre technique pour enrichir "
            "les marchés en 1h/4h. Le classement final doit être fait par le scan ChatGPT "
            "avec les règles NIL/HEI/HUMA et le contexte de marché."
        ),
        "active_eur_markets_above_min_volume": len(active),
        "min_quote_volume_eur_24h": MIN_QUOTE_VOLUME_EUR_24H,
        "markets": good,
        "details": details,
    }

    OUTPUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    write_scan_feed(generated_at, good, details)
    print(f"Écrit: {OUTPUT} + {SCAN_FEED} | {len(good)} marchés | {len(details)} détaillés")

if __name__ == "__main__":
    main()
