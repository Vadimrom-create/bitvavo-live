# Audit qualité des données Bitvavo

Scan : 2026-09-20T15:59:53.043292+00:00 (20260920T155755Z-ab2b470e)
Univers : 426 | strategy-grade : 32 | rejetés : 394
5m valides : 33 | 15m valides : 73 | deux intervalles valides : 32

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 393 |
| INVALID_15M | 353 |
| MISSING_LATEST_CLOSED_CANDLE | 290 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 393 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 353 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| INJ-EUR | 2751378 | +7.38% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 1591009 | -1.99% | INVALID_5M | 98/1 | 99/0 |
| WLD-EUR | 1513837 | +1.13% | INVALID_5M | 98/3 | 99/0 |
| PUMP-EUR | 1470078 | -0.28% | INVALID_5M | 99/2 | 99/0 |
| UNI-EUR | 1362553 | -1.88% | INVALID_5M | 98/1 | 99/0 |
| CAKE-EUR | 1326264 | +2.85% | INVALID_5M | 99/6 | 99/0 |
| LSK-EUR | 1167733 | -6.54% | INVALID_5M | 98/1 | 99/0 |
| LTC-EUR | 970519 | -0.81% | INVALID_5M | 98/2 | 99/0 |
| STRK-EUR | 955904 | +3.05% | INVALID_5M | 98/2 | 99/0 |
| STX-EUR | 893570 | +1.47% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/11 | 100/2 |
| FIL-EUR | 854384 | -6.77% | INVALID_15M, INVALID_5M | 93/6 | 99/4 |
| DOT-EUR | 850074 | -1.33% | INVALID_5M | 99/2 | 99/0 |
| SKL-EUR | 787512 | +8.61% | INVALID_5M | 99/2 | 99/0 |
| SHIB-EUR | 746547 | -1.31% | INVALID_5M | 99/4 | 99/0 |
| ZIL-EUR | 700330 | +6.90% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/16 | 100/1 |
| APT-EUR | 679355 | -1.97% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 100/0 |
| USELESS-EUR | 636007 | -8.07% | INVALID_5M | 98/2 | 99/0 |
| BCH-EUR | 635723 | -2.12% | INVALID_15M, INVALID_5M | 90/17 | 99/2 |
| PTB-EUR | 606340 | +22.84% | INVALID_15M | 86/0 | 91/5 |
| CAP-EUR | 590804 | -6.01% | INVALID_5M | 98/4 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
