# Audit qualité des données Bitvavo

Scan : 2026-09-20T01:36:10.763556+00:00 (20260920T013437Z-2a3c4ea7)
Univers : 427 | strategy-grade : 22 | rejetés : 405
5m valides : 25 | 15m valides : 66 | deux intervalles valides : 23

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 402 |
| INVALID_15M | 361 |
| MISSING_LATEST_CLOSED_CANDLE | 307 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 402 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 361 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 9183518 | -0.89% | INVALID_5M | 99/2 | 99/0 |
| USDC-EUR | 2706350 | +0.06% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2698519 | +0.93% | INVALID_5M | 99/1 | 99/0 |
| SYN-EUR | 2314086 | +3.21% | MISSING_LATEST_CLOSED_CANDLE | 100/0 | 100/0 |
| UNI-EUR | 2066192 | -1.03% | INVALID_5M | 100/6 | 99/0 |
| PUMP-EUR | 1792168 | -1.52% | INVALID_5M | 99/5 | 99/0 |
| HBAR-EUR | 1728657 | +5.07% | INVALID_5M | 99/3 | 99/0 |
| DOGE-EUR | 1600455 | -0.53% | INVALID_5M | 99/3 | 99/0 |
| WLD-EUR | 1456626 | +0.33% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1427299 | -20.28% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1415395 | -0.24% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 100/0 |
| APT-EUR | 1402267 | -2.31% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/1 |
| STRK-EUR | 1225814 | +8.42% | INVALID_5M | 99/1 | 99/0 |
| EPIC-EUR | 1214005 | +12.30% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| USELESS-EUR | 1096230 | -13.95% | INVALID_5M | 99/3 | 99/0 |
| ARB-EUR | 1054916 | -5.70% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 100/0 |
| OP-EUR | 1053910 | +2.89% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/22 | 100/3 |
| FIL-EUR | 916869 | -1.44% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/11 | 99/0 |
| SKY-EUR | 911146 | -2.69% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 94/16 | 100/2 |
| HEI-EUR | 885485 | +13.41% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/20 | 100/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
