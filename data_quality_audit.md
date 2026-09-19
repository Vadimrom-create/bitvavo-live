# Audit qualité des données Bitvavo

Scan : 2026-09-19T20:03:54.346179+00:00 (20260919T200223Z-341371f7)
Univers : 427 | strategy-grade : 35 | rejetés : 392
5m valides : 35 | 15m valides : 89 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 338 |
| MISSING_LATEST_CLOSED_CANDLE | 262 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 338 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| CAP-EUR | 1983162 | -14.01% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 1908050 | +3.84% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1807203 | -4.81% | INVALID_5M | 100/3 | 100/0 |
| APT-EUR | 1794519 | +4.64% | INVALID_5M | 99/6 | 99/0 |
| ARB-EUR | 1689917 | -6.20% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1547706 | +1.78% | INVALID_5M | 99/2 | 99/0 |
| OP-EUR | 1213807 | +5.58% | INVALID_5M | 99/8 | 100/0 |
| POL-EUR | 1192121 | -3.58% | INVALID_5M | 99/5 | 100/0 |
| SKY-EUR | 1048272 | -1.06% | INVALID_15M, INVALID_5M | 100/22 | 100/3 |
| BCH-EUR | 979300 | +0.29% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/8 | 100/1 |
| AAVE-EUR | 936710 | +2.92% | INVALID_5M | 99/5 | 99/0 |
| DOT-EUR | 934928 | -0.19% | INVALID_5M | 99/2 | 99/0 |
| SAGA-EUR | 882147 | -2.65% | INVALID_5M | 100/7 | 100/0 |
| COTI-EUR | 860034 | -6.71% | INVALID_5M | 99/3 | 99/0 |
| MORPHO-EUR | 837986 | +7.65% | INVALID_15M, INVALID_5M | 99/8 | 99/1 |
| F-EUR | 819750 | -8.74% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/15 | 99/2 |
| KAS-EUR | 800758 | +6.80% | INVALID_5M | 99/3 | 100/0 |
| STX-EUR | 794839 | +11.82% | INVALID_15M, INVALID_5M | 99/3 | 99/1 |
| JUP-EUR | 736904 | +4.01% | INVALID_5M | 99/5 | 99/0 |
| BNB-EUR | 611109 | -0.24% | INVALID_5M | 99/4 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
