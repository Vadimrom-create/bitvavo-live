# Audit qualité des données Bitvavo

Scan : 2026-09-19T15:00:15.077109+00:00 (20260919T145843Z-22ba4ecb)
Univers : 427 | strategy-grade : 34 | rejetés : 393
5m valides : 36 | 15m valides : 82 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 345 |
| MISSING_LATEST_CLOSED_CANDLE | 197 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 345 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| SYN-EUR | 2445025 | +35.00% | INVALID_5M | 99/1 | 100/0 |
| STRK-EUR | 2271981 | +25.05% | INVALID_5M | 99/2 | 100/0 |
| ARB-EUR | 2082503 | +0.16% | INVALID_5M | 99/1 | 100/0 |
| LSK-EUR | 1881790 | -6.46% | INVALID_5M | 100/1 | 100/0 |
| APT-EUR | 1805780 | +7.72% | INVALID_5M | 100/2 | 100/0 |
| POL-EUR | 1605048 | +4.56% | INVALID_5M | 99/3 | 100/0 |
| CAP-EUR | 1526341 | -14.30% | INVALID_15M | 84/0 | 100/2 |
| SAGA-EUR | 1332332 | +25.76% | INVALID_5M | 100/2 | 100/0 |
| SKY-EUR | 1254730 | -1.12% | INVALID_5M | 100/9 | 100/0 |
| OP-EUR | 1200373 | +9.82% | INVALID_5M | 100/4 | 100/0 |
| AAVE-EUR | 1081839 | +3.29% | MISSING_LATEST_CLOSED_CANDLE | 100/0 | 100/0 |
| DOT-EUR | 990469 | -1.13% | INVALID_5M | 99/3 | 100/0 |
| BCH-EUR | 951383 | -0.14% | INVALID_5M | 99/5 | 100/0 |
| C-EUR | 905398 | +16.34% | INVALID_5M | 99/4 | 100/0 |
| HEI-EUR | 816999 | +10.25% | INVALID_5M | 100/3 | 100/0 |
| MORPHO-EUR | 801524 | +11.25% | INVALID_5M | 99/1 | 100/0 |
| RAY-EUR | 796216 | +5.78% | INVALID_5M | 100/2 | 100/0 |
| JUP-EUR | 783009 | +6.07% | INVALID_5M | 99/3 | 100/0 |
| COTI-EUR | 767737 | -3.57% | INVALID_5M | 99/3 | 100/0 |
| EPIC-EUR | 762604 | +24.10% | INVALID_5M | 99/4 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
