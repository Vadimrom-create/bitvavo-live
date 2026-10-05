# Solaire — Winners / False Negatives audit

- Generated: `2026-10-05T21:29:13.809871+00:00`
- Anchor: `2026-10-05T21:24:23.864003+00:00`
- Window: **24 h**
- Cohort: top **20** positive 24h winners at the anchor snapshot.
- The endpoint ranking selects the cohort only; detector/gate milestones are reconstructed chronologically from committed production snapshots.
- Forward MFE/MAE are outcome measurements only and never alter the reconstructed decision path.

## Cohort

| Market | 24h | First BUILDING | First CONFIRMED | First gate / BUY | Primary cause | Remaining to anchor after decision | 4h MFE after decision |
|---|---:|---|---|---|---|---:|---:|
| RLC-EUR | 85.44% | 0.40154000 | 0.51568000 | STRUCTURAL_STOP_TOO_WIDE | `GATE_STRUCTURAL_STOP_TOO_WIDE` | 15.91% | 5.69% |
| ZEUS-EUR | 80.79% | 0.00232500 | 0.00364980 | SPREAD_TOO_WIDE | `GATE_SPREAD_TOO_WIDE` | 1.55% | 36.99% (partial) |
| NIL-EUR | 29.07% | 0.09055700 | 0.08332100 | BUY_SENT | `CAPTURED_BUY` | 16.05% | 12.33% |
| RAD-EUR | 27.55% | 0.27535000 | 0.23960000 | INSUFFICIENT_EXECUTION_LIQUIDITY | `GATE_INSUFFICIENT_EXECUTION_LIQUIDITY` | 25.73% | 30.98% |
| FLUID-EUR | 24.02% | 1.98490000 | 1.95980000 | STRUCTURAL_RANGE_TOO_NARROW | `GATE_STRUCTURAL_RANGE_TOO_NARROW` | -0.97% | 2.05% |
| GTC-EUR | 23.49% | 0.14921500 | 0.15987400 | SPREAD_TOO_WIDE | `GATE_SPREAD_TOO_WIDE` | 5.26% | 35.75% |
| MOVR-EUR | 17.31% | 1.68000000 | 1.74650000 | STRUCTURAL_STOP_TOO_WIDE | `GATE_STRUCTURAL_STOP_TOO_WIDE` | 2.28% | 22.36% |
| PNT-EUR | 17.00% | 0.06467700 | — | — | `BUILDING_NEVER_CONFIRMED` | -10.83% | -1.05% (partial) |
| EDU-EUR | 16.40% | 0.05267000 | 0.04910000 | BUY_SENT | `CAPTURED_BUY` | -1.41% | 2.12% (partial) |
| CARV-EUR | 14.58% | — | — | — | `DETECTOR_NEVER_BUILDING` | —% | —% (partial) |
| CAP-EUR | 14.30% | 0.06075700 | 0.06491890 | STRUCTURAL_RANGE_TOO_NARROW | `GATE_STRUCTURAL_RANGE_TOO_NARROW` | 1.51% | 2.13% (partial) |
| FIL-EUR | 13.99% | 0.98878000 | 1.02709000 | BUY_SENT | `CAPTURED_BUY` | 3.23% | 3.23% (partial) |
| LIGHTER-EUR | 13.33% | 3.48310000 | — | — | `BUILDING_NEVER_CONFIRMED` | 5.65% | 3.07% |
| DIA-EUR | 12.41% | 0.15138000 | 0.14861000 | BUY_SENT | `CAPTURED_BUY` | 1.87% | 4.66% (partial) |
| ORCA-EUR | 12.33% | 1.80769000 | 1.86261000 | STRUCTURAL_RANGE_TOO_NARROW | `GATE_STRUCTURAL_RANGE_TOO_NARROW` | 4.80% | 9.42% (partial) |
| VELO-EUR | 10.82% | 0.00509940 | 0.00517140 | INSUFFICIENT_EXECUTION_LIQUIDITY | `GATE_INSUFFICIENT_EXECUTION_LIQUIDITY` | 4.31% | 3.40% |
| PARTI-EUR | 10.70% | 0.02781100 | 0.02597700 | BUY_SENT | `CAPTURED_BUY` | 2.20% | 4.76% |
| FLUX-EUR | 9.89% | 0.07035100 | — | — | `BUILDING_NEVER_CONFIRMED` | 6.27% | 4.64% |
| GRASS-EUR | 9.80% | 0.66459000 | — | — | `BUILDING_NEVER_CONFIRMED` | 1.76% | 4.15% (partial) |
| BIO-EUR | 8.71% | 0.02733100 | — | — | `BUILDING_NEVER_CONFIRMED` | 7.12% | 0.22% |

## Attribution

- `BUILDING_NEVER_CONFIRMED`: **5**
- `CAPTURED_BUY`: **5**
- `GATE_STRUCTURAL_RANGE_TOO_NARROW`: **3**
- `GATE_INSUFFICIENT_EXECUTION_LIQUIDITY`: **2**
- `GATE_SPREAD_TOO_WIDE`: **2**
- `GATE_STRUCTURAL_STOP_TOO_WIDE`: **2**
- `DETECTOR_NEVER_BUILDING`: **1**

## Gate false-negative candidates

Cases rejected by the execution gate whose post-decision path still reached +5% MFE within a complete 4h window while avoiding -5% MAE.
- **RAD-EUR** — `GATE_INSUFFICIENT_EXECUTION_LIQUIDITY`; 4h MFE 30.98% / MAE -1.99%.
- **MOVR-EUR** — `GATE_STRUCTURAL_STOP_TOO_WIDE`; 4h MFE 22.36% / MAE -3.81%.

## Detector misses / late-stage diagnostics

- **PNT-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 17.00%; largest observed scan gap 80.91 min.
- **CARV-EUR** — `DETECTOR_NEVER_BUILDING`; 24h 14.58%; largest observed scan gap 285.45 min.
- **LIGHTER-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 13.33%; largest observed scan gap 285.45 min.
- **FLUX-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 9.89%; largest observed scan gap 285.45 min.
- **GRASS-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 9.80%; largest observed scan gap 285.45 min.
- **BIO-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 8.71%; largest observed scan gap 285.45 min.

## Safety / interpretation

- `cadence_gap_flag` is diagnostic only; it does not prove a signal would have fired inside the missing interval.
- `INSUFFICIENT_EXECUTION_LIQUIDITY` currently occurs before the order book is fetched; those rows explicitly record `book_checked=false` when evidence confirms that path.
- A positive post-rejection MFE does not by itself prove that a safe fill was available. Spread, depth, structural stop and exchange lifecycle risks remain separate constraints.
- This audit is measurement-only and makes no production changes.
