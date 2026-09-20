# Audit qualité des données Bitvavo

Scan : 2026-09-20T16:36:04.478694+00:00 (20260920T163438Z-7595bac6)
Univers : 426 | strategy-grade : 34 | rejetés : 392
5m valides : 37 | 15m valides : 77 | deux intervalles valides : 34

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 389 |
| INVALID_15M | 349 |
| MISSING_LATEST_CLOSED_CANDLE | 211 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 389 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 349 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| INJ-EUR | 2907066 | +9.17% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1626664 | +0.18% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1616883 | +2.92% | INVALID_5M | 99/2 | 99/0 |
| UNI-EUR | 1370481 | -0.13% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1321923 | +2.94% | INVALID_5M | 99/9 | 99/0 |
| LSK-EUR | 1237016 | -5.51% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 987273 | -0.12% | INVALID_5M | 99/2 | 99/0 |
| STRK-EUR | 928180 | +5.89% | INVALID_5M | 99/2 | 99/0 |
| STX-EUR | 892484 | +2.74% | INVALID_15M, INVALID_5M | 99/9 | 99/3 |
| DOT-EUR | 882657 | +0.99% | INVALID_5M | 99/1 | 99/0 |
| FIL-EUR | 856448 | -5.61% | INVALID_15M, INVALID_5M | 95/6 | 99/4 |
| RENDER-EUR | 855930 | +7.03% | INVALID_15M | 99/0 | 99/1 |
| SKL-EUR | 792378 | +6.68% | INVALID_5M | 99/3 | 99/0 |
| SHIB-EUR | 748755 | -1.35% | INVALID_5M | 99/5 | 99/0 |
| APT-EUR | 716945 | +0.16% | INVALID_5M | 99/5 | 99/0 |
| ZIL-EUR | 709194 | +5.26% | INVALID_15M, INVALID_5M | 99/22 | 99/2 |
| S-EUR | 700427 | +7.98% | INVALID_5M | 100/1 | 99/0 |
| USELESS-EUR | 646342 | -8.58% | INVALID_5M | 99/2 | 99/0 |
| AAVE-EUR | 642150 | -3.67% | INVALID_5M | 99/2 | 99/0 |
| BCH-EUR | 626827 | -2.29% | INVALID_15M, INVALID_5M | 95/10 | 100/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
