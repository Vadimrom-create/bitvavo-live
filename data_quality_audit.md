# Audit qualité des données Bitvavo

Scan : 2026-09-20T17:48:36.536299+00:00 (20260920T174705Z-f64ea5f0)
Univers : 426 | strategy-grade : 43 | rejetés : 383
5m valides : 49 | 15m valides : 82 | deux intervalles valides : 45

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 377 |
| INVALID_15M | 344 |
| MISSING_LATEST_CLOSED_CANDLE | 266 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 377 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 344 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| CAKE-EUR | 1356572 | +3.88% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 100/0 |
| UNI-EUR | 1308125 | +0.64% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 959644 | +3.16% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 892292 | +4.81% | INVALID_15M, INVALID_5M | 100/6 | 100/3 |
| SKL-EUR | 810927 | +7.97% | INVALID_5M | 99/3 | 99/0 |
| FIL-EUR | 788087 | -12.24% | INVALID_15M, INVALID_5M | 100/3 | 100/3 |
| SHIB-EUR | 775579 | -1.17% | INVALID_5M | 99/3 | 99/0 |
| S-EUR | 756620 | +13.87% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 732441 | +2.86% | INVALID_5M | 99/4 | 99/0 |
| ZIL-EUR | 712081 | +5.40% | INVALID_15M, INVALID_5M | 99/13 | 99/2 |
| XPL-EUR | 665313 | -1.29% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| KMNO-EUR | 657858 | +13.25% | INVALID_15M | 90/0 | 99/2 |
| POL-EUR | 606364 | +2.91% | INVALID_5M | 99/3 | 99/0 |
| BCH-EUR | 590680 | -0.86% | INVALID_15M, INVALID_5M | 98/8 | 99/1 |
| TIA-EUR | 575465 | +2.24% | INVALID_15M, INVALID_5M | 99/9 | 99/1 |
| GRASS-EUR | 571688 | +3.74% | INVALID_5M | 99/3 | 99/0 |
| VVV-EUR | 564578 | +4.20% | INVALID_5M | 100/3 | 100/0 |
| NPC-EUR | 550604 | +3.65% | INVALID_5M | 99/2 | 99/0 |
| JUP-EUR | 549233 | +1.81% | INVALID_5M | 99/2 | 99/0 |
| CRV-EUR | 500827 | +3.39% | INVALID_15M, INVALID_5M | 85/6 | 100/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
