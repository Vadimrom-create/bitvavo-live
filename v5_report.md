# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T05:32:17.119230+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-10-03T05:31:07.820744+00:00 | âge ticker : 190.4 s | durée : 191.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- GALA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FLUID-EUR : 1.4454 € ; score 87.92/100 ; SURVEILLE ; WICK_SETUP
- W-EUR : 0.012093 € ; score 85.91/100 ; SURVEILLE ; WICK_SETUP
- WLD-EUR : 0.51026 € ; score 85.22/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : 0.00796 € ; score 84.35/100 ; SURVEILLE ; WICK_SETUP
- AXS-EUR : 1.1249 € ; score 83.61/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.069392 | +67.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.09752 | +23.26 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ENJ-EUR | 0.031761 | +16.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023659 | +14.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.006064 | +13.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APE-EUR | 0.14931 | +10.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AXS-EUR | 1.1249 | +9.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BAT-EUR | 0.08769 | +9.59 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| YGG-EUR | 0.025966 | +9.46 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AGI-EUR | 0.006137 | +9.39 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 2030 scans ; 868766 observations ; 1602 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
