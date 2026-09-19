# Audit qualité des données Bitvavo

Scan : 2026-09-19T13:59:00.702304+00:00 (20260919T135730Z-10520548)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 34 | 15m valides : 85 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 393 |
| INVALID_15M | 342 |
| MISSING_LATEST_CLOSED_CANDLE | 281 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 393 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 342 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 2989175 | +3.79% | INVALID_5M | 99/1 | 99/0 |
| ENA-EUR | 2631479 | +22.44% | INVALID_5M | 99/1 | 99/0 |
| G-EUR | 2554822 | +1.89% | INVALID_5M | 99/1 | 99/0 |
| LSK-EUR | 2175967 | -5.07% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1791377 | +6.49% | INVALID_5M | 99/3 | 99/0 |
| F-EUR | 1639443 | +25.50% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1625659 | +4.70% | INVALID_5M | 99/4 | 99/0 |
| SKY-EUR | 1418483 | +3.97% | INVALID_5M | 99/9 | 99/0 |
| AAVE-EUR | 1194457 | +2.46% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1176087 | +10.94% | INVALID_5M | 100/2 | 99/0 |
| DOT-EUR | 986621 | -1.27% | INVALID_5M | 100/2 | 99/0 |
| CAP-EUR | 933441 | -5.29% | INVALID_15M | 99/0 | 99/2 |
| BCH-EUR | 931377 | -0.10% | INVALID_5M | 99/10 | 99/0 |
| HEI-EUR | 868538 | +25.94% | INVALID_5M | 100/1 | 99/0 |
| C-EUR | 842077 | +17.68% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/7 | 99/0 |
| RAY-EUR | 841971 | +7.98% | INVALID_5M | 99/1 | 99/0 |
| COTI-EUR | 814664 | -3.94% | INVALID_5M | 99/2 | 99/0 |
| MORPHO-EUR | 797105 | +14.18% | INVALID_5M | 99/7 | 99/0 |
| LPT-EUR | 794529 | +6.59% | INVALID_5M | 99/4 | 99/0 |
| BNB-EUR | 758748 | +1.43% | INVALID_5M | 99/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
