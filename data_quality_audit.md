# Audit qualité des données Bitvavo

Scan : 2026-09-19T19:09:15.217189+00:00 (20260919T190740Z-2292a44f)
Univers : 427 | strategy-grade : 34 | rejetés : 393
5m valides : 36 | 15m valides : 101 | deux intervalles valides : 36

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 326 |
| MISSING_LATEST_CLOSED_CANDLE | 287 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 326 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| STRK-EUR | 2027272 | -1.74% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 1932483 | -4.94% | INVALID_5M | 99/2 | 99/0 |
| CAP-EUR | 1900984 | -12.93% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1833572 | +5.37% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| ARB-EUR | 1714809 | -6.00% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| LTC-EUR | 1516901 | +1.10% | INVALID_5M | 99/3 | 99/0 |
| POL-EUR | 1475344 | +0.20% | INVALID_5M | 99/4 | 99/0 |
| OP-EUR | 1235500 | +5.79% | INVALID_5M | 99/6 | 99/0 |
| SKY-EUR | 1052997 | -1.48% | INVALID_15M, INVALID_5M | 100/16 | 99/3 |
| BCH-EUR | 983179 | +0.42% | INVALID_5M | 99/6 | 99/0 |
| DOT-EUR | 963736 | -0.13% | INVALID_5M | 99/3 | 99/0 |
| F-EUR | 936209 | -6.73% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/12 | 99/0 |
| SAGA-EUR | 904904 | +2.83% | INVALID_5M | 99/3 | 99/0 |
| AAVE-EUR | 904667 | +2.99% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 99/0 |
| COTI-EUR | 884939 | -5.15% | INVALID_5M | 99/5 | 99/0 |
| MORPHO-EUR | 837026 | +9.41% | INVALID_5M | 99/5 | 99/0 |
| HEI-EUR | 828865 | +12.70% | INVALID_5M | 99/1 | 99/0 |
| KAS-EUR | 806582 | +7.37% | INVALID_5M | 99/2 | 99/0 |
| JUP-EUR | 744398 | +4.64% | INVALID_5M | 99/8 | 99/0 |
| C-EUR | 714100 | +10.43% | INVALID_5M | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
