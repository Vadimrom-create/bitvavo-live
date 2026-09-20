# Audit qualité des données Bitvavo

Scan : 2026-09-20T02:40:38.120588+00:00 (20260920T023907Z-94a3cc5e)
Univers : 427 | strategy-grade : 25 | rejetés : 402
5m valides : 28 | 15m valides : 57 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 399 |
| INVALID_15M | 370 |
| MISSING_LATEST_CLOSED_CANDLE | 270 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 399 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 370 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| NEAR-EUR | 6004003 | -8.17% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2698337 | -1.40% | INVALID_5M | 99/3 | 99/0 |
| SYN-EUR | 2316361 | +12.77% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 2019345 | -3.06% | INVALID_5M | 99/6 | 99/0 |
| CAP-EUR | 2002132 | -15.11% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 100/0 |
| HBAR-EUR | 1854498 | +1.64% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1843778 | -4.97% | INVALID_5M | 100/5 | 99/0 |
| DOGE-EUR | 1577811 | -2.14% | INVALID_5M | 100/4 | 99/0 |
| CNPY-EUR | 1441743 | -22.44% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1413402 | -1.58% | INVALID_5M | 100/9 | 99/0 |
| VET-EUR | 1303260 | +8.47% | INVALID_5M | 99/3 | 99/0 |
| APT-EUR | 1259871 | -3.54% | INVALID_15M, INVALID_5M | 100/11 | 99/2 |
| EPIC-EUR | 1210016 | +12.41% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/13 | 99/2 |
| STRK-EUR | 1206461 | +5.01% | INVALID_5M | 99/1 | 99/0 |
| ARB-EUR | 1097868 | -4.41% | INVALID_5M | 99/3 | 99/0 |
| USELESS-EUR | 1077763 | -15.48% | INVALID_5M | 99/3 | 99/0 |
| OP-EUR | 980059 | -0.85% | INVALID_15M, INVALID_5M | 99/25 | 99/4 |
| FIL-EUR | 911027 | +0.23% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/15 | 100/1 |
| HEI-EUR | 892985 | +14.58% | INVALID_15M, INVALID_5M | 100/19 | 99/2 |
| STX-EUR | 886131 | +14.21% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
