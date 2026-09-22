# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T11:59:38.632796+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T11:59:07.152110+00:00 | âge ticker : 157.5 s | durée : 158.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- RAY-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- W-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- IOST-EUR : 0.0007781 € ; score 89.44/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- RSR-EUR : 0.0014303 € ; score 88.03/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- CAT-EUR : 2.0194e-06 € ; score 86.70/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- MON-EUR : 0.022161 € ; score 85.43/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TNSR-EUR : 0.032571 € ; score 84.78/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017814 | +102.66 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014258 | +81.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.118818 | +35.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.056229 | +32.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.068223 | +23.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BTT-EUR | 3.6755e-07 | +23.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FORM-EUR | 0.2836 | +21.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.22271 | +18.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.2965e-06 | +16.77 % | DETECTED_EARLY | NONE | NONE |
| GRASS-EUR | 0.37844 | +16.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1180 scans ; 505417 observations ; 482 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
