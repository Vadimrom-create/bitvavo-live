# Audit qualité des données Bitvavo

Scan : 2026-09-19T21:50:10.567117+00:00 (20260919T214834Z-28ee1e50)
Univers : 427 | strategy-grade : 31 | rejetés : 396
5m valides : 33 | 15m valides : 79 | deux intervalles valides : 31

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 394 |
| INVALID_15M | 348 |
| MISSING_LATEST_CLOSED_CANDLE | 237 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 394 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 348 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| USDC-EUR | 2694346 | -0.05% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 2361005 | -5.47% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1862435 | -5.97% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1701008 | -0.76% | INVALID_15M, INVALID_5M | 100/8 | 99/1 |
| STRK-EUR | 1506716 | -3.96% | INVALID_5M | 100/1 | 100/0 |
| WLD-EUR | 1494556 | -0.16% | INVALID_5M | 100/2 | 99/0 |
| CNPY-EUR | 1395148 | -18.87% | INVALID_5M | 100/1 | 99/0 |
| ARB-EUR | 1363980 | -7.83% | INVALID_5M | 100/1 | 99/0 |
| USELESS-EUR | 1260753 | -13.91% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1235402 | +0.59% | INVALID_5M | 100/8 | 99/0 |
| POL-EUR | 1087131 | -1.74% | INVALID_5M | 100/5 | 100/0 |
| SKY-EUR | 1071163 | -1.88% | INVALID_15M, INVALID_5M | 100/21 | 99/4 |
| BCH-EUR | 969700 | -2.66% | INVALID_15M, INVALID_5M | 100/15 | 99/2 |
| DOT-EUR | 922281 | -2.42% | INVALID_5M | 100/2 | 99/0 |
| AAVE-EUR | 877158 | +1.63% | INVALID_5M | 100/3 | 99/0 |
| HEI-EUR | 867605 | +13.16% | INVALID_5M | 100/4 | 99/0 |
| MORPHO-EUR | 857765 | +8.14% | INVALID_15M, INVALID_5M | 100/6 | 100/1 |
| FIL-EUR | 851315 | +11.03% | INVALID_5M | 100/3 | 100/0 |
| SAGA-EUR | 833078 | -0.91% | INVALID_5M | 100/12 | 100/0 |
| COTI-EUR | 817487 | -10.66% | INVALID_5M | 100/4 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
