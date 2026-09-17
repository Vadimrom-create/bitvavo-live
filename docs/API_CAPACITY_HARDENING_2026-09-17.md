# Public API capacity hardening

Base: `3843b8a2ea720a74c127bdfead384a6e8eb1f819`.
Scope: acquisition scheduling only. No scoring, frozen V4, DL-V1/DL-V2,
OHLCV representation, candidate selection, pilot publication or monitoring release change.

## Protection

`research/api_budget.py` centralizes public endpoint weights (global 24h ticker:
25; trades: 5; other currently allowed public endpoints: 1). Every HTTP attempt,
including retries and failures, reserves its weight atomically in SQLite.
All PublicClient instances of the same Unix user on the same host share a
boot-specific file in the system temporary directory, independent of checkout.
No process-local fallback is permitted if that ledger cannot be opened.

Ceiling: 750 points in a rolling **61-second** ledger window (60 seconds plus
one second dispatch margin), against the exchange's 1000 points/minute.
The existing per-client 12 req/s pacing remains, but is no longer the quota
protection. Reservations are rechecked after every wait; no lock is held asleep.
The database is operational state, never a journal or publication artifact.
Do not delete it between runs to regain capacity; it expires reservations itself.
Linux is the existing runtime; boot identity uses `/proc/sys/kernel/random/boot_id`.

Headers cannot replenish the ledger. A remaining value below 250 only adds a
pause when the limit is 1000 and reset is finite, future and at most 61 seconds
away. Past, nonfinite and far-future resets are ignored. A 403/429 persists a
host-wide cooldown of at least 900 seconds, extended by Retry-After (seconds or
HTTP date) and resetat. That logical call stops: no immediate retry storm.
The 900-second bound follows the documented unauthenticated-IP ban, not a new
trading threshold. Other transient failures retain the existing retry count and
backoff, but every retry must obtain a new weighted reservation.

Reference: https://docs.bitvavo.com/docs/rate-limits/ (consulted in preceding audit).

## Real consumers and boundaries

* Pipeline: collector, V3/V4 acquisition, market control, execution diagnostics,
  full-universe diagnostics and public surveillance share PublicClient.
* `scripts/live_quotes.py` is a separate process immediately before the pipeline
  in update.yml. It now shares the same host ledger, even though those calls are
  sequential. Repeated manual runs and two simultaneous scanner processes also
  share it. Multiprocessing regression verifies the common envelope.
* update.yml already serializes its runs through
  `bitvavo-prospection-single-writer`. Position monitoring uses a separate hosted
  runner and concurrency group. No evidence establishes a common egress IP
  between those GitHub-hosted runners. Do not claim an IP-independent global
  limiter: this is deliberately not a distributed service.
* The deployed monitoring SHA remains pinned and is **not upgraded by this lot**.
  Its private read validation is PENDING PRIVATE CONFIGURATION. Authenticated
  account requests have a distinct account quota and are not charged to the
  unauthenticated ledger. Feedback, evaluation and prospective bookkeeping use
  files, not Bitvavo HTTP.
* Unmanaged software, different Unix users, isolated containers or separate hosts
  sharing one NAT IP are outside this ledger. Such a deployment needs shared
  scheduling before simultaneous use. Response headers are only an additional
  warning, not proof that such external consumers do not exist.

## Freshness

Each PublicClient has a cumulative collection horizon of 300 seconds, matching
the existing source freshness horizon. It cannot be extended by retries. The
shorter existing optional 120-second diagnostic deadline still applies.
Quota waits that cannot fit fail before network access. Socket timeout is capped
by remaining collection time. A response received after the effective deadline
is rejected before caching, journaling raw input or becoming consumable.

`COLLECTION_FRESHNESS_DEADLINE` distinguishes global acquisition abandonment
from `OPTIONAL_COLLECTION_DEADLINE`, HTTP failure and native candle gaps.
All universe rows remain represented, with explicit errors. Pipeline health
reports the shared budget, cumulative thread-wait time and abandoned calls;
a freshness-abandoned cycle is degraded and cannot publish a buy recommendation.
Existing final per-source freshness checks still identify data that aged during
collection. Cached snapshots retain their original timestamps; reading the cache
never refreshes the source's age. Serialization/CPU work and a slow streaming
HTTP body are not a hard real-time scheduler guarantee: overdue responses are
rejected, not asserted fresh.

## 15m reuse decision

The certified scan `20260917T115722Z-d04093bb` was checked again against its raw
responses: **124/124** later 15m/40 or 15m/50 closed-candle sequences equal the
subset of an earlier 15m/100 response. This proves parity for that scan only.
It does not establish a source immutability contract for later calls or future
15m boundaries. A closed 5m value revision already exists in the audit evidence.

No cross-limit reuse is enabled. Real saving in this lot: **0 requests / 0 points**.
Potential ceiling remains 124 points per comparable scan. An immutable source
snapshot contract or prospective equality evidence is required before changing
those acquisitions; no heuristic reuse is silently introduced. Existing exact
URL/params caching is retained.

## Validation and reproducibility

* `python scripts/run_tests.py all` (executor dependencies required): 209 tests,
  no failure or skip in the final local validation.
* `python -m unittest discover -s tests -p test_api_budget.py`: weighted reserve,
  two real processes, invalid headers, conservative remaining/reset, shared 429,
  retry charging, late response rejection, bounded timeout and complete explicit
  universe after abandonment.
* `test_capacity_stress.py` runs five offline scenarios through the actual
  PublicClient and actual SQLite transactions, with eight worker threads per
  consumer and a virtual transport clock. Workload: 1575 calls / 1695 points,
  matching the audited endpoint counts. This deliberately concurrent stress is
  not a reproduction of the pipeline's sequential stages or live OHLCV coverage.
  It prints request/point peak, retries, timeouts, completed timeframe pairs,
  freshness abandonment and final response ages. 429 is separately injected in
  unit tests; zero 429 in a simulated successful server is not a live finding.
* The certified raw V4 snapshot replays exactly against frozen, instrumented and
  recorded outputs (12 watch rows). ReplayClient has no network/budget dependency.
* Public CI smoke measures a fresh scan with the unchanged opt-in audit and
  immediately replays its raw V4 snapshot. This job is read-only, invokes no
  publisher, account, alert sender or pilot. Compare its telemetry to the base
  1575 requests / 1695 points / peak 724 / 151.92 seconds; market movements mean
  actual entry/trend acquisition counts and native candle continuity may vary.

## Rollback

Revert this acquisition-only commit if needed; do not rewrite historical logs or
change policy identities. A rollback loses weighted quota coordination; retain
single-consumer scheduling. No database migration of market data is involved.
The capacity tests and telemetry are validation artifacts, not held-out evidence.
