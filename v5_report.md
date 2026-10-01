# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T09:28:20.276938+00:00
État : OK | marchés EUR : 430 | V4 : 390 | données valides : 430
Récupération : 2026-10-01T09:27:45.176513+00:00 | âge ticker : 151.0 s | durée : 151.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- PROM-EUR : 5.7836 € ; score 92.60/100 ; SURVEILLE ; WICK_SETUP
- HUMA-EUR : 0.029614 € ; score 84.67/100 ; SURVEILLE ; seuil achat non atteint
- SENT-EUR : 0.01949 € ; score 84.59/100 ; SURVEILLE ; seuil achat non atteint
- MERL-EUR : 0.028199 € ; score 83.38/100 ; SURVEILLE ; seuil achat non atteint
- ALICE-EUR : 0.15058 € ; score 82.86/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CT-EUR | 0.38524 | +61.19 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0027884 | +47.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVR-EUR | 2.5179 | +43.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.34135 | +21.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0661 | +20.82 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MON-EUR | 0.028433 | +17.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JASMY-EUR | 0.0054265 | +17.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.4637 | +16.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VELO-EUR | 0.0051979 | +15.51 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| TRAC-EUR | 0.4129 | +14.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1899 scans ; 812648 observations ; 1466 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
