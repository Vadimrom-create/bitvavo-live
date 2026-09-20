# Audit qualité des données Bitvavo

Scan : 2026-09-20T18:41:03.841538+00:00 (20260920T183932Z-ce96c7eb)
Univers : 426 | strategy-grade : 41 | rejetés : 385
5m valides : 46 | 15m valides : 83 | deux intervalles valides : 42

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 380 |
| INVALID_15M | 343 |
| MISSING_LATEST_CLOSED_CANDLE | 274 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 380 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 343 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| CELR-EUR | 3305758 | +35.98% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| INJ-EUR | 2922012 | +1.04% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 99/0 |
| G-EUR | 2871652 | -33.58% | INVALID_5M | 100/1 | 99/0 |
| PUMP-EUR | 1695686 | +0.12% | INVALID_5M | 100/1 | 99/0 |
| CAKE-EUR | 1397891 | +5.64% | INVALID_5M | 100/8 | 99/0 |
| UNI-EUR | 1287570 | +0.14% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1250979 | -3.40% | INVALID_5M | 99/1 | 99/0 |
| SKL-EUR | 848786 | +9.70% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 845698 | +3.99% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| VET-EUR | 805689 | -3.12% | INVALID_5M | 99/1 | 99/0 |
| S-EUR | 797348 | +14.16% | INVALID_5M | 99/2 | 99/0 |
| ZIL-EUR | 689354 | +0.30% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/11 | 99/2 |
| FIL-EUR | 686363 | -11.32% | INVALID_15M, INVALID_5M | 100/4 | 99/2 |
| KMNO-EUR | 684974 | +13.17% | INVALID_15M | 95/0 | 99/2 |
| XPL-EUR | 670727 | -3.30% | INVALID_5M | 100/2 | 99/0 |
| POL-EUR | 627567 | +2.28% | INVALID_5M | 99/1 | 99/0 |
| VVV-EUR | 622324 | +5.05% | INVALID_5M | 100/3 | 99/0 |
| TIA-EUR | 573665 | +1.69% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 99/1 |
| NPC-EUR | 563286 | +3.74% | INVALID_5M | 99/1 | 99/0 |
| GRASS-EUR | 552366 | +2.21% | INVALID_5M | 100/6 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
