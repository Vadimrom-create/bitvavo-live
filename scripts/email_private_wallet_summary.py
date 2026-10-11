#!/usr/bin/env python3
"""Deliver a confidential, read-only Bitvavo wallet digest directly by Gmail.

Runs before encrypting/deleting the local wallet snapshot. Never logs holdings,
tokens, prices or SMTP payloads. No trading API write permissions are used.
"""
from __future__ import annotations

import json
import math
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from email_alert import send_email

SUMMARY = ROOT / "wallet_private_summary.json"
RECIPIENT = "bellonirom@gmail.com"
MAX_ACCOUNT_AGE_SECONDS = 180
MAX_EVIDENCE_AGE_SECONDS = 180


def number(value):
    if isinstance(value, bool):
        return None
    try:
        n = float(value)
        return n if math.isfinite(n) else None
    except (ValueError, TypeError, OverflowError):
        return None


def timestamp(value):
    try:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return dt.timestamp() if dt.tzinfo is not None else None
    except (ValueError, TypeError, OverflowError):
        return None


def age_valid(value, now, limit):
    ts = timestamp(value)
    return ts is not None and -10 <= now - ts <= limit


def money(value):
    n = number(value)
    return "n/d" if n is None else f"{n:,.2f} EUR".replace(",", " ")


def price(value):
    n = number(value)
    return "n/d" if n is None else f"{n:.{2 if n >= 100 else 5 if n >= 1 else 8}f} EUR"


def pct(value):
    n = number(value)
    return "n/d" if n is None else f"{n:+.2f}%"


def quantity(value):
    n = number(value)
    return "n/d" if n is None else f"{n:.10g}"


def _book_trade_lines(evidence, now):
    status = evidence.get("status", "NOT_OBSERVED")
    book_fresh = age_valid(evidence.get("book_retrieved_at_utc"), now, MAX_EVIDENCE_AGE_SECONDS)
    trades_fresh = age_valid(evidence.get("trades_retrieved_at_utc"), now, MAX_EVIDENCE_AGE_SECONDS)
    if status != "OK" or not book_fresh or not trades_fresh:
        return [f"Carnet/trades : {status} / fraîcheur non garantie — ne pas utiliser pour exécuter."]
    near = (evidence.get("near_depth") or {}).get("within_1pct") or {}
    flow = evidence.get("recent_public_trade_flow") or {}
    buy_share = number(flow.get("buy_taker_share"))
    latest = evidence.get("latest_public_trade") or {}
    estimate = evidence.get("held_quantity_sell_estimate") or {}
    result = [
        "Carnet : bid " + price(evidence.get("best_bid")) +
        " | ask " + price(evidence.get("best_ask")) +
        " | spread " + pct(evidence.get("spread_pct")),
        "Profondeur +/-1% : bids " + money(near.get("bid_notional_eur")) +
        " | asks " + money(near.get("ask_notional_eur")),
        "100 derniers trades max : acheteurs " +
        ("n/d" if buy_share is None else f"{buy_share*100:.1f}%") +
        " | échantillon " + str(flow.get("sample_trades", "n/d")) +
        " | dernier trade âge " +
        ("n/d" if number(latest.get("age_seconds_at_write")) is None
         else f"{number(latest.get('age_seconds_at_write')):.0f}s"),
        "Volume 24h " + money(evidence.get("quote_volume_24h_eur")) +
        " | variation 24h " + pct(evidence.get("change_24h_pct")),
    ]
    if estimate.get("complete_in_depth") is True:
        result.append("Vente de la quantité détenue au carnet observé (avant frais) : " +
                      money(estimate.get("estimated_proceeds_eur")) +
                      " | impact vs bid " + pct(-number(estimate.get("impact_below_best_bid_pct")))
                      if number(estimate.get("impact_below_best_bid_pct")) is not None else
                      "Vente quantité détenue estimée : " + money(estimate.get("estimated_proceeds_eur")))
    else:
        result.append("Vente quantité détenue : profondeur de carnet insuffisante / n/d.")
    return result


def build_digest(summary, now=None):
    now = time.time() if now is None else now
    if not isinstance(summary, dict) or not isinstance(summary.get("positions"), list):
        raise ValueError("INVALID_WALLET_SCHEMA")
    if not age_valid(summary.get("generated_at_utc"), now, MAX_ACCOUNT_AGE_SECONDS):
        raise ValueError("STALE_PRIVATE_WALLET_SNAPSHOT")
    for k in ("cash_eur", "wallet_value_eur", "positions_value_eur"):
        if number(summary.get(k)) is None or number(summary[k]) < 0:
            raise ValueError("INVALID_PRIVATE_WALLET_TOTAL")
    if abs(summary["cash_eur"] + summary["positions_value_eur"] - summary["wallet_value_eur"]) > 0.05:
        raise ValueError("INCONSISTENT_PRIVATE_WALLET_TOTAL")
    stamp = datetime.fromtimestamp(timestamp(summary["generated_at_utc"]), timezone.utc)
    paris = stamp.astimezone(ZoneInfo("Europe/Paris")).strftime("%d/%m/%Y %H:%M:%S")
    lines = [
        "SOLAIRE WALLET — RELEVÉ CONFIDENTIEL",
        "Message privé pour analyse dans ChatGPT. Ne pas publier ni transférer.",
        "Source : compte Bitvavo en lecture seule et observations publiques.",
        "Observation du compte : " + paris + " (Paris)",
        "Cash disponible : " + money(summary["cash_eur"]),
        "Positions valorisées : " + money(summary["positions_value_eur"]),
        "WALLET TOTAL : " + money(summary["wallet_value_eur"]),
        "Positions détenues : " + str(len(summary["positions"])),
        "",
    ]
    invested = 0.0
    pnl = 0.0
    unknown = False
    for row in summary["positions"]:
        if not isinstance(row, dict) or not isinstance(row.get("market"), str):
            raise ValueError("INVALID_WALLET_POSITION")
        held = number(row.get("quantity"))
        pru = number(row.get("pru_eur"))
        value = number(row.get("value_eur"))
        bid = number(row.get("price_eur"))
        if held is None or held <= 0:
            raise ValueError("INVALID_WALLET_QUANTITY")
        cost = held * pru if pru is not None and pru > 0 else None
        gain = value - cost if value is not None and cost is not None else None
        gain_pct = (gain / cost * 100) if gain is not None and cost else None
        if gain is None:
            unknown = True
        else:
            invested += cost
            pnl += gain
        evidence = row.get("execution_evidence") or {}
        if not isinstance(evidence, dict):
            evidence = {}
        lines.extend([
            row["market"] + " — " + str(row.get("management_state", "HOLD")),
            "Quantité : " + quantity(held) + " | PRU reconstruit : " + price(pru),
            "Bid de valorisation : " + price(bid) + " | valeur : " + money(value),
            "PnL latent brut : " + money(gain) + " | " + pct(gain_pct),
            *_book_trade_lines(evidence, now),
            "",
        ])
    if unknown:
        lines.append("PnL TOTAL : NON CALCULABLE (PRU ou valorisation manquant pour au moins une position).")
        lines.append("PnL des seules lignes connues : " + money(pnl) + " (partiel, ne pas traiter comme PnL total).")
    else:
        lines.append("PnL TOTAL LATENT BRUT : " + money(pnl) +
                     " | " + pct(pnl / invested * 100 if invested > 0 else None))
    coverage = summary.get("execution_coverage") or {}
    lines.extend([
        "Couverture carnets/trades : " + str((coverage.get("status_counts") or {}).get("OK", 0)) +
        "/" + str(len(summary["positions"])) + " OK",
        "PRU reconstruit depuis l'historique accessible ; peut être incomplet.",
        "PnL brut hors frais et fiscalité ; cash = EUR disponible, hors EUR bloqués dans des ordres.",
        "Pas de visibilité sur les ordres ouverts avec la clé en lecture seule.",
        "Carnets instantanés et transactions publiques : pas une garantie de liquidité future.",
        "Aucun ordre automatique. Les données deviennent périmées après la collecte.",
    ])
    return "SOLAIRE WALLET — relevé privé", "\n".join(lines)


def main():
    # The receiving mailbox is intentionally hardcoded to prevent accidental
    # or malicious recipient changes through unrelated workflow parameters.
    user = os.getenv("ALERT_GMAIL_USER", "").strip()
    password = os.getenv("GMAIL_APP_PASSWORD", "").replace(" ", "").strip()
    recipient = os.getenv("ALERT_EMAIL_TO", "").strip()
    if not user or not password or recipient.lower() != RECIPIENT:
        print("PRIVATE_WALLET_EMAIL_CONFIG_MISSING_OR_RECIPIENT_MISMATCH")
        return 2
    try:
        summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
        subject, body = build_digest(summary)
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print("PRIVATE_WALLET_EMAIL_UNSAFE_SNAPSHOT " + type(exc).__name__)
        return 2
    try:
        send_email(user, password, RECIPIENT, subject, body)
    except Exception as exc:
        # Never leak SMTP exceptions; they may include message or mailbox data.
        print("PRIVATE_WALLET_EMAIL_TRANSPORT_FAILED " + type(exc).__name__)
        return 2
    print("PRIVATE_WALLET_EMAIL_SENT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
