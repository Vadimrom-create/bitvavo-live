# Audit qualité des données Bitvavo

Scan : 2026-09-18T22:18:25.682900+00:00 (20260918T221658Z-e4bfe887)
Univers : 427 | strategy-grade : 3 | rejetés : 424
5m valides : 32 | 15m valides : 83 | deux intervalles valides : 32

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 395 |
| INVALID_15M | 344 |
| ENTRY_INPUTS_UNAVAILABLE | 318 |
| MISSING_LATEST_CLOSED_CANDLE | 249 |
| STALE_DAILY_PROFILE | 2 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 395 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 344 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| BTC-EUR | 75445306 | +6.43% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| XRP-EUR | 57700130 | +8.55% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| SOL-EUR | 43160800 | +12.23% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ETH-EUR | 36727145 | +7.66% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| HYPE-EUR | 21047300 | +10.78% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| NEAR-EUR | 19338612 | +21.95% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ADA-EUR | 14766735 | +12.49% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| SUI-EUR | 7428954 | +11.98% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| UNI-EUR | 6208297 | +18.38% | ENTRY_INPUTS_UNAVAILABLE, INVALID_5M | 99/1 | 99/0 |
| ONDO-EUR | 4711046 | +8.13% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| LINK-EUR | 3916984 | +10.01% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ARB-EUR | 3413568 | +29.47% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| G-EUR | 3124139 | +48.84% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| PUMP-EUR | 2926979 | +10.06% | INVALID_5M | 100/4 | 100/0 |
| LSK-EUR | 2755184 | -0.51% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| USDC-EUR | 2715635 | -0.15% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| FET-EUR | 2670802 | +10.01% | ENTRY_INPUTS_UNAVAILABLE | 100/0 | 100/0 |
| WLD-EUR | 2517274 | +12.90% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2007316 | +56.54% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| COTI-EUR | 1965108 | -16.29% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
