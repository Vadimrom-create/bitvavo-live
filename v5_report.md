# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T01:40:50.232665+00:00
État : OK | marchés EUR : 430 | V4 : 393 | données valides : 430
Récupération : 2026-10-01T01:39:52.196797+00:00 | âge ticker : 171.9 s | durée : 173.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PLUME-EUR : 0.0170564 € | IGNITION | score 92.58/100 | entrée 7.65/10
  Entrée 0.0170565 € ; stop 0.0164026 € ; TP1 0.0183642 € ; TP2 0.0190181 € ; montant 250.00 € ; risque théorique 11.30 € ; R/R net 1.54.
  Chase risk : 4.056/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SUI-EUR : 1.04394 € ; score 92.84/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : 1.0853 € ; score 92.45/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AAVE-EUR : 142.61 € ; score 92.32/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : 0.0020782 € ; score 91.64/100 ; SURVEILLE ; seuil achat non atteint
- SUSHI-EUR : 0.24013 € ; score 91.48/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.9546 | +75.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.36863 | +54.24 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRAC-EUR | 0.42436 | +27.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.44695 | +24.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008349 | +22.19 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.33674 | +20.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.027936 | +17.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0618718 | +16.02 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NOS-EUR | 0.45117 | +12.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0020849 | +11.58 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1877 scans ; 803188 observations ; 1430 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
