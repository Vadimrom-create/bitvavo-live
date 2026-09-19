# Audit qualité des données Bitvavo

Scan : 2026-09-19T09:08:13.445056+00:00 (20260919T090641Z-23342b10)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 35 | 15m valides : 73 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 354 |
| MISSING_LATEST_CLOSED_CANDLE | 255 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 354 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 4705448 | +3.36% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 2095914 | -2.74% | INVALID_5M | 99/1 | 99/0 |
| USELESS-EUR | 1947962 | +3.26% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1731198 | +8.15% | INVALID_5M | 99/2 | 99/0 |
| F-EUR | 1591135 | +25.27% | INVALID_5M | 99/3 | 96/0 |
| POL-EUR | 1589883 | +3.73% | INVALID_5M | 100/3 | 99/0 |
| CNPY-EUR | 1470719 | +5.19% | INVALID_5M | 99/2 | 99/0 |
| SKY-EUR | 1460500 | +15.80% | INVALID_5M | 99/7 | 99/0 |
| HBAR-EUR | 1193690 | +2.45% | INVALID_5M | 99/2 | 99/0 |
| AAVE-EUR | 1140767 | +8.26% | INVALID_5M | 99/2 | 99/0 |
| OP-EUR | 1103206 | +9.92% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |
| BCH-EUR | 1030607 | -0.94% | INVALID_15M, INVALID_5M | 100/6 | 99/2 |
| SAGA-EUR | 926110 | +19.79% | INVALID_5M | 100/3 | 99/0 |
| LPT-EUR | 894366 | +8.02% | INVALID_5M | 100/8 | 99/0 |
| COTI-EUR | 893575 | -7.45% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| BNB-EUR | 859636 | +1.77% | INVALID_15M, INVALID_5M | 99/7 | 99/1 |
| S-EUR | 827000 | +7.69% | INVALID_5M | 99/9 | 99/0 |
| MORPHO-EUR | 825909 | +18.18% | INVALID_15M, INVALID_5M | 99/2 | 99/1 |
| SUPER-EUR | 800228 | +10.44% | INVALID_15M, INVALID_5M | 94/6 | 99/6 |
| C-EUR | 794726 | +14.56% | INVALID_5M | 100/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
