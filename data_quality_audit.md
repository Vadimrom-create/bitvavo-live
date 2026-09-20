# Audit qualité des données Bitvavo

Scan : 2026-09-20T01:50:35.378097+00:00 (20260920T014902Z-4be9833f)
Univers : 427 | strategy-grade : 25 | rejetés : 402
5m valides : 26 | 15m valides : 65 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 401 |
| INVALID_15M | 362 |
| MISSING_LATEST_CLOSED_CANDLE | 267 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 401 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 362 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 9136580 | -1.96% | INVALID_5M | 99/2 | 99/0 |
| XLM-EUR | 2689186 | +0.28% | INVALID_5M | 99/1 | 100/0 |
| SYN-EUR | 2314417 | +6.31% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 2060894 | -2.07% | INVALID_5M | 99/6 | 99/0 |
| PUMP-EUR | 1818413 | -2.05% | INVALID_5M | 100/4 | 99/0 |
| HBAR-EUR | 1756812 | +3.71% | INVALID_5M | 99/3 | 99/0 |
| DOGE-EUR | 1592620 | -1.01% | INVALID_5M | 100/3 | 99/0 |
| CNPY-EUR | 1432122 | -23.44% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1426891 | -0.29% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1413608 | -1.24% | INVALID_5M | 99/7 | 99/0 |
| APT-EUR | 1374665 | -1.58% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 100/1 |
| EPIC-EUR | 1213611 | +11.42% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/9 | 99/0 |
| STRK-EUR | 1211146 | +6.56% | INVALID_5M | 100/1 | 99/0 |
| USELESS-EUR | 1096293 | -13.81% | INVALID_5M | 99/3 | 99/0 |
| ARB-EUR | 1063541 | -5.38% | INVALID_5M | 99/2 | 99/0 |
| OP-EUR | 1043308 | +1.19% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/25 | 100/3 |
| FIL-EUR | 916040 | -1.69% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/11 | 100/1 |
| HEI-EUR | 885355 | +12.36% | INVALID_15M, INVALID_5M | 100/22 | 99/1 |
| SKY-EUR | 879168 | -3.56% | INVALID_15M, INVALID_5M | 92/19 | 100/2 |
| STX-EUR | 877398 | +14.41% | INVALID_5M | 99/4 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
