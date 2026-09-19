# Audit qualité des données Bitvavo

Scan : 2026-09-19T06:23:13.706786+00:00 (20260919T062141Z-8a76a7a0)
Univers : 427 | strategy-grade : 30 | rejetés : 397
5m valides : 31 | 15m valides : 66 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 396 |
| INVALID_15M | 361 |
| MISSING_LATEST_CLOSED_CANDLE | 266 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 396 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 361 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 5118456 | +6.86% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 2535216 | -5.34% | INVALID_5M | 99/2 | 99/0 |
| WLD-EUR | 2528721 | +0.45% | INVALID_5M | 99/2 | 99/0 |
| USDC-EUR | 2453609 | -0.22% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2064097 | +18.57% | INVALID_5M | 99/2 | 99/0 |
| AVAX-EUR | 1676042 | +6.64% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1673518 | +12.14% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1664332 | +4.08% | INVALID_5M | 99/2 | 99/0 |
| POL-EUR | 1611403 | +3.47% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 99/0 |
| F-EUR | 1551375 | +26.39% | INVALID_5M | 99/1 | 88/0 |
| SKY-EUR | 1409588 | +16.16% | INVALID_5M | 99/7 | 99/0 |
| DOT-EUR | 1298620 | -1.00% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 1243540 | +2.97% | INVALID_15M, INVALID_5M | 99/12 | 99/1 |
| RAY-EUR | 1198266 | +4.66% | INVALID_15M, INVALID_5M | 99/8 | 99/1 |
| COTI-EUR | 1065397 | -14.55% | INVALID_15M, INVALID_5M | 99/11 | 99/2 |
| BCH-EUR | 982752 | -0.14% | INVALID_15M, INVALID_5M | 100/2 | 99/2 |
| BNB-EUR | 971707 | +1.13% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| LPT-EUR | 965423 | +8.70% | INVALID_5M | 100/3 | 99/0 |
| SAGA-EUR | 911704 | +14.53% | INVALID_5M | 99/8 | 99/0 |
| VET-EUR | 878116 | +8.65% | INVALID_5M | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
