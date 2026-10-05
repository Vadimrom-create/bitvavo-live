# Audit qualité des données Bitvavo

Scan : 2026-10-05T16:07:01.095746+00:00 (20261005T160530Z-6c077c8d)
Univers : 427 | strategy-grade : 426 | rejetés : 1
5m valides : 427 | 15m valides : 426 | deux intervalles valides : 426

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_15M | 1 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| INSUFFICIENT_CLOSED_CANDLES | 1 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| PNT-EUR | 1348133 | +43.01% | INVALID_15M | 49/0 | 16/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
