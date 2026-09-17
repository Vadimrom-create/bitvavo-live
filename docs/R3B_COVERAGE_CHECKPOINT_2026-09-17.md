# R3-B coverage validation checkpoint — 2026-09-17

Resume of `codex/astra-coverage-20260916`, published parent
`387a2688133e488cd0e9f4ed7816ff8529e9f5e1`, descendant of the exact R2 integration
`f8925b02626925cef91075f8460e0f8772ebc197`.

The restored Work checkout initially contained clean Phase 3 `2de92fc...`.
The uncommitted timestamp fix was absent. The two coverage commits were recovered
from GitHub without rebuilding or rewriting them. The previous coverage
diagnostic is retained in `COVERAGE_CORRECTION_2026-09-16.md`; it was not rerun.

## Demonstrated integration defect and minimal correction

The real corrected CI artifact (run 35134392975, artifact 10462508087) contains
an original ticker response at 18:26:48.720308Z and the separate public-watch
response at 18:29:09.733310Z on 2026-09-16. Observation prices came from the former,
but their timestamp incorrectly came from the latter via URL-keyed cache metadata.
This could make old inputs appear fresh. The frozen V4 output itself was not
modified by this late lookup.

The pipeline now retains the original atomic `capture` response and obtains both
its prices and its timestamp from that response. The later watch keeps its own
source identity and timestamp. A full pipeline regression with two responses
120 seconds apart fails on the published parent and succeeds with the fix.
No collection budget, worker count, pacing, scoring, threshold, decision policy
or monitoring version changes.

## Validation

* 188 local tests pass, zero failures/errors/skips, 3.646 seconds.
* The predecessor corrected CI passed all 187 then-existing tests and a real
  public scan: `20260916T182647Z-efcdd17a`, 430/430 market watches, 26 continuous
  5m series and 57 continuous 15m series. Sparse OHLCV remains explicitly marked.
* That real scan's frozen replay is exact (14 watch entries).
* Three available raw snapshots are replayed with the correction: the older
  Phase 3 snapshot (50 entries), R2 (12), and corrected coverage (14).
* All 499 DL-V1 historical references, including the initial 113, are replayed.
* Tests retain source candles, reject invalid quotes, preserve market visibility
  when optional enrichment expires, and never feed sparse slots into trading.
* The final commit must pass the same read-only CI and public scan again. Their
  exact SHA, logs and immutable artifact identify the final remote validation.

## Publication boundary — still open for a real pilot

Validation uses `ci.yml` with `contents: read`. Its public smoke step performs
acquisition and replay, then uploads an Actions artifact. It does not call
`publish_data.py`, enroll prospective sessions, send emails or execute orders.
The coverage diagnostic workflow also has read-only contents permission.

`update.yml` and `evaluate.yml` still read `main`, and the publisher still defaults
to `branch='main'`. They are deliberately **not dispatched** in this validation.
An isolated data/publication target and its fail-closed routing have not been
implemented or validated. Uploading a CI artifact is not proof of that isolation.
Thus this is a reproducible coverage checkpoint, **not authorization to start
the prospective pilot**. Private validation remains PENDING PRIVATE CONFIGURATION.

Next required task before a real pilot: explicitly isolate its data reads/writes
and publication destination, prove no fallback or production Pages deployment,
then authorize one isolated live cycle. No pilot is started by this checkpoint.
