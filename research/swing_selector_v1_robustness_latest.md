# Swing Selector v1 — temporal robustness

Version: SWING_SELECTOR_V1_FROZEN_2026-10-08
Generated: 2026-10-07T23:20:19.162059+00:00
**Not clean out-of-sample. True OOS starts now in swing_history/.**

| Selector | Horizon | N | Close >0 | Hit +10 | Hit +20 | Hit +30 | Med MFE | Med MAE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Baseline all markets | 24h | 5055 | 53.75% | 13.08% | 3.56% | 1.54% | 3.49% | -2.33% |
| Baseline all markets | 48h | 4962 | 52.42% | 23.92% | 7.72% | 3.51% | 5.24% | -3.48% |
| Baseline all markets | 72h | 4662 | 56.78% | 33.27% | 11.35% | 5.38% | 6.69% | -4.35% |
| Baseline all markets | 168h | 3432 | 58.65% | 55.22% | 25.55% | 13.23% | 11.08% | -5.44% |
| V4 ENTRY | 24h | 1330 | 51.88% | 15.04% | 3.38% | 1.43% | 4.04% | -3.01% |
| V4 ENTRY | 48h | 1315 | 51.33% | 27.15% | 8.67% | 3.73% | 5.67% | -4.28% |
| V4 ENTRY | 72h | 1278 | 53.36% | 35.05% | 13.54% | 6.42% | 6.94% | -5.38% |
| V4 ENTRY | 168h | 1008 | 57.94% | 54.56% | 27.08% | 14.88% | 11.09% | -6.90% |
| Swing top10 raw | 24h | 313 | 49.84% | 20.45% | 6.07% | 2.24% | 4.00% | -2.80% |
| Swing top10 raw | 48h | 295 | 53.22% | 33.56% | 11.86% | 5.42% | 5.91% | -3.74% |
| Swing top10 raw | 72h | 278 | 55.40% | 41.01% | 16.91% | 8.27% | 7.74% | -4.48% |
| Swing top10 raw | 168h | 210 | 63.33% | 65.24% | 38.57% | 19.52% | 14.10% | -6.16% |
| Swing HUMAN_REVIEW | 24h | 257 | 48.25% | 17.51% | 6.23% | 1.56% | 3.82% | -2.99% |
| Swing HUMAN_REVIEW | 48h | 245 | 54.29% | 29.80% | 11.02% | 4.49% | 5.94% | -3.94% |
| Swing HUMAN_REVIEW | 72h | 237 | 52.74% | 39.24% | 16.03% | 7.59% | 7.75% | -4.82% |
| Swing HUMAN_REVIEW | 168h | 175 | 64.00% | 64.00% | 38.86% | 19.43% | 13.23% | -6.46% |

## Temporal split (robustness only)

Cut: 2026-09-26T07:45:01+00:00

| Selector | Segment | 7d N | 7d close >0 | Hit +20 | Hit +30 |
|---|---|---:|---:|---:|---:|
| Baseline all markets | early_60pct | 2047 | 63.07% | 30.19% | 15.44% |
| Baseline all markets | late_40pct | 1385 | 52.13% | 18.70% | 9.96% |
| V4 ENTRY | early_60pct | 591 | 64.97% | 34.35% | 19.29% |
| V4 ENTRY | late_40pct | 417 | 47.96% | 16.79% | 8.63% |
| Swing top10 raw | early_60pct | 121 | 68.60% | 39.67% | 20.66% |
| Swing top10 raw | late_40pct | 89 | 56.18% | 37.08% | 17.98% |
| Swing HUMAN_REVIEW | early_60pct | 102 | 69.61% | 42.16% | 20.59% |
| Swing HUMAN_REVIEW | late_40pct | 73 | 56.16% | 34.25% | 17.81% |

## Notes

- No production behavior changed.
- News modifier is excluded historically because news snapshots were not archived.
- 5m/15m acceleration is not an input to the swing thesis.
- The forward live shadow history is the only clean OOS evidence for v1.
