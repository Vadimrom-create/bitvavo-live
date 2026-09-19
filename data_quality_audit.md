# Audit qualité des données Bitvavo

Scan : 2026-09-19T14:18:31.124750+00:00 (20260919T141701Z-b4d189dd)
Univers : 427 | strategy-grade : 34 | rejetés : 393
5m valides : 35 | 15m valides : 82 | deux intervalles valides : 34

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 345 |
| MISSING_LATEST_CLOSED_CANDLE | 226 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 345 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 2998550 | +2.81% | INVALID_5M | 99/1 | 99/0 |
| G-EUR | 2465608 | -6.92% | INVALID_5M | 99/1 | 99/0 |
| ARB-EUR | 2115028 | -1.88% | INVALID_5M | 99/1 | 99/0 |
| LSK-EUR | 2009485 | -8.12% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1795726 | +9.56% | INVALID_5M | 99/3 | 99/0 |
| F-EUR | 1648508 | +24.48% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1628417 | +4.79% | INVALID_5M | 99/3 | 99/0 |
| SKY-EUR | 1396920 | +2.33% | INVALID_5M | 99/9 | 99/0 |
| OP-EUR | 1182162 | +12.67% | INVALID_5M | 99/4 | 99/0 |
| AAVE-EUR | 1142400 | +3.58% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 1138677 | -5.35% | INVALID_15M | 99/0 | 99/2 |
| DOT-EUR | 970721 | -1.48% | INVALID_5M | 99/3 | 99/0 |
| BCH-EUR | 913785 | +0.21% | INVALID_5M | 99/7 | 99/0 |
| HEI-EUR | 867524 | +22.30% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| C-EUR | 854498 | +17.71% | INVALID_5M | 99/8 | 99/0 |
| RAY-EUR | 819903 | +6.67% | INVALID_5M | 99/1 | 99/0 |
| COTI-EUR | 798073 | -4.24% | INVALID_5M | 99/2 | 100/0 |
| MORPHO-EUR | 796283 | +11.32% | INVALID_5M | 99/6 | 100/0 |
| BNB-EUR | 751017 | +1.48% | INVALID_5M | 99/2 | 99/0 |
| EPIC-EUR | 748831 | +19.03% | INVALID_5M | 99/4 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
