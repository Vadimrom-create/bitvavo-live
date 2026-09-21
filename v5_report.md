# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T22:24:19.998524+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-21T22:23:46.723133+00:00 | âge ticker : 149.0 s | durée : 149.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SHIB-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- COW-EUR : 0.13734 € ; score 89.16/100 ; SURVEILLE ; seuil achat non atteint
- AI-EUR : 0.01855 € ; score 86.75/100 ; SURVEILLE ; seuil achat non atteint
- MIOTA-EUR : 0.042092 € ; score 86.57/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- QNT-EUR : 58.76 € ; score 84.99/100 ; SURVEILLE ; WICK_SETUP
- RECALL-EUR : 0.039026 € ; score 83.82/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0014699 | +89.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.0145 | +68.82 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.124838 | +54.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.052292 | +51.78 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.3123 | +38.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0010917 | +36.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008699 | +35.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.04341 | +34.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUFFER-EUR | 0.026178 | +24.40 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SYN-EUR | 0.227242 | +22.54 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1125 scans ; 481987 observations ; 406 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
