# Audit qualité des données Bitvavo

Scan : 2026-09-19T19:23:43.787458+00:00 (20260919T192213Z-26e4aa78)
Univers : 427 | strategy-grade : 35 | rejetés : 392
5m valides : 35 | 15m valides : 98 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 329 |
| MISSING_LATEST_CLOSED_CANDLE | 292 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 329 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| STRK-EUR | 2007445 | -2.16% | INVALID_5M | 99/3 | 99/0 |
| CAP-EUR | 1960321 | -12.08% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1899530 | -6.19% | INVALID_5M | 100/2 | 99/0 |
| APT-EUR | 1818646 | +4.16% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| ARB-EUR | 1699573 | -6.65% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1519610 | +0.74% | INVALID_5M | 99/3 | 99/0 |
| POL-EUR | 1461163 | +0.33% | INVALID_5M | 100/3 | 99/0 |
| OP-EUR | 1230166 | +5.40% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 100/0 |
| SKY-EUR | 1055030 | -1.12% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/17 | 99/3 |
| BCH-EUR | 983617 | +0.50% | INVALID_5M | 99/4 | 99/0 |
| DOT-EUR | 964208 | -0.42% | INVALID_5M | 100/3 | 99/0 |
| AAVE-EUR | 908817 | +2.62% | INVALID_5M | 99/3 | 99/0 |
| F-EUR | 900396 | -6.79% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/12 | 100/1 |
| SAGA-EUR | 896024 | -0.33% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 99/0 |
| COTI-EUR | 877743 | -5.34% | INVALID_5M | 99/5 | 99/0 |
| MORPHO-EUR | 838201 | +8.06% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/5 | 100/0 |
| KAS-EUR | 808976 | +6.08% | INVALID_5M | 99/2 | 99/0 |
| JUP-EUR | 740692 | +4.29% | INVALID_5M | 100/4 | 99/0 |
| C-EUR | 723733 | +6.18% | INVALID_5M | 99/1 | 99/0 |
| RAY-EUR | 655115 | -3.60% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
