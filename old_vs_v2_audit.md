# Old vs Solaire V2 — archived snapshot audit

Snapshots: 369 from 2026-09-20.

Old reference commit: `3628856b6dceb27f82d0cceac960348c38933eed`.

## OLD_DECISION_LAYER

| Horizon | n | mean net close | median MFE | median MAE | +10% MFE | positive net close | Σ PnL / 100€ signals |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 4h | 307 | -1.06% | 1.01% | -1.19% | 0 | 112 | -325.87 € |
| 24h | 222 | 0.91% | 4.09% | -2.25% | 40 | 117 | 203.01 € |
| 48h | 140 | 5.09% | 8.10% | -2.64% | 60 | 96 | 712.25 € |
| 72h | 56 | 8.85% | 12.93% | -2.88% | 36 | 48 | 495.80 € |

## Method note

This is a same-archive signal-quality comparison. It does not claim actual executable account PnL; overlapping hypothetical positions are summed independently. V2 delivered emails are reported separately when the archive contains DELIVERY_COMPLETED state.
