# Audit qualité des données Bitvavo

Scan : 2026-09-19T05:14:28.922556+00:00 (20260919T051257Z-38a6319c)
Univers : 427 | strategy-grade : 24 | rejetés : 403
5m valides : 26 | 15m valides : 57 | deux intervalles valides : 24

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 401 |
| INVALID_15M | 370 |
| MISSING_LATEST_CLOSED_CANDLE | 288 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 401 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 370 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 5371389 | +5.51% | INVALID_5M | 99/1 | 99/0 |
| USDC-EUR | 2623461 | -0.14% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 2572670 | -0.23% | INVALID_5M | 98/2 | 99/0 |
| PUMP-EUR | 2424610 | -2.08% | INVALID_5M | 99/4 | 99/0 |
| XLM-EUR | 2120554 | +3.22% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2015428 | +15.96% | INVALID_5M | 99/1 | 99/0 |
| PEPE-EUR | 1873667 | +3.16% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1864977 | +3.58% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1710460 | +14.48% | INVALID_5M | 99/5 | 99/0 |
| AVAX-EUR | 1677050 | +6.86% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1628545 | +6.14% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1567246 | +5.88% | INVALID_5M | 99/7 | 99/0 |
| F-EUR | 1523198 | +34.56% | INVALID_5M | 99/2 | 83/0 |
| DOT-EUR | 1347145 | -0.81% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1323940 | +14.11% | INVALID_5M | 99/10 | 99/0 |
| RAY-EUR | 1276146 | +4.29% | INVALID_15M, INVALID_5M | 99/6 | 99/1 |
| HBAR-EUR | 1251102 | +2.73% | INVALID_15M, INVALID_5M | 99/17 | 99/1 |
| COTI-EUR | 1218840 | -8.86% | INVALID_15M, INVALID_5M | 99/11 | 99/2 |
| AAVE-EUR | 1110712 | +6.33% | INVALID_5M | 99/1 | 99/0 |
| BNB-EUR | 1022487 | +1.21% | INVALID_15M, INVALID_5M | 100/1 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
