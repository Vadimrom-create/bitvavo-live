# Audit qualité des données Bitvavo

Scan : 2026-09-20T13:24:30.600281+00:00 (20260920T132301Z-5d12a290)
Univers : 426 | strategy-grade : 28 | rejetés : 398
5m valides : 31 | 15m valides : 77 | deux intervalles valides : 29

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 395 |
| INVALID_15M | 349 |
| MISSING_LATEST_CLOSED_CANDLE | 296 |

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
| USDC-EUR | 2761498 | +0.06% | INVALID_5M | 98/1 | 99/0 |
| FET-EUR | 2074583 | -5.30% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 1659441 | -33.49% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 1545501 | -5.09% | INVALID_5M | 99/3 | 99/0 |
| CNPY-EUR | 1478340 | -12.99% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1431237 | -2.28% | INVALID_5M | 99/5 | 99/0 |
| PUMP-EUR | 1398650 | -1.96% | INVALID_5M | 98/4 | 99/0 |
| DOGE-EUR | 1339360 | -4.52% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1276522 | +3.69% | INVALID_5M | 99/6 | 99/0 |
| LSK-EUR | 1241803 | -11.83% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1121632 | -1.59% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 99/0 |
| ARB-EUR | 1068901 | +0.05% | INVALID_5M | 99/2 | 99/0 |
| STX-EUR | 893600 | -0.43% | INVALID_15M, INVALID_5M | 99/16 | 99/2 |
| FIL-EUR | 872412 | -6.56% | INVALID_15M, INVALID_5M | 84/28 | 99/4 |
| DOT-EUR | 838877 | -2.53% | INVALID_5M | 100/2 | 99/0 |
| APT-EUR | 796017 | -2.47% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| SHIB-EUR | 776319 | -2.01% | INVALID_5M | 99/2 | 99/0 |
| USELESS-EUR | 759705 | -3.27% | INVALID_5M | 99/2 | 99/0 |
| SKL-EUR | 739176 | +8.71% | INVALID_5M | 98/2 | 99/0 |
| BCH-EUR | 738032 | -1.93% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 89/12 | 100/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
