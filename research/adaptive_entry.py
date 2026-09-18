"""Operational adaptive rescue for V4 entry enrichment.

Keeps frozen V4 opportunity/entry scoring intact. Markets skipped by V4's
bounded entry-enrichment stage can be promoted in the same cycle when current
market behaviour warrants a closer look.
"""
from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from v3_common import f, maybe, pct
from v4_common import load_v4_history, save_json, suggested_trade_plan, V4_HISTORY

EXTRA_ENRICH_CAP = 24
URGENT_MOVER_CAP = 12
ACCELERATION_CAP = 8
MIN_PROMOTION_VOLUME_EUR = 75_000
MIN_WATCH_VOLUME_EUR = 30_000
AUDIT_PATH = Path("adaptive_enrichment.json")


def _trajectory_peak(row: dict, key_prefix: str) -> float:
    t = row.get("trajectory") or {}
    vals = [maybe(t.get(f"{key_prefix}_{h}")) for h in ("15m", "30m", "60m")]
    vals = [x for x in vals if x is not None]
    return max(vals) if vals else 0.0


def promotion_signal(row: dict, hist: dict, now_ts: float) -> dict:
    """Selection-only priority. Never changes V4 opportunity or entry scores."""
    vol = f(row.get("quote_volume_24h_eur"))
    ch24 = f(row.get("change_24h_pct"))
    m15 = row.get("m15") or {}
    score = 0.0
    reasons = []

    persistent = f(hist.get("watch_until_ts")) > now_ts
    if persistent and vol >= MIN_WATCH_VOLUME_EUR:
        score += 4.0
        reasons.append("PERSISTENT_WATCH")

    if vol >= MIN_PROMOTION_VOLUME_EUR:
        if ch24 >= 15:
            score += 4.0
            reasons.append("LARGE_MOVER_24H")
        elif ch24 >= 8:
            score += 3.0
            reasons.append("EMERGING_MOVER_24H")
        elif ch24 >= 4:
            score += 1.5
            reasons.append("POSITIVE_MOVER_24H")

        c1 = f(m15.get("change_1_candle_pct"))
        c4 = f(m15.get("change_4_candles_pct"))
        c16 = f(m15.get("change_16_candles_pct"))
        vr1 = f(m15.get("volume_last_vs_prev20"))
        vr4 = f(m15.get("volume_4_vs_prev4"))
        if c1 >= 0.30:
            score += 1.2
            reasons.append("M15_IMPULSE")
        if c4 >= 0.90:
            score += 1.4
            reasons.append("H1_ACCELERATION")
        if c16 >= 2.0:
            score += 0.8
            reasons.append("H4_MOMENTUM")
        if vr1 >= 2.0:
            score += 1.2
            reasons.append("VOLUME_SPIKE")
        elif vr1 >= 1.4:
            score += 0.6
            reasons.append("VOLUME_BUILDING")
        if vr4 >= 1.35:
            score += 0.8
            reasons.append("VOLUME_ACCELERATION")

        rank_jump = _trajectory_peak(row, "drank")
        price_jump = _trajectory_peak(row, "dprice")
        if rank_jump >= 50:
            score += 2.0
            reasons.append("RANK_SURGE")
        elif rank_jump >= 20:
            score += 1.0
            reasons.append("RANK_IMPROVEMENT")
        if price_jump >= 0.75:
            score += 1.0
            reasons.append("FAST_PRICE_ACCELERATION")

        if f(row.get("ignition_score")) >= 7.0:
            score += 1.0
            reasons.append("HIGH_IGNITION")
        if f(row.get("opportunity_score")) >= 7.0:
            score += 0.8
            reasons.append("HIGH_OPPORTUNITY")

    eligible = persistent or score >= 2.5
    return {"eligible": eligible, "score": round(score, 3), "reasons": reasons}


def _apply_frozen_entry_decision(row: dict, enrichment: dict, hm: dict, now_ts: float) -> None:
    """Re-run the existing frozen V4 entry function and thresholds unchanged."""
    import v4_detector

    opp = f(row.get("opportunity_score"))
    profile = row.get("trend_profile") or {}
    ent, flags, hard, entry_mode = v4_detector.entry_score(row, enrichment, profile, opp)
    row["entry_score"] = ent
    row["entry_mode"] = entry_mode
    row["risk_flags"] = flags + hard

    confirms = int(f(hm.get("opportunity_confirm_count")))
    buy_ready = False
    action = "NONE"
    if opp >= v4_detector.OPPORTUNITY_WATCH:
        action = "WATCH"
    if opp >= v4_detector.OPPORTUNITY_STRONG and ent >= v4_detector.ENTRY_WINDOW:
        action = "ENTRY_WINDOW"
    if hard:
        action = "TOO_LATE" if any(x.startswith("TOO_LATE") for x in hard) else "WATCH_RISK"
    else:
        ret7 = maybe(profile.get("ret7d"))
        chase_risk = (f(row.get("change_24h_pct")) > 10.0 or (ret7 is not None and ret7 > 30.0)) and entry_mode != "PULLBACK"
        if chase_risk:
            flags.append("CHASE_RISK")
            row["risk_flags"] = flags + hard
        if (opp >= v4_detector.BUY_OPPORTUNITY and ent >= v4_detector.ENTRY_READY
                and confirms >= v4_detector.CONFIRMATIONS_REQUIRED and not chase_risk):
            action = "BUY_READY"
            buy_ready = True

    last = f(row.get("last"))
    peak = maybe(hm.get("peak_since_signal"))
    drawdown = pct(last, peak) if peak else None
    s15 = enrichment.get("15m") or {}
    rebound = f(s15.get("ch4")) > 0.15 and f((enrichment.get("1h") or {}).get("ch4")) > -1.0
    if (hm.get("ever_buy_ready") and not hard and opp >= 8.0 and ent >= 6.8
            and drawdown is not None and -7.5 <= drawdown <= -0.8 and rebound):
        action = "REENTRY_READY"
        buy_ready = True
        row["reentry_reason"] = f"clean reset {drawdown:.2f}% from post-signal peak + rebound"

    if buy_ready:
        hm["ever_buy_ready"] = True
        hm["last_buy_ready_ts"] = now_ts
    hm["last_opportunity_score"] = opp
    hm["last_entry_score"] = ent
    hm["last_action_status"] = action
    row["confirm_count"] = confirms
    row["action_status"] = action
    row["buy_ready"] = buy_ready
    row["trade_plan"] = suggested_trade_plan(row, profile, opp, ent) if action in {"BUY_READY", "REENTRY_READY", "ENTRY_WINDOW"} else None


def promote_and_enrich(rows: list[dict], enriched: dict, generated: str, now_ts: float,
                       live_details: dict | None = None, enrich_func=None) -> dict:
    """Promote extra markets into real same-cycle entry enrichment."""
    if enrich_func is None:
        from v3_common import enrich_market
        enrich_func = enrich_market

    history = load_v4_history()
    hm_all = history["markets"]
    existing = set(enriched)
    candidates = []
    for row in rows:
        market = row.get("market")
        if not market or market in existing:
            continue
        signal = promotion_signal(row, hm_all.get(market, {}), now_ts)
        if signal["eligible"]:
            candidates.append((signal["score"], f(row.get("quote_volume_24h_eur")), market, signal, row))

    candidates.sort(key=lambda x: (x[0], x[1]), reverse=True)

    # One global ranking let persistent-watch candidates crowd out fresh movers.
    # Reserve capacity for current movement and acceleration first; fill the
    # remainder by overall score. This changes selection only, never V4 scoring.
    selected = []
    selected_markets = set()
    def take(pool, limit):
        for item in pool:
            market = item[2]
            if market in selected_markets:
                continue
            selected.append(item)
            selected_markets.add(market)
            if sum(1 for x in selected if x in pool) >= limit:
                break

    urgent = sorted(
        [x for x in candidates if any(r in x[3]["reasons"] for r in ("LARGE_MOVER_24H", "EMERGING_MOVER_24H"))],
        key=lambda x: (f(x[4].get("change_24h_pct")), x[0], x[1]),
        reverse=True,
    )
    acceleration = sorted(
        [x for x in candidates if any(r in x[3]["reasons"] for r in
             ("RANK_SURGE", "FAST_PRICE_ACCELERATION", "M15_IMPULSE", "H1_ACCELERATION", "VOLUME_SPIKE", "VOLUME_ACCELERATION"))],
        key=lambda x: (x[0], x[1]),
        reverse=True,
    )

    for item in urgent[:URGENT_MOVER_CAP]:
        selected.append(item); selected_markets.add(item[2])
    accel_added = 0
    for item in acceleration:
        if item[2] in selected_markets:
            continue
        selected.append(item); selected_markets.add(item[2]); accel_added += 1
        if accel_added >= ACCELERATION_CAP:
            break
    for item in candidates:
        if len(selected) >= EXTRA_ENRICH_CAP:
            break
        if item[2] in selected_markets:
            continue
        selected.append(item); selected_markets.add(item[2])
    selected = selected[:EXTRA_ENRICH_CAP]
    promoted = []
    details = live_details or {}

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(enrich_func, market, details): (market, signal, row)
                   for _, _, market, signal, row in selected}
        for future in as_completed(futures):
            market, signal, row = futures[future]
            try:
                returned_market, data = future.result()
            except Exception as exc:
                data = {"error": str(exc)}
                returned_market = market
            if returned_market != market:
                data = {"error": "market_mismatch"}
            enriched[market] = data
            before = {
                "entry_score": row.get("entry_score"),
                "action_status": row.get("action_status"),
                "buy_ready": row.get("buy_ready"),
                "risk_flags": list(row.get("risk_flags") or []),
            }
            if not data.get("error"):
                hm = hm_all.setdefault(market, {})
                _apply_frozen_entry_decision(row, data, hm, now_ts)
            promoted.append({
                "market": market,
                "promotion_score": signal["score"],
                "promotion_reasons": signal["reasons"],
                "before": before,
                "after": {
                    "entry_score": row.get("entry_score"),
                    "action_status": row.get("action_status"),
                    "buy_ready": row.get("buy_ready"),
                    "risk_flags": list(row.get("risk_flags") or []),
                },
                "error": data.get("error"),
            })

    history["generated_at_utc"] = generated
    save_json(V4_HISTORY, history)
    audit = {
        "generated_at_utc": generated,
        "mode": "OPERATIONAL_SAME_CYCLE",
        "base_enriched_count": len(existing),
        "extra_cap": EXTRA_ENRICH_CAP,
        "urgent_mover_cap": URGENT_MOVER_CAP,
        "acceleration_cap": ACCELERATION_CAP,
        "candidate_count": len(candidates),
        "promoted_count": len(promoted),
        "total_enriched_count": len(enriched),
        "promoted": sorted(promoted, key=lambda x: x["promotion_score"], reverse=True),
        "note": "Selection is adaptive; scoring and V4 entry thresholds are unchanged.",
    }
    AUDIT_PATH.write_text(json.dumps(audit, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return audit


def patch_watch_output(rows: list[dict], enriched: dict, audit: dict) -> None:
    """Expose adaptive decisions to the real stabilizer/output path."""
    import v4_detector

    path = Path("v4_watch.json")
    if not path.exists():
        return
    payload = json.loads(path.read_text(encoding="utf-8"))
    status_rank = {"BUY_READY": 5, "REENTRY_READY": 5, "ENTRY_WINDOW": 4, "WATCH": 3,
                   "WATCH_RISK": 2, "TOO_LATE": 1, "NONE": 0}
    out_rows = sorted(
        [r for r in rows if f(r.get("opportunity_score")) >= 6.5 or r.get("action_status") != "NONE"],
        key=lambda r: (status_rank.get(r.get("action_status"), 0),
                       f(r.get("opportunity_score")), f(r.get("entry_score"))),
        reverse=True,
    )[:v4_detector.OUTPUT_COUNT]
    payload["watch"] = out_rows
    payload["enriched"] = {r["market"]: enriched.get(r["market"], {})
                           for r in out_rows if r.get("market") in enriched}
    payload["adaptive_entry"] = {
        "mode": audit.get("mode"),
        "promoted_count": audit.get("promoted_count"),
        "total_enriched_count": audit.get("total_enriched_count"),
        "extra_cap": audit.get("extra_cap"),
    }
    payload["method_note"] = (
        str(payload.get("method_note") or "") +
        " Operational adaptive entry rescue promotes persistent-watch, accelerating, "
        "emerging-mover and fast-rank-improvement markets into same-cycle enrichment; "
        "frozen V4 scoring and entry thresholds are unchanged."
    )
    path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
