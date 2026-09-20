# Audit qualité des données Bitvavo

Scan : 2026-09-20T14:43:56.153557+00:00 (20260920T144226Z-7af24c2c)
Univers : 426 | strategy-grade : 31 | rejetés : 395
5m valides : 35 | 15m valides : 76 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 350 |
| MISSING_LATEST_CLOSED_CANDLE | 304 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 350 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| INJ-EUR | 2714427 | +4.37% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| FET-EUR | 2140334 | -6.25% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 1801846 | -4.25% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1424979 | -2.26% | INVALID_5M | 100/4 | 99/0 |
| UNI-EUR | 1422006 | -3.95% | INVALID_5M | 100/2 | 99/0 |
| WLD-EUR | 1414527 | -2.26% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 99/0 |
| CAKE-EUR | 1322085 | +2.39% | INVALID_5M | 100/2 | 99/0 |
| LSK-EUR | 1176487 | -14.64% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1063455 | -1.26% | INVALID_5M | 99/2 | 99/0 |
| ARB-EUR | 1063010 | -2.76% | INVALID_5M | 99/1 | 99/0 |
| FIL-EUR | 904625 | -7.20% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 92/8 | 99/4 |
| STX-EUR | 903119 | +0.19% | INVALID_15M, INVALID_5M | 100/9 | 99/2 |
| DOT-EUR | 847122 | -3.18% | INVALID_5M | 99/4 | 99/0 |
| SKL-EUR | 760756 | +4.90% | INVALID_5M | 99/3 | 99/0 |
| SHIB-EUR | 758493 | -3.00% | INVALID_5M | 99/5 | 99/0 |
| APT-EUR | 743750 | -2.77% | INVALID_5M | 99/4 | 99/0 |
| USELESS-EUR | 716676 | -7.38% | INVALID_5M | 100/3 | 99/0 |
| ZIL-EUR | 700041 | +5.73% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/10 | 99/0 |
| S-EUR | 678959 | +9.36% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 648843 | -2.80% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 92/12 | 99/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
