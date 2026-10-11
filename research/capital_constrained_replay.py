"""Conservative, finite-capital research replay on explicitly supplied closed 5m candles.

This module never fetches market data, accesses a wallet or places trades.
A model fill is an explicitly hypothetical execution, NEVER a proven Bitvavo fill.

A complete PnL requires complete evidence for *all* predeclared candidate
events; missing future paths fail the whole reported portfolio, not just losers.
"""
from __future__ import annotations

from datetime import datetime, timezone, timedelta
from decimal import Decimal, InvalidOperation

BAR_SECONDS = 300
HORIZONS = (24, 48, 72, 168)


class ReplayError(ValueError):
    pass


def dec(value, label, positive=False):
    if value is None or isinstance(value, bool):
        raise ReplayError(f"{label}: finite numeric required")
    try:
        d = Decimal(str(value))
    except (TypeError, InvalidOperation, ValueError) as exc:
        raise ReplayError(f"{label}: numeric required") from exc
    if not d.is_finite() or (d <= 0 if positive else d < 0):
        raise ReplayError(f"{label}: invalid magnitude")
    return d


def utc(value, label):
    if not isinstance(value, str):
        raise ReplayError(f"{label}: UTC timestamp required")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ReplayError(f"{label}: invalid timestamp") from exc
    if dt.tzinfo is None or dt.utcoffset() != timedelta(0):
        raise ReplayError(f"{label}: explicit UTC required")
    return dt.astimezone(timezone.utc)


def number(value):
    return round(float(value), 8)


def _bar_grid(series, asof):
    """Only accept chronological *completed* candles; gaps are never padded."""
    if not isinstance(series, list):
        raise ReplayError("candle series must be list")
    candles = {}
    for item in series:
        if not isinstance(item, dict):
            raise ReplayError("5m candle must be object")
        t = utc(item.get("start_utc"), "bar.start_utc")
        if t.second or t.microsecond or t.minute % 5:
            raise ReplayError("5m bar timestamp not aligned to 5 minutes")
        if t + timedelta(seconds=BAR_SECONDS) > asof:
            raise ReplayError("partial or future candle cannot be used")
        if t in candles:
            raise ReplayError("duplicated 5m candle")
        o = dec(item.get("open"), "bar.open", positive=True)
        h = dec(item.get("high"), "bar.high", positive=True)
        l = dec(item.get("low"), "bar.low", positive=True)
        c = dec(item.get("close"), "bar.close", positive=True)
        if l > min(o, c) or h < max(o, c) or l > h:
            raise ReplayError("inconsistent OHLC")
        candles[t] = (o, h, l, c)
    return candles


def candidate_outcome(event, candles, asof, horizon_hours, fee_rate, slip_rate):
    """Independent candidate trajectory; NOT a capital allocation decision."""
    if not isinstance(event, dict) or event.get("event_type") != "MODEL_SIGNAL":
        raise ReplayError("signals must explicitly identify as MODEL_SIGNAL")
    ts = utc(event.get("decision_at_utc"), "decision")
    book = utc(event.get("book_available_at_utc"), "book availability")
    if book < ts:
        # A pre-decision book could be ex-ante, but this replay intentionally
        # uses no data before the signal and requires full provenance.
        pass
    start_after = max(ts, book)
    if start_after > asof:
        raise ReplayError("decision/book from the future")
    entry_first = datetime.fromtimestamp(
        ((int(start_after.timestamp()) // BAR_SECONDS) + 1) * BAR_SECONDS,
        timezone.utc,
    )
    expiry = start_after + timedelta(hours=horizon_hours)
    limit = dec(event.get("entry_limit_eur"), "entry_limit", positive=True)
    stop = dec(event.get("stop_eur"), "stop", positive=True)
    target = dec(event.get("target_eur"), "target", positive=True)
    budget = dec(event.get("stake_eur"), "stake", positive=True)
    if not stop < limit < target:
        raise ReplayError("invalid stop / limit / target geometry")
    if event.get("book_entry_covered") is not True or event.get("book_exit_covered") is not True:
        return {"state": "NOT_EXECUTABLE_BOOK", "reason": "MISSING_DEPTH", "event": event}
    if expiry > asof:
        return {"state": "NOT_MATURED", "reason": "HORIZON_NOT_DUE", "event": event}
    # Expiry may cut a candle; require all full five-minute intervals until
    # the first fully closed candle ending no later than expiry.
    end = datetime.fromtimestamp(int(expiry.timestamp()) // BAR_SECONDS * BAR_SECONDS,
                                 timezone.utc)
    first = candles.get(entry_first)
    if first is None:
        return {"state": "CENSORED", "reason": "ENTRY_CANDLE_MISSING", "event": event}
    open_, high, low, close = first
    # Passive limit is held one full, post-book candle only. Cautiously
    # treat the quote as a hypothetical adverse-slippage fill (not a limit fill).
    if low > limit:
        return {"state": "UNFILLED", "reason": "LIMIT_NOT_TOUCHED", "event": event}
    if open_ <= stop:
        return {"state": "UNFILLED", "reason": "INVALIDATED_AT_CANDLE_OPEN", "event": event}
    if first[2] <= stop:
        # Cannot ascertain whether stop came before/after limit entry.
        return {"state": "CENSORED", "reason": "ENTRY_STOP_INTRABAR_ORDER_UNKNOWN", "event": event}
    if first[1] >= target:
        return {"state": "CENSORED", "reason": "ENTRY_TARGET_INTRABAR_ORDER_UNKNOWN", "event": event}
    entry = limit * (1 + slip_rate)
    # At first eligible bar's end, the trade becomes open only if a possible
    # order fill existed in that bar; this is an adverse model, not a guarantee.
    first_closed = entry_first + timedelta(seconds=BAR_SECONDS)
    if first_closed > end:
        return {"state": "CENSORED", "reason": "NO_COMPLETE_EXIT_WINDOW", "event": event}
    exit_px = None
    exit_at = None
    reason = None
    t = first_closed
    while t < end:
        bar = candles.get(t)
        if bar is None:
            return {"state": "CENSORED", "reason": "FUTURE_BAR_MISSING", "event": event}
        o, h, l, c = bar
        if l <= stop:
            exit_px = min(stop, o) * (1 - slip_rate)
            exit_at = t + timedelta(seconds=BAR_SECONDS)
            reason = "STOP_FIRST_CONSERVATIVE"
            break
        if h >= target:
            exit_px = target * (1 - slip_rate)
            exit_at = t + timedelta(seconds=BAR_SECONDS)
            reason = "TARGET"
            break
        t += timedelta(seconds=BAR_SECONDS)
    if exit_px is None:
        # Last candle open at end-300s is required, including when a trade
        # held through the entire horizon.
        final_t = end - timedelta(seconds=BAR_SECONDS)
        final = candles.get(final_t)
        if final is None:
            return {"state": "CENSORED", "reason": "HORIZON_CLOSE_MISSING", "event": event}
        exit_px = final[3] * (1 - slip_rate)
        exit_at = end
        reason = "HORIZON_CLOSE"
    qty = budget / (entry * (1 + fee_rate))
    gross_buy = qty * entry
    entry_fee = gross_buy * fee_rate
    gross_sell = qty * exit_px
    exit_fee = gross_sell * fee_rate
    buy_cost = gross_buy + entry_fee
    sell_proceeds = gross_sell - exit_fee
    return {
        "state": "MODELED_COMPLETED", "event": event,
        "opened_at": first_closed, "closed_at": exit_at,
        "buy_cost": buy_cost, "sell_proceeds": sell_proceeds,
        "fees": entry_fee + exit_fee,
        "net_pnl": sell_proceeds - buy_cost,
        "exit_reason": reason,
        "modeled_entry_eur": entry, "modeled_exit_eur": exit_px,
    }


def replay_portfolio(
    events,
    bars_by_market,
    asof_utc,
    *,
    horizon_hours=24,
    initial_capital_eur=2300,
    fee_each_side=0.0025,
    slippage_each_side=0.001,
    maximum_open_positions=10,
):
    """Replay a predeclared event cohort, failing closed on all missing paths.

    Exit results are computed for validation, but the allocation scheduler
    reads only predeclared event order/size and currently available cash,
    never an outcome or signal's future maximum.
    """
    asof = utc(asof_utc, "asof")
    if isinstance(horizon_hours, bool) or horizon_hours not in HORIZONS:
        raise ReplayError("unsupported horizon; expected 24/48/72/168h")
    capital = dec(initial_capital_eur, "capital", positive=True)
    fee = dec(fee_each_side, "fee")
    slip = dec(slippage_each_side, "slip")
    if fee >= 1 or slip >= 1:
        raise ReplayError("fee/slip must be fractions less than 1")
    if isinstance(maximum_open_positions, bool) or not isinstance(maximum_open_positions, int) or maximum_open_positions < 1:
        raise ReplayError("max open positions invalid")
    if not isinstance(events, list) or not isinstance(bars_by_market, dict):
        raise ReplayError("predeclared events list and bars map required")
    grids = {m: _bar_grid(series, asof) for m, series in bars_by_market.items()}
    prepared = []
    identifiers = set()
    for e in events:
        if not isinstance(e, dict):
            raise ReplayError("event must be a dict")
        eid = e.get("event_id")
        market = e.get("market")
        if not isinstance(eid, str) or not eid or eid in identifiers:
            raise ReplayError("missing or duplicated event ID")
        identifiers.add(eid)
        if not isinstance(market, str) or not market.endswith("-EUR"):
            raise ReplayError("market not an EUR market")
        state = candidate_outcome(e, grids.get(market, {}), asof,
                                  horizon_hours, fee, slip)
        state["event_id"] = eid
        state["market"] = market
        prepared.append(state)
    # A missing or ambiguous event poisons the WHOLE portfolio score; do not
    # cherry-pick only winners with complete future candles.
    blockers = [r for r in prepared if r["state"] in ("CENSORED", "NOT_MATURED")]
    counts = {}
    for r in prepared:
        counts[r["state"]] = counts.get(r["state"], 0) + 1
    core = {
        "schema": "solaire_capital_replay_v1",
        "research_only": True,
        "modeled_fills_not_real": True,
        "capital_eur": number(capital),
        "horizon_hours": horizon_hours,
        "asof_utc": asof.isoformat(),
        "fee_rate_each_side": number(fee),
        "adverse_slippage_each_side": number(slip),
        "max_concurrent_positions": maximum_open_positions,
        "candidate_count": len(prepared),
        "candidate_states": counts,
        "missing_or_ambiguous_event_ids": [x["event_id"] for x in blockers],
        "actual_exchange_fills_verified": 0,
        "real_bitvavo_pnl_eur": None,
        "modeled_portfolio_pnl_eur": None,
        "modeled_ending_cash_eur": None,
        "max_drawdown_eur": None,
        "trade_count": None,
        "allocation_reject_count": None,
    }
    if blockers or not prepared:
        return {**core, "status": "NOT_IDENTIFIABLE_INCOMPLETE_OR_EMPTY_COHORT",
                "selection_policy": "PREDECLARED_EVENTS_NO_FUTURE_FILTER"}
    proposed = [x for x in prepared if x["state"] == "MODELED_COMPLETED"]
    # Deterministic tie break independent of future outcome. To be considered
    # for capital, entry must be feasible and have a modeled complete path.
    proposed.sort(key=lambda x: (x["opened_at"], x["event_id"]))
    active = []
    cash = capital
    realized_pnl = Decimal(0)
    all_fees = Decimal(0)
    trades = []
    allocation_rejects = 0
    for r in proposed:
        due = sorted([p for p in active if p["closed_at"] <= r["opened_at"]],
                     key=lambda p: (p["closed_at"], p["event_id"]))
        for p in due:
            cash += p["sell_proceeds"]
            realized_pnl += p["net_pnl"]
            all_fees += p["fees"]
            active.remove(p)
        if len(active) >= maximum_open_positions or r["buy_cost"] > cash:
            allocation_rejects += 1
            continue
        cash -= r["buy_cost"]
        active.append(r)
        trades.append({
            "event_id": r["event_id"], "market": r["market"],
            "modeled_opened_utc": r["opened_at"].isoformat(),
            "modeled_closed_utc": r["closed_at"].isoformat(),
            "modeled_buy_cost_eur": number(r["buy_cost"]),
            "modeled_sell_proceeds_eur": number(r["sell_proceeds"]),
            "modeled_net_pnl_eur": number(r["net_pnl"]),
            "modeled_fees_eur": number(r["fees"]),
            "exit_reason": r["exit_reason"],
        })
    for p in sorted(active, key=lambda x: (x["closed_at"], x["event_id"])):
        cash += p["sell_proceeds"]
        realized_pnl += p["net_pnl"]
        all_fees += p["fees"]
    if abs(cash - capital - realized_pnl) > Decimal("0.000001"):
        raise ReplayError("cash/pnl reconciliation failed")
    return {
        **core,
        "status": "MODELED_CLOSED_COHORT_ONLY_NO_EXECUTION_PROOF",
        "selection_policy": "PREDECLARED_EVENTS_CHRONOLOGICAL_NO_FUTURE_FILTER",
        "modeled_portfolio_pnl_eur": number(realized_pnl),
        "modeled_ending_cash_eur": number(cash),
        "modeled_total_fees_eur": number(all_fees),
        "modeled_return_pct": number((cash / capital - 1) * 100),
        "max_drawdown_eur": None,
        "trade_count": len(trades),
        "allocation_reject_count": allocation_rejects,
        "trades": trades,
        "drawdown_note": "No synchronized 5-minute mark-to-market for every open holding; drawdown remains NULL.",
    }
