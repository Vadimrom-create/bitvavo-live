# Audit qualité des données Bitvavo

Scan : 2026-09-20T16:19:50.803487+00:00 (20260920T161826Z-e7348884)
Univers : 426 | strategy-grade : 33 | rejetés : 393
5m valides : 34 | 15m valides : 75 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 351 |
| MISSING_LATEST_CLOSED_CANDLE | 180 |

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
| INJ-EUR | 2857137 | +8.46% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1525510 | +1.33% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 1483657 | +0.58% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 1358885 | -1.25% | INVALID_5M | 98/1 | 99/0 |
| CAKE-EUR | 1323659 | +2.84% | INVALID_5M | 99/7 | 100/0 |
| LSK-EUR | 1221656 | -3.96% | INVALID_5M | 98/1 | 99/0 |
| LTC-EUR | 984246 | -0.34% | INVALID_5M | 99/2 | 99/0 |
| STRK-EUR | 939614 | +4.27% | INVALID_5M | 99/2 | 99/0 |
| STX-EUR | 898231 | +1.61% | INVALID_15M, INVALID_5M | 99/10 | 99/3 |
| FIL-EUR | 854944 | -5.38% | INVALID_15M, INVALID_5M | 94/6 | 99/4 |
| DOT-EUR | 848626 | +0.39% | INVALID_5M | 99/1 | 99/0 |
| SKL-EUR | 789738 | +7.96% | INVALID_5M | 99/2 | 100/0 |
| SHIB-EUR | 750152 | -1.61% | INVALID_5M | 100/4 | 100/0 |
| APT-EUR | 710572 | -1.89% | INVALID_5M | 99/5 | 99/0 |
| ZIL-EUR | 707954 | +5.49% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 98/21 | 99/2 |
| USELESS-EUR | 646188 | -7.02% | INVALID_5M | 98/2 | 99/0 |
| PTB-EUR | 637483 | +22.73% | INVALID_15M | 89/0 | 92/2 |
| BCH-EUR | 634882 | -2.27% | INVALID_15M, INVALID_5M | 92/17 | 99/2 |
| TIA-EUR | 560843 | +0.43% | INVALID_15M, INVALID_5M | 99/18 | 99/1 |
| POL-EUR | 551677 | +0.02% | INVALID_5M | 99/11 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
