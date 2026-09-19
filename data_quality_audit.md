# Audit qualité des données Bitvavo

Scan : 2026-09-19T09:55:08.016257+00:00 (20260919T095339Z-f1a5f35d)
Univers : 427 | strategy-grade : 31 | rejetés : 396
5m valides : 35 | 15m valides : 76 | deux intervalles valides : 31

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 351 |
| MISSING_LATEST_CLOSED_CANDLE | 247 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 351 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| PUMP-EUR | 2120709 | -2.70% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 1945292 | +5.62% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1767859 | +8.65% | INVALID_5M | 100/2 | 99/0 |
| F-EUR | 1601583 | +31.02% | INVALID_5M | 100/3 | 99/0 |
| POL-EUR | 1594484 | +4.50% | INVALID_5M | 100/4 | 99/0 |
| SKY-EUR | 1462416 | +11.57% | INVALID_5M | 99/5 | 99/0 |
| CNPY-EUR | 1428743 | +7.75% | INVALID_5M | 100/1 | 99/0 |
| DOT-EUR | 1219703 | -3.78% | INVALID_5M | 99/1 | 99/0 |
| AAVE-EUR | 1131446 | +7.60% | INVALID_5M | 100/1 | 99/0 |
| HBAR-EUR | 1130393 | +2.70% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1084123 | +10.31% | INVALID_5M | 100/2 | 99/0 |
| BCH-EUR | 1042418 | +0.40% | INVALID_5M | 100/8 | 99/0 |
| SAGA-EUR | 940640 | +28.21% | INVALID_5M | 99/1 | 99/0 |
| LPT-EUR | 896275 | +7.00% | INVALID_5M | 100/3 | 99/0 |
| COTI-EUR | 880728 | -7.71% | INVALID_15M, INVALID_5M | 100/5 | 100/1 |
| BNB-EUR | 862319 | +2.03% | INVALID_15M, INVALID_5M | 100/1 | 99/1 |
| MORPHO-EUR | 848447 | +19.07% | INVALID_5M | 99/1 | 99/0 |
| S-EUR | 821488 | +7.34% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/11 | 100/0 |
| SUPER-EUR | 802168 | +9.81% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 88/10 | 100/5 |
| C-EUR | 800128 | +13.10% | INVALID_5M | 100/5 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
