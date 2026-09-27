# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T13:36:27.730298+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T13:35:57.172035+00:00 | âge ticker : 145.2 s | durée : 146.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- ENJ-EUR : 0.027048 € ; score 92.79/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- ONDO-EUR : 0.48452 € ; score 92.59/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TNSR-EUR : 0.035866 € ; score 91.69/100 ; SURVEILLE ; seuil achat non atteint
- LTC-EUR : 62.517 € ; score 89.41/100 ; SURVEILLE ; STABILITY_HOLD
- CFG-EUR : 0.146774 € ; score 88.72/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 142.729 | +54.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.12302 | +54.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008636 | +46.42 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AUDIO-EUR | 0.0177 | +38.77 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.25501 | +33.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.5495 | +21.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.01315 | +18.29 % | DETECTED_EARLY | NONE | NONE |
| WLD-EUR | 0.50717 | +17.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006142 | +17.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.23987 | +17.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1619 scans ; 692681 observations ; 1142 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
