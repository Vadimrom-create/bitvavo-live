# Audit qualité des données Bitvavo

Scan : 2026-09-20T05:43:17.610481+00:00 (20260920T054146Z-17127eb3)
Univers : 427 | strategy-grade : 23 | rejetés : 404
5m valides : 23 | 15m valides : 60 | deux intervalles valides : 23

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 404 |
| INVALID_15M | 367 |
| MISSING_LATEST_CLOSED_CANDLE | 301 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 404 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 367 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ONDO-EUR | 6064085 | +1.98% | INVALID_5M | 99/2 | 99/0 |
| INJ-EUR | 3197917 | +10.09% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2777737 | -2.62% | INVALID_5M | 99/2 | 99/0 |
| SYN-EUR | 2315923 | +6.54% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 2124728 | +2.11% | INVALID_5M | 99/6 | 99/0 |
| FET-EUR | 2099008 | -4.04% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 2001354 | -17.95% | INVALID_5M | 99/9 | 99/0 |
| PUMP-EUR | 1971466 | -2.92% | INVALID_5M | 99/2 | 99/0 |
| DOGE-EUR | 1650894 | -2.40% | INVALID_5M | 99/4 | 99/0 |
| LSK-EUR | 1517150 | -10.52% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1487743 | -26.82% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1416268 | -1.80% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 99/0 |
| WLD-EUR | 1371420 | +1.49% | INVALID_5M | 99/1 | 99/0 |
| VET-EUR | 1187347 | +0.84% | INVALID_5M | 99/2 | 99/0 |
| EPIC-EUR | 1175934 | +10.44% | INVALID_15M, INVALID_5M | 100/2 | 99/3 |
| APT-EUR | 1158900 | -6.34% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/14 | 100/2 |
| STRK-EUR | 1058190 | +11.87% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| USELESS-EUR | 1012776 | -7.11% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 950814 | +16.24% | INVALID_5M | 99/2 | 99/0 |
| FIL-EUR | 910291 | -3.50% | INVALID_15M, INVALID_5M | 100/19 | 99/3 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
