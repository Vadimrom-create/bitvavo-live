# Audit qualité des données Bitvavo

Scan : 2026-09-20T11:53:49.619820+00:00 (20260920T115216Z-4c36639d)
Univers : 426 | strategy-grade : 25 | rejetés : 401
5m valides : 25 | 15m valides : 77 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 401 |
| INVALID_15M | 349 |
| MISSING_LATEST_CLOSED_CANDLE | 291 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 401 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 349 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 6924630 | -0.81% | INVALID_5M | 99/1 | 99/0 |
| USDC-EUR | 3259564 | +0.03% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2641617 | +0.49% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2492376 | -2.07% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 2051022 | -32.95% | INVALID_5M | 99/5 | 99/0 |
| UNI-EUR | 1600512 | -3.69% | INVALID_5M | 99/3 | 99/0 |
| CNPY-EUR | 1515975 | -24.34% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1505616 | -3.66% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 1438346 | -2.27% | INVALID_5M | 99/2 | 99/0 |
| WLD-EUR | 1427543 | -1.93% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |
| CAKE-EUR | 1238406 | +0.86% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/2 |
| LSK-EUR | 1220057 | -14.36% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1190423 | -1.53% | INVALID_5M | 100/2 | 99/0 |
| ARB-EUR | 1103462 | +1.35% | INVALID_5M | 99/3 | 99/0 |
| STRK-EUR | 1036551 | +3.04% | INVALID_5M | 99/1 | 99/0 |
| EPIC-EUR | 1009045 | +8.09% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 928775 | -0.58% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/8 | 99/0 |
| FIL-EUR | 852453 | -3.64% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 86/19 | 100/2 |
| APT-EUR | 847910 | -2.41% | INVALID_5M | 99/8 | 99/0 |
| DOT-EUR | 830033 | -2.84% | INVALID_5M | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
