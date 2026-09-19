# Audit qualité des données Bitvavo

Scan : 2026-09-19T07:17:14.238362+00:00 (20260919T071538Z-50bc7775)
Univers : 427 | strategy-grade : 30 | rejetés : 397
5m valides : 35 | 15m valides : 66 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 361 |
| MISSING_LATEST_CLOSED_CANDLE | 259 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 361 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 5072451 | +6.66% | INVALID_5M | 99/1 | 100/0 |
| WLD-EUR | 2430324 | -2.43% | INVALID_5M | 99/2 | 100/0 |
| PUMP-EUR | 2249873 | -5.10% | INVALID_5M | 99/1 | 100/0 |
| INJ-EUR | 2219493 | +24.53% | INVALID_5M | 99/1 | 99/0 |
| AVAX-EUR | 1684333 | +7.64% | INVALID_5M | 99/1 | 100/0 |
| POL-EUR | 1663363 | +3.27% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1609729 | +3.90% | INVALID_5M | 99/1 | 100/0 |
| F-EUR | 1559897 | +27.67% | INVALID_5M | 99/1 | 91/0 |
| SKY-EUR | 1418952 | +14.17% | INVALID_5M | 99/6 | 99/0 |
| HBAR-EUR | 1250748 | +3.00% | INVALID_15M, INVALID_5M | 99/2 | 100/1 |
| DOT-EUR | 1249056 | -3.20% | INVALID_5M | 99/1 | 99/0 |
| AAVE-EUR | 1126135 | +6.34% | INVALID_5M | 99/1 | 100/0 |
| RAY-EUR | 1118887 | +5.57% | INVALID_15M, INVALID_5M | 99/8 | 99/1 |
| OP-EUR | 1094059 | +12.87% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 100/0 |
| BCH-EUR | 1026145 | +0.31% | INVALID_15M, INVALID_5M | 100/1 | 100/2 |
| COTI-EUR | 950859 | -11.18% | INVALID_15M, INVALID_5M | 99/3 | 100/2 |
| VET-EUR | 942397 | +11.38% | INVALID_5M | 99/1 | 99/0 |
| LPT-EUR | 926854 | +8.06% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 100/0 |
| SAGA-EUR | 910525 | +15.81% | INVALID_5M | 99/8 | 99/0 |
| BNB-EUR | 895527 | +0.31% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/5 | 100/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
