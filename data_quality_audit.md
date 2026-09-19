# Audit qualité des données Bitvavo

Scan : 2026-09-19T22:21:49.326229+00:00 (20260919T222015Z-f6fcbab5)
Univers : 427 | strategy-grade : 31 | rejetés : 396
5m valides : 32 | 15m valides : 76 | deux intervalles valides : 31

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 395 |
| INVALID_15M | 351 |
| MISSING_LATEST_CLOSED_CANDLE | 282 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 395 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 351 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| USDC-EUR | 2672827 | -0.06% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 100/0 |
| UNI-EUR | 2282676 | -4.79% | INVALID_5M | 100/1 | 99/0 |
| PUMP-EUR | 1870402 | -5.12% | INVALID_5M | 100/2 | 99/0 |
| APT-EUR | 1692166 | -2.17% | INVALID_15M, INVALID_5M | 99/5 | 99/1 |
| WLD-EUR | 1419935 | +0.55% | INVALID_5M | 100/1 | 99/0 |
| STRK-EUR | 1412837 | -2.35% | INVALID_5M | 100/3 | 99/0 |
| CNPY-EUR | 1391935 | -23.88% | INVALID_5M | 100/1 | 99/0 |
| ARB-EUR | 1340873 | -7.68% | INVALID_5M | 100/1 | 99/0 |
| OP-EUR | 1216020 | +2.40% | INVALID_5M | 99/5 | 99/0 |
| USELESS-EUR | 1212638 | -14.88% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1072717 | -1.74% | INVALID_15M, INVALID_5M | 99/15 | 99/4 |
| POL-EUR | 1057412 | -2.60% | INVALID_5M | 100/6 | 99/0 |
| BCH-EUR | 976071 | -3.27% | INVALID_15M, INVALID_5M | 100/14 | 99/2 |
| DOT-EUR | 898671 | -3.00% | INVALID_5M | 99/3 | 99/0 |
| AAVE-EUR | 886606 | +1.02% | INVALID_5M | 99/3 | 99/0 |
| FIL-EUR | 875564 | +2.57% | INVALID_5M | 99/5 | 99/0 |
| HEI-EUR | 870509 | +13.42% | INVALID_5M | 100/6 | 99/0 |
| MORPHO-EUR | 854816 | +6.32% | INVALID_15M, INVALID_5M | 99/3 | 99/1 |
| SAGA-EUR | 830091 | +1.99% | INVALID_5M | 100/9 | 99/0 |
| STX-EUR | 827324 | +7.44% | INVALID_5M | 100/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
