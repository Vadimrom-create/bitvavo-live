# Audit qualité des données Bitvavo

Scan : 2026-09-20T03:31:41.349221+00:00 (20260920T033014Z-3aacd44b)
Univers : 427 | strategy-grade : 28 | rejetés : 399
5m valides : 30 | 15m valides : 57 | deux intervalles valides : 28

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 397 |
| INVALID_15M | 370 |
| MISSING_LATEST_CLOSED_CANDLE | 266 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 397 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 370 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| NEAR-EUR | 6003079 | -6.61% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2818932 | -1.80% | INVALID_5M | 99/2 | 99/0 |
| SYN-EUR | 2308495 | +8.33% | INVALID_5M | 99/2 | 100/0 |
| ZAMA-EUR | 2251370 | +33.22% | INVALID_5M | 99/1 | 100/0 |
| CAP-EUR | 2003794 | -15.43% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/9 | 100/0 |
| UNI-EUR | 1996994 | -3.24% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1980614 | -6.55% | INVALID_5M | 99/2 | 100/0 |
| DOGE-EUR | 1650273 | -2.28% | INVALID_5M | 99/3 | 100/0 |
| CNPY-EUR | 1464402 | -26.00% | INVALID_5M | 99/1 | 100/0 |
| LTC-EUR | 1442607 | -2.23% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/8 | 100/0 |
| VET-EUR | 1349618 | +7.44% | INVALID_5M | 99/3 | 100/0 |
| APT-EUR | 1262630 | -5.39% | INVALID_15M, INVALID_5M | 99/8 | 100/1 |
| EPIC-EUR | 1208922 | +13.22% | INVALID_15M, INVALID_5M | 99/14 | 100/3 |
| STRK-EUR | 1191644 | -0.16% | INVALID_5M | 99/2 | 99/0 |
| ARB-EUR | 1133788 | -0.03% | INVALID_5M | 99/2 | 99/0 |
| USELESS-EUR | 1091950 | -15.80% | INVALID_5M | 100/1 | 100/0 |
| OP-EUR | 984251 | -1.63% | INVALID_15M, INVALID_5M | 100/9 | 100/4 |
| FIL-EUR | 908731 | -1.18% | INVALID_15M, INVALID_5M | 100/17 | 100/1 |
| HEI-EUR | 892148 | +14.91% | INVALID_15M, INVALID_5M | 100/15 | 100/2 |
| BCH-EUR | 851777 | -3.43% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 97/24 | 100/3 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
