#!/usr/bin/env python3
"""Read-only causal liquidity/volume diagnostic for Solaire shadow evaluations.

This script DOES NOT rank buys, predict profits, change production gates,
or acquire market caps using fragile/unverified token-symbol matching.
It can ingest a *separately verified, timestamped* market-cap snapshot.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "solaire_volume_turnover_shadow_v1"
UTC = timezone.utc


class BadEvidence(ValueError):
    pass


def utc(value, field):
    if not isinstance(value, str):
        raise BadEvidence(f"{field}: missing UTC timestamp")
    try:
        date = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise BadEvidence(f"{field}: invalid timestamp") from exc
    if date.tzinfo is None or date.utcoffset().total_seconds() != 0:
        raise BadEvidence(f"{field}: UTC timezone required")
    return date.astimezone(UTC)


def amount(value):
    if type(value) not in (float, int) or not math.isfinite(value):
        return None
    return float(value) if value >= 0 else None


def positive(value):
    v = amount(value)
    return v if v is not None and v > 0 else None


def cap_map(cap_snapshot):
    if cap_snapshot is None:
        return {}
    if not isinstance(cap_snapshot, dict) or not isinstance(cap_snapshot.get("rows"), list):
        raise BadEvidence("market-cap source requires JSON object with rows array")
    result = {}
    for cap in cap_snapshot["rows"]:
        if not isinstance(cap, dict) or not isinstance(cap.get("market"), str):
            raise BadEvidence("market-cap rows need market")
        name = cap["market"]
        if name in result:
            raise BadEvidence(f"duplicate market-cap identity for {name}")
        result[name] = cap
    return result


def cap_metrics(row, cap, live_ts, max_cap_age_hours):
    if cap is None:
        return {"status": "CAP_UNAVAILABLE", "cap_eur": None, "turnover_bitvavo_24h_pct": None,
                "turnover_global_24h_pct": None, "cap_source": None,
                "cap_asof_utc": None}
    cap_asof = cap.get("asof_utc")
    data = {"status": "CAP_UNVERIFIED", "cap_eur": None, "turnover_bitvavo_24h_pct": None,
            "turnover_global_24h_pct": None, "cap_source": None,
            "cap_asof_utc": cap_asof if isinstance(cap_asof, str) else None}
    if cap.get("identity_verified") is not True or not isinstance(cap.get("asset_id"), str) or not cap["asset_id"].strip():
        return data
    if not isinstance(cap.get("source"), str) or not cap["source"].strip():
        return data
    if cap_asof is None:
        return data
    try:
        date = utc(cap_asof, "cap.asof_utc")
    except BadEvidence:
        return data
    lag_hours = (live_ts - date).total_seconds() / 3600
    if lag_hours < 0:
        data["status"] = "CAP_FUTURE_LOOKAHEAD"
        return data
    if lag_hours > max_cap_age_hours:
        data["status"] = "CAP_STALE"
        return data
    mc = positive(cap.get("market_cap_eur"))
    if mc is None:
        return data
    data.update(status="CAP_VALID", cap_eur=mc, cap_source=cap["source"],
                cap_asof_utc=date.isoformat())
    exchange_vol = amount(row.get("quote_volume_24h_eur"))
    if exchange_vol is not None:
        data["turnover_bitvavo_24h_pct"] = round(exchange_vol / mc * 100, 5)
    global_volume = amount(cap.get("global_volume_24h_eur"))
    if global_volume is not None:
        # Must originate from same verified provider and share its timestamp.
        data["turnover_global_24h_pct"] = round(global_volume / mc * 100, 5)
    return data


def summarize(live, caps=None, max_cap_age_hours=24):
    if not isinstance(live, dict) or not isinstance(live.get("markets"), list):
        raise BadEvidence("live requires markets array")
    live_at = utc(live.get("generated_at_utc"), "live.generated_at_utc")
    cm = cap_map(caps)
    output, seen = [], set()
    for row in live["markets"]:
        if not isinstance(row, dict):
            raise BadEvidence("market row must be a mapping")
        market = row.get("market")
        if not isinstance(market, str) or not market.endswith("-EUR") or market in seen:
            raise BadEvidence(f"invalid/duplicate market {market!r}")
        seen.add(market)
        features = row.get("m15") or {}
        if not isinstance(features, dict):
            features = {}
        last15 = amount(features.get("volume_last_vs_prev20"))
        last1h = amount(features.get("volume_4_vs_prev4"))
        last4h = amount(features.get("volume_16_vs_prev16"))
        cap = cap_metrics(row, cm.get(market), live_at, max_cap_age_hours)
        record = {
            "market": market,
            "price_eur": positive(row.get("last")),
            "bitvavo_quote_volume_24h_eur": amount(row.get("quote_volume_24h_eur")),
            "spread_pct": amount(row.get("spread_pct")),
            "volume_last_15m_vs_prev20": last15,
            "volume_last_1h_vs_prev_1h": last1h,
            "volume_last_4h_vs_prev_4h": last4h,
            **cap,
        }
        # No recommendation, score or signal generated by this diagnostic.
        output.append(record)
    count = Counter(x["status"] for x in output)
    top_4h = sorted((x for x in output if x["volume_last_4h_vs_prev_4h"] is not None),
                    key=lambda x: (-x["volume_last_4h_vs_prev_4h"], x["market"]))[:20]
    top_turn = sorted((x for x in output if x["turnover_bitvavo_24h_pct"] is not None),
                      key=lambda x: (-x["turnover_bitvavo_24h_pct"], x["market"]))[:20]
    return {
        "schema": SCHEMA,
        "snapshot_at_utc": live_at.isoformat(),
        "source": "bitvavo_live.json + optional identity-verified marketcap rows",
        "measurement_only": True,
        "changes_detection": False,
        "changes_buy_gate": False,
        "changes_email": False,
        "ranked_not_actionable": True,
        "market_count": len(output),
        "cap_validation_counts": dict(count),
        "cap_coverage_pct": round(100 * count.get("CAP_VALID", 0) / len(output), 2) if output else 0,
        "largest_4h_relative_volume_descriptive": [{"market": x["market"], "volume_last_4h_vs_prev_4h": x["volume_last_4h_vs_prev_4h"]} for x in top_4h],
        "largest_bitvavo_turnover_descriptive": [{"market": x["market"], "turnover_bitvavo_24h_pct": x["turnover_bitvavo_24h_pct"]} for x in top_turn],
        "observations": output,
        "known_limitations": [
            "Volume Bitvavo is a subset of exchange/global activity; it is not global token turnover.",
            "Global turnover is only computed from volume and cap in a single verified capitalisation snapshot.",
            "Same token symbols may refer to different assets: cap identity must be curated, never inferred from ticker alone.",
            "Coin market caps may use circulating supply estimates and can diverge by vendor.",
            "15-minute volume ratios come from the snapshot's candle aggregates, not complete trade books.",
            "RVOL and turnover are diagnostics only; no future price or execution outcome is implied.",
            "True predictive impact requires frozen ex-ante snapshots and prospective OOS comparisons of winners AND losers.",
        ],
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--live", required=True)
    p.add_argument("--marketcap", help="optional timestamped verified identity mapping")
    p.add_argument("--output", required=True)
    p.add_argument("--max-cap-age-hours", type=float, default=24)
    a = p.parse_args(argv)
    try:
        if a.max_cap_age_hours <= 0 or not math.isfinite(a.max_cap_age_hours):
            raise BadEvidence("max cap age must be positive finite hours")
        live = json.loads(Path(a.live).read_text(encoding="utf-8"))
        caps = json.loads(Path(a.marketcap).read_text(encoding="utf-8")) if a.marketcap else None
        report = summarize(live, caps, a.max_cap_age_hours)
        out = json.dumps(report, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
        Path(a.output).parent.mkdir(parents=True, exist_ok=True)
        Path(a.output).write_text(out, encoding="utf-8")
        print(json.dumps({"status": "OK", "markets": report["market_count"],
                          "cap_coverage_pct": report["cap_coverage_pct"],
                          "output": a.output, "snapshot_at_utc": report["snapshot_at_utc"]}))
        return 0
    except (BadEvidence, OSError, ValueError) as exc:
        print(f"VOLUME_SHADOW_INPUT_ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
