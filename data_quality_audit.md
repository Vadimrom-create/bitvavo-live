# Audit qualité des données Bitvavo

Scan : 2026-09-19T16:00:12.971896+00:00 (20260919T155837Z-65496227)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 36 | 15m valides : 83 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 344 |
| MISSING_LATEST_CLOSED_CANDLE | 206 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 344 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| SYN-EUR | 2517883 | +31.17% | INVALID_5M | 100/1 | 100/0 |
| STRK-EUR | 2235634 | +18.89% | INVALID_5M | 100/2 | 100/0 |
| ARB-EUR | 2027731 | -0.81% | INVALID_5M | 99/1 | 100/0 |
| APT-EUR | 1867726 | +7.34% | INVALID_5M | 99/1 | 100/0 |
| CAP-EUR | 1677821 | -13.11% | INVALID_15M | 92/0 | 100/2 |
| POL-EUR | 1546946 | +4.94% | INVALID_5M | 100/5 | 100/0 |
| HBAR-EUR | 1395597 | +2.66% | INVALID_5M | 99/1 | 100/0 |
| SAGA-EUR | 1355511 | +22.69% | INVALID_5M | 100/3 | 100/0 |
| OP-EUR | 1201607 | +11.87% | INVALID_5M | 99/10 | 100/0 |
| SKY-EUR | 1127918 | -1.35% | INVALID_5M | 99/6 | 100/0 |
| AAVE-EUR | 1096883 | +2.50% | INVALID_5M | 100/3 | 100/0 |
| BCH-EUR | 973679 | +1.21% | INVALID_5M | 100/3 | 100/0 |
| DOT-EUR | 960773 | -1.14% | INVALID_5M | 100/3 | 100/0 |
| COTI-EUR | 873979 | -1.97% | INVALID_5M | 100/2 | 100/0 |
| EPIC-EUR | 845485 | +28.37% | INVALID_5M | 99/3 | 100/0 |
| JUP-EUR | 778928 | +6.49% | INVALID_5M | 100/1 | 100/0 |
| MORPHO-EUR | 778611 | +11.30% | INVALID_5M | 99/2 | 100/0 |
| HEI-EUR | 757172 | +17.29% | INVALID_5M | 100/4 | 100/0 |
| RAY-EUR | 744404 | +6.88% | INVALID_5M | 100/1 | 100/0 |
| KAS-EUR | 709610 | +9.29% | INVALID_5M | 99/1 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
