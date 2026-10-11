# SCAN abstention accountability — shadow V1 (24 / 48 / 72 h)

**Status:** research-only, no deployment into production, no orders, no threshold changes.

## Problem to measure

A strong crypto market regime does **not** guarantee every rising asset is executable or profitable. Conversely, replacing most Solaire ACHETE signals with an assistant recommendation to wait can itself have a cost. Neither position may be defended without a prospective, paired, execution-aware comparison.

This change **extends** the existing private SCAN sidecar; it does not duplicate the economic machine-signal or cash ledger proposed in PR #162 / #163 (issue #134).

## Categories

- **ACHAT_TEST** -> existing chatgpt_action=BUY; a small explicitly advised trade, never an automatic order.
- **ATTENDRE_CONFIRMATION** -> WAIT_RECHECK; requires a reason, objective trigger and due time.
- **ECARTER** -> REJECT_STRUCTURAL; explain verifiable structural/liquidity rejection.
- **NON_CLASSABLE** -> INSUFFICIENT_DATA; an explicit missing-data bucket, **not** a disguised rejection.

The field decision_category may be written explicitly in a private scan_decision record. The script rejects contradictions with the original chatgpt_action. Legacy records without the field are marked LEGACY_INFERRED, never mislabeled as contemporaneously explicit.

## Input and provenance

Use existing private SCAN session capture, scripts/capture_chatgpt_scan_session.py, to write decisions to the private JSONL ledger. A fresh and immutable machine source reference, captured human decision timestamp, Bitvavo book timestamp, quantified risk, explicit output and documented reason remain necessary for a valid BUY. The ledger is intentionally stored **outside the public GitHub repository**. The scripts do not capture ChatGPT conversations automatically.

Run the new evaluator after the session has been captured:

~~~bash
python scripts/measure_scan_abstentions.py \
  --decisions /tmp/private-scan-accountability.jsonl \
  --asof 2026-10-14T21:00:00Z \
  --output /tmp/private-abstention-report.json
~~~

For actual economic comparisons, add a separate **independently verified** private paired-outcome JSONL file and pass --pairs /tmp/private-paired-outcomes.jsonl. The existing strict paired-outcome interface requires both_executions_validated, matched_budget_policy_costs, horizon_matured, and independent_episode to be true, plus two net euro outcomes. Prefer an evidence_observed_at_utc timestamp; the new evaluator excludes pairs observed before maturity or after cutoff. Never manufacture these fields from highs, simulated peak profits, or signal scores.

## Exact outputs

For **each** decision, produce the category, whether the source machine action was ACHETE, reason codes, source age and per-horizon (24 / 48 / 72) state:

- NOT_MATURE before the time window elapses.
- MATURE_NO_VERIFIED_PAIR after maturity but without **both comparable, evidenced** economic outcomes.
- VERIFIED_PAIRED_NET only when the supporting paired proof passes validation, is causally mature and is time admissible.

Aggregate economic results **by original decision category and horizon**. Coverage denominator is matured decisions with an observed machine ACHETE. Missing pairs are not treated as zero PnL, and category aggregate values stay null until the first verified pair exists. Even with verified pairs, results are DESCRIPTIVE_ONLY, never a calibrated prediction or causal proof of ChatGPT's superiority.

## Operational limits and next steps

1. Record **every** SCAN decision at the moment it is made, including unfavorable cases, rather than selecting interesting outcomes afterward.
2. Preserve source event IDs, exact entry limits, order-book depth/fees, risks and explicit WAIT recheck conditions **before** seeing future prices.
3. Revisit outcomes at 24, 48 and 72 hours with independently verified comparable execution and exit assumptions. Missing execution evidence remains non-measurable.
4. Join the prospective SCAN decisions to the independent machine event and cash ledgers from PR #162 / #163. Do not equate machine signals with actual fills.
5. Compare net outcomes and opportunity costs on matched market/date/capital/risk cohorts, while monitoring selection bias, correlated episodes and attrition.
6. Do **not** loosen live filters or issue orders on the basis of preliminary shadow results.

No private balances, personal mail contents, secret token or user decision text are committed in this PR. The CI uses synthetic fixtures only.


## Empirical gap audit (public machine journals)

A separate read-only script audits the *retained* canonical production journal and the five-minute direct decision journal, de-duplicates by stable decision ID, and counts recorded outcome coverage. It never generates a trading return or a ChatGPT decision.

~~~bash
python scripts/audit_evaluation_coverage.py \
  --canonical production_decision_journal.json \
  --direct production_direct_decision_journal.json \
  --asof 2026-10-11T20:00:00Z \
  --output /tmp/solaire_research_evaluation_coverage.json
~~~

Current production evaluation implementation only lists horizons of **4, 12 and 24 hours** and requests **400 × 5-minute** Bitvavo candles (approximately 33h20 of available history), regardless of the age of the signal. Its current interval window cannot reconstruct many older due outcomes, and it has no 48h or 72h horizon. A missing evaluation is **unknown**, not zero profit or a failed trade. The research CI runs the gap audit on real public journals and retains an aggregate-only artifact.

The small scan_history.json leaderboard cache is also insufficient as a 24/48/72h price evaluation source: the 11 October sample matched only 12/171 mature 24h machine BUY events within one hour after target, 9/121 at 48h and 15/81 at 72h. These counts are diagnostic only, from the retained cache and an as-of cutoff of 2026-10-11T16:45:39Z. Do not treat sampled last prices as executable bid/ask or realizable performance.

**Next prerequisite:** use the existing complete, timestamped 5-minute source or archived execution observations to create and verify paired, capital-constrained forward outcomes. Only then can the private ChatGPT decision ledger from this PR be joined for a non-biased economic comparison. Until that data exists, the evaluator returns NON_MESURABLE.


## Bounded historical 5-minute price-path check (research only)

After finding 0% 48h and 72h outcome coverage in the retained main production journal, a separate price-only recovery helper checks matured machine BUY_SENT signals against Bitvavo's public historical candlestick endpoint. Bitvavo explicitly supports interval=5m, UTC millisecond start/end and a maximum limit of 1440 candles; 72 hours fit this maximum. Reference: https://docs.bitvavo.com/docs/rest-api/get-candlestick-data/

~~~bash
python scripts/research_mature_price_paths.py \
  --source production_direct_decision_journal.json \
  --max-per-horizon 4 \
  --output /tmp/solaire_research_mature_paths.json
~~~

- Choose the four most recently matured BUY_SENT events per horizon (24, 48 and 72h), strictly by timestamp, with no repeated market inside a horizon. This is a PREDECLARED de-correlation sampling rule, not cherry-picking winners.
- Use candle START/END-aligned parameters, closed 5m intervals after the decision candle, and the existing conservative stop-before-profit tie-breaker from research.production_journal.
- Primary strict observations treat missing 5m candle intervals as INCOMPLETE. Separately, an INDICATIVE market price mark may carry forward the last observed trade across Bitvavo-documented zero-trade gaps. The two outputs are never combined into a proven trade, execution price, or PnL. Failed requests are SOURCE_ERROR.
- Completed records expose price-only close, MFE and MAE relative to the machine's proposed, not executed, entry.
- actual_fill_proven=false, future_exit_executable_proven=false, net_pnl_eur=null, chatgpt_decision_joined=false for all rows.
- CI runs only on PR and uploads a small research artifact; there is no production scan/policy/workflow modification or automatic trading.

This gives a factual starting point for 48/72h paths but does not yet calculate net executable outcomes or prove that ChatGPT's abstentions were good or bad. The next join requires matched historical bid/ask evidence and private ChatGPT decisions, plus exit-fee/stop/latency assumptions.

Even where the indicative zero-trade-gap price path has a nonzero reference close return, this is not an executable strategy return and does not validate an assistant buy/refusal. Every such observation reports the gap count and preserves strict completeness separately.
