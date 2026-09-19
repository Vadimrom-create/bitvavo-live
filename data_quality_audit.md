# Audit qualité des données Bitvavo

Scan : 2026-09-19T01:08:59.016580+00:00 (20260919T010728Z-ca368e9e)
Univers : 427 | strategy-grade : 23 | rejetés : 404
5m valides : 24 | 15m valides : 65 | deux intervalles valides : 23

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 403 |
| INVALID_15M | 362 |
| MISSING_LATEST_CLOSED_CANDLE | 284 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 403 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 362 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 6268936 | +14.19% | INVALID_5M | 99/5 | 99/0 |
| TAO-EUR | 6078069 | +7.14% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 2802887 | +4.49% | INVALID_5M | 99/3 | 99/0 |
| USDC-EUR | 2701589 | -0.20% | INVALID_5M | 99/5 | 99/0 |
| WLD-EUR | 2586122 | +10.12% | INVALID_5M | 99/5 | 99/0 |
| XLM-EUR | 2048365 | +5.62% | INVALID_5M | 99/4 | 99/0 |
| INJ-EUR | 1906836 | +16.91% | INVALID_5M | 99/3 | 99/0 |
| CNPY-EUR | 1832136 | -2.65% | INVALID_5M | 99/3 | 99/0 |
| PEPE-EUR | 1806597 | +4.40% | INVALID_5M | 99/1 | 99/0 |
| RAY-EUR | 1539542 | +17.37% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 99/0 |
| APT-EUR | 1524189 | +21.56% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1520976 | +6.58% | INVALID_5M | 99/2 | 99/0 |
| COTI-EUR | 1488011 | -11.57% | INVALID_5M | 100/8 | 99/0 |
| AVAX-EUR | 1487996 | +9.10% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1370577 | +6.96% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 1327777 | +3.38% | INVALID_5M | 99/4 | 99/0 |
| HBAR-EUR | 1280079 | +5.19% | INVALID_5M | 100/1 | 99/0 |
| SKY-EUR | 1187949 | +19.23% | INVALID_5M | 99/7 | 99/0 |
| AAVE-EUR | 1105265 | +9.84% | INVALID_5M | 99/6 | 99/0 |
| BCH-EUR | 1063759 | +8.48% | INVALID_5M | 99/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
