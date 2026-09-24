# Solaire V3 — prospective laboratory

Solaire V3 is a research shadow deployed beside the frozen Solaire V2 decision path. It does **not** replace V2 alerts, send its own BUY email, or submit orders. Its purpose is to test the original strategic hypotheses plus the entry-timing and persistent-thesis extensions before the longer Astra challenger is fully deployed.

## Frozen comparator

The immutable V2 code reference is commit `34b042121bb8425b0e4b46e3d1a694d4b1f4ec75`. Runtime JSON files on `main` may continue to evolve; the comparison code reference does not.

## Six axes

1. **Where to look — context and narratives.** Public crypto news, project mentions and sector rotation can create a priority watch before a full V2 quantitative confirmation. Context never creates a BUY by itself. The direction must still be confirmed by market data. News-to-asset resolution covers the complete current Bitvavo EUR universe: tickers come from the neutral universe snapshot, canonical project names are fetched dynamically from Bitvavo `/assets`, and the small legacy alias table is supplemental only—not a whitelist. RSS/aggregated news is matched against that dynamic map, so any listed asset can open a news prewatch.

2. **How long to stay — adaptive horizons.** The evaluation grid is 4h, 24h, 48h, 72h, 96h, 7d, 14d and 30d. Opportunities are provisionally labelled WATCH / TACTICAL / SWING / POSITION and can be reclassified as evidence changes. The +10%/24h outcome remains diagnostic, not the economic objective.

3. **Where to place capital — opportunity cost.** A standardized shadow portfolio (EUR 2,400 reference capital, EUR 100 reference position, max three positions) records KEEP/OPEN/ROTATE/CLOSE logic. It is **not** the user's account balance and does not trade. Rotation requires a materially higher forward opportunity score, so churn is measurable.

4. **Where/when price discovery starts — global market.** A batch first-stage scan now covers the complete Bitvavo symbol universe on available Binance, Bybit and OKX spot tickers every cycle and compares each venue with its prior V3 cycle. External sparks can therefore create a watch before Bitvavo itself accelerates. A bounded second-stage candle check then uses Binance, Bybit, OKX, Coinbase and Kraken for richer 20m/60m confirmation. Expensive second-stage work, derivatives, long-trend profiles and execution checks use rotating fair queues rather than fixed top-N slices, so no eligible market can be starved indefinitely. Bitvavo remains the execution-quality reference.

5. **When to enter — entry-timing laboratory.** The raw `ENTRY_READY_SHADOW` remains the neutral baseline. V3 also measures a 30-minute persistence path and a pullback/reclaim path. These variants never affect V2, emails, orders or the baseline capital-rotation shadow.

6. **Opportunity is not entry — persistent thesis layer.** A strong prewatch context can seed a thesis **before** a full entry trigger, and a fresh opportunity can also open one. The thesis survives disappearance of the short acceleration and tracks continuation, pullback, reclaim/re-entry, invalidation and expiry independently from the short episode. Long-horizon profiling is refreshed through a fair rotating queue. A credible `REENTRY_READY_THESIS` is promoted back into the main V3 candidate stream and its latest execution state is forwarded to V3.1; a temporary R:R/spread/structure failure remains a retryable WAIT rather than causing the opportunity to disappear.

## V3 entry path

A V3-only early entry hypothesis requires:
- multiple early quantitative facts, **and**
- independent positive context (positive/material news catalyst, static or dynamic full-universe rotation context, or cross-exchange confirmation).

News attention and entry direction are separated: negative catalysts can create a watch and an explicit penalty but do not count as bullish entry confirmation.

The frozen V2 confirmed path is also evaluated as a common reference.

Every hypothetical entry is then revalidated on Bitvavo:
- EUR-market availability,
- 24h quote liquidity,
- 25-level ask-book walk for the EUR 100 reference size,
- spread,
- visible-depth slippage,
- valid 15m structure,
- structural invalidation and stop distance.

Unlike V2, a spread/liquidity/structure failure is a **reversible WAITING state**, not a terminally handled episode. V3 deliberately does not require V2's >=6% consolidation-range gate; the research hypothesis is that earlier contextual focus can preserve better entry geometry.

## Measurement hardening

V3 measurement is cumulative from a fixed T0 and does not age trades out of a rolling cohort. The evaluator:
- sorts bars chronologically;
- excludes the decision-containing bar;
- requires complete start and end coverage for each horizon;
- never calls an immature horizon complete;
- keeps missing evidence missing;
- uses the same strict method for V3 and the V2 reference.

Estimated net close returns use a fixed 0.70% round-trip cost convention for comparison. These are not actual fills.

## Outputs

- `production_universe_snapshot.json`: neutral export from the exact same Bitvavo scan used by V2.
- `solaire_v3_candidates.json`: current prioritized watch and execution diagnostics; its selection semantics remain unchanged for V3.1.
- `solaire_v3_theses.json`: isolated persistent Opportunity/Entry research stream, including long-trend context and thesis-only re-entry execution checks.
- `solaire_v3_state.json`: reversible short-episode state plus persistent opportunity-thesis state.
- `solaire_v3_journal.json`: cumulative prospective V3 events.
- `solaire_v2_frozen_benchmark_journal.json`: prospective V2 detection reference.
- `solaire_v3_rotation_state.json`: standardized paper capital-allocation shadow.
- `solaire_v2_reference_outcomes.json`: post-T0 V2 BUY outcomes under the strict evaluator.
- `solaire_v3_comparison.json`: same-horizon V2/V3 comparison and context lead times.
- `solaire_v3_status.json`, `solaire_v3_evaluation_status.json`: health/status.

## Deliberate limitations

GitHub Actions remains a scheduled, non-continuous runtime. Astra measured a much slower effective cadence than the nominal five-minute cron. V3 therefore tests whether these research axes add value **despite** that limitation; it does not claim to solve latency. Astra remains the independent continuous-architecture challenger.

External feeds are best-effort and non-blocking. A missing external venue/news source cannot become positive evidence. News mapping is full-universe and uses title-level entity resolution plus structured provider tickers to avoid ordinary-word collisions. Canonical project names are never shortened into generic words. The source set includes media/aggregator feeds plus official Binance announcements, Coinbase/Kraken feeds and first-seen monitoring of official Bybit/OKX announcement pages. Every event is classified by catalyst type/direction/materiality before it can support an entry. No live order is submitted by V3.

Every new prospective event is stamped with the current V3 architecture version and runtime commit. Legacy journal events are explicitly marked as pre-versioning observations so pre- and post-change performance cannot be silently pooled.
