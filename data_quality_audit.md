# Audit qualité des données Bitvavo

Scan : 2026-09-19T16:36:42.003697+00:00 (20260919T163439Z-902cb991)
Univers : 427 | strategy-grade : 31 | rejetés : 396
5m valides : 36 | 15m valides : 86 | deux intervalles valides : 32

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 341 |
| MISSING_LATEST_CLOSED_CANDLE | 266 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 341 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| SYN-EUR | 2539499 | +30.70% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2178309 | +17.48% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1860671 | +7.70% | INVALID_5M | 100/2 | 99/0 |
| CAP-EUR | 1777104 | -12.35% | INVALID_15M | 97/0 | 99/2 |
| POL-EUR | 1563003 | +3.29% | INVALID_5M | 99/3 | 99/0 |
| WLD-EUR | 1548572 | -1.13% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 1461290 | +2.92% | INVALID_5M | 100/1 | 99/0 |
| SAGA-EUR | 1366907 | +20.21% | INVALID_5M | 99/3 | 99/0 |
| OP-EUR | 1206192 | +8.42% | INVALID_5M | 99/8 | 99/0 |
| F-EUR | 1166444 | -13.92% | INVALID_5M | 99/4 | 99/0 |
| SKY-EUR | 1098403 | -0.72% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/9 | 99/0 |
| AAVE-EUR | 1089827 | +2.66% | INVALID_5M | 99/5 | 99/0 |
| VET-EUR | 1065772 | +7.77% | INVALID_5M | 100/1 | 99/0 |
| BCH-EUR | 984760 | +1.58% | INVALID_5M | 99/3 | 99/0 |
| DOT-EUR | 944550 | -1.75% | INVALID_5M | 100/2 | 99/0 |
| COTI-EUR | 916984 | -3.00% | INVALID_5M | 99/2 | 99/0 |
| EPIC-EUR | 866678 | +24.76% | INVALID_5M | 99/1 | 99/0 |
| MORPHO-EUR | 803016 | +11.57% | INVALID_5M | 100/2 | 99/0 |
| JUP-EUR | 777377 | +6.73% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 100/0 |
| KAS-EUR | 772753 | +9.21% | INVALID_5M | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
