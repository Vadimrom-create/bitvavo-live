# Audit qualité des données Bitvavo

Scan : 2026-09-20T08:19:46.541322+00:00 (20260920T081819Z-0b489c79)
Univers : 426 | strategy-grade : 32 | rejetés : 394
5m valides : 36 | 15m valides : 67 | deux intervalles valides : 34

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 390 |
| INVALID_15M | 359 |
| MISSING_LATEST_CLOSED_CANDLE | 241 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 390 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 359 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2583177 | -1.30% | INVALID_5M | 98/2 | 99/0 |
| ZAMA-EUR | 2433713 | +19.41% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| CAP-EUR | 2028508 | -25.11% | INVALID_5M | 99/1 | 100/0 |
| FET-EUR | 1959942 | -5.22% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1687292 | -3.41% | INVALID_5M | 99/7 | 99/0 |
| DOGE-EUR | 1653090 | -2.35% | INVALID_5M | 98/2 | 99/0 |
| WLD-EUR | 1391266 | +1.41% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| LTC-EUR | 1267856 | -0.11% | INVALID_5M | 99/2 | 99/0 |
| EPIC-EUR | 1070085 | +10.13% | INVALID_15M, INVALID_5M | 99/4 | 99/1 |
| CAKE-EUR | 1066753 | -0.91% | INVALID_15M, INVALID_5M | 81/2 | 100/5 |
| STX-EUR | 999208 | +11.22% | INVALID_5M | 98/3 | 99/0 |
| APT-EUR | 945089 | +3.26% | INVALID_15M, INVALID_5M | 98/15 | 99/1 |
| VET-EUR | 942002 | -2.36% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 865280 | -5.16% | INVALID_5M | 98/3 | 99/0 |
| FIL-EUR | 861999 | -2.31% | INVALID_15M, INVALID_5M | 99/9 | 99/2 |
| BCH-EUR | 805759 | -0.40% | INVALID_15M, INVALID_5M | 85/15 | 100/2 |
| KAS-EUR | 778237 | +4.12% | INVALID_15M, INVALID_5M | 94/2 | 99/7 |
| SAGA-EUR | 773965 | +10.71% | INVALID_5M | 99/1 | 99/0 |
| JUP-EUR | 740505 | -0.97% | INVALID_15M, INVALID_5M | 99/7 | 99/1 |
| SHIB-EUR | 722464 | -0.57% | INVALID_15M, INVALID_5M | 99/4 | 99/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
