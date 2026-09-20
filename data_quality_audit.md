# Audit qualité des données Bitvavo

Scan : 2026-09-20T06:56:03.922879+00:00 (20260920T065437Z-081e2d87)
Univers : 426 | strategy-grade : 31 | rejetés : 395
5m valides : 32 | 15m valides : 64 | deux intervalles valides : 31

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 394 |
| INVALID_15M | 362 |
| MISSING_LATEST_CLOSED_CANDLE | 292 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 394 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 362 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2745161 | -1.36% | INVALID_5M | 99/4 | 99/0 |
| HBAR-EUR | 2122171 | +2.38% | INVALID_5M | 100/1 | 99/0 |
| FET-EUR | 2018307 | -4.50% | INVALID_5M | 99/2 | 99/0 |
| CAP-EUR | 2008966 | -20.03% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1725709 | -3.03% | INVALID_5M | 99/4 | 99/0 |
| DOGE-EUR | 1680061 | -2.33% | INVALID_5M | 99/3 | 99/0 |
| CNPY-EUR | 1478729 | -31.47% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1314691 | -0.52% | INVALID_5M | 99/2 | 99/0 |
| VET-EUR | 1154953 | -3.62% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| EPIC-EUR | 1121482 | +8.30% | INVALID_15M, INVALID_5M | 99/2 | 99/3 |
| STRK-EUR | 1029605 | +9.85% | INVALID_5M | 99/3 | 99/0 |
| APT-EUR | 986282 | +1.02% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/18 | 99/2 |
| HEI-EUR | 921981 | +6.65% | INVALID_15M, INVALID_5M | 99/10 | 99/2 |
| FIL-EUR | 891370 | -1.33% | INVALID_15M, INVALID_5M | 100/17 | 99/3 |
| BCH-EUR | 840366 | -0.42% | INVALID_15M, INVALID_5M | 84/20 | 99/4 |
| CAKE-EUR | 766971 | +1.90% | INVALID_15M, INVALID_5M | 100/14 | 99/8 |
| SAGA-EUR | 742190 | +9.14% | INVALID_5M | 99/1 | 99/0 |
| COTI-EUR | 742023 | -7.06% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/10 | 99/5 |
| SHIB-EUR | 740093 | -0.21% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/11 | 99/2 |
| JUP-EUR | 738610 | +0.09% | INVALID_5M | 99/7 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
