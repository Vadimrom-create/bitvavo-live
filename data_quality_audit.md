# Audit qualité des données Bitvavo

Scan : 2026-09-19T04:26:49.108039+00:00 (20260919T042519Z-6a72cc0c)
Univers : 427 | strategy-grade : 22 | rejetés : 405
5m valides : 23 | 15m valides : 57 | deux intervalles valides : 22

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 404 |
| INVALID_15M | 370 |
| MISSING_LATEST_CLOSED_CANDLE | 305 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 404 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 370 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ARB-EUR | 2968301 | -6.33% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 2527275 | +3.81% | INVALID_5M | 100/6 | 99/0 |
| WLD-EUR | 2472558 | +0.28% | INVALID_5M | 99/6 | 99/0 |
| FET-EUR | 2403595 | -0.89% | INVALID_5M | 99/4 | 99/0 |
| XLM-EUR | 2088861 | +3.65% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1874969 | +4.18% | INVALID_5M | 100/2 | 99/0 |
| PEPE-EUR | 1859349 | +3.98% | INVALID_5M | 100/1 | 99/0 |
| CNPY-EUR | 1745654 | +14.70% | INVALID_5M | 99/8 | 99/0 |
| LTC-EUR | 1566880 | +7.93% | INVALID_5M | 99/2 | 99/0 |
| F-EUR | 1507479 | +38.44% | INVALID_5M | 100/2 | 80/0 |
| POL-EUR | 1502891 | +6.05% | INVALID_5M | 100/8 | 99/0 |
| ENA-EUR | 1424192 | +9.79% | INVALID_5M | 99/2 | 99/0 |
| RAY-EUR | 1372956 | +5.96% | INVALID_15M, INVALID_5M | 100/8 | 99/1 |
| DOT-EUR | 1350040 | +1.23% | INVALID_5M | 99/2 | 99/0 |
| COTI-EUR | 1326687 | -15.74% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/15 | 99/2 |
| SKY-EUR | 1278911 | +13.68% | INVALID_5M | 100/9 | 99/0 |
| HBAR-EUR | 1256509 | +3.33% | INVALID_15M, INVALID_5M | 100/14 | 99/1 |
| AAVE-EUR | 1143575 | +6.91% | INVALID_5M | 99/1 | 99/0 |
| XPL-EUR | 1008098 | +2.03% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/9 | 99/0 |
| BNB-EUR | 1007045 | +1.88% | INVALID_15M, INVALID_5M | 99/4 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
