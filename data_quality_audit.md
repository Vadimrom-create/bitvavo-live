# Audit qualité des données Bitvavo

Scan : 2026-09-20T00:28:09.157351+00:00 (20260920T002639Z-fce5119a)
Univers : 427 | strategy-grade : 21 | rejetés : 406
5m valides : 23 | 15m valides : 68 | deux intervalles valides : 22

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 404 |
| INVALID_15M | 359 |
| MISSING_LATEST_CLOSED_CANDLE | 313 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 404 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 359 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 9753170 | -0.79% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| XLM-EUR | 2819481 | +0.48% | INVALID_5M | 99/1 | 99/0 |
| USDC-EUR | 2688073 | +0.02% | INVALID_5M | 99/4 | 99/0 |
| UNI-EUR | 2142665 | -2.79% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| CAP-EUR | 2047747 | -16.39% | INVALID_5M | 99/6 | 99/0 |
| PUMP-EUR | 1789881 | -0.50% | INVALID_5M | 99/5 | 99/0 |
| DOGE-EUR | 1627539 | -0.09% | INVALID_5M | 99/2 | 99/0 |
| HBAR-EUR | 1607238 | +2.57% | INVALID_5M | 100/2 | 99/0 |
| APT-EUR | 1494784 | -1.67% | INVALID_15M, INVALID_5M | 99/4 | 99/1 |
| LTC-EUR | 1487003 | -0.99% | INVALID_5M | 100/4 | 99/0 |
| WLD-EUR | 1451337 | +0.57% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |
| CNPY-EUR | 1449274 | -25.77% | INVALID_5M | 99/2 | 99/0 |
| STRK-EUR | 1341260 | +3.97% | INVALID_5M | 99/1 | 99/0 |
| EPIC-EUR | 1223249 | +12.12% | INVALID_5M | 100/1 | 99/0 |
| USELESS-EUR | 1144353 | -13.33% | INVALID_5M | 100/1 | 99/0 |
| OP-EUR | 1128406 | +1.21% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/18 | 99/0 |
| ARB-EUR | 1101074 | -8.39% | INVALID_5M | 99/2 | 99/0 |
| SKY-EUR | 991160 | -2.21% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 94/13 | 99/4 |
| FIL-EUR | 909533 | +0.01% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 99/0 |
| POL-EUR | 892482 | -0.23% | INVALID_5M | 99/6 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
