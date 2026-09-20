# Audit qualité des données Bitvavo

Scan : 2026-09-20T17:03:40.584811+00:00 (20260920T170212Z-719b9402)
Univers : 426 | strategy-grade : 38 | rejetés : 388
5m valides : 41 | 15m valides : 81 | deux intervalles valides : 38

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 385 |
| INVALID_15M | 345 |
| MISSING_LATEST_CLOSED_CANDLE | 203 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 385 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 345 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| WLD-EUR | 1729183 | +2.55% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1333353 | +3.47% | INVALID_5M | 99/9 | 99/0 |
| LSK-EUR | 1239163 | -5.25% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1094382 | +1.90% | INVALID_5M | 99/2 | 99/0 |
| RENDER-EUR | 1056109 | +9.63% | INVALID_15M | 99/0 | 99/1 |
| STRK-EUR | 939501 | +6.80% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 933579 | +2.61% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 895979 | +3.70% | INVALID_15M, INVALID_5M | 99/9 | 99/3 |
| FIL-EUR | 840147 | -10.94% | INVALID_15M, INVALID_5M | 99/7 | 100/4 |
| SKL-EUR | 800533 | +5.82% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 758339 | +1.04% | INVALID_5M | 99/4 | 99/0 |
| SHIB-EUR | 751481 | -1.74% | INVALID_5M | 99/3 | 99/0 |
| S-EUR | 722091 | +13.33% | INVALID_5M | 99/2 | 99/0 |
| ZIL-EUR | 712357 | +6.48% | INVALID_15M, INVALID_5M | 99/22 | 99/2 |
| AAVE-EUR | 656186 | -4.56% | INVALID_5M | 99/2 | 99/0 |
| BCH-EUR | 632011 | -1.68% | INVALID_15M, INVALID_5M | 96/6 | 100/1 |
| POL-EUR | 598608 | +1.24% | INVALID_5M | 99/5 | 99/0 |
| GRASS-EUR | 572171 | +3.60% | INVALID_5M | 99/8 | 100/0 |
| VVV-EUR | 569374 | +1.80% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 100/0 |
| XPL-EUR | 568267 | -2.55% | INVALID_5M | 99/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
