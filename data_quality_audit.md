# Audit qualité des données Bitvavo

Scan : 2026-09-20T13:54:53.093514+00:00 (20260920T135251Z-5e81b097)
Univers : 426 | strategy-grade : 35 | rejetés : 391
5m valides : 38 | 15m valides : 80 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 388 |
| INVALID_15M | 346 |
| MISSING_LATEST_CLOSED_CANDLE | 277 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 388 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 346 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| FET-EUR | 2117281 | -5.40% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 1465941 | -4.52% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 1457491 | -2.51% | INVALID_5M | 99/5 | 99/0 |
| WLD-EUR | 1435391 | -2.56% | INVALID_5M | 100/5 | 99/0 |
| CAKE-EUR | 1300513 | +3.57% | INVALID_5M | 98/5 | 99/0 |
| LSK-EUR | 1219358 | -13.79% | INVALID_5M | 98/1 | 99/0 |
| LTC-EUR | 1111185 | -1.54% | INVALID_5M | 98/5 | 99/0 |
| ARB-EUR | 1062301 | +0.21% | INVALID_5M | 99/2 | 99/0 |
| STX-EUR | 887692 | -0.99% | INVALID_15M, INVALID_5M | 99/17 | 99/2 |
| FIL-EUR | 878173 | -6.75% | INVALID_15M, INVALID_5M | 88/24 | 99/4 |
| DOT-EUR | 833505 | -2.71% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 98/3 | 99/0 |
| APT-EUR | 785972 | -1.79% | INVALID_5M | 99/4 | 99/0 |
| SHIB-EUR | 777553 | -2.37% | INVALID_5M | 99/3 | 99/0 |
| USELESS-EUR | 750248 | -3.37% | INVALID_5M | 98/3 | 99/0 |
| SKL-EUR | 740426 | +6.47% | INVALID_5M | 99/2 | 99/0 |
| BCH-EUR | 738644 | -2.67% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 90/13 | 100/2 |
| ZIL-EUR | 703844 | +6.72% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 100/0 |
| S-EUR | 668690 | +5.79% | INVALID_5M | 99/2 | 99/0 |
| DRIFT-EUR | 664457 | +3.28% | INVALID_15M, INVALID_5M | 99/7 | 99/1 |
| TIA-EUR | 584619 | -1.95% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/6 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
