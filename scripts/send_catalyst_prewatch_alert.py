#!/usr/bin/env python3
"""Send early CATALYST_PREWATCH emails from official project/partner sources.

This is an information/monitoring alert, not a BUY instruction and never sends
an order. It exists specifically to surface a potentially market-moving event
before the realised NEWS and before price acceleration.
"""
from __future__ import annotations

import json
import os
import smtplib
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import email_alert
from research.common import atomic_json, finite, read_json, utc

INPUT = "production_alert_candidates.json"
STATE = "production_catalyst_alert_state.json"
STATUS = "production_catalyst_alert_status.json"
MAX_SNAPSHOT_AGE = 15 * 60


def _ts(value):
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


def credentials():
    user = os.getenv("ALERT_GMAIL_USER", "").strip()
    recipient = os.getenv("ALERT_EMAIL_TO", "").strip()
    password = os.getenv("GMAIL_APP_PASSWORD", "").strip().replace(" ", "")
    if recipient.lower() != "bellonirom@gmail.com" or not user or not password:
        return None
    return user, password, recipient


def eligible_rows(payload: dict, state: dict, now: float) -> list[dict]:
    generated = _ts(payload.get("generated_at_utc"))
    if generated is None or not -30 <= now - generated <= MAX_SNAPSHOT_AGE:
        return []

    rows = []
    markets_state = state.setdefault("markets", {})
    for row in payload.get("catalyst_prewatch") or []:
        if not isinstance(row, dict) or not row.get("market"):
            continue
        catalyst = ((row.get("news") or {}).get("catalyst") or {})
        top = catalyst.get("top") or {}
        if not catalyst.get("prewatch_trigger"):
            continue
        level = int(finite(catalyst.get("level"), 0) or 0)
        if level < 2:
            continue
        catalyst_id = str(top.get("catalyst_id") or "")
        if not catalyst_id:
            continue
        previous = markets_state.get(row["market"]) or {}
        if (
            previous.get("last_catalyst_id") == catalyst_id
            and int(previous.get("last_level", 0)) >= level
        ):
            continue
        rows.append(row)

    rows.sort(
        key=lambda row: (
            int(finite(((row.get("news") or {}).get("catalyst") or {}).get("level"), 0) or 0),
            finite(((row.get("news") or {}).get("catalyst") or {}).get("score"), 0),
            finite(row.get("quote_volume_24h_eur"), 0),
        ),
        reverse=True,
    )
    return rows


def subject(rows: list[dict]) -> str:
    if len(rows) == 1:
        row = rows[0]
        catalyst = ((row.get("news") or {}).get("catalyst") or {})
        return f"PREWATCH CATALYSEUR — {row['market']} — {catalyst.get('label', 'UPCOMING')}"
    markets = ", ".join(row["market"] for row in rows[:4])
    suffix = "" if len(rows) <= 4 else f" +{len(rows)-4}"
    return f"PREWATCH CATALYSEUR — {len(rows)} marchés — {markets}{suffix}"


def section(row: dict) -> str:
    catalyst = ((row.get("news") or {}).get("catalyst") or {})
    top = catalyst.get("top") or {}
    accel = row.get("acceleration") or {}
    direction = str(catalyst.get("direction") or "UNKNOWN")
    if catalyst.get("speculative_review"):
        interpretation = (
            "Catalyseur positif IMMINENT : candidat à une petite entrée spéculative "
            "à évaluer manuellement avant l'annonce, avec risque strictement borné."
        )
    elif direction == "POSITIVE":
        interpretation = "Catalyseur potentiellement haussier à surveiller AVANT l'annonce effective."
    elif direction == "NEGATIVE":
        interpretation = "Catalyseur potentiellement négatif : vigilance, pas de position longue anticipée sur ce seul signal."
    else:
        interpretation = "Événement imminent/probable détecté, direction de marché encore inconnue."

    lines = [
        f"{row['market']} — CATALYST_PREWATCH {catalyst.get('label', 'UPCOMING')}",
        f"Niveau : {int(finite(catalyst.get('level'), 0) or 0)}/3",
        f"Score catalyseur : {finite(catalyst.get('score'), 0):.2f}/10",
        f"Direction estimée : {direction}",
        f"Prix actuel : {finite(row.get('last'), 0):.8g} €",
        f"Variation 24 h : {finite(row.get('change_24h_pct'), 0):+.2f} %",
        f"Volume 24 h : {finite(row.get('quote_volume_24h_eur'), 0):,.0f} €",
        f"Quant actuel : {accel.get('state', 'NO_ACCELERATION')} — {finite(accel.get('score'), 0):.2f}/10 — preuves {accel.get('evidence_count', 0)}",
        "",
        f"Source : {top.get('source', 'n/a')} ({top.get('source_role', 'n/a')})",
        f"Publication : {top.get('published_at_utc', 'n/a')}",
        f"Âge : {finite(top.get('age_minutes'), 0):.1f} min",
        f"Signal temporel : {', '.join(top.get('timing_cues') or []) or 'n/a'}",
        f"Catégories : {', '.join(top.get('categories') or []) or 'n/a'}",
        f"Titre / message : {top.get('title', 'n/a')}",
    ]
    if top.get("url"):
        lines.append(f"Lien : {top['url']}")
    lines.extend([
        "",
        interpretation,
        "Ce mail est une alerte d'anticipation, pas un ordre ACHÈTE.",
        "Aucun ordre n'a été envoyé automatiquement.",
    ])
    return "\n".join(lines)


def body(rows: list[dict]) -> str:
    intro = [
        "Solaire a détecté un événement officiel AVANT une éventuelle réaction de prix.",
        "Objectif : permettre une surveillance ou une décision spéculative de petite taille avant la NEWS réalisée.",
    ]
    for idx, row in enumerate(rows, 1):
        intro.extend(["", "=" * 52, f"{idx}/{len(rows)}", "=" * 52, section(row)])
    return "\n".join(intro)


def main() -> int:
    now = time.time()
    payload = read_json(INPUT, {})
    state = read_json(STATE, {"schema": "solaire_catalyst_alert_state_v1", "markets": {}})
    status = {
        "schema": "solaire_catalyst_alert_status_v1",
        "checked_at_utc": utc(now),
        "status": "STARTING",
        "email": "NONE",
    }
    rows = eligible_rows(payload, state, now)
    if not rows:
        status.update(status="OK", reason="NO_NEW_CATALYST_PREWATCH")
        atomic_json(STATE, state)
        atomic_json(STATUS, status)
        print("SOLAIRE_CATALYST_ALERT " + json.dumps(status))
        return 0

    creds = credentials()
    if creds is None:
        status.update(status="DEGRADED", reason="SMTP_CONFIG_MISSING", pending=len(rows))
        atomic_json(STATUS, status)
        print("SOLAIRE_CATALYST_ALERT " + json.dumps(status))
        return 0

    try:
        email_alert.send_email(creds[0], creds[1], creds[2], subject(rows), body(rows))
    except smtplib.SMTPAuthenticationError:
        status.update(status="DEGRADED", reason="SMTP_AUTHENTICATION_ERROR", email="DELIVERY_PENDING_RETRY")
        atomic_json(STATUS, status)
        print("SOLAIRE_CATALYST_ALERT " + json.dumps(status))
        return 0
    except (smtplib.SMTPException, OSError) as exc:
        status.update(status="DEGRADED", reason=f"SMTP_DELIVERY_ERROR:{type(exc).__name__}", email="DELIVERY_PENDING_RETRY")
        atomic_json(STATUS, status)
        print("SOLAIRE_CATALYST_ALERT " + json.dumps(status))
        return 0

    sent_at = time.time()
    for row in rows:
        catalyst = ((row.get("news") or {}).get("catalyst") or {})
        top = catalyst.get("top") or {}
        state.setdefault("markets", {})[row["market"]] = {
            "last_catalyst_id": top.get("catalyst_id"),
            "last_level": int(finite(catalyst.get("level"), 0) or 0),
            "last_score": finite(catalyst.get("score"), 0),
            "last_sent_ts": sent_at,
            "last_sent_price": row.get("last"),
            "last_source": top.get("source"),
            "last_title": top.get("title"),
        }
    state["updated_at_ts"] = sent_at
    atomic_json(STATE, state)
    status.update(
        status="OK",
        email="SENT",
        sent_count=len(rows),
        markets=[row["market"] for row in rows],
    )
    atomic_json(STATUS, status)
    print("SOLAIRE_CATALYST_ALERT " + json.dumps(status))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
