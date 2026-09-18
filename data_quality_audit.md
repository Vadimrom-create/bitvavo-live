# Audit qualité des données Bitvavo

Scan : 2026-09-18T23:47:21.737148+00:00 (20260918T234552Z-d6f75ac3)
Univers : 427 | strategy-grade : 25 | rejetés : 402
5m valides : 25 | 15m valides : 74 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 402 |
| INVALID_15M | 353 |
| MISSING_LATEST_CLOSED_CANDLE | 298 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 402 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 353 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 6297767 | +13.81% | INVALID_5M | 99/3 | 100/0 |
| PUMP-EUR | 2777844 | +5.06% | INVALID_5M | 99/4 | 99/0 |
| USDC-EUR | 2748076 | -0.17% | INVALID_5M | 99/2 | 100/0 |
| LSK-EUR | 2713660 | -0.21% | INVALID_5M | 99/1 | 99/0 |
| FET-EUR | 2685509 | +6.76% | INVALID_5M | 99/1 | 100/0 |
| WLD-EUR | 2556752 | +10.53% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 100/0 |
| XLM-EUR | 1960762 | +4.62% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |
| INJ-EUR | 1854812 | +15.88% | INVALID_5M | 99/5 | 100/0 |
| COTI-EUR | 1716199 | -15.36% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 100/0 |
| RAY-EUR | 1550360 | +19.75% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1478672 | +6.77% | INVALID_5M | 99/2 | 100/0 |
| APT-EUR | 1294011 | +21.88% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 1278655 | +4.52% | INVALID_5M | 99/3 | 99/0 |
| POL-EUR | 1265991 | +8.53% | INVALID_5M | 100/2 | 100/0 |
| HBAR-EUR | 1183116 | +6.15% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1087285 | +16.38% | INVALID_15M, INVALID_5M | 99/13 | 100/1 |
| DRIFT-EUR | 1062424 | +0.34% | INVALID_5M | 99/1 | 100/0 |
| XPL-EUR | 1004310 | +6.80% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 99/0 |
| AAVE-EUR | 948417 | +8.29% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 99/0 |
| LPT-EUR | 884803 | +15.90% | INVALID_5M | 100/3 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
