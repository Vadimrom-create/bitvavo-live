# Audit qualité des données Bitvavo

Scan : 2026-09-20T00:49:51.597882+00:00 (20260920T004818Z-06fd3140)
Univers : 427 | strategy-grade : 21 | rejetés : 406
5m valides : 22 | 15m valides : 67 | deux intervalles valides : 21

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 405 |
| INVALID_15M | 360 |
| MISSING_LATEST_CLOSED_CANDLE | 283 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 405 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 360 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 9442133 | -0.94% | INVALID_5M | 99/2 | 99/0 |
| XLM-EUR | 2769702 | +0.70% | INVALID_5M | 100/1 | 100/0 |
| USDC-EUR | 2697416 | +0.03% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 2117563 | -2.83% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| CAP-EUR | 2009943 | -15.08% | INVALID_5M | 98/6 | 99/0 |
| PUMP-EUR | 1769679 | -0.05% | INVALID_5M | 100/5 | 100/0 |
| DOGE-EUR | 1625813 | -0.20% | INVALID_5M | 99/3 | 99/0 |
| HBAR-EUR | 1575306 | +3.71% | INVALID_5M | 100/2 | 100/0 |
| LTC-EUR | 1484906 | -1.32% | INVALID_5M | 100/5 | 100/0 |
| APT-EUR | 1466944 | -2.35% | INVALID_15M, INVALID_5M | 98/5 | 99/1 |
| CNPY-EUR | 1444624 | -24.52% | INVALID_5M | 99/2 | 99/0 |
| WLD-EUR | 1427393 | +1.46% | INVALID_5M | 98/2 | 99/0 |
| STRK-EUR | 1295420 | +6.28% | INVALID_5M | 98/1 | 99/0 |
| EPIC-EUR | 1222453 | +7.42% | INVALID_5M | 99/2 | 99/0 |
| USELESS-EUR | 1145113 | -14.58% | INVALID_5M | 98/1 | 99/0 |
| OP-EUR | 1089373 | +1.87% | INVALID_15M, INVALID_5M | 100/19 | 100/2 |
| ARB-EUR | 1087401 | -8.65% | INVALID_5M | 99/3 | 99/0 |
| SKY-EUR | 951670 | -2.89% | INVALID_15M, INVALID_5M | 93/16 | 99/3 |
| FIL-EUR | 918122 | +0.11% | INVALID_5M | 100/5 | 100/0 |
| HEI-EUR | 883717 | +13.07% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/19 | 100/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
