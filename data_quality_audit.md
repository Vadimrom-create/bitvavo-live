# Audit qualité des données Bitvavo

Scan : 2026-09-20T17:33:18.799354+00:00 (20260920T173150Z-b6c7551d)
Univers : 426 | strategy-grade : 40 | rejetés : 386
5m valides : 47 | 15m valides : 82 | deux intervalles valides : 41

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 379 |
| INVALID_15M | 344 |
| MISSING_LATEST_CLOSED_CANDLE | 244 |

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
| WLD-EUR | 1756659 | +0.85% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1355843 | +3.41% | INVALID_5M | 99/7 | 99/0 |
| LSK-EUR | 1240872 | -6.11% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 970645 | +7.58% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 966316 | +2.11% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 899692 | +4.58% | INVALID_15M, INVALID_5M | 100/6 | 100/3 |
| FIL-EUR | 844619 | -12.63% | INVALID_15M, INVALID_5M | 99/4 | 99/4 |
| SKL-EUR | 808026 | +7.35% | INVALID_5M | 99/3 | 100/0 |
| SHIB-EUR | 774707 | -2.37% | INVALID_5M | 99/3 | 100/0 |
| S-EUR | 754063 | +13.80% | INVALID_5M | 100/2 | 100/0 |
| APT-EUR | 740054 | +1.58% | INVALID_5M | 99/4 | 99/0 |
| ZIL-EUR | 712596 | +6.50% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/20 | 99/2 |
| AAVE-EUR | 669119 | -4.56% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 620968 | +2.00% | INVALID_5M | 99/3 | 99/0 |
| KMNO-EUR | 615484 | +14.94% | INVALID_15M, INVALID_5M | 88/5 | 99/2 |
| BCH-EUR | 595956 | -1.50% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 97/6 | 99/1 |
| TIA-EUR | 587578 | +1.25% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/7 | 100/1 |
| GRASS-EUR | 580529 | +3.63% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| VVV-EUR | 560615 | +2.63% | INVALID_5M | 99/3 | 99/0 |
| NPC-EUR | 546962 | +1.13% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
