# Audit qualité des données Bitvavo

Scan : 2026-09-18T22:51:32.032469+00:00 (20260918T224937Z-0e5ff684)
Univers : 427 | strategy-grade : 1 | rejetés : 426
5m valides : 28 | 15m valides : 83 | deux intervalles valides : 27

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 399 |
| INVALID_15M | 344 |
| ENTRY_INPUTS_UNAVAILABLE | 321 |
| MISSING_LATEST_CLOSED_CANDLE | 289 |
| STALE_DAILY_PROFILE | 3 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 399 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 344 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| BTC-EUR | 75886129 | +6.02% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| XRP-EUR | 58590009 | +7.72% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| SOL-EUR | 43404974 | +11.19% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ETH-EUR | 37107924 | +6.95% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| HYPE-EUR | 21009167 | +9.96% | STALE_DAILY_PROFILE | 99/0 | 99/0 |
| NEAR-EUR | 19139124 | +20.69% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ADA-EUR | 14658839 | +12.20% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| SUI-EUR | 7484354 | +11.11% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| UNI-EUR | 6348798 | +14.52% | ENTRY_INPUTS_UNAVAILABLE, INVALID_5M | 99/1 | 99/0 |
| TAO-EUR | 5709012 | +8.06% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ONDO-EUR | 4671098 | +6.52% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| LINK-EUR | 3964878 | +8.35% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| ARB-EUR | 3498766 | +23.16% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| G-EUR | 3144220 | +52.50% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| PUMP-EUR | 2913574 | +5.54% | INVALID_5M | 99/4 | 99/0 |
| LSK-EUR | 2758054 | -1.22% | INVALID_5M | 100/1 | 99/0 |
| USDC-EUR | 2732737 | -0.15% | ENTRY_INPUTS_UNAVAILABLE, MISSING_LATEST_CLOSED_CANDLE | 99/0 | 100/0 |
| FET-EUR | 2726536 | +8.76% | INVALID_5M, STALE_DAILY_PROFILE | 100/1 | 99/0 |
| STRK-EUR | 2053593 | +54.67% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |
| USELESS-EUR | 2022290 | +11.33% | ENTRY_INPUTS_UNAVAILABLE | 99/0 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
