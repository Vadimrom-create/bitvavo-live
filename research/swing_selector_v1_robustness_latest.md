# Swing Selector v1 — temporal robustness

Version: SWING_SELECTOR_V1_FROZEN_2026-10-08_R2
Generated: 2026-10-07T23:25:15.317275+00:00
**Not clean out-of-sample. True OOS starts now in swing_history/.**

| Selector | Horizon | N | Close >0 | Hit +10 | Hit +20 | Hit +30 | Med MFE | Med MAE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Baseline all markets | 24h | 5051 | 53.79% | 13.09% | 3.56% | 1.54% | 3.50% | -2.33% |
| Baseline all markets | 48h | 4959 | 52.43% | 23.94% | 7.72% | 3.51% | 5.24% | -3.47% |
| Baseline all markets | 72h | 4659 | 56.75% | 33.29% | 11.35% | 5.39% | 6.70% | -4.35% |
| Baseline all markets | 168h | 3429 | 58.65% | 55.23% | 25.58% | 13.24% | 11.12% | -5.44% |
| V4 ENTRY | 24h | 1330 | 51.88% | 15.04% | 3.38% | 1.43% | 4.04% | -3.01% |
| V4 ENTRY | 48h | 1315 | 51.33% | 27.15% | 8.67% | 3.73% | 5.67% | -4.28% |
| V4 ENTRY | 72h | 1278 | 53.36% | 35.05% | 13.54% | 6.42% | 6.94% | -5.38% |
| V4 ENTRY | 168h | 1008 | 57.94% | 54.56% | 27.08% | 14.88% | 11.09% | -6.90% |
| Swing top10 raw | 24h | 313 | 49.84% | 20.77% | 5.75% | 2.24% | 4.02% | -2.81% |
| Swing top10 raw | 48h | 295 | 52.88% | 33.56% | 11.86% | 5.42% | 5.91% | -3.81% |
| Swing top10 raw | 72h | 278 | 55.76% | 40.65% | 16.91% | 8.27% | 7.88% | -4.58% |
| Swing top10 raw | 168h | 210 | 63.33% | 65.24% | 39.05% | 20.00% | 14.10% | -6.26% |
| Swing HUMAN_REVIEW | 24h | 258 | 48.45% | 17.83% | 5.81% | 1.55% | 3.88% | -3.00% |
| Swing HUMAN_REVIEW | 48h | 246 | 54.47% | 29.67% | 10.98% | 4.47% | 6.05% | -3.86% |
| Swing HUMAN_REVIEW | 72h | 238 | 53.36% | 38.66% | 15.97% | 7.56% | 7.75% | -4.79% |
| Swing HUMAN_REVIEW | 168h | 176 | 64.20% | 64.20% | 38.64% | 19.32% | 13.17% | -6.46% |

## Temporal split (robustness only)

Cut: 2026-09-26T07:56:37.600000+00:00

| Selector | Segment | 7d N | 7d close >0 | Hit +20 | Hit +30 |
|---|---|---:|---:|---:|---:|
| Baseline all markets | early_60pct | 2045 | 63.03% | 30.22% | 15.45% |
| Baseline all markets | late_40pct | 1384 | 52.17% | 18.71% | 9.97% |
| V4 ENTRY | early_60pct | 591 | 64.97% | 34.35% | 19.29% |
| V4 ENTRY | late_40pct | 417 | 47.96% | 16.79% | 8.63% |
| Swing top10 raw | early_60pct | 121 | 68.60% | 40.50% | 21.49% |
| Swing top10 raw | late_40pct | 89 | 56.18% | 37.08% | 17.98% |
| Swing HUMAN_REVIEW | early_60pct | 102 | 69.61% | 42.16% | 20.59% |
| Swing HUMAN_REVIEW | late_40pct | 74 | 56.76% | 33.78% | 17.57% |

## Notes

- No production behavior changed.
- News modifier is excluded historically because news snapshots were not archived.
- 5m/15m acceleration is not an input to the swing thesis.
- The forward live shadow history is the only clean OOS evidence for v1.
