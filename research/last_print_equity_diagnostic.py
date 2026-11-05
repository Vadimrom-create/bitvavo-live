"""Read-only, last-traded-price portfolio equity diagnostics for explicit MODEL trades.

Cannot measure executable liquidation value or certified maximum drawdown.
Any incomplete as-of mark invalidates the whole modeled drawdown result.
"""
from __future__ import annotations
import bisect
from datetime import timedelta
from decimal import Decimal

from research.capital_constrained_replay import dec, utc, ReplayError


def summarize_last_print_equity(
    trades, plans_by_event_id, markets, asof_utc, *,
    initial_capital_eur=2300,
    fee_each_side=0.0025,
    slippage_each_side=0.001,
    maximum_price_staleness_minutes=720,
):
    if not isinstance(trades, list) or not isinstance(plans_by_event_id, dict):
        raise ReplayError("trades must be list and plans must be keyed mapping")
    if not isinstance(markets, dict):
        raise ReplayError("market candles must be mapping")
    asof = utc(asof_utc, "asof")
    start_capital = dec(initial_capital_eur, "capital", positive=True)
    fee = dec(fee_each_side, "fee")
    slip = dec(slippage_each_side, "slippage")
    if not isinstance(maximum_price_staleness_minutes, int) or maximum_price_staleness_minutes < 0:
        raise ReplayError("invalid price staleness")
    if fee >= 1 or slip >= 1:
        raise ReplayError("invalid fee or slippage")
    times = {}
    for market, raw in markets.items():
        if not isinstance(raw, list):
            raise ReplayError("invalid candle bundle")
        series = []
        for candle in raw:
            open_ts = utc(candle.get("start_utc"), "candle time")
            t = open_ts + timedelta(minutes=5)
            if t > asof:
                raise ReplayError("future / partial mark candle")
            close = dec(candle.get("close"), "candle close", positive=True)
            series.append((t, close))
        series.sort(key=lambda x: x[0])
        if len(series) != len({t for t, _ in series}):
            raise ReplayError("duplicated candle timestamp")
        times[market] = ([t for t, _ in series], [p for _, p in series])
    raw_moves = []
    modeled_net_total = Decimal(0)
    ids = set()
    for trade in trades:
        eid = trade.get("event_id")
        if not isinstance(eid, str) or not eid or eid in ids:
            raise ReplayError("duplicate or missing trade event id")
        ids.add(eid)
        plan = plans_by_event_id.get(eid)
        if not isinstance(plan, dict):
            raise ReplayError("trade missing original event plan")
        market = trade.get("market")
        if market != plan.get("market") or market not in times:
            raise ReplayError("trade/plan market mismatch")
        opened = utc(trade.get("modeled_opened_utc"), "trade open")
        closed = utc(trade.get("modeled_closed_utc"), "trade close")
        if not opened < closed <= asof:
            raise ReplayError("invalid model trade time")
        if any(t.second or t.microsecond or t.minute % 5 for t in (opened, closed)):
            raise ReplayError("trade event not on completed 5-minute clock")
        buy_cost = dec(trade.get("modeled_buy_cost_eur"), "buy cost", positive=True)
        proceeds = dec(trade.get("modeled_sell_proceeds_eur"), "sell proceeds")
        expected_net = Decimal(str(trade.get("modeled_net_pnl_eur")))
        if not expected_net.is_finite() or abs(expected_net - (proceeds - buy_cost)) > Decimal("0.00001"):
            raise ReplayError("trade model PnL does not reconcile with cost/proceeds")
        modeled_net_total += proceeds - buy_cost
        limit = dec(plan.get("entry_limit_eur"), "proposed entry", positive=True)
        modeled_entry = limit * (1 + slip)
        quantity = buy_cost / (modeled_entry * (1 + fee))
        if quantity <= 0:
            raise ReplayError("impossible marked quantity")
        raw_moves.extend([
            (opened, 1, eid, market, buy_cost, quantity),
            (closed, 0, eid, market, proceeds, quantity),
        ])
    if not raw_moves:
        return {
            "schema": "solaire_last_print_equity_diagnostic_v1",
            "status": "NOT_IDENTIFIABLE_NO_MODELED_TRADES",
            "max_drawdown_last_print_eur_est": None,
            "average_deployed_cash_eur_est": None,
            "real_executable_drawdown_eur": None,
            "note": "Empty simulated cohort is not a zero-risk historical outcome.",
        }
    # Settle sells then consider buys at exactly the same modeled timestamp.
    raw_moves.sort(key=lambda x: (x[0], x[1], x[2]))
    first_ts = raw_moves[0][0]
    last_ts = raw_moves[-1][0]
    instant = first_ts
    cash = start_capital
    open_positions = {}
    cursor = 0
    peak = start_capital
    max_drawdown = Decimal(0)
    min_equity = start_capital
    max_equity = start_capital
    max_deployed = Decimal(0)
    sum_deployed = Decimal(0)
    step_count = 0
    examples = []
    while instant <= last_ts:
        while cursor < len(raw_moves) and raw_moves[cursor][0] <= instant:
            _, action, eid, market, euro, qty = raw_moves[cursor]
            if action == 1:
                if eid in open_positions or euro > cash:
                    raise ReplayError("duplicate entry or cash overdraw")
                cash -= euro
                open_positions[eid] = (market, qty, euro)
            else:
                if eid not in open_positions:
                    raise ReplayError("closed nonexistent model position")
                cash += euro
                del open_positions[eid]
            cursor += 1
        deployed = sum((row[2] for row in open_positions.values()), Decimal(0))
        max_deployed = max(max_deployed, deployed)
        sum_deployed += deployed
        equity = cash
        for eid, (market, qty, original_cost) in open_positions.items():
            timestamps, prices = times[market]
            idx = bisect.bisect_right(timestamps, instant) - 1
            if idx < 0 or instant - timestamps[idx] > timedelta(minutes=maximum_price_staleness_minutes):
                examples.append({"event_id": eid, "market": market, "at_utc": instant.isoformat()})
                break
            equity += qty * prices[idx]
        if examples:
            break
        peak = max(peak, equity)
        min_equity = min(min_equity, equity)
        max_equity = max(max_equity, equity)
        max_drawdown = max(max_drawdown, peak - equity)
        step_count += 1
        instant += timedelta(minutes=5)
    if examples:
        return {
            "schema": "solaire_last_print_equity_diagnostic_v1",
            "status": "NOT_IDENTIFIABLE_MISSING_OR_STALE_MARK",
            "missing_mark_examples": examples[:10],
            "max_drawdown_last_print_eur_est": None,
            "average_deployed_cash_eur_est": None,
            "real_executable_drawdown_eur": None,
        }
    if open_positions or cursor != len(raw_moves):
        raise ReplayError("nonzero open positions after last modeled exit")
    if step_count == 0:
        raise ReplayError("unexpected empty mark clock")
    if abs(cash - start_capital - modeled_net_total) > Decimal("0.0002"):
        raise ReplayError("post-trade equity/cash/PnL reconciliation failed")
    return {
        "schema": "solaire_last_print_equity_diagnostic_v1",
        "status": "LAST_TRADED_PRICE_PROXY_ONLY",
        "mark_count": step_count,
        "first_mark_at_utc": first_ts.isoformat(),
        "last_mark_at_utc": last_ts.isoformat(),
        "initial_capital_eur": float(start_capital),
        "last_print_min_equity_eur_est": round(float(min_equity), 6),
        "last_print_max_equity_eur_est": round(float(max_equity), 6),
        "max_drawdown_last_print_eur_est": round(float(max_drawdown), 6),
        "max_deployed_cash_eur_est": round(float(max_deployed), 6),
        "average_deployed_cash_eur_est": round(float(sum_deployed / step_count), 6),
        "average_deployed_cash_pct_of_capital_est": round(float(sum_deployed / step_count / start_capital * 100), 6),
        "model_final_cash_eur": round(float(cash), 6),
        "real_executable_drawdown_eur": None,
        "exit_liquidation_price_confirmed": False,
        "note": "Marks use latest published traded close, not bid/book liquidation or guaranteed fills. Drawdown is indicative and may materially understate executable loss.",
    }
