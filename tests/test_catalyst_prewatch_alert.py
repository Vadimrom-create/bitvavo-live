import time

from scripts import send_catalyst_prewatch_alert as alert


def _payload(catalyst_id="cat-1", level=3):
    now = time.time()
    return {
        "generated_at_utc": alert.utc(now),
        "catalyst_prewatch": [{
            "market": "ETHFI-EUR",
            "last": 0.66,
            "change_24h_pct": 0.2,
            "quote_volume_24h_eur": 250000,
            "acceleration": {"state": "NO_ACCELERATION", "score": 1.0, "evidence_count": 0},
            "news": {
                "catalyst": {
                    "level": level,
                    "label": "IMMINENT" if level == 3 else "UPCOMING",
                    "score": 9.0 if level == 3 else 7.1,
                    "direction": "POSITIVE",
                    "prewatch_trigger": True,
                    "top": {
                        "catalyst_id": catalyst_id,
                        "source": "OFFICIAL_X:@ether_fi",
                        "source_role": "PROJECT",
                        "title": "Major stablecoin launch tomorrow at 14:00 UTC",
                    },
                }
            },
        }],
    }, now


def test_new_catalyst_is_alerted_once():
    payload, now = _payload()
    state = {"markets": {}}
    rows = alert.eligible_rows(payload, state, now)
    assert [row["market"] for row in rows] == ["ETHFI-EUR"]

    state = {
        "markets": {
            "ETHFI-EUR": {
                "last_catalyst_id": "cat-1",
                "last_level": 3,
            }
        }
    }
    assert alert.eligible_rows(payload, state, now) == []


def test_level_upgrade_is_alerted_even_for_same_catalyst():
    payload, now = _payload(level=3)
    state = {
        "markets": {
            "ETHFI-EUR": {
                "last_catalyst_id": "cat-1",
                "last_level": 2,
            }
        }
    }
    rows = alert.eligible_rows(payload, state, now)
    assert len(rows) == 1
    assert rows[0]["market"] == "ETHFI-EUR"


def test_stale_payload_is_not_alerted():
    payload, now = _payload()
    payload["generated_at_utc"] = alert.utc(now - alert.MAX_SNAPSHOT_AGE - 60)
    assert alert.eligible_rows(payload, {"markets": {}}, now) == []
