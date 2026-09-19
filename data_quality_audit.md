# Audit qualité des données Bitvavo

Scan : 2026-09-19T08:52:29.118671+00:00 (20260919T085057Z-bcab6a5e)
Univers : 427 | strategy-grade : 35 | rejetés : 392
5m valides : 36 | 15m valides : 72 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 355 |
| MISSING_LATEST_CLOSED_CANDLE | 279 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 355 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 4770368 | +4.80% | INVALID_5M | 99/2 | 99/0 |
| USELESS-EUR | 1948230 | +6.92% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1684143 | +6.31% | INVALID_5M | 99/2 | 99/0 |
| POL-EUR | 1591968 | +3.84% | INVALID_5M | 99/2 | 99/0 |
| F-EUR | 1585870 | +27.37% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 95/0 |
| CNPY-EUR | 1469591 | +6.86% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 100/0 |
| SKY-EUR | 1444281 | +15.48% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 99/0 |
| HBAR-EUR | 1218963 | +2.72% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 100/0 |
| AAVE-EUR | 1139003 | +6.87% | INVALID_5M | 99/2 | 99/0 |
| OP-EUR | 1104209 | +9.83% | INVALID_5M | 99/1 | 99/0 |
| RAY-EUR | 1100191 | +9.18% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 1043125 | -0.32% | INVALID_15M, INVALID_5M | 100/5 | 99/2 |
| SAGA-EUR | 921284 | +19.47% | INVALID_5M | 99/4 | 99/0 |
| LPT-EUR | 897791 | +6.55% | INVALID_5M | 99/7 | 99/0 |
| COTI-EUR | 882087 | -9.07% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| BNB-EUR | 854337 | +1.43% | INVALID_15M, INVALID_5M | 99/7 | 99/1 |
| S-EUR | 828415 | +8.20% | INVALID_5M | 100/7 | 99/0 |
| MORPHO-EUR | 820188 | +15.54% | INVALID_15M, INVALID_5M | 99/2 | 99/1 |
| C-EUR | 795034 | +13.63% | INVALID_5M | 100/2 | 99/0 |
| SUPER-EUR | 791613 | +11.80% | INVALID_15M, INVALID_5M | 95/5 | 99/6 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
