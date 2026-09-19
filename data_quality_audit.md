# Audit qualité des données Bitvavo

Scan : 2026-09-19T08:21:16.231287+00:00 (20260919T081943Z-9c8b3b27)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 42 | 15m valides : 68 | deux intervalles valides : 34

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 385 |
| INVALID_15M | 359 |
| MISSING_LATEST_CLOSED_CANDLE | 256 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 385 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 359 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 4919623 | +4.74% | INVALID_5M | 99/2 | 99/0 |
| USELESS-EUR | 1989402 | +6.38% | INVALID_5M | 100/2 | 99/0 |
| APT-EUR | 1652449 | +7.34% | INVALID_5M | 100/1 | 99/0 |
| POL-EUR | 1644424 | +3.45% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 100/0 |
| F-EUR | 1581541 | +29.78% | INVALID_5M | 99/2 | 93/0 |
| CNPY-EUR | 1534470 | +5.06% | INVALID_5M | 100/1 | 99/0 |
| SKY-EUR | 1423272 | +15.98% | INVALID_5M | 100/6 | 99/0 |
| HBAR-EUR | 1220336 | +3.13% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| AAVE-EUR | 1118994 | +6.58% | INVALID_5M | 99/2 | 99/0 |
| OP-EUR | 1107126 | +11.66% | INVALID_5M | 99/3 | 99/0 |
| RAY-EUR | 1081664 | +5.51% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 1040960 | -0.59% | INVALID_15M, INVALID_5M | 99/2 | 99/2 |
| SAGA-EUR | 913404 | +17.00% | INVALID_5M | 99/5 | 99/0 |
| COTI-EUR | 908542 | -7.53% | INVALID_15M, MISSING_LATEST_CLOSED_CANDLE | 99/0 | 100/2 |
| LPT-EUR | 903777 | +8.67% | INVALID_5M | 100/6 | 99/0 |
| BNB-EUR | 855149 | +1.22% | INVALID_15M, INVALID_5M | 99/7 | 99/1 |
| S-EUR | 835781 | +9.17% | INVALID_5M | 99/8 | 99/0 |
| MORPHO-EUR | 835230 | +14.05% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| XPL-EUR | 806742 | +1.67% | INVALID_15M, INVALID_5M | 99/16 | 99/2 |
| C-EUR | 794341 | +13.17% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
