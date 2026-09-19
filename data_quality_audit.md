# Audit qualité des données Bitvavo

Scan : 2026-09-19T11:45:49.873061+00:00 (20260919T114419Z-c97362f6)
Univers : 427 | strategy-grade : 35 | rejetés : 392
5m valides : 36 | 15m valides : 80 | deux intervalles valides : 36

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 347 |
| MISSING_LATEST_CLOSED_CANDLE | 201 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 347 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| G-EUR | 2881785 | +0.82% | MISSING_LATEST_CLOSED_CANDLE | 100/0 | 100/0 |
| WLD-EUR | 2153045 | -2.26% | INVALID_5M | 99/1 | 100/0 |
| STRK-EUR | 2080464 | +35.94% | INVALID_5M | 99/2 | 100/0 |
| LTC-EUR | 1657840 | +5.13% | INVALID_5M | 99/2 | 100/0 |
| F-EUR | 1619780 | +28.40% | INVALID_5M | 100/4 | 100/0 |
| POL-EUR | 1599820 | +5.61% | INVALID_5M | 99/6 | 100/0 |
| SKY-EUR | 1391145 | +4.28% | INVALID_5M | 100/5 | 100/0 |
| HBAR-EUR | 1203075 | +3.93% | INVALID_5M | 99/1 | 100/0 |
| AAVE-EUR | 1199166 | +6.17% | INVALID_5M | 99/1 | 100/0 |
| OP-EUR | 1115476 | +14.06% | INVALID_5M | 99/3 | 100/0 |
| BCH-EUR | 1065580 | +1.69% | INVALID_5M | 99/11 | 100/0 |
| SAGA-EUR | 987687 | +33.18% | INVALID_5M | 99/1 | 100/0 |
| LPT-EUR | 849660 | +6.67% | INVALID_5M | 99/6 | 100/0 |
| MORPHO-EUR | 848902 | +15.35% | INVALID_5M | 100/3 | 100/0 |
| COTI-EUR | 847612 | -0.67% | INVALID_5M | 100/4 | 100/0 |
| S-EUR | 817875 | +6.48% | INVALID_15M, INVALID_5M | 99/20 | 100/3 |
| C-EUR | 810564 | +15.08% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| BNB-EUR | 804465 | +1.97% | INVALID_15M, INVALID_5M | 99/1 | 100/1 |
| SUPER-EUR | 792428 | +7.28% | INVALID_15M, INVALID_5M | 80/24 | 100/3 |
| LAPTOP-EUR | 747812 | -18.27% | INVALID_5M | 100/2 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
