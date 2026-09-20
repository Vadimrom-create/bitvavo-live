# Audit qualité des données Bitvavo

Scan : 2026-09-20T16:50:13.594690+00:00 (20260920T164841Z-4c8f37cd)
Univers : 426 | strategy-grade : 36 | rejetés : 390
5m valides : 39 | 15m valides : 79 | deux intervalles valides : 36

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 387 |
| INVALID_15M | 347 |
| MISSING_LATEST_CLOSED_CANDLE | 135 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 387 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 347 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| WLD-EUR | 1677390 | +2.03% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1326759 | +3.59% | INVALID_5M | 100/9 | 99/0 |
| LSK-EUR | 1231950 | -3.98% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1031130 | +1.46% | INVALID_5M | 99/2 | 99/0 |
| STRK-EUR | 951188 | +5.87% | INVALID_5M | 99/2 | 99/0 |
| RENDER-EUR | 897155 | +8.94% | INVALID_15M | 99/0 | 99/1 |
| DOT-EUR | 895935 | +3.57% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 894654 | +3.46% | INVALID_15M, INVALID_5M | 99/9 | 99/3 |
| FIL-EUR | 835588 | -7.58% | INVALID_15M, INVALID_5M | 97/7 | 99/4 |
| SKL-EUR | 796990 | +6.31% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 765858 | +1.45% | INVALID_5M | 99/4 | 99/0 |
| SHIB-EUR | 759566 | -0.99% | INVALID_5M | 99/5 | 99/0 |
| ZIL-EUR | 709325 | +5.74% | INVALID_15M, INVALID_5M | 100/22 | 100/2 |
| S-EUR | 702093 | +11.41% | INVALID_5M | 99/2 | 99/0 |
| AAVE-EUR | 656138 | -3.65% | INVALID_5M | 99/2 | 99/0 |
| USELESS-EUR | 648793 | -8.21% | INVALID_5M | 99/2 | 99/0 |
| BCH-EUR | 635593 | -1.93% | INVALID_15M, INVALID_5M | 95/6 | 99/1 |
| POL-EUR | 582436 | +0.73% | INVALID_5M | 100/4 | 99/0 |
| VVV-EUR | 568539 | +1.50% | INVALID_5M | 99/1 | 99/0 |
| GRASS-EUR | 565652 | +3.40% | INVALID_5M | 99/8 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
