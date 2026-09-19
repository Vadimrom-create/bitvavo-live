# Audit qualité des données Bitvavo

Scan : 2026-09-19T00:36:49.425527+00:00 (20260919T003519Z-4352905b)
Univers : 427 | strategy-grade : 23 | rejetés : 404
5m valides : 23 | 15m valides : 68 | deux intervalles valides : 23

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 404 |
| INVALID_15M | 359 |
| MISSING_LATEST_CLOSED_CANDLE | 290 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 404 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 359 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 6245297 | +14.93% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 2792829 | +5.48% | INVALID_5M | 99/3 | 99/0 |
| USDC-EUR | 2733980 | -0.18% | INVALID_5M | 100/4 | 99/0 |
| LSK-EUR | 2680436 | -5.34% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 2558945 | +10.57% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 100/0 |
| XLM-EUR | 1993174 | +6.55% | INVALID_5M | 99/4 | 99/0 |
| INJ-EUR | 1898840 | +18.70% | INVALID_5M | 100/2 | 99/0 |
| CNPY-EUR | 1816265 | +1.74% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 100/0 |
| PEPE-EUR | 1802862 | +6.24% | INVALID_5M | 99/1 | 99/0 |
| COTI-EUR | 1604348 | -17.25% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/7 | 100/0 |
| RAY-EUR | 1549289 | +17.18% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1534573 | +8.05% | INVALID_5M | 99/2 | 99/0 |
| AVAX-EUR | 1441102 | +8.69% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1428074 | +23.19% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1365950 | +7.32% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 1330756 | +4.55% | INVALID_5M | 100/3 | 99/0 |
| HBAR-EUR | 1234496 | +6.36% | INVALID_5M | 99/2 | 99/0 |
| SKY-EUR | 1154610 | +18.92% | INVALID_15M, INVALID_5M | 99/5 | 99/1 |
| BCH-EUR | 1058867 | +9.04% | INVALID_5M | 100/1 | 99/0 |
| DRIFT-EUR | 1015836 | +4.91% | INVALID_5M | 99/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
