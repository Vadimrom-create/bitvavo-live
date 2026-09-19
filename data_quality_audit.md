# Audit qualité des données Bitvavo

Scan : 2026-09-19T21:05:16.692779+00:00 (20260919T210343Z-8d891de9)
Univers : 427 | strategy-grade : 30 | rejetés : 397
5m valides : 31 | 15m valides : 82 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 396 |
| INVALID_15M | 345 |
| MISSING_LATEST_CLOSED_CANDLE | 230 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 396 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 345 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| USDC-EUR | 2660455 | -0.03% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 2370556 | -4.43% | INVALID_5M | 100/1 | 99/0 |
| PUMP-EUR | 1842702 | -4.58% | INVALID_5M | 100/3 | 99/0 |
| APT-EUR | 1721065 | -0.21% | INVALID_15M, INVALID_5M | 99/11 | 99/1 |
| ARB-EUR | 1402229 | -8.77% | INVALID_5M | 99/3 | 99/0 |
| WLD-EUR | 1318498 | +2.05% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1286144 | -22.45% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 1279461 | -12.99% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1225008 | +2.40% | INVALID_5M | 100/8 | 100/0 |
| POL-EUR | 1080738 | -2.57% | INVALID_5M | 99/6 | 99/0 |
| SKY-EUR | 1050990 | -1.99% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/25 | 99/3 |
| BCH-EUR | 972372 | -1.12% | INVALID_15M, INVALID_5M | 99/15 | 99/2 |
| DOT-EUR | 932873 | -1.65% | INVALID_5M | 100/3 | 99/0 |
| AAVE-EUR | 875241 | +1.20% | INVALID_5M | 100/5 | 99/0 |
| HEI-EUR | 865582 | +15.41% | INVALID_5M | 100/2 | 99/0 |
| MORPHO-EUR | 846118 | +7.74% | INVALID_15M, INVALID_5M | 99/6 | 99/1 |
| SAGA-EUR | 831531 | -0.68% | INVALID_5M | 99/9 | 100/0 |
| COTI-EUR | 827232 | -10.28% | INVALID_5M | 100/2 | 99/0 |
| STX-EUR | 815396 | +8.83% | INVALID_5M | 100/1 | 99/0 |
| FIL-EUR | 812811 | +10.45% | INVALID_5M | 100/1 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
