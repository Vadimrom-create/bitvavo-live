# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T07:11:40.610665+00:00
État : OK | marchés EUR : 426 | V4 : 378 | données valides : 426
Récupération : 2026-09-21T07:11:10.492696+00:00 | âge ticker : 146.1 s | durée : 148.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AIOZ-EUR : INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : SPREAD_RISK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ONDO-EUR : 0.37681 € ; score 93.14/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : 0.20008 € ; score 88.43/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SKY-EUR : 0.062175 € ; score 88.35/100 ; SURVEILLE ; seuil achat non atteint
- SUPER-EUR : 0.12314 € ; score 87.74/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MEGA-EUR : 0.03795 € ; score 87.37/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.054465 | +63.40 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0009181 | +49.63 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.26063 | +42.42 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.058628 | +34.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.031605 | +30.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.52992 | +28.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NEAR-EUR | 3.751 | +24.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.029221 | +23.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VVV-EUR | 29.3914 | +22.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.049355 | +18.61 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1055 scans ; 452167 observations ; 328 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
