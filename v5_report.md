# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T11:36:44.771868+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-23T11:36:12.883359+00:00 | âge ticker : 156.5 s | durée : 157.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- MEGA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- BICO-EUR : 0.01986 € ; score 84.25/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- SAFE-EUR : 0.097379 € ; score 84.04/100 ; SURVEILLE ; LOW_LIQUIDITY
- ARX-EUR : 0.18717 € ; score 83.24/100 ; SURVEILLE ; SPREAD_RISK
- REZ-EUR : 0.0035164 € ; score 82.83/100 ; SURVEILLE ; seuil achat non atteint
- ICP-EUR : 2.725 € ; score 82.61/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.033518 | +39.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.3515 | +38.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 305.94 | +30.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.288935 | +27.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2933 | +25.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.085 | +25.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.01895 | +24.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SUPER-EUR | 0.1586 | +20.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.040355 | +20.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.01967 | +19.59 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1266 scans ; 542053 observations ; 642 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
