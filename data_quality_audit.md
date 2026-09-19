# Audit qualité des données Bitvavo

Scan : 2026-09-19T22:36:16.275985+00:00 (20260919T223443Z-857b334f)
Univers : 427 | strategy-grade : 32 | rejetés : 395
5m valides : 34 | 15m valides : 76 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 393 |
| INVALID_15M | 351 |
| MISSING_LATEST_CLOSED_CANDLE | 312 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 393 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 351 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| USDC-EUR | 2666304 | -0.07% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| UNI-EUR | 2194679 | -2.54% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 2027512 | -16.70% | MISSING_LATEST_CLOSED_CANDLE | 100/0 | 100/0 |
| PUMP-EUR | 1867916 | -3.89% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 100/0 |
| APT-EUR | 1688339 | -0.48% | INVALID_15M, INVALID_5M | 100/6 | 99/1 |
| CNPY-EUR | 1401441 | -20.52% | INVALID_5M | 100/1 | 99/0 |
| STRK-EUR | 1387681 | -0.90% | INVALID_5M | 99/3 | 99/0 |
| ARB-EUR | 1303368 | -6.46% | INVALID_5M | 100/1 | 99/0 |
| OP-EUR | 1226742 | +2.36% | INVALID_5M | 100/5 | 99/0 |
| SKY-EUR | 1062464 | -1.40% | INVALID_15M, INVALID_5M | 99/13 | 99/4 |
| POL-EUR | 1038408 | -1.60% | INVALID_5M | 100/6 | 99/0 |
| BCH-EUR | 967104 | -4.48% | INVALID_15M, INVALID_5M | 99/15 | 99/2 |
| DOT-EUR | 922129 | -2.43% | INVALID_5M | 100/2 | 99/0 |
| FIL-EUR | 887296 | +2.37% | INVALID_5M | 99/4 | 99/0 |
| AAVE-EUR | 878165 | +1.74% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 100/0 |
| HEI-EUR | 871594 | +11.90% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/7 | 100/0 |
| MORPHO-EUR | 847269 | +5.73% | INVALID_15M, INVALID_5M | 100/3 | 99/1 |
| STX-EUR | 828774 | +8.04% | INVALID_5M | 99/1 | 99/0 |
| SAGA-EUR | 821210 | +1.85% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/9 | 100/0 |
| COTI-EUR | 802304 | -11.14% | INVALID_5M | 100/9 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
