# Audit qualité des données Bitvavo

Scan : 2026-09-20T07:45:47.900800+00:00 (20260920T074419Z-5f4077e7)
Univers : 426 | strategy-grade : 34 | rejetés : 392
5m valides : 37 | 15m valides : 62 | deux intervalles valides : 34

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 389 |
| INVALID_15M | 364 |
| MISSING_LATEST_CLOSED_CANDLE | 142 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 389 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 364 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2624030 | -0.82% | INVALID_5M | 99/5 | 100/0 |
| HBAR-EUR | 2292086 | +4.15% | INVALID_5M | 100/1 | 100/0 |
| FET-EUR | 1964658 | -3.94% | INVALID_5M | 99/1 | 100/0 |
| PUMP-EUR | 1684986 | -2.51% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 100/0 |
| DOGE-EUR | 1680428 | -1.93% | INVALID_5M | 99/3 | 100/0 |
| LTC-EUR | 1319706 | -0.09% | INVALID_5M | 100/3 | 100/0 |
| EPIC-EUR | 1073698 | +9.00% | INVALID_15M, INVALID_5M | 99/4 | 100/3 |
| CAKE-EUR | 1047422 | -1.04% | INVALID_15M, INVALID_5M | 99/15 | 100/6 |
| VET-EUR | 1022967 | -4.08% | INVALID_5M | 99/2 | 100/0 |
| STX-EUR | 994793 | +10.90% | INVALID_5M | 100/1 | 100/0 |
| APT-EUR | 950973 | +3.34% | INVALID_15M, INVALID_5M | 100/20 | 100/2 |
| FIL-EUR | 875550 | +1.14% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/10 | 100/3 |
| USELESS-EUR | 862954 | -6.22% | INVALID_5M | 99/2 | 100/0 |
| BCH-EUR | 824032 | +0.03% | INVALID_15M, INVALID_5M | 82/17 | 100/2 |
| HEI-EUR | 807641 | -6.01% | INVALID_15M, INVALID_5M | 99/4 | 100/2 |
| KAS-EUR | 768952 | +0.43% | INVALID_15M, INVALID_5M | 94/3 | 100/7 |
| JUP-EUR | 741464 | -0.41% | INVALID_15M, INVALID_5M | 100/9 | 100/1 |
| SHIB-EUR | 737821 | -0.23% | INVALID_15M, INVALID_5M | 100/6 | 100/2 |
| SKL-EUR | 670121 | +14.46% | INVALID_5M | 99/1 | 93/0 |
| COTI-EUR | 657562 | -7.22% | INVALID_15M, INVALID_5M | 98/11 | 100/5 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
