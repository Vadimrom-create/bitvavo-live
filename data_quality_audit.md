# Audit qualité des données Bitvavo

Scan : 2026-09-19T06:42:43.217668+00:00 (20260919T064116Z-da85b0f8)
Univers : 427 | strategy-grade : 30 | rejetés : 397
5m valides : 33 | 15m valides : 65 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 394 |
| INVALID_15M | 362 |
| MISSING_LATEST_CLOSED_CANDLE | 252 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 394 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 362 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 5181635 | +7.20% | INVALID_5M | 99/1 | 99/0 |
| USDC-EUR | 2510172 | -0.22% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 2508072 | +0.25% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 2487336 | -4.43% | INVALID_5M | 99/2 | 99/0 |
| INJ-EUR | 2142752 | +22.25% | INVALID_5M | 99/2 | 99/0 |
| AVAX-EUR | 1675687 | +8.24% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1671367 | +12.56% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1647195 | +3.04% | INVALID_5M | 100/3 | 99/0 |
| LTC-EUR | 1631713 | +4.08% | INVALID_5M | 99/1 | 99/0 |
| F-EUR | 1557173 | +27.48% | INVALID_5M | 99/1 | 89/0 |
| SKY-EUR | 1423198 | +14.61% | INVALID_5M | 99/5 | 99/0 |
| DOT-EUR | 1303759 | -2.57% | INVALID_5M | 100/1 | 99/0 |
| HBAR-EUR | 1248631 | +3.56% | INVALID_15M, INVALID_5M | 99/5 | 99/1 |
| RAY-EUR | 1140643 | +4.17% | INVALID_15M, INVALID_5M | 99/8 | 99/1 |
| OP-EUR | 1076531 | +12.68% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |
| COTI-EUR | 1048961 | -16.73% | INVALID_15M, INVALID_5M | 99/8 | 99/2 |
| BCH-EUR | 987270 | -0.16% | INVALID_15M, INVALID_5M | 99/1 | 99/2 |
| BNB-EUR | 970086 | +1.02% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 100/1 |
| LPT-EUR | 948086 | +10.38% | INVALID_5M | 99/1 | 99/0 |
| SAGA-EUR | 915189 | +15.78% | INVALID_5M | 99/8 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
