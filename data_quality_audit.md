# Audit qualité des données Bitvavo

Scan : 2026-09-20T19:10:43.100639+00:00 (20260920T190908Z-b42b1254)
Univers : 426 | strategy-grade : 39 | rejetés : 387
5m valides : 42 | 15m valides : 83 | deux intervalles valides : 39

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 384 |
| INVALID_15M | 343 |
| MISSING_LATEST_CLOSED_CANDLE | 234 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 384 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 343 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| CELR-EUR | 3271130 | +26.91% | INVALID_5M | 100/1 | 99/0 |
| USDC-EUR | 2889319 | +0.03% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2866829 | -0.57% | INVALID_5M | 100/3 | 99/0 |
| G-EUR | 2841939 | -30.95% | INVALID_5M | 100/1 | 99/0 |
| PUMP-EUR | 1681788 | +0.58% | INVALID_5M | 99/2 | 99/0 |
| CAKE-EUR | 1413439 | +5.71% | INVALID_5M | 99/5 | 99/0 |
| UNI-EUR | 1291355 | +1.59% | INVALID_5M | 99/2 | 99/0 |
| DOGE-EUR | 1278951 | -3.18% | INVALID_5M | 100/1 | 99/0 |
| SYN-EUR | 1182977 | -11.69% | INVALID_5M | 100/2 | 99/0 |
| SKL-EUR | 866999 | +11.65% | INVALID_5M | 99/1 | 99/0 |
| S-EUR | 799436 | +16.03% | INVALID_5M | 99/1 | 99/0 |
| VET-EUR | 763991 | -4.04% | INVALID_5M | 100/1 | 99/0 |
| KMNO-EUR | 706980 | +13.35% | INVALID_15M | 99/0 | 99/2 |
| XPL-EUR | 683041 | -3.05% | INVALID_5M | 100/3 | 99/0 |
| STX-EUR | 672943 | +2.29% | INVALID_15M, INVALID_5M | 100/1 | 99/1 |
| AAVE-EUR | 672315 | -4.08% | INVALID_5M | 100/1 | 99/0 |
| ZIL-EUR | 669035 | -1.26% | INVALID_15M, INVALID_5M | 100/9 | 99/2 |
| FIL-EUR | 662028 | -9.77% | INVALID_15M, INVALID_5M | 100/4 | 99/1 |
| NPC-EUR | 581132 | +5.05% | INVALID_5M | 99/1 | 99/0 |
| TIA-EUR | 576448 | +0.44% | INVALID_15M, INVALID_5M | 100/5 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
