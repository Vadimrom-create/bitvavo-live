# Audit qualité des données Bitvavo

Scan : 2026-09-19T15:47:03.135794+00:00 (20260919T154534Z-91acf78e)
Univers : 427 | strategy-grade : 34 | rejetés : 393
5m valides : 37 | 15m valides : 83 | deux intervalles valides : 34

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 390 |
| INVALID_15M | 344 |
| MISSING_LATEST_CLOSED_CANDLE | 243 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 390 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 344 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| SYN-EUR | 2520051 | +32.50% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2239193 | +20.75% | INVALID_5M | 99/2 | 99/0 |
| ARB-EUR | 2028268 | +0.69% | INVALID_5M | 100/1 | 100/0 |
| APT-EUR | 1856696 | +8.55% | INVALID_5M | 99/1 | 100/0 |
| CAP-EUR | 1650719 | -11.73% | INVALID_15M | 90/0 | 99/2 |
| POL-EUR | 1551324 | +5.18% | INVALID_5M | 100/5 | 100/0 |
| SAGA-EUR | 1351965 | +23.90% | INVALID_5M | 99/3 | 99/0 |
| OP-EUR | 1199523 | +12.05% | INVALID_5M | 100/9 | 100/0 |
| SKY-EUR | 1135491 | -1.88% | INVALID_5M | 99/6 | 100/0 |
| AAVE-EUR | 1097190 | +3.55% | INVALID_5M | 100/2 | 100/0 |
| DOT-EUR | 969815 | -0.99% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| BCH-EUR | 966151 | +1.65% | INVALID_5M | 99/3 | 99/0 |
| C-EUR | 891485 | +4.75% | INVALID_5M | 99/3 | 99/0 |
| COTI-EUR | 879072 | -2.44% | INVALID_5M | 99/1 | 100/0 |
| EPIC-EUR | 826591 | +28.60% | INVALID_5M | 99/4 | 99/0 |
| MORPHO-EUR | 778525 | +11.38% | INVALID_5M | 100/1 | 100/0 |
| HEI-EUR | 763437 | +15.81% | INVALID_5M | 99/4 | 100/0 |
| RAY-EUR | 752392 | +7.34% | INVALID_5M | 99/1 | 99/0 |
| BNB-EUR | 717354 | +1.66% | INVALID_5M | 99/1 | 99/0 |
| KAS-EUR | 703097 | +9.68% | INVALID_5M | 100/1 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
