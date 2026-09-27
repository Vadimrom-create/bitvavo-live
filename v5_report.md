# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T14:23:38.237992+00:00
État : OK | marchés EUR : 427 | V4 : 384 | données valides : 427
Récupération : 2026-09-27T14:23:05.628412+00:00 | âge ticker : 156.0 s | durée : 157.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- A-EUR : 0.092442 € ; score 93.26/100 ; SURVEILLE ; WICK_SETUP
- HUMA-EUR : 0.024899 € ; score 92.92/100 ; SURVEILLE ; WICK_SETUP
- ACU-EUR : 0.12001 € ; score 90.42/100 ; SURVEILLE ; WICK_SETUP
- HNT-EUR : 0.45522 € ; score 89.69/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD
- DATAIP-EUR : 0.2013 € ; score 87.92/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 144.257 | +54.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.1511 | +52.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008519 | +41.02 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.25395 | +33.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.2556 | +27.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AUDIO-EUR | 0.015784 | +23.75 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRASS-EUR | 0.55323 | +21.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MAGIC-EUR | 0.055223 | +20.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006113 | +17.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.006118 | +15.41 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1622 scans ; 693962 observations ; 1145 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
