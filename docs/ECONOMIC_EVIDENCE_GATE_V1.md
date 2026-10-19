# Solaire — economic evidence gate v1 (research only)

**Scope:** GitHub issue #134, chantier B. This is an *evidence-readiness* check, **not** the requested full capital-constrained economic replay.

## What it does

Run on a checked-out repository snapshot:

```bash
python scripts/economic_evidence_gate.py \
  --exit-status production_exit_policy_shadow_status.json \
  --oos-status research/swing_selector_oos_latest.json \
  --output /tmp/solaire-economic-evidence.json
python -m unittest tests.test_economic_evidence_gate
```

The script uses only already-published **aggregate research**:
- Match current vs full-1.4R exit-policy shadow cohorts at 4h/12h/24h.
- Reject missing, non-finite, incoherent, mismatched or zero-maturity values.
- Independently reconcile the aggregate PnL delta (within publishing-rounding tolerance).
- Show winning vs losing event counts and median returns alongside sum PnL.
- Report R2 7-day maturity *without* declaring GO on maturity alone.
- Reserve real portfolio PnL, drawdown and ChatGPT contribution as **null**, not zero.
- Cite original source timestamps; does not invent fresh prices.

**Forbidden interpretations:** A positive shadow PnL sum does not imply a positive return on a 2,300 EUR portfolio. The same capital may be reused, episodes may overlap, net assumptions can differ, and market-order fills may be unavailable. MFE target touches are not sale proceeds. A favourable 1.4R total with a negative median cannot be promoted based on the total alone.

## Current evidence (11 October 2026)

Source: `production_exit_policy_shadow_status.json` generated at 09:27:55 UTC, versus `research/swing_selector_oos_latest.json` at 11:37:33 UTC.

| Horizon | Same matured cases | Current net proxy EUR | Full 1.4R net proxy EUR | Delta EUR | Full 1.4R median |
|:--|--:|--:|--:|--:|--:|
| 4 h | 165 | +7.79 | +138.30 | +130.51 | -0.9592% |
| 12 h | 147 | +15.51 | +160.58 | +145.07 | -0.5801% |
| 24 h | 114 | +218.21 | +191.29 | -26.92 | -0.7738% |

At 4h the candidate has 71 positive / 94 negative cases. Versus *full 1.5R* (not the current exit), its reported pairwise table has 5 wins, 33 losses and 127 ties despite an aggregate +30.59 EUR advantage. **This warrants distribution and concentration analysis, not a declaration of superiority.**

At the cited point, the 7-day R2 OOS cohorts have zero matured results. Subsequent report updates must not retroactively rewrite this timestamped baseline.

## Full replay still necessary

Before comparing V4 vs R2 vs a simple benchmark in euros for 2,300 EUR, build an independently validated normalized event ledger including:
1. Source policy/version, immutable evidence reference, feature timestamp and ex-ante entry condition.
2. Bid/ask observations or genuine fills, depth, fees, timestamps and trade eligibility.
3. Deterministic trade ordering, cash reservation/release and simultaneous-capital constraint.
4. Path-aware stop/target resolution, censored/missing outcomes, conservative spread/slippage and stress x2.
5. Per-policy portfolio equity, cash/positions reconciliation, max drawdown, positive/negative trade distribution and net incremental return versus same-period reference.
6. Out-of-sample comparison with frozen rules, unique event IDs and multiple regimes.

**Human/ChatGPT PnL** remains NOT_IDENTIFIABLE pending private decisions plus true transactions. The public repository must never receive private wallet holdings, transactions, emails or chat exports.

**No orders or trading policy changes.** New code is offline research; it is not imported by production scripts or scheduled workflows. God Layer remains paused.
