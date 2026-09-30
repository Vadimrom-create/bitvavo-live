# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T22:39:09.136093+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-09-30T22:38:38.833844+00:00 | âge ticker : 156.3 s | durée : 157.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CRV-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SYRUP-EUR : 0.19857 € ; score 91.89/100 ; SURVEILLE ; WICK_SETUP
- ALGO-EUR : 0.111212 € ; score 89.47/100 ; SURVEILLE ; WICK_SETUP
- KAS-EUR : 0.038392 € ; score 89.24/100 ; SURVEILLE ; seuil achat non atteint
- MEW-EUR : 0.00043991 € ; score 89.18/100 ; SURVEILLE ; seuil achat non atteint
- PLUME-EUR : 0.0169198 € ; score 86.98/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.8844 | +74.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35513 | +48.59 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOON-EUR | 0.43594 | +21.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008309 | +20.02 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.33088 | +17.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0602799 | +14.69 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NOS-EUR | 0.44758 | +12.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOMI-EUR | 0.19916 | +12.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.026699 | +11.47 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NOM-EUR | 0.0020814 | +11.44 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1868 scans ; 799318 observations ; 1424 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
