# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-16T09:41:01.764993+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-10-16T09:39:50.878580+00:00 | âge ticker : 189.1 s | durée : 190.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- PYTH-EUR : 0.083176 € ; score 75.10/100 ; SURVEILLE ; WICK_SETUP
- BEAM-EUR : 0.0027022 € ; score 73.63/100 ; SURVEILLE ; SPREAD_RISK
- ZK-EUR : 0.015561 € ; score 73.54/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- DEEP-EUR : 0.020293 € ; score 73.53/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- DODO-EUR : 0.018733 € ; score 72.47/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.001502 | +29.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TIA-EUR | 0.60726 | +27.65 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| INJ-EUR | 8.1261 | +25.56 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ICNT-EUR | 0.12398 | +21.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.035208 | +19.24 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ALIGN-EUR | 0.004819 | +18.81 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZRO-EUR | 1.9776 | +16.44 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ETHFI-EUR | 0.62521 | +15.85 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOLV-EUR | 0.0039384 | +15.84 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ARB-EUR | 0.17803 | +14.14 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2172 scans ; 929336 observations ; 1659 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
