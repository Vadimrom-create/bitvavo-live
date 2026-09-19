# Audit qualité des données Bitvavo

Scan : 2026-09-19T20:51:31.519356+00:00 (20260919T204929Z-78afabef)
Univers : 427 | strategy-grade : 32 | rejetés : 395
5m valides : 34 | 15m valides : 87 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 393 |
| INVALID_15M | 340 |
| MISSING_LATEST_CLOSED_CANDLE | 301 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 393 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 340 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| USDC-EUR | 2688784 | -0.05% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 100/0 |
| UNI-EUR | 2348014 | -4.57% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1847969 | -4.17% | INVALID_5M | 100/2 | 99/0 |
| APT-EUR | 1707588 | +0.31% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/11 | 100/0 |
| ARB-EUR | 1434371 | -8.75% | INVALID_5M | 100/2 | 99/0 |
| USELESS-EUR | 1292660 | -12.74% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1245066 | +2.55% | INVALID_5M | 100/2 | 99/0 |
| OP-EUR | 1230803 | +3.30% | INVALID_5M | 99/8 | 99/0 |
| POL-EUR | 1082704 | -3.13% | INVALID_5M | 100/5 | 99/0 |
| SKY-EUR | 1048667 | -1.85% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/22 | 100/3 |
| BCH-EUR | 968666 | -0.34% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/13 | 100/2 |
| DOT-EUR | 933774 | -1.21% | INVALID_5M | 99/4 | 99/0 |
| AAVE-EUR | 932511 | +1.11% | INVALID_5M | 100/5 | 99/0 |
| HEI-EUR | 861918 | +15.20% | INVALID_5M | 99/2 | 99/0 |
| MORPHO-EUR | 841355 | +7.80% | INVALID_15M, INVALID_5M | 99/7 | 99/1 |
| SAGA-EUR | 834981 | -3.04% | INVALID_5M | 99/9 | 99/0 |
| COTI-EUR | 830608 | -9.67% | INVALID_5M | 100/2 | 99/0 |
| STX-EUR | 812859 | +9.32% | INVALID_5M | 99/1 | 99/0 |
| FIL-EUR | 811672 | +11.13% | INVALID_5M | 99/1 | 99/0 |
| F-EUR | 782046 | -7.61% | INVALID_15M, INVALID_5M | 100/18 | 99/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
