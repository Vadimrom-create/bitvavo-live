# Audit qualité des données Bitvavo

Scan : 2026-09-19T22:49:06.323693+00:00 (20260919T224732Z-a4562d19)
Univers : 427 | strategy-grade : 31 | rejetés : 396
5m valides : 33 | 15m valides : 76 | deux intervalles valides : 32

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 394 |
| INVALID_15M | 351 |
| MISSING_LATEST_CLOSED_CANDLE | 265 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 394 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 351 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| USDC-EUR | 2662122 | -0.05% | INVALID_5M | 99/4 | 99/0 |
| UNI-EUR | 2159645 | -1.96% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 2027902 | -15.98% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 1861139 | -1.21% | INVALID_5M | 99/3 | 99/0 |
| APT-EUR | 1655507 | +0.89% | INVALID_15M, INVALID_5M | 99/4 | 100/1 |
| LTC-EUR | 1499017 | -0.79% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| STRK-EUR | 1403537 | +0.10% | INVALID_5M | 99/3 | 99/0 |
| CNPY-EUR | 1403482 | -21.91% | INVALID_5M | 99/1 | 100/0 |
| ARB-EUR | 1252231 | -5.87% | INVALID_5M | 99/1 | 100/0 |
| OP-EUR | 1225083 | +1.49% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/5 | 100/0 |
| SKY-EUR | 1035324 | -1.20% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/11 | 99/4 |
| POL-EUR | 1022672 | -1.40% | INVALID_5M | 99/6 | 100/0 |
| FIL-EUR | 890795 | +4.11% | INVALID_5M | 99/4 | 99/0 |
| AAVE-EUR | 879926 | +2.31% | INVALID_5M | 99/2 | 99/0 |
| HEI-EUR | 871288 | +12.88% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/7 | 100/0 |
| DOT-EUR | 870436 | -0.86% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| MORPHO-EUR | 840722 | +6.28% | INVALID_15M, INVALID_5M | 99/3 | 99/1 |
| STX-EUR | 830874 | +8.53% | INVALID_5M | 99/1 | 99/0 |
| SAGA-EUR | 811394 | +1.27% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/9 | 99/0 |
| COTI-EUR | 801409 | -11.12% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/9 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
