# Audit qualité des données Bitvavo

Scan : 2026-09-20T06:18:56.067773+00:00 (20260920T061724Z-d4c38bce)
Univers : 427 | strategy-grade : 25 | rejetés : 402
5m valides : 27 | 15m valides : 64 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 400 |
| INVALID_15M | 363 |
| MISSING_LATEST_CLOSED_CANDLE | 283 |

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
| ONDO-EUR | 6012655 | +3.57% | INVALID_5M | 99/2 | 99/0 |
| INJ-EUR | 3124374 | +8.18% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2769688 | -1.72% | INVALID_5M | 99/4 | 99/0 |
| SYN-EUR | 2312440 | +1.17% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 2113896 | +2.81% | INVALID_5M | 99/5 | 99/0 |
| FET-EUR | 2106080 | -3.70% | INVALID_5M | 100/1 | 100/0 |
| CAP-EUR | 2002932 | -19.36% | INVALID_5M | 99/3 | 100/0 |
| PUMP-EUR | 1746006 | -1.65% | INVALID_5M | 99/3 | 100/0 |
| DOGE-EUR | 1638814 | -2.20% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 100/0 |
| CNPY-EUR | 1496031 | -27.80% | INVALID_5M | 99/1 | 99/0 |
| LSK-EUR | 1491297 | -9.16% | INVALID_5M | 99/2 | 100/0 |
| WLD-EUR | 1416367 | +2.51% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1314361 | -0.25% | INVALID_5M | 99/3 | 99/0 |
| VET-EUR | 1169998 | +2.30% | INVALID_5M | 99/3 | 100/0 |
| EPIC-EUR | 1139023 | +9.01% | INVALID_15M, INVALID_5M | 99/1 | 99/3 |
| STRK-EUR | 1046722 | +10.55% | INVALID_5M | 99/3 | 99/0 |
| APT-EUR | 1038578 | +2.89% | INVALID_15M, INVALID_5M | 99/17 | 99/2 |
| STX-EUR | 979301 | +17.16% | INVALID_5M | 99/1 | 99/0 |
| FIL-EUR | 904551 | -0.94% | INVALID_15M, INVALID_5M | 100/15 | 100/3 |
| HEI-EUR | 902255 | +11.80% | INVALID_15M, INVALID_5M | 100/11 | 100/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
