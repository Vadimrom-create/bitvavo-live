# Audit qualité des données Bitvavo

Scan : 2026-09-20T09:51:15.060593+00:00 (20260920T094948Z-f04a2f26)
Univers : 426 | strategy-grade : 33 | rejetés : 393
5m valides : 36 | 15m valides : 68 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 390 |
| INVALID_15M | 358 |
| MISSING_LATEST_CLOSED_CANDLE | 284 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 390 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 358 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ZAMA-EUR | 2207232 | +7.88% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 2030217 | -23.60% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 100/0 |
| PUMP-EUR | 1634813 | -3.45% | INVALID_5M | 100/4 | 99/0 |
| WLD-EUR | 1423441 | +0.88% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1140451 | +0.69% | INVALID_15M, INVALID_5M | 91/3 | 99/3 |
| EPIC-EUR | 1065853 | +11.28% | INVALID_5M | 100/2 | 99/0 |
| STX-EUR | 1020029 | +9.38% | INVALID_5M | 100/4 | 99/0 |
| USELESS-EUR | 864956 | -5.16% | INVALID_5M | 99/3 | 99/0 |
| APT-EUR | 856320 | +0.88% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/7 | 100/1 |
| FIL-EUR | 848742 | -1.42% | INVALID_15M, INVALID_5M | 99/8 | 99/2 |
| KAS-EUR | 810054 | +3.69% | INVALID_15M | 96/0 | 99/1 |
| SAGA-EUR | 809153 | +3.13% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 807577 | -1.38% | INVALID_5M | 100/1 | 99/0 |
| BCH-EUR | 790297 | -0.77% | INVALID_15M, INVALID_5M | 86/12 | 99/1 |
| SHIB-EUR | 729180 | -0.72% | INVALID_5M | 99/1 | 99/0 |
| SKL-EUR | 710681 | +14.33% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 95/0 |
| JUP-EUR | 687353 | -2.97% | INVALID_15M, INVALID_5M | 99/7 | 99/1 |
| COTI-EUR | 606888 | -10.52% | INVALID_15M, INVALID_5M | 91/15 | 99/1 |
| DRIFT-EUR | 598304 | -7.43% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 100/0 |
| POL-EUR | 597131 | +0.82% | INVALID_5M | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
