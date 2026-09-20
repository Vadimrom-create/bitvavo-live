# Audit qualité des données Bitvavo

Scan : 2026-09-20T09:38:33.254132+00:00 (20260920T093634Z-915a51d6)
Univers : 426 | strategy-grade : 32 | rejetés : 394
5m valides : 37 | 15m valides : 67 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 389 |
| INVALID_15M | 359 |
| MISSING_LATEST_CLOSED_CANDLE | 291 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 389 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 359 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ZAMA-EUR | 2212817 | +9.12% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 2033411 | -24.97% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 1642975 | -2.77% | INVALID_5M | 99/4 | 99/0 |
| DOGE-EUR | 1575335 | -1.99% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1426271 | +1.28% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1116688 | +1.18% | INVALID_15M, INVALID_5M | 89/3 | 99/3 |
| EPIC-EUR | 1064060 | +8.56% | INVALID_5M | 99/2 | 99/0 |
| STX-EUR | 1009650 | +9.91% | INVALID_5M | 99/5 | 99/0 |
| APT-EUR | 854872 | +1.03% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/7 | 99/1 |
| USELESS-EUR | 850848 | -2.85% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 99/0 |
| FIL-EUR | 838398 | -2.10% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/5 | 100/2 |
| KAS-EUR | 817998 | +5.51% | INVALID_15M | 96/0 | 99/1 |
| SAGA-EUR | 809332 | +5.63% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 806567 | -0.97% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 794509 | -0.63% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 87/9 | 100/1 |
| SHIB-EUR | 729588 | -0.24% | INVALID_5M | 99/1 | 99/0 |
| SKL-EUR | 711501 | +17.23% | INVALID_5M | 99/1 | 95/0 |
| JUP-EUR | 697098 | -2.46% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 99/1 |
| COTI-EUR | 603567 | -9.64% | INVALID_15M, INVALID_5M | 90/16 | 99/2 |
| DRIFT-EUR | 599352 | -7.29% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
