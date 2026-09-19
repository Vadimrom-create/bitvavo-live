# Audit qualité des données Bitvavo

Scan : 2026-09-19T21:22:22.834364+00:00 (20260919T212052Z-c4dc9c8b)
Univers : 427 | strategy-grade : 29 | rejetés : 398
5m valides : 30 | 15m valides : 79 | deux intervalles valides : 29

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 397 |
| INVALID_15M | 348 |
| MISSING_LATEST_CLOSED_CANDLE | 264 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 397 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 348 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| USDC-EUR | 2698916 | -0.03% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 2373676 | -6.25% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1840021 | -5.65% | INVALID_5M | 99/4 | 99/0 |
| APT-EUR | 1729047 | -2.72% | INVALID_15M, INVALID_5M | 99/10 | 99/1 |
| STRK-EUR | 1547498 | -0.99% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1393604 | +0.48% | INVALID_5M | 99/2 | 99/0 |
| ARB-EUR | 1388549 | -9.90% | INVALID_5M | 99/1 | 99/0 |
| CNPY-EUR | 1294140 | -20.37% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 1281608 | -13.71% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1233917 | +0.50% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/9 | 100/0 |
| POL-EUR | 1108290 | -4.03% | INVALID_5M | 99/4 | 99/0 |
| SKY-EUR | 1056231 | -2.08% | INVALID_15M, INVALID_5M | 99/25 | 99/4 |
| BCH-EUR | 982615 | -2.21% | INVALID_15M, INVALID_5M | 99/15 | 99/2 |
| DOT-EUR | 926201 | -3.69% | INVALID_5M | 99/2 | 99/0 |
| AAVE-EUR | 876294 | +0.75% | INVALID_5M | 99/5 | 99/0 |
| HEI-EUR | 864461 | +15.46% | INVALID_5M | 100/2 | 99/0 |
| MORPHO-EUR | 852500 | +7.76% | INVALID_15M, INVALID_5M | 99/5 | 99/1 |
| SAGA-EUR | 833065 | -1.03% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/10 | 99/0 |
| COTI-EUR | 823289 | -10.40% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 100/0 |
| FIL-EUR | 820045 | +10.75% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
