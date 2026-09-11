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
