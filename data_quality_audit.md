# Audit qualité des données Bitvavo

Scan : 2026-09-20T01:20:38.932993+00:00 (20260920T011911Z-805087f7)
Univers : 427 | strategy-grade : 21 | rejetés : 406
5m valides : 22 | 15m valides : 66 | deux intervalles valides : 21

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 405 |
| INVALID_15M | 361 |
| MISSING_LATEST_CLOSED_CANDLE | 237 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 405 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 361 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 9348602 | -0.79% | INVALID_5M | 99/2 | 99/0 |
| XLM-EUR | 2741539 | +1.23% | INVALID_5M | 100/2 | 99/0 |
| USDC-EUR | 2709690 | +0.07% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 2069480 | -0.46% | INVALID_5M | 100/6 | 99/0 |
| CAP-EUR | 1999878 | -12.04% | INVALID_5M | 99/3 | 100/0 |
| PUMP-EUR | 1762272 | -0.21% | INVALID_5M | 100/7 | 99/0 |
| HBAR-EUR | 1690893 | +6.34% | INVALID_5M | 100/3 | 99/0 |
| DOGE-EUR | 1607365 | -0.30% | INVALID_5M | 100/2 | 99/0 |
| WLD-EUR | 1463699 | +1.56% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1447046 | +0.49% | INVALID_5M | 100/6 | 99/0 |
| CNPY-EUR | 1429274 | -19.42% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1409520 | -2.88% | INVALID_15M, INVALID_5M | 99/4 | 100/1 |
| STRK-EUR | 1276155 | +7.87% | INVALID_5M | 100/1 | 99/0 |
| EPIC-EUR | 1216633 | +9.58% | INVALID_5M | 100/3 | 100/0 |
| USELESS-EUR | 1113042 | -14.53% | INVALID_5M | 100/2 | 100/0 |
| OP-EUR | 1081019 | +3.42% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/22 | 99/2 |
| ARB-EUR | 1055325 | -6.71% | INVALID_5M | 100/3 | 99/0 |
| SKY-EUR | 923120 | -1.55% | INVALID_15M, INVALID_5M | 94/16 | 99/3 |
| FIL-EUR | 916328 | +0.34% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/7 | 100/0 |
| HEI-EUR | 885660 | +13.93% | INVALID_15M, INVALID_5M | 100/19 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
