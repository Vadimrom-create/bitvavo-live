# Audit qualité des données Bitvavo

Scan : 2026-09-19T07:32:38.269977+00:00 (20260919T073109Z-a392fb44)
Univers : 427 | strategy-grade : 30 | rejetés : 397
5m valides : 35 | 15m valides : 67 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 360 |
| MISSING_LATEST_CLOSED_CANDLE | 262 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 360 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 4973525 | +4.40% | INVALID_5M | 99/1 | 100/0 |
| WLD-EUR | 2408142 | -2.65% | INVALID_5M | 99/2 | 99/0 |
| PUMP-EUR | 2233547 | -4.18% | INVALID_5M | 99/1 | 99/0 |
| AVAX-EUR | 1722505 | +8.77% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1659953 | +3.30% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 100/0 |
| CNPY-EUR | 1613095 | +14.54% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1595759 | +3.11% | INVALID_5M | 99/1 | 99/0 |
| F-EUR | 1559591 | +28.27% | INVALID_5M | 99/1 | 92/0 |
| SKY-EUR | 1416721 | +14.55% | INVALID_5M | 99/6 | 100/0 |
| HBAR-EUR | 1252067 | +2.85% | INVALID_15M, INVALID_5M | 99/2 | 99/1 |
| RAY-EUR | 1119520 | +4.48% | INVALID_15M, INVALID_5M | 99/6 | 99/1 |
| AAVE-EUR | 1112027 | +5.62% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1094321 | +11.82% | INVALID_5M | 99/3 | 100/0 |
| BCH-EUR | 1024513 | -0.11% | INVALID_15M | 100/0 | 100/2 |
| COTI-EUR | 997169 | -12.65% | INVALID_15M, INVALID_5M | 99/3 | 99/2 |
| VET-EUR | 984402 | +15.38% | INVALID_5M | 99/1 | 99/0 |
| LPT-EUR | 914788 | +8.69% | INVALID_5M | 100/5 | 100/0 |
| SAGA-EUR | 907714 | +17.53% | INVALID_5M | 100/7 | 100/0 |
| BNB-EUR | 882520 | +0.65% | INVALID_15M, INVALID_5M | 99/6 | 99/1 |
| MORPHO-EUR | 865287 | +14.29% | INVALID_15M, INVALID_5M | 99/1 | 100/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
