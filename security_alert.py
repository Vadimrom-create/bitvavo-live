#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path

EVENT = Path("security_event.json")
STATE = Path("security_alert_state.json")


def load(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def main():
    event = load(EVENT, {})
    event_id = event.get("event_id")
    if not event_id:
        print("No security event.")
        return

    state = load(STATE, {})
    if state.get("last_event_id") == event_id:
        print("Security event already alerted.")
        return

    user = os.getenv("ALERT_GMAIL_USER", "").strip()
    target = os.getenv("ALERT_EMAIL_TO", "").strip() or user
    password = os.getenv("GMAIL_APP_PASSWORD", "").strip()
    if not user or not target or not password:
        raise RuntimeError("Missing Gmail alert credentials")

    subject = "🚨 URGENT — activité Bitvavo non autorisée détectée"
    lines = [
        "La sentinelle Bitvavo privée a détecté une activité qui ne correspond pas à son registre d'ordres autorisés.",
        "",
        f"Détection: {event.get('detected_at_utc')}",
        f"Raison: {event.get('reason')}",
        f"Marché: {event.get('market')}",
        f"Type événement: {event.get('event')}",
        f"Sens: {event.get('side')}",
        f"Type ordre: {event.get('orderType')}",
        f"Statut: {event.get('status')}",
        f"Actions automatiques: {', '.join(event.get('action_taken') or [])}",
        "",
        "Le moteur doit être considéré gelé jusqu'à vérification.",
    ]

    msg = EmailMessage()
    msg["From"] = user
    msg["To"] = target
    msg["Subject"] = subject
    msg.set_content("\n".join(lines))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context, timeout=30) as smtp:
        smtp.login(user, password)
        smtp.send_message(msg)

    STATE.write_text(json.dumps({"last_event_id": event_id}, indent=2) + "\n", encoding="utf-8")
    print("Security alert sent.")


if __name__ == "__main__":
    main()
