# Audit qualité des données Bitvavo

Scan : 2026-09-19T05:30:40.867954+00:00 (20260919T052911Z-e5f4a20b)
Univers : 427 | strategy-grade : 25 | rejetés : 402
5m valides : 27 | 15m valides : 63 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 400 |
| INVALID_15M | 364 |
| MISSING_LATEST_CLOSED_CANDLE | 232 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 400 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 364 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 5286672 | +4.87% | INVALID_5M | 100/1 | 100/0 |
| USDC-EUR | 2603093 | -0.17% | INVALID_5M | 99/1 | 100/0 |
| WLD-EUR | 2569003 | +0.64% | INVALID_5M | 100/1 | 100/0 |
| PUMP-EUR | 2408818 | -1.72% | INVALID_5M | 100/3 | 100/0 |
| XLM-EUR | 2112604 | +4.10% | INVALID_5M | 99/1 | 100/0 |
| INJ-EUR | 2000962 | +16.46% | INVALID_5M | 99/2 | 100/0 |
| DOGE-EUR | 1846383 | +3.98% | INVALID_5M | 100/2 | 100/0 |
| CNPY-EUR | 1707174 | +13.25% | INVALID_5M | 99/1 | 100/0 |
| AVAX-EUR | 1678476 | +7.35% | INVALID_5M | 100/1 | 100/0 |
| POL-EUR | 1603329 | +4.16% | INVALID_5M | 100/7 | 100/0 |
| LTC-EUR | 1602545 | +6.21% | INVALID_5M | 99/1 | 100/0 |
| F-EUR | 1523740 | +35.07% | INVALID_5M | 100/2 | 85/0 |
| DOT-EUR | 1337714 | -0.58% | INVALID_5M | 100/1 | 100/0 |
| SKY-EUR | 1310994 | +14.60% | INVALID_5M | 99/10 | 100/0 |
| RAY-EUR | 1265887 | +5.75% | INVALID_15M, INVALID_5M | 100/6 | 100/1 |
| HBAR-EUR | 1237378 | +3.32% | INVALID_15M, INVALID_5M | 100/17 | 100/1 |
| COTI-EUR | 1147045 | -6.97% | INVALID_15M, INVALID_5M | 100/13 | 100/2 |
| AAVE-EUR | 1110624 | +7.52% | INVALID_5M | 99/1 | 100/0 |
| BNB-EUR | 1020253 | +1.45% | INVALID_15M, INVALID_5M | 100/1 | 100/1 |
| BCH-EUR | 980638 | -0.12% | INVALID_15M, INVALID_5M | 99/12 | 100/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
