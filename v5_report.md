# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T05:07:07.598878+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T05:06:32.941894+00:00 | âge ticker : 156.9 s | durée : 157.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- ENJ-EUR : 0.026677 € ; score 91.07/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.757 € ; score 87.30/100 ; SURVEILLE ; seuil achat non atteint
- INJ-EUR : 6.7975 € ; score 86.94/100 ; SURVEILLE ; seuil achat non atteint
- REZ-EUR : 0.0038468 € ; score 86.93/100 ; SURVEILLE ; STABILITY_HOLD
- EIGEN-EUR : 0.23769 € ; score 86.81/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 167.821 | +92.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.27192 | +48.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0005952 | +32.83 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.0076 | +31.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| RARE-EUR | 0.017166 | +29.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.00634 | +23.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRC-EUR | 0.001281 | +22.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TAIKO-EUR | 0.09798 | +20.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.69816 | +19.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.85999 | +19.43 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1590 scans ; 680298 observations ; 1083 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
