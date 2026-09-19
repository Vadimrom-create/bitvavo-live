# Audit qualité des données Bitvavo

Scan : 2026-09-19T16:50:14.540245+00:00 (20260919T164843Z-8a10cb3c)
Univers : 427 | strategy-grade : 35 | rejetés : 392
5m valides : 39 | 15m valides : 85 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 388 |
| INVALID_15M | 342 |
| MISSING_LATEST_CLOSED_CANDLE | 220 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 388 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 342 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| STRK-EUR | 2162738 | +20.89% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1864043 | +8.61% | INVALID_5M | 100/2 | 100/0 |
| CAP-EUR | 1786175 | -13.91% | INVALID_15M | 99/0 | 99/2 |
| POL-EUR | 1538353 | +4.23% | INVALID_5M | 100/3 | 99/0 |
| WLD-EUR | 1485425 | +3.40% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 1471681 | +3.90% | INVALID_5M | 100/1 | 99/0 |
| SAGA-EUR | 1373985 | +22.38% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1202506 | +8.39% | INVALID_5M | 99/7 | 99/0 |
| F-EUR | 1133702 | -17.07% | INVALID_5M | 100/4 | 99/0 |
| SKY-EUR | 1087756 | +0.23% | INVALID_15M, INVALID_5M | 100/10 | 99/1 |
| VET-EUR | 1059283 | +7.74% | INVALID_5M | 99/1 | 99/0 |
| AAVE-EUR | 1057251 | +3.56% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/5 | 100/0 |
| DOT-EUR | 944047 | -0.68% | INVALID_5M | 100/2 | 99/0 |
| BCH-EUR | 915696 | +2.99% | INVALID_5M | 100/4 | 99/0 |
| COTI-EUR | 910694 | -1.87% | INVALID_5M | 99/1 | 99/0 |
| MORPHO-EUR | 803539 | +11.82% | INVALID_5M | 100/2 | 99/0 |
| KAS-EUR | 795965 | +8.78% | INVALID_5M | 99/1 | 99/0 |
| JUP-EUR | 773968 | +7.31% | INVALID_5M | 100/5 | 100/0 |
| HEI-EUR | 773390 | +15.09% | INVALID_5M | 100/3 | 99/0 |
| LAPTOP-EUR | 650183 | -9.47% | INVALID_5M | 99/2 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
