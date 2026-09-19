# Audit qualité des données Bitvavo

Scan : 2026-09-19T05:58:39.688793+00:00 (20260919T055635Z-2ddd5a55)
Univers : 427 | strategy-grade : 27 | rejetés : 400
5m valides : 29 | 15m valides : 65 | deux intervalles valides : 28

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 398 |
| INVALID_15M | 362 |
| MISSING_LATEST_CLOSED_CANDLE | 281 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 398 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 362 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 5168874 | +5.30% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 2537404 | +1.83% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 2495646 | -4.86% | INVALID_5M | 99/2 | 99/0 |
| USDC-EUR | 2471055 | -0.21% | INVALID_5M | 99/1 | 99/0 |
| INJ-EUR | 2059107 | +18.11% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1703455 | +12.21% | INVALID_5M | 99/1 | 99/0 |
| AVAX-EUR | 1672328 | +7.57% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1631425 | +4.85% | INVALID_5M | 99/2 | 99/0 |
| POL-EUR | 1608849 | +3.75% | INVALID_5M | 99/6 | 99/0 |
| F-EUR | 1536163 | +29.90% | INVALID_5M | 99/2 | 86/0 |
| SKY-EUR | 1368096 | +15.72% | INVALID_5M | 99/10 | 99/0 |
| DOT-EUR | 1297035 | +0.35% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 1236517 | +3.68% | INVALID_15M, INVALID_5M | 99/14 | 99/1 |
| RAY-EUR | 1231528 | +4.72% | INVALID_15M, INVALID_5M | 99/7 | 99/1 |
| COTI-EUR | 1130892 | -9.63% | INVALID_15M, INVALID_5M | 99/12 | 99/2 |
| BCH-EUR | 985396 | -0.12% | INVALID_15M, INVALID_5M | 99/2 | 99/2 |
| BNB-EUR | 982966 | +1.30% | INVALID_15M, INVALID_5M | 99/1 | 99/1 |
| LPT-EUR | 967595 | +10.38% | INVALID_15M, INVALID_5M | 99/6 | 99/1 |
| SAGA-EUR | 911866 | +21.10% | INVALID_5M | 99/7 | 99/0 |
| VET-EUR | 866084 | +9.90% | INVALID_5M | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
