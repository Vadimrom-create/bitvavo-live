from research import production_news as news
from research.production_gate import build_alert_payload


def _quality():
    return {"ok": True, "reasons": []}


def test_ethfi_news_opens_watch_before_quant():
    original = news._fetch_source
    try:
        def fake_fetch(source):
            name, _, weight = source
            return (
                name,
                weight,
                [
                    {
                        "id": "ethfi-stablecoin",
                        "source": name,
                        "title": "Ether.fi lance son stablecoin avec l'infrastructure d'Ethena",
                        "description": "Le protocole lance ether.fi USD, powered by Ethena.",
                        "url": "https://example.test/ethfi",
                        "published_at_utc": "2026-10-06T19:00:00+00:00",
                        "published_ts": 1000.0,
                    }
                ],
                None,
            )
        news._fetch_source = fake_fetch
        context = news.collect_news_context(
            [{"market": "ETHFI-EUR", "base": "ETHFI"}],
            now_ts=1100.0,
        )
    finally:
        news._fetch_source = original

    signal = context["markets"]["ETHFI-EUR"]
    assert signal["watch_trigger"] is True
    assert signal["direction"] == "POSITIVE"
    assert signal["score"] >= 8.0

    obs = {
        "market": "ETHFI-EUR",
        "price_eur": 0.69,
        "change_24h_pct": 0.2,
        "quote_volume_24h_eur": 350000,
        "data_quality": _quality(),
        "acceleration": {
            "state": "NO_ACCELERATION",
            "score": 1.0,
            "evidence_count": 0,
        },
        "news": signal,
    }
    payload = build_alert_payload([obs], "2026-10-06T19:01:40+00:00", {})
    assert payload["watch"] == []
    assert payload["news_watch"][0]["market"] == "ETHFI-EUR"
    assert payload["news_watch"][0]["signal_state"] == "NEWS_WATCH_POSITIVE"
    assert payload["news_watch"][0]["signal_source"] == "NEWS"


def test_positive_news_materially_boosts_score_but_cannot_buy_without_confirmation():
    signal = {
        "score": 10.0,
        "direction": "POSITIVE",
        "watch_trigger": True,
        "top": {"title": "Major launch", "source": "TEST"},
    }
    obs = {
        "market": "ETHFI-EUR",
        "price_eur": 0.69,
        "change_24h_pct": 1.0,
        "quote_volume_24h_eur": 350000,
        "data_quality": _quality(),
        "acceleration": {
            "state": "BUILDING_ACCELERATION",
            "score": 5.5,
            "evidence_count": 2,
        },
        "news": signal,
    }
    payload = build_alert_payload([obs], "2026-10-06T19:10:00+00:00", {})
    row = payload["tracking"][0]
    assert row["quant_score"] == 5.5
    assert row["signal_score"] > 6.5
    assert row["signal_source"] == "NEWS_PLUS_DIRECT_ACCELERATION"
    assert payload["watch"] == []


def test_negative_news_can_reduce_long_score_and_block_candidate():
    signal = {
        "score": 10.0,
        "direction": "NEGATIVE",
        "watch_trigger": True,
        "top": {"title": "Protocol exploit", "source": "TEST"},
    }
    obs = {
        "market": "TEST-EUR",
        "price_eur": 1.0,
        "change_24h_pct": 5.0,
        "quote_volume_24h_eur": 500000,
        "data_quality": _quality(),
        "acceleration": {
            "state": "CONFIRMED_ACCELERATION",
            "score": 7.0,
            "evidence_count": 4,
        },
        "news": signal,
    }
    payload = build_alert_payload([obs], "2026-10-06T19:10:00+00:00", {})
    assert payload["tracking"][0]["signal_score"] < 6.5
    assert payload["watch"] == []
