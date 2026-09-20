# Audit qualité des données Bitvavo

Scan : 2026-09-20T14:56:48.743336+00:00 (20260920T145525Z-ffb084ee)
Univers : 426 | strategy-grade : 34 | rejetés : 392
5m valides : 37 | 15m valides : 73 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 389 |
| INVALID_15M | 353 |
| MISSING_LATEST_CLOSED_CANDLE | 312 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 389 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 353 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| INJ-EUR | 2711875 | +4.95% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 1753396 | -4.07% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1430265 | -1.68% | INVALID_5M | 99/5 | 99/0 |
| UNI-EUR | 1419620 | -3.56% | INVALID_5M | 99/3 | 99/0 |
| WLD-EUR | 1399273 | -1.74% | INVALID_5M | 99/2 | 99/0 |
| CAKE-EUR | 1321071 | +2.33% | INVALID_5M | 100/3 | 99/0 |
| LTC-EUR | 1054636 | -0.92% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 99/0 |
| STRK-EUR | 966677 | +4.83% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 903101 | +1.71% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/9 | 100/2 |
| FIL-EUR | 902384 | -6.90% | INVALID_15M, INVALID_5M | 94/8 | 99/4 |
| DOT-EUR | 840660 | -2.69% | INVALID_5M | 99/4 | 99/0 |
| SKL-EUR | 763640 | +6.54% | INVALID_5M | 99/3 | 99/0 |
| SHIB-EUR | 753304 | -2.69% | INVALID_5M | 99/4 | 99/0 |
| APT-EUR | 737468 | -3.18% | INVALID_5M | 100/4 | 99/0 |
| CAP-EUR | 736627 | -7.80% | MISSING_LATEST_CLOSED_CANDLE | 100/0 | 99/0 |
| USELESS-EUR | 700270 | -7.39% | INVALID_5M | 100/4 | 99/0 |
| ZIL-EUR | 699080 | +6.46% | INVALID_15M, INVALID_5M | 99/12 | 99/1 |
| BCH-EUR | 653931 | -3.04% | INVALID_15M, INVALID_5M | 93/13 | 99/2 |
| DRIFT-EUR | 632888 | +6.66% | INVALID_15M | 99/0 | 99/1 |
| TIA-EUR | 585144 | -1.77% | INVALID_15M, INVALID_5M | 99/11 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
