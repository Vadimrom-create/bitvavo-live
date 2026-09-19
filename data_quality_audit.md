# Audit qualité des données Bitvavo

Scan : 2026-09-19T13:33:04.381941+00:00 (20260919T133129Z-26947ab5)
Univers : 427 | strategy-grade : 34 | rejetés : 393
5m valides : 37 | 15m valides : 84 | deux intervalles valides : 37

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 390 |
| INVALID_15M | 343 |
| MISSING_LATEST_CLOSED_CANDLE | 256 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 390 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 343 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 3057174 | +2.09% | INVALID_5M | 99/1 | 99/0 |
| ENA-EUR | 2600853 | +20.32% | INVALID_5M | 99/1 | 99/0 |
| G-EUR | 2581402 | +7.43% | INVALID_5M | 99/3 | 99/0 |
| LSK-EUR | 2193905 | -6.48% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1797905 | +6.81% | INVALID_5M | 99/3 | 99/0 |
| F-EUR | 1629791 | +27.44% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1623027 | +5.25% | INVALID_5M | 99/2 | 99/0 |
| SKY-EUR | 1393071 | +5.53% | INVALID_5M | 99/10 | 100/0 |
| AAVE-EUR | 1202888 | +2.45% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1180828 | +9.17% | INVALID_5M | 99/1 | 100/0 |
| BCH-EUR | 1070915 | +0.32% | INVALID_5M | 99/9 | 99/0 |
| DOT-EUR | 1054596 | -2.84% | INVALID_5M | 99/1 | 99/0 |
| RAY-EUR | 880819 | +9.03% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| HEI-EUR | 852404 | +29.39% | INVALID_5M | 99/1 | 99/0 |
| COTI-EUR | 839116 | -3.95% | MISSING_LATEST_CLOSED_CANDLE | 100/0 | 100/0 |
| C-EUR | 838727 | +14.95% | INVALID_5M | 100/6 | 100/0 |
| MORPHO-EUR | 817695 | +11.72% | INVALID_5M | 99/8 | 100/0 |
| LPT-EUR | 805681 | +5.91% | INVALID_5M | 99/6 | 100/0 |
| BNB-EUR | 800429 | +2.22% | INVALID_5M | 100/2 | 100/0 |
| JUP-EUR | 751981 | +5.03% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
