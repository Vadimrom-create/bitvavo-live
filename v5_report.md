# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T16:17:32.674036+00:00
État : OK | marchés EUR : 426 | V4 : 408 | données valides : 426
Récupération : 2026-09-23T16:16:59.455786+00:00 | âge ticker : 145.7 s | durée : 146.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- API3-EUR : 0.23153 € ; score 91.70/100 ; SURVEILLE ; SPREAD_RISK
- FLOCK-EUR : 0.066896 € ; score 88.88/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- NEWT-EUR : 0.043567 € ; score 87.55/100 ; SURVEILLE ; seuil achat non atteint
- FLUID-EUR : 1.1885 € ; score 86.75/100 ; SURVEILLE ; LOW_LIQUIDITY, STABILITY_HOLD
- MANA-EUR : 0.073549 € ; score 85.77/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.032795 | +36.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.043448 | +33.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.31491 | +22.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PROM-EUR | 4.5244 | +18.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DBR-EUR | 0.017066 | +18.33 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| RAY-EUR | 1.78484 | +16.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3058 | +16.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.15516 | +15.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.26309 | +15.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.083147 | +14.49 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1281 scans ; 548443 observations ; 659 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
