# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T10:31:42.889943+00:00
État : OK | marchés EUR : 430 | V4 : 388 | données valides : 430
Récupération : 2026-10-01T10:31:01.794339+00:00 | âge ticker : 161.2 s | durée : 162.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- ALICE-EUR : 0.15062 € ; score 83.19/100 ; SURVEILLE ; seuil achat non atteint
- TRX-EUR : 0.29574 € ; score 81.71/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- WLD-EUR : 0.45579 € ; score 79.55/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 145.2 € ; score 79.39/100 ; SURVEILLE ; WICK_SETUP
- KAIA-EUR : 0.032242 € ; score 78.36/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.5302 | +63.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.45238 | +45.96 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0026091 | +32.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.34021 | +20.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0653783 | +19.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOS-EUR | 0.46861 | +16.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.027925 | +14.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JASMY-EUR | 0.0052433 | +14.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HEI-EUR | 0.137785 | +14.70 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| VELO-EUR | 0.0051446 | +13.71 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1902 scans ; 813938 observations ; 1475 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
