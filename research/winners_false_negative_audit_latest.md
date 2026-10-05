# Solaire — Winners / False Negatives audit

- Generated: `2026-10-05T22:07:32.037297+00:00`
- Anchor: `2026-10-05T21:54:24.193979+00:00`
- Window: **24 h**
- Cohort: top **20** positive 24h winners at the anchor snapshot.
- The endpoint ranking selects the cohort only; detector/gate milestones are reconstructed chronologically from committed production snapshots.
- Forward MFE/MAE are outcome measurements only and never alter the reconstructed decision path.

## Cohort

| Market | 24h | First BUILDING | First CONFIRMED | First gate / BUY | Primary cause | Remaining to anchor after decision | 4h MFE after decision |
|---|---:|---|---|---|---|---:|---:|
| RLC-EUR | 92.66% | 0.40154000 | 0.51568000 | STRUCTURAL_STOP_TOO_WIDE | `GATE_STRUCTURAL_STOP_TOO_WIDE` | 20.43% | 5.69% |
| ZEUS-EUR | 83.34% | 0.00232500 | 0.00364980 | SPREAD_TOO_WIDE | `GATE_SPREAD_TOO_WIDE` | 2.93% | 36.99% (partial) |
| RAD-EUR | 30.01% | — | 0.23960000 | INSUFFICIENT_EXECUTION_LIQUIDITY | `GATE_INSUFFICIENT_EXECUTION_LIQUIDITY` | 28.16% | 30.98% |
| NIL-EUR | 28.57% | — | 0.08332100 | BUY_SENT | `CAPTURED_BUY` | 15.48% | 12.33% |
| PNT-EUR | 23.07% | 0.06467700 | — | — | `BUILDING_NEVER_CONFIRMED` | -6.20% | -1.05% (partial) |
| FLUID-EUR | 23.03% | — | 1.95980000 | STRUCTURAL_RANGE_TOO_NARROW | `GATE_STRUCTURAL_RANGE_TOO_NARROW` | -1.85% | 2.05% |
| MOVR-EUR | 18.28% | 1.68000000 | 1.74650000 | STRUCTURAL_STOP_TOO_WIDE | `GATE_STRUCTURAL_STOP_TOO_WIDE` | 1.89% | 22.36% |
| DIA-EUR | 16.20% | — | 0.14861000 | BUY_SENT | `CAPTURED_BUY` | 5.11% | 5.11% (partial) |
| GTC-EUR | 15.74% | 0.14921500 | 0.15987400 | SPREAD_TOO_WIDE | `GATE_SPREAD_TOO_WIDE` | 4.90% | 35.75% |
| CARV-EUR | 14.59% | — | — | — | `DETECTOR_NEVER_BUILDING` | —% | —% (partial) |
| ORCA-EUR | 13.83% | 1.80769000 | 1.86261000 | STRUCTURAL_RANGE_TOO_NARROW | `GATE_STRUCTURAL_RANGE_TOO_NARROW` | 6.42% | 9.42% (partial) |
| EDU-EUR | 13.74% | — | 0.04910000 | BUY_SENT | `CAPTURED_BUY` | -3.66% | 2.12% (partial) |
| CAP-EUR | 13.48% | 0.06075700 | 0.06491890 | STRUCTURAL_RANGE_TOO_NARROW | `GATE_STRUCTURAL_RANGE_TOO_NARROW` | 0.26% | 2.13% (partial) |
| FIL-EUR | 13.46% | 0.98878000 | 1.02709000 | BUY_SENT | `CAPTURED_BUY` | 3.26% | 3.57% (partial) |
| LIGHTER-EUR | 12.60% | 3.48310000 | — | — | `BUILDING_NEVER_CONFIRMED` | 4.40% | 3.07% |
| PARTI-EUR | 11.87% | — | 0.02597700 | BUY_SENT | `CAPTURED_BUY` | 3.01% | 4.76% |
| VELO-EUR | 10.67% | 0.00509940 | 0.00517140 | INSUFFICIENT_EXECUTION_LIQUIDITY | `GATE_INSUFFICIENT_EXECUTION_LIQUIDITY` | 3.89% | 3.40% |
| FLUX-EUR | 10.27% | 0.07035100 | — | — | `BUILDING_NEVER_CONFIRMED` | 6.27% | 4.64% |
| GRASS-EUR | 9.81% | 0.66459000 | — | — | `BUILDING_NEVER_CONFIRMED` | 1.52% | 4.15% (partial) |
| S-EUR | 8.92% | 0.03887100 | — | — | `BUILDING_NEVER_CONFIRMED` | 0.22% | 0.22% (partial) |

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

- **PNT-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 23.07%; largest observed scan gap 80.91 min.
- **CARV-EUR** — `DETECTOR_NEVER_BUILDING`; 24h 14.59%; largest observed scan gap 285.45 min.
- **LIGHTER-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 12.60%; largest observed scan gap 285.45 min.
- **FLUX-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 10.27%; largest observed scan gap 285.45 min.
- **GRASS-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 9.81%; largest observed scan gap 285.45 min.
- **S-EUR** — `BUILDING_NEVER_CONFIRMED`; 24h 8.92%; largest observed scan gap 285.45 min.

## Safety / interpretation

- `cadence_gap_flag` is diagnostic only; it does not prove a signal would have fired inside the missing interval.
- `INSUFFICIENT_EXECUTION_LIQUIDITY` currently occurs before the order book is fetched; those rows explicitly record `book_checked=false` when evidence confirms that path.
- A positive post-rejection MFE does not by itself prove that a safe fill was available. Spread, depth, structural stop and exchange lifecycle risks remain separate constraints.
- This audit is measurement-only and makes no production changes.
