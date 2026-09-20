# Audit qualité des données Bitvavo

Scan : 2026-09-20T01:03:24.302620+00:00 (20260920T010124Z-17b64a34)
Univers : 427 | strategy-grade : 21 | rejetés : 406
5m valides : 22 | 15m valides : 66 | deux intervalles valides : 21

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 405 |
| INVALID_15M | 361 |
| MISSING_LATEST_CLOSED_CANDLE | 277 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 405 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 361 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 9319700 | -0.94% | INVALID_5M | 99/2 | 99/0 |
| XLM-EUR | 2767177 | +0.66% | INVALID_5M | 99/2 | 99/0 |
| USDC-EUR | 2693442 | +0.05% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 2065968 | -1.20% | INVALID_5M | 99/6 | 99/0 |
| CAP-EUR | 1999752 | -11.32% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 1758740 | -0.03% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/6 | 100/0 |
| DOGE-EUR | 1611667 | -0.41% | INVALID_5M | 99/3 | 100/0 |
| HBAR-EUR | 1568950 | +4.06% | INVALID_5M | 99/3 | 99/0 |
| LTC-EUR | 1459380 | -0.15% | INVALID_5M | 100/6 | 100/0 |
| CNPY-EUR | 1434769 | -21.01% | INVALID_5M | 99/2 | 99/0 |
| WLD-EUR | 1429126 | +1.37% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1425678 | -1.04% | INVALID_15M, INVALID_5M | 99/4 | 99/1 |
| STRK-EUR | 1288904 | +4.74% | INVALID_5M | 99/1 | 99/0 |
| EPIC-EUR | 1223383 | +8.27% | INVALID_5M | 100/1 | 100/0 |
| USELESS-EUR | 1123541 | -14.15% | INVALID_5M | 100/1 | 100/0 |
| OP-EUR | 1087615 | +2.26% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/20 | 100/2 |
| ARB-EUR | 1050920 | -7.79% | INVALID_5M | 99/3 | 99/0 |
| SKY-EUR | 957444 | -2.34% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 95/16 | 99/3 |
| FIL-EUR | 916927 | +2.45% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 99/0 |
| HEI-EUR | 886251 | +12.56% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/20 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
