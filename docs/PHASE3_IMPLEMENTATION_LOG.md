# Phase 3 — implementation evidence

Starting commit: `6312a153e80e0e4c9b06c5e6672c541149caefbf`.
Architecture: `ASTRA_PHASE3_RECONCILED_PLAN_2026-09-11.md`.
All prospective data starts as TECHNICAL_PILOT, never held-out.

## Lot 1 — References and identities

- Checked remote main, clean isolated checkout, workflows, and four intervening data-only commits. No preceding implementation to reuse.
- Baseline: 61 tests pass. New reference/identity tests fail before implementation, then pass.
- Protected initial market journals, frozen V4 sources and DL-V1 by Git blob hash. Old truncated audit checkout untouched.
- Separated data, decision, execution and evaluation identifiers; no scoring or execution behavior changed.
- Rollback: remove new documentation/identity consumers only; never alter protected history.
- Private validation and deployed legacy daemon: PENDING PRIVATE CONFIGURATION / DEPLOYMENT VERIFICATION.

## Resume checkpoint — 2026-09-11

- Resume SHA `ab475f17ac3a1a95a5b15a41bc1f601f4fad33bf`, branch `codex/astra-phase3-20260911`. Only untracked `tests/test_executor_safety.py`; lot 2 still RED, no production change. Lot 1 is the only completed lot; no phase-3 commit published.
- Remote main `7efa5dc77e818611e839b8d02809aaf63a017359`: 34 additional data-only commits, 17 new market/DL journals; no source/workflow change. Latest eight scheduled runs successful, newest `34596469789`. None validates phase-3 code.
- Re-read complete architectural plan and launch/resume scope. Previous validation: 61 baseline + 2 lot-1 tests; historical V4 raw replay not rerun; DL-V1 audit evidence remains distinct.
- Runtime dependencies did not survive session restart; restored from declared requirements before continuing executor tests. Old audit checkout and all historical artifacts preserved.

## Lot 2 — Legacy executor closed and private

- Reproduced 13 failing assertions in the six previously written safety tests before interruption; implementation now passes all six. Full suite: 69 tests pass.
- Central GET-only transport rejects POST/PUT/PATCH/DELETE before signing or network, including the secondary cancellation route. Environment settings cannot reopen execution; approvals are always rejected.
- Missing/restarted state freezes; malformed state fails explicitly. Public status schema v2 is a strict seven-field whitelist; stdout contains only a generic event code. Private state/events keep diagnostics with mode 0600.
- Sentinel payloads and nested private values tested at caller and publication transport boundaries; zero mutation transport calls. No real account or SMTP access.
- CI installs the existing executor requirements for its new test suite. V4/DL-V1 code and histories unchanged; no market replay needed for this isolated lot.
- Rollback: stop legacy publication/daemon, retain central closure. Exposure ledger remains deferred, not claimed implemented.
- Deployed daemon SHA and prior publicly committed private details cannot be verified/remediated from the repository alone: PENDING PRIVATE CONFIGURATION / DEPLOYMENT VERIFICATION.

## Lot 3 — Independent critical monitoring

- New isolation tests reproduced eager-buy import failure, candle calls preceding justified exits, and absence of a standalone workflow. After changes: 23 monitoring tests and 73 total tests pass; workflow YAML parses.
- Dedicated monitoring workflow has its own timeout/concurrency, no needs dependency, a pinned release SHA and exact cryptography/cffi/pycparser dependencies. Current encrypted state is copied separately from main; only this workflow sends SMTP. CI runs monitoring/data/shadow/executor suites independently.
- Quotes for every holding are assessed first. An exit/partial event prevents candle enrichment and optional buy imports. Fault injection at optional input boundaries covers six named external-failure contexts; no real external outage or email delivery is claimed.
- Publisher commits/rebases only a temporary publication worktree, preserving executing HEAD. Concurrent distinct-file publication succeeds; conflicting same-state publication refuses. Test expectation updated to require the source checkout stay unchanged.
- Private telemetry records successful evaluation intervals and account/book ages; failed/UNCONFIGURED cycles do not become successful monitoring. SMTP accepted followed by state-save failure is explicitly uncertain.
- New buy module retains the original top-one selection until lot 8. Workflow new buys remain disabled until coherent manifests and fallback are validated. No V2 route exists.
- Public live CI no longer commits observations back onto a review branch; validation artifacts remain uploadable. No historical source or journal changed. No V4/DL-V1 replay required for this isolated lot.
- Rollback: pin previous validated monitoring SHA with current encrypted state; never restore a second sender. Real account, SMTP and seven-day cadence: PENDING PRIVATE CONFIGURATION. Release pin is recorded in the immediately following metadata commit after validation.

## Lot 4 — Minimum temporal contract

- Four new temporal tests failed before implementation; five targeted tests now pass, full suite 78 tests pass.
- PublicClient.capture binds copied content and metadata, request/response identity, per-consumer/key sequence and availability cutoff. Refreshed same-URL responses coexist. ReplayClient replays consumer-bound responses with no network fallback; old journals retain their legacy reader.
- Source-close bound uses request start plus measured server offset minus clock uncertainty; HTTP Date is retained separately and is not a market-content timestamp. Actual cache closure correction follows in lot 5.
- Pipeline records four policy identities, input snapshot/cutoff and separate baseline/diagnostic readiness. This lot still labels legacy inputs LEGACY_OBSERVED_V1; later diagnostics do not become earlier V4 inputs.
- Downloaded actual CI raw snapshot from run 34596469789, artifact 10261523827. Local replay of 20260911T115709Z-f616cf19: frozen reference = instrumented = recorded live, 50 watch rows. All 113 DL-V1 journals present in the starting checkout replay exactly on every field returned by decide.
- Source/historical blob protections pass. No historical journal or baseline source changed. Rollback: legacy replay reader remains; reject ambiguous inputs rather than replacing an earlier response.

## Lot 5 — Per-profile cache and source-closed inputs

- Four cache/closure tests failed before implementation. Targeted tests cover AAA + insufficient NEW, restart, failure without clock renewal, three-hour expiry, BTC/ETH dependency freshness, crossing request/close boundaries and unchanged daily-profile formula.
- New TrendCache keeps each market's attempt/acquisition/source independently; TTL remains 90 minutes and maximum age three hours. Expired references cannot silently confer fresh relative strength. Original v4_common.py is untouched.
- Versioned V4 adapter filters candles according to request-start clock bound and supplies corrected profiles without editing the frozen formulas. Corrected rolling states and journals use separate namespaces; no synthetic freshness migration from legacy cache. --data-policy CORRECTED_INPUTS_V1 selects this path.
- Legacy V4 plus repaired diagnostic data is explicitly LEGACY_V4_CORRECTED_DIAGNOSTICS_V1, with separate journals; it is not relabeled as original historical input policy. The default CLI retains this reference path until prospective orchestration is installed.
- Diagnostics and monitoring bind candle content/metadata. A cache captured before closure cannot acquire that closure on later read; insufficient latest closure remains unavailable. Post-baseline diagnostic reception has its own cutoff, not an earlier V4 timestamp.
- Full pipeline fixture exercises legacy and corrected paths in isolated subprocesses and exact consumer-aware replay against both frozen and instrumented engines. A cold-cache {} replay initialization discrepancy was found and fixed. These fabricated fixture observations are not saved into repository journals.
- 83 tests pass. Actual CI raw legacy replay 20260911T115709Z-f616cf19 remains exact (50 watch rows). V4/DL-V1 source and historical hash invariants pass; prior 113 DL-V1 replays remain valid.
- Rollback: suspend corrected consumer / reject ambiguous closure; retain its logs and original replay mode. Live corrected acquisition still needs a prospective run; private monitoring remains PENDING PRIVATE CONFIGURATION. Monitoring release pin will advance after all critical-path changes are validated.
