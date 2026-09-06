#!/usr/bin/env python3
"""Envoie une alerte Gmail uniquement pour un signal d'achat technique confirmé."""

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

MIN_EARLY_SCORE = 9.25
MIN_VOL24_EUR = 250_000.0
MAX_SPREAD_PCT = 0.15
MIN_BID_SHARE = 0.52
MIN_CHANGE24_PCT = -1.0
MAX_CHANGE24_PCT = 8.0
MIN_SINCE_FIRST_PCT = 0.35
MAX_SINCE_FIRST_PCT = 3.0
MIN_SIGNAL_AGE_SECONDS = 10 * 60
MAX_SIGNAL_AGE_SECONDS = 60 * 60
MIN_SCORE_ACCEL_15M = 1.0
MIN_RANK_ACCEL_15M = 20.0
MIN_PRICE_ACCEL_15M = 0.20
MAX_PRICE_ACCEL_15M = 2.50
COOLDOWN_SECONDS = 12 * 3600
RESEND_SCORE_IMPROVEMENT = 1.0
MAX_SNAPSHOT_AGE_SECONDS = 15 * 60
MAX_CANDIDATES = 1
ALLOWED_STAGES = {"IGNITION"}


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


def timeframe(payload: dict[str, Any], market: str, label: str) -> dict[str, Any]:
    value = enrichment(payload, market).get(label) or {}
    return value if isinstance(value, dict) else {}


def price_vs_ema_pct(summary: dict[str, Any]) -> float | None:
    last = number(summary.get("last"))
    ema20 = number(summary.get("ema20"))
    if last is None or ema20 in (None, 0):
        return None
    return (last / ema20 - 1) * 100


def btc_rejection_reason(live_payload: dict[str, Any]) -> str | None:
    markets = live_payload.get("markets") or []
    btc = next(
        (row for row in markets if isinstance(row, dict) and row.get("market") == "BTC-EUR"),
        None,
    )
    if not btc:
        return "contexte BTC absent"
    btc_m15 = btc.get("m15") or {}
    change24 = number(btc.get("change_24h_pct"))
    change1h = number(btc_m15.get("change_4_candles_pct"))
    change4h = number(btc_m15.get("change_16_candles_pct"))
    if change24 is None or change1h is None or change4h is None:
        return "contexte BTC incomplet"
    if change24 < -3.0 or change1h < -1.0 or change4h < -3.0:
        return "contexte BTC trop baissier"
    return None


def candidate_rejection_reason(
    row: dict[str, Any],
    payload: dict[str, Any],
    live_payload: dict[str, Any],
    state: dict[str, Any],
    now_ts: float,
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
    dprice15 = number(trajectory.get("dprice_15m_pct"))
    first_seen_ts = parse_timestamp(trajectory.get("first_early_seen"))
    bid_share = book_bid_share(payload, market)
    s5 = timeframe(payload, market, "5m")
    s15 = timeframe(payload, market, "15m")
    s1h = timeframe(payload, market, "1h")
    s4h = timeframe(payload, market, "4h")

    if not market:
        return "marché absent"
    if stage not in ALLOWED_STAGES:
        return "pas en IGNITION"
    if score < MIN_EARLY_SCORE:
        return "score inférieur au seuil d'achat"
    if volume < MIN_VOL24_EUR:
        return "volume 24 h insuffisant"
    if spread is None or spread > MAX_SPREAD_PCT:
        return "spread trop large ou absent"
    if bid_share is None or bid_share < MIN_BID_SHARE:
        return "acheteurs non dominants dans le carnet"
    if not MIN_CHANGE24_PCT <= change24 <= MAX_CHANGE24_PCT:
        return "variation 24 h hors zone d'achat"
    if not MIN_SINCE_FIRST_PCT <= since_first <= MAX_SINCE_FIRST_PCT:
        return "progression depuis le premier signal hors zone d'achat"
    if first_seen_ts is None:
        return "premier signal non daté"
    signal_age = now_ts - first_seen_ts
    if not MIN_SIGNAL_AGE_SECONDS <= signal_age <= MAX_SIGNAL_AGE_SECONDS:
        return "signal pas encore confirmé ou déjà trop ancien"
    if dscore15 is None or dscore15 < MIN_SCORE_ACCEL_15M:
        return "score sans accélération confirmée sur 15 min"
    if drank15 is None or drank15 < MIN_RANK_ACCEL_15M:
        return "rang sans accélération confirmée sur 15 min"
    if dprice15 is None or not MIN_PRICE_ACCEL_15M <= dprice15 <= MAX_PRICE_ACCEL_15M:
        return "prix 15 min sans progression exploitable"

    if not all((s5, s15, s1h, s4h)):
        return "données multi-timeframes incomplètes"

    required_metrics = (
        (s5, ("ch1", "ch4", "vr1", "wick", "dist8high", "last", "ema20")),
        (s15, ("ch1", "ch4", "ch16", "vr1", "vr4", "wick", "dist8high", "last", "ema20")),
        (s1h, ("ch1", "ch4", "ch16", "vr1", "vr4", "dist8high", "last", "ema20")),
        (s4h, ("ch1", "ch4", "ch16", "dist8high", "last", "ema20")),
    )
    for summary, names in required_metrics:
        if any(number(summary.get(name)) is None for name in names):
            return "indicateurs multi-timeframes incomplets"

    if not 0.05 <= number(s5.get("ch1"), -99.0) <= 0.80:
        return "impulsion 5 min absente ou déjà trop verticale"
    if not 0.30 <= number(s5.get("ch4"), -99.0) <= 2.50:
        return "structure 5 min non exploitable"
    if number(s5.get("vr1"), 0.0) < 1.20:
        return "volume 5 min non confirmé"
    if number(s5.get("wick"), 99.0) > 0.65:
        return "rejet par mèche sur 5 min"
    if number(s5.get("dist8high"), -99.0) < -1.0:
        return "prix 5 min trop loin du sommet récent"
    extension5 = price_vs_ema_pct(s5)
    if extension5 is None or extension5 > 1.0:
        return "prix 5 min trop étendu au-dessus de sa moyenne"

    if not 0.10 <= number(s15.get("ch1"), -99.0) <= 1.50:
        return "impulsion 15 min absente ou déjà trop verticale"
    if not 0.50 <= number(s15.get("ch4"), -99.0) <= 3.50:
        return "structure 1 h non exploitable"
    if not 0.0 <= number(s15.get("ch16"), -99.0) <= 6.0:
        return "structure 4 h non exploitable"
    if number(s15.get("vr1"), 0.0) < 1.20 or number(s15.get("vr4"), 0.0) < 1.10:
        return "volume 15 min non confirmé"
    if number(s15.get("wick"), 99.0) > 0.65:
        return "rejet par mèche sur 15 min"
    if number(s15.get("dist8high"), -99.0) < -1.25:
        return "prix 15 min trop loin du sommet récent"

    if not 0.10 <= number(s1h.get("ch1"), -99.0) <= 3.0:
        return "confirmation 1 h absente ou trop avancée"
    if not 0.20 <= number(s1h.get("ch4"), -99.0) <= 5.0:
        return "tendance 4 h non confirmée"
    if number(s1h.get("ch16"), -99.0) < -1.0:
        return "tendance 16 h défavorable"
    if number(s1h.get("vr1"), 0.0) < 0.80 or number(s1h.get("vr4"), 0.0) < 0.80:
        return "volume horaire non confirmé"
    if number(s1h.get("dist8high"), -99.0) < -2.0:
        return "structure horaire en retrait"

    if number(s4h.get("ch1"), -99.0) < 0.0 or number(s4h.get("ch4"), -99.0) < 0.0:
        return "tendance 4 h non alignée"
    if number(s4h.get("ch16"), 99.0) > 12.0:
        return "mouvement multi-jours déjà trop avancé"
    if number(s4h.get("dist8high"), -99.0) < -4.0:
        return "structure 4 h trop éloignée du sommet"

    for label, summary in (("5 min", s5), ("15 min", s15), ("1 h", s1h), ("4 h", s4h)):
        last = number(summary.get("last"))
        ema20 = number(summary.get("ema20"))
        if last is None or ema20 is None or last < ema20:
            return f"prix sous EMA20 en {label}"

    btc_reason = btc_rejection_reason(live_payload)
    if btc_reason:
        return btc_reason

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
    payload: dict[str, Any], live_payload: dict[str, Any], state: dict[str, Any], now_ts: float
) -> tuple[list[dict[str, Any]], dict[str, str]]:
    accepted: list[dict[str, Any]] = []
    rejected: dict[str, str] = {}
    rows = payload.get("watch") or []
    for row in rows:
        if not isinstance(row, dict):
            continue
        reason = candidate_rejection_reason(row, payload, live_payload, state, now_ts)
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
        "BITVAVO — SIGNAL D'ACHAT TECHNIQUE CONFIRMÉ",
        f"Snapshot : {snapshot_label(payload.get('generated_at_utc'))}",
        "Décision du filtre : ACHAT POTENTIEL À VALIDER.",
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
            "Action : vérifier le graphique Bitvavo puis lancer le scan ChatGPT pour valider le point d'entrée, le TP et le SL.",
            "⚠️ Un signal automatisé n'est jamais une garantie de hausse.",
        ]
    )

    message = EmailMessage()
    message["Subject"] = f"🟢 Bitvavo ACHAT POTENTIEL — {first_market} {first_score:.2f}/10{extra}"
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
    candidates, rejected = select_candidates(payload, live_payload, state, now_ts)
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

    label = "test" if test_mode else "BUY_READY:" + ", ".join(row["market"] for row in candidates)
    print(f"EMAIL_ALERT_SENT recipient={recipient} mode={label}")
    write_job_summary(f"✅ E-mail envoyé à `{recipient}` ({label}).")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print(f"EMAIL_ALERT_ERROR {error}", file=sys.stderr)
        sys.exit(1)
