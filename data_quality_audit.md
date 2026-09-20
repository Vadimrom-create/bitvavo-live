# Audit qualité des données Bitvavo

Scan : 2026-09-20T15:32:49.758089+00:00 (20260920T153121Z-73695bad)
Univers : 426 | strategy-grade : 33 | rejetés : 393
5m valides : 35 | 15m valides : 72 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 354 |
| MISSING_LATEST_CLOSED_CANDLE | 268 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 354 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| INJ-EUR | 2717980 | +6.03% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 1672247 | -2.57% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1483902 | -1.16% | INVALID_5M | 99/4 | 99/0 |
| WLD-EUR | 1464035 | -0.20% | INVALID_5M | 99/2 | 99/0 |
| UNI-EUR | 1385039 | -2.97% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1320883 | +3.67% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 100/0 |
| LTC-EUR | 969228 | -1.21% | INVALID_5M | 99/3 | 100/0 |
| STRK-EUR | 957850 | +5.63% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 899413 | +1.03% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/8 | 100/2 |
| FIL-EUR | 866451 | -5.83% | INVALID_15M, INVALID_5M | 93/4 | 99/4 |
| DOT-EUR | 850889 | -0.73% | INVALID_5M | 99/2 | 99/0 |
| SKL-EUR | 786822 | +8.69% | INVALID_5M | 99/1 | 100/0 |
| SHIB-EUR | 734981 | -1.81% | INVALID_5M | 99/4 | 99/0 |
| APT-EUR | 717834 | -2.62% | INVALID_5M | 100/3 | 100/0 |
| ZIL-EUR | 700666 | +6.90% | INVALID_15M, INVALID_5M | 100/15 | 100/1 |
| USELESS-EUR | 664594 | -7.82% | INVALID_5M | 99/3 | 99/0 |
| BCH-EUR | 652983 | -3.08% | INVALID_15M, INVALID_5M | 91/15 | 100/2 |
| CAP-EUR | 646519 | -7.94% | INVALID_5M | 99/4 | 100/0 |
| DRIFT-EUR | 612098 | +4.36% | INVALID_15M | 99/0 | 99/1 |
| PTB-EUR | 582478 | +17.33% | INVALID_15M | 84/0 | 91/5 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
