# Audit qualité des données Bitvavo

Scan : 2026-09-19T14:47:03.797372+00:00 (20260919T144534Z-b0910449)
Univers : 427 | strategy-grade : 32 | rejetés : 395
5m valides : 34 | 15m valides : 81 | deux intervalles valides : 32

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 393 |
| INVALID_15M | 346 |
| MISSING_LATEST_CLOSED_CANDLE | 244 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 393 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 346 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| SYN-EUR | 2451989 | +34.71% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2273481 | +25.80% | INVALID_5M | 99/1 | 100/0 |
| G-EUR | 2200661 | -15.71% | INVALID_5M | 99/1 | 99/0 |
| ARB-EUR | 2086512 | +0.33% | INVALID_5M | 99/1 | 100/0 |
| LSK-EUR | 1908471 | -7.08% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1800596 | +7.99% | INVALID_5M | 100/2 | 100/0 |
| POL-EUR | 1614362 | +5.18% | INVALID_5M | 99/3 | 99/0 |
| CAP-EUR | 1499907 | -18.58% | INVALID_15M | 81/0 | 99/2 |
| SAGA-EUR | 1330290 | +26.50% | INVALID_5M | 99/2 | 100/0 |
| SKY-EUR | 1309177 | -0.89% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/10 | 100/0 |
| OP-EUR | 1197247 | +11.52% | INVALID_5M | 100/4 | 100/0 |
| DOT-EUR | 986379 | -0.44% | INVALID_5M | 99/3 | 99/0 |
| BCH-EUR | 954442 | -0.31% | INVALID_5M | 100/5 | 100/0 |
| C-EUR | 880093 | +20.91% | INVALID_5M | 99/4 | 99/0 |
| HEI-EUR | 825013 | +10.62% | INVALID_5M | 99/2 | 100/0 |
| RAY-EUR | 805810 | +5.91% | INVALID_5M | 99/2 | 100/0 |
| MORPHO-EUR | 801912 | +10.83% | INVALID_5M | 99/5 | 100/0 |
| JUP-EUR | 775530 | +7.48% | INVALID_5M | 99/3 | 99/0 |
| COTI-EUR | 764256 | -3.94% | INVALID_5M | 100/3 | 100/0 |
| EPIC-EUR | 753936 | +20.21% | INVALID_5M | 99/6 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
