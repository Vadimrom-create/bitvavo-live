# Audit qualité des données Bitvavo

Scan : 2026-09-20T02:23:41.955811+00:00 (20260920T022213Z-1c4c0189)
Univers : 427 | strategy-grade : 22 | rejetés : 405
5m valides : 23 | 15m valides : 59 | deux intervalles valides : 22

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 404 |
| INVALID_15M | 368 |
| MISSING_LATEST_CLOSED_CANDLE | 305 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 404 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 368 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 9086053 | -2.44% | INVALID_5M | 99/2 | 99/0 |
| NEAR-EUR | 6110902 | -7.01% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2693267 | +0.22% | INVALID_5M | 99/2 | 99/0 |
| SYN-EUR | 2329491 | +6.92% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 2021285 | -3.20% | INVALID_5M | 100/6 | 99/0 |
| CAP-EUR | 2002132 | -15.11% | INVALID_5M | 100/2 | 99/0 |
| PUMP-EUR | 1818255 | -2.42% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| HBAR-EUR | 1807235 | +3.09% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1579431 | -1.37% | INVALID_5M | 99/4 | 99/0 |
| CNPY-EUR | 1438993 | -23.69% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1413481 | -1.44% | INVALID_5M | 100/7 | 99/0 |
| WLD-EUR | 1405760 | +0.60% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1301405 | -3.42% | INVALID_15M, INVALID_5M | 99/10 | 99/2 |
| VET-EUR | 1294264 | +9.29% | INVALID_5M | 99/3 | 99/0 |
| STRK-EUR | 1212004 | +3.37% | INVALID_5M | 99/2 | 99/0 |
| EPIC-EUR | 1211123 | +12.36% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/10 | 100/2 |
| ARB-EUR | 1094055 | -3.59% | INVALID_5M | 99/3 | 99/0 |
| USELESS-EUR | 1077459 | -12.82% | INVALID_5M | 99/3 | 99/0 |
| OP-EUR | 985189 | +1.10% | INVALID_15M, INVALID_5M | 100/24 | 99/4 |
| FIL-EUR | 911276 | +0.79% | INVALID_15M, INVALID_5M | 100/15 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
