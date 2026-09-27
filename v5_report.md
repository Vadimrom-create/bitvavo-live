# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T16:37:54.964595+00:00
État : OK | marchés EUR : 427 | V4 : 384 | données valides : 427
Récupération : 2026-09-27T16:37:24.582179+00:00 | âge ticker : 147.1 s | durée : 147.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVNT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- GALA-EUR : 0.0020015 € ; score 93.46/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HUMA-EUR : 0.025635 € ; score 92.53/100 ; SURVEILLE ; seuil achat non atteint
- NOT-EUR : 0.00045982 € ; score 92.17/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- TOWNS-EUR : 0.0019621 € ; score 88.72/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- ACH-EUR : 0.0055777 € ; score 88.65/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 162.936 | +56.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.29498 | +54.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.98913 | +33.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.016372 | +28.79 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARX-EUR | 0.25981 | +28.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.00732 | +20.59 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| W-EUR | 0.013495 | +19.34 % | DETECTED_EARLY | NONE | NONE |
| INX-EUR | 0.006259 | +18.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.55122 | +15.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XVG-EUR | 0.0032045 | +12.51 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |

Historique : 1630 scans ; 697378 observations ; 1154 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
