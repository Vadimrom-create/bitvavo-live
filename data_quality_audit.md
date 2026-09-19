# Audit qualité des données Bitvavo

Scan : 2026-09-19T09:26:00.024411+00:00 (20260919T092433Z-2505331c)
Univers : 427 | strategy-grade : 31 | rejetés : 396
5m valides : 36 | 15m valides : 75 | deux intervalles valides : 32

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 352 |
| MISSING_LATEST_CLOSED_CANDLE | 267 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 352 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 4669766 | +2.26% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 2113692 | -2.77% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 1943394 | +4.69% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1761794 | +7.99% | INVALID_5M | 100/2 | 99/0 |
| POL-EUR | 1594231 | +3.99% | INVALID_5M | 99/4 | 99/0 |
| F-EUR | 1593426 | +27.51% | INVALID_5M | 100/2 | 97/0 |
| SKY-EUR | 1472256 | +15.50% | INVALID_5M | 99/5 | 99/0 |
| CNPY-EUR | 1437437 | +4.76% | INVALID_5M | 99/2 | 99/0 |
| DOT-EUR | 1253760 | -3.21% | INVALID_5M | 100/1 | 99/0 |
| HBAR-EUR | 1168562 | +2.51% | INVALID_5M | 99/1 | 99/0 |
| AAVE-EUR | 1141472 | +7.87% | INVALID_5M | 100/1 | 99/0 |
| OP-EUR | 1083427 | +9.25% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 1033265 | +0.29% | INVALID_15M, INVALID_5M | 100/7 | 99/1 |
| SAGA-EUR | 932846 | +23.02% | INVALID_5M | 99/4 | 99/0 |
| LPT-EUR | 889991 | +7.12% | INVALID_5M | 100/8 | 99/0 |
| COTI-EUR | 885238 | -6.93% | INVALID_15M, INVALID_5M | 100/1 | 99/1 |
| BNB-EUR | 862698 | +1.61% | INVALID_15M, INVALID_5M | 99/3 | 99/1 |
| MORPHO-EUR | 839241 | +17.52% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| S-EUR | 824002 | +6.82% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/10 | 99/0 |
| SUPER-EUR | 799574 | +10.19% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 92/6 | 100/4 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
