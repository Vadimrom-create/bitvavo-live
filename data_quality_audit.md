# Audit qualité des données Bitvavo

Scan : 2026-09-19T00:53:09.126187+00:00 (20260919T005143Z-1c6e64fc)
Univers : 427 | strategy-grade : 23 | rejetés : 404
5m valides : 23 | 15m valides : 65 | deux intervalles valides : 23

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 404 |
| INVALID_15M | 362 |
| MISSING_LATEST_CLOSED_CANDLE | 288 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 404 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 362 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 6214150 | +14.75% | INVALID_5M | 100/3 | 99/0 |
| TAO-EUR | 6084632 | +8.05% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 2797847 | +4.92% | INVALID_5M | 99/3 | 99/0 |
| USDC-EUR | 2712263 | -0.18% | INVALID_5M | 99/5 | 99/0 |
| WLD-EUR | 2587520 | +10.72% | INVALID_5M | 99/5 | 99/0 |
| XLM-EUR | 2048787 | +6.51% | INVALID_5M | 99/4 | 99/0 |
| INJ-EUR | 1900648 | +17.35% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1822669 | +4.08% | INVALID_5M | 99/3 | 99/0 |
| PEPE-EUR | 1804476 | +5.42% | INVALID_5M | 99/1 | 99/0 |
| RAY-EUR | 1547593 | +16.85% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 100/0 |
| COTI-EUR | 1530265 | -13.36% | INVALID_5M | 100/8 | 99/0 |
| LTC-EUR | 1529035 | +8.05% | INVALID_5M | 99/2 | 99/0 |
| AVAX-EUR | 1493630 | +8.92% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1476081 | +23.40% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 1363684 | +7.46% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 1324600 | +4.02% | INVALID_5M | 99/4 | 99/0 |
| HBAR-EUR | 1277247 | +5.59% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1162532 | +18.29% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/5 | 100/1 |
| AAVE-EUR | 1105254 | +11.48% | INVALID_5M | 99/6 | 99/0 |
| BCH-EUR | 1058921 | +9.04% | INVALID_5M | 99/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
