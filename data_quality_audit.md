# Audit qualité des données Bitvavo

Scan : 2026-09-19T17:59:33.447071+00:00 (20260919T175802Z-508a349d)
Univers : 427 | strategy-grade : 34 | rejetés : 393
5m valides : 37 | 15m valides : 94 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 390 |
| INVALID_15M | 333 |
| MISSING_LATEST_CLOSED_CANDLE | 272 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 390 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 333 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| STRK-EUR | 2148606 | +15.03% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 1955372 | -3.91% | INVALID_5M | 100/1 | 99/0 |
| APT-EUR | 1860742 | +5.41% | INVALID_5M | 99/2 | 99/0 |
| CAP-EUR | 1858854 | -15.50% | INVALID_15M | 99/0 | 99/1 |
| POL-EUR | 1523330 | +3.20% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1446745 | +1.96% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 98/1 | 99/0 |
| WLD-EUR | 1362178 | +3.74% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1228219 | +7.14% | INVALID_5M | 100/4 | 99/0 |
| VET-EUR | 1154874 | +10.93% | INVALID_5M | 98/1 | 99/0 |
| F-EUR | 1072255 | -10.85% | INVALID_5M | 99/5 | 99/0 |
| SKY-EUR | 1063663 | -0.83% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/6 | 99/1 |
| SAGA-EUR | 989584 | -2.08% | INVALID_5M | 99/2 | 99/0 |
| DOT-EUR | 979206 | -0.92% | INVALID_5M | 99/1 | 99/0 |
| BCH-EUR | 978611 | +1.31% | INVALID_5M | 99/5 | 99/0 |
| AAVE-EUR | 907132 | +2.99% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/5 | 99/0 |
| COTI-EUR | 890722 | -4.58% | INVALID_5M | 100/3 | 99/0 |
| MORPHO-EUR | 814569 | +8.09% | INVALID_5M | 99/3 | 99/0 |
| HEI-EUR | 798357 | +12.52% | INVALID_5M | 99/2 | 99/0 |
| JUP-EUR | 735404 | +5.35% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/8 | 99/0 |
| C-EUR | 693933 | -3.19% | MISSING_LATEST_CLOSED_CANDLE | 99/0 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
