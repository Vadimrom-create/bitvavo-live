# Audit qualité des données Bitvavo

Scan : 2026-09-20T08:50:31.277303+00:00 (20260920T084902Z-2d627838)
Univers : 426 | strategy-grade : 31 | rejetés : 395
5m valides : 34 | 15m valides : 67 | deux intervalles valides : 31

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 359 |
| MISSING_LATEST_CLOSED_CANDLE | 182 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 359 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2562438 | -1.78% | INVALID_5M | 99/1 | 99/0 |
| ZAMA-EUR | 2358431 | +5.93% | INVALID_5M | 100/1 | 99/0 |
| CAP-EUR | 2030607 | -25.68% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 1672933 | -3.63% | INVALID_5M | 100/7 | 99/0 |
| DOGE-EUR | 1623095 | -3.02% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1397557 | -0.63% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1275251 | -0.93% | INVALID_5M | 100/1 | 99/0 |
| CAKE-EUR | 1094448 | +0.55% | INVALID_15M, INVALID_5M | 85/4 | 99/4 |
| EPIC-EUR | 1072720 | +9.87% | INVALID_5M | 100/4 | 99/0 |
| STX-EUR | 1005746 | +10.60% | INVALID_5M | 99/5 | 99/0 |
| APT-EUR | 953330 | +2.73% | INVALID_15M, INVALID_5M | 100/7 | 99/1 |
| VET-EUR | 896580 | -2.79% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 870981 | -6.37% | INVALID_5M | 100/3 | 99/0 |
| FIL-EUR | 857620 | -3.61% | INVALID_15M, INVALID_5M | 100/9 | 99/2 |
| DOT-EUR | 821261 | -2.81% | INVALID_5M | 99/1 | 99/0 |
| SAGA-EUR | 810188 | +7.24% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 799712 | -1.25% | INVALID_15M, INVALID_5M | 90/9 | 99/1 |
| KAS-EUR | 798010 | +4.36% | INVALID_15M, INVALID_5M | 95/2 | 99/2 |
| SHIB-EUR | 723708 | -1.34% | INVALID_5M | 99/3 | 100/0 |
| JUP-EUR | 720414 | -1.52% | INVALID_15M, INVALID_5M | 100/6 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
