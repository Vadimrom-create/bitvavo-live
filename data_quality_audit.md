# Audit qualité des données Bitvavo

Scan : 2026-09-19T03:01:51.375267+00:00 (20260919T030025Z-032a35ae)
Univers : 427 | strategy-grade : 20 | rejetés : 407
5m valides : 22 | 15m valides : 59 | deux intervalles valides : 21

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 405 |
| INVALID_15M | 368 |
| MISSING_LATEST_CLOSED_CANDLE | 265 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 405 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 368 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 6112616 | +13.62% | INVALID_5M | 99/4 | 99/0 |
| G-EUR | 3350820 | +52.57% | INVALID_5M | 99/2 | 99/0 |
| ARB-EUR | 3290624 | +5.56% | INVALID_5M | 100/3 | 100/0 |
| PUMP-EUR | 2725662 | +4.35% | INVALID_5M | 100/5 | 100/0 |
| USDC-EUR | 2707238 | -0.18% | INVALID_5M | 99/2 | 100/0 |
| WLD-EUR | 2571125 | +4.81% | INVALID_5M | 100/7 | 100/0 |
| FET-EUR | 2484455 | +1.78% | INVALID_5M | 100/3 | 100/0 |
| INJ-EUR | 1973013 | +17.26% | INVALID_5M | 99/5 | 99/0 |
| DOGE-EUR | 1938976 | +6.42% | INVALID_5M | 99/1 | 99/0 |
| CNPY-EUR | 1796268 | +4.82% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/9 | 100/0 |
| AVAX-EUR | 1686001 | +11.13% | INVALID_5M | 99/1 | 100/0 |
| LTC-EUR | 1542719 | +7.62% | INVALID_5M | 99/3 | 99/0 |
| F-EUR | 1501822 | +35.22% | INVALID_5M | 99/1 | 100/0 |
| RAY-EUR | 1494717 | +14.75% | INVALID_15M, INVALID_5M | 100/11 | 100/1 |
| POL-EUR | 1471877 | +8.18% | INVALID_5M | 100/2 | 100/0 |
| COTI-EUR | 1427376 | -12.25% | INVALID_15M, INVALID_5M | 99/13 | 100/1 |
| DOT-EUR | 1321175 | +2.79% | INVALID_5M | 99/3 | 100/0 |
| SKY-EUR | 1302676 | +16.82% | INVALID_5M | 100/5 | 100/0 |
| ENA-EUR | 1293362 | +6.39% | MISSING_LATEST_CLOSED_CANDLE | 100/0 | 100/0 |
| HBAR-EUR | 1266833 | +3.87% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/5 | 100/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
