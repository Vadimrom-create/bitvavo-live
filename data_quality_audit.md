# Audit qualité des données Bitvavo

Scan : 2026-09-19T05:45:26.336018+00:00 (20260919T054353Z-01f8e87f)
Univers : 427 | strategy-grade : 24 | rejetés : 403
5m valides : 25 | 15m valides : 65 | deux intervalles valides : 24

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 402 |
| INVALID_15M | 362 |
| MISSING_LATEST_CLOSED_CANDLE | 203 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 402 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 362 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 5216234 | +4.77% | INVALID_5M | 99/1 | 100/0 |
| WLD-EUR | 2564101 | +1.13% | INVALID_5M | 99/3 | 100/0 |
| USDC-EUR | 2477201 | -0.17% | INVALID_5M | 99/1 | 100/0 |
| PUMP-EUR | 2352115 | -2.96% | INVALID_5M | 99/2 | 100/0 |
| XLM-EUR | 2120800 | +4.39% | INVALID_5M | 99/1 | 100/0 |
| INJ-EUR | 2019160 | +16.38% | INVALID_5M | 100/2 | 100/0 |
| DOGE-EUR | 1817175 | +4.01% | INVALID_5M | 100/1 | 100/0 |
| CNPY-EUR | 1706301 | +13.56% | INVALID_5M | 99/1 | 100/0 |
| AVAX-EUR | 1673047 | +7.63% | INVALID_5M | 100/1 | 100/0 |
| POL-EUR | 1610626 | +4.38% | INVALID_5M | 100/6 | 100/0 |
| LTC-EUR | 1594912 | +5.53% | INVALID_5M | 99/2 | 100/0 |
| F-EUR | 1526019 | +34.13% | INVALID_5M | 100/2 | 86/0 |
| SKY-EUR | 1339220 | +15.59% | INVALID_5M | 99/11 | 100/0 |
| DOT-EUR | 1320846 | +0.59% | INVALID_5M | 99/1 | 100/0 |
| RAY-EUR | 1243035 | +4.82% | INVALID_15M, INVALID_5M | 99/7 | 100/1 |
| HBAR-EUR | 1234783 | +3.78% | INVALID_15M, INVALID_5M | 99/14 | 100/1 |
| COTI-EUR | 1140106 | -9.71% | INVALID_15M, INVALID_5M | 99/14 | 100/2 |
| AAVE-EUR | 1125784 | +7.22% | INVALID_5M | 100/1 | 100/0 |
| BNB-EUR | 1019406 | +1.11% | INVALID_15M, INVALID_5M | 100/1 | 100/1 |
| BCH-EUR | 985229 | +0.16% | INVALID_15M, INVALID_5M | 100/4 | 100/2 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
