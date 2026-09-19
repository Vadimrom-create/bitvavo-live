# Audit qualité des données Bitvavo

Scan : 2026-09-19T23:32:40.002565+00:00 (20260919T233107Z-0d1e7169)
Univers : 427 | strategy-grade : 28 | rejetés : 399
5m valides : 29 | 15m valides : 75 | deux intervalles valides : 28

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 398 |
| INVALID_15M | 352 |
| MISSING_LATEST_CLOSED_CANDLE | 297 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 398 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 352 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2807017 | +1.74% | INVALID_5M | 99/1 | 100/0 |
| USDC-EUR | 2654943 | -0.01% | INVALID_5M | 99/3 | 99/0 |
| CAP-EUR | 2031134 | -15.93% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 99/0 |
| PUMP-EUR | 1812431 | -1.63% | INVALID_5M | 100/5 | 100/0 |
| APT-EUR | 1607127 | -0.79% | INVALID_15M, INVALID_5M | 99/2 | 99/1 |
| DOGE-EUR | 1595717 | -0.01% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1523520 | -0.00% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 100/0 |
| STRK-EUR | 1410360 | +0.69% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1405365 | -21.85% | INVALID_5M | 100/2 | 100/0 |
| OP-EUR | 1229861 | +1.06% | INVALID_5M | 100/10 | 100/0 |
| EPIC-EUR | 1229200 | +11.67% | INVALID_5M | 99/1 | 99/0 |
| ARB-EUR | 1169778 | -6.66% | INVALID_5M | 100/1 | 100/0 |
| SKY-EUR | 1039915 | -0.41% | INVALID_15M, INVALID_5M | 99/9 | 100/3 |
| POL-EUR | 986801 | -1.32% | INVALID_5M | 99/6 | 100/0 |
| FIL-EUR | 906542 | +3.28% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| DOT-EUR | 888888 | -1.01% | INVALID_5M | 99/3 | 99/0 |
| HEI-EUR | 875163 | +12.77% | INVALID_15M, INVALID_5M | 99/13 | 99/1 |
| AAVE-EUR | 871943 | +1.59% | INVALID_5M | 100/5 | 100/0 |
| STX-EUR | 844897 | +8.93% | INVALID_5M | 99/1 | 99/0 |
| SAGA-EUR | 809216 | +0.45% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/17 | 100/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
