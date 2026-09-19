# Audit qualité des données Bitvavo

Scan : 2026-09-19T11:17:27.360546+00:00 (20260919T111558Z-8bc14db5)
Univers : 427 | strategy-grade : 34 | rejetés : 393
5m valides : 36 | 15m valides : 79 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 348 |
| MISSING_LATEST_CLOSED_CANDLE | 253 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 348 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| WLD-EUR | 2185380 | -0.20% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2042002 | +33.72% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1624807 | +3.71% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |
| F-EUR | 1608730 | +28.46% | INVALID_5M | 99/4 | 99/0 |
| POL-EUR | 1578329 | +5.65% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 100/0 |
| SKY-EUR | 1446304 | +5.06% | INVALID_5M | 99/3 | 100/0 |
| AAVE-EUR | 1165275 | +6.94% | INVALID_5M | 99/1 | 100/0 |
| HBAR-EUR | 1147425 | +4.58% | INVALID_5M | 99/1 | 100/0 |
| DOT-EUR | 1126033 | -0.08% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1100165 | +15.99% | INVALID_5M | 99/4 | 99/0 |
| BCH-EUR | 1070521 | +1.50% | INVALID_5M | 100/12 | 100/0 |
| SAGA-EUR | 969161 | +34.53% | INVALID_5M | 99/2 | 99/0 |
| LPT-EUR | 855177 | +7.33% | INVALID_5M | 99/6 | 99/0 |
| MORPHO-EUR | 846755 | +16.22% | INVALID_5M | 99/2 | 99/0 |
| COTI-EUR | 841391 | +0.56% | INVALID_5M | 99/4 | 100/0 |
| S-EUR | 811643 | +7.50% | INVALID_15M, INVALID_5M | 100/22 | 100/3 |
| C-EUR | 810802 | +16.94% | INVALID_5M | 99/5 | 99/0 |
| SUPER-EUR | 800653 | +8.09% | INVALID_15M, INVALID_5M | 83/20 | 100/2 |
| BNB-EUR | 787984 | +1.89% | INVALID_15M, INVALID_5M | 99/1 | 100/1 |
| LAPTOP-EUR | 752569 | -17.64% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
