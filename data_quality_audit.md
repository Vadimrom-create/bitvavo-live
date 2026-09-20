# Audit qualité des données Bitvavo

Scan : 2026-09-20T09:04:03.612164+00:00 (20260920T090238Z-9dffea25)
Univers : 426 | strategy-grade : 31 | rejetés : 395
5m valides : 35 | 15m valides : 68 | deux intervalles valides : 31

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 358 |
| MISSING_LATEST_CLOSED_CANDLE | 258 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 358 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2561921 | -1.42% | INVALID_5M | 99/1 | 99/0 |
| ZAMA-EUR | 2287809 | +9.16% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 2032638 | -25.90% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 1670520 | -3.89% | INVALID_5M | 99/6 | 99/0 |
| DOGE-EUR | 1597601 | -2.85% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1413304 | -0.54% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1280069 | -1.00% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1120723 | +2.77% | INVALID_15M, INVALID_5M | 86/4 | 99/4 |
| EPIC-EUR | 1078952 | +8.96% | INVALID_5M | 100/3 | 100/0 |
| STX-EUR | 1005437 | +10.10% | INVALID_5M | 99/5 | 99/0 |
| APT-EUR | 920496 | +1.85% | INVALID_15M, INVALID_5M | 100/7 | 100/1 |
| USELESS-EUR | 863246 | -3.47% | INVALID_5M | 99/3 | 100/0 |
| FIL-EUR | 858232 | -2.74% | INVALID_15M, INVALID_5M | 99/9 | 99/2 |
| DOT-EUR | 810300 | -2.45% | INVALID_5M | 99/1 | 99/0 |
| SAGA-EUR | 806063 | +8.14% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 804336 | -1.23% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 90/6 | 100/1 |
| KAS-EUR | 802131 | +4.61% | INVALID_15M, INVALID_5M | 95/1 | 99/2 |
| SHIB-EUR | 724901 | -1.34% | INVALID_5M | 99/2 | 99/0 |
| JUP-EUR | 721487 | -1.20% | INVALID_15M, INVALID_5M | 99/7 | 99/1 |
| SKL-EUR | 696509 | +16.93% | INVALID_5M | 99/1 | 95/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
