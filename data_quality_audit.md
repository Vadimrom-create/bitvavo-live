# Audit qualité des données Bitvavo

Scan : 2026-09-18T22:37:39.364801+00:00 (20260918T223606Z-8ccc9686)
Univers : 427 | strategy-grade : 2 | rejetés : 425
5m valides : 31 | 15m valides : 84 | deux intervalles valides : 30

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 396 |
| INVALID_15M | 343 |
| ENTRY_INPUTS_UNAVAILABLE | 320 |
| MISSING_LATEST_CLOSED_CANDLE | 273 |
| STALE_DAILY_PROFILE | 2 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 396 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 343 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| BTC-EUR | 75678669 | +6.18% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| XRP-EUR | 58207219 | +7.70% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| SOL-EUR | 43325397 | +11.44% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ETH-EUR | 36874574 | +7.23% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| HYPE-EUR | 20926872 | +9.45% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| NEAR-EUR | 19379230 | +22.40% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ADA-EUR | 14678335 | +11.89% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| SUI-EUR | 7520411 | +10.73% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| UNI-EUR | 6311971 | +14.36% | ENTRY_INPUTS_UNAVAILABLE, INVALID_5M | 99/1 | 99/0 |
| TAO-EUR | 5642597 | +8.27% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ONDO-EUR | 4656176 | +7.36% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| LINK-EUR | 3914339 | +8.35% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ARB-EUR | 3454159 | +24.65% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| G-EUR | 3141535 | +47.64% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| PUMP-EUR | 2924502 | +8.50% | INVALID_5M | 99/4 | 99/0 |
| LSK-EUR | 2751269 | -0.91% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 100/0 |
| USDC-EUR | 2727349 | -0.14% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| FET-EUR | 2623459 | +8.72% | ENTRY_INPUTS_UNAVAILABLE, INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 2534809 | +11.77% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 2044575 | +53.14% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
