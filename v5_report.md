# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T06:57:47.541631+00:00
État : OK | marchés EUR : 430 | V4 : 392 | données valides : 430
Récupération : 2026-10-01T06:57:15.684561+00:00 | âge ticker : 154.0 s | durée : 155.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PUMP-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- W-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SEI-EUR : 0.065998 € ; score 88.87/100 ; SURVEILLE ; seuil achat non atteint
- W-EUR : 0.012094 € ; score 88.21/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MERL-EUR : 0.028212 € ; score 87.84/100 ; SURVEILLE ; seuil achat non atteint
- KSM-EUR : 4.6908 € ; score 86.90/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- DOT-EUR : 1.1045 € ; score 86.26/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.6035 | +88.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.3658 | +53.05 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STX-EUR | 0.36464 | +33.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.030132 | +27.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.009249 | +22.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0651045 | +21.43 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TRAC-EUR | 0.42583 | +20.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0022362 | +19.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.48029 | +18.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0179211 | +15.44 % | DETECTED_EARLY | NONE | NONE |

Historique : 1892 scans ; 809638 observations ; 1448 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
