# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T06:03:16.352721+00:00
État : OK | marchés EUR : 430 | V4 : 393 | données valides : 430
Récupération : 2026-10-01T06:02:44.850529+00:00 | âge ticker : 148.0 s | durée : 149.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- AERO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PUMP-EUR : SELLER_HEAVY_BOOK, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : INSUFFICIENT_NET_RISK_REWARD
- XVG-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ETHFI-EUR : 0.68376 € ; score 92.67/100 ; SURVEILLE ; SPREAD_RISK
- LPT-EUR : 1.5653 € ; score 92.60/100 ; SURVEILLE ; seuil achat non atteint
- XVG-EUR : 0.0029414 € ; score 92.09/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- STRK-EUR : 0.038442 € ; score 91.71/100 ; SURVEILLE ; WICK_SETUP
- SOMI-EUR : 0.1949 € ; score 91.66/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.3667 | +84.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.34632 | +44.90 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.009007 | +28.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.35255 | +28.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.029729 | +26.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TRAC-EUR | 0.43959 | +26.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0652543 | +21.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOM-EUR | 0.002197 | +16.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ESP-EUR | 0.098495 | +14.33 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| PLUME-EUR | 0.0179594 | +14.24 % | DETECTED_EARLY | NONE | NONE |

Historique : 1890 scans ; 808778 observations ; 1445 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
