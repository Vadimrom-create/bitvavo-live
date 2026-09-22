# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T01:20:44.866770+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-22T01:20:15.260955+00:00 | âge ticker : 153.0 s | durée : 154.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- KAS-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- PROVE-EUR : 0.20997 € ; score 92.16/100 ; SURVEILLE ; SPREAD_RISK
- THE-EUR : 0.06939 € ; score 90.95/100 ; SURVEILLE ; SPREAD_RISK
- WAL-EUR : 0.029762 € ; score 90.67/100 ; SURVEILLE ; seuil achat non atteint
- ARX-EUR : 0.17798 € ; score 85.67/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- MON-EUR : 0.021955 € ; score 85.33/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.016587 | +95.58 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014782 | +88.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.055738 | +51.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.05102 | +48.09 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.11127 | +38.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.31138 | +36.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043435 | +31.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.026749 | +22.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008068 | +22.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.3393e-06 | +22.24 % | DETECTED_EARLY | NONE | NONE |

Historique : 1137 scans ; 487099 observations ; 435 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
