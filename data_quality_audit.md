# Audit qualité des données Bitvavo

Scan : 2026-09-20T12:12:27.808606+00:00 (20260920T121104Z-87375667)
Univers : 426 | strategy-grade : 26 | rejetés : 400
5m valides : 27 | 15m valides : 75 | deux intervalles valides : 26

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 399 |
| INVALID_15M | 351 |
| MISSING_LATEST_CLOSED_CANDLE | 304 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 399 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 351 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 6842451 | -1.14% | INVALID_5M | 99/1 | 99/0 |
| USDC-EUR | 2856695 | +0.01% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2645365 | +1.11% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2473598 | -1.92% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 2006024 | -34.75% | INVALID_5M | 99/3 | 99/0 |
| UNI-EUR | 1596339 | -4.36% | INVALID_5M | 99/3 | 99/0 |
| CNPY-EUR | 1517882 | -23.40% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1493733 | -3.42% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1424513 | -1.92% | INVALID_5M | 99/3 | 99/0 |
| WLD-EUR | 1407617 | -2.00% | INVALID_5M | 99/4 | 99/0 |
| CAKE-EUR | 1233919 | +1.90% | INVALID_15M, INVALID_5M | 100/5 | 99/2 |
| LSK-EUR | 1229999 | -14.75% | INVALID_5M | 100/1 | 99/0 |
| LTC-EUR | 1177930 | -1.66% | INVALID_5M | 100/4 | 99/0 |
| ARB-EUR | 1102574 | +1.81% | INVALID_5M | 99/3 | 99/0 |
| STX-EUR | 911197 | -2.10% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/9 | 99/2 |
| FIL-EUR | 860161 | -3.55% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 88/22 | 99/2 |
| APT-EUR | 843980 | -1.62% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/5 | 99/0 |
| DOT-EUR | 835066 | -3.03% | INVALID_5M | 100/1 | 99/0 |
| USELESS-EUR | 797530 | -3.43% | INVALID_5M | 99/2 | 99/0 |
| BCH-EUR | 768527 | -1.61% | INVALID_15M, INVALID_5M | 84/18 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
