# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T04:55:42.219868+00:00
État : OK | marchés EUR : 426 | V4 : 373 | données valides : 426
Récupération : 2026-09-21T04:55:14.578510+00:00 | âge ticker : 153.4 s | durée : 154.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- AIOZ-EUR : 0.079387 € ; score 92.72/100 ; SURVEILLE ; seuil achat non atteint
- DYM-EUR : 0.015382 € ; score 89.58/100 ; SURVEILLE ; WICK_SETUP
- VET-EUR : 0.0073191 € ; score 89.48/100 ; SURVEILLE ; WICK_SETUP
- ENS-EUR : 5.683 € ; score 89.43/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- COTI-EUR : 0.015629 € ; score 89.17/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.059017 | +75.24 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0010431 | +68.87 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.25493 | +39.70 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.030728 | +27.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NEAR-EUR | 3.8386 | +26.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.055109 | +25.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VVV-EUR | 28.4888 | +22.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.029013 | +20.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.050361 | +20.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 10.013 | +19.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1048 scans ; 449185 observations ; 323 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
