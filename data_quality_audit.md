# Audit qualité des données Bitvavo

Scan : 2026-09-19T23:19:31.775862+00:00 (20260919T231758Z-21f6eefe)
Univers : 427 | strategy-grade : 30 | rejetés : 397
5m valides : 32 | 15m valides : 76 | deux intervalles valides : 31

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 395 |
| INVALID_15M | 351 |
| MISSING_LATEST_CLOSED_CANDLE | 286 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 395 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 351 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XLM-EUR | 2799949 | +2.02% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| USDC-EUR | 2654304 | -0.03% | INVALID_5M | 99/3 | 99/0 |
| CAP-EUR | 2031070 | -16.25% | INVALID_5M | 99/4 | 99/0 |
| PUMP-EUR | 1813125 | -0.80% | INVALID_5M | 99/5 | 99/0 |
| APT-EUR | 1600338 | -0.27% | INVALID_15M, INVALID_5M | 99/2 | 99/1 |
| DOGE-EUR | 1587154 | +0.02% | INVALID_5M | 99/1 | 100/0 |
| LTC-EUR | 1530539 | +0.08% | INVALID_5M | 99/2 | 99/0 |
| STRK-EUR | 1402588 | +0.98% | INVALID_5M | 98/3 | 99/0 |
| OP-EUR | 1231422 | +2.13% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/9 | 100/0 |
| EPIC-EUR | 1228393 | +12.26% | INVALID_5M | 99/1 | 100/0 |
| SKY-EUR | 1031164 | -0.61% | INVALID_15M, INVALID_5M | 99/10 | 99/4 |
| POL-EUR | 989821 | -2.36% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/7 | 99/0 |
| FIL-EUR | 901011 | +3.67% | INVALID_5M | 99/4 | 99/0 |
| DOT-EUR | 887871 | -0.82% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| HEI-EUR | 874175 | +13.22% | INVALID_15M, INVALID_5M | 100/11 | 100/1 |
| AAVE-EUR | 873278 | +2.13% | INVALID_5M | 99/4 | 99/0 |
| STX-EUR | 835100 | +9.22% | INVALID_5M | 98/1 | 99/0 |
| SAGA-EUR | 809251 | +1.23% | INVALID_15M, INVALID_5M | 100/17 | 100/1 |
| COTI-EUR | 796334 | -10.46% | INVALID_5M | 99/11 | 99/0 |
| KAS-EUR | 778730 | +3.43% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/9 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
