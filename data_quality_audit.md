# Audit qualité des données Bitvavo

Scan : 2026-09-20T17:38:42.491565+00:00 (20260920T173712Z-640f03c0)
Univers : 426 | strategy-grade : 41 | rejetés : 385
5m valides : 47 | 15m valides : 82 | deux intervalles valides : 41

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 379 |
| INVALID_15M | 344 |
| MISSING_LATEST_CLOSED_CANDLE | 265 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 379 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 344 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| WLD-EUR | 1777093 | +2.18% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1356815 | +3.45% | INVALID_5M | 99/7 | 99/0 |
| LSK-EUR | 1240695 | -6.79% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 970937 | +6.96% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 955890 | +3.36% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 892245 | +4.39% | INVALID_15M, INVALID_5M | 99/6 | 99/3 |
| FIL-EUR | 833699 | -12.20% | INVALID_15M, INVALID_5M | 99/3 | 99/4 |
| SKL-EUR | 808298 | +7.35% | INVALID_5M | 99/3 | 99/0 |
| SHIB-EUR | 776974 | -1.54% | INVALID_5M | 99/3 | 99/0 |
| S-EUR | 754074 | +13.80% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 726770 | +3.40% | INVALID_5M | 99/4 | 99/0 |
| ZIL-EUR | 712544 | +6.57% | INVALID_15M, INVALID_5M | 99/19 | 99/2 |
| AAVE-EUR | 666191 | -4.34% | INVALID_5M | 99/1 | 99/0 |
| KMNO-EUR | 635203 | +14.03% | INVALID_15M | 88/0 | 99/2 |
| POL-EUR | 610383 | +2.58% | INVALID_5M | 99/3 | 99/0 |
| BCH-EUR | 596308 | -1.26% | INVALID_15M, INVALID_5M | 98/7 | 99/1 |
| TIA-EUR | 586809 | +2.30% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/7 | 99/1 |
| GRASS-EUR | 572180 | +4.02% | INVALID_5M | 99/3 | 99/0 |
| VVV-EUR | 561063 | +2.53% | INVALID_5M | 99/3 | 99/0 |
| NPC-EUR | 544185 | +1.40% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
