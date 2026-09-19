# Audit qualité des données Bitvavo

Scan : 2026-09-19T19:37:28.538668+00:00 (20260919T193552Z-4f64f5c1)
Univers : 427 | strategy-grade : 35 | rejetés : 392
5m valides : 35 | 15m valides : 97 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 330 |
| MISSING_LATEST_CLOSED_CANDLE | 300 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 330 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| CAP-EUR | 1975225 | -12.73% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 1945980 | +5.35% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 1878787 | -5.18% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| APT-EUR | 1809376 | +5.19% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 100/0 |
| ARB-EUR | 1691084 | -7.18% | INVALID_5M | 100/2 | 99/0 |
| LTC-EUR | 1491533 | +1.63% | INVALID_5M | 99/2 | 99/0 |
| POL-EUR | 1392600 | -1.46% | INVALID_5M | 100/4 | 99/0 |
| OP-EUR | 1230784 | +6.64% | INVALID_5M | 99/8 | 99/0 |
| SKY-EUR | 1047779 | -1.36% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/18 | 100/3 |
| BCH-EUR | 982618 | +0.59% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 100/0 |
| DOT-EUR | 941776 | -0.04% | INVALID_5M | 99/3 | 99/0 |
| AAVE-EUR | 907806 | +2.79% | INVALID_5M | 99/4 | 99/0 |
| SAGA-EUR | 892886 | -1.05% | INVALID_5M | 99/6 | 99/0 |
| F-EUR | 884012 | -8.03% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/12 | 100/1 |
| COTI-EUR | 877449 | -5.51% | INVALID_5M | 100/5 | 99/0 |
| MORPHO-EUR | 832343 | +8.69% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 100/0 |
| KAS-EUR | 809898 | +5.49% | INVALID_5M | 100/2 | 99/0 |
| JUP-EUR | 737341 | +4.49% | INVALID_5M | 99/5 | 99/0 |
| C-EUR | 736991 | +4.28% | INVALID_5M | 99/1 | 99/0 |
| BNB-EUR | 614571 | -0.39% | INVALID_5M | 99/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
