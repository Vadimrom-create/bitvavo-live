# Audit qualité des données Bitvavo

Scan : 2026-09-20T10:05:58.529094+00:00 (20260920T100428Z-3e446cea)
Univers : 426 | strategy-grade : 33 | rejetés : 393
5m valides : 37 | 15m valides : 69 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 389 |
| INVALID_15M | 357 |
| MISSING_LATEST_CLOSED_CANDLE | 237 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 389 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 357 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ZAMA-EUR | 2198053 | +11.64% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 2028673 | -23.54% | INVALID_5M | 100/6 | 99/0 |
| DOGE-EUR | 1571549 | -2.56% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1449849 | -4.75% | INVALID_5M | 99/2 | 99/0 |
| WLD-EUR | 1430528 | -0.15% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1152517 | +0.73% | INVALID_15M, INVALID_5M | 92/3 | 99/3 |
| EPIC-EUR | 1064954 | +10.62% | INVALID_5M | 99/1 | 100/0 |
| STX-EUR | 1037026 | +8.27% | INVALID_5M | 100/4 | 99/0 |
| APT-EUR | 876980 | -0.24% | INVALID_15M, INVALID_5M | 100/7 | 99/1 |
| USELESS-EUR | 860298 | -5.02% | INVALID_5M | 100/3 | 99/0 |
| FIL-EUR | 853512 | -1.57% | INVALID_15M, INVALID_5M | 99/9 | 100/2 |
| KAS-EUR | 812122 | +3.34% | INVALID_15M | 96/0 | 99/1 |
| SAGA-EUR | 810228 | +2.94% | INVALID_5M | 100/1 | 99/0 |
| DOT-EUR | 810064 | -1.81% | INVALID_5M | 100/1 | 99/0 |
| BCH-EUR | 768229 | -0.95% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 85/12 | 100/1 |
| SHIB-EUR | 735337 | -0.97% | INVALID_5M | 99/1 | 99/0 |
| SKL-EUR | 709348 | +17.10% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 96/0 |
| JUP-EUR | 671973 | -3.45% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 100/1 |
| COTI-EUR | 604962 | -9.65% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 89/15 | 100/1 |
| DRIFT-EUR | 599271 | -7.93% | INVALID_5M | 100/6 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
