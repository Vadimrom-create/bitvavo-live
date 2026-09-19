# Audit qualité des données Bitvavo

Scan : 2026-09-19T04:43:22.522962+00:00 (20260919T044152Z-07f23b12)
Univers : 427 | strategy-grade : 24 | rejetés : 403
5m valides : 27 | 15m valides : 56 | deux intervalles valides : 24

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 400 |
| INVALID_15M | 371 |
| MISSING_LATEST_CLOSED_CANDLE | 288 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 400 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 371 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| WLD-EUR | 2570600 | +0.49% | INVALID_5M | 99/4 | 99/0 |
| PUMP-EUR | 2560693 | -0.14% | INVALID_5M | 99/6 | 99/0 |
| FET-EUR | 2420409 | -1.22% | INVALID_5M | 99/2 | 99/0 |
| XLM-EUR | 2100786 | +2.47% | INVALID_5M | 99/1 | 99/0 |
| PEPE-EUR | 1862086 | +3.14% | INVALID_5M | 99/1 | 99/0 |
| DOGE-EUR | 1837092 | +3.63% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1736398 | +11.35% | INVALID_5M | 99/6 | 99/0 |
| LTC-EUR | 1592122 | +6.39% | INVALID_5M | 99/2 | 99/0 |
| POL-EUR | 1516195 | +5.41% | INVALID_5M | 99/7 | 99/0 |
| ENA-EUR | 1515350 | +8.12% | INVALID_5M | 99/2 | 99/0 |
| F-EUR | 1514193 | +34.70% | INVALID_5M | 99/2 | 81/0 |
| RAY-EUR | 1352633 | +3.93% | INVALID_15M, INVALID_5M | 99/4 | 99/1 |
| DOT-EUR | 1350609 | -0.16% | INVALID_5M | 99/2 | 99/0 |
| SKY-EUR | 1299151 | +14.34% | INVALID_5M | 99/10 | 99/0 |
| COTI-EUR | 1292166 | -11.65% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/15 | 99/2 |
| HBAR-EUR | 1274259 | +2.54% | INVALID_15M, INVALID_5M | 99/15 | 99/1 |
| AAVE-EUR | 1128901 | +5.25% | INVALID_5M | 99/1 | 99/0 |
| BNB-EUR | 1030180 | +0.97% | INVALID_15M, INVALID_5M | 99/3 | 99/1 |
| XPL-EUR | 1009319 | +1.63% | INVALID_15M, INVALID_5M | 99/8 | 99/1 |
| BCH-EUR | 1002844 | +0.30% | INVALID_15M, INVALID_5M | 99/16 | 99/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
