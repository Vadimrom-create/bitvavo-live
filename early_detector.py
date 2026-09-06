#!/usr/bin/env python3
"""Bitvavo Ignition Detector V3 orchestrator."""
from __future__ import annotations

import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

from v3_common import (
    EARLY_JSON, EARLY_TXT, ENRICH_COUNT, HISTORY, LIVE, SCAN, SIGNAL_LOG,
    SIGNAL_LOG_RETENTION_SEC, WATCH_COUNT, btc_risk, enrich_market, f,
    load_history, maybe, pct, thin_samples, trajectory,
)
from v3_scoring import burst_score, continuation_score, finalize_row, select_pre_enrichment, slow_score


def load_signal_log():
    try:
        data = json.loads(SIGNAL_LOG.read_text(encoding="utf-8")) if SIGNAL_LOG.exists() else {}
    except Exception:
        data = {}
    if not isinstance(data, dict):
        data = {}
    data.setdefault("version", 1)
    data.setdefault("events", [])
    return data


def update_signal_log(log, rows_by_market, now_ts, generated):
    events = [e for e in log.get("events", []) if f(e.get("created_ts")) >= now_ts - SIGNAL_LOG_RETENTION_SEC]
    for event in events:
        row = rows_by_market.get(event.get("market"))
        if not row:
            continue
        last, first = f(row.get("last")), f(event.get("first_price"))
        event["last_seen_utc"], event["last_price"] = generated, last
        event["pct_now"] = round(pct(last, first) or 0.0, 4) if first else None
        event["max_price"] = max(f(event.get("max_price"), last), last)
        old_min = maybe(event.get("min_price"))
        event["min_price"] = min(old_min if old_min is not None else last, last)
        event["mfe_pct"] = round(pct(f(event["max_price"]), first) or 0.0, 4) if first else None
        event["mae_pct"] = round(pct(f(event["min_price"]), first) or 0.0, 4) if first else None
        elapsed = now_ts - f(event.get("created_ts"))
        checkpoints = event.setdefault("checkpoints", {})
        for label, seconds in (("30m",1800),("60m",3600),("3h",10800),("6h",21600),("12h",43200)):
            if first and elapsed >= seconds and label not in checkpoints:
                checkpoints[label] = {"ts_utc": generated, "price": last, "pct": round(pct(last, first) or 0.0, 4)}
        if elapsed >= 12 * 3600:
            event["status"] = "CLOSED"

    active = {e["market"]: e for e in events if e.get("status") == "ACTIVE"}
    for market, row in rows_by_market.items():
        if f(row.get("final_score")) < 7.5 or row.get("early_stage") in {"REJECTED", "TOO_LATE"}:
            continue
        if market in active and now_ts - f(active[market].get("created_ts")) < 12 * 3600:
            continue
        last = f(row.get("last"))
        event = {
            "market": market, "mode": row.get("signal_mode"), "created_ts": now_ts,
            "first_seen_utc": generated, "first_price": last, "first_score": row.get("final_score"),
            "first_stage": row.get("early_stage"), "last_seen_utc": generated, "last_price": last,
            "max_price": last, "min_price": last, "pct_now": 0.0, "mfe_pct": 0.0, "mae_pct": 0.0,
            "status": "ACTIVE", "checkpoints": {},
        }
        events.append(event)
        active[market] = event
    log["generated_at_utc"], log["events"] = generated, events
    return log


def fmt(value, digits=2):
    if value is None:
        return "n/a"
    try:
        return f"{float(value):.{digits}f}"
    except Exception:
        return str(value)


def tf(summary):
    summary = summary or {}
    return (
        f"ch1={fmt(summary.get('ch1'))},ch4={fmt(summary.get('ch4'))},ch16={fmt(summary.get('ch16'))},"
        f"vr1={fmt(summary.get('vr1'))},vr4={fmt(summary.get('vr4'))},wick={fmt(summary.get('wick'))}"
    )


def main():
    live = json.loads(LIVE.read_text(encoding="utf-8"))
    rows = live.get("markets", [])
    generated = live.get("generated_at_utc") or datetime.utcnow().isoformat() + "+00:00"
    try:
        now_ts = datetime.fromisoformat(generated.replace("Z", "+00:00")).timestamp()
    except Exception:
        now_ts = time.time()

    history = load_history()
    markets_history = history["markets"]
    for rank, row in enumerate(rows, 1):
        hm = markets_history.setdefault(row["market"], {})
        t = trajectory(row, rank, hm, now_ts)
        row["current_rank"], row["trajectory"] = rank, t
        row["scores"] = {
            "burst": burst_score(row, t),
            "slow": slow_score(row, t),
            "continuation": continuation_score(row, t, hm),
        }

    selected = select_pre_enrichment(rows, markets_history, now_ts, ENRICH_COUNT)
    enriched, live_details = {}, live.get("details") or {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(enrich_market, row["market"], live_details) for row in selected]
        for future in as_completed(futures):
            market, data = future.result()
            enriched[market] = data

    market_risk = btc_risk(live)
    selected_by_name = {row["market"]: row for row in selected}
    for market, row in selected_by_name.items():
        finalize_row(row, enriched.get(market, {}), markets_history.setdefault(market, {}), now_ts, generated, market_risk)

    for row in rows:
        if "final_score" in row:
            continue
        scores = row["scores"]
        mode = max(scores, key=scores.get)
        score = scores[mode]
        row.update({
            "signal_mode": mode.upper(), "setup_score": score, "final_score": score, "early_score": score,
            "early_stage": "WATCH" if score >= 5 else "NONE", "risk_flags": ["NOT_ENRICHED"],
            "buy_ready": False, "confirm_count": int(f(markets_history.get(row["market"], {}).get("confirm_count"))),
        })

    active_markets = set()
    for row in rows:
        market = row["market"]
        active_markets.add(market)
        hm = markets_history.setdefault(market, {})
        m15 = row.get("m15") or {}
        sample = [now_ts, row.get("current_rank"), row.get("collector_priority"), row.get("last"), row.get("change_24h_pct"), m15.get("volume_last_vs_prev20"), m15.get("volume_4_vs_prev4"), row.get("final_score")]
        hm["samples"] = thin_samples(hm.get("samples", []) + [sample], now_ts)
    for market in list(markets_history):
        hm = markets_history[market]
        hm["samples"] = thin_samples(hm.get("samples", []), now_ts)
        if market not in active_markets and not hm["samples"] and f(hm.get("watch_until_ts")) < now_ts:
            markets_history.pop(market, None)
    history["generated_at_utc"] = generated
    HISTORY.write_text(json.dumps(history, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    rows_by_market = {row["market"]: row for row in rows}
    signal_log = update_signal_log(load_signal_log(), rows_by_market, now_ts, generated)
    SIGNAL_LOG.write_text(json.dumps(signal_log, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    ranked = sorted(selected, key=lambda row: (bool(row.get("buy_ready")), f(row.get("final_score")), f(row.get("setup_score"))), reverse=True)
    audit_candidates = [row for row in rows if f(row.get("quote_volume_24h_eur")) >= 75_000 and f(row.get("spread_pct"), 99) <= 0.30]
    gainers_audit = []
    for row in sorted(audit_candidates, key=lambda r: f(r.get("change_24h_pct")), reverse=True)[:15]:
        hm = markets_history.get(row["market"], {})
        first_price = maybe(hm.get("first_signal_price"))
        gainers_audit.append({
            "market": row["market"], "change_24h_pct": row.get("change_24h_pct"), "last": row.get("last"),
            "final_score": row.get("final_score"), "signal_mode": row.get("signal_mode"),
            "first_signal_seen": hm.get("first_signal_seen"),
            "gain_since_first_signal_pct": round(pct(f(row.get("last")), first_price), 4) if first_price else None,
        })

    lines = [
        "BITVAVO IGNITION WATCH V3", f"generated_at_utc: {generated}", f"btc_risk: {market_risk}",
        "NOTE: V3 sépare BURST / SLOW / CONTINUATION, garde une watchlist 12h et mesure les performances.",
        "rank | market | final | mode | stage | BUY | confirms | raw[b,s,c] | current_rank | dscore15 | drank15 | price15% | price60% | price240% | since_first% | ch24% | vol24EUR | spread% | bid_share | flags | 5m | 15m | 1h | 4h | first_seen",
    ]
    for index, row in enumerate(ranked[:WATCH_COUNT], 1):
        t, e, scores = row.get("trajectory") or {}, enriched.get(row["market"], {}), row.get("scores") or {}
        book = e.get("book", {}) if isinstance(e, dict) else {}
        lines.append(
            f"{index} | {row['market']} | {fmt(row.get('final_score'),3)} | {row.get('signal_mode')} | {row.get('early_stage')} | {str(bool(row.get('buy_ready'))).upper()} | {row.get('confirm_count')} | "
            f"[{fmt(scores.get('burst'))},{fmt(scores.get('slow'))},{fmt(scores.get('continuation'))}] | {row.get('current_rank')} | {fmt(t.get('dscore_15m'))} | {fmt(t.get('drank_15m'),0)} | {fmt(t.get('dprice_15m_pct'))} | {fmt(t.get('dprice_60m_pct'))} | {fmt(t.get('dprice_240m_pct'))} | {fmt(t.get('price_since_first_early_pct'))} | "
            f"{fmt(row.get('change_24h_pct'))} | {fmt(row.get('quote_volume_24h_eur'),0)} | {fmt(row.get('spread_pct'),4)} | {fmt(book.get('bid_share'),3)} | {','.join(row.get('risk_flags') or []) or '-'} | "
            f"5m[{tf(e.get('5m'))}] | 15m[{tf(e.get('15m'))}] | 1h[{tf(e.get('1h'))}] | 4h[{tf(e.get('4h'))}] | {t.get('first_early_seen') or 'n/a'}"
        )
    lines += ["", "TOP_GAINERS_AUDIT"]
    for item in gainers_audit:
        lines.append(
            f"{item['market']} | ch24={fmt(item['change_24h_pct'])}% | score={fmt(item['final_score'])} | mode={item['signal_mode']} | "
            f"first={item['first_signal_seen'] or 'n/a'} | gain_since_first={fmt(item['gain_since_first_signal_pct'])}%"
        )

    EARLY_TXT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    payload = {
        "generated_at_utc": generated, "version": 3,
        "method_note": "V3: BURST + SLOW + CONTINUATION; historique aminci 24h; watchlist persistante 12h; mèches pénalisées, rejet HEI seulement si confirmé; buy_ready exige deux confirmations.",
        "btc_risk": market_risk, "watch": ranked[:WATCH_COUNT],
        "enriched": {m: enriched.get(m, {}) for m in [r["market"] for r in ranked[:WATCH_COUNT]]},
        "gainers_audit": gainers_audit,
    }
    EARLY_JSON.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    base_scan = SCAN.read_text(encoding="utf-8") if SCAN.exists() else ""
    SCAN.write_text("\n".join(lines[:min(len(lines), 22)]) + "\n\n--- CURRENT_STRENGTH SNAPSHOT ---\n" + base_scan, encoding="utf-8")
    ready = [r["market"] for r in ranked if r.get("buy_ready")]
    print(f"IGNITION V3: {len(rows)} marchés, {len(selected)} enrichis, buy_ready={ready or 'none'}, history=24h")


if __name__ == "__main__":
    main()
