# Audit qualité des données Bitvavo

Scan : 2026-09-19T06:57:20.732234+00:00 (20260919T065553Z-99f989d4)
Univers : 427 | strategy-grade : 30 | rejetés : 397
5m valides : 34 | 15m valides : 66 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 393 |
| INVALID_15M | 361 |
| MISSING_LATEST_CLOSED_CANDLE | 262 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 393 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 361 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 5088982 | +6.55% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 2525281 | -1.51% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 2486486 | -4.22% | INVALID_5M | 99/1 | 99/0 |
| USDC-EUR | 2439865 | -0.20% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2154428 | +23.78% | INVALID_5M | 99/2 | 99/0 |
| AVAX-EUR | 1705383 | +7.13% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1658106 | +13.84% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1652239 | +3.60% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1624752 | +3.96% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1416259 | +14.99% | INVALID_5M | 99/6 | 99/0 |
| DOT-EUR | 1280655 | -2.54% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 1242993 | +3.76% | INVALID_15M, INVALID_5M | 99/3 | 99/1 |
| RAY-EUR | 1125495 | +5.47% | INVALID_15M, INVALID_5M | 99/8 | 99/1 |
| OP-EUR | 1087690 | +11.84% | INVALID_5M | 99/2 | 99/0 |
| BCH-EUR | 1011199 | +0.01% | INVALID_15M, INVALID_5M | 99/1 | 99/2 |
| COTI-EUR | 996950 | -12.06% | INVALID_15M, INVALID_5M | 99/5 | 99/2 |
| BNB-EUR | 971289 | +0.81% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 99/1 |
| LPT-EUR | 939731 | +9.23% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 99/0 |
| SAGA-EUR | 921395 | +15.93% | INVALID_5M | 99/7 | 99/0 |
| VET-EUR | 906260 | +14.65% | INVALID_5M | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
