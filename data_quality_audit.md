# Audit qualité des données Bitvavo

Scan : 2026-09-20T03:48:01.879399+00:00 (20260920T034630Z-288ead91)
Univers : 427 | strategy-grade : 27 | rejetés : 400
5m valides : 30 | 15m valides : 57 | deux intervalles valides : 28

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 397 |
| INVALID_15M | 370 |
| MISSING_LATEST_CLOSED_CANDLE | 256 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 397 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 370 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| NEAR-EUR | 5957771 | -7.61% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2818970 | -2.35% | INVALID_5M | 99/2 | 99/0 |
| SYN-EUR | 2311191 | +10.74% | INVALID_5M | 99/1 | 99/0 |
| ZAMA-EUR | 2261583 | +33.81% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 2065990 | +0.73% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 100/0 |
| PUMP-EUR | 2012526 | -7.71% | INVALID_5M | 99/2 | 100/0 |
| CAP-EUR | 2004232 | -15.96% | INVALID_5M | 100/10 | 100/0 |
| UNI-EUR | 1988831 | -4.03% | INVALID_5M | 100/1 | 100/0 |
| DOGE-EUR | 1651905 | -2.91% | INVALID_5M | 100/2 | 100/0 |
| LTC-EUR | 1428728 | -2.66% | INVALID_5M | 100/9 | 100/0 |
| VET-EUR | 1347576 | +6.57% | INVALID_5M | 99/3 | 100/0 |
| APT-EUR | 1253283 | -6.52% | INVALID_15M, INVALID_5M | 99/9 | 100/1 |
| EPIC-EUR | 1210210 | +13.45% | INVALID_15M, INVALID_5M | 99/14 | 100/3 |
| STRK-EUR | 1190558 | +0.10% | INVALID_5M | 99/2 | 99/0 |
| ARB-EUR | 1144436 | +1.30% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 1076287 | -17.38% | INVALID_5M | 100/1 | 100/0 |
| STX-EUR | 931986 | +12.52% | INVALID_5M | 99/1 | 99/0 |
| FIL-EUR | 919095 | -2.37% | INVALID_15M, INVALID_5M | 99/19 | 100/1 |
| OP-EUR | 899243 | -2.47% | INVALID_15M, INVALID_5M | 99/5 | 100/4 |
| HEI-EUR | 893745 | +13.31% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/14 | 100/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
