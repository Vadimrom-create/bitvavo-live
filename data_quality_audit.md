# Audit qualité des données Bitvavo

Scan : 2026-09-19T03:52:49.639918+00:00 (20260919T035049Z-58b4652a)
Univers : 427 | strategy-grade : 20 | rejetés : 407
5m valides : 22 | 15m valides : 59 | deux intervalles valides : 21

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 405 |
| INVALID_15M | 368 |
| MISSING_LATEST_CLOSED_CANDLE | 320 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 405 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 368 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ARB-EUR | 3105395 | -5.99% | INVALID_5M | 99/3 | 99/0 |
| USDC-EUR | 2688069 | -0.09% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 2586753 | +3.90% | INVALID_5M | 99/8 | 99/0 |
| WLD-EUR | 2496248 | +2.71% | INVALID_5M | 99/8 | 99/0 |
| FET-EUR | 2409601 | -0.87% | INVALID_5M | 99/4 | 99/0 |
| XLM-EUR | 2119305 | +2.54% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 100/0 |
| INJ-EUR | 1998702 | +16.93% | INVALID_5M | 99/3 | 99/0 |
| DOGE-EUR | 1931453 | +4.21% | INVALID_5M | 99/3 | 99/0 |
| PEPE-EUR | 1810674 | +2.34% | INVALID_5M | 99/1 | 99/0 |
| CNPY-EUR | 1745972 | +12.41% | INVALID_5M | 99/10 | 99/0 |
| LTC-EUR | 1542140 | +6.82% | INVALID_5M | 99/3 | 99/0 |
| F-EUR | 1503913 | +33.34% | INVALID_5M | 100/1 | 99/0 |
| POL-EUR | 1497695 | +6.78% | INVALID_5M | 99/6 | 99/0 |
| RAY-EUR | 1402562 | +4.93% | INVALID_15M, INVALID_5M | 100/13 | 99/1 |
| COTI-EUR | 1372439 | -14.24% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/16 | 99/1 |
| DOT-EUR | 1357543 | +1.26% | INVALID_5M | 99/3 | 99/0 |
| ENA-EUR | 1339013 | +12.19% | INVALID_5M | 99/2 | 99/0 |
| SKY-EUR | 1285653 | +12.93% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/7 | 100/0 |
| HBAR-EUR | 1261272 | +2.82% | INVALID_15M, INVALID_5M | 99/10 | 99/1 |
| AAVE-EUR | 1158551 | +6.49% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
