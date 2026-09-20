# Audit qualité des données Bitvavo

Scan : 2026-09-20T11:41:01.944115+00:00 (20260920T113858Z-0f4a2aec)
Univers : 426 | strategy-grade : 26 | rejetés : 400
5m valides : 27 | 15m valides : 74 | deux intervalles valides : 27

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 399 |
| INVALID_15M | 352 |
| MISSING_LATEST_CLOSED_CANDLE | 294 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 399 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 352 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 6935940 | -1.42% | INVALID_5M | 99/1 | 99/0 |
| USDC-EUR | 3268933 | +0.05% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2658263 | +1.84% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2495357 | -2.17% | INVALID_5M | 100/1 | 99/0 |
| CAP-EUR | 2089948 | -27.71% | INVALID_5M | 100/5 | 99/0 |
| UNI-EUR | 1602005 | -3.62% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 99/0 |
| CNPY-EUR | 1516055 | -25.57% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1500348 | -3.69% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 1434447 | -2.54% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 99/0 |
| WLD-EUR | 1433248 | -1.67% | INVALID_5M | 100/1 | 99/0 |
| LTC-EUR | 1272815 | -1.26% | INVALID_5M | 100/2 | 99/0 |
| CAKE-EUR | 1248980 | +1.87% | INVALID_15M, INVALID_5M | 100/2 | 99/2 |
| LSK-EUR | 1228217 | -14.95% | INVALID_5M | 100/1 | 99/0 |
| ARB-EUR | 1120093 | +1.12% | INVALID_5M | 100/2 | 99/0 |
| STRK-EUR | 1101806 | +0.83% | INVALID_5M | 99/1 | 99/0 |
| EPIC-EUR | 1009155 | +7.82% | INVALID_5M | 100/1 | 99/0 |
| STX-EUR | 993745 | +2.88% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 100/0 |
| APT-EUR | 856011 | -2.07% | INVALID_5M | 100/8 | 99/0 |
| FIL-EUR | 852475 | -3.58% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 88/19 | 99/2 |
| DOT-EUR | 818618 | -3.14% | INVALID_5M | 100/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
