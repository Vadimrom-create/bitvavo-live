# Audit qualité des données Bitvavo

Scan : 2026-09-20T19:25:20.958059+00:00 (20260920T192345Z-db8491b9)
Univers : 426 | strategy-grade : 39 | rejetés : 387
5m valides : 43 | 15m valides : 85 | deux intervalles valides : 39

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 383 |
| INVALID_15M | 341 |
| MISSING_LATEST_CLOSED_CANDLE | 256 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 383 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 341 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| CELR-EUR | 3252531 | +30.26% | INVALID_5M | 99/1 | 99/0 |
| USDC-EUR | 2898069 | +0.05% | INVALID_5M | 100/1 | 99/0 |
| INJ-EUR | 2841131 | -1.51% | INVALID_5M | 100/3 | 99/0 |
| G-EUR | 2797128 | -33.65% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1864108 | -0.49% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1683973 | +0.39% | INVALID_5M | 99/2 | 99/0 |
| CAKE-EUR | 1422440 | +5.09% | INVALID_5M | 100/6 | 99/0 |
| UNI-EUR | 1294896 | +0.92% | INVALID_5M | 100/2 | 99/0 |
| DOGE-EUR | 1239325 | -3.50% | INVALID_5M | 99/1 | 99/0 |
| SYN-EUR | 1175546 | -12.66% | INVALID_5M | 100/3 | 100/0 |
| S-EUR | 788592 | +16.81% | INVALID_5M | 99/1 | 99/0 |
| VET-EUR | 724437 | -3.53% | INVALID_5M | 99/1 | 99/0 |
| KMNO-EUR | 713488 | +14.76% | INVALID_15M | 99/0 | 99/2 |
| XPL-EUR | 686230 | -4.17% | INVALID_5M | 99/4 | 99/0 |
| AAVE-EUR | 667560 | -4.23% | INVALID_5M | 100/1 | 99/0 |
| ZIL-EUR | 666232 | +0.22% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/9 | 100/2 |
| FIL-EUR | 646945 | -9.46% | INVALID_5M | 100/4 | 99/0 |
| STX-EUR | 613465 | +3.37% | INVALID_15M, INVALID_5M | 99/3 | 100/1 |
| NPC-EUR | 575591 | +4.15% | INVALID_5M | 99/1 | 99/0 |
| TIA-EUR | 575041 | -0.55% | INVALID_15M, INVALID_5M | 100/6 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
