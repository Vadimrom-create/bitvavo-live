# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T09:51:09.474848+00:00
État : OK | marchés EUR : 430 | V4 : 389 | données valides : 430
Récupération : 2026-10-01T09:50:31.327387+00:00 | âge ticker : 154.9 s | durée : 155.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- ALICE-EUR : 0.1521 € ; score 84.34/100 ; SURVEILLE ; WICK_SETUP
- MERL-EUR : 0.027899 € ; score 82.81/100 ; SURVEILLE ; seuil achat non atteint
- REZ-EUR : 0.0041196 € ; score 80.10/100 ; SURVEILLE ; seuil achat non atteint
- DEEP-EUR : 0.020451 € ; score 79.96/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- DIA-EUR : 0.15511 € ; score 79.18/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CT-EUR | 0.41381 | +73.14 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0028176 | +48.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVR-EUR | 2.4552 | +39.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.34496 | +22.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.065983 | +21.06 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MON-EUR | 0.028405 | +16.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JASMY-EUR | 0.0053526 | +16.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.46567 | +16.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VELO-EUR | 0.0051536 | +14.65 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| TRAC-EUR | 0.42088 | +14.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1900 scans ; 813078 observations ; 1472 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
