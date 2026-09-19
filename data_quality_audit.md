# Audit qualité des données Bitvavo

Scan : 2026-09-19T12:57:09.646894+00:00 (20260919T125541Z-b61e76ad)
Univers : 427 | strategy-grade : 38 | rejetés : 389
5m valides : 39 | 15m valides : 82 | deux intervalles valides : 38

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 388 |
| INVALID_15M | 345 |
| MISSING_LATEST_CLOSED_CANDLE | 277 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 388 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 345 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 3207855 | +5.47% | INVALID_5M | 99/1 | 99/0 |
| G-EUR | 2628083 | +5.57% | INVALID_5M | 99/3 | 99/0 |
| ENA-EUR | 2457860 | +20.28% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1823527 | +6.36% | INVALID_5M | 99/2 | 99/0 |
| F-EUR | 1625562 | +25.04% | INVALID_5M | 99/2 | 99/0 |
| POL-EUR | 1619762 | +4.28% | INVALID_5M | 99/5 | 99/0 |
| LTC-EUR | 1618482 | +4.95% | INVALID_5M | 99/2 | 99/0 |
| SKY-EUR | 1375677 | +6.76% | INVALID_5M | 100/9 | 99/0 |
| SAGA-EUR | 1298963 | +30.58% | INVALID_5M | 99/1 | 99/0 |
| AAVE-EUR | 1195793 | +3.66% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 1071742 | +1.20% | INVALID_5M | 100/9 | 99/0 |
| MORPHO-EUR | 838742 | +12.01% | INVALID_5M | 100/8 | 99/0 |
| HEI-EUR | 838118 | +29.44% | INVALID_5M | 99/1 | 99/0 |
| C-EUR | 831836 | +15.78% | INVALID_5M | 99/7 | 99/0 |
| LPT-EUR | 819720 | +5.57% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/9 | 99/0 |
| BNB-EUR | 806217 | +3.31% | INVALID_15M, INVALID_5M | 99/2 | 99/1 |
| EPIC-EUR | 748086 | +21.08% | INVALID_5M | 99/3 | 99/0 |
| LAPTOP-EUR | 746144 | -16.91% | INVALID_5M | 99/1 | 99/0 |
| SUPER-EUR | 732233 | +4.86% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/32 | 100/5 |
| ACH-EUR | 706048 | +13.03% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
