# Audit qualité des données Bitvavo

Scan : 2026-09-19T11:58:31.455693+00:00 (20260919T115704Z-3f89aa78)
Univers : 427 | strategy-grade : 35 | rejetés : 392
5m valides : 36 | 15m valides : 80 | deux intervalles valides : 36

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 347 |
| MISSING_LATEST_CLOSED_CANDLE | 279 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 347 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| G-EUR | 2832864 | +3.62% | INVALID_5M | 99/2 | 99/0 |
| ENA-EUR | 2256516 | +16.33% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| WLD-EUR | 2141457 | -3.35% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2110426 | +31.63% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1700304 | +4.75% | INVALID_5M | 99/2 | 99/0 |
| F-EUR | 1620947 | +28.12% | INVALID_5M | 99/3 | 99/0 |
| POL-EUR | 1599886 | +5.45% | INVALID_5M | 99/6 | 99/0 |
| SKY-EUR | 1388764 | +4.40% | INVALID_5M | 100/5 | 99/0 |
| AAVE-EUR | 1198982 | +5.78% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 1197691 | +4.54% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1130867 | +14.13% | INVALID_5M | 99/2 | 99/0 |
| BCH-EUR | 1063508 | +1.26% | INVALID_5M | 100/10 | 99/0 |
| SAGA-EUR | 997680 | +32.84% | INVALID_5M | 99/1 | 99/0 |
| MORPHO-EUR | 850869 | +14.00% | INVALID_5M | 99/3 | 99/0 |
| LPT-EUR | 850381 | +7.06% | INVALID_5M | 99/6 | 99/0 |
| S-EUR | 818872 | +6.50% | INVALID_15M, INVALID_5M | 100/19 | 99/3 |
| C-EUR | 811012 | +17.82% | INVALID_5M | 100/6 | 99/0 |
| BNB-EUR | 805760 | +2.29% | INVALID_15M, INVALID_5M | 100/1 | 99/1 |
| SUPER-EUR | 792406 | +8.02% | INVALID_15M, INVALID_5M | 100/25 | 99/3 |
| LAPTOP-EUR | 746166 | -18.26% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
