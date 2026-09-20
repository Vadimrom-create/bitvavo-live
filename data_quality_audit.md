# Audit qualité des données Bitvavo

Scan : 2026-09-20T15:46:42.815566+00:00 (20260920T154515Z-de147776)
Univers : 426 | strategy-grade : 32 | rejetés : 394
5m valides : 34 | 15m valides : 73 | deux intervalles valides : 32

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 353 |
| MISSING_LATEST_CLOSED_CANDLE | 255 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 353 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| INJ-EUR | 2708529 | +5.68% | INVALID_5M | 99/1 | 100/0 |
| XLM-EUR | 1594496 | -2.29% | INVALID_5M | 99/1 | 100/0 |
| PUMP-EUR | 1481723 | -1.14% | INVALID_5M | 100/3 | 100/0 |
| WLD-EUR | 1467009 | -0.25% | INVALID_5M | 99/3 | 99/0 |
| UNI-EUR | 1360044 | -2.68% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1323049 | +3.00% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 100/0 |
| LSK-EUR | 1166921 | -10.21% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 963701 | -1.35% | INVALID_5M | 99/2 | 100/0 |
| STRK-EUR | 952486 | +4.39% | INVALID_5M | 99/2 | 99/0 |
| STX-EUR | 893957 | +0.64% | INVALID_15M, INVALID_5M | 100/11 | 100/2 |
| FIL-EUR | 859101 | -6.57% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 92/4 | 100/4 |
| DOT-EUR | 851717 | -1.42% | INVALID_5M | 100/1 | 100/0 |
| SKL-EUR | 787078 | +9.32% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 100/0 |
| SHIB-EUR | 737088 | -1.86% | INVALID_5M | 99/4 | 99/0 |
| ZIL-EUR | 700580 | +7.51% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/16 | 100/1 |
| APT-EUR | 693844 | -1.68% | INVALID_5M | 100/4 | 100/0 |
| USELESS-EUR | 640903 | -8.60% | INVALID_5M | 99/2 | 100/0 |
| BCH-EUR | 640376 | -3.35% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 89/16 | 100/2 |
| CAP-EUR | 617146 | -7.20% | INVALID_5M | 100/4 | 100/0 |
| DRIFT-EUR | 594557 | +3.92% | INVALID_15M, MISSING_LATEST_CLOSED_CANDLE | 100/0 | 100/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
