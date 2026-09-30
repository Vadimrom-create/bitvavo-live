# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T17:23:36.972620+00:00
État : OK | marchés EUR : 430 | V4 : 393 | données valides : 430
Récupération : 2026-09-30T17:23:00.631016+00:00 | âge ticker : 152.9 s | durée : 153.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- PLUME-EUR : 0.0166058 € ; score 85.57/100 ; SURVEILLE ; seuil achat non atteint
- ZIG-EUR : 0.048789 € ; score 84.77/100 ; SURVEILLE ; seuil achat non atteint
- WOO-EUR : 0.012205 € ; score 82.67/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ICP-EUR : 3.0549 € ; score 82.23/100 ; SURVEILLE ; WICK_SETUP
- COMP-EUR : 22.176 € ; score 81.81/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.4504 | +51.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.34894 | +46.00 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.008194 | +24.36 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 266.603 | +22.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.43607 | +21.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.002151 | +20.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0023705 | +15.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UP-EUR | 0.069678 | +14.30 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.068178 | +14.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.317 | +13.92 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1852 scans ; 792438 observations ; 1410 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
