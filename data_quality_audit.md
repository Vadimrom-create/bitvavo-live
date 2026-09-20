# Audit qualité des données Bitvavo

Scan : 2026-09-20T06:39:19.611427+00:00 (20260920T063750Z-f6ec07ad)
Univers : 427 | strategy-grade : 25 | rejetés : 402
5m valides : 27 | 15m valides : 64 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 400 |
| INVALID_15M | 363 |
| MISSING_LATEST_CLOSED_CANDLE | 298 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 400 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 363 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ONDO-EUR | 5917495 | +2.64% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 3103458 | +3.72% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2743161 | -1.83% | INVALID_5M | 99/4 | 99/0 |
| HBAR-EUR | 2115349 | +2.11% | INVALID_5M | 99/3 | 99/0 |
| FET-EUR | 2029999 | -4.63% | INVALID_5M | 99/2 | 99/0 |
| CAP-EUR | 2005638 | -19.62% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1728317 | -2.70% | INVALID_5M | 99/4 | 99/0 |
| DOGE-EUR | 1639532 | -2.36% | INVALID_5M | 99/4 | 99/0 |
| CNPY-EUR | 1491337 | -30.95% | INVALID_5M | 99/1 | 99/0 |
| LSK-EUR | 1454531 | -4.51% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1424959 | +1.28% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1303879 | -0.59% | INVALID_5M | 99/3 | 99/0 |
| VET-EUR | 1177609 | -0.54% | INVALID_5M | 98/3 | 99/0 |
| EPIC-EUR | 1121857 | +8.06% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/3 |
| STRK-EUR | 1037878 | +8.51% | INVALID_5M | 98/3 | 99/0 |
| APT-EUR | 1007310 | +2.01% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/17 | 99/2 |
| STX-EUR | 988332 | +14.32% | INVALID_5M | 99/1 | 99/0 |
| HEI-EUR | 902711 | +5.34% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/12 | 99/2 |
| FIL-EUR | 893608 | -2.05% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/16 | 100/3 |
| BCH-EUR | 838986 | -0.11% | INVALID_15M, INVALID_5M | 83/20 | 99/4 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
