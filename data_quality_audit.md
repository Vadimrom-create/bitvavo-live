# Audit qualité des données Bitvavo

Scan : 2026-09-20T04:22:03.391868+00:00 (20260920T042034Z-61c24a1f)
Univers : 427 | strategy-grade : 30 | rejetés : 397
5m valides : 32 | 15m valides : 58 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 395 |
| INVALID_15M | 369 |
| MISSING_LATEST_CLOSED_CANDLE | 297 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 395 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 369 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ONDO-EUR | 6145257 | -0.49% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2816311 | -2.69% | INVALID_5M | 99/2 | 99/0 |
| SYN-EUR | 2314638 | +15.98% | INVALID_5M | 99/1 | 99/0 |
| ZAMA-EUR | 2286859 | +39.80% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 2079584 | +0.75% | INVALID_5M | 100/4 | 99/0 |
| PUMP-EUR | 2038259 | -7.26% | INVALID_5M | 99/2 | 99/0 |
| CAP-EUR | 2003957 | -15.67% | INVALID_5M | 99/14 | 99/0 |
| UNI-EUR | 1918937 | -0.93% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1646948 | -2.72% | INVALID_5M | 100/4 | 99/0 |
| CNPY-EUR | 1455077 | -27.71% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1440922 | -2.72% | INVALID_5M | 100/6 | 99/0 |
| APT-EUR | 1219852 | -6.75% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/10 | 100/1 |
| EPIC-EUR | 1209825 | +16.72% | INVALID_15M, INVALID_5M | 100/6 | 99/3 |
| STRK-EUR | 1098645 | +11.40% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 1051936 | -15.55% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 933900 | +12.67% | INVALID_5M | 99/1 | 99/0 |
| FIL-EUR | 910836 | -2.80% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/18 | 100/1 |
| HEI-EUR | 896531 | +15.00% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/13 | 100/2 |
| BCH-EUR | 848346 | -0.63% | INVALID_15M, INVALID_5M | 91/27 | 99/4 |
| COTI-EUR | 794916 | -9.96% | INVALID_15M, INVALID_5M | 100/25 | 99/5 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
