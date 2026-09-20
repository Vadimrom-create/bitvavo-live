# Audit qualité des données Bitvavo

Scan : 2026-09-20T12:34:46.411367+00:00 (20260920T123312Z-725c6ac8)
Univers : 426 | strategy-grade : 27 | rejetés : 399
5m valides : 29 | 15m valides : 76 | deux intervalles valides : 27

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 397 |
| INVALID_15M | 350 |
| MISSING_LATEST_CLOSED_CANDLE | 257 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 397 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 350 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 6979389 | -2.00% | INVALID_5M | 98/1 | 99/0 |
| USDC-EUR | 2818704 | +0.01% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2668619 | -0.58% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2474548 | -3.13% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 1986283 | -35.83% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 1619749 | -5.69% | INVALID_5M | 99/3 | 99/0 |
| CNPY-EUR | 1497695 | -18.22% | INVALID_5M | 98/1 | 99/0 |
| DOGE-EUR | 1446242 | -3.82% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1425937 | -3.82% | INVALID_5M | 99/3 | 99/0 |
| WLD-EUR | 1418343 | -2.91% | INVALID_5M | 100/5 | 100/0 |
| LSK-EUR | 1226308 | -14.80% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1215884 | +1.66% | INVALID_5M | 99/6 | 99/0 |
| LTC-EUR | 1151649 | -1.65% | INVALID_5M | 98/4 | 100/0 |
| ARB-EUR | 1110591 | +1.07% | INVALID_5M | 99/2 | 99/0 |
| STX-EUR | 904365 | -1.05% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/10 | 99/2 |
| FIL-EUR | 858817 | -5.48% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 85/23 | 99/2 |
| DOT-EUR | 848960 | -3.59% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 810394 | -1.19% | INVALID_5M | 99/5 | 99/0 |
| BCH-EUR | 771656 | -2.14% | INVALID_15M, INVALID_5M | 86/16 | 99/1 |
| USELESS-EUR | 765898 | -4.79% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
