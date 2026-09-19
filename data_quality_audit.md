# Audit qualité des données Bitvavo

Scan : 2026-09-19T03:21:42.794589+00:00 (20260919T032015Z-4c45a3c3)
Univers : 427 | strategy-grade : 19 | rejetés : 408
5m valides : 19 | 15m valides : 59 | deux intervalles valides : 19

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 408 |
| INVALID_15M | 368 |
| MISSING_LATEST_CLOSED_CANDLE | 289 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 408 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 368 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 5922575 | +7.56% | INVALID_5M | 99/1 | 99/0 |
| G-EUR | 3399441 | +74.90% | INVALID_5M | 99/2 | 99/0 |
| ARB-EUR | 3232055 | -2.08% | INVALID_5M | 99/3 | 99/0 |
| USDC-EUR | 2710197 | -0.14% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 2608670 | +3.64% | INVALID_5M | 100/6 | 99/0 |
| WLD-EUR | 2565659 | +5.27% | INVALID_5M | 99/7 | 99/0 |
| FET-EUR | 2478010 | -0.11% | INVALID_5M | 100/4 | 99/0 |
| INJ-EUR | 1998928 | +17.46% | INVALID_5M | 99/3 | 99/0 |
| DOGE-EUR | 1932621 | +4.82% | INVALID_5M | 100/1 | 99/0 |
| CNPY-EUR | 1773330 | +14.75% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/9 | 100/0 |
| AVAX-EUR | 1690903 | +9.12% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1540101 | +7.33% | INVALID_5M | 99/3 | 99/0 |
| F-EUR | 1502830 | +34.45% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1470634 | +7.29% | INVALID_5M | 99/4 | 99/0 |
| RAY-EUR | 1457551 | +8.18% | INVALID_15M, INVALID_5M | 99/12 | 99/1 |
| COTI-EUR | 1392285 | -10.87% | INVALID_15M, INVALID_5M | 100/13 | 99/1 |
| DOT-EUR | 1329320 | +2.58% | INVALID_5M | 99/4 | 99/0 |
| SKY-EUR | 1296060 | +16.27% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/5 | 100/0 |
| ENA-EUR | 1286703 | +7.41% | INVALID_5M | 99/2 | 99/0 |
| HBAR-EUR | 1271317 | +3.51% | INVALID_15M, INVALID_5M | 100/6 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
