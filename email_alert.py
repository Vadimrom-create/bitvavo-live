#!/usr/bin/env python3
"""Envoie une alerte Gmail uniquement pour les signaux EARLY V2 exploitables."""

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

MIN_EARLY_SCORE = 7.40
STRONG_SCORE = 8.20
MIN_VOL24_EUR = 75_000.0
MAX_SPREAD_PCT = 0.25
MIN_BID_SHARE = 0.42
MAX_CHANGE24_PCT = 12.0
MAX_SINCE_FIRST_PCT = 5.0
MIN_SCORE_ACCEL_15M = 0.80
MIN_RANK_ACCEL_15M = 20.0
COOLDOWN_SECONDS = 3 * 3600
RESEND_SCORE_IMPROVEMENT = 0.80
MAX_SNAPSHOT_AGE_SECONDS = 15 * 60
MAX_CANDIDATES = 4
ALLOWED_STAGES = {"EARLY", "IGNITION"}


def number(value: Any, default: float | None = None) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def env_flag(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "on"}


def load_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Fichier JSON illisible: {path}: {exc}") from exc


def parse_timestamp(value: Any) -> float | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()
    except (TypeError, ValueError):
        return None


def snapshot_age_seconds(payload: dict[str, Any], now_ts: float) -> float | None:
    generated_ts = parse_timestamp(payload.get("generated_at_utc"))
    return now_ts - generated_ts if generated_ts is not None else None


def load_state() -> dict[str, Any]:
    state = load_json(STATE_JSON, {"markets": {}})
    if not isinstance(state, dict):
        state = {"markets": {}}
    if not isinstance(state.get("markets"), dict):
        state["markets"] = {}
    return state


def save_state(state: dict[str, Any]) -> None:
    temporary = STATE_JSON.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(STATE_JSON)


def enrichment(payload: dict[str, Any], market: str) -> dict[str, Any]:
    value = (payload.get("enriched") or {}).get(market, {})
    return value if isinstance(value, dict) else {}


def book_bid_share(payload: dict[str, Any], market: str) -> float | None:
    book = enrichment(payload, market).get("book") or {}
    return number(book.get("bid_share", book.get("bid_share_50")))


def candidate_rejection_reason(
    row: dict[str, Any], payload: dict[str, Any], state: dict[str, Any], now_ts: float
) -> str | None:
    market = str(row.get("market") or "")
    score = number(row.get("early_score"), 0.0) or 0.0
    stage = str(row.get("early_stage") or "")
    volume = number(row.get("quote_volume_24h_eur"), 0.0) or 0.0
    spread = number(row.get("spread_pct"))
    change24 = number(row.get("change_24h_pct"), 0.0) or 0.0
    trajectory = row.get("trajectory") or {}
    since_first = number(trajectory.get("price_since_first_early_pct"), 0.0) or 0.0
    dscore15 = number(trajectory.get("dscore_15m"))
    drank15 = number(trajectory.get("drank_15m"))
    bid_share = book_bid_share(payload, market)

    if not market:
        return "marché absent"
    if stage not in ALLOWED_STAGES:
        return "stage non admis"
    if score < MIN_EARLY_SCORE:
        return "score insuffisant"
    if volume < MIN_VOL24_EUR:
        return "volume 24 h insuffisant"
    if spread is None or spread > MAX_SPREAD_PCT:
        return "spread trop large ou absent"
    if bid_share is None or bid_share < MIN_BID_SHARE:
        return "carnet acheteur insuffisant ou absent"
    if change24 > MAX_CHANGE24_PCT:
        return "mouvement 24 h déjà trop avancé"
    if since_first > MAX_SINCE_FIRST_PCT:
        return "mouvement depuis le premier signal déjà trop avancé"
    if score < STRONG_SCORE and not (
        (dscore15 is not None and dscore15 >= MIN_SCORE_ACCEL_15M)
        or (drank15 is not None and drank15 >= MIN_RANK_ACCEL_15M)
    ):
        return "accélération 15 min insuffisante"

    previous = (state.get("markets") or {}).get(market) or {}
    last_sent_ts = number(previous.get("last_sent_ts"))
    last_sent_score = number(previous.get("last_sent_score"), 0.0) or 0.0
    if (
        last_sent_ts is not None
        and now_ts - last_sent_ts < COOLDOWN_SECONDS
        and score - last_sent_score < RESEND_SCORE_IMPROVEMENT
    ):
        return "cooldown anti-répétition"
    return None


def select_candidates(
    payload: dict[str, Any], state: dict[str, Any], now_ts: float
) -> tuple[list[dict[str, Any]], dict[str, str]]:
    accepted: list[dict[str, Any]] = []
    rejected: dict[str, str] = {}
    rows = payload.get("watch") or []
    for row in rows:
        if not isinstance(row, dict):
            continue
        reason = candidate_rejection_reason(row, payload, state, now_ts)
        market = str(row.get("market") or "inconnu")
        if reason:
            rejected[market] = reason
        else:
            accepted.append(row)
    accepted.sort(key=lambda row: number(row.get("early_score"), 0.0) or 0.0, reverse=True)
    return accepted[:MAX_CANDIDATES], rejected


def fmt(value: Any, digits: int = 2, signed: bool = False) -> str:
    parsed = number(value)
    if parsed is None:
        return "n/d"
    sign = "+" if signed else ""
    return f"{parsed:{sign}.{digits}f}"


def fmt_price(value: Any) -> str:
    parsed = number(value)
    if parsed is None:
        return "n/d"
    digits = 2 if parsed >= 100 else 4 if parsed >= 1 else 6 if parsed >= 0.01 else 8
    return f"{parsed:.{digits}f} €"


def timeframe_line(label: str, summary: dict[str, Any]) -> str:
    if not isinstance(summary, dict) or not summary:
        return f"  {label}: n/d"
    ch1 = summary.get("ch1", summary.get("change_1_candle_pct"))
    ch4 = summary.get("ch4", summary.get("change_4_candles_pct"))
    ch16 = summary.get("ch16", summary.get("change_16_candles_pct"))
    vr1 = summary.get("vr1", summary.get("volume_last_vs_prev20"))
    vr4 = summary.get("vr4", summary.get("volume_4_vs_prev4"))
    wick = summary.get("wick", summary.get("max_upper_wick_ratio_8bar"))
    return (
        f"  {label}: Δ1={fmt(ch1, 2, True)} % | Δ4={fmt(ch4, 2, True)} % | "
        f"Δ16={fmt(ch16, 2, True)} % | vol1/20={fmt(vr1)}x | "
        f"vol4/4={fmt(vr4)}x | mèche={fmt(wick)}"
    )


def snapshot_label(generated_at: Any) -> str:
    ts = parse_timestamp(generated_at)
    if ts is None:
        return str(generated_at or "n/d")
    local = datetime.fromtimestamp(ts, tz=timezone.utc).astimezone(ZoneInfo("Europe/Paris"))
    utc = datetime.fromtimestamp(ts, tz=timezone.utc)
    return f"{local:%d/%m/%Y %H:%M} (Paris) — {utc:%H:%M} UTC"


def btc_context(live_payload: dict[str, Any]) -> str:
    markets = live_payload.get("markets") or []
    btc = next(
        (row for row in markets if isinstance(row, dict) and row.get("market") == "BTC-EUR"),
        None,
    )
    if not btc:
        return "BTC : contexte indisponible"
    m15 = btc.get("m15") or {}
    return (
        f"BTC : {fmt_price(btc.get('last'))} | 24 h {fmt(btc.get('change_24h_pct'), 2, True)} % | "
        f"15 min Δ4 {fmt(m15.get('change_4_candles_pct'), 2, True)} % | "
        f"vol4/4 {fmt(m15.get('volume_4_vs_prev4'))}x"
    )


def build_alert_message(
    candidates: list[dict[str, Any]],
    payload: dict[str, Any],
    live_payload: dict[str, Any],
    sender: str,
    recipient: str,
) -> EmailMessage:
    first = candidates[0]
    first_market = str(first.get("market") or "?").removesuffix("-EUR")
    first_score = number(first.get("early_score"), 0.0) or 0.0
    extra = f" (+{len(candidates) - 1})" if len(candidates) > 1 else ""

    lines = [
        "BITVAVO — ALERTE EARLY V2",
        f"Snapshot : {snapshot_label(payload.get('generated_at_utc'))}",
        "⚠️ Ceci n'est pas un ordre d'achat.",
        "",
    ]
    for index, row in enumerate(candidates, 1):
        market = str(row.get("market") or "?")
        trajectory = row.get("trajectory") or {}
        enriched = enrichment(payload, market)
        book = enriched.get("book") or {}
        bid_share = number(book.get("bid_share", book.get("bid_share_50")))
        lines.extend(
            [
                f"{index}. {market} — {fmt(row.get('early_score'))}/10 — {row.get('early_stage', 'n/d')}",
                f"  Cours : {fmt_price(row.get('last'))} | 24 h : {fmt(row.get('change_24h_pct'), 2, True)} %",
                f"  Liquidité : {fmt(row.get('quote_volume_24h_eur'), 0)} € / 24 h | spread {fmt(row.get('spread_pct'), 4)} % | acheteurs carnet {fmt((bid_share or 0) * 100, 1)} %",
                f"  Trajectoire 15 min : Δscore {fmt(trajectory.get('dscore_15m'), 2, True)} | Δrang {fmt(trajectory.get('drank_15m'), 0, True)} | Δprix {fmt(trajectory.get('dprice_15m_pct'), 2, True)} %",
                f"  Depuis premier EARLY : {fmt(trajectory.get('price_since_first_early_pct'), 2, True)} %",
                timeframe_line("5 min", enriched.get("5m") or {}),
                timeframe_line("15 min", enriched.get("15m") or row.get("m15") or {}),
                timeframe_line("1 h", enriched.get("1h") or {}),
                timeframe_line("4 h", enriched.get("4h") or {}),
                "",
            ]
        )
    lines.extend(
        [
            btc_context(live_payload),
            "",
            "Action : lancer le scan ChatGPT pour validation NIL / HEI / HUMA avant toute entrée.",
        ]
    )

    message = EmailMessage()
    message["Subject"] = f"🚨 Bitvavo EARLY — {first_market} {first_score:.2f}/10{extra}"
    message["From"] = f"Bitvavo Early Alert <{sender}>"
    message["To"] = recipient
    message.set_content("\n".join(lines))
    return message


def build_test_message(
    payload: dict[str, Any], sender: str, recipient: str
) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = "✅ Test alerte Bitvavo — configuration OK"
    message["From"] = f"Bitvavo Early Alert <{sender}>"
    message["To"] = recipient
    message.set_content(
        "\n".join(
            [
                "BITVAVO — TEST DE L'ALERTE E-MAIL",
                f"Snapshot : {snapshot_label(payload.get('generated_at_utc'))}",
                "",
                "La collecte, la détection EARLY V2 et l'envoi Gmail sont opérationnels.",
                "Ceci est un test technique, pas un signal d'achat.",
            ]
        )
    )
    return message


def send_gmail(message: EmailMessage, user: str, password: str) -> None:
    clean_password = "".join(password.split())
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30, context=context) as smtp:
        smtp.login(user, clean_password)
        refused = smtp.send_message(message)
    if refused:
        raise RuntimeError(f"Gmail a refusé au moins un destinataire: {', '.join(refused)}")


def write_job_summary(text: str) -> None:
    path = os.getenv("GITHUB_STEP_SUMMARY")
    if not path:
        return
    try:
        with Path(path).open("a", encoding="utf-8") as stream:
            stream.write(f"### Alerte e-mail Bitvavo\n\n{text}\n")
    except OSError:
        pass


def main() -> int:
    now_ts = time.time()
    test_mode = env_flag("ALERT_TEST_MODE")
    dry_run = env_flag("ALERT_DRY_RUN")
    payload = load_json(EARLY_JSON, {})
    live_payload = load_json(LIVE_JSON, {})
    if not isinstance(payload, dict) or not payload.get("watch"):
        raise RuntimeError("early_watch.json ne contient aucun snapshot exploitable")

    age = snapshot_age_seconds(payload, now_ts)
    if age is None or age < -300 or age > MAX_SNAPSHOT_AGE_SECONDS:
        message = f"Aucun envoi : snapshot absent ou trop ancien (âge={fmt(age, 0)} s)."
        print(f"EMAIL_ALERT_SKIPPED {message}")
        write_job_summary(message)
        return 0

    sender = os.getenv("ALERT_GMAIL_USER", "").strip()
    recipient = os.getenv("ALERT_EMAIL_TO", "").strip()
    password = os.getenv("GMAIL_APP_PASSWORD", "")
    if not sender or not recipient:
        message = "Aucun envoi : ALERT_GMAIL_USER ou ALERT_EMAIL_TO manque."
        print(f"EMAIL_ALERT_SKIPPED {message}")
        write_job_summary(message)
        return 2 if test_mode else 0

    state = load_state()
    candidates, rejected = select_candidates(payload, state, now_ts)
    if test_mode:
        outgoing = build_test_message(payload, sender, recipient)
    elif candidates:
        outgoing = build_alert_message(candidates, payload, live_payload, sender, recipient)
    else:
        message = f"Aucun envoi : 0 candidat sur {len(payload.get('watch') or [])}."
        print(f"EMAIL_ALERT_SKIPPED {message}")
        for market, reason in list(rejected.items())[:10]:
            print(f"  {market}: {reason}")
        write_job_summary(message)
        return 0

    if dry_run:
        print("EMAIL_ALERT_DRY_RUN")
        print(outgoing.as_string())
        return 0
    if not password:
        message = "Aucun envoi : secret GMAIL_APP_PASSWORD absent."
        print(f"EMAIL_ALERT_SKIPPED {message}")
        write_job_summary(message)
        return 2 if test_mode else 0

    try:
        send_gmail(outgoing, sender, password)
    except Exception as exc:
        write_job_summary(f"❌ Échec SMTP : {type(exc).__name__}.")
        raise RuntimeError(f"Échec de l'envoi Gmail ({type(exc).__name__}): {exc}") from exc

    if not test_mode:
        markets = state.setdefault("markets", {})
        for row in candidates:
            market = str(row.get("market") or "")
            markets[market] = {
                "last_sent_ts": now_ts,
                "last_sent_score": number(row.get("early_score"), 0.0) or 0.0,
                "last_sent_stage": str(row.get("early_stage") or ""),
                "last_sent_price": number(row.get("last"), 0.0) or 0.0,
            }
        state["updated_at_utc"] = datetime.now(timezone.utc).isoformat()
        save_state(state)

    label = "test" if test_mode else ", ".join(row["market"] for row in candidates)
    print(f"EMAIL_ALERT_SENT recipient={recipient} mode={label}")
    write_job_summary(f"✅ E-mail envoyé à `{recipient}` ({label}).")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print(f"EMAIL_ALERT_ERROR {error}", file=sys.stderr)
        sys.exit(1)
