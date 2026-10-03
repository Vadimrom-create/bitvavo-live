# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T14:42:34.656940+00:00
État : OK | marchés EUR : 426 | V4 : 391 | données valides : 426
Récupération : 2026-10-03T14:41:26.997994+00:00 | âge ticker : 186.5 s | durée : 187.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- IMX-EUR : 0.16563 € ; score 80.81/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- FLUID-EUR : 1.4774 € ; score 80.01/100 ; SURVEILLE ; seuil achat non atteint
- ATH-EUR : 0.0064044 € ; score 79.68/100 ; SURVEILLE ; WICK_SETUP
- AAVE-EUR : 160.25 € ; score 79.22/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.54922 € ; score 78.64/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GLMR-EUR | 0.010938 | +42.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.91222 | +26.50 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SUPER-EUR | 0.23604 | +18.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WIN-EUR | 4.6283e-05 | +15.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAND-EUR | 0.065716 | +14.94 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| WLD-EUR | 0.54922 | +9.47 % | DETECTED_EARLY | NONE | NONE |
| ATH-EUR | 0.0064044 | +8.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.0065 | +8.82 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| HFT-EUR | 0.006078 | +8.56 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.66839 | +8.29 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 2046 scans ; 875582 observations ; 1623 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
