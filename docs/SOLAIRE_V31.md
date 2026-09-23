# Solaire V3.1 — economic-selection challenger

V3.1 is a prospective shadow challenger launched after the NIL / APE / FORM observation. It does **not** alter the frozen V3 detector. It receives the exact V3 candidate output and tests only whether a different ranking, entry-quality and sizing layer improves economic outcomes.

## Frozen comparator

V3 detector/ranking code reference: `2b0a5b25173e8ac5dd67625f80755f26acbedabf`.

The existing V3 path remains unchanged. V3.1 sends no email and no order.

## Pre-registered hypotheses

The motivating observation is treated as an adversarial case, not training data for prospective performance:

- NIL was detected by V2 before a large continuation;
- APE and FORM were later executed and stopped;
- a higher legacy signal score did not guarantee a better economic outcome.

V3.1 therefore tests the following hypotheses prospectively:

1. **Legacy score is not authority.** V2 score and V3 opportunity score are logged but have zero weight in the V3.1 economic score.
2. **Persistence matters.** 20-minute, 1-hour and 4-hour continuation and acceleration are weighted explicitly.
3. **Relative strength matters.** 1-hour and especially 4-hour relative strength are separated from raw market direction.
4. **Contradiction is information.** Negative 4-hour trend, negative 4-hour relative strength, short-term reversal and late extension create explicit penalties.
5. **Context is capped.** News/narrative/external context can support a move but cannot dominate price/participation evidence.
6. **Execution quality belongs in ranking.** Spread, visible-depth slippage, structural stop geometry and net R:R affect the final score.
7. **Sizing is risk-based.** Qualified positions receive a theoretical stake from a score-aware risk budget, stop distance and liquidity cap.

## Isolation

V3.1 performs no additional market discovery and no extra external-venue calls. It consumes:

- `production_universe_snapshot.json`
- `solaire_v3_candidates.json`

This avoids slowing the production scan or changing what V3 sees.

Only candidates already execution-checked by V3 can become V3.1-qualified entries. Candidates not checked by V3 are reported as unchecked rather than silently treated as failures.

## Prospective measurement

First-cycle observations are left-censored so that pre-existing setups do not become fake prospective discoveries. From V3.1 T0 onward, every execution-ready V3 candidate is recorded once per episode as either:

- `V31_QUALIFIED_ENTRY`
- `V31_REJECTED_READY`

Both cohorts are evaluated on the same strict horizons as V3: 4h, 24h, 48h, 72h, 96h, 7d, 14d and 30d. This makes it possible to test whether V3.1 rejects more losers than winners and whether higher V3.1 scores are actually associated with better outcomes.

NIL / APE / FORM are excluded from V3.1 prospective performance because they occurred before V3.1 T0.

## Shadow allocation

Reference capital remains EUR 2,400 for comparability with V3. Maximum open positions: 3. The shadow can rotate only when a new qualified candidate exceeds the weakest open position by at least 1.25 economic-score points.

No real account state, email or order is affected.
