# Solaire — Machine event ledger and constrained cash accounting v1

**11 October 2026. Research-only. Tracks issue #134.**

## Precise scope

This is the first **event-level** economic evidence step, not a completed V4-versus-R2 comparative backtest. It normalizes the **public machine decisions available now** and supplies a tested stand-alone cash-and-fill calculator for *future verified executions or explicitly identified hypothetical fills*. It does not synthesize fills from signals. It has no Bitvavo requests, secrets, email, wallet or order modifications.

### 1. Public machine decisions

```bash
python scripts/build_economic_signal_ledger.py \
  --source production_direct_decision_journal.json \
  --output /tmp/economic_machine_events.json
```

Each row retains original decision/episode/signal IDs, original timestamp, market regime and source observation pointer, signal price and machine's proposed entry/stop/targets/stake. Every row has explicit unknown fields for actual fills, costs, net PnL and actual execution.

Input is the **retention-limited** `production_direct_decision_journal.json`, NOT the whole historical Bitvavo dataset. It only covers as much history as the current publication retains. Decisions labeled `BUY_SENT` mean alerts sent by the machine, **not** actual orders or necessarily emails read by the user. `REJECTED` is a machine verdict, not a rejection by ChatGPT. Count missing/out-of-window observations as UNKNOWN, never "non-detected".

The snapshot observed at 2026-10-11 18:34 UTC contained **702 machine decisions**: **222 BUY_SENT** and **480 REJECTED**. All 222 BUY_SENT have an entry/stop/TP/stake structure in this particular snapshot, but **no one** has a verified fill/exit or realized PnL from this source. Those numbers will differ in future retained snapshots; the workflow reports actual counts at execution time.

The producer SHA-256 (raw input bytes) and source publication timestamp are retained. The normalized view does **not** assert immutable code SHA/feature provenance at every decision: source policy commit and feature-as-of are null until proven.

### 1b. Historical execution book join (still not fills)

```bash
python scripts/enrich_economic_signal_books.py \
  --source /tmp/economic_machine_events.json \
  --observations-dir execution_observations \
  --output /tmp/economic_machine_books.json
```

The join accepts *only* `observation_<32-hex>.json` files and matches the observation, decision, signal and market IDs exactly. Missing, malformed or mismatched observations are flagged, not invented. For matched observations it retains:
- Exact **availability timestamp** relative to the machine decision (`book_was_known_at_decision` is false if it arrived afterwards);
- Historical best bid/ask, spread, book coverage and same-snapshot hypothetical entry/exit cost at **100 EUR and 150 EUR** when present;
- Explicit `actual_fill_proven=false`, even when the quoted order book depth was adequate.

The important causal distinction: a book collected *after* a decision may be evidence for a later **hypothetical** execution, but cannot be retroactively attributed to the decision maker's knowledge. Same-snapshot liquidation costs are **not** a future order's spread/slippage, and no price target touch is an executed trade.

### 2. Separate deterministic capital accounting

`research/economic_cash_ledger.py` has a tested `calculate_cash_ledger(...)` helper. It **accepts only explicit independent `FILL_CONFIRMED` records**, never `BUY_SENT`. For each record: unique fill ID, UTC time, market, BUY/SELL, quantity, executed price, explicit nonnegative fee, and source classification (`MODEL_FILL` vs `OPERATOR_ATTESTED_FILL`). The latter requires a private proof pointer and is still **not independently verified**.

On a given **hypothetical** 2,300 EUR budget, it:
- Processes chronologically and checks exact running cash via decimal arithmetic, prevents borrowing/double-use of cash and short sales.
- Tracks cost basis including buying fees and realizes profit/loss on actual supplied sell records (after selling fees).
- Checks `cash + remaining cost basis = initial capital + realized PnL` on every fill.
- Requires valid, recent post-fill marks before calculating total equity or overall profit. Missing/stale/future marks leave those numbers null.
- Never constructs maximum drawdown from a single snapshot and never declares independent evidence of executable profitability.

This is accounting plumbing, **not** a claim that the public machine emitted any trade fills. Do not run against real private data inside this public repository. Private reconciliations must happen in trusted private storage.

### 3. Constraints on follow-up replay

To compare V4, R2 and a simple benchmark on genuinely equal grounds, we still need an event-level, time-consistent **join** with historical market books or properly time-bounded fill models:
- Same observation timestamp cutoff, feature freshness and policy commit, identical funding and exit assumptions.
- Eligibility, spread and available bid/ask depth at signal time for 100-150 EUR orders, zero-volume/gap censoring and order-latency rules.
- Hourly/5-minute path-aware exits with stop-first handling of ambiguous bars, fixed time horizon and stress costs.
- Chronological competition for scarce cash, no two policies cherry-picking unrelated dates, and mark-to-market drawdown.
- Chronologically independent out-of-sample test and separate human decision attribution only after the private chat export.

**No 2,300 EUR return can be calculated honestly from the public BUY_SENT journal alone.**

### 4. Verification and no production mutation

```bash
python -m unittest tests.test_economic_signal_ledger -v
```

The PR-only workflow loads the actual public journal into the normalized ledger and verifies counts/fill fields. It keeps the output in a **time-limited CI artifact**; neither raw files nor private user data are committed. This PR does not change any production workflow, BUY thresholds, alerts, stops, executor, wallet access, or God Layer. No automatic merging.
