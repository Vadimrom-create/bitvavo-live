# Audit qualité des données Bitvavo

Scan : 2026-09-19T22:03:19.313044+00:00 (20260919T220145Z-2ac03b9a)
Univers : 427 | strategy-grade : 31 | rejetés : 396
5m valides : 34 | 15m valides : 78 | deux intervalles valides : 32

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 393 |
| INVALID_15M | 349 |
| MISSING_LATEST_CLOSED_CANDLE | 281 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 393 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 349 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| USDC-EUR | 2691951 | -0.03% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 2355592 | -5.71% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1865684 | -5.19% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1702099 | -1.50% | INVALID_15M, INVALID_5M | 99/7 | 99/1 |
| STRK-EUR | 1469625 | -0.52% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 100/0 |
| WLD-EUR | 1439695 | +0.21% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1400351 | -21.81% | INVALID_5M | 99/1 | 99/0 |
| ARB-EUR | 1343553 | -8.28% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 1234249 | -13.16% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1217793 | +1.88% | INVALID_5M | 99/5 | 99/0 |
| POL-EUR | 1081213 | -1.99% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 99/0 |
| SKY-EUR | 1071411 | -1.35% | INVALID_15M, INVALID_5M | 100/22 | 100/4 |
| BCH-EUR | 970646 | -2.54% | INVALID_15M, INVALID_5M | 100/13 | 100/2 |
| DOT-EUR | 924625 | -2.72% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| AAVE-EUR | 880776 | +1.27% | INVALID_5M | 99/4 | 99/0 |
| HEI-EUR | 869053 | +13.10% | INVALID_5M | 99/4 | 100/0 |
| MORPHO-EUR | 858639 | +7.19% | INVALID_15M, INVALID_5M | 99/3 | 99/1 |
| FIL-EUR | 849344 | +8.17% | INVALID_5M | 99/5 | 99/0 |
| SAGA-EUR | 830267 | -0.10% | INVALID_5M | 99/12 | 99/0 |
| STX-EUR | 825198 | +6.57% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
