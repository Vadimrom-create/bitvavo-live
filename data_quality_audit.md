# Audit qualité des données Bitvavo

Scan : 2026-09-19T13:46:15.883856+00:00 (20260919T134445Z-6b32a683)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 33 | 15m valides : 85 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 394 |
| INVALID_15M | 342 |
| MISSING_LATEST_CLOSED_CANDLE | 256 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 394 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 342 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 3040203 | +1.43% | INVALID_5M | 99/1 | 100/0 |
| ENA-EUR | 2625693 | +18.98% | INVALID_5M | 99/1 | 100/0 |
| G-EUR | 2563837 | +6.17% | INVALID_5M | 99/3 | 99/0 |
| LSK-EUR | 2179072 | -7.40% | INVALID_5M | 99/1 | 100/0 |
| APT-EUR | 1783607 | +5.25% | INVALID_5M | 99/3 | 100/0 |
| F-EUR | 1631432 | +27.30% | INVALID_5M | 99/1 | 100/0 |
| POL-EUR | 1623938 | +4.74% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/2 | 100/0 |
| SKY-EUR | 1407347 | +3.90% | INVALID_5M | 99/9 | 99/0 |
| AAVE-EUR | 1192765 | +0.89% | INVALID_5M | 99/1 | 100/0 |
| OP-EUR | 1180236 | +9.74% | INVALID_5M | 99/2 | 100/0 |
| DOT-EUR | 1019145 | -3.28% | INVALID_5M | 100/2 | 100/0 |
| BCH-EUR | 981391 | -0.16% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/8 | 100/0 |
| RAY-EUR | 871775 | +6.57% | INVALID_5M | 99/1 | 100/0 |
| HEI-EUR | 867191 | +27.54% | INVALID_5M | 99/1 | 100/0 |
| C-EUR | 839316 | +15.41% | INVALID_5M | 100/7 | 100/0 |
| MORPHO-EUR | 810810 | +12.26% | INVALID_5M | 100/7 | 100/0 |
| LPT-EUR | 804926 | +4.67% | INVALID_5M | 99/5 | 100/0 |
| COTI-EUR | 800117 | -4.44% | INVALID_5M | 99/2 | 100/0 |
| BNB-EUR | 797460 | +1.39% | INVALID_5M | 99/3 | 100/0 |
| CAP-EUR | 770121 | -0.04% | INVALID_15M, INVALID_5M | 99/4 | 100/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
