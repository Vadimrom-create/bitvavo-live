"""Automatic encrypted management plans from read-only account history.

No trade permission and no manual GitHub position secret are required.
The module reconstructs the current position cycle from Bitvavo account
transactions, derives actual average cost, then attaches either the most
recent Solaire structural plan or a fresh structural plan.
"""
from __future__ import annotations

from datetime import datetime
from hashlib import sha256
from typing import Any

from research.common import finite
from research.risk import structural_plan


def _ts(value: Any) -> float | None:
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


def merge_transaction_ledger(state: dict, fresh: list[dict]) -> list[dict]:
    """Merge by transactionId into encrypted state and keep deterministic order."""
    ledger = state.setdefault("transaction_ledger", {})
    for row in fresh:
        txid = row.get("transactionId")
        if isinstance(txid, str) and txid:
            ledger[txid] = row
    rows = list(ledger.values())
    rows.sort(key=lambda r: (_ts(r.get("executedAt")) or 0.0, str(r.get("transactionId") or "")))
    # Bound encrypted state size. Five thousand account transactions are ample
    # for the current monitoring use; fail-closed pagination protects bootstrap.
    if len(rows) > 5000:
        rows = rows[-5000:]
        state["transaction_ledger"] = {
            str(r["transactionId"]): r for r in rows if r.get("transactionId")
        }
    return rows


def update_transaction_ledger(account, state: dict, now: float) -> list[dict]:
    """Bootstrap full history once, then refresh with a 48h overlap."""
    ledger = state.get("transaction_ledger") or {}
    if not ledger:
        fresh = account.transaction_history(max_pages=50)
    else:
        last = max((_ts(r.get("executedAt")) or 0.0) for r in ledger.values())
        start_ms = int(max(0.0, last - 48 * 3600) * 1000)
        fresh = account.transaction_history(from_date=start_ms, max_pages=10)
    rows = merge_transaction_ledger(state, fresh)
    state["transaction_history_refreshed_at"] = now
    return rows


def reconstruct_positions(transactions: list[dict]) -> dict[str, dict]:
    """Average-cost inventory for the currently open cycle of each asset."""
    positions: dict[str, dict] = {}
    for row in transactions:
        kind = str(row.get("type") or "").lower()
        if kind not in {"buy", "sell"}:
            continue
        sent_cur = str(row.get("sentCurrency") or "")
        recv_cur = str(row.get("receivedCurrency") or "")
        sent = finite(row.get("sentAmount"))
        recv = finite(row.get("receivedAmount"))
        fee_cur = str(row.get("feesCurrency") or "")
        fee = finite(row.get("feesAmount"), 0.0) or 0.0
        when = _ts(row.get("executedAt"))
        if sent is None or recv is None or sent < 0 or recv < 0 or when is None:
            continue

        if kind == "buy" and sent_cur == "EUR" and recv_cur and recv_cur != "EUR":
            asset = recv_cur
            qty = recv - (fee if fee_cur == asset else 0.0)
            eur = sent + (fee if fee_cur == "EUR" else 0.0)
            if qty <= 0 or eur <= 0:
                continue
            p = positions.setdefault(asset, {
                "quantity": 0.0, "cost_eur": 0.0, "peak_quantity": 0.0,
                "cycle_started_ts": when, "latest_buy_ts": when,
                "sold_in_cycle": False, "last_sell_ts": None,
            })
            if p["quantity"] <= 1e-15:
                p.update(
                    quantity=0.0, cost_eur=0.0, peak_quantity=0.0,
                    cycle_started_ts=when, sold_in_cycle=False, last_sell_ts=None,
                )
            p["quantity"] += qty
            p["cost_eur"] += eur
            p["peak_quantity"] = max(p["peak_quantity"], p["quantity"])
            p["latest_buy_ts"] = when
            continue

        if kind == "sell" and recv_cur == "EUR" and sent_cur and sent_cur != "EUR":
            asset = sent_cur
            qty = sent + (fee if fee_cur == asset else 0.0)
            if qty <= 0:
                continue
            p = positions.get(asset)
            if not p or p["quantity"] <= 0:
                continue
            before = p["quantity"]
            reduction = min(qty, before)
            avg = p["cost_eur"] / before if before > 0 else 0.0
            p["quantity"] = max(0.0, before - reduction)
            p["cost_eur"] = max(0.0, p["cost_eur"] - reduction * avg)
            p["sold_in_cycle"] = True
            p["last_sell_ts"] = when
            if p["quantity"] <= 1e-12:
                p["quantity"] = 0.0
                p["cost_eur"] = 0.0

    result = {}
    for asset, p in positions.items():
        if p["quantity"] <= 0:
            continue
        p = dict(p)
        p["avg_cost_eur"] = p["cost_eur"] / p["quantity"] if p["quantity"] > 0 else None
        result[asset] = p
    return result


def _recent_solaire_plan(market: str, latest_buy_ts: float | None, alert_state: dict) -> dict | None:
    row = (alert_state.get("markets") or {}).get(market) or {}
    sent = finite(row.get("last_sent_ts"))
    if sent is None or latest_buy_ts is None:
        return None
    # The actual account buy must occur after the Solaire signal and close enough
    # in time that association is credible.
    if latest_buy_ts < sent - 60 or latest_buy_ts - sent > 6 * 3600:
        return None
    stop = finite(row.get("last_sent_stop_eur"))
    tp1 = finite(row.get("last_sent_profit_alert_eur"), finite(row.get("last_sent_tp1_eur")))
    tp2 = finite(row.get("last_sent_runner_reference_eur"), finite(row.get("last_sent_tp2_eur")))
    if stop is None or stop <= 0 or tp1 is None or tp1 <= 0:
        return None
    return {"stop_eur": stop, "tp1_eur": tp1, "tp2_eur": tp2}


def automatic_plan(
    market: str,
    balance: dict,
    inventory: dict | None,
    quote: dict,
    features: dict,
    meta: dict,
    alert_state: dict,
) -> dict | None:
    """Build a verified management plan without user-maintained JSON."""
    if not inventory:
        return None
    held = finite(balance.get("amount"))
    avg_cost = finite(inventory.get("avg_cost_eur"))
    if held is None or held <= 0 or avg_cost is None or avg_cost <= 0:
        return None

    signal_plan = _recent_solaire_plan(
        market, finite(inventory.get("latest_buy_ts")), alert_state
    )
    source = "ACCOUNT_HISTORY+SOLAIRE_ALERT"
    if signal_plan is None:
        ask = finite(quote.get("ask"))
        if ask is None or ask <= 0:
            return None
        fresh = structural_plan({"market": market, "ask": ask}, features, meta)
        if not fresh.get("valid"):
            return None
        signal_plan = {
            "stop_eur": fresh["stop_eur"],
            "tp1_eur": fresh["tp1_eur"],
            "tp2_eur": fresh["tp2_eur"],
        }
        source = "ACCOUNT_HISTORY+FRESH_STRUCTURE"

    stop = finite(signal_plan.get("stop_eur"))
    tp1 = finite(signal_plan.get("tp1_eur"))
    tp2 = finite(signal_plan.get("tp2_eur"))
    bid = finite(quote.get("bid"))
    if stop is None or tp1 is None or stop <= 0 or tp1 <= 0 or bid is None or bid <= 0:
        return None
    if stop >= bid:
        # A newly generated plan must never start with an already-breached stop.
        return None

    cycle = finite(inventory.get("cycle_started_ts"), 0.0) or 0.0
    position_id = sha256(f"{market}:{cycle:.3f}".encode()).hexdigest()[:24]
    initial = max(
        held,
        finite(inventory.get("peak_quantity"), held) or held,
    )
    return {
        "position_id": position_id,
        "verified": True,
        "auto_generated": True,
        "plan_source": source,
        "initial_amount": initial,
        "cost_basis_eur": avg_cost,
        "stop_eur": stop,
        "tp1_eur": tp1,
        "tp2_eur": tp2,
        "tp1_fraction": 0.5,
        "tp1_done": bool(inventory.get("sold_in_cycle")),
        "fee_rate": 0.0025,
        "slippage_rate": 0.001,
        "cycle_started_ts": cycle,
        "latest_buy_ts": finite(inventory.get("latest_buy_ts")),
    }
