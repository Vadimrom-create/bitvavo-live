# Public universe coverage — 2026-09-16

Base: integration `f8925b02626925cef91075f8460e0f8772ebc197`.
No pilot enrollment, private account access, orders or alert delivery is part of this experiment.

## Measured cause

The original real CI scan `20260915T230621Z-ba404415` contains 429 EUR markets,
858 diagnostic candle consumptions and zero API errors or abandoned enrichments.
All 429 responses in each timeframe have at least 25 closed candles. The strict
last-25 continuity test rejects 410 markets in 5m and 364 in 15m. Thus the health
counts 19 and 65 are **continuous candle series**, not markets queried. After
also checking freshness, only 18 and 60 respectively remain usable. Missing
latest closed periods overlap the gap category (305 and 220 respectively).

The diagnostic phase used 468 new HTTP responses and 390 cached responses, in
approximately 39.1 seconds. The 120-second deadline did not cause these rejects.
No request was lost to timeout, retry exhaustion, rate limiting or the deadline.
The complete pipeline has 1553 successful HTTP responses and 2038 consumptions.

Original artifact: Actions run 35034098945, artifact 10422254209;
ZIP SHA256 `5e1fedc117b836ca9233f828e823c647e1d3db951aef7e1ddfdd0f351961e6f2`.

## Native simultaneous-cutoff measurement

Actions run 35133575537, diagnostic commit `4777dcb4ad969b405a7beccfbeb4f4d9fafe8837`.
Reference 2026-09-16T18:18:41.825223Z. 430 current EUR markets (TREAD-EUR added).
All requests use the same fixed end boundary; response availability remains later
than that boundary and is recorded. This is an acquisition experiment, not a
historically available decision or prospective pilot observation.

| Timeframe | Queried | Responses | >=25 closed bars | Last 25 continuous | Continuous and latest present |
|---|---:|---:|---:|---:|---:|
| 5m | 430 | 430 | 430 | 26 | 26 |
| 15m | 430 | 430 | 429 | 57 | 57 |
| 30m | 430 | 430 | 429 | 91 | 91 |
| 1h | 430 | 430 | 427 | 148 | 148 |

Primary disjoint rejection counts: source gaps 404/372/338/279; short series
0/1/1/3. One HTTP 500 on NOT-EUR recovered; no final collection failures or 429s.
1720 candle responses plus five initial public responses, 1726 HTTP attempts;
143.67 seconds with 8 workers and 12 requests/second. 1439 candle requests began
within the first 120 seconds and 281 afterwards; none was abandoned. Four
timeframes do not fit a cold 120-second budget at this pacing. The production
path retains two timeframes and its existing pacing/budget; increasing that
budget would not repair source gaps.

## Correction and alternatives

Bitvavo documents no candle for an interval with no trades:
https://docs.bitvavo.com/docs/rest-api/get-candlestick-data/
Rate weights and reset headers remain respected:
https://docs.bitvavo.com/docs/rate-limits/

* Adaptive native timeframe: useful as an additional contextual diagnostic, but
  even 1h covers only 148/430 here; replacing 5m would lose early information.
  No adaptive series is substituted into V4 or DL.
* Trades: an independent check can help investigate source anomalies; a finite
  trade page cannot prove completeness of an arbitrary past interval. No
  reconstructed history from incomplete trades is introduced.
* Filling OHLCV: rejected for active calculations. A zero-volume carry-forward
  would change indicators and require a new input policy and independent tests.
* Implemented: fresh bulk ticker **and** book collection for the entire universe,
  independent of optional candle-enrichment deadlines. A full market watch shows
  last trade price (not assumed recent), 24h change/volume, current bid/ask and
  spread, source IDs/timestamps, and explicit gaps in a 25-period calendar grid.
  Missing slots contain no OHLCV. Absence within returned coverage is inferred
  as no trade under the API contract, not independently proven. Before the first
  returned candle, absence is UNKNOWN; failed collection never implies no trade.

`universe_surveillance.json` is bound to its scan, immutable journal and sealed
publication manifest, and exposed in the public feed. Each market is either
`PUBLIC_MARKET_WATCH` or `PUBLIC_SNAPSHOT_UNAVAILABLE` with actual reasons.
NaN, infinity, invalid/crossed book and stale public responses are rejected.
The strict candle and trading capabilities are preserved and reported separately.
No watch-only market becomes an active buy or gains a fabricated fixed-period
indicator. This fixes the universe surveillance blind spot, not sparse-market
trading eligibility or a claim of improved strategy recall.

Applying this representation to the above real measurement gives 430/430 public
market watches, zero exclusions, without changing any source candle.

## Identity, invariants and rollback

Raw trading inputs remain `CORRECTED_INPUTS_V1`. The additional non-trading
representation explicitly identifies `SOURCE_ABSENCE_GRID_V1` and the observer
`PUBLIC_SPARSE_WATCH_V1`. It has no route to V4/DL1/DL2 inputs or active alerts.
Frozen scoring, all four decision/execution/evaluation identities, historical
journals, and the pinned monitoring release remain unchanged. Raw slots are
never written as candles in the historical index or used as outcome labels.

Tests cover holes, short/empty sources, explicit collection failures, zero
enrichment budget with complete bulk watch, invalid/stale quotes and no active
route. The existing full suite and exact pipeline replay are required before
publication. A real corrected public CI scan must confirm full watch coverage.

Rollback: revert the additive watch producer/manifest/report integration only;
preserve all archives already written and their original identities. No historical
rewrite, retuning, main merge or monitoring deployment accompanies this work.
