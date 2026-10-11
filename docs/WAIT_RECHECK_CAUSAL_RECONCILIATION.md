# WAIT_RECHECK — private-to-machine causal reconciliation (research only)

## What the checker does
`scripts/reconcile_private_wait_recheck.py` compares a *private* timestamped ChatGPT SCAN decision ledger with the public, versioned `production_direct_decision_journal.json`.

For each market's **latest** private decision, only `WAIT_RECHECK` remains open. It detects machine `BUY_SENT` after that decision and overdue review deadlines. `BUY_SENT` is evidence of a machine alert recorded as sent; it is **not** evidence of a filled trade, nor permission to buy.

Results:
- `REVIEW_NEW_MACHINE_BUY`: at least one subsequent Solaire `BUY_SENT`; immediate **human re-evaluation is required** with a fresh book, market news and structure.
- `REVIEW_OVERDUE`: the private deadline expired; no subsequent `BUY_SENT` appears in the *retained* public journal.
- `AWAITING_TRIGGER_OR_DEADLINE`: no new `BUY_SENT` in the retained journal and deadline is not yet due.

Historical absence is **never** reported as `NON_DETECTE`: public journal retention is incomplete.

## Run on a private filesystem, outside the public repository

```bash
python scripts/reconcile_private_wait_recheck.py \
  --decisions /private/scan_decisions_private_v1.jsonl \
  --journal production_direct_decision_journal.json \
  --asof 2026-10-11T14:00:00Z \
  --output /private/wait_recheck_review.json
```

The tool prints **counts only**. Full output is written to a file with private permissions; the path must be outside the repository. It does not fetch private ChatGPT Library data automatically. A connected, authorized ChatGPT session must retrieve and materialize the *actual* private ledger first. No historic user decisions are bundled with this PR.

## Mandatory integration into each user-requested SCAN

1. Read the latest private ledger from the user's Library and the current public Solaire journal.
2. Reconcile from the **actual private** decision timestamp, never from a reconstructed guess.
3. Prioritize `REVIEW_NEW_MACHINE_BUY` and `REVIEW_OVERDUE` in the SCAN, checking a *fresh* Bitvavo book plus macro news. Historical signals may already be invalid.
4. Write a **new, explicit human decision** privately (or report missing persistence honestly). Never have this script silently mark an old WAIT as reviewed.
5. Keep the new decision, its machine evidence SHA, and its freshness in the same private append-only history with version checks. If private persistence fails, disclose it.

An autonomous out-of-chat service is **not** installed by this PR. Neither GitHub Actions nor a GitHub workflow should be given private ChatGPT Library contents. Add any future conditional monitoring in a separate explicitly approved private workflow, not in production.

## Safety
- Only additive research script, tests, CI test job and documentation. No production workflow, scanner, email sender, threshold, stop, order, or GOD Layer modifications.
- No external requests, SDK, auth credentials, or console disclosure of private decision contents.
- UTC chronology and duplicate events handled; false absence forbidden.
- An event newer than `--asof` is excluded.
- If any required record is malformed, fail closed and do not emit a recommendation.
- Preexisting private files are never modified.

## Independent closure checks

P0 heartbeat is independently closed **only after** a full 12-cycle production workflow succeeds and a successor workflow starts scanning on schedule. This PR cannot provide that proof.

P1 WAIT_RECHECK is independently closed **only after** an actual SCAN reads private decisions, re-evaluates post-WAIT Solaire confirmations, persists the superseding decisions privately, and a second read verifies them. This PR supplies one causal diagnostic component, **not** that full end-to-end integration.

Run synthetic tests:
`python -m unittest discover -s tests -p 'test_reconcile_private_wait_recheck.py' -v`.
