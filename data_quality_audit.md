# Audit qualité des données Bitvavo

Scan : 2026-09-19T17:16:06.516238+00:00 (20260919T171441Z-b67068e5)
Univers : 427 | strategy-grade : 36 | rejetés : 391
5m valides : 38 | 15m valides : 89 | deux intervalles valides : 36

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 389 |
| INVALID_15M | 338 |
| MISSING_LATEST_CLOSED_CANDLE | 236 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 389 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 338 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| STRK-EUR | 2179239 | +17.54% | INVALID_5M | 99/1 | 100/0 |
| APT-EUR | 1858694 | +6.59% | INVALID_5M | 100/2 | 100/0 |
| CAP-EUR | 1809277 | -16.05% | INVALID_15M | 99/0 | 100/2 |
| POL-EUR | 1538657 | +3.80% | INVALID_5M | 99/3 | 100/0 |
| LTC-EUR | 1526662 | +3.36% | INVALID_5M | 100/1 | 100/0 |
| HBAR-EUR | 1439898 | +4.85% | INVALID_5M | 99/1 | 100/0 |
| WLD-EUR | 1422370 | +5.63% | INVALID_5M | 99/1 | 100/0 |
| OP-EUR | 1206327 | +8.99% | INVALID_5M | 99/8 | 100/0 |
| F-EUR | 1105428 | -15.27% | INVALID_5M | 100/5 | 100/0 |
| VET-EUR | 1087459 | +10.78% | INVALID_5M | 99/1 | 100/0 |
| SKY-EUR | 1062687 | +0.48% | INVALID_15M, INVALID_5M | 100/7 | 100/1 |
| DOT-EUR | 945463 | +0.33% | INVALID_5M | 100/2 | 100/0 |
| AAVE-EUR | 916805 | +3.92% | INVALID_5M | 99/7 | 100/0 |
| COTI-EUR | 902294 | -2.03% | INVALID_5M | 99/1 | 100/0 |
| BCH-EUR | 889582 | +3.20% | INVALID_5M | 99/4 | 100/0 |
| KAS-EUR | 804899 | +9.08% | INVALID_5M | 99/1 | 100/0 |
| MORPHO-EUR | 801570 | +11.92% | INVALID_5M | 100/3 | 100/0 |
| HEI-EUR | 778025 | +13.03% | INVALID_5M | 99/3 | 100/0 |
| JUP-EUR | 743539 | +6.09% | INVALID_5M | 99/7 | 100/0 |
| LAPTOP-EUR | 648430 | -9.58% | INVALID_5M | 100/1 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
