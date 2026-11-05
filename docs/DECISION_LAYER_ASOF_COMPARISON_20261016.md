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


## Third experiment — bounded real DIRECT buy signals and retrospective price references (16 October, 09:00 UTC)

[PR-only workflow #38877402095 — SUCCESS](https://github.com/Vadimrom-create/bitvavo-live/actions/runs/38877402095) with **38 passing synthetic regression tests**, archive and source alignment, and bounded public Bitvavo read-only candle requests. Artifacts include \`direct-dl-price-paths.json\` and \`v4-dl-price-paths.json\`; 14-day artifact retention.

Moving retention-limited machine journal at execution: **1,809** decisions including **514 BUY_SENT**; **2,088** historical DL archives. Only **24 BUY_SENT** have an earlier DL generation of at most 900 seconds (4.67% of 514); the remaining **490** had only older DL states. Availability on GitHub *by signal time* still unverified. From these 24, the deterministic first *five distinct markets* with mature horizons were RLC, W, TREAD, LUMIA, FIL, for 15 horizon observations (5 markets × 24/48/72h) — **not 15 independent trades**.

All 15 strict 5m histories are \`INCOMPLETE\` because Bitvavo has gaps in the 5m trade candles. Indicative forward-filled zero-trade mark **only if >=80% actual observed 5m slots**, never a filled trade:

| Pair | Historic machine date UTC | Prior DL generated state | 72h actual 5m coverage | Indicative 72h close vs SIGNAL LAST | Indicative 72h MFE | Indicative stop-vs-TP1 touch |
|---|---|---|---:|---:|---:|---|
| RLC-EUR | 2026-10-06 21:16 | WATCH | 98.84% | +31.9658% | +87.5826% | STOP before rebound |
| W-EUR | 2026-10-07 23:16 | PLACE_LIMITE_PASSIVE | 83.66% | +10.9513% | +19.2300% | TP1 touched |
| TREAD-EUR | 2026-10-11 00:04 | WATCH | 26.54% | CENSORED | CENSORED | UNKNOWN |
| LUMIA-EUR | 2026-10-11 12:58 | WATCH | 80.88% | -35.4341% | +3.8091% | STOP |
| FIL-EUR | 2026-10-11 20:50 | PLACE_LIMITE_PASSIVE | 75.32% | CENSORED | CENSORED | UNKNOWN |

Very important: RLC initially had a 24h indicative close of **-15.3505%** with planned stop touched; its 72h +31.9658% mark / +87.5826% MFE cannot be counted as a realizable winner following the submitted stop. W's signal-time reference entry was **0.014181 EUR** but its machine limit entry was separate; a TP1 wick alone is not evidence of a filled limit order. LUMIA peaked only +3.8091% while closing -35.4341% at 72h. This is *descriptive evidence* for future classification research, not an estimator of DL avoided loss or missed profit.

Also on V4 15 October: 6 observations are 24h mature, 0 strictly complete; only DUSK and PUFFER passed the >=80% 5m coverage threshold for separate indicative marks. No 48/72h reached maturity for that V4 date at this run.

### Research priority

1. Compare **real DIRECT BUY_SENT and REJECTED on identical prospective market snapshots**; current DL is based on older, independent V4 data and is not an actual same-input treatment.
2. Isolate direct machine **order plans** (limit/stop/TP1), historical bid/ask books and true availability; do not convert arbitrary positive/negative candle paths into fills.
3. Study 24/48/72h conditional on observed stop-before-target sequence, delayed continuation and liquidity, with predeclared OOS sampling.
4. Publish N independent cash-constrained matched trades only once the input and execution evidence are valid. Until then, economic superiority: **NOT ESTABLISHED**.

No changes to production, live V4, LIVE direct scanner, thresholds, email alerts, or actual orders. PR #169 remains draft.


## Fourth experiment — Git commit metadata and DL cadence collapse (16 Oct ~17:55 UTC)

Read-only CI [run #38943082749, SUCCESS](https://github.com/Vadimrom-create/bitvavo-live/actions/runs/38943082749) uses the **path-scoped GitHub repository API** for every DL snapshot referenced by an eligible DIRECT BUY_SENT. No changes to order paths, production workflow, private account credentials or trading thresholds.

At this checkpoint the rolling machine log contained **1,866** decisions including **530 BUY_SENT**. Only **25/530 (4.72%)** BUY_SENT had a previous generated DL snapshot less than 15 minutes old. The commit metadata audit found **18 distinct archival commits**, all with committer timestamps **before** the associated 25 sender starts: **24/25** were at least 30 seconds earlier, **1/25** was within 30 seconds (FIL-EUR 15 October, about 3.7 seconds earlier). **This is metadata timing consistency, not proof GitHub had made the commit remotely visible or the user could have acted at that time.** The unresolved **505/530** cannot be interpreted as DL rejections.

Independent archive-cadence analysis on full UTC calendar days (periods selected *after observing the discontinuity*, descriptive only):

- **10 Sep–2 Oct**: 23 days, **1,923** DL shadow generations, mean **83.61/day**, median **85/day**.
- **4 Oct–15 Oct**: 12 days, **121** generations, mean **10.08/day**, median **9/day**.
- **3 Oct transition**: **35** generations; schedule deterioration begins around this date, before the 4 Oct heartbeat commit.
- Mean cadence decline about **87.94%**; date-selected exploration, NOT a randomized or causal change-point test and NOT proof of dropped GitHub schedule events.

The original update.yml still has cron '7,22,37,52 * * * *' with cancel-in-progress: false. The direct heartbeat's separate concurrency group cannot itself prove the origin of the decline. Do not edit the direct scanner or merge an expensive watchdog based on chronological coincidence. First obtain schedule-run telemetry, Actions queue/runner saturation and estimated GitHub minutes. A reliable same-input prospective DL shadow *cannot* be inferred merely by rerunning V4 on a later Bitvavo read: features, books and clock times differ. Production and research isolation remain mandatory.

The new script scripts/verify_dl_commit_asof.py performs this commit-metadata check automatically in **PR-only** CI using read-only GITHUB_TOKEN and bounded path lookups. The added calendar comparison treats days with zero archived files as **zero**, not as absent sampling days. Evidence flags for actual publication, same-input causal A/B and net portfolio PnL remain false/null.

Decision: **NO-GO** to reinstate DL as an alert veto; retain PR #169 as draft; next engineering milestone is capture a deterministic, simultaneous DIRECT and V4/DL feature packet in a separate research path with independent timestamps, fill feasibility, and 24/48/72h outcomes, without moving any direct scan critical path.

## Prospective DIRECT feature-receipt pilot — 17 Oct (nonactivated draft)

GitHub officially documents that scheduled Actions events may be delayed or dropped during high load; this is a plausible contributing mechanism for the October archive collapse, **not a proved root cause for this repository**. The independent production heartbeat is already event-chained, whereas the legacy V4/DL scan is largely dependent on best-effort schedule dispatches.

A separate **read-only observer** is drafted at `.github/workflows/research_direct_dl_receipt.yml` and `scripts/capture_direct_dl_prospective_receipt.py`. Trigger design: after a **successful** production heartbeat completes on `main`, checkout the latest public `main` snapshot in a **distinct concurrency group**, with only `contents: read`. It does not call Bitvavo, rebuild V4, publish repo files, access wallet/secrets, send alerts, execute orders, or alter/directly wait on production. It stores one gzip artifact with 3-day retention; possible impact is **additional GitHub runner minutes and shared quota**, to be reviewed before activation.

**Important activation constraint:** GitHub `workflow_run` workflows must exist on the repository's default branch. The draft PR does **not** activate the recurring observer; merging is a separate change requiring safety review/approval.

Proof from **PR-only CI run #39013586383 — SUCCESS**, **68 offline regression tests passed** and a real input snapshot:
- `2026-10-17T07:20:10.021189Z` DIRECT scan, **427 markets**.
- At the CI capture time, source age **432.866 seconds** (within the 900s cap), synchronized timestamps across production scan status, alert candidates and universe file.
- **Three** DIRECT `ACCELERATION_READY` candidates in the source snapshot: **GTC-EUR, RSR-EUR, ZIG-EUR**. These are NOT validated `BUY_SENT` emails or simulated fills.
- Features captured for those three candidates: **5m and 15m**; all three marked `UNSUPPORTED_NO_V4_BASELINE`. Their DIRECT data are hash-linked to the source Git checkout; every source JSON SHA256 is preserved. The prior V4/DL generation at DIRECT scan time was **4,443 seconds old**, clearly labeled `DL_OLDER_THAN_15_MINUTES`.
- The entire gzip research receipt is **3,122 bytes** for this cycle and makes no extra public market requests.
- `same_cycle_direct_features_proven=true`; `same_input_v4_dl_classification_proven=false`; `real_buy_sent_proven=false`; `net_portfolio_pnl_eur=null`.

**Remaining central engineering blocker:** these synchronous DIRECT features do not contain V4's `baseline` (opportunity, entry, trend, buy_ready, etc.). An exact same-input DL V1 action CANNOT be reconstructed from them. Real A/B needs **a separately frozen V4 feature packet computed on a matching market-data timestamp**, or a transparently separate direct-input challenger with its own independently evaluated logic. Do not silently map missing values to zero/WATCH. If a prospective observer is activated, validate GitHub runner usage, actual hourly capture continuity, 5m source completeness, timestamp publication margins, and daily artifact retention before broadening scope.

**No merge, production order, stop, threshold or DL gate activation has occurred.**

### Full-market correction — 17 October, validation of the 427-row retention

The initial 3,122-byte receipt archived source rows for only the three DIRECT candidates and hashes for the entire market. That is **insufficient to study missed nonselected winners**, a serious source of selection bias. The receipt was strengthened to archive **all 427 public market rows**, including DIRECT 5m/15m features, acceleration state, data quality, timestamps and source news, plus the candidate shortlist. It enforces a hard **2,000,000-byte compressed artifact budget** and discards/censors full-market data if the checkout's source is older than 15 minutes. No extra Bitvavo calls or trading side effects.

**Proven on full real repository data:** [PR CI #39014058377 SUCCESS](https://github.com/Vadimrom-create/bitvavo-live/actions/runs/39014058377), **68 regression tests PASS**. DIRECT scan of 17 Oct **07:30:23.858842 UTC**, **427/427 original source market rows** archived, **1** DIRECT `ACCELERATION_READY` candidate in this later scan, captured **273.914 seconds** after the scan, compressed report **162,131 bytes** (under the 2MB cap). The preceding independent V4/DL timestamp was still **5,056.898 seconds older** than this scan. Same-source candidate classifications remain **not possible** for DL V1 because V4 structural `baseline` fields are absent; no BUY_SENT or fill claims.

The code and event-driven read-only workflow are only on the **draft PR**. On `main`, activation would cause approximately one observer run per successful hourly heartbeat (not every 5-minute scan), and **consume additional shared GitHub Actions capacity**; it requires deliberate review before merging. This is a path to prospective full-universe accountability, *not a deployed remediation of V4/DL cadence*.
