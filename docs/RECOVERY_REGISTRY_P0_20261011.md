# Recovery registry P0 — safety contract

A pre-compaction backup reference exists at `backup/solaire-recovery-precompact-20261011` (commit `f270d99a0f3d602977de2b129f694ccbbc25d2a4`).

Never remove the historical JSON unless a byte-identical compressed archive, SHA-256 source and archive hashes, Git blob ID, episode count, and a decompression round-trip are verified and persisted in the same commit as migration. Never change production BUY logic, trading thresholds, orders or HUMAN SWING during registry maintenance.

The repeated full-registry deep copies in `observe_episode()` must be replaced with an explicitly normalized, in-place batch path used only after one copy at the heartbeat entrypoint; public calling semantics remain unchanged. Regression tests must check identical episode transitions, TTL, chronology, deduplication and history integrity.

Fail closed on ambiguous dual registry files, invalid JSON, missing history, concurrent publication and failed archive validation. A GitHub workflow status of success is not proof of a valid scan cadence; measure scanner, gate, registry, follow-up and Git publication wall times.
