# V2 detection + Old timing counterfactual

V2 BUY_SENT: 60; Old matched: 60; hybrid greenlights: 3; skipped: 57.

## Old action at the exact V2 buy moment

| Old action | V2 buys | mature 24h | V2 stops | V2 TP1 | median MAE | median MFE | mean net close |
|---|---:|---:|---:|---:|---:|---:|---:|
| WATCH | 35 | 21 | 13 | 4 | -7.67% | 6.33% | -0.69% |
| ATTENDS_REPRISE_OU_REENTREE | 13 | 7 | 1 | 1 | -6.86% | 10.84% | -1.05% |
| LATENT_ACCELERATOR | 8 | 6 | 2 | 1 | -7.50% | 6.93% | -1.15% |
| VETO_STRUCTUREL | 4 | 3 | 1 | 0 | -7.23% | 9.76% | -1.87% |

## Counterfactual

| Policy | Horizon | n | mean net close | median MFE | median MAE | +10% MFE | positive net close | MAE <= -5% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| V2 actual | 4h | 58 | -0.80% | 3.17% | -3.66% | 8 | 12 | 23 |
| V2 detect + Old greenlight | 4h | 2 | 5.11% | 6.72% | -1.60% | 1 | 1 | 0 |
| V2 actual | 12h | 50 | -0.77% | 5.06% | -5.43% | 11 | 11 | 28 |
| V2 detect + Old greenlight | 12h | 2 | 2.81% | 7.81% | -1.60% | 1 | 1 | 0 |
| V2 actual | 24h | 37 | -0.93% | 8.28% | -7.25% | 14 | 9 | 26 |
| V2 detect + Old greenlight | 24h | 1 | -3.56% | 15.12% | -3.42% | 1 | 0 | 0 |
