# Audit qualité des données Bitvavo

Scan : 2026-09-20T08:36:08.909765+00:00 (20260920T083442Z-4abb9219)
Univers : 426 | strategy-grade : 32 | rejetés : 394
5m valides : 35 | 15m valides : 66 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 360 |
| MISSING_LATEST_CLOSED_CANDLE | 258 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 360 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2575585 | -1.60% | INVALID_5M | 99/1 | 99/0 |
| ZAMA-EUR | 2397767 | +11.00% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 2028839 | -24.61% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 100/0 |
| PUMP-EUR | 1676073 | -3.84% | INVALID_5M | 100/8 | 99/0 |
| DOGE-EUR | 1637447 | -2.73% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1390965 | -0.05% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1266871 | -0.70% | INVALID_5M | 99/1 | 99/0 |
| EPIC-EUR | 1109025 | +8.89% | INVALID_15M, INVALID_5M | 99/4 | 99/1 |
| CAKE-EUR | 1084865 | +0.23% | INVALID_15M, INVALID_5M | 83/4 | 99/5 |
| STX-EUR | 1005966 | +11.12% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| APT-EUR | 964715 | +2.99% | INVALID_15M, INVALID_5M | 100/7 | 99/1 |
| VET-EUR | 905819 | -3.25% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 877593 | -7.13% | INVALID_5M | 99/3 | 99/0 |
| FIL-EUR | 853669 | -2.23% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/7 | 100/2 |
| BCH-EUR | 797523 | -0.94% | INVALID_15M, INVALID_5M | 87/12 | 99/1 |
| SAGA-EUR | 791707 | +9.70% | INVALID_5M | 99/1 | 99/0 |
| KAS-EUR | 782961 | +4.52% | INVALID_15M, INVALID_5M | 95/2 | 99/7 |
| JUP-EUR | 737012 | -0.69% | INVALID_15M, INVALID_5M | 99/5 | 99/1 |
| SHIB-EUR | 719794 | -1.16% | INVALID_15M, INVALID_5M | 99/4 | 99/2 |
| SKL-EUR | 690144 | +18.19% | INVALID_5M | 99/1 | 95/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
