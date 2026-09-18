# Audit qualité des données Bitvavo

Scan : 2026-09-18T23:12:07.833319+00:00 (20260918T231039Z-3c65b8b7)
Univers : 427 | strategy-grade : 26 | rejetés : 401
5m valides : 28 | 15m valides : 82 | deux intervalles valides : 27

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 399 |
| INVALID_15M | 345 |
| MISSING_LATEST_CLOSED_CANDLE | 298 |
| STALE_DAILY_PROFILE | 3 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 399 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 345 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 21209023 | +9.39% | STALE_DAILY_PROFILE | 99/0 | 99/0 |
| UNI-EUR | 6339725 | +14.32% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 99/0 |
| PUMP-EUR | 2943770 | +5.63% | INVALID_5M | 99/4 | 99/0 |
| USDC-EUR | 2730323 | -0.17% | INVALID_5M | 100/1 | 99/0 |
| FET-EUR | 2720163 | +7.59% | INVALID_5M, STALE_DAILY_PROFILE | 99/1 | 99/0 |
| LSK-EUR | 2709260 | +0.48% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 1959962 | +4.51% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 1853925 | +14.65% | INVALID_5M | 99/5 | 99/0 |
| COTI-EUR | 1781766 | -14.29% | INVALID_5M | 99/3 | 99/0 |
| RAY-EUR | 1481046 | +18.82% | INVALID_5M | 100/1 | 99/0 |
| LTC-EUR | 1474456 | +6.94% | INVALID_5M, STALE_DAILY_PROFILE | 99/2 | 99/0 |
| DOT-EUR | 1290981 | +4.55% | INVALID_5M | 100/1 | 99/0 |
| POL-EUR | 1251768 | +7.79% | INVALID_5M | 99/2 | 99/0 |
| HBAR-EUR | 1178751 | +6.26% | INVALID_5M | 99/1 | 99/0 |
| DRIFT-EUR | 1105039 | +5.49% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1092742 | +16.84% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/14 | 99/1 |
| XPL-EUR | 994270 | +7.08% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 99/0 |
| BCH-EUR | 977033 | +11.74% | INVALID_5M | 100/1 | 99/0 |
| AAVE-EUR | 948870 | +7.48% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 99/0 |
| LPT-EUR | 883680 | +14.29% | INVALID_5M | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
