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



def test_neutral_official_chatter_does_not_open_watch():
    original_fetch = news._fetch_source
    original_official = news._collect_official_items
    try:
        news._fetch_source = lambda source: (source[0], source[2], source[3], [], None)
        news._collect_official_items = lambda registry, now_ts: (
            [{
                "id": "x-neutral",
                "source": "OFFICIAL_X:@ether_fi",
                "source_kind": "official_project",
                "source_weight": 1.30,
                "title": "Join our community call tomorrow",
                "description": "",
                "url": "https://x.com/ether_fi/status/2",
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
    assert signal["direction"] == "NEUTRAL"
    assert signal["watch_trigger"] is False


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


def test_official_imminent_teaser_opens_catalyst_prewatch_before_quant():
    original_fetch = news._fetch_source
    original_official = news._collect_official_items
    try:
        news._fetch_source = lambda source: (source[0], source[2], source[3], [], None)
        news._collect_official_items = lambda registry, now_ts: (
            [{
                "id": "x-ethfi-teaser",
                "source": "OFFICIAL_X:@ether_fi",
                "source_kind": "official_project",
                "source_weight": 1.30,
                "title": "Major stablecoin launch tomorrow at 14:00 UTC — save the date",
                "description": "",
                "url": "https://x.com/ether_fi/status/teaser",
                "published_at_utc": "2026-10-05T12:00:00+00:00",
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
    catalyst = signal["catalyst"]
    assert catalyst["prewatch_trigger"] is True
    assert catalyst["level"] == 3
    assert catalyst["label"] == "IMMINENT"
    assert catalyst["speculative_review"] is True
    assert signal["watch_trigger"] is False

    obs = {
        "market": "ETHFI-EUR",
        "price_eur": 0.66,
        "change_24h_pct": 0.1,
        "quote_volume_24h_eur": 250000,
        "data_quality": _quality(),
        "acceleration": {
            "state": "NO_ACCELERATION",
            "score": 1.0,
            "evidence_count": 0,
        },
        "news": signal,
    }
    payload = build_alert_payload([obs], "2026-10-05T12:01:40+00:00", {})
    assert payload["watch"] == []
    assert payload["news_watch"] == []
    assert payload["catalyst_prewatch"][0]["market"] == "ETHFI-EUR"
    assert payload["catalyst_prewatch"][0]["signal_state"] == "CATALYST_PREWATCH_IMMINENT"
    assert payload["catalyst_prewatch"][0]["signal_source"] == "CATALYST_PREWATCH"


def test_generic_official_calendar_chatter_does_not_open_catalyst_prewatch():
    signal = news._catalyst_signal(
        "Join our community call tomorrow at 14:00 UTC",
        age_seconds=60,
        source_weight=1.3,
        official_direct=True,
    )
    assert signal is None


def test_short_ticker_and_project_substring_do_not_hijack_unrelated_news():
    original_fetch = news._fetch_source
    original_official = news._collect_official_items
    try:
        def fake_fetch(source):
            name, _, weight, kind = source
            return (
                name,
                weight,
                kind,
                [{
                    "id": "etherfi-media",
                    "source": name,
                    "title": "Ether.fi lance son stablecoin avec l'infrastructure d'Ethena",
                    "description": "",
                    "url": "https://example.test/etherfi",
                    "published_at_utc": "2026-10-06T17:00:00+00:00",
                    "published_ts": 1000.0,
                }],
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
            [
                {"market": "C-EUR", "base": "C"},
                {"market": "THE-EUR", "base": "THE"},
                {"market": "ETHFI-EUR", "base": "ETHFI"},
                {"market": "ENA-EUR", "base": "ENA"},
            ],
            now_ts=1100.0,
            asset_rows=[
                {"symbol": "C", "name": "C"},
                {"symbol": "THE", "name": "Thena"},
                {"symbol": "ETHFI", "name": "Ether.fi"},
                {"symbol": "ENA", "name": "Ethena"},
            ],
        )
    finally:
        news._fetch_source = original_fetch
        news._collect_official_items = original_official

    assert "C-EUR" not in context["markets"]
    assert "THE-EUR" not in context["markets"]
    assert "ETHFI-EUR" in context["markets"]
    assert "ENA-EUR" in context["markets"]


def test_official_html_future_teaser_survives_anchor_filter():
    payload = b"""
    <html><body>
      <a href="/announcement">Major stablecoin launch tomorrow at 14:00 UTC - save the date</a>
      <a href="/community">Join our community call tomorrow</a>
    </body></html>
    """
    rows = news._material_anchor_titles(payload)
    titles = [title for _, title in rows]
    assert "Major stablecoin launch tomorrow at 14:00 UTC - save the date" in titles
    assert "Join our community call tomorrow" not in titles
