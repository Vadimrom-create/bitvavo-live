# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T10:47:44.118081+00:00
État : OK | marchés EUR : 426 | V4 : 383 | données valides : 426
Récupération : 2026-09-21T10:47:12.191004+00:00 | âge ticker : 156.2 s | durée : 157.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ALGO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- IOST-EUR : 0.0007741 € ; score 89.38/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- XTZ-EUR : 0.30515 € ; score 88.67/100 ; SURVEILLE ; seuil achat non atteint
- KSM-EUR : 4.0398 € ; score 86.79/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SSV-EUR : 2.8016 € ; score 85.08/100 ; SURVEILLE ; seuil achat non atteint
- MERL-EUR : 0.023768 € ; score 84.50/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.053568 | +72.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.056058 | +70.84 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0009533 | +50.98 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.057446 | +33.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.030457 | +30.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.2372 | +29.62 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SEI-EUR | 0.053101 | +28.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.031358 | +23.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.043998 | +22.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 0.8678 | +22.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1069 scans ; 458131 observations ; 349 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
