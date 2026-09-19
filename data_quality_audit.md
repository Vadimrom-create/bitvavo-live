# Audit qualité des données Bitvavo

Scan : 2026-09-19T01:26:58.581501+00:00 (20260919T012529Z-b0442d54)
Univers : 427 | strategy-grade : 23 | rejetés : 404
5m valides : 24 | 15m valides : 66 | deux intervalles valides : 23

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 403 |
| INVALID_15M | 361 |
| MISSING_LATEST_CLOSED_CANDLE | 260 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 403 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 361 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 6243323 | +13.23% | INVALID_5M | 100/5 | 99/0 |
| TAO-EUR | 6147455 | +6.98% | INVALID_5M | 99/1 | 99/0 |
| G-EUR | 3194842 | +47.48% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 2796586 | +4.80% | INVALID_5M | 99/3 | 99/0 |
| USDC-EUR | 2705523 | -0.18% | INVALID_5M | 99/4 | 99/0 |
| WLD-EUR | 2588910 | +8.69% | INVALID_5M | 100/5 | 99/0 |
| XLM-EUR | 2122422 | +4.63% | INVALID_5M | 99/4 | 99/0 |
| INJ-EUR | 1908031 | +17.01% | INVALID_5M | 100/3 | 99/0 |
| PEPE-EUR | 1858131 | +2.97% | INVALID_5M | 99/1 | 99/0 |
| CNPY-EUR | 1831120 | -1.18% | INVALID_5M | 99/3 | 99/0 |
| LTC-EUR | 1541846 | +6.50% | INVALID_5M | 99/2 | 99/0 |
| RAY-EUR | 1534398 | +16.30% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 99/0 |
| APT-EUR | 1531428 | +22.24% | INVALID_5M | 99/1 | 99/0 |
| AVAX-EUR | 1498854 | +8.83% | INVALID_5M | 100/1 | 99/0 |
| COTI-EUR | 1461615 | -12.86% | INVALID_5M | 100/8 | 99/0 |
| POL-EUR | 1365343 | +5.93% | INVALID_5M | 100/1 | 99/0 |
| DOT-EUR | 1328355 | +3.52% | INVALID_5M | 99/5 | 99/0 |
| HBAR-EUR | 1275655 | +4.87% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1217251 | +18.53% | INVALID_5M | 100/6 | 99/0 |
| AAVE-EUR | 1133018 | +8.03% | INVALID_5M | 99/5 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
