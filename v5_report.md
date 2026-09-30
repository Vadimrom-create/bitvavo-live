# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T18:23:47.023738+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 430
Récupération : 2026-09-30T18:23:04.650522+00:00 | âge ticker : 158.4 s | durée : 159.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- STX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- TRB-EUR : 18.281 € ; score 92.83/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ALGO-EUR : 0.11088 € ; score 87.90/100 ; SURVEILLE ; WICK_SETUP
- S-EUR : 0.035451 € ; score 84.05/100 ; SURVEILLE ; WICK_SETUP
- XLM-EUR : 0.19883 € ; score 82.65/100 ; SURVEILLE ; WICK_SETUP
- COMP-EUR : 21.809 € ; score 81.86/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.5451 | +60.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.34363 | +43.78 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| UP-EUR | 0.07699 | +26.29 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.44103 | +23.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008098 | +22.29 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 261.23 | +15.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0021127 | +14.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MERL-EUR | 0.02844 | +14.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.31758 | +12.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.42392 | +12.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1855 scans ; 793728 observations ; 1416 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
