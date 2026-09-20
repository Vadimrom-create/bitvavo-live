# Audit qualité des données Bitvavo

Scan : 2026-09-20T05:10:29.937311+00:00 (20260920T050859Z-c1d7c32c)
Univers : 427 | strategy-grade : 24 | rejetés : 403
5m valides : 25 | 15m valides : 59 | deux intervalles valides : 24

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 402 |
| INVALID_15M | 368 |
| MISSING_LATEST_CLOSED_CANDLE | 278 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 402 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 368 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ONDO-EUR | 6093545 | +0.59% | INVALID_5M | 100/2 | 99/0 |
| INJ-EUR | 3150790 | +9.54% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2778560 | -1.78% | INVALID_5M | 99/1 | 99/0 |
| SYN-EUR | 2313229 | +5.46% | INVALID_5M | 99/2 | 99/0 |
| ZAMA-EUR | 2309633 | +31.60% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 2088204 | +1.86% | INVALID_5M | 99/6 | 99/0 |
| FET-EUR | 2066045 | -5.10% | INVALID_5M | 100/1 | 99/0 |
| CAP-EUR | 1997450 | -16.46% | INVALID_5M | 99/13 | 99/0 |
| PUMP-EUR | 1968927 | -3.78% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1647785 | -2.54% | INVALID_5M | 99/3 | 99/0 |
| LSK-EUR | 1520543 | -8.53% | INVALID_5M | 100/2 | 99/0 |
| CNPY-EUR | 1483689 | -29.40% | INVALID_5M | 100/1 | 99/0 |
| LTC-EUR | 1416216 | -2.43% | INVALID_5M | 99/3 | 99/0 |
| WLD-EUR | 1343646 | +1.26% | INVALID_5M | 100/1 | 99/0 |
| EPIC-EUR | 1211015 | +12.05% | INVALID_15M, INVALID_5M | 99/2 | 99/3 |
| VET-EUR | 1198041 | +0.11% | INVALID_5M | 100/2 | 99/0 |
| APT-EUR | 1169852 | -6.84% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/12 | 100/2 |
| USELESS-EUR | 1012657 | -9.23% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 944121 | +13.91% | INVALID_5M | 99/2 | 99/0 |
| HEI-EUR | 903653 | +15.30% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/15 | 100/3 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
