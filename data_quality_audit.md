# Audit qualité des données Bitvavo

Scan : 2026-09-20T04:38:52.483242+00:00 (20260920T043721Z-be7af3d2)
Univers : 427 | strategy-grade : 29 | rejetés : 398
5m valides : 32 | 15m valides : 58 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 395 |
| INVALID_15M | 369 |
| MISSING_LATEST_CLOSED_CANDLE | 323 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 395 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 369 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ONDO-EUR | 6116486 | -0.08% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2813477 | -1.61% | INVALID_5M | 99/2 | 99/0 |
| SYN-EUR | 2311691 | +11.45% | INVALID_5M | 99/2 | 99/0 |
| ZAMA-EUR | 2286138 | +35.78% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 2059227 | +1.49% | INVALID_5M | 99/6 | 99/0 |
| CAP-EUR | 1998196 | -16.57% | INVALID_5M | 99/14 | 99/0 |
| DOGE-EUR | 1646389 | -2.11% | INVALID_5M | 99/3 | 99/0 |
| LSK-EUR | 1528522 | -8.75% | INVALID_5M | 100/1 | 99/0 |
| CNPY-EUR | 1474754 | -29.25% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1414142 | -1.83% | INVALID_5M | 99/6 | 99/0 |
| VET-EUR | 1251629 | +2.79% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1215810 | -5.34% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/15 | 99/1 |
| EPIC-EUR | 1209582 | +16.38% | INVALID_15M, INVALID_5M | 99/5 | 99/3 |
| STRK-EUR | 1089262 | +9.15% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 1050907 | -12.14% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 944106 | +14.32% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |
| FIL-EUR | 910496 | -1.93% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/18 | 100/1 |
| HEI-EUR | 899711 | +17.23% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/17 | 99/2 |
| BCH-EUR | 871154 | +0.28% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 91/17 | 100/4 |
| COTI-EUR | 796346 | -8.03% | INVALID_15M, INVALID_5M | 99/24 | 99/5 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
