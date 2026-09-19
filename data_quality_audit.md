# Audit qualité des données Bitvavo

Scan : 2026-09-19T18:53:43.272509+00:00 (20260919T185209Z-53fd781c)
Univers : 427 | strategy-grade : 36 | rejetés : 391
5m valides : 37 | 15m valides : 100 | deux intervalles valides : 37

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 390 |
| INVALID_15M | 327 |
| MISSING_LATEST_CLOSED_CANDLE | 280 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 390 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 327 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| STRK-EUR | 2159120 | +4.90% | INVALID_5M | 99/4 | 99/0 |
| PUMP-EUR | 1917270 | -4.16% | INVALID_5M | 99/2 | 99/0 |
| CAP-EUR | 1879932 | -14.45% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1837994 | +6.11% | INVALID_5M | 99/2 | 99/0 |
| POL-EUR | 1503859 | +0.71% | INVALID_5M | 100/3 | 99/0 |
| LTC-EUR | 1461247 | +0.77% | INVALID_5M | 99/3 | 99/0 |
| OP-EUR | 1252842 | +6.82% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 99/0 |
| SKY-EUR | 1059820 | -0.66% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/16 | 99/2 |
| F-EUR | 992670 | -8.06% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/9 | 100/0 |
| BCH-EUR | 981872 | +0.60% | INVALID_5M | 99/6 | 99/0 |
| DOT-EUR | 977040 | -0.37% | INVALID_5M | 99/2 | 99/0 |
| SAGA-EUR | 930591 | +0.22% | INVALID_5M | 100/2 | 99/0 |
| AAVE-EUR | 907953 | +2.83% | INVALID_5M | 99/5 | 99/0 |
| COTI-EUR | 879610 | -4.57% | INVALID_5M | 99/5 | 99/0 |
| MORPHO-EUR | 824405 | +9.74% | INVALID_5M | 99/5 | 99/0 |
| KAS-EUR | 816420 | +8.16% | INVALID_5M | 100/1 | 99/0 |
| HEI-EUR | 808938 | +11.17% | INVALID_5M | 99/2 | 99/0 |
| JUP-EUR | 743031 | +5.51% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/7 | 99/0 |
| C-EUR | 706510 | +6.69% | INVALID_5M | 99/1 | 99/0 |
| RAY-EUR | 667299 | -0.81% | INVALID_5M | 100/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
