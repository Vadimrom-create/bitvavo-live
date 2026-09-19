# Audit qualité des données Bitvavo

Scan : 2026-09-19T13:17:40.565194+00:00 (20260919T131610Z-e9a8f305)
Univers : 427 | strategy-grade : 37 | rejetés : 390
5m valides : 39 | 15m valides : 83 | deux intervalles valides : 38

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 388 |
| INVALID_15M | 344 |
| MISSING_LATEST_CLOSED_CANDLE | 228 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 388 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 344 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 3191856 | +3.55% | INVALID_5M | 99/1 | 100/0 |
| G-EUR | 2601816 | +3.12% | INVALID_5M | 99/3 | 99/0 |
| ENA-EUR | 2543530 | +22.95% | INVALID_5M | 99/1 | 99/0 |
| LSK-EUR | 2252591 | -10.55% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1800804 | +6.84% | INVALID_5M | 99/3 | 99/0 |
| LTC-EUR | 1642995 | +4.54% | INVALID_5M | 99/1 | 99/0 |
| F-EUR | 1629117 | +26.92% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1622331 | +4.44% | INVALID_5M | 99/3 | 99/0 |
| SKY-EUR | 1371551 | +6.22% | INVALID_5M | 99/11 | 100/0 |
| AAVE-EUR | 1208545 | +2.77% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 1070571 | +0.84% | INVALID_5M | 99/10 | 99/0 |
| DOT-EUR | 1057260 | -2.11% | INVALID_5M | 99/1 | 99/0 |
| HEI-EUR | 848363 | +29.01% | INVALID_5M | 99/1 | 99/0 |
| C-EUR | 837666 | +14.48% | INVALID_5M | 100/7 | 100/0 |
| MORPHO-EUR | 821573 | +11.36% | INVALID_5M | 99/7 | 100/0 |
| LPT-EUR | 808046 | +5.99% | INVALID_5M | 99/7 | 100/0 |
| BNB-EUR | 804199 | +2.68% | INVALID_5M | 99/2 | 100/0 |
| EPIC-EUR | 749968 | +21.05% | INVALID_5M | 99/3 | 99/0 |
| LAPTOP-EUR | 734756 | -16.35% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 100/0 |
| SUPER-EUR | 729298 | +5.31% | INVALID_15M, INVALID_5M | 100/39 | 100/6 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
