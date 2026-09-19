# Audit qualité des données Bitvavo

Scan : 2026-09-19T10:44:55.950952+00:00 (20260919T104330Z-d910f2be)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 34 | 15m valides : 82 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 393 |
| INVALID_15M | 345 |
| MISSING_LATEST_CLOSED_CANDLE | 274 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 393 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 345 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| PUMP-EUR | 2503214 | -3.35% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 2288162 | -3.24% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2096068 | +31.05% | INVALID_5M | 99/2 | 99/0 |
| F-EUR | 1606137 | +28.38% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 99/0 |
| POL-EUR | 1582887 | +3.91% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 99/0 |
| SKY-EUR | 1517167 | +12.50% | INVALID_5M | 100/4 | 99/0 |
| CNPY-EUR | 1479247 | +0.24% | INVALID_5M | 98/1 | 99/0 |
| DOT-EUR | 1174509 | -2.05% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 1147191 | +3.20% | INVALID_5M | 99/2 | 99/0 |
| AAVE-EUR | 1137605 | +6.58% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1107395 | +12.92% | INVALID_5M | 98/4 | 99/0 |
| BCH-EUR | 1078169 | +0.51% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/9 | 99/0 |
| SAGA-EUR | 949722 | +31.76% | INVALID_5M | 99/1 | 99/0 |
| LPT-EUR | 887229 | +6.15% | INVALID_5M | 100/5 | 99/0 |
| COTI-EUR | 870453 | -4.90% | INVALID_5M | 98/5 | 99/0 |
| MORPHO-EUR | 853129 | +16.69% | INVALID_5M | 99/2 | 99/0 |
| S-EUR | 812153 | +6.32% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/19 | 100/2 |
| BNB-EUR | 807137 | +1.74% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| C-EUR | 806651 | +14.14% | INVALID_5M | 99/3 | 99/0 |
| SUPER-EUR | 802864 | +8.06% | INVALID_15M, INVALID_5M | 84/15 | 99/4 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
