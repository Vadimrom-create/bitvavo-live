# Audit qualité des données Bitvavo

Scan : 2026-09-19T10:13:53.228701+00:00 (20260919T101158Z-333cf1be)
Univers : 427 | strategy-grade : 30 | rejetés : 397
5m valides : 33 | 15m valides : 78 | deux intervalles valides : 31

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 394 |
| INVALID_15M | 349 |
| MISSING_LATEST_CLOSED_CANDLE | 291 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 394 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 349 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| PUMP-EUR | 2423328 | -1.26% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2117853 | +25.96% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |
| APT-EUR | 1770121 | +10.77% | INVALID_5M | 99/1 | 99/0 |
| F-EUR | 1603454 | +28.62% | INVALID_5M | 100/3 | 99/0 |
| POL-EUR | 1592882 | +3.79% | INVALID_5M | 99/5 | 99/0 |
| SKY-EUR | 1498338 | +11.64% | INVALID_5M | 99/4 | 99/0 |
| CNPY-EUR | 1451999 | -0.04% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 1208068 | -2.93% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 1132687 | +2.55% | INVALID_5M | 99/2 | 99/0 |
| AAVE-EUR | 1130381 | +6.12% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1081321 | +11.08% | INVALID_5M | 99/4 | 99/0 |
| BCH-EUR | 1070069 | +0.01% | INVALID_5M | 100/10 | 99/0 |
| SAGA-EUR | 948468 | +27.96% | INVALID_5M | 99/1 | 99/0 |
| LPT-EUR | 893570 | +7.02% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 99/0 |
| COTI-EUR | 882728 | -7.97% | INVALID_5M | 99/5 | 99/0 |
| BNB-EUR | 865515 | +2.23% | INVALID_15M, INVALID_5M | 99/2 | 99/1 |
| MORPHO-EUR | 850574 | +18.01% | INVALID_5M | 99/1 | 99/0 |
| S-EUR | 812442 | +7.66% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/16 | 100/1 |
| SUPER-EUR | 805152 | +8.99% | INVALID_15M, INVALID_5M | 87/13 | 99/4 |
| C-EUR | 800638 | +13.87% | INVALID_5M | 99/5 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
