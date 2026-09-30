# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T23:15:38.625590+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-09-30T23:15:05.685026+00:00 | âge ticker : 155.0 s | durée : 156.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PLUME-EUR : INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BONK-EUR : 3.37e-06 € ; score 91.56/100 ; SURVEILLE ; seuil achat non atteint
- PLUME-EUR : 0.0167137 € ; score 88.98/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : 0.34736 € ; score 88.12/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : 0.40658 € ; score 88.08/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.21838 € ; score 86.94/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.9626 | +82.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35608 | +48.99 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.00863 | +25.78 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.43472 | +20.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.32801 | +16.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0603451 | +13.73 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| MON-EUR | 0.027005 | +13.21 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOMI-EUR | 0.20005 | +12.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| REZ-EUR | 0.0041721 | +10.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TRAC-EUR | 0.37151 | +10.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1870 scans ; 800178 observations ; 1425 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
