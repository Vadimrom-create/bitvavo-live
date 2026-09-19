# Audit qualité des données Bitvavo

Scan : 2026-09-19T09:42:20.730842+00:00 (20260919T094050Z-d9b48c7b)
Univers : 427 | strategy-grade : 30 | rejetés : 397
5m valides : 34 | 15m valides : 75 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 393 |
| INVALID_15M | 352 |
| MISSING_LATEST_CLOSED_CANDLE | 276 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 393 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 352 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 4564114 | +2.60% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 2120577 | -3.32% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 1947628 | +4.60% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1774734 | +8.94% | INVALID_5M | 99/2 | 99/0 |
| F-EUR | 1596438 | +27.93% | INVALID_5M | 99/3 | 98/0 |
| POL-EUR | 1594702 | +4.09% | INVALID_5M | 100/5 | 99/0 |
| SKY-EUR | 1485010 | +15.34% | INVALID_5M | 99/4 | 99/0 |
| CNPY-EUR | 1431385 | +7.10% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 1218657 | -4.37% | INVALID_5M | 99/1 | 99/0 |
| AAVE-EUR | 1138933 | +6.98% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 1130071 | +2.60% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1090621 | +9.71% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |
| BCH-EUR | 1038753 | +0.35% | INVALID_5M | 100/8 | 99/0 |
| SAGA-EUR | 941292 | +24.03% | INVALID_5M | 99/3 | 99/0 |
| LPT-EUR | 895290 | +6.75% | INVALID_5M | 99/6 | 99/0 |
| COTI-EUR | 881652 | -6.90% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 99/1 |
| BNB-EUR | 863501 | +1.92% | INVALID_15M, INVALID_5M | 100/2 | 99/1 |
| MORPHO-EUR | 841391 | +19.13% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| S-EUR | 821739 | +7.05% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/11 | 100/0 |
| SUPER-EUR | 799296 | +9.97% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 90/10 | 99/4 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
