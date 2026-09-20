# Audit qualité des données Bitvavo

Scan : 2026-09-20T13:06:54.748286+00:00 (20260920T130523Z-b6b35dd4)
Univers : 426 | strategy-grade : 28 | rejetés : 398
5m valides : 31 | 15m valides : 77 | deux intervalles valides : 28

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 395 |
| INVALID_15M | 349 |
| MISSING_LATEST_CLOSED_CANDLE | 287 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 395 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 349 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| USDC-EUR | 2802476 | +0.01% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2730595 | +3.00% | INVALID_5M | 100/1 | 99/0 |
| FET-EUR | 2047578 | -6.93% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 1847409 | -34.57% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 1568818 | -4.63% | INVALID_5M | 100/2 | 99/0 |
| CNPY-EUR | 1489281 | -17.31% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1432587 | -4.29% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1424383 | -2.99% | INVALID_5M | 99/6 | 99/0 |
| PUMP-EUR | 1421659 | -2.13% | INVALID_5M | 99/3 | 99/0 |
| LSK-EUR | 1215709 | -13.00% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1191488 | +2.43% | INVALID_5M | 99/6 | 99/0 |
| LTC-EUR | 1153027 | -1.41% | INVALID_5M | 100/3 | 99/0 |
| ARB-EUR | 1102474 | -0.73% | INVALID_5M | 99/3 | 99/0 |
| STX-EUR | 894278 | -0.04% | INVALID_15M, INVALID_5M | 100/14 | 99/2 |
| FIL-EUR | 851329 | -4.77% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 83/28 | 99/3 |
| DOT-EUR | 848345 | -2.81% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 785402 | -1.28% | INVALID_5M | 99/3 | 99/0 |
| SHIB-EUR | 775244 | -2.07% | INVALID_5M | 99/2 | 99/0 |
| USELESS-EUR | 765489 | -2.67% | INVALID_5M | 99/3 | 99/0 |
| BCH-EUR | 746228 | -1.96% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 90/12 | 100/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
