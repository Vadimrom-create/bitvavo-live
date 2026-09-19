# Audit qualité des données Bitvavo

Scan : 2026-09-19T08:37:46.874630+00:00 (20260919T083616Z-348ca369)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 38 | 15m valides : 68 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 389 |
| INVALID_15M | 359 |
| MISSING_LATEST_CLOSED_CANDLE | 276 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 389 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 359 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 4939837 | +5.93% | INVALID_5M | 99/2 | 99/0 |
| USELESS-EUR | 1969207 | +7.49% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1674366 | +7.03% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |
| POL-EUR | 1647196 | +4.16% | INVALID_5M | 99/2 | 99/0 |
| F-EUR | 1584627 | +27.16% | INVALID_5M | 99/2 | 94/0 |
| CNPY-EUR | 1488929 | +3.08% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1432520 | +15.46% | INVALID_5M | 99/6 | 99/0 |
| HBAR-EUR | 1221975 | +2.98% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| AAVE-EUR | 1116684 | +7.57% | INVALID_5M | 99/2 | 99/0 |
| OP-EUR | 1107186 | +10.95% | INVALID_5M | 99/3 | 99/0 |
| RAY-EUR | 1095907 | +5.92% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 1048180 | -0.38% | INVALID_15M, INVALID_5M | 100/3 | 99/2 |
| SAGA-EUR | 915974 | +16.60% | INVALID_5M | 99/4 | 99/0 |
| LPT-EUR | 904734 | +7.26% | INVALID_5M | 99/7 | 99/0 |
| COTI-EUR | 888940 | -7.56% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| BNB-EUR | 853274 | +1.21% | INVALID_15M, INVALID_5M | 100/7 | 99/1 |
| S-EUR | 828861 | +8.98% | INVALID_5M | 99/8 | 99/0 |
| MORPHO-EUR | 815446 | +14.71% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 100/1 |
| XPL-EUR | 805366 | +1.73% | INVALID_15M, INVALID_5M | 100/10 | 99/2 |
| C-EUR | 794604 | +13.67% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
