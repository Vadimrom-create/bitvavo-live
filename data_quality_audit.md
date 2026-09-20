# Audit qualité des données Bitvavo

Scan : 2026-09-20T11:07:57.206254+00:00 (20260920T110624Z-00bf2dff)
Univers : 426 | strategy-grade : 29 | rejetés : 397
5m valides : 30 | 15m valides : 74 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 396 |
| INVALID_15M | 352 |
| MISSING_LATEST_CLOSED_CANDLE | 287 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 396 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 352 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 6959137 | -1.32% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2659601 | +4.27% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 100/0 |
| XLM-EUR | 2522125 | -2.52% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 2081045 | -23.17% | INVALID_5M | 100/4 | 99/0 |
| UNI-EUR | 1578642 | -2.75% | INVALID_5M | 99/2 | 99/0 |
| DOGE-EUR | 1510805 | -3.82% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1435645 | -1.61% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1427574 | -2.86% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1288080 | -0.48% | INVALID_5M | 99/1 | 99/0 |
| LSK-EUR | 1253212 | -16.37% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1150898 | +0.83% | INVALID_15M, INVALID_5M | 100/1 | 99/3 |
| ARB-EUR | 1125290 | +0.05% | INVALID_5M | 99/2 | 99/0 |
| STRK-EUR | 1074608 | +2.13% | INVALID_5M | 99/1 | 99/0 |
| EPIC-EUR | 1012696 | +5.70% | INVALID_5M | 99/2 | 99/0 |
| STX-EUR | 1012355 | +5.77% | INVALID_5M | 99/2 | 99/0 |
| FIL-EUR | 851373 | -3.31% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 93/12 | 100/3 |
| APT-EUR | 848784 | -2.74% | INVALID_5M | 99/8 | 99/0 |
| USELESS-EUR | 833785 | -2.90% | INVALID_5M | 99/4 | 99/0 |
| DOT-EUR | 806187 | -2.88% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 750590 | -2.07% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 80/16 | 100/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
