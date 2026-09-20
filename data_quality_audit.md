# Audit qualité des données Bitvavo

Scan : 2026-09-20T07:58:28.130108+00:00 (20260920T075658Z-9e7eb15b)
Univers : 426 | strategy-grade : 33 | rejetés : 393
5m valides : 36 | 15m valides : 62 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 390 |
| INVALID_15M | 364 |
| MISSING_LATEST_CLOSED_CANDLE | 232 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 390 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 364 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2581589 | -1.06% | INVALID_5M | 99/5 | 99/0 |
| HBAR-EUR | 2305156 | +4.34% | INVALID_5M | 99/1 | 99/0 |
| FET-EUR | 1955133 | -4.63% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1684430 | -3.49% | INVALID_5M | 99/6 | 99/0 |
| DOGE-EUR | 1680701 | -1.96% | INVALID_5M | 99/3 | 99/0 |
| LTC-EUR | 1270313 | -0.09% | INVALID_5M | 99/2 | 99/0 |
| EPIC-EUR | 1072988 | +9.44% | INVALID_15M, INVALID_5M | 99/4 | 99/3 |
| CAKE-EUR | 1048806 | -0.38% | INVALID_15M, INVALID_5M | 100/9 | 99/6 |
| VET-EUR | 1006479 | -3.91% | INVALID_5M | 99/2 | 99/0 |
| STX-EUR | 993076 | +10.16% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 100/0 |
| APT-EUR | 947278 | +3.92% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/20 | 100/2 |
| FIL-EUR | 876923 | +0.22% | INVALID_15M, INVALID_5M | 99/9 | 99/3 |
| USELESS-EUR | 863605 | -6.53% | INVALID_5M | 99/2 | 99/0 |
| BCH-EUR | 823166 | +0.08% | INVALID_15M, INVALID_5M | 81/18 | 99/2 |
| HEI-EUR | 776116 | -9.23% | INVALID_15M, INVALID_5M | 100/4 | 99/2 |
| KAS-EUR | 775921 | +1.96% | INVALID_15M, INVALID_5M | 94/2 | 99/7 |
| SHIB-EUR | 740285 | -0.21% | INVALID_15M, INVALID_5M | 99/4 | 99/2 |
| JUP-EUR | 739585 | +0.16% | INVALID_15M, INVALID_5M | 99/9 | 99/1 |
| SKL-EUR | 672628 | +16.44% | INVALID_5M | 99/1 | 92/0 |
| COTI-EUR | 652413 | -7.31% | INVALID_15M, INVALID_5M | 97/12 | 99/5 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
