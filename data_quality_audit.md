# Audit qualité des données Bitvavo

Scan : 2026-09-19T20:38:09.648071+00:00 (20260919T203636Z-787d3abb)
Univers : 427 | strategy-grade : 31 | rejetés : 396
5m valides : 32 | 15m valides : 87 | deux intervalles valides : 31

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 395 |
| INVALID_15M | 340 |
| MISSING_LATEST_CLOSED_CANDLE | 293 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 395 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 340 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| CAP-EUR | 1984764 | -14.73% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1836456 | -4.81% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1720316 | +0.98% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/8 | 100/0 |
| LTC-EUR | 1562559 | +0.96% | INVALID_5M | 99/1 | 99/0 |
| ARB-EUR | 1498552 | -8.19% | INVALID_5M | 99/2 | 99/0 |
| USELESS-EUR | 1313353 | -11.31% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1272149 | +2.73% | INVALID_5M | 99/2 | 99/0 |
| OP-EUR | 1241347 | +3.15% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/8 | 100/0 |
| POL-EUR | 1101310 | -3.51% | INVALID_5M | 99/4 | 99/0 |
| SKY-EUR | 1047838 | -0.97% | INVALID_15M, INVALID_5M | 100/21 | 99/3 |
| BCH-EUR | 977175 | +0.22% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/14 | 99/1 |
| DOT-EUR | 935305 | -0.74% | INVALID_5M | 99/3 | 99/0 |
| AAVE-EUR | 933280 | +2.01% | INVALID_5M | 99/5 | 99/0 |
| HEI-EUR | 861696 | +15.31% | INVALID_5M | 99/2 | 99/0 |
| MORPHO-EUR | 840203 | +7.61% | INVALID_15M, INVALID_5M | 99/7 | 99/1 |
| SAGA-EUR | 839612 | -2.57% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 100/0 |
| COTI-EUR | 824452 | -8.39% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 100/0 |
| STX-EUR | 813097 | +8.94% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| FIL-EUR | 812785 | +10.49% | INVALID_5M | 100/1 | 99/0 |
| F-EUR | 788837 | -7.82% | INVALID_15M, INVALID_5M | 99/18 | 99/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
