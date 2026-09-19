# Audit qualité des données Bitvavo

Scan : 2026-09-19T10:57:49.476246+00:00 (20260919T105622Z-dc869691)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 35 | 15m valides : 83 | deux intervalles valides : 34

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 344 |
| MISSING_LATEST_CLOSED_CANDLE | 294 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 344 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| PUMP-EUR | 2503694 | -3.42% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 2269632 | -2.49% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2100740 | +30.33% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1648680 | +2.83% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| F-EUR | 1607501 | +27.43% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 99/0 |
| POL-EUR | 1585296 | +4.47% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 99/0 |
| SKY-EUR | 1488049 | +9.97% | INVALID_5M | 99/5 | 99/0 |
| DOT-EUR | 1155343 | -1.96% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 1151971 | +3.04% | INVALID_5M | 99/2 | 99/0 |
| AAVE-EUR | 1148202 | +6.19% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1110306 | +12.83% | INVALID_5M | 99/4 | 99/0 |
| BCH-EUR | 1077761 | +0.18% | INVALID_5M | 99/11 | 99/0 |
| SAGA-EUR | 945122 | +34.74% | INVALID_5M | 100/1 | 99/0 |
| LPT-EUR | 866797 | +6.41% | INVALID_5M | 99/6 | 99/0 |
| MORPHO-EUR | 848862 | +17.31% | INVALID_5M | 100/1 | 99/0 |
| COTI-EUR | 846793 | -2.68% | INVALID_5M | 99/4 | 99/0 |
| S-EUR | 811944 | +7.25% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/20 | 99/2 |
| C-EUR | 806518 | +14.42% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 99/0 |
| BNB-EUR | 802803 | +1.53% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| SUPER-EUR | 801698 | +8.82% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 84/15 | 100/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
