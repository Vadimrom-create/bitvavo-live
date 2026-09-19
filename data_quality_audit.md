# Audit qualité des données Bitvavo

Scan : 2026-09-19T10:30:08.309414+00:00 (20260919T102843Z-5f29404a)
Univers : 427 | strategy-grade : 31 | rejetés : 396
5m valides : 32 | 15m valides : 82 | deux intervalles valides : 31

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 395 |
| INVALID_15M | 345 |
| MISSING_LATEST_CLOSED_CANDLE | 210 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 395 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 345 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| PUMP-EUR | 2478637 | -1.93% | INVALID_5M | 99/1 | 100/0 |
| WLD-EUR | 2291549 | -3.09% | INVALID_5M | 99/1 | 100/0 |
| STRK-EUR | 2107626 | +25.13% | INVALID_5M | 99/2 | 100/0 |
| APT-EUR | 1761110 | +9.59% | INVALID_5M | 100/1 | 100/0 |
| F-EUR | 1604232 | +28.87% | INVALID_5M | 100/3 | 100/0 |
| POL-EUR | 1579108 | +3.80% | INVALID_5M | 100/5 | 100/0 |
| SKY-EUR | 1502522 | +12.01% | INVALID_5M | 100/5 | 100/0 |
| CNPY-EUR | 1478741 | +0.84% | INVALID_5M | 100/1 | 100/0 |
| DOT-EUR | 1193481 | -2.27% | INVALID_5M | 100/1 | 100/0 |
| HBAR-EUR | 1135175 | +2.56% | INVALID_5M | 99/2 | 100/0 |
| AAVE-EUR | 1131685 | +6.15% | INVALID_5M | 100/1 | 100/0 |
| OP-EUR | 1103061 | +11.95% | INVALID_5M | 100/4 | 100/0 |
| BCH-EUR | 1073257 | +0.18% | INVALID_5M | 100/9 | 100/0 |
| SAGA-EUR | 951918 | +28.34% | INVALID_5M | 100/1 | 100/0 |
| LPT-EUR | 891697 | +6.29% | INVALID_5M | 100/6 | 100/0 |
| COTI-EUR | 876125 | -7.20% | INVALID_5M | 100/5 | 100/0 |
| MORPHO-EUR | 849639 | +16.65% | INVALID_5M | 100/1 | 100/0 |
| S-EUR | 812945 | +6.13% | INVALID_15M, INVALID_5M | 100/19 | 100/2 |
| BNB-EUR | 812667 | +1.88% | INVALID_15M, INVALID_5M | 100/1 | 100/1 |
| SUPER-EUR | 805052 | +8.65% | INVALID_15M, INVALID_5M | 85/14 | 100/4 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
