# Audit qualité des données Bitvavo

Scan : 2026-09-19T16:20:25.259996+00:00 (20260919T161850Z-f97201ed)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 38 | 15m valides : 85 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 389 |
| INVALID_15M | 342 |
| MISSING_LATEST_CLOSED_CANDLE | 215 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 389 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 342 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| SYN-EUR | 2527086 | +30.19% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2187191 | +18.66% | INVALID_5M | 100/2 | 99/0 |
| APT-EUR | 1856677 | +9.61% | INVALID_5M | 100/1 | 100/0 |
| CAP-EUR | 1755368 | -12.54% | INVALID_15M | 95/0 | 99/2 |
| POL-EUR | 1547246 | +3.91% | INVALID_5M | 100/3 | 99/0 |
| HBAR-EUR | 1431899 | +3.93% | INVALID_5M | 99/1 | 99/0 |
| SAGA-EUR | 1361314 | +21.62% | INVALID_5M | 100/3 | 99/0 |
| OP-EUR | 1208110 | +10.26% | INVALID_5M | 99/9 | 99/0 |
| F-EUR | 1195594 | -11.91% | INVALID_5M | 100/2 | 99/0 |
| SKY-EUR | 1107013 | -1.80% | INVALID_5M | 100/6 | 100/0 |
| AAVE-EUR | 1092987 | +2.29% | INVALID_5M | 100/3 | 100/0 |
| VET-EUR | 1076028 | +8.13% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 983764 | +1.09% | INVALID_5M | 99/3 | 99/0 |
| DOT-EUR | 954151 | -1.23% | INVALID_5M | 99/2 | 99/0 |
| COTI-EUR | 912654 | -2.84% | INVALID_5M | 99/2 | 99/0 |
| EPIC-EUR | 856237 | +28.55% | INVALID_5M | 99/2 | 99/0 |
| MORPHO-EUR | 801449 | +11.40% | INVALID_5M | 100/2 | 99/0 |
| JUP-EUR | 777458 | +6.77% | INVALID_5M | 100/2 | 99/0 |
| HEI-EUR | 767865 | +13.63% | INVALID_5M | 99/3 | 99/0 |
| KAS-EUR | 759635 | +11.46% | INVALID_5M | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
