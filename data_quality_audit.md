# Audit qualité des données Bitvavo

Scan : 2026-09-19T23:59:24.256696+00:00 (20260919T235754Z-fca74293)
Univers : 427 | strategy-grade : 24 | rejetés : 403
5m valides : 26 | 15m valides : 72 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 401 |
| INVALID_15M | 355 |
| MISSING_LATEST_CLOSED_CANDLE | 313 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 401 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 355 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2785674 | +1.55% | INVALID_5M | 99/1 | 99/0 |
| USDC-EUR | 2677150 | +0.02% | INVALID_5M | 99/4 | 99/0 |
| CAP-EUR | 2043704 | -13.77% | INVALID_5M | 99/6 | 99/0 |
| PUMP-EUR | 1820933 | +0.90% | INVALID_5M | 99/5 | 99/0 |
| HBAR-EUR | 1649280 | +3.12% | MISSING_LATEST_CLOSED_CANDLE | 100/0 | 99/0 |
| DOGE-EUR | 1619729 | +0.26% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1564300 | -0.82% | INVALID_15M, INVALID_5M | 100/2 | 99/1 |
| LTC-EUR | 1516388 | +0.45% | INVALID_5M | 99/3 | 99/0 |
| WLD-EUR | 1462675 | +1.80% | INVALID_5M | 99/1 | 99/0 |
| CNPY-EUR | 1418077 | -25.49% | INVALID_5M | 99/2 | 99/0 |
| STRK-EUR | 1375114 | +0.37% | INVALID_5M | 99/2 | 99/0 |
| EPIC-EUR | 1224365 | +9.03% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1223234 | +0.30% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/11 | 100/0 |
| USELESS-EUR | 1144113 | -12.53% | INVALID_5M | 99/1 | 99/0 |
| ARB-EUR | 1134624 | -7.00% | INVALID_5M | 99/2 | 99/0 |
| SKY-EUR | 1034754 | -0.41% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 96/7 | 100/3 |
| POL-EUR | 983907 | -2.41% | INVALID_5M | 99/6 | 99/0 |
| FIL-EUR | 905722 | +1.84% | INVALID_5M | 99/7 | 99/0 |
| HEI-EUR | 882761 | +11.57% | INVALID_15M, INVALID_5M | 99/15 | 99/1 |
| DOT-EUR | 882652 | -0.94% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
