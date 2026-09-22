# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T12:31:37.345638+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T12:31:10.896583+00:00 | âge ticker : 149.8 s | durée : 150.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZORA-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- IMX-EUR : 0.13133 € ; score 89.15/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SUSHI-EUR : 0.21686 € ; score 88.63/100 ; SURVEILLE ; seuil achat non atteint
- LDO-EUR : 0.36124 € ; score 87.60/100 ; SURVEILLE ; WICK_SETUP
- EIGEN-EUR : 0.20617 € ; score 87.41/100 ; SURVEILLE ; WICK_SETUP
- BAT-EUR : 0.07309 € ; score 86.71/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017401 | +97.83 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014102 | +78.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XMN-EUR | 0.00057 | +36.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.054044 | +29.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.07124 | +24.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.11662 | +22.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.28421 | +21.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.23059 | +19.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.3811 | +17.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.2894e-06 | +16.57 % | DETECTED_EARLY | NONE | NONE |

Historique : 1183 scans ; 506695 observations ; 491 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
