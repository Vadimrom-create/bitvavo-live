# Audit qualité des données Bitvavo

Scan : 2026-09-19T23:46:30.967989+00:00 (20260919T234501Z-0809c56a)
Univers : 427 | strategy-grade : 26 | rejetés : 401
5m valides : 28 | 15m valides : 72 | deux intervalles valides : 27

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 399 |
| INVALID_15M | 355 |
| MISSING_LATEST_CLOSED_CANDLE | 294 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 399 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 355 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2813682 | +1.78% | INVALID_5M | 99/1 | 100/0 |
| USDC-EUR | 2656509 | -0.01% | INVALID_5M | 99/4 | 100/0 |
| CAP-EUR | 2033654 | -14.56% | INVALID_5M | 99/6 | 100/0 |
| PUMP-EUR | 1798982 | -1.33% | INVALID_5M | 99/5 | 100/0 |
| APT-EUR | 1605756 | -0.84% | INVALID_15M, INVALID_5M | 100/2 | 100/1 |
| DOGE-EUR | 1584039 | +0.26% | INVALID_5M | 100/2 | 100/0 |
| LTC-EUR | 1530660 | +0.38% | INVALID_5M | 99/3 | 99/0 |
| CNPY-EUR | 1411606 | -24.70% | INVALID_5M | 99/2 | 100/0 |
| STRK-EUR | 1385238 | +1.09% | INVALID_5M | 100/2 | 100/0 |
| OP-EUR | 1230568 | +0.29% | INVALID_5M | 100/11 | 100/0 |
| EPIC-EUR | 1224698 | +9.96% | INVALID_5M | 100/1 | 100/0 |
| USELESS-EUR | 1159347 | -12.29% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 100/0 |
| ARB-EUR | 1152569 | -8.80% | INVALID_5M | 99/2 | 100/0 |
| SKY-EUR | 1035788 | +0.20% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 97/7 | 100/3 |
| POL-EUR | 981618 | -1.84% | INVALID_5M | 100/6 | 100/0 |
| FIL-EUR | 906108 | +3.36% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/5 | 100/0 |
| DOT-EUR | 888394 | -1.30% | INVALID_5M | 99/4 | 100/0 |
| HEI-EUR | 874664 | +11.06% | INVALID_15M, INVALID_5M | 100/14 | 100/1 |
| AAVE-EUR | 871916 | +1.50% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/5 | 100/0 |
| STX-EUR | 848289 | +9.35% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
