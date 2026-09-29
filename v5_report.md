# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T23:41:00.146585+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 429
Récupération : 2026-09-29T23:40:25.805191+00:00 | âge ticker : 152.2 s | durée : 153.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETHFI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZRO-EUR : 1.4761 € ; score 86.93/100 ; SURVEILLE ; seuil achat non atteint
- REZ-EUR : 0.0038148 € ; score 85.73/100 ; SURVEILLE ; seuil achat non atteint
- LAPTOP-EUR : 0.06889 € ; score 84.10/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- ICP-EUR : 3.0192 € ; score 83.26/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : 0.20828 € ; score 81.55/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.36761 | +35.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.67783 | +31.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0016321 | +28.48 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.078 | +26.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0022445 | +24.71 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0052146 | +20.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.063315 | +18.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.090575 | +14.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 237.48 | +14.79 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TRIA-EUR | 0.004016 | +14.61 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1802 scans ; 770968 observations ; 1344 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
