# Audit qualité des données Bitvavo

Scan : 2026-09-19T11:32:26.276777+00:00 (20260919T113058Z-7c0b9b7a)
Univers : 427 | strategy-grade : 36 | rejetés : 391
5m valides : 36 | 15m valides : 77 | deux intervalles valides : 36

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 391 |
| INVALID_15M | 350 |
| MISSING_LATEST_CLOSED_CANDLE | 244 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 391 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 350 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| WLD-EUR | 2161018 | -1.29% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2040203 | +35.59% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1626163 | +3.83% | INVALID_5M | 99/2 | 99/0 |
| F-EUR | 1615756 | +28.26% | INVALID_5M | 99/4 | 99/0 |
| POL-EUR | 1600630 | +5.80% | INVALID_5M | 99/7 | 100/0 |
| SKY-EUR | 1419273 | +3.71% | INVALID_5M | 100/4 | 100/0 |
| AAVE-EUR | 1201182 | +6.47% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 1164306 | +4.47% | INVALID_5M | 99/1 | 100/0 |
| OP-EUR | 1107552 | +14.38% | INVALID_5M | 99/3 | 99/0 |
| BCH-EUR | 1062730 | +1.29% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/13 | 99/0 |
| SAGA-EUR | 986851 | +32.33% | INVALID_5M | 99/1 | 99/0 |
| LPT-EUR | 849850 | +6.89% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 99/0 |
| MORPHO-EUR | 848255 | +16.11% | INVALID_5M | 100/3 | 100/0 |
| COTI-EUR | 842526 | -1.23% | INVALID_5M | 100/4 | 100/0 |
| S-EUR | 815782 | +7.92% | INVALID_15M, INVALID_5M | 99/23 | 100/3 |
| C-EUR | 810615 | +15.15% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 99/0 |
| SUPER-EUR | 793949 | +7.30% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 80/20 | 100/2 |
| BNB-EUR | 792957 | +1.75% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| LAPTOP-EUR | 746548 | -17.99% | INVALID_5M | 99/2 | 99/0 |
| EPIC-EUR | 735359 | +25.80% | INVALID_5M | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
