# Audit qualité des données Bitvavo

Scan : 2026-09-20T02:04:32.007660+00:00 (20260920T020302Z-03f77b72)
Univers : 427 | strategy-grade : 22 | rejetés : 405
5m valides : 23 | 15m valides : 61 | deux intervalles valides : 23

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 404 |
| INVALID_15M | 366 |
| MISSING_LATEST_CLOSED_CANDLE | 310 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 404 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 366 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 9126180 | -1.63% | INVALID_5M | 99/2 | 99/0 |
| NEAR-EUR | 6150280 | -6.59% | INVALID_5M | 98/1 | 99/0 |
| XLM-EUR | 2688269 | +0.63% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 98/1 | 99/0 |
| SYN-EUR | 2318001 | +8.10% | INVALID_5M | 98/1 | 99/0 |
| UNI-EUR | 2043201 | -3.23% | INVALID_5M | 99/6 | 100/0 |
| CAP-EUR | 2001998 | -15.91% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1818422 | -2.21% | INVALID_5M | 99/3 | 99/0 |
| HBAR-EUR | 1784807 | +3.05% | INVALID_5M | 99/3 | 100/0 |
| DOGE-EUR | 1587349 | -0.94% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1437393 | -22.84% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1412444 | -1.55% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/7 | 100/0 |
| WLD-EUR | 1390858 | +1.31% | INVALID_5M | 98/1 | 99/0 |
| APT-EUR | 1341175 | -4.54% | INVALID_15M, INVALID_5M | 100/8 | 100/2 |
| VET-EUR | 1299178 | +10.53% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |
| EPIC-EUR | 1211502 | +10.69% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 98/9 | 100/2 |
| STRK-EUR | 1205243 | +6.29% | INVALID_5M | 98/2 | 99/0 |
| ARB-EUR | 1088833 | -3.41% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| USELESS-EUR | 1077489 | -12.90% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 100/0 |
| OP-EUR | 1040055 | +2.67% | INVALID_15M, INVALID_5M | 99/25 | 99/4 |
| FIL-EUR | 910627 | +0.75% | INVALID_15M, INVALID_5M | 99/14 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
