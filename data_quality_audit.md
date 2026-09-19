# Audit qualité des données Bitvavo

Scan : 2026-09-19T04:56:20.932294+00:00 (20260919T045449Z-15723900)
Univers : 427 | strategy-grade : 23 | rejetés : 404
5m valides : 28 | 15m valides : 56 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 399 |
| INVALID_15M | 371 |
| MISSING_LATEST_CLOSED_CANDLE | 284 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 399 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 371 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| USDC-EUR | 2636218 | -0.13% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| WLD-EUR | 2571502 | -0.88% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 2519629 | -2.92% | INVALID_5M | 100/5 | 99/0 |
| FET-EUR | 2421448 | -1.69% | INVALID_5M | 99/2 | 99/0 |
| XLM-EUR | 2116978 | +2.84% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2036456 | +14.78% | MISSING_LATEST_CLOSED_CANDLE | 100/0 | 99/0 |
| DOGE-EUR | 1881912 | +3.50% | INVALID_5M | 99/2 | 99/0 |
| PEPE-EUR | 1877679 | +2.49% | INVALID_5M | 99/1 | 99/0 |
| CNPY-EUR | 1721282 | +13.01% | INVALID_5M | 99/4 | 99/0 |
| LTC-EUR | 1609807 | +5.65% | INVALID_5M | 99/2 | 99/0 |
| POL-EUR | 1535329 | +5.23% | INVALID_5M | 100/7 | 99/0 |
| F-EUR | 1522580 | +33.83% | INVALID_5M | 99/2 | 82/0 |
| ENA-EUR | 1518303 | +6.48% | INVALID_5M | 99/2 | 99/0 |
| DOT-EUR | 1352933 | -1.16% | INVALID_5M | 100/2 | 99/0 |
| RAY-EUR | 1343339 | +5.31% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 100/1 |
| SKY-EUR | 1309672 | +14.73% | INVALID_5M | 99/10 | 99/0 |
| COTI-EUR | 1260324 | -9.10% | INVALID_15M, INVALID_5M | 100/15 | 99/2 |
| HBAR-EUR | 1258498 | +2.36% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/15 | 100/1 |
| AAVE-EUR | 1121614 | +5.93% | INVALID_5M | 100/1 | 99/0 |
| BNB-EUR | 1034202 | +1.01% | INVALID_15M, INVALID_5M | 99/3 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
