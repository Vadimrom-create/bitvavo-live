# Audit qualité des données Bitvavo

Scan : 2026-09-30T14:53:37.813349+00:00 (20260930T145051Z-1d583f5a)
Univers : 430 | strategy-grade : 429 | rejetés : 1
5m valides : 430 | 15m valides : 429 | deux intervalles valides : 429

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
| CT-EUR | 1667547 | +38.18% | INVALID_15M | 58/0 | 19/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
