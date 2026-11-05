"""Deterministic, isolated cash accounting for *explicitly supplied* fills.

Public machine BUY_SENT alerts are NOT fills. This module never contacts an
exchange. An operator-attested record is not independently verified.
"""
from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation


class LedgerError(ValueError):
    pass


def amount(value, name, positive=False):
    if isinstance(value, bool) or value is None:
        raise LedgerError(f"{name}: numeric value required")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise LedgerError(f"{name}: numeric value required") from exc
    if not result.is_finite() or (result <= 0 if positive else result < 0):
        raise LedgerError(f"{name}: invalid value")
    return result


def utc_time(value, name):
    if not isinstance(value, str):
        raise LedgerError(f"{name}: ISO timestamp required")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise LedgerError(f"{name}: invalid timestamp") from exc
    if dt.tzinfo is None or dt.utcoffset() != __import__("datetime").timedelta(0):
        raise LedgerError(f"{name}: explicit UTC required")
    return dt.astimezone(timezone.utc)


def as_num(value):
    return round(float(value), 8)


def calculate_cash_ledger(fills, marks, asof_utc, initial_capital_eur=2300, max_mark_age_seconds=900):
    """Returns cash and realised PnL; equity only when every open holding has a fresh mark.

    Fill records MUST be distinct from a signal, include a unique fill_id,
    source kind and explicit proof attribution. No margin or shorting.
    """
    asof = utc_time(asof_utc, "asof_utc")
    capital = amount(initial_capital_eur, "initial_capital_eur", positive=True)
    if isinstance(max_mark_age_seconds, bool) or not isinstance(max_mark_age_seconds, int) or max_mark_age_seconds < 0:
        raise LedgerError("max_mark_age_seconds must be a nonnegative integer")
    if not isinstance(fills, list) or not isinstance(marks, dict):
        raise LedgerError("fills list and marks object required")
    ordered = []
    ids = set()
    for i, item in enumerate(fills):
        if not isinstance(item, dict):
            raise LedgerError(f"fills[{i}] must be an object")
        if item.get("record_type") != "FILL_CONFIRMED":
            raise LedgerError("BUY_SENT and recommendations are never fills")
        fid = item.get("fill_id")
        if not isinstance(fid, str) or not fid.strip() or fid in ids:
            raise LedgerError("missing or duplicate fill_id")
        ids.add(fid)
        kind = item.get("execution_kind")
        if kind not in ("MODEL_FILL", "OPERATOR_ATTESTED_FILL"):
            raise LedgerError("fill must declare model or attested execution")
        if kind == "OPERATOR_ATTESTED_FILL" and not item.get("proof_ref"):
            raise LedgerError("attested fill missing proof reference")
        when = utc_time(item.get("fill_ts_utc"), "fill timestamp")
        if when > asof:
            raise LedgerError("future fill relative to as-of")
        market = item.get("market")
        if not isinstance(market, str) or not market.endswith("-EUR"):
            raise LedgerError("market must be a EUR pair")
        side = item.get("side")
        if side not in ("BUY", "SELL"):
            raise LedgerError("side must be BUY or SELL")
        price = amount(item.get("price_eur"), "price_eur", positive=True)
        quantity = amount(item.get("quantity"), "quantity", positive=True)
        fee = amount(item.get("fee_eur"), "fee_eur")
        ordered.append((when, fid, market, side, price, quantity, fee, kind))
    ordered.sort(key=lambda row: (row[0], row[1]))

    cash = capital
    realized = Decimal(0)
    fees = Decimal(0)
    positions = {}
    movements = []
    model_count = 0
    attested_count = 0
    for when, fid, market, side, price, qty, fee, kind in ordered:
        gross = price * qty
        current = positions.get(market, {"qty": Decimal(0), "basis": Decimal(0), "last_ts": when})
        if side == "BUY":
            cost = gross + fee
            if cost > cash:
                raise LedgerError(f"{fid}: insufficient cash; no double spending or leverage")
            cash -= cost
            current["qty"] += qty
            current["basis"] += cost
        else:
            if qty > current["qty"]:
                raise LedgerError(f"{fid}: short sale or unmatched fill")
            basis_consumed = current["basis"] * qty / current["qty"]
            proceeds = gross - fee
            if proceeds < 0:
                raise LedgerError(f"{fid}: proceeds below fees")
            cash += proceeds
            realized += proceeds - basis_consumed
            current["qty"] -= qty
            current["basis"] -= basis_consumed
            if current["qty"] == 0:
                current["basis"] = Decimal(0)
        current["last_ts"] = when
        positions[market] = current
        fees += fee
        model_count += kind == "MODEL_FILL"
        attested_count += kind == "OPERATOR_ATTESTED_FILL"
        residual = cash + sum((p["basis"] for p in positions.values()), Decimal(0))
        if abs(residual - (capital + realized)) > Decimal("0.000001"):
            raise LedgerError("cash + cost basis != initial capital + realized PnL")
        movements.append({
            "fill_id": fid, "fill_ts_utc": when.isoformat(),
            "market": market, "side": side, "execution_kind": kind,
            "cash_after_eur": as_num(cash),
            "realized_pnl_cumulative_eur": as_num(realized),
        })
    active = {k: v for k, v in positions.items() if v["qty"] > 0}
    mark_value = Decimal(0)
    stale_or_missing = []
    visible_positions = {}
    for market, pos in sorted(active.items()):
        mark = marks.get(market)
        valid = isinstance(mark, dict)
        if valid:
            try:
                mark_ts = utc_time(mark.get("asof_utc"), "mark.asof_utc")
                mark_price = amount(mark.get("price_eur"), "mark.price_eur", positive=True)
                valid = (pos["last_ts"] <= mark_ts <= asof and (asof - mark_ts).total_seconds() <= max_mark_age_seconds)
            except LedgerError:
                valid = False
        if not valid:
            stale_or_missing.append(market)
        else:
            mark_value += pos["qty"] * mark_price
        visible_positions[market] = {
            "quantity": as_num(pos["qty"]),
            "cost_basis_eur": as_num(pos["basis"]),
            "marked_value_eur": as_num(pos["qty"] * mark_price) if valid else None,
        }
    fully_marked = not stale_or_missing
    equity = cash + mark_value if fully_marked else None
    return {
        "schema": "solaire_economic_cash_ledger_v1",
        "asof_utc": asof.isoformat(),
        "initial_capital_eur": as_num(capital),
        "fills_processed": len(ordered),
        "model_fill_count": model_count,
        "operator_attested_unverified_fill_count": attested_count,
        "cash_eur": as_num(cash),
        "realized_pnl_eur": as_num(realized),
        "fees_eur": as_num(fees),
        "positions": visible_positions,
        "marks_missing_or_stale": stale_or_missing,
        "equity_eur": as_num(equity) if equity is not None else None,
        "total_pnl_eur": as_num(equity - capital) if equity is not None else None,
        "max_drawdown_eur": None,
        "movements": movements,
        "evidence_class": "MODEL_ONLY" if model_count else (
            "OPERATOR_ATTESTED_NOT_INDEPENDENTLY_VERIFIED" if attested_count else "NO_FILLS"),
        "real_executable_pnl_proven": False,
        "orders_submitted": False,
    }
