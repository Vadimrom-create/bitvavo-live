# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T07:24:00.231677+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-22T07:23:28.512442+00:00 | âge ticker : 157.0 s | durée : 157.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AKT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- MANA-EUR : 0.075574 € ; score 91.22/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TURBO-EUR : 0.0009425 € ; score 90.17/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- DYM-EUR : 0.016254 € ; score 90.08/100 ; SURVEILLE ; SPREAD_RISK
- REZ-EUR : 0.0033783 € ; score 88.39/100 ; SURVEILLE ; seuil achat non atteint
- BICO-EUR : 0.019511 € ; score 88.38/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017587 | +108.82 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0015956 | +105.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.119685 | +46.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.056299 | +32.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.5009e-06 | +28.72 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.21954 | +23.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.38965 | +22.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.27768 | +22.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.25317 | +19.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.065718 | +19.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1161 scans ; 497323 observations ; 466 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
