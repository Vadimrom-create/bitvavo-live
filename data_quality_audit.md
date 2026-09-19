# Audit qualité des données Bitvavo

Scan : 2026-09-19T07:46:40.131526+00:00 (20260919T074511Z-48a688c9)
Univers : 427 | strategy-grade : 36 | rejetés : 391
5m valides : 42 | 15m valides : 67 | deux intervalles valides : 36

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 385 |
| INVALID_15M | 360 |
| MISSING_LATEST_CLOSED_CANDLE | 255 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 385 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 360 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 4930582 | +4.55% | INVALID_5M | 99/2 | 100/0 |
| AVAX-EUR | 1706139 | +7.90% | INVALID_5M | 99/1 | 100/0 |
| POL-EUR | 1659259 | +2.83% | INVALID_5M | 99/2 | 100/0 |
| CNPY-EUR | 1608420 | +14.02% | INVALID_5M | 99/1 | 100/0 |
| F-EUR | 1560250 | +28.61% | INVALID_5M | 99/1 | 93/0 |
| SKY-EUR | 1415841 | +15.06% | INVALID_5M | 100/6 | 100/0 |
| HBAR-EUR | 1253467 | +2.80% | INVALID_15M, INVALID_5M | 99/2 | 100/1 |
| AAVE-EUR | 1110747 | +6.00% | INVALID_5M | 100/1 | 100/0 |
| RAY-EUR | 1101008 | +4.72% | INVALID_15M, INVALID_5M | 99/6 | 100/1 |
| OP-EUR | 1095876 | +11.53% | INVALID_5M | 100/3 | 100/0 |
| BCH-EUR | 1023204 | -1.10% | INVALID_15M, INVALID_5M | 99/2 | 100/2 |
| COTI-EUR | 991954 | -11.16% | INVALID_15M | 99/0 | 100/2 |
| LPT-EUR | 917844 | +8.48% | INVALID_5M | 99/6 | 99/0 |
| SAGA-EUR | 910415 | +19.95% | INVALID_5M | 100/9 | 100/0 |
| MORPHO-EUR | 851260 | +12.71% | INVALID_15M, INVALID_5M | 99/1 | 100/1 |
| BNB-EUR | 850228 | +0.53% | INVALID_15M, INVALID_5M | 100/7 | 100/1 |
| S-EUR | 842665 | +8.56% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/6 | 100/0 |
| XPL-EUR | 841450 | +0.03% | INVALID_15M, INVALID_5M | 100/15 | 100/2 |
| TIA-EUR | 817604 | +3.89% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/8 | 100/0 |
| SUPER-EUR | 786384 | +13.41% | INVALID_15M, INVALID_5M | 96/10 | 99/6 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
