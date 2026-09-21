# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T22:57:29.225891+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-21T22:56:55.053697+00:00 | âge ticker : 155.1 s | durée : 156.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZEN-EUR : 6.721 € ; score 90.45/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- S-EUR : 0.034074 € ; score 89.74/100 ; SURVEILLE ; seuil achat non atteint
- DYM-EUR : 0.015918 € ; score 88.30/100 ; SURVEILLE ; seuil achat non atteint
- FIL-EUR : 0.86736 € ; score 87.86/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0080541 € ; score 87.61/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0014662 | +89.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.014998 | +75.29 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.122692 | +53.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.052519 | +52.44 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.31872 | +41.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0011076 | +36.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043809 | +35.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SWELL-EUR | 0.0008583 | +33.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUFFER-EUR | 0.025841 | +22.69 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| GRASS-EUR | 0.38361 | +22.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1129 scans ; 483691 observations ; 410 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
