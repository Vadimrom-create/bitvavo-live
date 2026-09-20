# Audit qualité des données Bitvavo

Scan : 2026-09-20T18:23:10.431169+00:00 (20260920T182141Z-fb724ce8)
Univers : 426 | strategy-grade : 42 | rejetés : 384
5m valides : 50 | 15m valides : 82 | deux intervalles valides : 44

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 376 |
| INVALID_15M | 344 |
| MISSING_LATEST_CLOSED_CANDLE | 268 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 376 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 344 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| INJ-EUR | 2942959 | +3.19% | INVALID_5M | 99/1 | 99/0 |
| G-EUR | 2910701 | -29.69% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| PUMP-EUR | 1681308 | +1.09% | INVALID_5M | 100/1 | 99/0 |
| CAKE-EUR | 1358219 | +4.02% | INVALID_5M | 99/9 | 99/0 |
| UNI-EUR | 1307839 | +1.87% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1261721 | -2.90% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| STX-EUR | 889989 | +5.64% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| SKL-EUR | 839871 | +10.78% | INVALID_5M | 99/2 | 99/0 |
| VET-EUR | 800444 | -1.36% | INVALID_5M | 99/1 | 99/0 |
| S-EUR | 780895 | +14.15% | INVALID_5M | 99/3 | 99/0 |
| SHIB-EUR | 774213 | -1.93% | INVALID_5M | 99/2 | 99/0 |
| FIL-EUR | 730046 | -15.73% | INVALID_15M, INVALID_5M | 100/2 | 99/2 |
| ZIL-EUR | 711703 | +3.87% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/12 | 99/2 |
| KMNO-EUR | 672060 | +13.60% | INVALID_15M | 95/0 | 99/2 |
| XPL-EUR | 669675 | -2.21% | INVALID_5M | 100/1 | 99/0 |
| VVV-EUR | 625959 | +5.87% | INVALID_5M | 99/3 | 99/0 |
| POL-EUR | 621903 | +3.09% | INVALID_5M | 99/1 | 99/0 |
| TIA-EUR | 577907 | +0.94% | INVALID_15M, INVALID_5M | 99/6 | 99/1 |
| NPC-EUR | 562593 | +4.04% | INVALID_5M | 100/1 | 99/0 |
| GRASS-EUR | 549750 | +3.72% | INVALID_5M | 99/6 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
