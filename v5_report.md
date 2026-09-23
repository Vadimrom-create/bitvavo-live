# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T18:23:38.175569+00:00
État : OK | marchés EUR : 426 | V4 : 409 | données valides : 426
Récupération : 2026-09-23T18:23:00.936696+00:00 | âge ticker : 151.0 s | durée : 151.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- SYN-EUR : 0.183904 € ; score 82.36/100 ; SURVEILLE ; seuil achat non atteint
- LSK-EUR : 0.26855 € ; score 76.80/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD
- PYTH-EUR : 0.054729 € ; score 76.66/100 ; SURVEILLE ; seuil achat non atteint
- BAT-EUR : 0.07741 € ; score 76.44/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0077408 € ; score 76.44/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.045242 | +35.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.032046 | +31.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.018499 | +28.08 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| NIL-EUR | 0.086402 | +20.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.30766 | +15.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.1531 | +14.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.262887 | +13.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.75368 | +12.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LIGHTER-EUR | 4.6552 | +9.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3267 | +9.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1288 scans ; 551425 observations ; 666 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
