# Audit qualité des données Bitvavo

Scan : 2026-09-19T15:34:16.525291+00:00 (20260919T153244Z-b9ad89f5)
Univers : 427 | strategy-grade : 32 | rejetés : 395
5m valides : 34 | 15m valides : 84 | deux intervalles valides : 32

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 393 |
| INVALID_15M | 343 |
| MISSING_LATEST_CLOSED_CANDLE | 238 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 393 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 343 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| SYN-EUR | 2504396 | +35.07% | INVALID_5M | 98/1 | 99/0 |
| STRK-EUR | 2250993 | +20.48% | INVALID_5M | 99/2 | 99/0 |
| ARB-EUR | 2027982 | +0.05% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1834048 | +9.62% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 1619113 | -9.08% | INVALID_15M | 88/0 | 99/2 |
| POL-EUR | 1566423 | +4.83% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 99/0 |
| SAGA-EUR | 1344383 | +25.08% | INVALID_5M | 99/3 | 99/0 |
| OP-EUR | 1201390 | +11.12% | INVALID_5M | 99/8 | 99/0 |
| SKY-EUR | 1164402 | -2.48% | INVALID_5M | 100/5 | 100/0 |
| AAVE-EUR | 1096203 | +3.30% | INVALID_5M | 99/2 | 99/0 |
| DOT-EUR | 977932 | -1.30% | INVALID_5M | 99/3 | 99/0 |
| BCH-EUR | 954736 | +0.75% | INVALID_5M | 99/3 | 99/0 |
| C-EUR | 897596 | +7.66% | INVALID_5M | 99/4 | 99/0 |
| COTI-EUR | 866116 | -2.62% | INVALID_5M | 99/3 | 99/0 |
| EPIC-EUR | 820253 | +27.34% | INVALID_5M | 99/4 | 99/0 |
| JUP-EUR | 781046 | +8.18% | INVALID_5M | 99/3 | 99/0 |
| MORPHO-EUR | 775520 | +10.50% | INVALID_5M | 99/2 | 99/0 |
| HEI-EUR | 771107 | +15.49% | INVALID_5M | 99/4 | 99/0 |
| RAY-EUR | 764896 | +5.86% | INVALID_5M | 99/2 | 99/0 |
| BNB-EUR | 735375 | +1.31% | INVALID_5M | 99/2 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
