# Audit qualité des données Bitvavo

Scan : 2026-09-19T12:24:02.140184+00:00 (20260919T122159Z-a62a177b)
Univers : 427 | strategy-grade : 37 | rejetés : 390
5m valides : 38 | 15m valides : 81 | deux intervalles valides : 38

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 389 |
| INVALID_15M | 346 |
| MISSING_LATEST_CLOSED_CANDLE | 251 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 389 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 346 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| G-EUR | 2749154 | -1.46% | INVALID_5M | 99/2 | 99/0 |
| ENA-EUR | 2320738 | +20.29% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 2045893 | -2.07% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1768234 | +8.92% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 100/0 |
| LTC-EUR | 1625825 | +5.18% | INVALID_5M | 99/2 | 99/0 |
| F-EUR | 1624310 | +26.12% | INVALID_5M | 99/4 | 99/0 |
| POL-EUR | 1621201 | +4.67% | INVALID_5M | 99/5 | 99/0 |
| SKY-EUR | 1372899 | +5.16% | INVALID_5M | 100/7 | 99/0 |
| SAGA-EUR | 1296807 | +29.18% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 1049333 | +0.91% | INVALID_5M | 99/11 | 99/0 |
| MORPHO-EUR | 859454 | +13.15% | INVALID_5M | 100/4 | 99/0 |
| LPT-EUR | 848019 | +4.91% | INVALID_5M | 99/7 | 99/0 |
| C-EUR | 824545 | +17.28% | INVALID_5M | 99/7 | 99/0 |
| BNB-EUR | 815131 | +2.56% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| SUPER-EUR | 768041 | +6.18% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/25 | 100/3 |
| LAPTOP-EUR | 754683 | -18.73% | INVALID_5M | 99/1 | 99/0 |
| EPIC-EUR | 741977 | +23.13% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 100/0 |
| JUP-EUR | 741275 | +8.83% | INVALID_5M | 99/1 | 99/0 |
| ACH-EUR | 703870 | +13.06% | INVALID_5M | 99/4 | 99/0 |
| S-EUR | 697808 | +0.43% | INVALID_15M, INVALID_5M | 100/22 | 99/3 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
