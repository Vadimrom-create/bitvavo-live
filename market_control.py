#!/usr/bin/env python3
"""Cross-sectional control table for every scan.

Purpose: complement prospective V3/V4 signals with an independent ranking of the
full active Bitvavo EUR universe by current 24h performance, then show whether
V3/V4 detected each leader. Public data only; no account/API key required.
"""

from __future__ import annotations

import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://api.bitvavo.com/v2"
HEADERS = {"Accept": "application/json", "User-Agent": "bitvavo-market-control/1.0"}

V4_PATH = Path("v4_watch.json")
V3_PATH = Path("early_watch.json")
COLLECTOR_PATH = Path("bitvavo_live.json")
OUT_JSON = Path("market_control.json")
OUT_TXT = Path("market_control.txt")

TOP_TEXT_COUNT = 40
TOP_COVERAGE_COUNTS = (10, 20, 40)
MATERIAL_MOVER_PCT = 5.0


def get_json(path: str, params: dict | None = None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def load(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def f(value, default=None):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def pct(last, open_):
    if not last or not open_:
        return None
    return (last / open_ - 1.0) * 100.0


def index_watch(payload: dict) -> dict[str, dict]:
    return {
        row.get("market"): row
        for row in payload.get("watch", [])
        if isinstance(row, dict) and row.get("market")
    }


def classify(v4: dict | None, v3: dict | None) -> str:
    if v4:
        action = str(v4.get("action_status") or v4.get("raw_action_status") or "WATCH")
        if v4.get("buy_ready") or action in {"BUY_READY", "REENTRY_READY"}:
            return "V4_ACTIONABLE"
        if action not in {"NONE", ""}:
            return "V4_TRACKED"
    if v3:
        if v3.get("buy_ready"):
            return "V3_BUY_ONLY"
        return "V3_TRACKED_ONLY"
    return "NOT_DETECTED_V3_V4"


def main():
    v4_payload = load(V4_PATH)
    v3_payload = load(V3_PATH)
    collector_payload = load(COLLECTOR_PATH)
    v4_idx = index_watch(v4_payload)
    v3_idx = index_watch(v3_payload)
    collector_idx = {
        row.get("market"): row
        for row in collector_payload.get("markets", [])
        if isinstance(row, dict) and row.get("market")
    }

    markets_raw = get_json("/markets")
    ticker_raw = get_json("/ticker/24h")
    ticker_idx = {
        row.get("market"): row
        for row in ticker_raw
        if isinstance(row, dict) and row.get("market")
    }

    active_eur = sorted(
        row.get("market")
        for row in markets_raw
        if isinstance(row, dict)
        and row.get("quote") == "EUR"
        and row.get("status") == "trading"
        and row.get("market")
    )

    rows = []
    for market in active_eur:
        t = ticker_idx.get(market, {})
        last = f(t.get("last"))
        open_ = f(t.get("open"))
        bid = f(t.get("bid"))
        ask = f(t.get("ask"))
        change = pct(last, open_)
        quote_volume = f(t.get("volumeQuote"), 0.0) or 0.0
        spread = None
        if bid and ask:
            mid = (bid + ask) / 2.0
            if mid:
                spread = (ask - bid) / mid * 100.0

        v4 = v4_idx.get(market)
        v3 = v3_idx.get(market)
        collector = collector_idx.get(market)
        rows.append({
            "market": market,
            "last": last,
            "change_24h_pct": round(change, 4) if change is not None else None,
            "quote_volume_24h_eur": round(quote_volume, 2),
            "bid": bid,
            "ask": ask,
            "spread_pct": round(spread, 5) if spread is not None else None,
            "in_collector_prefilter": collector is not None,
            "collector_priority": collector.get("collector_priority") if collector else None,
            "v4_present": v4 is not None,
            "v4_action": (v4 or {}).get("action_status"),
            "v4_raw_action": (v4 or {}).get("raw_action_status"),
            "v4_opportunity": (v4 or {}).get("opportunity_score"),
            "v4_entry": (v4 or {}).get("entry_score"),
            "v4_trend": (v4 or {}).get("trend_score"),
            "v4_buy_ready": bool((v4 or {}).get("buy_ready")),
            "v4_risk_flags": (v4 or {}).get("risk_flags", []),
            "v3_present": v3 is not None,
            "v3_stage": (v3 or {}).get("early_stage"),
            "v3_mode": (v3 or {}).get("signal_mode"),
            "v3_score": (v3 or {}).get("final_score"),
            "v3_buy_ready": bool((v3 or {}).get("buy_ready")),
            "audit_state": classify(v4, v3),
        })

    rows.sort(
        key=lambda row: row.get("change_24h_pct")
        if row.get("change_24h_pct") is not None else -10**9,
        reverse=True,
    )
    for rank, row in enumerate(rows, 1):
        row["rank_24h"] = rank

    coverage = {}
    for count in TOP_COVERAGE_COUNTS:
        sample = rows[:count]
        v4_seen = sum(1 for r in sample if r["v4_present"])
        v3_seen = sum(1 for r in sample if r["v3_present"])
        either_seen = sum(1 for r in sample if r["v4_present"] or r["v3_present"])
        coverage[f"top_{count}"] = {
            "count": len(sample),
            "v4_seen": v4_seen,
            "v3_seen": v3_seen,
            "either_seen": either_seen,
            "either_coverage_pct": round(100.0 * either_seen / len(sample), 1) if sample else None,
        }

    material_misses = [
        r for r in rows
        if (r.get("change_24h_pct") or -999) >= MATERIAL_MOVER_PCT
        and not r["v4_present"]
        and not r["v3_present"]
    ]

    prospective = sorted(
        [
            r for r in rows
            if r["v4_buy_ready"] and (r.get("change_24h_pct") or 0.0) < 8.0
        ],
        key=lambda r: (r.get("v4_opportunity") or -999, r.get("v4_entry") or -999),
        reverse=True,
    )

    generated_at = datetime.now(timezone.utc).isoformat()
    output = {
        "generated_at_utc": generated_at,
        "source": "Bitvavo public REST API + current V3/V4 outputs",
        "purpose": "Mandatory second reading for every scan: full active EUR market leaderboard cross-checked against prospective V3/V4 detection.",
        "active_eur_market_count": len(rows),
        "v4_generated_at_utc": v4_payload.get("generated_at_utc"),
        "v3_generated_at_utc": v3_payload.get("generated_at_utc"),
        "coverage": coverage,
        "material_mover_threshold_pct": MATERIAL_MOVER_PCT,
        "material_misses": material_misses,
        "prospective_v4_before_leaderboard": prospective,
        "top_gainers": rows[:TOP_TEXT_COUNT],
        "all_markets_ranked_24h": rows,
    }
    OUT_JSON.write_text(json.dumps(output, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    lines = [
        "BITVAVO MARKET CONTROL — FULL ACTIVE EUR UNIVERSE",
        f"generated_at_utc: {generated_at}",
        f"active_eur_markets: {len(rows)}",
        f"v4_generated_at_utc: {v4_payload.get('generated_at_utc')}",
        f"v3_generated_at_utc: {v3_payload.get('generated_at_utc')}",
        "RULE: this is the mandatory second reading of every scan; V3/V4 remain the prospective first reading.",
        "",
        "COVERAGE",
    ]
    for key, value in coverage.items():
        lines.append(
            f"{key}: V4={value['v4_seen']}/{value['count']} | V3={value['v3_seen']}/{value['count']} | "
            f"either={value['either_seen']}/{value['count']} ({value['either_coverage_pct']}%)"
        )

    lines.extend([
        "",
        "TOP_24H_GAINERS",
        "rank | market | ch24% | last | vol24EUR | collector | V4[action,opp,entry,trend] | V3[stage,buy,score] | audit",
    ])
    for r in rows[:TOP_TEXT_COUNT]:
        lines.append(
            f"{r['rank_24h']} | {r['market']} | {r['change_24h_pct']} | {r['last']} | "
            f"{r['quote_volume_24h_eur']:.0f} | {str(r['in_collector_prefilter']).upper()} | "
            f"{r['v4_action'] or '-'}, {r['v4_opportunity'] if r['v4_opportunity'] is not None else '-'}, "
            f"{r['v4_entry'] if r['v4_entry'] is not None else '-'}, {r['v4_trend'] if r['v4_trend'] is not None else '-'} | "
            f"{r['v3_stage'] or '-'}, {str(r['v3_buy_ready']).upper()}, {r['v3_score'] if r['v3_score'] is not None else '-'} | "
            f"{r['audit_state']}"
        )

    lines.extend(["", f"MISSED_MATERIAL_MOVERS_>={MATERIAL_MOVER_PCT:.0f}%"])
    if material_misses:
        for r in material_misses[:30]:
            lines.append(
                f"#{r['rank_24h']} {r['market']} | {r['change_24h_pct']:+.2f}% | "
                f"vol24={r['quote_volume_24h_eur']:.0f} EUR | collector={r['in_collector_prefilter']}"
            )
    else:
        lines.append("none")

    lines.extend(["", "PROSPECTIVE_V4_BEFORE_LEADERBOARD"])
    if prospective:
        for r in prospective[:20]:
            lines.append(
                f"{r['market']} | ch24={r['change_24h_pct']:+.2f}% | V4={r['v4_action']} | "
                f"opp={r['v4_opportunity']} entry={r['v4_entry']} trend={r['v4_trend']}"
            )
    else:
        lines.append("none")

    OUT_TXT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_JSON} + {OUT_TXT} | {len(rows)} active EUR markets")


if __name__ == "__main__":
    main()
