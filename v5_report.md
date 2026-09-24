# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T18:44:27.922405+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-24T18:43:48.458522+00:00 | âge ticker : 171.2 s | durée : 173.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LINK-EUR : 11.6551 € ; score 91.46/100 ; SURVEILLE ; WICK_SETUP
- CHZ-EUR : 0.014424 € ; score 90.30/100 ; SURVEILLE ; seuil achat non atteint
- XLM-EUR : 0.18665 € ; score 89.99/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BEAM-EUR : 0.0017946 € ; score 88.77/100 ; SURVEILLE ; SPREAD_RISK
- GRT-EUR : 0.022694 € ; score 84.94/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| XAI-EUR | 0.0100755 | +46.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.35918 | +32.44 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOM-EUR | 0.0019468 | +28.54 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| PEAQ-EUR | 0.036874 | +21.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ONDO-EUR | 0.43989 | +21.79 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 74.646 | +20.06 % | DETECTED_EARLY | NONE | NONE |
| PLUME-EUR | 0.0161233 | +18.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LTC-EUR | 62.975 | +17.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XPL-EUR | 0.090186 | +17.16 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARX-EUR | 0.22273 | +16.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1376 scans ; 588920 observations ; 752 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
