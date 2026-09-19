# Audit qualité des données Bitvavo

Scan : 2026-09-19T15:19:15.097339+00:00 (20260919T151749Z-a1b8036f)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 36 | 15m valides : 82 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 345 |
| MISSING_LATEST_CLOSED_CANDLE | 248 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 345 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| SYN-EUR | 2464113 | +31.28% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2258359 | +24.03% | INVALID_5M | 99/2 | 99/0 |
| ARB-EUR | 2059135 | +0.91% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1829396 | +9.29% | INVALID_5M | 99/2 | 99/0 |
| CAP-EUR | 1585308 | -10.51% | INVALID_15M | 87/0 | 99/2 |
| POL-EUR | 1581881 | +4.49% | INVALID_5M | 99/3 | 99/0 |
| SAGA-EUR | 1340412 | +27.83% | INVALID_5M | 99/3 | 99/0 |
| SKY-EUR | 1203440 | -2.88% | INVALID_5M | 99/6 | 99/0 |
| OP-EUR | 1201066 | +11.54% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/6 | 100/0 |
| AAVE-EUR | 1093932 | +3.78% | INVALID_5M | 99/2 | 99/0 |
| DOT-EUR | 986905 | -1.16% | INVALID_5M | 99/3 | 99/0 |
| BCH-EUR | 939299 | +0.42% | INVALID_5M | 99/5 | 99/0 |
| C-EUR | 906491 | +11.66% | INVALID_5M | 99/4 | 99/0 |
| COTI-EUR | 849685 | -1.40% | INVALID_5M | 99/3 | 99/0 |
| EPIC-EUR | 805242 | +27.84% | INVALID_5M | 99/4 | 99/0 |
| HEI-EUR | 789457 | +13.59% | INVALID_5M | 99/3 | 99/0 |
| JUP-EUR | 781014 | +8.21% | INVALID_5M | 99/3 | 99/0 |
| RAY-EUR | 780359 | +5.26% | INVALID_5M | 99/2 | 99/0 |
| MORPHO-EUR | 775695 | +11.37% | INVALID_5M | 100/1 | 100/0 |
| BNB-EUR | 736343 | +1.33% | INVALID_5M | 100/2 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
