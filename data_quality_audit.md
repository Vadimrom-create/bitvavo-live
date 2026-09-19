# Audit qualité des données Bitvavo

Scan : 2026-09-19T02:49:07.323695+00:00 (20260919T024735Z-f1c91571)
Univers : 427 | strategy-grade : 20 | rejetés : 407
5m valides : 21 | 15m valides : 60 | deux intervalles valides : 20

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 406 |
| INVALID_15M | 367 |
| MISSING_LATEST_CLOSED_CANDLE | 289 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 406 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 367 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| TAO-EUR | 6102958 | +7.85% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 6084212 | +12.87% | INVALID_5M | 99/4 | 99/0 |
| ARB-EUR | 3337076 | +6.87% | INVALID_5M | 99/3 | 99/0 |
| G-EUR | 3332495 | +54.47% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 2767569 | +4.05% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 99/0 |
| USDC-EUR | 2707168 | -0.18% | INVALID_5M | 99/3 | 99/0 |
| WLD-EUR | 2591759 | +6.31% | INVALID_5M | 99/7 | 99/0 |
| FET-EUR | 2484942 | +2.17% | INVALID_5M | 100/2 | 100/0 |
| INJ-EUR | 1964478 | +19.64% | INVALID_5M | 99/5 | 99/0 |
| DOGE-EUR | 1940737 | +6.55% | INVALID_5M | 99/1 | 99/0 |
| CNPY-EUR | 1801473 | +4.69% | INVALID_5M | 99/9 | 100/0 |
| AVAX-EUR | 1686138 | +10.73% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1537060 | +7.55% | INVALID_5M | 99/2 | 99/0 |
| F-EUR | 1498612 | +34.55% | INVALID_5M | 99/1 | 99/0 |
| RAY-EUR | 1495304 | +14.68% | INVALID_15M, INVALID_5M | 100/10 | 100/1 |
| POL-EUR | 1480911 | +8.01% | INVALID_5M | 99/2 | 99/0 |
| COTI-EUR | 1439027 | -11.80% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/14 | 99/1 |
| DOT-EUR | 1324720 | +2.77% | INVALID_5M | 100/3 | 100/0 |
| SKY-EUR | 1298884 | +17.23% | INVALID_5M | 99/4 | 99/0 |
| HBAR-EUR | 1272163 | +3.95% | INVALID_15M, INVALID_5M | 99/5 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
