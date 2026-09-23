# V2 entry timing variants

| Policy | n | mean net 24h | median MFE | median MAE | MFE >=10 | MAE <= -7 | stop proxy | positive |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline_snapshot | 37 | -1.75% | 5.94% | -6.39% | 11 | 16 | 14 | 8 |
| delay30 | 37 | -1.80% | 5.88% | -4.94% | 10 | 11 | 14 | 9 |
| delay60 | 37 | -1.94% | 6.33% | -5.49% | 9 | 14 | 14 | 9 |
| persist30_band_-2_+3 | 22 | -2.23% | 5.32% | -5.32% | 4 | 7 | 8 | 4 |
| persist60_band_-2_+3 | 14 | -3.18% | 5.92% | -5.33% | 2 | 5 | 6 | 2 |
| pullback2_reclaim1 | 23 | -1.74% | 6.06% | -4.17% | 6 | 8 | 10 | 8 |
| strength_score8_rel4_4_then_delay30 | 7 | -4.51% | 4.91% | -3.59% | 0 | 1 | 1 | 1 |
