#!/usr/bin/env python3
"""Join public historical book observations to machine signals, without fills.

Identifies POST-decision evidence explicitly. A historical executable book
snapshot is not a historical limit-order fill, even with sufficient depth.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path


OBS_PATTERN = re.compile(r"^observation_[a-f0-9]{32}$")


def _number(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        return None
    x = float(x)
    return x if math.isfinite(x) else None


def _empty(status):
    return {
        "book_observation_status": status,
        "book_available_at_utc": None,
        "book_vs_decision_seconds": None,
        "book_was_known_at_decision": False,
        "best_bid_eur": None,
        "best_ask_eur": None,
        "spread_pct": None,
        "stake_estimates": None,
        "actual_fill_proven": False,
    }


def join_one(row, root):
    obs_id = row.get("execution_observation_id")
    if not isinstance(obs_id, str) or not OBS_PATTERN.fullmatch(obs_id):
        return _empty("MISSING_OR_INVALID_OBSERVATION_REFERENCE")
    path = root / (obs_id + ".json")
    if not path.is_file():
        return _empty("OBSERVATION_FILE_UNAVAILABLE")
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return _empty("INVALID_OBSERVATION_DATA")
    if not isinstance(record, dict):
        return _empty("INVALID_OBSERVATION_DATA")
    ids = (("observation_id", obs_id), ("decision_id", row.get("decision_id")),
           ("signal_id", row.get("signal_id")), ("market", row.get("market")))
    if any(record.get(k) != v for k, v in ids):
        return _empty("OBSERVATION_IDENTITY_MISMATCH")
    costs = record.get("execution_costs")
    if not isinstance(costs, dict):
        return _empty("COST_EVIDENCE_MISSING")
    available = _number(costs.get("available_at_ts"))
    decision = _number(row.get("observation_ts"))
    bid = _number(costs.get("best_bid_eur"))
    ask = _number(costs.get("best_ask_eur"))
    spread = _number(costs.get("spread"))
    if (available is None or decision is None or available < 0
            or bid is None or ask is None or bid <= 0 or ask <= 0 or bid > ask
            or spread is None or spread < 0):
        return _empty("INVALID_BOOK_QUOTE_OR_TIMESTAMP")
    joined = {
        "book_observation_status": "MATCHED_PUBLIC_BOOK_ESTIMATE",
        "book_available_at_utc": datetime.fromtimestamp(available, timezone.utc).isoformat(),
        "book_vs_decision_seconds": round(available - decision, 4),
        "book_was_known_at_decision": available <= decision,
        "best_bid_eur": bid,
        "best_ask_eur": ask,
        "spread_pct": round(100 * spread, 5),
        "stake_estimates": {},
        "actual_fill_proven": False,
    }
    sizes = costs.get("sizes")
    if not isinstance(sizes, dict):
        joined["book_observation_status"] = "MATCHED_BUT_COST_SIZES_MISSING"
        joined["stake_estimates"] = None
        return joined
    for stake in ("100", "150"):
        sample = sizes.get(stake)
        if not isinstance(sample, dict):
            joined["stake_estimates"][stake] = None
            continue
        entry = sample.get("entry")
        sell = sample.get("immediate_exit_estimate")
        entry = entry if isinstance(entry, dict) else {}
        sell = sell if isinstance(sell, dict) else {}
        valid_entry = entry.get("covered") is True
        valid_exit = sell.get("covered") is True
        joined["stake_estimates"][stake] = {
            "entry_book_covered": valid_entry,
            "same_snapshot_exit_book_covered": valid_exit,
            "entry_vwap_eur_est": _number(entry.get("vwap_eur")) if valid_entry else None,
            "same_snapshot_exit_vwap_eur_est": _number(sell.get("vwap_eur")) if valid_exit else None,
            "roundtrip_adverse_cost_eur_est": _number(sample.get("roundtrip_adverse_cost_eur_est"))
                if valid_entry and valid_exit else None,
            "evidence_class": "SAME_SNAPSHOT_BOOK_ESTIMATE_NOT_FUTURE_FILL",
        }
    return joined


def enrich_machine_ledger(source, observation_dir):
    if not isinstance(source, dict) or source.get("schema") != "solaire_economic_machine_event_ledger_v1":
        raise ValueError("wrong machine event ledger schema")
    if not isinstance(source.get("records"), list):
        raise ValueError("event ledger records missing")
    stats = {}
    enriched = []
    for row in source["records"]:
        if row.get("execution_fill_status") != "UNKNOWN_NOT_PROVEN":
            raise ValueError("cannot enrich rows which already claim fills")
        next_row = dict(row)
        book = join_one(row, Path(observation_dir))
        state = book["book_observation_status"]
        stats[state] = stats.get(state, 0) + 1
        next_row["historical_book_evidence"] = book
        enriched.append(next_row)
    return {
        **{k: v for k, v in source.items() if k not in ("records",)},
        "schema": "solaire_economic_machine_book_join_v1",
        "records": enriched,
        "books_by_status": stats,
        "matched_book_count": stats.get("MATCHED_PUBLIC_BOOK_ESTIMATE", 0),
        "historical_fills_verified": 0,
        "portfolio_real_pnl_eur": None,
        "book_join_note": "Matching 100/150 EUR snapshot quotes model immediate liquidity only; never claim filled trades.",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", default="/tmp/solaire-machine-economic-ledger.json")
    p.add_argument("--observations-dir", default="execution_observations")
    p.add_argument("--output", help="Output JSON; otherwise stdout")
    args = p.parse_args()
    try:
        source = json.loads(Path(args.source).read_text(encoding="utf-8"))
        result = enrich_machine_ledger(source, args.observations_dir)
        value = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        if args.output:
            Path(args.output).write_text(value, encoding="utf-8")
        else:
            print(value, end="")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        p.exit(2, f"book join refused: {exc}\n")


if __name__ == "__main__":
    main()
