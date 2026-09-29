# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T16:30:39.448697+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 428
Récupération : 2026-09-29T16:30:00.385485+00:00 | âge ticker : 163.2 s | durée : 164.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- SKY-EUR : 0.07602 € ; score 87.93/100 ; SURVEILLE ; WICK_SETUP
- LINK-EUR : 13.1058 € ; score 85.14/100 ; SURVEILLE ; WICK_SETUP
- ARX-EUR : 0.23509 € ; score 83.76/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- ALGO-EUR : 0.115632 € ; score 82.97/100 ; SURVEILLE ; seuil achat non atteint
- JASMY-EUR : 0.0046755 € ; score 81.32/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016772 | +35.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| 0G-EUR | 0.29139 | +30.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.100938 | +26.42 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZBCN-EUR | 0.0022013 | +25.72 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRASS-EUR | 0.6077 | +20.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.35252 | +19.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NMR-EUR | 11.1376 | +15.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AAVE-EUR | 150.52 | +15.18 % | DETECTED_EARLY | NONE | NONE |
| SOON-EUR | 0.34528 | +14.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYRUP-EUR | 0.21502 | +14.12 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1779 scans ; 761101 observations ; 1331 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
