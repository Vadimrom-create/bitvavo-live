# Audit qualité des données Bitvavo

Scan : 2026-09-19T17:03:55.605951+00:00 (20260919T170226Z-8c5fcea3)
Univers : 427 | strategy-grade : 35 | rejetés : 392
5m valides : 38 | 15m valides : 86 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 389 |
| INVALID_15M | 341 |
| MISSING_LATEST_CLOSED_CANDLE | 251 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 389 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 341 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| STRK-EUR | 2175765 | +18.04% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1861031 | +8.56% | INVALID_5M | 99/3 | 99/0 |
| CAP-EUR | 1804594 | -15.29% | INVALID_15M | 99/0 | 99/2 |
| POL-EUR | 1535156 | +4.15% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 99/0 |
| HBAR-EUR | 1476136 | +4.85% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1449216 | +6.08% | INVALID_5M | 99/1 | 99/0 |
| SAGA-EUR | 1349437 | +11.23% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1204642 | +8.72% | INVALID_5M | 99/7 | 100/0 |
| F-EUR | 1118968 | -15.64% | INVALID_5M | 99/4 | 99/0 |
| VET-EUR | 1068314 | +8.95% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1058850 | +0.89% | INVALID_15M, INVALID_5M | 99/9 | 99/1 |
| DOT-EUR | 937143 | +0.34% | INVALID_5M | 99/2 | 99/0 |
| AAVE-EUR | 925863 | +3.88% | INVALID_5M | 99/7 | 99/0 |
| COTI-EUR | 902567 | -0.94% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 898600 | +2.76% | INVALID_5M | 99/5 | 99/0 |
| MORPHO-EUR | 806303 | +12.05% | INVALID_5M | 99/3 | 99/0 |
| KAS-EUR | 797968 | +9.58% | INVALID_5M | 99/1 | 99/0 |
| HEI-EUR | 775281 | +14.51% | INVALID_5M | 100/3 | 100/0 |
| JUP-EUR | 771253 | +7.54% | INVALID_5M | 99/7 | 99/0 |
| LAPTOP-EUR | 648685 | -9.55% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
