# Audit qualité des données Bitvavo

Scan : 2026-09-18T23:52:52.775773+00:00 (20260918T235119Z-c702d9be)
Univers : 427 | strategy-grade : 25 | rejetés : 402
5m valides : 25 | 15m valides : 74 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 402 |
| INVALID_15M | 353 |
| MISSING_LATEST_CLOSED_CANDLE | 314 |

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
| UNI-EUR | 6285387 | +13.41% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 2773186 | +4.49% | INVALID_5M | 99/4 | 99/0 |
| USDC-EUR | 2747739 | -0.18% | INVALID_5M | 99/2 | 99/0 |
| LSK-EUR | 2715561 | +0.48% | INVALID_5M | 99/1 | 99/0 |
| FET-EUR | 2691042 | +6.60% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 2555059 | +10.54% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |
| XLM-EUR | 1974738 | +5.01% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 1855351 | +16.45% | INVALID_5M | 99/5 | 99/0 |
| COTI-EUR | 1712493 | -16.28% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 100/0 |
| RAY-EUR | 1548649 | +18.56% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1481742 | +7.29% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1294880 | +22.46% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 1282119 | +4.91% | INVALID_5M | 99/3 | 99/0 |
| POL-EUR | 1266040 | +8.85% | INVALID_5M | 100/2 | 99/0 |
| HBAR-EUR | 1179982 | +6.03% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1087393 | +16.54% | INVALID_15M, INVALID_5M | 100/12 | 99/1 |
| DRIFT-EUR | 1050932 | +1.64% | INVALID_5M | 100/1 | 99/0 |
| XPL-EUR | 1004310 | +6.80% | INVALID_5M | 100/7 | 99/0 |
| AAVE-EUR | 949503 | +8.53% | INVALID_5M | 99/5 | 99/0 |
| LPT-EUR | 884783 | +15.90% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
