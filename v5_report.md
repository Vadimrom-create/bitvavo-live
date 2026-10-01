# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T06:32:56.513470+00:00
État : OK | marchés EUR : 430 | V4 : 391 | données valides : 430
Récupération : 2026-10-01T06:32:23.331106+00:00 | âge ticker : 154.2 s | durée : 155.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- AERO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XVG-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- STRK-EUR : 0.039023 € ; score 89.37/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- ASTER-EUR : 0.67706 € ; score 87.85/100 ; SURVEILLE ; WICK_SETUP
- RAY-EUR : 1.73978 € ; score 86.45/100 ; SURVEILLE ; seuil achat non atteint
- XVG-EUR : 0.0029517 € ; score 85.19/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ASTR-EUR : 0.0066377 € ; score 83.96/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.3592 | +74.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.36794 | +53.95 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STX-EUR | 0.3523 | +28.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.43989 | +27.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.029783 | +27.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.009054 | +23.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0022782 | +19.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0636239 | +18.69 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOS-EUR | 0.47058 | +16.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0181898 | +16.32 % | DETECTED_EARLY | NONE | NONE |

Historique : 1891 scans ; 809208 observations ; 1445 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
