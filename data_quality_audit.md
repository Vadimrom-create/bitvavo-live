# Audit qualité des données Bitvavo

Scan : 2026-09-19T20:22:14.172121+00:00 (20260919T202047Z-32331336)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 33 | 15m valides : 87 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 394 |
| INVALID_15M | 340 |
| MISSING_LATEST_CLOSED_CANDLE | 285 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 394 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 340 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| CAP-EUR | 1984498 | -14.00% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1808487 | -5.65% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1762525 | +1.95% | INVALID_5M | 99/8 | 99/0 |
| ARB-EUR | 1599744 | -7.29% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1566337 | +1.06% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1271950 | +3.29% | INVALID_5M | 100/1 | 99/0 |
| OP-EUR | 1235717 | +4.92% | INVALID_5M | 99/8 | 99/0 |
| POL-EUR | 1112566 | -2.37% | INVALID_5M | 99/5 | 99/0 |
| SKY-EUR | 1050923 | -1.64% | INVALID_15M, INVALID_5M | 99/21 | 99/3 |
| BCH-EUR | 978727 | +0.35% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/10 | 100/1 |
| AAVE-EUR | 932038 | +1.70% | INVALID_5M | 99/7 | 99/0 |
| DOT-EUR | 931909 | -0.66% | INVALID_5M | 99/3 | 99/0 |
| SAGA-EUR | 865552 | -5.14% | INVALID_5M | 99/6 | 99/0 |
| HEI-EUR | 857630 | +14.54% | INVALID_5M | 100/2 | 99/0 |
| MORPHO-EUR | 838566 | +7.50% | INVALID_15M, INVALID_5M | 99/7 | 99/1 |
| COTI-EUR | 832376 | -7.96% | INVALID_5M | 99/1 | 99/0 |
| FIL-EUR | 813982 | +10.79% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 812938 | +9.95% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| F-EUR | 797552 | -8.37% | INVALID_15M, INVALID_5M | 100/17 | 99/2 |
| KAS-EUR | 790155 | +6.48% | INVALID_5M | 99/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
