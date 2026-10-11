# Solaire — first finite-capital chronological replay (research only)

Status 11 October 2026: **engine implemented, the full historical economic comparison is NOT READY**. PR #163 / issue #134. No orders, production changes, wallet access or user-private data.

## What has been implemented

- `research/capital_constrained_replay.py`: deterministic, research-only simulation of a **2,300 EUR** cash account, chronological competition between **explicitly declared** model signals, at most ten simultaneous positions, stake 100/150 EUR, without capital reuse or leverage.
- Entry model: starts at the first complete 5-minute bar after BOTH the alert and the historical book become available. Hypothetical limit touch is modeled with adverse slippage, not presented as a filled Bitvavo limit order. A no-touch order is UNFILLED. If stop or target touches in the entry bar and intrabar order is unknowable, the case is **CENSORED**, not a retrospective win.
- Exit model: stop-first if TP and stop are both touched on the same bar, adverse gap/open loss, TP if observable afterwards; otherwise last fully closed bar by horizon. Missing bars mean **CENSORED**, never filled with synthetic prices.
- Default model fee **0.25% each side** and adverse slippage **0.10% each side**. These are assumptions for stress testing, NOT measured historical fills; order-book bid/ask and spread may impose additional costs. Do NOT describe this 0.70%-round-trip default as a verified Bitvavo execution cost.
- Supports 24/48/72/168 hour expiry. The same-timestamp allocation tie break uses ID only, independent of future profitable outcomes.
- Final modeled cash reconciles against modeled trade PnL; maximum drawdown remains `null` because a synchronized mark-to-market history of every open position is not assembled. Even a positive simulation is NOT proof of a historical actual wallet gain.

## Real public data adapters and current blocker

- `scripts/prepare_economic_replay.py` extracts fixed-stake 100/150 EUR **hypothetical** events from actual `BUY_SENT` + market books, preserving evidence IDs and original availability timestamps. Signals with missing or late book evidence become **missing evidence**, not trading losses or machine non-detections. Production BUY_SENT is **neither the historical V4 architecture nor R2**.
- `scripts/run_economic_portfolio_replay.py` gives an explicit **NOT_READY** result with null PnL when no continuous closed 5-minute price bundle is supplied; never substitutes shadow aggregates.
- Input closed candles bundle schema:

```json
{
  "schema": "solaire_closed_5m_candles_bundle_v1",
  "asof_utc": "2026-10-12T00:00:00Z",
  "source_sha256": "<sha256 of the source candle capture>",
  "markets": {
    "EXAMPLE-EUR": [
      {"start_utc": "2026-10-10T00:00:00Z", "open": 0.1, "high": 0.11, "low": 0.09, "close": 0.1}
    ]
  }
}
```

The `source_sha256` MUST match the canonical JSON bytes of `markets` encoded as UTF-8 with `json.dumps(markets, sort_keys=True, separators=(",", ":"), ensure_ascii=False)`. This integrity check prevents silently altered candle arrays, but it **does not authenticate** that the candles came from Bitvavo. Exchange/public collection provenance must be separately retained.

The example is format ONLY, not market evidence. The bundle must come from a real timestamped capture and include every relevant *full* five-minute candle (no data after `asof`). When any predeclared candidate has a missing/incomplete future trajectory, the entire portfolio comparison's PnL is **null**; incomplete cohorts must not be cherry-picked.

```bash
python scripts/build_economic_signal_ledger.py --output /tmp/machine.json
python scripts/enrich_economic_signal_books.py --source /tmp/machine.json --output /tmp/books.json
python scripts/prepare_economic_replay.py --books /tmp/books.json --stake 100 --output /tmp/preflight100.json
python scripts/prepare_economic_replay.py --books /tmp/books.json --stake 150 --output /tmp/preflight150.json
python scripts/run_economic_portfolio_replay.py --books /tmp/books.json --output /tmp/replay_readiness.json
python -m unittest tests.test_capital_constrained_replay tests.test_economic_replay_preflight -v
```

To run when and only when real closed 5m candles are independently provided:

```bash
python scripts/run_economic_portfolio_replay.py --books /tmp/books.json \
  --candles /tmp/closed_candles.json --asof '<same as bundle asof_utc>' \
  --horizon-hours 24 --output /tmp/model_24h.json
```

## Critical remaining steps before an honest V4 / R2 / baseline 2,300 EUR ranking

1. Time-stamped retention of **full closed price paths**, identified by market and period, with provenance, gaps and delistings. Old historical outcomes lacking gaps are NOT equivalent to verified paths.
2. Same opportunity set and same entry window for V4, R2 and simple reference, with entry/execution books, stable frozen policy versions and no hindsight selection; selectors without historical book proof remain `NON_COMPARABLE`.
3. Fee/spread/slippage stress and latency sensitivity, real archived fills separately where permitted and private.
4. Full five-minute portfolio mark-to-market for credible max drawdown and capital at risk. Until this exists `max_drawdown_eur=null`.
5. Out-of-sample, regimes and uncertainty; exit-policy selection must not use the same data twice to optimize and validate.

**Important economic interpretation:** the already verified 223 historical BUY_SENT book captures had a median same-snapshot adverse round-trip estimate of about 0.94% at 100 EUR and 0.95% at 150 EUR, which was calculated on *historical books*, not on filled orders or future exit-time liquidity. This should be used as a stress diagnostic, not simply added to a model that might already include overlapping fee/spread assumptions.

No change to production BUY gate, Solaire thresholds, stops, execution or private storage; no PR merge.
