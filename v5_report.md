# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T22:20:22.036716+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-09-30T22:19:48.428181+00:00 | âge ticker : 150.6 s | durée : 152.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ZIG-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZRO-EUR : 1.5333 € ; score 84.66/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- PLUME-EUR : 0.0166384 € ; score 84.51/100 ; SURVEILLE ; seuil achat non atteint
- INIT-EUR : 0.09123 € ; score 83.07/100 ; SURVEILLE ; seuil achat non atteint
- RED-EUR : 0.15629 € ; score 82.17/100 ; SURVEILLE ; SPREAD_RISK
- DIA-EUR : 0.14795 € ; score 82.03/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.8106 | +71.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35708 | +49.41 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.008494 | +23.91 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.43641 | +21.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0610078 | +16.20 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| STX-EUR | 0.3257 | +15.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.01551 | +14.09 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOS-EUR | 0.44758 | +12.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 251.445 | +11.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOMI-EUR | 0.19758 | +11.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1867 scans ; 798888 observations ; 1423 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
