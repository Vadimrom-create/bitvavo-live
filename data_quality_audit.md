# Audit qualité des données Bitvavo

Scan : 2026-09-19T18:22:06.622604+00:00 (20260919T182031Z-35f38d72)
Univers : 427 | strategy-grade : 36 | rejetés : 391
5m valides : 37 | 15m valides : 100 | deux intervalles valides : 37

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 390 |
| INVALID_15M | 327 |
| MISSING_LATEST_CLOSED_CANDLE | 277 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 390 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 327 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| STRK-EUR | 2125141 | +10.64% | INVALID_5M | 99/4 | 99/0 |
| PUMP-EUR | 1955380 | -4.24% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1857338 | +4.83% | INVALID_5M | 99/3 | 99/0 |
| POL-EUR | 1534901 | +2.14% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1450767 | +1.93% | INVALID_5M | 99/2 | 99/0 |
| WLD-EUR | 1350587 | +3.14% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1227311 | +7.15% | INVALID_5M | 99/3 | 99/0 |
| SKY-EUR | 1063817 | -0.72% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/11 | 100/2 |
| F-EUR | 1016018 | -9.39% | INVALID_5M | 100/6 | 99/0 |
| DOT-EUR | 991732 | -0.51% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 986675 | +0.35% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 99/0 |
| SAGA-EUR | 953271 | +1.65% | INVALID_5M | 99/2 | 99/0 |
| AAVE-EUR | 897988 | +2.81% | INVALID_5M | 99/7 | 99/0 |
| COTI-EUR | 876695 | -3.47% | INVALID_5M | 100/4 | 99/0 |
| MORPHO-EUR | 818806 | +8.44% | INVALID_5M | 100/3 | 99/0 |
| KAS-EUR | 817738 | +7.95% | INVALID_5M | 99/1 | 99/0 |
| HEI-EUR | 803443 | +13.90% | INVALID_5M | 99/2 | 99/0 |
| JUP-EUR | 737757 | +4.73% | INVALID_5M | 99/9 | 99/0 |
| C-EUR | 694894 | +1.73% | INVALID_5M | 99/1 | 99/0 |
| RAY-EUR | 671114 | -1.50% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
