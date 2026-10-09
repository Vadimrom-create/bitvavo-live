# Audit qualité des données Bitvavo

Scan : 2026-10-09T09:12:09.807367+00:00 (20261009T090953Z-d1a0d1b6)
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
| WHUF-EUR | 748379 | +10.44% | INVALID_15M | 27/0 | 9/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
