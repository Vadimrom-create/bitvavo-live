# Audit qualité des données Bitvavo

Scan : 2026-09-19T01:44:54.431613+00:00 (20260919T014250Z-2edc50a5)
Univers : 427 | strategy-grade : 25 | rejetés : 402
5m valides : 26 | 15m valides : 66 | deux intervalles valides : 25

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 401 |
| INVALID_15M | 361 |
| MISSING_LATEST_CLOSED_CANDLE | 286 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 401 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 361 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 6236095 | +14.30% | INVALID_5M | 98/4 | 99/0 |
| TAO-EUR | 6120730 | +6.03% | INVALID_5M | 98/1 | 99/0 |
| G-EUR | 3197137 | +43.47% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 98/1 | 99/0 |
| PUMP-EUR | 2769136 | +4.15% | INVALID_5M | 99/4 | 99/0 |
| USDC-EUR | 2704751 | -0.20% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/4 | 99/0 |
| WLD-EUR | 2593398 | +7.49% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 98/6 | 99/0 |
| XLM-EUR | 2135882 | +4.46% | INVALID_5M | 99/4 | 99/0 |
| INJ-EUR | 1929468 | +16.87% | INVALID_5M | 99/2 | 99/0 |
| PEPE-EUR | 1882555 | +2.20% | INVALID_5M | 98/1 | 99/0 |
| CNPY-EUR | 1829515 | -0.25% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/3 | 100/0 |
| LTC-EUR | 1562384 | +6.45% | INVALID_5M | 100/2 | 99/0 |
| AVAX-EUR | 1535064 | +10.05% | INVALID_5M | 98/2 | 99/0 |
| RAY-EUR | 1528232 | +13.79% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 99/0 |
| COTI-EUR | 1445397 | -11.73% | INVALID_5M | 100/10 | 99/0 |
| DOT-EUR | 1324778 | +2.31% | INVALID_5M | 99/4 | 99/0 |
| HBAR-EUR | 1285508 | +4.69% | INVALID_5M | 98/1 | 99/0 |
| SKY-EUR | 1231522 | +19.91% | INVALID_5M | 98/7 | 99/0 |
| AAVE-EUR | 1135826 | +8.37% | INVALID_5M | 100/3 | 99/0 |
| BCH-EUR | 1070750 | +8.03% | INVALID_5M | 99/5 | 99/0 |
| XPL-EUR | 985009 | +4.99% | INVALID_5M | 99/5 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
