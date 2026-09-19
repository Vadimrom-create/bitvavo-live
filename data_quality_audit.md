# Audit qualité des données Bitvavo

Scan : 2026-09-19T00:11:48.705932+00:00 (20260919T001022Z-8ff8c939)
Univers : 427 | strategy-grade : 25 | rejetés : 402
5m valides : 25 | 15m valides : 70 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 402 |
| INVALID_15M | 357 |
| MISSING_LATEST_CLOSED_CANDLE | 303 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 402 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 357 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 6258430 | +12.11% | INVALID_5M | 100/3 | 99/0 |
| PUMP-EUR | 2779665 | +3.17% | INVALID_5M | 99/5 | 99/0 |
| USDC-EUR | 2727325 | -0.17% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| LSK-EUR | 2715772 | -1.28% | INVALID_5M | 99/1 | 99/0 |
| FET-EUR | 2604259 | +6.68% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 2527094 | +10.60% | INVALID_5M | 99/4 | 99/0 |
| XLM-EUR | 1990295 | +5.16% | INVALID_5M | 99/2 | 99/0 |
| INJ-EUR | 1865351 | +17.02% | INVALID_5M | 99/3 | 99/0 |
| COTI-EUR | 1665651 | -17.90% | INVALID_5M | 100/7 | 99/0 |
| RAY-EUR | 1551836 | +18.06% | INVALID_5M | 99/1 | 99/0 |
| AVAX-EUR | 1428787 | +7.81% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1328296 | +23.66% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1290411 | +8.60% | INVALID_5M | 99/2 | 99/0 |
| DOT-EUR | 1284343 | +4.60% | INVALID_5M | 100/4 | 99/0 |
| HBAR-EUR | 1189429 | +6.39% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1109663 | +18.10% | INVALID_15M, INVALID_5M | 99/9 | 99/1 |
| BCH-EUR | 1055597 | +8.63% | INVALID_5M | 100/1 | 99/0 |
| DRIFT-EUR | 1034475 | +3.67% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| XPL-EUR | 983843 | +7.11% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/8 | 99/0 |
| AAVE-EUR | 959700 | +8.74% | INVALID_5M | 100/6 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
