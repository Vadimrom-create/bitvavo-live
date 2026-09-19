# Audit qualité des données Bitvavo

Scan : 2026-09-19T02:34:37.130518+00:00 (20260919T023306Z-99ea24b8)
Univers : 427 | strategy-grade : 19 | rejetés : 408
5m valides : 19 | 15m valides : 63 | deux intervalles valides : 19

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 408 |
| INVALID_15M | 364 |
| MISSING_LATEST_CLOSED_CANDLE | 284 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 408 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 364 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 6109620 | +14.29% | INVALID_5M | 99/4 | 99/0 |
| TAO-EUR | 6061311 | +6.70% | INVALID_5M | 98/1 | 99/0 |
| ARB-EUR | 3397036 | +7.90% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 100/0 |
| G-EUR | 3291695 | +54.99% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 2766113 | +3.82% | INVALID_5M | 99/6 | 99/0 |
| USDC-EUR | 2703260 | -0.20% | INVALID_5M | 98/5 | 99/0 |
| WLD-EUR | 2618441 | +4.99% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/8 | 99/0 |
| FET-EUR | 2493867 | +2.49% | INVALID_5M | 99/2 | 99/0 |
| XLM-EUR | 2142749 | +5.14% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 1959669 | +19.41% | INVALID_5M | 98/5 | 99/0 |
| DOGE-EUR | 1940749 | +6.52% | INVALID_5M | 99/1 | 99/0 |
| PEPE-EUR | 1887972 | +3.15% | INVALID_5M | 98/1 | 99/0 |
| CNPY-EUR | 1816912 | -2.02% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/7 | 99/0 |
| AVAX-EUR | 1665182 | +11.18% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1536317 | +7.77% | INVALID_5M | 99/4 | 99/0 |
| RAY-EUR | 1497614 | +14.75% | INVALID_15M, INVALID_5M | 99/10 | 99/1 |
| POL-EUR | 1474526 | +9.16% | INVALID_5M | 98/2 | 99/0 |
| COTI-EUR | 1436973 | -11.41% | INVALID_15M, INVALID_5M | 99/14 | 100/1 |
| DOT-EUR | 1328401 | +2.53% | INVALID_5M | 99/3 | 99/0 |
| SKY-EUR | 1291194 | +17.94% | INVALID_5M | 98/4 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
