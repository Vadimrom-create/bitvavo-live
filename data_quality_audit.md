# Audit qualité des données Bitvavo

Scan : 2026-09-20T13:40:11.208153+00:00 (20260920T133841Z-8a3263e8)
Univers : 426 | strategy-grade : 34 | rejetés : 392
5m valides : 36 | 15m valides : 77 | deux intervalles valides : 34

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 390 |
| INVALID_15M | 349 |
| MISSING_LATEST_CLOSED_CANDLE | 249 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 390 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 349 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| FET-EUR | 2135010 | -6.21% | INVALID_5M | 100/1 | 99/0 |
| UNI-EUR | 1521728 | -4.22% | INVALID_5M | 100/3 | 99/0 |
| WLD-EUR | 1442913 | -2.73% | INVALID_5M | 99/5 | 99/0 |
| PUMP-EUR | 1366560 | -2.53% | INVALID_5M | 99/5 | 99/0 |
| CAKE-EUR | 1300329 | +3.37% | INVALID_5M | 100/5 | 99/0 |
| LSK-EUR | 1232638 | -13.97% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1118122 | -1.90% | INVALID_5M | 100/5 | 99/0 |
| ARB-EUR | 1072177 | +0.72% | INVALID_5M | 100/2 | 99/0 |
| STX-EUR | 890973 | -1.71% | INVALID_15M, INVALID_5M | 100/17 | 99/2 |
| FIL-EUR | 882872 | -7.47% | INVALID_15M, INVALID_5M | 86/28 | 99/4 |
| DOT-EUR | 834143 | -3.22% | INVALID_5M | 100/3 | 99/0 |
| APT-EUR | 804410 | -2.05% | INVALID_5M | 100/4 | 99/0 |
| SHIB-EUR | 779333 | -2.26% | INVALID_5M | 100/2 | 99/0 |
| USELESS-EUR | 753907 | -3.06% | INVALID_5M | 100/3 | 99/0 |
| SKL-EUR | 739526 | +6.62% | INVALID_5M | 100/2 | 99/0 |
| BCH-EUR | 738434 | -2.44% | INVALID_15M, INVALID_5M | 90/12 | 99/2 |
| ZIL-EUR | 704552 | +7.21% | INVALID_5M | 100/2 | 99/0 |
| DRIFT-EUR | 666299 | +6.24% | INVALID_15M, INVALID_5M | 99/8 | 99/1 |
| S-EUR | 645866 | +6.58% | INVALID_5M | 99/2 | 99/0 |
| TIA-EUR | 584111 | -1.34% | INVALID_5M | 99/6 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
