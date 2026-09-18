# Audit qualité des données Bitvavo

Scan : 2026-09-18T23:41:49.748080+00:00 (20260918T234020Z-d0c5ba25)
Univers : 427 | strategy-grade : 25 | rejetés : 402
5m valides : 26 | 15m valides : 74 | deux intervalles valides : 26

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 401 |
| INVALID_15M | 353 |
| MISSING_LATEST_CLOSED_CANDLE | 312 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 401 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 353 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 6303318 | +14.58% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 2784410 | +3.88% | INVALID_5M | 99/4 | 99/0 |
| USDC-EUR | 2748440 | -0.17% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 99/0 |
| LSK-EUR | 2714658 | -0.33% | INVALID_5M | 99/1 | 99/0 |
| FET-EUR | 2688487 | +6.89% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 2558859 | +10.76% | INVALID_5M | 100/1 | 99/0 |
| XLM-EUR | 1961365 | +4.83% | INVALID_5M | 100/1 | 99/0 |
| INJ-EUR | 1854123 | +15.50% | INVALID_5M | 99/5 | 99/0 |
| COTI-EUR | 1727442 | -15.84% | INVALID_5M | 100/4 | 99/0 |
| RAY-EUR | 1549997 | +19.03% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1478570 | +6.84% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1291753 | +22.32% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 1281265 | +4.63% | INVALID_5M | 99/3 | 99/0 |
| POL-EUR | 1265937 | +8.38% | INVALID_5M | 99/2 | 99/0 |
| HBAR-EUR | 1183166 | +6.22% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1086812 | +16.51% | INVALID_15M, INVALID_5M | 99/13 | 99/1 |
| DRIFT-EUR | 1069865 | +0.05% | INVALID_5M | 99/1 | 99/0 |
| XPL-EUR | 999687 | +7.23% | INVALID_5M | 100/6 | 99/0 |
| AAVE-EUR | 945758 | +8.07% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 99/0 |
| LPT-EUR | 886042 | +16.08% | INVALID_5M | 100/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
