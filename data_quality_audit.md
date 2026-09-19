# Audit qualité des données Bitvavo

Scan : 2026-09-19T04:08:30.789693+00:00 (20260919T040657Z-c71eb638)
Univers : 427 | strategy-grade : 20 | rejetés : 407
5m valides : 21 | 15m valides : 59 | deux intervalles valides : 20

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 406 |
| INVALID_15M | 368 |
| MISSING_LATEST_CLOSED_CANDLE | 302 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 406 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 368 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ARB-EUR | 3033243 | -5.00% | INVALID_5M | 99/2 | 99/0 |
| USDC-EUR | 2675691 | -0.09% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 2581460 | +4.15% | INVALID_5M | 99/8 | 99/0 |
| WLD-EUR | 2469476 | +2.34% | INVALID_5M | 99/8 | 99/0 |
| FET-EUR | 2408147 | -0.18% | INVALID_5M | 99/4 | 99/0 |
| XLM-EUR | 2089085 | +3.84% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2032476 | +17.24% | INVALID_5M | 99/3 | 99/0 |
| DOGE-EUR | 1906484 | +4.59% | INVALID_5M | 99/3 | 99/0 |
| PEPE-EUR | 1809519 | +3.09% | INVALID_5M | 99/1 | 99/0 |
| CNPY-EUR | 1748928 | +14.20% | INVALID_5M | 99/10 | 99/0 |
| LTC-EUR | 1565967 | +8.32% | INVALID_5M | 99/1 | 99/0 |
| F-EUR | 1508137 | +35.39% | INVALID_5M | 99/2 | 79/0 |
| POL-EUR | 1490941 | +5.76% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 100/0 |
| ENA-EUR | 1428578 | +12.09% | INVALID_5M | 99/2 | 99/0 |
| RAY-EUR | 1375804 | +4.77% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/12 | 100/1 |
| COTI-EUR | 1358776 | -15.29% | INVALID_15M, INVALID_5M | 100/13 | 99/2 |
| DOT-EUR | 1351668 | +1.49% | INVALID_5M | 99/3 | 99/0 |
| SKY-EUR | 1276163 | +13.32% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/8 | 99/0 |
| HBAR-EUR | 1253905 | +2.94% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/10 | 100/1 |
| AAVE-EUR | 1121622 | +6.81% | INVALID_5M | 99/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
