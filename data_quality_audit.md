# Audit qualité des données Bitvavo

Scan : 2026-09-19T02:18:19.159983+00:00 (20260919T021647Z-854277c5)
Univers : 427 | strategy-grade : 19 | rejetés : 408
5m valides : 22 | 15m valides : 64 | deux intervalles valides : 22

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 405 |
| INVALID_15M | 363 |
| MISSING_LATEST_CLOSED_CANDLE | 286 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 405 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 363 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 6121306 | +15.57% | INVALID_5M | 99/4 | 99/0 |
| TAO-EUR | 6077355 | +6.42% | INVALID_5M | 100/1 | 100/0 |
| ARB-EUR | 3420893 | +9.94% | INVALID_5M | 99/1 | 99/0 |
| G-EUR | 3254461 | +52.44% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 2768577 | +4.55% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 100/0 |
| USDC-EUR | 2707303 | -0.17% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 99/0 |
| WLD-EUR | 2655827 | +6.82% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/7 | 99/0 |
| FET-EUR | 2495199 | +2.78% | MISSING_LATEST_CLOSED_CANDLE | 100/0 | 100/0 |
| XLM-EUR | 2136690 | +5.02% | INVALID_5M | 99/2 | 99/0 |
| INJ-EUR | 1936720 | +17.83% | INVALID_5M | 99/5 | 99/0 |
| DOGE-EUR | 1934628 | +7.01% | INVALID_5M | 99/1 | 100/0 |
| PEPE-EUR | 1875361 | +3.35% | INVALID_5M | 99/1 | 100/0 |
| CNPY-EUR | 1821198 | -1.12% | INVALID_5M | 99/7 | 99/0 |
| AVAX-EUR | 1643632 | +11.56% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1560287 | +7.99% | INVALID_5M | 99/4 | 99/0 |
| RAY-EUR | 1501665 | +15.27% | INVALID_15M, INVALID_5M | 99/10 | 99/1 |
| POL-EUR | 1438208 | +7.25% | INVALID_5M | 99/2 | 99/0 |
| COTI-EUR | 1437621 | -12.38% | INVALID_15M, INVALID_5M | 99/14 | 99/1 |
| DOT-EUR | 1328693 | +2.08% | INVALID_5M | 99/4 | 99/0 |
| HBAR-EUR | 1293491 | +4.96% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
