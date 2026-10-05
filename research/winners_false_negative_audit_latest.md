# Solaire — Winners / False Negatives audit

- Generated: `2026-10-05T22:34:58.299783+00:00`
- Anchor: `2026-10-05T22:26:21.238504+00:00`
- Window: **24 h**
- Cohort: top **20** positive 24h winners at the anchor snapshot.
- The endpoint ranking selects the cohort only; detector/gate milestones are reconstructed chronologically from committed production snapshots.
- Forward MFE/MAE are outcome measurements only and never alter the reconstructed decision path.

## Cohort

| Market | 24h | First BUILDING | First CONFIRMED | First gate / BUY | Primary cause | Remaining to anchor after decision | 4h MFE after decision |
|---|---:|---|---|---|---|---:|---:|
| RLC-EUR | 106.01% | 0.40154000 | 0.51568000 | STRUCTURAL_STOP_TOO_WIDE | `GATE_STRUCTURAL_STOP_TOO_WIDE` | 29.21% | 5.69% |
| ZEUS-EUR | 73.59% | 0.00232500 | 0.00364980 | SPREAD_TOO_WIDE | `GATE_SPREAD_TOO_WIDE` | -2.50% | 36.99% |
| RAD-EUR | 35.11% | — | 0.23960000 | INSUFFICIENT_EXECUTION_LIQUIDITY | `GATE_INSUFFICIENT_EXECUTION_LIQUIDITY` | 33.18% | 30.98% |
| NIL-EUR | 25.62% | — | 0.08332100 | BUY_SENT | `CAPTURED_BUY` | 14.76% | 12.33% |
| FLUID-EUR | 20.48% | — | 1.95980000 | STRUCTURAL_RANGE_TOO_NARROW | `GATE_STRUCTURAL_RANGE_TOO_NARROW` | -3.90% | 2.05% |
| ORCA-EUR | 19.41% | 1.80769000 | 1.86261000 | BUY_SENT | `CAPTURED_BUY` | 1.05% | 1.38% (partial) |
| MOVR-EUR | 18.53% | 1.68000000 | 1.74650000 | STRUCTURAL_STOP_TOO_WIDE | `GATE_STRUCTURAL_STOP_TOO_WIDE` | 1.80% | 22.36% |
| EDU-EUR | 14.90% | — | 0.04910000 | BUY_SENT | `CAPTURED_BUY` | -2.68% | 2.12% |
| PNT-EUR | 14.59% | 0.06467700 | 0.06036400 | BUY_SENT | `CAPTURED_BUY` | -6.85% | -3.86% (partial) |
| CAP-EUR | 13.53% | 0.06075700 | 0.06491890 | STRUCTURAL_RANGE_TOO_NARROW | `GATE_STRUCTURAL_RANGE_TOO_NARROW` | 1.17% | 2.13% |
| DIA-EUR | 13.18% | — | 0.14861000 | BUY_SENT | `CAPTURED_BUY` | 2.61% | 5.11% |
| FIL-EUR | 12.98% | 0.98878000 | 1.02709000 | BUY_SENT | `CAPTURED_BUY` | 2.97% | 4.17% (partial) |
| CARV-EUR | 12.59% | — | — | — | `DETECTOR_NEVER_BUILDING` | —% | —% (partial) |
| LIGHTER-EUR | 11.90% | 3.48310000 | — | — | `BUILDING_NEVER_CONFIRMED` | 4.65% | 3.07% |
| VELO-EUR | 11.67% | 0.00509940 | 0.00517140 | INSUFFICIENT_EXECUTION_LIQUIDITY | `GATE_INSUFFICIENT_EXECUTION_LIQUIDITY` | 5.44% | 3.40% |
| FLUX-EUR | 11.02% | 0.07035100 | — | — | `BUILDING_NEVER_CONFIRMED` | 8.08% | 4.64% |
| PARTI-EUR | 10.53% | — | 0.02597700 | BUY_SENT | `CAPTURED_BUY` | 1.77% | 4.76% |
| SENT-EUR | 9.90% | 0.02218200 | — | — | `BUILDING_NEVER_CONFIRMED` | 1.74% | 2.10% (partial) |
| KAIA-EUR | 8.48% | — | — | — | `DETECTOR_NEVER_BUILDING` | —% | —% (partial) |
| S-EUR | 8.33% | 0.03887100 | — | — | `BUILDING_NEVER_CONFIRMED` | 0.49% | 0.57% (partial) |

## Attribution

- `CAPTURED_BUY`: **7**
- `BUILDING_NEVER_CONFIRMED`: **4**
- `DETECTOR_NEVER_BUILDING`: **2**
- `GATE_INSUFFICIENT_EXECUTION_LIQUIDITY`: **2**
- `GATE_STRUCTURAL_RANGE_TOO_NARROW`: **2**
- `GATE_STRUCTURAL_STOP_TOO_WIDE`: **2**
- `GATE_SPREAD_TOO_WIDE`: **1**

## Gate false-negative candidates

Cases rejected by the execution gate whose post-decision path still reached +5% MFE within a complete 4h window while avoiding -5% MAE.
- **RAD-EUR** — `GATE_INSUFFICIENT_EXECUTION_LIQUIDITY`; 4h MFE 30.98% / MAE -1.99%.
- **MOVR-EUR** — `GATE_STRUCTURAL_STOP_TOO_WIDE`; 4h MFE 22.36% / MAE -3.81%.

## Late entries after prior rejection

- **ORCA-EUR** — first rejected at 1.86261000 (`STRUCTURAL_RANGE_TOO_NARROW`), later BUY at 2.07231000; premium vs first rejection **11.26%**, vs first CONFIRMED **11.26%**, delay 222.60 min.
- **EDU-EUR** — first rejected at 0.04910000 (`INSUFFICIENT_EXECUTION_LIQUIDITY`), later BUY at 0.05515000; premium vs first rejection **12.32%**, vs first CONFIRMED **12.32%**, delay 623.75 min.
- **DIA-EUR** — first rejected at 0.14861000 (`INSUFFICIENT_EXECUTION_LIQUIDITY`), later BUY at 0.15707000; premium vs first rejection **5.69%**, vs first CONFIRMED **5.69%**, delay 324.81 min.

## Detector misses / late-stage diagnostics

- **CARV-EUR** — `DETECTOR_NEVER_BUILDING`; 24h 12.59%; largest observed scan gap 285.45 min.
- **LIGHTER-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 11.90%; largest observed scan gap 285.45 min.
- **FLUX-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 11.02%; largest observed scan gap 285.45 min.
- **SENT-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 9.90%; largest observed scan gap 285.45 min.
- **KAIA-EUR** — `DETECTOR_NEVER_BUILDING`; 24h 8.48%; largest observed scan gap 285.45 min.
- **S-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 8.33%; largest observed scan gap 285.45 min.

## Safety / interpretation

- `cadence_gap_flag` is diagnostic only; it does not prove a signal would have fired inside the missing interval.
- `INSUFFICIENT_EXECUTION_LIQUIDITY` currently occurs before the order book is fetched; those rows explicitly record `book_checked=false` when evidence confirms that path.
- A positive post-rejection MFE does not by itself prove that a safe fill was available. Spread, depth, structural stop and exchange lifecycle risks remain separate constraints.
- This audit is measurement-only and makes no production changes.
