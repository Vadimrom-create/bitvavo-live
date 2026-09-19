# Audit qualité des données Bitvavo

Scan : 2026-09-19T12:42:48.644995+00:00 (20260919T124124Z-6892696a)
Univers : 427 | strategy-grade : 36 | rejetés : 391
5m valides : 37 | 15m valides : 82 | deux intervalles valides : 36

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 390 |
| INVALID_15M | 345 |
| MISSING_LATEST_CLOSED_CANDLE | 275 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 390 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 345 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 3267865 | +5.36% | INVALID_5M | 99/1 | 99/0 |
| G-EUR | 2673647 | +3.68% | INVALID_5M | 99/2 | 99/0 |
| ENA-EUR | 2393350 | +21.68% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1829504 | +7.05% | INVALID_5M | 99/1 | 99/0 |
| F-EUR | 1625185 | +26.20% | INVALID_5M | 99/3 | 99/0 |
| LTC-EUR | 1622605 | +5.03% | INVALID_5M | 99/2 | 99/0 |
| POL-EUR | 1618245 | +4.36% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 99/0 |
| SKY-EUR | 1381923 | +6.36% | INVALID_5M | 99/9 | 99/0 |
| SAGA-EUR | 1304311 | +29.39% | INVALID_5M | 99/1 | 99/0 |
| AAVE-EUR | 1202002 | +3.52% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 1066664 | +0.49% | INVALID_5M | 99/11 | 99/0 |
| MORPHO-EUR | 848949 | +12.62% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/6 | 99/0 |
| C-EUR | 828789 | +16.05% | INVALID_5M | 99/7 | 99/0 |
| LPT-EUR | 828238 | +4.96% | INVALID_5M | 100/8 | 99/0 |
| HEI-EUR | 825120 | +31.52% | INVALID_5M | 99/1 | 99/0 |
| BNB-EUR | 814692 | +2.81% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| JUP-EUR | 757216 | +7.61% | INVALID_5M | 99/1 | 99/0 |
| LAPTOP-EUR | 748966 | -17.26% | INVALID_5M | 99/1 | 99/0 |
| SUPER-EUR | 746084 | +4.89% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/32 | 99/3 |
| EPIC-EUR | 738427 | +23.66% | INVALID_5M | 99/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
