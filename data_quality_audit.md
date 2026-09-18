# Audit qualité des données Bitvavo

Scan : 2026-09-18T23:23:39.432741+00:00 (20260918T232210Z-9b918f58)
Univers : 427 | strategy-grade : 25 | rejetés : 402
5m valides : 27 | 15m valides : 78 | deux intervalles valides : 26

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 400 |
| INVALID_15M | 349 |
| MISSING_LATEST_CLOSED_CANDLE | 307 |
| STALE_DAILY_PROFILE | 1 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 400 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 349 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 21073483 | +9.23% | STALE_DAILY_PROFILE | 99/0 | 99/0 |
| UNI-EUR | 6319285 | +14.69% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 2812888 | +4.59% | INVALID_5M | 99/3 | 99/0 |
| USDC-EUR | 2743597 | -0.14% | INVALID_5M | 99/1 | 99/0 |
| LSK-EUR | 2706745 | +0.01% | INVALID_5M | 99/1 | 99/0 |
| FET-EUR | 2700616 | +7.02% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 2559344 | +11.19% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 1963776 | +4.52% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 1856211 | +14.99% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 100/0 |
| COTI-EUR | 1757219 | -14.90% | INVALID_5M | 99/3 | 99/0 |
| RAY-EUR | 1548737 | +21.29% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1481486 | +6.90% | INVALID_5M | 99/2 | 99/0 |
| DOT-EUR | 1290576 | +3.87% | INVALID_5M | 100/2 | 99/0 |
| POL-EUR | 1256941 | +8.32% | INVALID_5M | 100/2 | 99/0 |
| HBAR-EUR | 1182125 | +6.44% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1093598 | +17.02% | INVALID_15M, INVALID_5M | 100/13 | 99/1 |
| DRIFT-EUR | 1086488 | +3.95% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 1051840 | +8.38% | INVALID_5M | 99/1 | 99/0 |
| XPL-EUR | 995455 | +7.69% | INVALID_5M | 99/7 | 99/0 |
| AAVE-EUR | 947671 | +7.79% | INVALID_5M | 99/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
