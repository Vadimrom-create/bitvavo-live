from research.official_source_registry import ensure_universe_entries, _resolve_id


def test_registry_covers_every_active_bitvavo_market():
    markets = [
        {"market": "ETHFI-EUR", "base": "ETHFI", "quote": "EUR", "status": "trading"},
        {"market": "AAVE-EUR", "base": "AAVE", "quote": "EUR", "status": "trading"},
        {"market": "SEI-EUR", "base": "SEI", "quote": "EUR", "status": "trading"},
    ]
    assets = [
        {"symbol": "ETHFI", "name": "Ether.fi"},
        {"symbol": "AAVE", "name": "Aave"},
        {"symbol": "SEI", "name": "Sei"},
    ]
    registry = ensure_universe_entries({"markets": {}}, markets, assets)
    assert registry["active_market_count"] == len(markets)
    assert set(registry["markets"]) == {row["market"] for row in markets}
    assert all(registry["markets"][row["market"]]["active_on_bitvavo"] for row in markets)


def test_ethfi_official_override_is_seeded():
    registry = ensure_universe_entries(
        {"markets": {}},
        [{"market": "ETHFI-EUR", "base": "ETHFI"}],
        [{"symbol": "ETHFI", "name": "Ether.fi"}],
    )
    row = registry["markets"]["ETHFI-EUR"]
    assert row["x_handle"] == "ether_fi"
    assert any("ether.fi" in url for url in row["homepage"])
    assert row["discovery_status"] == "VERIFIED_OVERRIDE"


def test_symbol_collision_is_never_guessed():
    rows = [
        {"id": "alpha-one", "symbol": "ABC", "name": "Alpha One"},
        {"id": "alpha-two", "symbol": "ABC", "name": "Alpha Two"},
    ]
    coin_id, method = _resolve_id("ABC", "Unknown Project", rows)
    assert coin_id is None
    assert method == "AMBIGUOUS_SYMBOL"

    coin_id, method = _resolve_id("ABC", "Alpha Two", rows)
    assert coin_id == "alpha-two"
    assert method == "SYMBOL_AND_NAME"
