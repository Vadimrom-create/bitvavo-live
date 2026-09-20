# Audit qualité des données Bitvavo

Scan : 2026-09-20T02:54:49.896413+00:00 (20260920T025320Z-77447537)
Univers : 427 | strategy-grade : 25 | rejetés : 402
5m valides : 28 | 15m valides : 56 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 399 |
| INVALID_15M | 371 |
| MISSING_LATEST_CLOSED_CANDLE | 234 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 399 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 371 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| NEAR-EUR | 5880174 | -9.29% | INVALID_5M | 98/1 | 99/0 |
| XLM-EUR | 2701388 | -1.76% | INVALID_5M | 98/3 | 99/0 |
| SYN-EUR | 2326810 | +9.80% | INVALID_5M | 98/1 | 99/0 |
| UNI-EUR | 2028063 | -3.26% | INVALID_5M | 99/4 | 99/0 |
| CAP-EUR | 2002621 | -16.15% | INVALID_5M | 99/6 | 99/0 |
| HBAR-EUR | 1964968 | +0.84% | INVALID_5M | 98/1 | 99/0 |
| PUMP-EUR | 1948102 | -6.85% | INVALID_5M | 99/5 | 99/0 |
| DOGE-EUR | 1600116 | -2.80% | INVALID_5M | 99/4 | 99/0 |
| CNPY-EUR | 1442736 | -23.51% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1441021 | -2.13% | INVALID_5M | 99/10 | 99/0 |
| VET-EUR | 1325291 | +6.96% | INVALID_5M | 98/3 | 99/0 |
| APT-EUR | 1269905 | -7.04% | INVALID_15M, INVALID_5M | 98/11 | 99/2 |
| EPIC-EUR | 1208360 | +11.60% | INVALID_15M, INVALID_5M | 99/13 | 99/3 |
| STRK-EUR | 1205032 | +4.79% | INVALID_5M | 99/1 | 99/0 |
| ARB-EUR | 1128901 | -5.27% | INVALID_5M | 98/3 | 99/0 |
| USELESS-EUR | 1083621 | -16.76% | INVALID_5M | 98/3 | 99/0 |
| OP-EUR | 970927 | -2.48% | INVALID_15M, INVALID_5M | 99/22 | 99/4 |
| FIL-EUR | 912489 | -1.08% | INVALID_15M, INVALID_5M | 99/19 | 99/1 |
| STX-EUR | 903995 | +10.31% | INVALID_5M | 99/2 | 99/0 |
| HEI-EUR | 892680 | +11.40% | INVALID_15M, INVALID_5M | 100/16 | 99/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
