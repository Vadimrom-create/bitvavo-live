# Audit qualité des données Bitvavo

Scan : 2026-09-20T04:00:38.068198+00:00 (20260920T035903Z-b9ea243d)
Univers : 427 | strategy-grade : 29 | rejetés : 398
5m valides : 31 | 15m valides : 57 | deux intervalles valides : 29

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 396 |
| INVALID_15M | 370 |
| MISSING_LATEST_CLOSED_CANDLE | 246 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 396 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 370 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2821796 | -1.98% | INVALID_5M | 100/2 | 100/0 |
| SYN-EUR | 2312542 | +14.01% | INVALID_5M | 99/1 | 100/0 |
| ZAMA-EUR | 2266492 | +36.73% | INVALID_5M | 99/1 | 100/0 |
| HBAR-EUR | 2066204 | +1.06% | INVALID_5M | 99/3 | 100/0 |
| PUMP-EUR | 2020685 | -6.71% | INVALID_5M | 99/2 | 100/0 |
| CAP-EUR | 2004519 | -15.62% | INVALID_5M | 100/12 | 100/0 |
| UNI-EUR | 1952911 | -1.28% | INVALID_5M | 100/1 | 100/0 |
| DOGE-EUR | 1652764 | -2.64% | INVALID_5M | 99/3 | 100/0 |
| LTC-EUR | 1430323 | -2.86% | INVALID_5M | 99/8 | 100/0 |
| VET-EUR | 1344680 | +6.92% | INVALID_5M | 99/3 | 100/0 |
| APT-EUR | 1243417 | -6.28% | INVALID_15M, INVALID_5M | 99/10 | 100/1 |
| EPIC-EUR | 1211601 | +14.14% | INVALID_15M, INVALID_5M | 100/14 | 100/3 |
| ARB-EUR | 1167120 | +1.40% | INVALID_5M | 99/1 | 100/0 |
| STRK-EUR | 1165856 | -1.92% | INVALID_5M | 99/2 | 100/0 |
| USELESS-EUR | 1058856 | -15.78% | INVALID_5M | 100/2 | 100/0 |
| STX-EUR | 932581 | +12.94% | INVALID_5M | 99/1 | 100/0 |
| FIL-EUR | 922986 | -2.76% | INVALID_15M, INVALID_5M | 99/18 | 100/1 |
| HEI-EUR | 894248 | +12.93% | INVALID_15M, INVALID_5M | 100/14 | 100/2 |
| OP-EUR | 876867 | -2.72% | INVALID_15M, INVALID_5M | 99/2 | 100/4 |
| SKY-EUR | 802700 | -3.69% | INVALID_15M, INVALID_5M | 89/13 | 100/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
