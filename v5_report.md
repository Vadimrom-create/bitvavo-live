# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T08:35:56.411320+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-24T08:35:24.188060+00:00 | âge ticker : 148.6 s | durée : 149.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TAIKO-EUR : 0.08071 € ; score 91.22/100 ; SURVEILLE ; WICK_SETUP
- RECALL-EUR : 0.040469 € ; score 87.51/100 ; SURVEILLE ; WICK_SETUP
- LISTA-EUR : 0.070412 € ; score 86.79/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- GMX-EUR : 7.0724 € ; score 84.19/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- POL-EUR : 0.089138 € ; score 84.15/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0023874 | +56.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.12267 | +36.24 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| LSK-EUR | 0.37071 | +35.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.81658 | +14.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMU-EUR | 0.001942 | +12.83 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CELR-EUR | 0.0028883 | +11.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOSO-EUR | 0.28892 | +10.04 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| ARX-EUR | 0.20988 | +9.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CNPY-EUR | 0.38499 | +9.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.15136 | +7.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1341 scans ; 574003 observations ; 698 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
