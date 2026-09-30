# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T19:05:30.812174+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-09-30T19:04:26.482014+00:00 | âge ticker : 184.8 s | durée : 185.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PUMP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- XLM-EUR : 0.1995 € ; score 92.02/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XVG-EUR : 0.0028812 € ; score 91.31/100 ; SURVEILLE ; seuil achat non atteint
- GMT-EUR : 0.007559 € ; score 87.87/100 ; SURVEILLE ; LOW_LIQUIDITY
- RED-EUR : 0.15655 € ; score 82.57/100 ; SURVEILLE ; SPREAD_RISK
- NOT-EUR : 0.00043379 € ; score 82.13/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.5638 | +54.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.36472 | +52.60 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOON-EUR | 0.43484 | +21.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UP-EUR | 0.073369 | +19.37 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GLMR-EUR | 0.007942 | +17.55 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.068536 | +15.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.37376 | +14.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOMI-EUR | 0.19768 | +12.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MERL-EUR | 0.02855 | +11.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.059 | +11.92 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1857 scans ; 794588 observations ; 1416 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
