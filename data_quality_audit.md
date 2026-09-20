# Audit qualité des données Bitvavo

Scan : 2026-09-20T19:04:28.024182+00:00 (20260920T190256Z-64ff7e1f)
Univers : 426 | strategy-grade : 39 | rejetés : 387
5m valides : 44 | 15m valides : 83 | deux intervalles valides : 41

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 382 |
| INVALID_15M | 343 |
| MISSING_LATEST_CLOSED_CANDLE | 246 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 382 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 343 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| CELR-EUR | 3271144 | +34.28% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2884620 | -0.23% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 100/0 |
| G-EUR | 2852716 | -31.41% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1685998 | +0.01% | INVALID_5M | 99/2 | 99/0 |
| CAKE-EUR | 1410639 | +5.58% | INVALID_5M | 99/5 | 99/0 |
| DOGE-EUR | 1288129 | -3.42% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 1285826 | +0.60% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 98/1 | 99/0 |
| SYN-EUR | 1183428 | -12.21% | MISSING_LATEST_CLOSED_CANDLE | 100/0 | 100/0 |
| SKL-EUR | 853346 | +11.63% | INVALID_5M | 99/1 | 99/0 |
| S-EUR | 794157 | +14.91% | INVALID_5M | 99/1 | 99/0 |
| VET-EUR | 768842 | -4.93% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 743578 | +2.63% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| KMNO-EUR | 706612 | +13.14% | INVALID_15M | 98/0 | 99/2 |
| XPL-EUR | 682362 | -3.00% | INVALID_5M | 98/3 | 99/0 |
| ZIL-EUR | 671315 | +0.30% | INVALID_15M, INVALID_5M | 100/8 | 100/2 |
| AAVE-EUR | 671160 | -4.40% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| FIL-EUR | 664373 | -12.19% | INVALID_15M, INVALID_5M | 99/5 | 99/1 |
| VVV-EUR | 624464 | +5.82% | INVALID_5M | 99/2 | 99/0 |
| NPC-EUR | 580122 | +5.05% | INVALID_5M | 99/1 | 99/0 |
| TIA-EUR | 574581 | -0.15% | INVALID_15M, INVALID_5M | 98/5 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
