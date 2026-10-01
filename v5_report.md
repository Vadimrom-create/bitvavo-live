# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T05:02:43.181070+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 430
Récupération : 2026-10-01T05:02:10.148190+00:00 | âge ticker : 168.0 s | durée : 168.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ICP-EUR : 2.9846 € ; score 93.04/100 ; SURVEILLE ; seuil achat non atteint
- CRO-EUR : 0.060367 € ; score 89.92/100 ; SURVEILLE ; WIDE_SPREAD_RISK, WICK_SETUP
- SYRUP-EUR : 0.20199 € ; score 89.41/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.22332 € ; score 88.70/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : 0.1812 € ; score 88.17/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.0249 | +72.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.3514 | +47.03 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRAC-EUR | 0.44289 | +29.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008622 | +27.94 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.34583 | +25.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.028612 | +21.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0621743 | +17.43 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PLUME-EUR | 0.0183486 | +16.64 % | DETECTED_EARLY | NONE | NONE |
| RED-EUR | 0.16152 | +14.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAFE-EUR | 0.10782 | +12.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1887 scans ; 807488 observations ; 1440 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
