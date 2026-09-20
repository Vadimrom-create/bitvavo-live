# Audit qualité des données Bitvavo

Scan : 2026-09-20T12:52:13.446350+00:00 (20260920T125040Z-9733bac2)
Univers : 426 | strategy-grade : 28 | rejetés : 398
5m valides : 31 | 15m valides : 78 | deux intervalles valides : 28

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 395 |
| INVALID_15M | 348 |
| MISSING_LATEST_CLOSED_CANDLE | 294 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 395 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 348 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| USDC-EUR | 2781632 | +0.01% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2692649 | +1.48% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 1966561 | -38.91% | INVALID_5M | 99/1 | 99/0 |
| FET-EUR | 1954938 | -7.07% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 1610666 | -5.27% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1483200 | -17.91% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1442294 | -3.88% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1421993 | -2.47% | INVALID_5M | 99/3 | 99/0 |
| WLD-EUR | 1421753 | -2.62% | INVALID_5M | 99/6 | 99/0 |
| LSK-EUR | 1223577 | -14.45% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1202454 | +1.77% | INVALID_5M | 99/7 | 99/0 |
| LTC-EUR | 1152160 | -1.54% | INVALID_5M | 99/3 | 99/0 |
| ARB-EUR | 1075582 | +0.59% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| STX-EUR | 895232 | -0.19% | INVALID_15M, INVALID_5M | 100/12 | 99/2 |
| FIL-EUR | 857034 | -4.30% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 85/25 | 100/3 |
| DOT-EUR | 847115 | -3.24% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 787343 | -1.73% | INVALID_5M | 100/5 | 99/0 |
| SHIB-EUR | 768349 | -2.26% | INVALID_5M | 99/2 | 99/0 |
| USELESS-EUR | 763247 | -3.57% | INVALID_5M | 99/3 | 99/0 |
| BCH-EUR | 745364 | -2.41% | INVALID_15M, INVALID_5M | 89/12 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
