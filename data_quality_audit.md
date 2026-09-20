# Audit qualité des données Bitvavo

Scan : 2026-09-20T10:39:15.825733+00:00 (20260920T103747Z-d668c993)
Univers : 426 | strategy-grade : 32 | rejetés : 394
5m valides : 34 | 15m valides : 69 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 357 |
| MISSING_LATEST_CLOSED_CANDLE | 262 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 357 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 7242484 | -0.96% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2541523 | -1.86% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| CAP-EUR | 2033960 | -24.34% | INVALID_5M | 99/7 | 99/0 |
| UNI-EUR | 1621074 | -4.75% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1518147 | -3.68% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1438709 | -3.06% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1361609 | -0.79% | INVALID_5M | 99/1 | 99/0 |
| LSK-EUR | 1241146 | -16.48% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1146096 | +1.61% | INVALID_15M, INVALID_5M | 96/1 | 99/3 |
| ARB-EUR | 1140734 | -0.85% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 1076294 | +4.62% | INVALID_5M | 99/1 | 99/0 |
| EPIC-EUR | 1037746 | +6.22% | INVALID_5M | 99/2 | 99/0 |
| STX-EUR | 1016452 | +6.32% | INVALID_5M | 100/2 | 99/0 |
| APT-EUR | 866919 | -1.73% | INVALID_15M, INVALID_5M | 100/5 | 99/1 |
| USELESS-EUR | 863444 | -2.82% | INVALID_5M | 99/3 | 99/0 |
| FIL-EUR | 855556 | -3.08% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 98/11 | 100/2 |
| KAS-EUR | 815831 | +1.53% | INVALID_15M, INVALID_5M | 98/1 | 99/1 |
| DOT-EUR | 806058 | -2.90% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 750397 | -1.87% | INVALID_15M, INVALID_5M | 82/18 | 99/1 |
| SHIB-EUR | 736265 | -1.84% | INVALID_5M | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
