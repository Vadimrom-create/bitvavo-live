# Audit qualité des données Bitvavo

Scan : 2026-09-20T18:01:52.216977+00:00 (20260920T175951Z-2fb8b864)
Univers : 426 | strategy-grade : 46 | rejetés : 380
5m valides : 49 | 15m valides : 83 | deux intervalles valides : 46

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 377 |
| INVALID_15M | 343 |
| MISSING_LATEST_CLOSED_CANDLE | 257 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 377 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 343 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| INJ-EUR | 2980696 | +2.41% | INVALID_5M | 99/1 | 100/0 |
| CAKE-EUR | 1356740 | +3.82% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/6 | 100/0 |
| UNI-EUR | 1292944 | +0.87% | INVALID_5M | 100/1 | 100/0 |
| STX-EUR | 890822 | +4.37% | INVALID_15M, INVALID_5M | 100/7 | 100/3 |
| SKL-EUR | 827179 | +8.47% | INVALID_5M | 99/2 | 100/0 |
| SHIB-EUR | 777534 | -1.87% | INVALID_5M | 99/3 | 100/0 |
| FIL-EUR | 768667 | -14.83% | INVALID_15M, INVALID_5M | 100/2 | 100/3 |
| S-EUR | 757093 | +13.39% | INVALID_5M | 100/2 | 100/0 |
| ZIL-EUR | 712582 | +5.03% | INVALID_15M, INVALID_5M | 100/12 | 100/2 |
| XPL-EUR | 665374 | -3.06% | INVALID_5M | 99/1 | 100/0 |
| KMNO-EUR | 663922 | +12.70% | INVALID_15M | 92/0 | 100/2 |
| VVV-EUR | 631228 | +5.90% | INVALID_5M | 99/3 | 99/0 |
| POL-EUR | 604422 | +2.25% | INVALID_5M | 99/2 | 100/0 |
| TIA-EUR | 572388 | +1.41% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/7 | 100/1 |
| GRASS-EUR | 568796 | +3.82% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| NPC-EUR | 549339 | +3.86% | INVALID_5M | 99/1 | 99/0 |
| JUP-EUR | 546634 | +0.61% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 100/0 |
| BCH-EUR | 531344 | -1.59% | INVALID_15M, INVALID_5M | 97/7 | 100/1 |
| CRV-EUR | 506552 | +2.36% | INVALID_15M, INVALID_5M | 85/7 | 100/2 |
| FTT-EUR | 498692 | +25.17% | INVALID_15M | 99/0 | 99/61 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
