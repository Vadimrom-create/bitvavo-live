#!/usr/bin/env python3
"""Transport e-mail pour Bitvavo Ignition V3.

La logique de trading vit dans early_detector.py. Ce script n'envoie un mail normal
que pour les lignes explicitement marquées buy_ready=True par V3. Il conserve un
mode test manuel et un cooldown anti-spam.
"""
from __future__ import annotations

import json
import os
import smtplib
import ssl
import sys
import time
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

EARLY_JSON = Path("early_watch.json")
LIVE_JSON = Path("bitvavo_live.json")
STATE_JSON = Path("alert_state.json")

MAX_SNAPSHOT_AGE_SECONDS = 15 * 60
COOLDOWN_SECONDS = 6 * 3600
RESEND_SCORE_IMPROVEMENT = 0.70
MAX_CANDIDATES = 2


def num(x: Any, default: float | None = None) -> float | None:
    try:
        return float(x)
    except Exception:
        return default


def env_flag(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "on"}


def load_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default
    except Exception as exc:
        raise RuntimeError(f"Fichier JSON illisible: {path}: {exc}") from exc


def parse_ts(value: Any) -> float | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


def load_state() -> dict:
    state = load_json(STATE_JSON, {"markets": {}})
    if not isinstance(state, dict):
        state = {"markets": {}}
    if not isinstance(state.get("markets"), dict):
        state["markets"] = {}
    return state


def save_state(state: dict) -> None:
    tmp = STATE_JSON.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(STATE_JSON)


def fmt(x: Any, digits=2, signed=False) -> str:
    v = num(x)
    if v is None:
        return "n/d"
    return f"{v:+.{digits}f}" if signed else f"{v:.{digits}f}"


def fmt_price(x: Any) -> str:
    v = num(x)
    if v is None:
        return "n/d"
    digits = 2 if v >= 100 else 4 if v >= 1 else 6 if v >= 0.01 else 8
    return f"{v:.{digits}f} €"


def tf_line(label: str, s: dict) -> str:
    if not s:
        return f"  {label}: n/d"
    return (
        f"  {label}: Δ1={fmt(s.get('ch1'),2,True)}% | Δ4={fmt(s.get('ch4'),2,True)}% | "
        f"vol1={fmt(s.get('vr1'))}x | vol4={fmt(s.get('vr4'))}x | wick={fmt(s.get('wick'))}"
    )


def select_buy_ready(payload: dict, state: dict, now_ts: float) -> list[dict]:
    accepted = []
    for row in payload.get("watch") or []:
        if not isinstance(row, dict) or not row.get("buy_ready"):
            continue
        market = str(row.get("market") or "")
        if not market:
            continue
        score = num(row.get("final_score", row.get("early_score")), 0.0) or 0.0
        previous = state["markets"].get(market, {})
        last_sent = num(previous.get("last_sent_ts"))
        last_score = num(previous.get("last_sent_score"), 0.0) or 0.0
        if last_sent is not None and now_ts - last_sent < COOLDOWN_SECONDS and score - last_score < RESEND_SCORE_IMPROVEMENT:
            continue
        accepted.append(row)
    accepted.sort(key=lambda r: num(r.get("final_score", r.get("early_score")), 0.0) or 0.0, reverse=True)
    return accepted[:MAX_CANDIDATES]


def btc_context(live: dict) -> str:
    btc = next((r for r in live.get("markets", []) if r.get("market") == "BTC-EUR"), None)
    if not btc:
        return "BTC: n/d"
    return f"BTC: {fmt_price(btc.get('last'))} | 24 h {fmt(btc.get('change_24h_pct'),2,True)}%"


def build_body(payload: dict, live: dict, candidates: list[dict], test_mode: bool) -> str:
    generated = payload.get("generated_at_utc", "n/d")
    try:
        local = datetime.fromisoformat(str(generated).replace("Z", "+00:00")).astimezone(ZoneInfo("Europe/Paris"))
        generated_local = local.strftime("%d/%m/%Y %H:%M:%S")
    except Exception:
        generated_local = str(generated)

    lines = [
        "BITVAVO — IGNITION V3",
        f"Snapshot : {generated_local} (Paris)",
        btc_context(live),
        "",
    ]
    if test_mode:
        lines += [
            "TEST DE L'ALERTE E-MAIL — aucun ordre d'achat n'est implicite.",
            "",
        ]
    else:
        lines += [
            "V3 a classé le setup BUY_READY après au moins deux confirmations.",
            "Une vérification finale dans ChatGPT reste recommandée avant exécution.",
            "",
        ]

    enriched = payload.get("enriched") or {}
    for row in candidates:
        market = row.get("market")
        t = row.get("trajectory") or {}
        sc = row.get("scores") or {}
        e = enriched.get(market, {}) or {}
        book = e.get("book") or {}
        lines += [
            f"{market} — {row.get('early_stage')} — {row.get('signal_mode')}",
            f"Score final : {fmt(row.get('final_score', row.get('early_score')),2)}/10 | confirmations : {row.get('confirm_count','n/d')}",
            f"Scores bruts : BURST {fmt(sc.get('burst'))} | SLOW {fmt(sc.get('slow'))} | CONT {fmt(sc.get('continuation'))}",
            f"Prix : {fmt_price(row.get('last'))} | 24 h {fmt(row.get('change_24h_pct'),2,True)}%",
            f"Δ15 min : {fmt(t.get('dprice_15m_pct'),2,True)}% | Δ1 h : {fmt(t.get('dprice_60m_pct'),2,True)}% | Δ4 h : {fmt(t.get('dprice_240m_pct'),2,True)}%",
            f"Depuis premier signal : {fmt(t.get('price_since_first_early_pct'),2,True)}% | rang actuel #{row.get('current_rank','n/d')}",
            f"Volume 24 h : {fmt(row.get('quote_volume_24h_eur'),0)} € | spread {fmt(row.get('spread_pct'),4)}% | carnet acheteur {fmt((num(book.get('bid_share')) or 0)*100,1)}%",
            f"Flags : {', '.join(row.get('risk_flags') or []) or 'aucun'}",
            tf_line("5 min", e.get("5m") or {}),
            tf_line("15 min", e.get("15m") or {}),
            tf_line("1 h", e.get("1h") or {}),
            tf_line("4 h", e.get("4h") or {}),
            "",
        ]
    if not test_mode:
        lines.append("Action : ouvre ChatGPT et demande « lance le scan » pour la validation finale NIL / HEI / HUMA.")
    return "\n".join(lines)


def send_email(user: str, password: str, recipient: str, subject: str, body: str) -> None:
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = recipient
    msg.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context, timeout=20) as smtp:
        smtp.login(user, password)
        smtp.send_message(msg)


def write_job_summary(text: str) -> None:
    path = os.getenv("GITHUB_STEP_SUMMARY")
    if not path:
        return
    try:
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(text + "\n")
    except Exception:
        pass


def main() -> int:
    user = os.getenv("ALERT_GMAIL_USER", "").strip()
    recipient = os.getenv("ALERT_EMAIL_TO", "").strip()
    password = os.getenv("GMAIL_APP_PASSWORD", "").strip().replace(" ", "")
    test_mode = env_flag("ALERT_TEST_MODE")

    if not user or not recipient or not password:
        print("EMAIL_ALERT_CONFIG_MISSING")
        write_job_summary("⚠️ Alerte e-mail non configurée.")
        return 0

    payload = load_json(EARLY_JSON, {})
    live = load_json(LIVE_JSON, {})
    now_ts = time.time()
    generated_ts = parse_ts(payload.get("generated_at_utc"))
    if generated_ts is None or now_ts - generated_ts > MAX_SNAPSHOT_AGE_SECONDS:
        print("EMAIL_ALERT_SKIPPED stale_snapshot")
        return 0

    state = load_state()
    candidates = select_buy_ready(payload, state, now_ts)

    if test_mode:
        if not candidates:
            candidates = [r for r in (payload.get("watch") or [])[:3] if isinstance(r, dict)]
        subject = "[TEST] Bitvavo Ignition V3 — alerte e-mail opérationnelle"
    elif not candidates:
        print("EMAIL_ALERT_SKIPPED no_buy_ready")
        write_job_summary("✅ Aucun BUY_READY : aucun e-mail envoyé.")
        return 0
    else:
        top = candidates[0]
        extra = f" +{len(candidates)-1}" if len(candidates) > 1 else ""
        subject = f"🚨 Bitvavo BUY_READY — {top.get('market')} {fmt(top.get('final_score', top.get('early_score')),2)}/10{extra}"

    body = build_body(payload, live, candidates, test_mode)
    send_email(user, password, recipient, subject, body)

    if not test_mode:
        for row in candidates:
            market = str(row.get("market"))
            state["markets"][market] = {
                "last_sent_ts": now_ts,
                "last_sent_score": num(row.get("final_score", row.get("early_score")), 0.0),
                "last_sent_stage": row.get("early_stage"),
                "last_sent_mode": row.get("signal_mode"),
                "last_sent_price": num(row.get("last")),
            }
        state["updated_at_utc"] = datetime.now(timezone.utc).isoformat()
        save_state(state)

    label = "test" if test_mode else "BUY_READY:" + ", ".join(str(r.get("market")) for r in candidates)
    print(f"EMAIL_ALERT_SENT recipient={recipient} mode={label}")
    write_job_summary(f"✅ E-mail envoyé à `{recipient}` ({label}).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"EMAIL_ALERT_ERROR {exc}", file=sys.stderr)
        raise
