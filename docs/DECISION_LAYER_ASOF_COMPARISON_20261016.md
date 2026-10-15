# Decision Layer vs Solaire direct — as-of evidence (research only)

Issue #134, 16 October 2026. No production scanner changes, orders, thresholds, stops, wallet data, secrets or ChatGPT transcripts.

## Question answered

For every retained public machine event (BUY_SENT or REJECTED), retrieve the most recently generated **earlier** Decision Layer shadow state. Require the same Bitvavo market and an age at most 3600 seconds. Do not mistake missing, stale or corrupt shadows for DL rejections.

This is **descriptive alignment, not a paired strategy backtest**: the policies score different upstream inputs (DL on V4; direct on acceleration). Production decision_ts is sender start, not completed email delivery. DL generated_at_utc establishes that a snapshot was generated, **not verified published or available** to a consumer before the signal. Never claim causal impact from this join alone.

## Offline run

    python -m unittest discover -s tests -p 'test_compare_direct_decision_shadow.py' -v
    python scripts/compare_direct_decision_shadow.py --machine production_direct_decision_journal.json --decision-history decision_history --max-age-seconds 3600 --output /tmp/dl-asof-evidence.json

PR-only CI emits a temporary public-research artifact, without publishing private decisions or altering main. Rows contain decision IDs, market, machine state, shadow state, archive and age. Every fill and PnL remains unknown. Report denominators for *all* machine events, matched events, and BUY_SENT events separately.

## Remaining gates before an economic conclusion

1. Independently verify DL publication/availability times. A generated-before-signal snapshot alone is insufficient for strong causal evidence.
2. Pair identical machine candidate episodes using frozen timestamps, same capital, stops/targets, entry and exit book prices, fees, slippage, bid depth and stop-first ambiguous bars. Explicitly report missing histories.
3. Compare DIRECT and DIRECT + DL at exactly the same candidate universe and dates; report rejected winners AND avoided losers.
4. Compare 24/48/72-hour and 7-day net capital-constrained results only for adequately matured independent episodes with valid fill hypotheses and a reserved out-of-sample window.
5. Study 6/12/24-month price-memory zones as a **separate shadow variable**: FET's rebound is a hypothesis, not proof of systematic mean reversion.

Do not reinstate the Decision Layer as a production veto without separately approved prospective evidence.
