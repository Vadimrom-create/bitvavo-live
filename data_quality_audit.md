# Audit qualité des données Bitvavo

Scan : 2026-09-20T07:14:33.280687+00:00 (20260920T071306Z-86835ee1)
Univers : 426 | strategy-grade : 29 | rejetés : 397
5m valides : 31 | 15m valides : 65 | deux intervalles valides : 29

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 395 |
| INVALID_15M | 361 |
| MISSING_LATEST_CLOSED_CANDLE | 298 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 395 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 361 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2692362 | -0.91% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 98/4 | 99/0 |
| HBAR-EUR | 2192094 | +4.07% | INVALID_5M | 98/1 | 99/0 |
| CAP-EUR | 2010323 | -17.73% | INVALID_5M | 99/1 | 99/0 |
| FET-EUR | 2003850 | -4.56% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1717749 | -2.67% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 99/0 |
| DOGE-EUR | 1676532 | -2.08% | INVALID_5M | 99/3 | 99/0 |
| CNPY-EUR | 1493128 | -30.14% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1319103 | -0.70% | INVALID_5M | 99/2 | 99/0 |
| VET-EUR | 1114970 | -0.60% | INVALID_5M | 98/2 | 99/0 |
| EPIC-EUR | 1089958 | +9.92% | INVALID_15M, INVALID_5M | 100/2 | 99/3 |
| STRK-EUR | 1041435 | +11.83% | INVALID_5M | 98/3 | 99/0 |
| APT-EUR | 962210 | +2.02% | INVALID_15M, INVALID_5M | 99/20 | 99/2 |
| HEI-EUR | 906555 | +4.17% | INVALID_15M, INVALID_5M | 99/7 | 99/2 |
| USELESS-EUR | 891787 | -9.68% | INVALID_5M | 99/1 | 99/0 |
| FIL-EUR | 888579 | -0.20% | INVALID_15M, INVALID_5M | 99/16 | 99/3 |
| BCH-EUR | 836467 | -0.28% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 84/20 | 99/4 |
| CAKE-EUR | 807096 | +0.61% | INVALID_15M, INVALID_5M | 99/15 | 99/7 |
| SAGA-EUR | 752475 | +9.03% | INVALID_5M | 99/1 | 99/0 |
| KAS-EUR | 751989 | +1.96% | INVALID_15M, INVALID_5M | 92/6 | 99/7 |
| JUP-EUR | 742605 | -0.58% | INVALID_5M | 99/6 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
