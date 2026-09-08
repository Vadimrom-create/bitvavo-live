from __future__ import annotations

from datetime import datetime, timezone

from v3_common import (
    BUY_READY_THRESHOLD,
    IGNITION_THRESHOLD,
    SESSION_RESET_SEC,
    SIGNAL_THRESHOLD,
    WATCH_PERSIST_SEC,
    clamp,
    f,
    maybe,
    pct,
)

BURST_POOL = 18
SLOW_POOL = 18
CONT_POOL = 14
STRENGTH_POOL = 10
ACTIVE_POOL = 15


def liquidity_component(row):
    vol = f(row.get("quote_volume_24h_eur"))
    spread = f(row.get("spread_pct"), 99)
    x = 0.0
    if vol >= 1_000_000:
        x += 0.85
    elif vol >= 250_000:
        x += 0.65
    elif vol >= 75_000:
        x += 0.40
    elif vol >= 25_000:
        x += 0.10
    elif vol < 10_000:
        x -= 1.20
    else:
        x -= 0.45

    if spread <= 0.05:
        x += 0.60
    elif spread <= 0.12:
        x += 0.45
    elif spread <= 0.20:
        x += 0.20
    elif spread > 0.80:
        x -= 1.80
    elif spread > 0.40:
        x -= 1.00
    elif spread > 0.25:
        x -= 0.45
    return x


def burst_score(row, t):
    s = row.get("m15") or {}
    vr1 = max(0.0, f(s.get("volume_last_vs_prev20")))
    vr4 = max(0.0, f(s.get("volume_4_vs_prev4")))
    ch1h = f(s.get("change_4_candles_pct"))
    ch4h = f(s.get("change_16_candles_pct"))
    ch24 = f(row.get("change_24h_pct"))
    wick = f(s.get("max_upper_wick_ratio_8bar"))
    dist = f(s.get("distance_from_8bar_high_pct"), -99)

    x = 1.25 + liquidity_component(row)
    x += min(max(vr1 - 1.0, 0.0), 10.0) * 0.18
    x += min(max(vr4 - 1.0, 0.0), 8.0) * 0.36

    d15, d30 = t.get("dscore_15m"), t.get("dscore_30m")
    r15, r30 = t.get("drank_15m"), t.get("drank_30m")
    if d15 is not None:
        x += min(max(d15, 0.0), 6.0) * 0.42
    if d30 is not None:
        x += min(max(d30, 0.0), 7.0) * 0.16
    if r15 is not None:
        x += min(max(r15, 0.0), 160.0) / 160.0 * 1.05
    if r30 is not None:
        x += min(max(r30, 0.0), 240.0) / 240.0 * 0.55

    dp15 = t.get("dprice_15m_pct")
    if dp15 is not None:
        if -0.35 <= dp15 <= 1.80:
            x += 0.65
        elif 1.80 < dp15 <= 3.50:
            x += 0.20
        elif dp15 > 5.0:
            x -= 1.10
        elif dp15 < -1.5:
            x -= 0.65

    if 0.10 <= ch1h <= 4.0:
        x += 0.50
    elif ch1h > 7.0:
        x -= 0.90
    if -1.0 <= ch4h <= 7.0:
        x += 0.35
    elif ch4h > 12.0:
        x -= 1.00
    if -3.0 <= ch24 <= 7.0:
        x += 0.45
    elif ch24 > 15.0:
        x -= 1.30
    if dist >= -1.2:
        x += 0.30

    # mèche ≠ rejet automatique
    if wick >= 0.90 and (ch1h < 0 or dist < -1.5):
        x -= 1.15
    elif wick >= 0.80:
        x -= 0.35
    return round(clamp(x), 3)


def slow_score(row, t):
    s = row.get("m15") or {}
    ch1h = f(s.get("change_4_candles_pct"))
    ch4h = f(s.get("change_16_candles_pct"))
    vr4 = f(s.get("volume_4_vs_prev4"))
    ch24 = f(row.get("change_24h_pct"))
    x = 1.35 + liquidity_component(row)

    for m, lo, hi, weight in ((60, 0.20, 3.5, 0.70), (120, 0.45, 6.0, 0.85), (240, 0.80, 10.0, 1.00)):
        dp = t.get(f"dprice_{m}m_pct")
        if dp is not None:
            if lo <= dp <= hi:
                x += weight
            elif -0.5 <= dp < lo:
                x += 0.15
            elif dp > hi * 1.5:
                x -= 0.45
        dr = t.get(f"drank_{m}m")
        if dr is not None and dr > 0:
            x += min(dr, 180.0) / 180.0 * (0.35 + m / 480.0)
        ds = t.get(f"dscore_{m}m")
        if ds is not None and ds > 0:
            x += min(ds, 5.0) * (0.10 if m == 60 else 0.08)

    positives = sum(
        1
        for m in (30, 60, 120, 240)
        if t.get(f"dprice_{m}m_pct") is not None and f(t.get(f"dprice_{m}m_pct")) > 0.15
    )
    if positives >= 3:
        x += 0.80
    elif positives >= 2:
        x += 0.45

    if 0.20 <= ch1h <= 4.5:
        x += 0.55
    if 0.50 <= ch4h <= 10.0:
        x += 0.55
    if 1.05 <= vr4 <= 8.0:
        x += 0.45
    elif vr4 > 15.0:
        x += 0.10

    dp15 = t.get("dprice_15m_pct")
    if dp15 is not None and dp15 < -1.2:
        x -= 0.70
    if ch24 > 18.0:
        x -= 1.70
    elif ch24 > 12.0:
        x -= 0.70
    return round(clamp(x), 3)


def continuation_score(row, t, hm):
    first_price = maybe(hm.get("first_signal_price"))
    first_ts = f(hm.get("first_signal_ts"))
    last = f(row.get("last"))
    ch24 = f(row.get("change_24h_pct"))
    peak = maybe(hm.get("peak_since_signal"))

    if not (bool(first_price and first_ts) or 4.0 <= ch24 <= 18.0):
        return 0.0

    x = 1.10 + liquidity_component(row)
    since = pct(last, first_price) if first_price else None
    if since is not None:
        if 2.0 <= since <= 10.0:
            x += 1.55
        elif 0.0 <= since < 2.0:
            x += 0.65
        elif 10.0 < since <= 15.0:
            x += 0.45
        elif since > 18.0:
            x -= 1.50

    dp15, dp30 = t.get("dprice_15m_pct"), t.get("dprice_30m_pct")
    if dp15 is not None and 0.10 <= dp15 <= 2.5:
        x += 1.05
    if dp30 is not None and 0.20 <= dp30 <= 4.0:
        x += 0.75

    if peak and peak > 0:
        drawdown = pct(last, peak)
        if -5.5 <= drawdown <= -0.6:
            x += 0.95
        elif drawdown > -0.6 and dp15 is not None and dp15 > 0.2:
            x += 0.50

    s = row.get("m15") or {}
    vr4 = f(s.get("volume_4_vs_prev4"))
    ch1h = f(s.get("change_4_candles_pct"))
    if vr4 >= 1.2:
        x += min(vr4, 6.0) * 0.16
    if 0.2 <= ch1h <= 5.0:
        x += 0.55
    r30 = t.get("drank_30m")
    if r30 is not None and r30 > 0:
        x += min(r30, 150.0) / 150.0 * 0.65
    if ch24 > 20:
        x -= 1.2
    return round(clamp(x), 3)


def select_pre_enrichment(rows, hm_all, now_ts, cap=50):
    burst = sorted(rows, key=lambda r: r["scores"]["burst"], reverse=True)[:BURST_POOL]
    slow = sorted(rows, key=lambda r: r["scores"]["slow"], reverse=True)[:SLOW_POOL]
    cont = sorted(rows, key=lambda r: r["scores"]["continuation"], reverse=True)[:CONT_POOL]
    active_names = {m for m, hm in hm_all.items() if f(hm.get("watch_until_ts")) > now_ts}
    active = [r for r in rows if r["market"] in active_names]
    active.sort(key=lambda r: f(hm_all.get(r["market"], {}).get("last_final_score")), reverse=True)
    strength = sorted(rows, key=lambda r: f(r.get("collector_priority")), reverse=True)[:STRENGTH_POOL]
    refs = [r for r in rows if r.get("market") in {"NIL-EUR", "HEI-EUR", "HUMA-EUR", "BTC-EUR"}]
    groups = [burst, slow, cont, active[:ACTIVE_POOL], strength, refs]

    names, selected = set(), []
    max_len = max((len(g) for g in groups), default=0)
    for i in range(max_len):
        for group in groups:
            if i >= len(group):
                continue
            row = group[i]
            if row["market"] in names:
                continue
            names.add(row["market"])
            selected.append(row)
            if len(selected) >= cap:
                return selected
    return selected


def quality_adjustment(row, e):
    flags, hard = [], []
    adj = 0.0
    spread = f(row.get("spread_pct"), 99)
    vol = f(row.get("quote_volume_24h_eur"))
    ch24 = f(row.get("change_24h_pct"))

    if vol < 10_000:
        hard.append("ILLIQUID")
    elif vol < 50_000:
        flags.append("LOW_LIQUIDITY")
        adj -= 0.55
    if spread > 0.80:
        hard.append("WIDE_SPREAD")
    elif spread > 0.30:
        flags.append("SPREAD")
        adj -= 0.55

    book = e.get("book") or {}
    bid = maybe(book.get("bid_share"))
    if bid is not None:
        if bid >= 0.55:
            adj += 0.45
        elif bid >= 0.45:
            adj += 0.25
        elif bid < 0.20:
            flags.append("VERY_SELLER_HEAVY_BOOK")
            adj -= 0.95
        elif bid < 0.30:
            flags.append("SELLER_HEAVY_BOOK")
            adj -= 0.50
    else:
        flags.append("NO_BOOK")

    s5, s15, s1h, s4h = (e.get("5m") or {}, e.get("15m") or {}, e.get("1h") or {}, e.get("4h") or {})
    w5, w15 = f(s5.get("wick")), f(s15.get("wick"))
    d5, d15 = f(s5.get("dist8high"), -99), f(s15.get("dist8high"), -99)
    c5, c15 = f(s5.get("ch1")), f(s15.get("ch1"))
    max_wick = max(w5, w15)

    # HEI uniquement si grosse mèche + vrai rejet du sommet.
    true_rejection = max_wick >= 0.88 and ((d5 < -1.5 and c5 < -0.15) or (d15 < -1.8 and c15 < -0.20))
    if true_rejection:
        hard.append("HEI_REJECTION")
        adj -= 1.50
    elif max_wick >= 0.82:
        flags.append("WICK_SETUP")
        adj -= 0.15

    for label, summary, weight in (("5m", s5, 0.35), ("15m", s15, 0.40), ("1h", s1h, 0.35), ("4h", s4h, 0.25)):
        ch4 = maybe(summary.get("ch4"))
        if ch4 is None:
            continue
        if 0.1 <= ch4 <= (3.0 if label in {"5m", "15m"} else 8.0):
            adj += weight
        elif ch4 < -3.0:
            adj -= weight

    if ch24 > 25.0:
        hard.append("TOO_LATE_24H")
    elif ch24 > 15.0:
        flags.append("EXTENDED_24H")
        adj -= 0.90

    vr5, vr15 = maybe(s5.get("vr4")), maybe(s15.get("vr4"))
    if vr5 is not None and 1.2 <= vr5 <= 15:
        adj += 0.30
    if vr15 is not None and 1.1 <= vr15 <= 12:
        adj += 0.30
    return adj, flags, hard


def finalize_row(row, e, hm, now_ts, generated, global_btc_risk):
    scores = row["scores"]
    mode = max(scores, key=scores.get)
    base = scores[mode]
    adj, flags, hard = quality_adjustment(row, e)
    final = round(clamp(base + adj), 3)

    last = f(row.get("last"))
    first_price = maybe(hm.get("first_signal_price"))
    first_ts = f(hm.get("first_signal_ts"))
    since_first = pct(last, first_price) if first_price else None

    if global_btc_risk:
        flags.append("BTC_RISK")
        final = round(max(0.0, final - 0.45), 3)
    if since_first is not None and since_first > 16:
        hard.append("TOO_LATE_FROM_SIGNAL")

    if hard:
        stage = "TOO_LATE" if any(x.startswith("TOO_LATE") for x in hard) else "REJECTED"
    elif final >= IGNITION_THRESHOLD:
        stage = "SECOND_IGNITION" if mode == "continuation" else "IGNITION"
    elif final >= 6.50:
        stage = "PRE_IGNITION"
    elif final >= 5.0:
        stage = "WATCH"
    else:
        stage = "NONE"

    if final >= SIGNAL_THRESHOLD and stage not in {"REJECTED", "TOO_LATE"}:
        hm["watch_until_ts"] = max(f(hm.get("watch_until_ts")), now_ts + WATCH_PERSIST_SEC)
        if not first_price or not first_ts or now_ts - first_ts > SESSION_RESET_SEC:
            hm.update(
                {
                    "first_signal_ts": now_ts,
                    "first_signal_seen": generated,
                    "first_signal_price": last,
                    "first_signal_mode": mode,
                    "peak_since_signal": last,
                    "trough_since_signal": last,
                }
            )
            first_price, first_ts, since_first = last, now_ts, 0.0
        hm["peak_since_signal"] = max(f(hm.get("peak_since_signal"), last), last)
        trough = maybe(hm.get("trough_since_signal"))
        hm["trough_since_signal"] = min(trough if trough is not None else last, last)
    elif f(hm.get("watch_until_ts")) < now_ts and first_ts and now_ts - first_ts > SESSION_RESET_SEC:
        for key in ("first_signal_ts", "first_signal_seen", "first_signal_price", "first_signal_mode", "peak_since_signal", "trough_since_signal"):
            hm.pop(key, None)
        since_first = None

    previous_final = f(hm.get("last_final_score"))
    previous_confirm = int(f(hm.get("confirm_count")))
    if final >= 7.5 and stage in {"IGNITION", "SECOND_IGNITION", "PRE_IGNITION"}:
        confirm = previous_confirm + 1 if previous_final >= 7.0 else 1
    else:
        confirm = 0
    hm["confirm_count"] = min(confirm, 12)
    hm["last_final_score"] = final
    hm["last_mode"] = mode
    hm["last_stage"] = stage
    hm["last_seen_ts"] = now_ts

    book = e.get("book") or {}
    bid_share = maybe(book.get("bid_share"))
    spread = f(row.get("spread_pct"), 99)
    vol = f(row.get("quote_volume_24h_eur"))
    ch24 = f(row.get("change_24h_pct"))
    s5, s15 = e.get("5m") or {}, e.get("15m") or {}

    buy_ready = (
        final >= BUY_READY_THRESHOLD
        and stage in {"IGNITION", "SECOND_IGNITION"}
        and hm["confirm_count"] >= 2
        and vol >= 100_000
        and spread <= 0.18
        and (bid_share is None or bid_share >= 0.33)
        and ch24 <= 15.0
        and (since_first is None or since_first <= 8.0)
        and f(s5.get("ch4"), -99) > -1.0
        and f(s15.get("ch4"), -99) > -1.5
        and not global_btc_risk
        and not hard
    )

    row.update(
        {
            "signal_mode": mode.upper(),
            "setup_score": base,
            "final_score": final,
            "early_score": final,
            "early_stage": stage,
            "risk_flags": sorted(set(flags + hard)),
            "buy_ready": bool(buy_ready),
            "confirm_count": hm["confirm_count"],
        }
    )
    t = row.get("trajectory") or {}
    t["first_early_seen"] = hm.get("first_signal_seen")
    t["first_early_price"] = hm.get("first_signal_price")
    t["price_since_first_early_pct"] = round(since_first, 4) if since_first is not None else None
    t["watch_until_utc"] = datetime.fromtimestamp(f(hm.get("watch_until_ts")), timezone.utc).isoformat() if f(hm.get("watch_until_ts")) > now_ts else None
    row["trajectory"] = t
    return row
