# Solaire Human/Swing precision audit

Generated: 2026-10-07T23:10:45.477486+00:00
Measurement only. No production behavior changed.

## Baseline vs Solaire signal precision

Success below means the price reached the target at least once within the forward window (MFE).

| Source | Horizon | N | Close >0 | Hit +5 | Hit +10 | Hit +20 | Hit +30 | Median MFE | Median MAE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BASELINE | 24h | 12223 | 54.50% | 31.18% | 11.06% | 3.40% | 1.58% | 3.09% | -2.38% |
| BASELINE | 48h | 11814 | 54.31% | 48.55% | 22.55% | 7.43% | 3.42% | 4.81% | -3.37% |
| BASELINE | 72h | 11393 | 58.18% | 58.91% | 33.07% | 11.92% | 5.69% | 6.45% | -4.25% |
| BASELINE | 168h | 9697 | 68.30% | 79.12% | 59.26% | 31.28% | 16.86% | 12.71% | -5.68% |
| V4 WATCH episodes | 24h | 16616 | 53.62% | 36.64% | 14.03% | 3.57% | 1.44% | 3.60% | -2.79% |
| V4 WATCH episodes | 48h | 16490 | 56.12% | 53.69% | 26.96% | 8.36% | 3.69% | 5.51% | -3.83% |
| V4 WATCH episodes | 72h | 16227 | 59.24% | 63.25% | 36.74% | 13.22% | 6.11% | 7.21% | -4.59% |
| V4 WATCH episodes | 168h | 14399 | 67.89% | 81.57% | 62.00% | 33.78% | 18.61% | 13.65% | -5.95% |
| V4 ENTRY episodes | 24h | 8743 | 51.90% | 38.69% | 15.20% | 3.55% | 1.32% | 3.77% | -2.97% |
| V4 ENTRY episodes | 48h | 8707 | 54.29% | 54.29% | 28.66% | 9.04% | 3.65% | 5.65% | -4.11% |
| V4 ENTRY episodes | 72h | 8617 | 58.07% | 63.83% | 38.08% | 14.96% | 6.84% | 7.40% | -4.98% |
| V4 ENTRY episodes | 168h | 7677 | 68.26% | 81.80% | 63.55% | 36.51% | 20.91% | 14.35% | -6.44% |
| V4 BUY_READY episodes | 24h | 1719 | 51.02% | 37.75% | 14.60% | 2.73% | 0.81% | 3.63% | -3.05% |
| V4 BUY_READY episodes | 48h | 1716 | 51.63% | 52.21% | 26.81% | 7.52% | 2.51% | 5.32% | -4.34% |
| V4 BUY_READY episodes | 72h | 1705 | 54.84% | 61.64% | 36.01% | 11.96% | 5.04% | 7.03% | -5.34% |
| V4 BUY_READY episodes | 168h | 1538 | 65.15% | 78.93% | 60.34% | 34.01% | 17.04% | 13.12% | -6.59% |
| ACCELERATION episodes | 24h | 2833 | 43.17% | 45.04% | 23.61% | 9.28% | 5.15% | 4.31% | -4.41% |
| ACCELERATION episodes | 48h | 2803 | 45.52% | 57.44% | 33.39% | 15.38% | 8.95% | 6.27% | -5.80% |
| ACCELERATION episodes | 72h | 2725 | 46.28% | 64.07% | 39.41% | 18.79% | 11.38% | 7.52% | -6.66% |
| ACCELERATION episodes | 168h | 2251 | 49.40% | 78.76% | 57.35% | 32.39% | 20.48% | 12.02% | -8.15% |
| CONFIRMED ACCEL episodes | 24h | 931 | 37.49% | 50.91% | 29.54% | 13.96% | 8.49% | 5.12% | -5.95% |
| CONFIRMED ACCEL episodes | 48h | 918 | 37.58% | 59.69% | 38.56% | 19.17% | 11.33% | 6.87% | -7.78% |
| CONFIRMED ACCEL episodes | 72h | 894 | 38.48% | 65.66% | 44.63% | 21.59% | 13.65% | 8.30% | -8.56% |
| CONFIRMED ACCEL episodes | 168h | 740 | 40.95% | 78.24% | 59.73% | 34.73% | 22.43% | 12.80% | -10.23% |
| PIPELINE ACHETE episodes | 24h | 173 | 41.62% | 43.93% | 19.65% | 3.47% | 1.73% | 4.12% | -4.25% |
| PIPELINE ACHETE episodes | 48h | 173 | 48.55% | 55.49% | 32.95% | 7.51% | 2.89% | 6.21% | -5.49% |
| PIPELINE ACHETE episodes | 72h | 170 | 46.47% | 61.76% | 40.00% | 10.59% | 4.71% | 6.96% | -6.28% |
| PIPELINE ACHETE episodes | 168h | 150 | 55.33% | 74.00% | 55.33% | 30.67% | 16.00% | 11.98% | -7.75% |
| DL actionable episodes | 24h | 5705 | 47.41% | 37.67% | 16.00% | 4.80% | 2.14% | 3.59% | -3.45% |
| DL actionable episodes | 48h | 5553 | 48.28% | 52.19% | 26.71% | 9.87% | 4.92% | 5.26% | -4.93% |
| DL actionable episodes | 72h | 5343 | 50.53% | 61.00% | 34.64% | 13.78% | 7.30% | 6.64% | -5.96% |
| DL actionable episodes | 168h | 4533 | 54.93% | 75.95% | 53.67% | 28.13% | 16.85% | 10.94% | -7.33% |
| DL ACHETE_MAINTENANT episodes | 24h | 1018 | 48.23% | 35.36% | 12.77% | 2.65% | 0.98% | 3.41% | -3.08% |
| DL ACHETE_MAINTENANT episodes | 48h | 1016 | 49.02% | 48.82% | 23.62% | 6.59% | 2.17% | 4.91% | -4.37% |
| DL ACHETE_MAINTENANT episodes | 72h | 1006 | 51.19% | 57.75% | 30.62% | 9.05% | 3.88% | 6.25% | -5.60% |
| DL ACHETE_MAINTENANT episodes | 168h | 854 | 55.15% | 72.13% | 49.77% | 23.07% | 10.19% | 9.95% | -6.83% |

## Signal episode counts

- v4_watch: 16771
- v4_entry: 8789
- v4_buy_ready: 1721
- acceleration: 2922
- confirmed_acceleration: 968
- pipeline_buy: 173
- dl_actionable: 5828
- dl_buy_now: 1019

## WATCH features: 7d episodes that reached +20% vs misses

| Feature | Winner median | Miss median | Delta | Winner N | Miss N |
|---|---:|---:|---:|---:|---:|
| quote_volume_24h_eur | 160580.21 | 102923.93 | 57656.28 | 1784 | 5766 |
| ret14d | 11.70 | 15.43 | -3.73 | 4827 | 9480 |
| rs_btc_30d | 6.36 | 8.78 | -2.42 | 4786 | 9405 |
| confirm_count | 45.00 | 47.00 | -2.00 | 4864 | 9535 |
| rs_btc_7d | 8.61 | 6.83 | 1.77 | 4786 | 9405 |
| dist_ema50_pct | 14.47 | 16.02 | -1.55 | 4826 | 9472 |
| rs_btc_14d | 9.23 | 7.93 | 1.30 | 4786 | 9405 |
| ret7d | 12.28 | 11.30 | 0.98 | 4827 | 9480 |
| ret3d | 3.66 | 2.69 | 0.97 | 4827 | 9480 |
| rs_btc_3d | 3.07 | 2.14 | 0.93 | 4786 | 9405 |
| ret30d | 23.72 | 22.82 | 0.90 | 4827 | 9480 |
| since_first_signal_pct | 1.74 | 2.19 | -0.45 | 4864 | 9535 |
| ema20_slope_5d_pct | 4.48 | 4.84 | -0.36 | 4827 | 9480 |
| drawdown_30d_high_pct | -9.58 | -9.32 | -0.26 | 4827 | 9480 |
| breakout20_pct | -8.31 | -8.14 | -0.17 | 4827 | 9480 |
| entry_score | 5.70 | 5.55 | 0.15 | 4864 | 9535 |
| vol3_vs_prev20 | 0.85 | 0.77 | 0.08 | 4827 | 9480 |
| change_24h_pct | 1.55 | 1.50 | 0.05 | 4864 | 9535 |
| ignition_score | 8.05 | 8.08 | -0.03 | 4823 | 9460 |
| dist_ema20_pct | 9.40 | 9.38 | 0.02 | 4827 | 9480 |

## Method notes

- History: 630 hourly samples from 2104 committed journals.
- Decision Layer: 604 hourly samples from 2020 journals.
- Repeated hourly presence is collapsed into episodes; a new episode begins only after more than two hours without the state.
- Baseline is not a trading strategy; it is a neutral reference for how easy the market regime was.
- MFE is ex-post maximum favorable excursion, so hit rates measure opportunity presence, not realized PnL.
- Only complete forward windows are included.
