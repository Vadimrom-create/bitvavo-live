# Audit qualité des données Bitvavo

Scan : 2026-09-19T21:37:02.571126+00:00 (20260919T213529Z-1d1f259c)
Univers : 427 | strategy-grade : 30 | rejetés : 397
5m valides : 31 | 15m valides : 80 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 396 |
| INVALID_15M | 347 |
| MISSING_LATEST_CLOSED_CANDLE | 254 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 396 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 347 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| USDC-EUR | 2716488 | -0.05% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 2385733 | -6.36% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1842506 | -5.80% | INVALID_5M | 99/4 | 99/0 |
| APT-EUR | 1725291 | -2.34% | INVALID_15M, INVALID_5M | 99/10 | 99/1 |
| STRK-EUR | 1528516 | -3.41% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1466167 | -0.77% | INVALID_5M | 99/2 | 99/0 |
| ARB-EUR | 1376282 | -10.07% | INVALID_5M | 99/1 | 99/0 |
| CNPY-EUR | 1337963 | -16.12% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 1274616 | -13.97% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1242970 | -0.19% | INVALID_5M | 99/10 | 99/0 |
| POL-EUR | 1113159 | -3.47% | INVALID_5M | 100/4 | 99/0 |
| SKY-EUR | 1064297 | -1.68% | INVALID_15M, INVALID_5M | 100/25 | 99/4 |
| BCH-EUR | 982930 | -2.60% | INVALID_15M, INVALID_5M | 100/14 | 99/2 |
| DOT-EUR | 926755 | -3.51% | INVALID_5M | 99/2 | 99/0 |
| AAVE-EUR | 880223 | +0.58% | INVALID_5M | 99/4 | 99/0 |
| HEI-EUR | 864410 | +13.71% | INVALID_5M | 99/4 | 99/0 |
| MORPHO-EUR | 857675 | +8.22% | INVALID_15M, INVALID_5M | 100/5 | 99/1 |
| FIL-EUR | 838308 | +11.55% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 100/0 |
| SAGA-EUR | 835475 | -0.94% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/11 | 100/0 |
| COTI-EUR | 825511 | -9.52% | INVALID_5M | 100/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
