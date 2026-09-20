# Audit qualité des données Bitvavo

Scan : 2026-09-20T07:31:17.513912+00:00 (20260920T072921Z-2eecd1da)
Univers : 426 | strategy-grade : 31 | rejetés : 395
5m valides : 34 | 15m valides : 64 | deux intervalles valides : 31

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 362 |
| MISSING_LATEST_CLOSED_CANDLE | 250 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 362 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2680841 | -0.62% | INVALID_5M | 99/5 | 100/0 |
| HBAR-EUR | 2247015 | +3.65% | INVALID_5M | 99/1 | 100/0 |
| CAP-EUR | 2020883 | -19.21% | INVALID_5M | 100/1 | 100/0 |
| FET-EUR | 2011470 | -3.95% | INVALID_5M | 99/1 | 100/0 |
| PUMP-EUR | 1714250 | -2.99% | INVALID_5M | 99/5 | 100/0 |
| DOGE-EUR | 1673356 | -2.16% | INVALID_5M | 100/3 | 100/0 |
| LTC-EUR | 1320802 | -0.33% | INVALID_5M | 99/3 | 100/0 |
| EPIC-EUR | 1085568 | +11.57% | INVALID_15M, INVALID_5M | 100/4 | 100/3 |
| VET-EUR | 1060965 | -4.21% | INVALID_5M | 99/2 | 100/0 |
| STRK-EUR | 1034395 | +13.25% | INVALID_5M | 99/3 | 100/0 |
| CAKE-EUR | 1034072 | -1.27% | INVALID_15M, INVALID_5M | 99/15 | 100/7 |
| STX-EUR | 993612 | +11.35% | INVALID_5M | 99/1 | 100/0 |
| APT-EUR | 957932 | +2.86% | INVALID_15M, INVALID_5M | 100/20 | 100/2 |
| FIL-EUR | 871378 | +0.68% | INVALID_15M, INVALID_5M | 99/16 | 100/3 |
| USELESS-EUR | 863299 | -7.40% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 100/0 |
| HEI-EUR | 837387 | -3.28% | INVALID_15M, INVALID_5M | 99/6 | 100/2 |
| BCH-EUR | 820631 | +0.50% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 83/15 | 100/2 |
| SAGA-EUR | 758509 | +7.32% | INVALID_5M | 99/1 | 100/0 |
| KAS-EUR | 756809 | +1.99% | INVALID_15M, INVALID_5M | 94/3 | 100/7 |
| JUP-EUR | 741880 | -0.07% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
