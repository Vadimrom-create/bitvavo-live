# Audit qualité des données Bitvavo

Scan : 2026-09-20T14:11:48.521919+00:00 (20260920T141018Z-7092e807)
Univers : 426 | strategy-grade : 34 | rejetés : 392
5m valides : 35 | 15m valides : 78 | deux intervalles valides : 34

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 348 |
| MISSING_LATEST_CLOSED_CANDLE | 293 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 348 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| FET-EUR | 2137908 | -6.32% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 1847124 | -4.03% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 1437139 | -4.15% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 1431232 | -2.16% | INVALID_5M | 99/5 | 99/0 |
| WLD-EUR | 1428226 | -1.93% | INVALID_5M | 99/6 | 99/0 |
| CAKE-EUR | 1313399 | +3.63% | INVALID_5M | 99/3 | 99/0 |
| LSK-EUR | 1190356 | -12.18% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1104354 | -0.73% | INVALID_5M | 100/4 | 99/0 |
| ARB-EUR | 1046133 | -0.66% | INVALID_5M | 99/1 | 99/0 |
| FIL-EUR | 895507 | -6.88% | INVALID_15M, INVALID_5M | 91/23 | 99/4 |
| STX-EUR | 892477 | +0.34% | INVALID_15M, INVALID_5M | 99/16 | 99/2 |
| DOT-EUR | 838820 | -1.80% | INVALID_5M | 100/4 | 99/0 |
| APT-EUR | 783631 | -2.19% | INVALID_5M | 100/4 | 99/0 |
| SHIB-EUR | 779953 | -2.06% | INVALID_5M | 100/3 | 99/0 |
| USELESS-EUR | 742258 | -4.44% | INVALID_5M | 99/3 | 99/0 |
| SKL-EUR | 741392 | +6.32% | INVALID_5M | 99/2 | 99/0 |
| BCH-EUR | 738400 | -2.63% | INVALID_15M, INVALID_5M | 89/14 | 99/2 |
| ZIL-EUR | 700831 | +4.20% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 99/0 |
| S-EUR | 671125 | +7.48% | INVALID_5M | 100/2 | 99/0 |
| DRIFT-EUR | 646158 | +4.62% | INVALID_15M, INVALID_5M | 99/7 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
