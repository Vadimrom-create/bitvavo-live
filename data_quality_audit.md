# Audit qualité des données Bitvavo

Scan : 2026-09-20T04:53:46.480704+00:00 (20260920T045210Z-fc293e69)
Univers : 427 | strategy-grade : 26 | rejetés : 401
5m valides : 29 | 15m valides : 59 | deux intervalles valides : 26

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 398 |
| INVALID_15M | 368 |
| MISSING_LATEST_CLOSED_CANDLE | 294 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 398 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 368 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ONDO-EUR | 6104981 | +1.21% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |
| INJ-EUR | 3144394 | +9.86% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2794888 | -1.67% | INVALID_5M | 99/1 | 99/0 |
| ZAMA-EUR | 2301630 | +33.43% | INVALID_5M | 99/1 | 99/0 |
| SYN-EUR | 2296685 | +12.27% | INVALID_5M | 99/2 | 99/0 |
| HBAR-EUR | 2067488 | +2.02% | INVALID_5M | 99/6 | 99/0 |
| CAP-EUR | 1996713 | -16.28% | INVALID_5M | 99/14 | 99/0 |
| DOGE-EUR | 1651999 | -2.37% | INVALID_5M | 99/3 | 99/0 |
| LSK-EUR | 1529020 | -10.00% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1479840 | -28.00% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1397111 | -2.08% | INVALID_5M | 99/6 | 99/0 |
| WLD-EUR | 1373643 | +1.73% | INVALID_5M | 99/1 | 99/0 |
| VET-EUR | 1241104 | +1.59% | INVALID_5M | 99/2 | 99/0 |
| EPIC-EUR | 1212315 | +19.33% | INVALID_15M, INVALID_5M | 99/2 | 99/3 |
| APT-EUR | 1195413 | -5.39% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/10 | 100/2 |
| STRK-EUR | 1082378 | +9.97% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 1028636 | -10.64% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 940540 | +13.75% | INVALID_5M | 99/2 | 99/0 |
| FIL-EUR | 907149 | -3.06% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/24 | 100/2 |
| HEI-EUR | 904743 | +15.26% | INVALID_15M, INVALID_5M | 99/18 | 99/3 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
