# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T19:27:52.569354+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 430
Récupération : 2026-09-30T19:27:15.165234+00:00 | âge ticker : 158.9 s | durée : 159.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PUMP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- NEAR-EUR : 4.7913 € ; score 85.46/100 ; SURVEILLE ; WICK_SETUP
- FET-EUR : 0.19745 € ; score 85.32/100 ; SURVEILLE ; WICK_SETUP
- KAS-EUR : 0.038185 € ; score 85.28/100 ; SURVEILLE ; seuil achat non atteint
- HBAR-EUR : 0.094852 € ; score 81.72/100 ; SURVEILLE ; seuil achat non atteint
- MIOTA-EUR : 0.047044 € ; score 80.82/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CT-EUR | 0.37135 | +55.38 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.562 | +52.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.42712 | +19.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.00812 | +19.11 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOS-EUR | 0.44205 | +16.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UP-EUR | 0.070505 | +14.71 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TRAC-EUR | 0.37041 | +13.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.06775 | +12.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| REZ-EUR | 0.004178 | +11.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0593477 | +11.31 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1858 scans ; 795018 observations ; 1416 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
