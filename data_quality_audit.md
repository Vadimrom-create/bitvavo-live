# Audit qualité des données Bitvavo

Scan : 2026-09-20T11:25:01.952036+00:00 (20260920T112329Z-ee9d85e0)
Univers : 426 | strategy-grade : 29 | rejetés : 397
5m valides : 29 | 15m valides : 74 | deux intervalles valides : 29

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 397 |
| INVALID_15M | 352 |
| MISSING_LATEST_CLOSED_CANDLE | 243 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 397 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 352 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 6949507 | -1.52% | INVALID_5M | 100/1 | 99/0 |
| INJ-EUR | 2668198 | +2.13% | INVALID_5M | 100/1 | 99/0 |
| XLM-EUR | 2519247 | -2.54% | INVALID_5M | 100/1 | 99/0 |
| CAP-EUR | 2085290 | -27.57% | INVALID_5M | 99/5 | 99/0 |
| UNI-EUR | 1559095 | -4.53% | INVALID_5M | 100/2 | 99/0 |
| DOGE-EUR | 1501531 | -3.90% | INVALID_5M | 100/1 | 99/0 |
| PUMP-EUR | 1445937 | -2.66% | INVALID_5M | 100/1 | 99/0 |
| WLD-EUR | 1434383 | -1.86% | INVALID_5M | 100/1 | 99/0 |
| LTC-EUR | 1277522 | -0.73% | INVALID_5M | 100/1 | 99/0 |
| LSK-EUR | 1242239 | -15.97% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1158520 | +1.56% | INVALID_15M, INVALID_5M | 100/2 | 99/3 |
| ARB-EUR | 1122859 | +0.45% | INVALID_5M | 100/2 | 99/0 |
| STRK-EUR | 1083563 | +0.93% | INVALID_5M | 99/1 | 99/0 |
| EPIC-EUR | 1008941 | +7.59% | INVALID_5M | 100/1 | 99/0 |
| STX-EUR | 995936 | +2.97% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 100/0 |
| FIL-EUR | 851730 | -3.51% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 90/16 | 100/2 |
| APT-EUR | 846305 | -2.98% | INVALID_5M | 100/8 | 99/0 |
| USELESS-EUR | 825450 | -3.19% | INVALID_5M | 100/4 | 99/0 |
| DOT-EUR | 815343 | -2.92% | INVALID_5M | 100/1 | 99/0 |
| BCH-EUR | 750896 | -2.07% | INVALID_15M, INVALID_5M | 80/17 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
