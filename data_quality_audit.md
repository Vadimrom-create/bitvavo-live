# Audit qualité des données Bitvavo

Scan : 2026-09-20T05:55:55.847582+00:00 (20260920T055427Z-ea73fd44)
Univers : 427 | strategy-grade : 25 | rejetés : 402
5m valides : 26 | 15m valides : 60 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 401 |
| INVALID_15M | 367 |
| MISSING_LATEST_CLOSED_CANDLE | 272 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 401 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 367 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ONDO-EUR | 6109765 | +2.12% | INVALID_5M | 99/2 | 99/0 |
| INJ-EUR | 3220344 | +9.56% | INVALID_5M | 100/1 | 99/0 |
| XLM-EUR | 2770738 | -2.34% | INVALID_5M | 100/3 | 99/0 |
| SYN-EUR | 2322112 | +5.88% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 2124137 | +2.30% | INVALID_5M | 100/6 | 99/0 |
| FET-EUR | 2098120 | -4.35% | INVALID_5M | 100/1 | 99/0 |
| CAP-EUR | 2001232 | -17.25% | INVALID_5M | 100/6 | 99/0 |
| PUMP-EUR | 1791306 | -1.85% | INVALID_5M | 100/2 | 99/0 |
| DOGE-EUR | 1652681 | -2.49% | INVALID_5M | 100/4 | 99/0 |
| LSK-EUR | 1507035 | -11.39% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1491732 | -28.06% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1379851 | -0.57% | INVALID_5M | 99/2 | 99/0 |
| WLD-EUR | 1374582 | +2.24% | INVALID_5M | 99/1 | 99/0 |
| VET-EUR | 1178272 | +2.02% | INVALID_5M | 100/2 | 99/0 |
| EPIC-EUR | 1169975 | +10.79% | INVALID_15M, INVALID_5M | 99/1 | 99/3 |
| APT-EUR | 1091749 | -0.75% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/16 | 100/2 |
| STRK-EUR | 1064225 | +11.32% | INVALID_5M | 100/3 | 99/0 |
| STX-EUR | 969876 | +17.91% | INVALID_5M | 99/1 | 99/0 |
| HEI-EUR | 911518 | +8.68% | INVALID_15M, INVALID_5M | 100/11 | 99/2 |
| FIL-EUR | 909701 | -3.63% | INVALID_15M, INVALID_5M | 100/19 | 99/3 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
