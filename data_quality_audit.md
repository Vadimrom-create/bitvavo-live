# Audit qualité des données Bitvavo

Scan : 2026-09-19T17:46:44.814496+00:00 (20260919T174510Z-15b4a45f)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 35 | 15m valides : 94 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 333 |
| MISSING_LATEST_CLOSED_CANDLE | 259 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 333 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| STRK-EUR | 2146105 | +17.38% | INVALID_5M | 100/2 | 100/0 |
| PUMP-EUR | 1958108 | -3.03% | INVALID_5M | 99/1 | 100/0 |
| APT-EUR | 1861139 | +4.86% | INVALID_5M | 100/2 | 100/0 |
| CAP-EUR | 1853877 | -16.01% | INVALID_15M | 99/0 | 100/1 |
| POL-EUR | 1525800 | +3.15% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1500930 | +1.58% | INVALID_5M | 99/1 | 100/0 |
| WLD-EUR | 1371071 | +3.08% | INVALID_5M | 99/1 | 100/0 |
| HBAR-EUR | 1357486 | +3.77% | INVALID_5M | 99/1 | 100/0 |
| OP-EUR | 1226747 | +7.04% | INVALID_5M | 99/4 | 100/0 |
| VET-EUR | 1145593 | +10.53% | INVALID_5M | 99/1 | 99/0 |
| F-EUR | 1087371 | -13.35% | INVALID_5M | 100/5 | 100/0 |
| SKY-EUR | 1063079 | -0.43% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/6 | 100/1 |
| SAGA-EUR | 1017622 | +1.40% | INVALID_5M | 99/2 | 99/0 |
| DOT-EUR | 969486 | -0.95% | INVALID_5M | 100/2 | 100/0 |
| BCH-EUR | 937338 | +1.87% | INVALID_5M | 99/5 | 100/0 |
| AAVE-EUR | 908453 | +3.02% | INVALID_5M | 99/5 | 100/0 |
| COTI-EUR | 889381 | -4.41% | INVALID_5M | 100/3 | 100/0 |
| MORPHO-EUR | 812833 | +7.78% | INVALID_5M | 99/3 | 99/0 |
| HEI-EUR | 785820 | +12.25% | INVALID_5M | 99/2 | 100/0 |
| JUP-EUR | 731925 | +4.15% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/7 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
