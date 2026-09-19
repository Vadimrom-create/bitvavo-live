# Audit qualité des données Bitvavo

Scan : 2026-09-19T01:57:35.477341+00:00 (20260919T015606Z-5eaceada)
Univers : 427 | strategy-grade : 23 | rejetés : 404
5m valides : 24 | 15m valides : 67 | deux intervalles valides : 23

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 403 |
| INVALID_15M | 360 |
| MISSING_LATEST_CLOSED_CANDLE | 309 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 403 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 360 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 6223952 | +14.09% | INVALID_5M | 99/4 | 99/0 |
| TAO-EUR | 6110358 | +6.15% | INVALID_5M | 99/1 | 99/0 |
| ARB-EUR | 3520101 | +10.24% | INVALID_5M | 99/1 | 99/0 |
| G-EUR | 3199732 | +45.67% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 2768818 | +4.53% | INVALID_5M | 99/4 | 99/0 |
| USDC-EUR | 2706442 | -0.17% | INVALID_5M | 99/5 | 99/0 |
| WLD-EUR | 2666267 | +8.19% | INVALID_5M | 99/6 | 99/0 |
| XLM-EUR | 2134379 | +4.70% | INVALID_5M | 99/4 | 99/0 |
| INJ-EUR | 1936399 | +17.38% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| PEPE-EUR | 1878881 | +2.66% | INVALID_5M | 100/1 | 99/0 |
| CNPY-EUR | 1824535 | -0.88% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 99/0 |
| AVAX-EUR | 1597115 | +12.76% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1562926 | +7.23% | INVALID_5M | 99/4 | 99/0 |
| RAY-EUR | 1514077 | +14.96% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/7 | 100/0 |
| COTI-EUR | 1439577 | -12.38% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/10 | 100/0 |
| POL-EUR | 1379315 | +6.11% | INVALID_5M | 100/1 | 99/0 |
| DOT-EUR | 1331659 | +2.42% | INVALID_5M | 99/3 | 99/0 |
| HBAR-EUR | 1285678 | +5.21% | INVALID_5M | 100/1 | 99/0 |
| SKY-EUR | 1261062 | +20.35% | INVALID_5M | 99/4 | 99/0 |
| AAVE-EUR | 1129706 | +8.22% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
