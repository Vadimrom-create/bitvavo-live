# Audit qualité des données Bitvavo

Scan : 2026-09-20T17:21:04.436584+00:00 (20260920T171936Z-ba6f1ed7)
Univers : 426 | strategy-grade : 40 | rejetés : 386
5m valides : 45 | 15m valides : 82 | deux intervalles valides : 40

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 381 |
| INVALID_15M | 344 |
| MISSING_LATEST_CLOSED_CANDLE | 269 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 381 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 344 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| WLD-EUR | 1729152 | +0.94% | INVALID_5M | 100/1 | 99/0 |
| CAKE-EUR | 1342359 | +3.66% | INVALID_5M | 99/8 | 99/0 |
| LSK-EUR | 1244491 | -5.62% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 955111 | +8.20% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 934291 | +2.29% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 899880 | +4.18% | INVALID_15M, INVALID_5M | 99/9 | 99/3 |
| SKL-EUR | 807978 | +6.81% | INVALID_5M | 100/3 | 99/0 |
| FIL-EUR | 781359 | -11.76% | INVALID_15M, INVALID_5M | 99/6 | 99/4 |
| S-EUR | 754042 | +12.28% | INVALID_5M | 99/2 | 99/0 |
| SHIB-EUR | 747165 | -2.92% | INVALID_5M | 99/3 | 99/0 |
| APT-EUR | 742186 | +1.14% | INVALID_5M | 99/4 | 99/0 |
| ZIL-EUR | 713982 | +6.25% | INVALID_15M, INVALID_5M | 100/20 | 99/2 |
| AAVE-EUR | 664005 | -4.82% | INVALID_5M | 99/1 | 99/0 |
| XPL-EUR | 655594 | -1.94% | INVALID_5M | 99/2 | 99/0 |
| POL-EUR | 625397 | +1.19% | INVALID_5M | 99/3 | 99/0 |
| KMNO-EUR | 601822 | +15.81% | INVALID_15M, INVALID_5M | 87/8 | 99/2 |
| BCH-EUR | 593386 | -1.61% | INVALID_15M, INVALID_5M | 97/6 | 99/1 |
| TIA-EUR | 586114 | -0.02% | INVALID_15M, INVALID_5M | 100/7 | 99/1 |
| GRASS-EUR | 579494 | +3.81% | INVALID_5M | 99/6 | 99/0 |
| VVV-EUR | 562867 | +0.88% | INVALID_5M | 99/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
