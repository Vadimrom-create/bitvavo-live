from research import production_news as news
from research.production_gate import build_alert_payload


def _quality():
    return {"ok": True, "reasons": []}


def test_ethfi_news_opens_watch_before_quant():
    original_fetch = news._fetch_source
    original_official = news._collect_official_items
    try:
        def fake_fetch(source):
            name, _, weight, kind = source
            return (
                name,
                weight,
                kind,
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
        news._collect_official_items = lambda registry, now_ts: ([], [], {
            "registered_official_pages": 0,
            "polled_official_pages": 0,
            "registered_x_handles": 0,
            "registry_coverage": {},
        })
        context = news.collect_news_context(
            [{"market": "ETHFI-EUR", "base": "ETHFI"}],
            now_ts=1100.0,
            asset_rows=[{"symbol": "ETHFI", "name": "Ether.fi"}],
        )
    finally:
        news._fetch_source = original_fetch
        news._collect_official_items = original_official

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


def test_official_project_news_has_priority_over_media():
    original_fetch = news._fetch_source
    original_official = news._collect_official_items
    try:
        news._fetch_source = lambda source: (source[0], source[2], source[3], [], None)
        news._collect_official_items = lambda registry, now_ts: (
            [{
                "id": "x-etherfi",
                "source": "OFFICIAL_X:@ether_fi",
                "source_kind": "official_project",
                "source_weight": 1.30,
                "title": "Introducing ether.fi USD, our own stablecoin powered by Ethena",
                "description": "",
                "url": "https://x.com/ether_fi/status/1",
                "published_at_utc": "2026-10-06T12:01:00+00:00",
                "published_ts": 1000.0,
                "direct_markets": ["ETHFI-EUR"],
                "timestamp_semantics": "X_CREATED_AT",
            }],
            [{"source": "X_OFFICIAL", "ok": True}],
            {
                "registered_official_pages": 1,
                "polled_official_pages": 1,
                "registered_x_handles": 1,
                "registry_coverage": {"active_markets": 1, "with_any_official_source": 1},
            },
        )
        context = news.collect_news_context(
            [{"market": "ETHFI-EUR", "base": "ETHFI"}],
            now_ts=1100.0,
            asset_rows=[{"symbol": "ETHFI", "name": "Ether.fi"}],
        )
    finally:
        news._fetch_source = original_fetch
        news._collect_official_items = original_official

    signal = context["markets"]["ETHFI-EUR"]
    assert signal["top"]["source_kind"] == "official_project"
    assert signal["top"]["official_direct_match"] is True
    assert signal["top"]["timestamp_semantics"] == "X_CREATED_AT"
    assert signal["score"] >= news.NEWS_WATCH_MIN


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
