# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T06:37:23.959945+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T06:36:53.244136+00:00 | âge ticker : 150.5 s | durée : 151.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- THE-EUR : 0.07297 € ; score 87.65/100 ; SURVEILLE ; WICK_SETUP
- PYTH-EUR : 0.055052 € ; score 81.93/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 82.239 € ; score 81.73/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MERL-EUR : 0.025296 € ; score 81.40/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- DYM-EUR : 0.016106 € ; score 81.35/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.016712 | +98.39 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0015388 | +98.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.122109 | +52.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.437e-06 | +26.47 % | DETECTED_EARLY | NONE | NONE |
| KERNEL-EUR | 0.055293 | +25.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WIF-EUR | 0.21613 | +22.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.385 | +21.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.037451 | +21.26 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FORM-EUR | 0.27318 | +20.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TAO-EUR | 281.32 | +19.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1157 scans ; 495619 observations ; 463 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
