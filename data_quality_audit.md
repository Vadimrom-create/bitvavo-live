# Audit qualité des données Bitvavo

Scan : 2026-10-05T15:32:06.086616+00:00 (20261005T153032Z-b80ccf11)
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
| PNT-EUR | 1313050 | +43.69% | INVALID_15M | 42/0 | 14/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
