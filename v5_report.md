# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T00:47:19.599700+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 429
Récupération : 2026-09-30T00:46:43.127240+00:00 | âge ticker : 157.7 s | durée : 158.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- SYRUP-EUR : 0.20854 € ; score 82.80/100 ; SURVEILLE ; WICK_SETUP
- AAVE-EUR : 143.6 € ; score 80.01/100 ; SURVEILLE ; STABILITY_HOLD
- ALICE-EUR : 0.14753 € ; score 79.44/100 ; SURVEILLE ; seuil achat non atteint
- COMP-EUR : 21.974 € ; score 78.85/100 ; SURVEILLE ; seuil achat non atteint
- SEI-EUR : 0.065019 € ; score 78.64/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.36402 | +41.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.0963 | +31.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0016576 | +31.06 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.65045 | +24.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 235.54 | +18.20 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0051106 | +17.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.064142 | +17.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRIA-EUR | 0.00406 | +15.87 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ZBCN-EUR | 0.0022186 | +15.44 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INIT-EUR | 0.090236 | +15.39 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1805 scans ; 772255 observations ; 1345 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
