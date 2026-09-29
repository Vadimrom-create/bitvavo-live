# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T10:26:21.785769+00:00
État : OK | marchés EUR : 428 | V4 : 395 | données valides : 428
Récupération : 2026-09-29T10:25:13.974046+00:00 | âge ticker : 185.7 s | durée : 186.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DIA-EUR : 0.14413 € ; score 91.82/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- IMX-EUR : 0.15238 € ; score 90.80/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AZTEC-EUR : 0.016875 € ; score 86.40/100 ; SURVEILLE ; seuil achat non atteint
- XDC-EUR : 0.031758 € ; score 85.81/100 ; SURVEILLE ; seuil achat non atteint
- PENDLE-EUR : 2.125 € ; score 85.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.00204 | +66.73 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NMR-EUR | 11.5359 | +28.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.60561 | +21.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.34961 | +20.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYRUP-EUR | 0.21693 | +19.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.2624 | +18.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CVX-EUR | 2.0708 | +17.81 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AMP-EUR | 0.0006248 | +17.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.087583 | +16.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZBCN-EUR | 0.0020394 | +15.26 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1762 scans ; 753809 observations ; 1296 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
