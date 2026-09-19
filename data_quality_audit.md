# Audit qualité des données Bitvavo

Scan : 2026-09-19T03:38:11.949041+00:00 (20260919T033640Z-6b48e945)
Univers : 427 | strategy-grade : 20 | rejetés : 407
5m valides : 21 | 15m valides : 58 | deux intervalles valides : 20

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 406 |
| INVALID_15M | 369 |
| MISSING_LATEST_CLOSED_CANDLE | 294 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 406 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 369 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| G-EUR | 3436767 | +69.14% | INVALID_5M | 99/1 | 99/0 |
| ARB-EUR | 3176673 | -3.03% | INVALID_5M | 99/3 | 99/0 |
| USDC-EUR | 2695959 | -0.15% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 2593063 | +3.11% | INVALID_5M | 99/8 | 99/0 |
| WLD-EUR | 2548074 | +4.40% | INVALID_5M | 99/7 | 99/0 |
| FET-EUR | 2416632 | -0.73% | INVALID_5M | 99/4 | 99/0 |
| INJ-EUR | 1989645 | +17.15% | INVALID_5M | 99/3 | 99/0 |
| DOGE-EUR | 1932008 | +4.72% | INVALID_5M | 99/2 | 99/0 |
| PEPE-EUR | 1819187 | +2.27% | INVALID_5M | 99/1 | 99/0 |
| CNPY-EUR | 1757654 | +16.21% | INVALID_5M | 99/10 | 99/0 |
| LTC-EUR | 1556702 | +6.99% | INVALID_5M | 100/3 | 99/0 |
| F-EUR | 1503288 | +35.54% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1482448 | +6.90% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 100/0 |
| RAY-EUR | 1424298 | +4.91% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/12 | 99/1 |
| COTI-EUR | 1385494 | -12.45% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/13 | 100/1 |
| DOT-EUR | 1355501 | +1.46% | INVALID_5M | 100/3 | 99/0 |
| ENA-EUR | 1306442 | +10.41% | INVALID_5M | 99/2 | 99/0 |
| SKY-EUR | 1288800 | +13.92% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 99/0 |
| HBAR-EUR | 1268145 | +3.09% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 99/1 |
| AAVE-EUR | 1141096 | +7.02% | INVALID_5M | 99/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
