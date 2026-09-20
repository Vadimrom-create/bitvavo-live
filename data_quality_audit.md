# Audit qualité des données Bitvavo

Scan : 2026-09-20T15:16:38.504237+00:00 (20260920T151507Z-3432774f)
Univers : 426 | strategy-grade : 34 | rejetés : 392
5m valides : 36 | 15m valides : 72 | deux intervalles valides : 34

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 390 |
| INVALID_15M | 354 |
| MISSING_LATEST_CLOSED_CANDLE | 244 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 390 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 354 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| INJ-EUR | 2728111 | +5.96% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 1769634 | -2.32% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1465625 | -0.92% | INVALID_5M | 99/2 | 100/0 |
| PUMP-EUR | 1416580 | -1.77% | INVALID_5M | 100/4 | 100/0 |
| UNI-EUR | 1402703 | -4.08% | INVALID_5M | 99/2 | 99/0 |
| CAKE-EUR | 1321946 | +2.96% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| LTC-EUR | 975270 | -1.16% | INVALID_5M | 99/4 | 100/0 |
| STRK-EUR | 964829 | +4.81% | INVALID_5M | 99/1 | 100/0 |
| STX-EUR | 900041 | +2.30% | INVALID_15M, INVALID_5M | 99/8 | 100/2 |
| FIL-EUR | 877906 | -5.62% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 93/7 | 100/4 |
| DOT-EUR | 846926 | -1.55% | INVALID_5M | 99/3 | 99/0 |
| SKL-EUR | 785347 | +9.92% | INVALID_5M | 99/2 | 100/0 |
| SHIB-EUR | 750192 | -1.98% | INVALID_5M | 99/4 | 100/0 |
| APT-EUR | 740002 | -3.46% | INVALID_5M | 100/3 | 100/0 |
| ZIL-EUR | 701105 | +7.05% | INVALID_15M, INVALID_5M | 100/13 | 100/1 |
| USELESS-EUR | 699888 | -8.92% | INVALID_5M | 99/3 | 100/0 |
| CAP-EUR | 683225 | -7.83% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 100/0 |
| BCH-EUR | 669024 | -2.88% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 92/13 | 100/2 |
| DRIFT-EUR | 609888 | +6.67% | INVALID_15M | 100/0 | 100/1 |
| PTB-EUR | 570785 | +17.42% | INVALID_15M | 83/0 | 90/5 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
