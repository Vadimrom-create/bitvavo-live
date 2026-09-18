# Audit qualité des données Bitvavo

Scan : 2026-09-18T22:23:45.100263+00:00 (20260918T222211Z-72bcd7a7)
Univers : 427 | strategy-grade : 5 | rejetés : 422
5m valides : 30 | 15m valides : 83 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 397 |
| INVALID_15M | 344 |
| ENTRY_INPUTS_UNAVAILABLE | 320 |
| MISSING_LATEST_CLOSED_CANDLE | 267 |
| STALE_DAILY_PROFILE | 2 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 397 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 344 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| BTC-EUR | 75455778 | +6.48% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| XRP-EUR | 57907945 | +8.61% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| SOL-EUR | 43203867 | +12.12% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ETH-EUR | 36719603 | +7.72% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| HYPE-EUR | 21032191 | +10.56% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| NEAR-EUR | 19339835 | +23.45% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ADA-EUR | 14648718 | +12.51% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| SUI-EUR | 7495780 | +12.24% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| UNI-EUR | 6249630 | +17.39% | ENTRY_INPUTS_UNAVAILABLE, INVALID_5M | 99/1 | 99/0 |
| LINK-EUR | 3908760 | +9.77% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ARB-EUR | 3413881 | +28.02% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| G-EUR | 3126012 | +50.68% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| PUMP-EUR | 2927324 | +10.72% | INVALID_5M | 99/4 | 99/0 |
| LSK-EUR | 2754929 | -0.88% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| USDC-EUR | 2724873 | -0.17% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| FET-EUR | 2646739 | +9.31% | ENTRY_INPUTS_UNAVAILABLE, MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |
| WLD-EUR | 2532580 | +12.96% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2015702 | +55.41% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| COTI-EUR | 1944530 | -15.30% | INVALID_5M | 99/2 | 99/0 |
| XLM-EUR | 1926263 | +5.52% | ENTRY_INPUTS_UNAVAILABLE, INVALID_5M | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
