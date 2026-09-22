# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T16:55:44.292292+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-22T16:55:17.477656+00:00 | âge ticker : 143.3 s | durée : 144.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- GALA-EUR : 0.0018662 € ; score 88.57/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WLD-EUR : 0.39611 € ; score 87.38/100 ; SURVEILLE ; seuil achat non atteint
- PLUME-EUR : 0.0132248 € ; score 87.36/100 ; SURVEILLE ; seuil achat non atteint
- ORCA-EUR : 1.30067 € ; score 86.25/100 ; SURVEILLE ; WICK_SETUP
- AI-EUR : 0.018386 € ; score 86.22/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CHR-EUR | 0.020718 | +36.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MLN-EUR | 1.6092 | +32.12 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.071995 | +27.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.079669 | +25.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 285.66 | +24.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.050575 | +22.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.381 | +18.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2041 | +17.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12076 | +16.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.4574 | +14.92 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1199 scans ; 513511 observations ; 518 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
