# Audit qualité des données Bitvavo

Scan : 2026-09-19T23:02:22.874844+00:00 (20260919T230021Z-d0666203)
Univers : 427 | strategy-grade : 30 | rejetés : 397
5m valides : 31 | 15m valides : 75 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 396 |
| INVALID_15M | 352 |
| MISSING_LATEST_CLOSED_CANDLE | 276 |

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
| USDC-EUR | 2652829 | -0.05% | INVALID_5M | 99/4 | 100/0 |
| CAP-EUR | 2029917 | -16.18% | INVALID_5M | 99/3 | 100/0 |
| PUMP-EUR | 1824772 | -1.82% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| DOGE-EUR | 1594414 | -0.49% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1590026 | +1.84% | INVALID_15M, INVALID_5M | 100/1 | 100/1 |
| LTC-EUR | 1528572 | -0.13% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 1409765 | +1.61% | INVALID_5M | 99/3 | 100/0 |
| EPIC-EUR | 1239428 | +11.44% | INVALID_5M | 99/1 | 100/0 |
| ARB-EUR | 1234688 | -6.26% | INVALID_5M | 100/1 | 100/0 |
| OP-EUR | 1232216 | +2.60% | INVALID_5M | 100/8 | 100/0 |
| SKY-EUR | 1029344 | -1.04% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/8 | 100/4 |
| POL-EUR | 1008359 | -1.45% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 99/0 |
| FIL-EUR | 904156 | +3.73% | INVALID_5M | 99/4 | 100/0 |
| DOT-EUR | 887914 | -1.12% | INVALID_5M | 99/2 | 99/0 |
| AAVE-EUR | 875208 | +1.97% | INVALID_5M | 100/3 | 100/0 |
| HEI-EUR | 870890 | +12.48% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/11 | 100/1 |
| STX-EUR | 833368 | +8.49% | INVALID_5M | 99/1 | 100/0 |
| MORPHO-EUR | 823353 | +4.68% | INVALID_15M, INVALID_5M | 100/2 | 100/1 |
| SAGA-EUR | 811884 | +1.03% | INVALID_15M, INVALID_5M | 100/15 | 100/1 |
| COTI-EUR | 790135 | -10.94% | INVALID_5M | 99/11 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
