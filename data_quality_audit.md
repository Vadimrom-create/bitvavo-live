# Audit qualité des données Bitvavo

Scan : 2026-09-20T09:22:21.350895+00:00 (20260920T092054Z-e16b6778)
Univers : 426 | strategy-grade : 33 | rejetés : 393
5m valides : 37 | 15m valides : 68 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 389 |
| INVALID_15M | 358 |
| MISSING_LATEST_CLOSED_CANDLE | 308 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 389 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 358 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ZAMA-EUR | 2249480 | +9.53% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 2036440 | -25.55% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 1652709 | -3.43% | INVALID_5M | 99/6 | 99/0 |
| DOGE-EUR | 1583138 | -2.79% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1425063 | +0.89% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1307911 | -0.35% | INVALID_5M | 100/1 | 99/0 |
| CAKE-EUR | 1113799 | +1.62% | INVALID_15M, INVALID_5M | 89/4 | 99/4 |
| EPIC-EUR | 1073416 | +14.39% | INVALID_5M | 99/4 | 99/0 |
| STX-EUR | 1008941 | +10.93% | INVALID_5M | 99/5 | 99/0 |
| APT-EUR | 872243 | +1.43% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 100/1 |
| USELESS-EUR | 858697 | -4.23% | INVALID_5M | 99/4 | 99/0 |
| FIL-EUR | 853315 | -2.27% | INVALID_15M, INVALID_5M | 100/5 | 99/2 |
| KAS-EUR | 812360 | +5.22% | INVALID_15M | 96/0 | 99/1 |
| SAGA-EUR | 809545 | +5.12% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 805878 | -1.73% | INVALID_5M | 100/1 | 99/0 |
| BCH-EUR | 799426 | -1.25% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 89/7 | 99/1 |
| JUP-EUR | 717859 | -2.45% | INVALID_15M, INVALID_5M | 100/6 | 99/1 |
| SKL-EUR | 701442 | +14.67% | INVALID_5M | 99/1 | 95/0 |
| COTI-EUR | 601595 | -8.83% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 90/17 | 99/1 |
| DRIFT-EUR | 600681 | -7.17% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
