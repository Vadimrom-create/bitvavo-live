# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T23:34:13.088156+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-09-30T23:33:11.918251+00:00 | âge ticker : 187.2 s | durée : 188.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CRV-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PLUME-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- APT-EUR : 0.6825 € ; score 87.65/100 ; SURVEILLE ; seuil achat non atteint
- ZIG-EUR : 0.049265 € ; score 86.82/100 ; SURVEILLE ; seuil achat non atteint
- KSM-EUR : 4.5766 € ; score 85.40/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- BONK-EUR : 3.3611e-06 € ; score 85.19/100 ; SURVEILLE ; seuil achat non atteint
- XLM-EUR : 0.20103 € ; score 84.71/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.8962 | +75.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35425 | +48.22 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.008448 | +22.86 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.43628 | +19.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.32776 | +17.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.027332 | +14.88 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CAP-EUR | 0.0599462 | +13.12 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOMI-EUR | 0.19824 | +12.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| REZ-EUR | 0.0041712 | +10.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RED-EUR | 0.15612 | +10.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1871 scans ; 800608 observations ; 1425 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
