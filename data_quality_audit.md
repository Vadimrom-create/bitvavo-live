# Audit qualité des données Bitvavo

Scan : 2026-09-19T18:40:26.477538+00:00 (20260919T183820Z-3d68b4d2)
Univers : 427 | strategy-grade : 38 | rejetés : 389
5m valides : 38 | 15m valides : 99 | deux intervalles valides : 38

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 389 |
| INVALID_15M | 328 |
| MISSING_LATEST_CLOSED_CANDLE | 234 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 389 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 328 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| STRK-EUR | 2164678 | +8.02% | INVALID_5M | 99/4 | 99/0 |
| PUMP-EUR | 1920578 | -4.09% | INVALID_5M | 100/2 | 99/0 |
| APT-EUR | 1836711 | +5.82% | INVALID_5M | 99/2 | 99/0 |
| POL-EUR | 1548797 | +1.94% | INVALID_5M | 100/2 | 99/0 |
| LTC-EUR | 1443069 | +1.78% | INVALID_5M | 100/2 | 99/0 |
| OP-EUR | 1249320 | +7.28% | INVALID_5M | 99/3 | 99/0 |
| SKY-EUR | 1059571 | -0.66% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/12 | 100/2 |
| F-EUR | 1011687 | -9.23% | INVALID_5M | 100/8 | 99/0 |
| DOT-EUR | 988926 | -0.22% | INVALID_5M | 100/1 | 99/0 |
| BCH-EUR | 983424 | +0.20% | INVALID_5M | 100/5 | 99/0 |
| SAGA-EUR | 944896 | -1.09% | INVALID_5M | 100/2 | 99/0 |
| AAVE-EUR | 907272 | +3.01% | INVALID_5M | 100/6 | 99/0 |
| COTI-EUR | 879488 | -3.96% | INVALID_5M | 99/5 | 99/0 |
| MORPHO-EUR | 825569 | +9.49% | INVALID_5M | 100/4 | 99/0 |
| KAS-EUR | 815752 | +7.67% | INVALID_5M | 99/1 | 99/0 |
| HEI-EUR | 808554 | +11.95% | INVALID_5M | 99/2 | 99/0 |
| JUP-EUR | 737235 | +5.75% | INVALID_5M | 99/8 | 99/0 |
| C-EUR | 693630 | +5.47% | INVALID_5M | 99/1 | 99/0 |
| RAY-EUR | 667663 | -0.46% | INVALID_5M | 100/2 | 99/0 |
| BNB-EUR | 633259 | -0.29% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
