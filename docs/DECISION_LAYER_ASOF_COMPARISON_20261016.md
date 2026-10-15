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

## First empirical cadence audit — 16 October checkpoint

Research workflow [#38819050737](https://github.com/Vadimrom-create/bitvavo-live/actions/runs/38819050737) **SUCCESS**; regression tests and both archive studies passed. Data are a moving retention-limited snapshot, not a frozen 30-day strategy cohort.

- **1,766** public machine decisions, including **497 BUY_SENT**, **1,269 REJECTED**; **2,086** readable historical DL snapshots.
- 15-min (900 s) maximal DL age: **24 / 497 BUY_SENT matched (4.83%)**.
- 30-min (1800 s): **41 / 497 (8.25%)**.
- 60-min (3600 s): **89 / 497 (17.91%)**; all machine events 308 / 1766 (17.44%).
- 120-min (7200 s): **212 / 497 (42.66%)**; all machine events 671 / 1766 (38.00%).
- Full UTC day 2026-10-14: **9** archived DL generations for **96 nominal quarter-hour slots**, median observed gap **178.75 min**, max gap **302.29 min**.
- Partial UTC day 2026-10-15 through last observed generation at 22:12: **6** archived DL generations, median observed gap **278.08 min**, maximum **286.52 min**. Do not compare this partial day to a complete day's 96 slots.

The schedule `7,22,37,52 * * * *` has been configured since at least the October 4 workflow revision. The scheduled runs examined on October 15 passed their tests, pipeline and DL generation steps; the observed omissions are **not currently attributed** to any one GitHub cause. The data establish low *published archive cadence*, not the number or origin of missed cron dispatches. The outcomes do **not** establish an economic benefit of DL. Accepting a 120-minute stale state for 42.66% matching is a sensitivity study, **not an acceptable trading decision latency**.

A prospective synchronous study must timestamp same-cycle context and publication separately, and be isolated from Solaire production. **No promotion or auto-merge.**

## Second empirical experiment — identical frozen V4 scan (16 Oct checkpoint)

PR-only workflow [#38822675635](https://github.com/Vadimrom-create/bitvavo-live/actions/runs/38822675635) **SUCCESS**: 24 synthetic tests passed; recalculated `research/decision_layer.classify` actions agree with all the six archived `decision_history` reports (`frozen_dl_replay_mismatches=0`). The earlier 198 mismatches were a **bug in the research classification of missing V4 profiles**, now corrected with a regression test; they were not policy drift.

Inputs: **6** immutable full-market `history/2026-10-15/*.json.gz` scans, **2,562** observations, same scan IDs and source features for original/recomputed DL and archived V4 acceleration states. Among the **43** V4 `CONFIRMED_ACCELERATION` states: `DL ACHETE_MAINTENANT=0`, `WATCH=36`, `VETO_STRUCTUREL=3`, `PLACE_LIMITE_PASSIVE=2`, `ATTENDS_REPRISE_OU_REENTREE=1`, `DL_UNCLASSIFIABLE_NO_BASELINE=1`.

**What is established**: consistent DL code replay on the same immutable V4 observations and an apparent strictness/timing conflict between V4 acceleration evidence and DL immediate-buy classification. No policy mismatch in this selected day.

**What is NOT established**: these are **not modern DIRECT BUY_SENT signals**. V4 acceleration is *legacy upstream evidence* and its `CONFIRMED_ACCELERATION` does not guarantee a safe fill or a BUY from the independent direct scanner. Original DL generation occurs after its source scan; archival replay is not verified delivery-time classification. No matched DIRECT vs DL PnL, no actual fills, and no reason to relax safety vetoes or change production.

Remaining target for #134: prospective same-cycle independent source capture, causal as-of timestamp and immutable direct event IDs; evaluate avoided losers vs forgone winners after stop-first, spread, true bid/ask liquidity, fees, capital concurrency and matured 24/48/72h. Preserve separate 6/12/24-month price-memory research to avoid FET hindsight.
