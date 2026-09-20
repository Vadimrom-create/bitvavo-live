# Audit qualité des données Bitvavo

Scan : 2026-09-20T18:54:15.814085+00:00 (20260920T185244Z-d2564f0c)
Univers : 426 | strategy-grade : 40 | rejetés : 386
5m valides : 43 | 15m valides : 84 | deux intervalles valides : 40

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 383 |
| INVALID_15M | 342 |
| MISSING_LATEST_CLOSED_CANDLE | 279 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 383 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 342 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| CELR-EUR | 3289681 | +31.43% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2895332 | +0.95% | INVALID_5M | 99/2 | 99/0 |
| G-EUR | 2875277 | -33.76% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1690937 | -0.28% | INVALID_5M | 99/2 | 99/0 |
| CAKE-EUR | 1398892 | +5.47% | INVALID_5M | 99/7 | 99/0 |
| UNI-EUR | 1290654 | +0.61% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1242842 | -3.15% | INVALID_5M | 99/1 | 99/0 |
| SKL-EUR | 851541 | +9.56% | INVALID_5M | 99/1 | 99/0 |
| S-EUR | 801334 | +14.63% | INVALID_5M | 99/1 | 99/0 |
| VET-EUR | 778487 | -4.27% | INVALID_5M | 98/1 | 99/0 |
| STX-EUR | 748981 | +2.55% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| KMNO-EUR | 694813 | +13.67% | INVALID_15M | 96/0 | 99/2 |
| ZIL-EUR | 677974 | -0.79% | INVALID_15M, INVALID_5M | 100/8 | 99/2 |
| XPL-EUR | 673111 | -3.59% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| FIL-EUR | 667824 | -12.12% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 99/2 |
| POL-EUR | 639560 | +2.35% | INVALID_5M | 98/1 | 99/0 |
| VVV-EUR | 622144 | +5.02% | INVALID_5M | 99/3 | 99/0 |
| NPC-EUR | 579072 | +5.13% | INVALID_5M | 99/1 | 99/0 |
| TIA-EUR | 572900 | +0.47% | INVALID_15M, INVALID_5M | 98/5 | 99/1 |
| GRASS-EUR | 554651 | +2.52% | INVALID_5M | 100/6 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
