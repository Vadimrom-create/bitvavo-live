# Prospective cadence and health contract

This change follows #104. It changes collection orchestration and observability only.
C0, detector, execution gates, sizing, sender, orders and challenger selection are unchanged.

## Wakeup graph and recursion proof

Existing production activity can still trigger both the prospective collector and the
production watchdog via `workflow_run`. Prospective completion can still trigger the
watchdog. The collector does **not** subscribe to watchdog completion.

A separate watchdog job may request exactly one `workflow_dispatch` of the collector,
only if its own event is `schedule`, `push` or `workflow_dispatch`, and the current slot
is due according to the published state. Both the YAML job guard and the Python guard
reject `workflow_run`. Therefore the path
independent watchdog → dispatch collector → watchdog(workflow_run) terminates.
No workflow dispatches itself. No polling loop or new external service is introduced.
The existing production rescue job is unchanged, including its email/order rules.
The observer has no SMTP credentials and cannot modify repository contents.

## One logical slot, bounded attempts

The collector retains cron `13,43 * * * *`, the single
`solaire-prospective-shadow-measurements` concurrency group and
`cancel-in-progress: false`. Every wakeup is checked against the latest main checkout.
An already completed slot skips all market work. Failed slots allow at most two
attempts, separated by at least 600 seconds. The attempt reservation and wakeup receipt
are committed before any market capture. Failure to publish the reservation stops
collection. A runner crash therefore cannot erase an attempt already allowed to collect.
RESERVED and IN_PROGRESS transitions are published separately before the heavy work.
An active reservation expires after 1,200 seconds (the workflow timeout), preventing
permanent locks after a hard crash. An explicitly FAILED attempt is retryable after the
600-second cooldown. Two failures yield ABANDONED_RETRY_LIMIT for that slot only.
COMPLETED is set only after fresh successful outputs have been verified.
The actual input revision is captured again after reservation publication/rebase.

Every created wakeup has a `prospective_wakeup_receipts/<run>_<attempt>.json` record
when publication succeeds, including trigger/upstream, slot, collect/skip reason and
health at that instant. Complete/failed collections retain their separate cycle receipt.
GitHub logs/artifacts remain evidence if publication itself fails.

Late collection captures current data only. Closed missed slots remain gaps; no
historical price backfill or retrospective candidate substitution occurs.

## Health is a time-dependent observation

Run `python scripts/prospective_cycle.py health` on a fresh main checkout to compute
current health from canonical state and the current clock, without changing any state.
This also detects closed holes accumulated since the last writer.
The reader reports published_health_age_seconds and CURRENT_HEALTH / STALE_HEALTH
separately from freshly recomputed current-slot health. The freshness threshold is
300 seconds, shortened at the next slot boundary or the end of its delay grace period.

The persisted `prospective_collection_health.json` is deliberately **not a live badge**:
`status = SNAPSHOT_REQUIRES_REEVALUATION`. Its `current_slot_status_at_check` is
`OK`, `DELAYED` or `MISSED`, scoped to `checked_at_utc` and bounded by `valid_until_utc`.
Readers must recompute or show UNKNOWN/STALE after expiry; a legacy v1 file without this
contract is also only a dated observation. Never display its raw historical OK as live OK.

Current-slot health, `historical_coverage_status`/missed slots, and the actual timestamp
and age of the last valid observation are independent fields. Current OK does not erase
historical gaps. At each independent watchdog opportunity a GitHub job summary reports
freshly calculated health, even if no collection is needed; collector begin/finish do too.

GitHub cannot execute a detector while it supplies no runner/event at all. This design
provides additional independent opportunities and makes old health explicitly non-current;
it does not guarantee punctual cron, uninterrupted collection, or alerts during a complete
GitHub Actions outage. A stale snapshot is observable from any read using the above contract.

## C0 scope remains unchanged

C0 is the contemporaneous production detector candidate payload, either
PRODUCTION_OBSERVED or explicitly RECOMPUTED_SHADOW on the same causal snapshot.
It is not proof of a delivered BUY or fill. Each consumer/event rechecks the 300-second
limit. Missing, mismatched or expired controls remain ineligible for paired statistics.
No past event is retrospectively paired or recomputed by this change.
