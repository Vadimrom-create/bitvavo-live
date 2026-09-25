from scripts.send_production_buy_alert import subject_for, body_for
from research.production_journal import record_cycle

def _validated(market, score=8.0):
    return {
        "row": {
            "market": market,
            "signal_score": score,
            "signal_phase": "FIRST_CONFIRMATION",
            "last": 1.0,
            "episode_start_price": 1.0,
            "episode_extension_pct": 0.0,
            "episode_age_seconds": 0.0,
            "context": {},
            "acceleration": {
                "state": "CONFIRMED_ACCELERATION",
                "evidence_count": 4,
                "confirmation_scope": "MULTI_TIMEFRAME",
                "timeframe_confirmation_15m": True,
                "components": {"confirmation_15m": 7.0},
            },
        },
        "trade": {
            "entry_eur": 1.01,
            "stop_eur": 0.95,
            "tp1_eur": 1.13,
            "tp2_eur": 1.19,
            "profit_alert_eur": 1.13,
            "runner_reference_eur": 1.19,
            "profit_management_policy": "ALERT_PARTIAL_THEN_RUNNER",
            "stake_eur": 100.0,
            "theoretical_loss_eur": 6.0,
            "stop_distance_pct": 5.94,
        },
        "price_drift_pct": 1.0,
        "spread_pct": 0.2,
        "structural_range_15m_pct": 7.0,
        "prior_thesis_status": "NO_TRACKED_PRIOR_BUY_THESIS",
    }

def test_multi_candidate_email_is_single_consolidated_action():
    selected=[_validated("AAA-EUR"),_validated("BBB-EUR")]
    subject=subject_for(selected)
    body=body_for(selected)
    assert subject.startswith("ACHÈTE — 2 candidats Solaire")
    assert "AAA-EUR" in subject and "BBB-EUR" in subject
    assert "Marché : AAA-EUR" in body
    assert "Marché : BBB-EUR" in body
    assert "2 signaux Solaire validés" in body
    assert "alerte/réévaluation" in body
    assert "ne pas liquider 100 %" in body

def test_journal_records_every_delivery_in_consolidated_email():
    payload={
        "generated_at_utc":"2026-09-22T06:30:00+00:00",
        "watch":[
            {"market":"AAA-EUR","last":1.0,"signal_score":8.0,"context":{}},
            {"market":"BBB-EUR","last":2.0,"signal_score":7.5,"context":{}},
        ],
    }
    alert={
        "checked_at_utc":"2026-09-22T06:31:00+00:00",
        "email":"DELIVERY_COMPLETED",
        "market":"AAA-EUR",
        "deliveries":[
            {"market":"AAA-EUR","entry_eur":1.01,"stop_eur":0.95,"tp1_eur":1.13,"tp2_eur":1.19,"stake_eur":100.0,"structural_range_15m_pct":7.0,"stop_distance_pct":5.94},
            {"market":"BBB-EUR","entry_eur":2.01,"stop_eur":1.90,"tp1_eur":2.23,"tp2_eur":2.34,"stake_eur":100.0,"structural_range_15m_pct":6.5,"stop_distance_pct":5.47},
        ],
        "rejections":[],
    }
    journal=record_cycle(payload,alert,{})
    buys=[e for e in journal["entries"] if e["decision_type"]=="BUY_SENT"]
    assert [e["market"] for e in buys]==["AAA-EUR","BBB-EUR"]
