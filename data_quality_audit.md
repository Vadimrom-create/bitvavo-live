# Audit qualité des données Bitvavo

Scan : 2026-09-20T10:23:25.804826+00:00 (20260920T102151Z-85ee17d9)
Univers : 426 | strategy-grade : 35 | rejetés : 391
5m valides : 40 | 15m valides : 69 | deux intervalles valides : 36

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 386 |
| INVALID_15M | 357 |
| MISSING_LATEST_CLOSED_CANDLE | 268 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 386 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 357 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| CAP-EUR | 2030226 | -24.65% | INVALID_5M | 99/7 | 99/0 |
| UNI-EUR | 1639276 | -4.97% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| DOGE-EUR | 1564880 | -3.37% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1333787 | -4.66% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| CAKE-EUR | 1155885 | +0.48% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 94/2 | 100/3 |
| ARB-EUR | 1129582 | +0.39% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 1071493 | +5.53% | INVALID_5M | 99/1 | 99/0 |
| EPIC-EUR | 1047585 | +7.25% | INVALID_5M | 99/2 | 99/0 |
| STX-EUR | 1029582 | +6.35% | INVALID_5M | 100/2 | 99/0 |
| APT-EUR | 873806 | -1.67% | INVALID_15M, INVALID_5M | 99/4 | 99/1 |
| USELESS-EUR | 859979 | -4.95% | INVALID_5M | 99/4 | 99/0 |
| FIL-EUR | 856519 | -2.56% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/9 | 100/2 |
| KAS-EUR | 815946 | +1.52% | INVALID_15M, MISSING_LATEST_CLOSED_CANDLE | 96/0 | 99/1 |
| DOT-EUR | 811000 | -2.60% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 757554 | -1.27% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 82/12 | 100/1 |
| SHIB-EUR | 740353 | -1.31% | INVALID_5M | 99/1 | 99/0 |
| SKL-EUR | 706521 | +17.09% | INVALID_5M | 99/5 | 97/0 |
| JUP-EUR | 645538 | -5.55% | INVALID_15M, INVALID_5M | 100/5 | 99/1 |
| DRIFT-EUR | 609511 | -8.43% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 99/0 |
| COTI-EUR | 605148 | -10.89% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 89/15 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
