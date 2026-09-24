# Solaire V3.1 — economic-selection challenger

V3.1 is a prospective shadow challenger launched after the NIL / APE / FORM observation. It does **not** alter the frozen V3 detector. It receives the exact V3 candidate output and tests only whether a different ranking, entry-quality and sizing layer improves economic outcomes.

## Frozen comparator

Historical V3 benchmark reference: `2b0a5b25173e8ac5dd67625f80755f26acbedabf`. This commit is now labelled **benchmark-only**; it is not represented as the live V3 input. Each V3.1 cycle records the actual upstream V3 architecture version and runtime commit. V3.1 sends no email and no order.

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

V3.1 can qualify either the RAW V3 execution path or a persistent-thesis re-entry path forwarded by V3. A re-entry that is temporarily blocked by net R:R, spread, structure or another execution condition remains visible as a retryable wait; it is not discarded. Raw and thesis re-entry decisions are journalled separately even when they occur in the same market episode.

## Prospective measurement

First-cycle observations are left-censored so that pre-existing setups do not become fake prospective discoveries. From V3.1 T0 onward, every execution-ready V3 candidate is recorded once per episode as either:

- `V31_QUALIFIED_ENTRY`
- `V31_REJECTED_READY`

Both cohorts are evaluated on the same strict horizons as V3: 4h, 24h, 48h, 72h, 96h, 7d, 14d and 30d. This makes it possible to test whether V3.1 rejects more losers than winners and whether higher V3.1 scores are actually associated with better outcomes.

NIL / APE / FORM are excluded from V3.1 prospective performance because they occurred before V3.1 T0.

## Shadow allocation

Reference capital remains EUR 2,400 for comparability with V3. Maximum open positions: 3. The shadow can rotate only when a new qualified candidate exceeds the weakest open position by at least 1.25 economic-score points.

No real account state, email or order is affected.


## Timing-factorial extension

V3 later added an independent prospective timing laboratory at commit `0c05e0fbf55b0ff99dae3f10bcfc3411bbee0cc6`. V3.1 keeps its original RAW economic ranking/gate unchanged and now crosses it with the two V3-recorded timing paths:

- `RAW`: original V3.1 behaviour, unchanged;
- `PERSIST_30M`: V3 has already recorded that execution-ready persisted for at least 30 minutes inside its own drift constraints;
- `PULLBACK_RECLAIM`: V3 has already recorded its pullback/reclaim timing condition.

V3.1 does not copy or reimplement the timing thresholds. The upstream V3 timing event is authoritative. This avoids drift between two definitions of the same timing rule.

The prospective comparison is therefore factorial:

| Selection layer | RAW | PERSIST_30M | PULLBACK_RECLAIM |
| --- | --- | --- | --- |
| V3 | measured by V3 | measured by V3 | measured by V3 |
| V3.1 economic gate | measured | measured | measured |

The original V3.1 RAW journal and portfolio remain intact. Two new shadow portfolios are maintained separately:

- `solaire_v31_portfolio_persist30.json`
- `solaire_v31_portfolio_pullback_reclaim.json`

The first timing-extension cycle is left-censored. A timing condition already active when the extension starts cannot be counted as a fresh prospective timing success or open a timing portfolio position.

This extension still sends no email, submits no order, and cannot modify V2 or V3.


## Architecture provenance and catalyst handling

V3.1 uses positive/material news context rather than raw headline count in its context component, and applies an explicit penalty when a strong negative catalyst dominates. It inherits V3's full-universe news/external discovery and dynamic rotation context without maintaining its own discovery whitelist. New V3.1 events are architecture-versioned; legacy events are tagged as pre-versioning observations.
